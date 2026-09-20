# -*- coding: utf-8 -*-
"""
screen.py — L1 文献池：去重 + 期刊分级 + 相关度打分（海洋AI研究日报专用）

输入：data/pool/YYYY-MM-DD.jsonl（harvest.py 产出）
输出：data/library.db（SQLite 全量池，累积）
      data/pool_index.json（前沿看板数据源，体积受控）
      data/pending_journals.txt（待确认期刊清单，问答式校准用）

打分口径：期刊等级权重（S 6 / A 5 / B 4 / C 3 / P 2.5 / D 1 / ? 0）× 100
          + 相关度（方向关键词命中）× 8
          + 时效（≤14 天，越新越高，近 7 天加权）
          + 被引（log 缩放，新刊多为 0）
预警刊（D）强制置底并保留标注，不删除——供人工取舍。

用法：
  py -3 screen.py                       # 处理最新池文件
  py -3 screen.py --date 2026-09-20
  py -3 screen.py --top 60 --board-cap 1500
"""
import json
import math
import re
import sqlite3
import argparse
import datetime
from pathlib import Path
from collections import defaultdict

import tier_engine

ROOT = Path(__file__).resolve().parent
POOL = ROOT / "data" / "pool"
DB = ROOT / "data" / "library.db"
INDEX = ROOT / "data" / "pool_index.json"
PENDING_TXT = ROOT / "data" / "pending_journals.txt"

REL_TERMS = {
    1: ["machine learning", "deep learning", "neural network", "artificial intelligence",
        "transformer", "cnn", "lstm", "diffusion model", "foundation model", "llm",
        "computer vision", "convolutional", "random forest", "xgboost", "reinforcement learning"],
    2: ["digital twin", "data assimilation", "reanalysis", "forecast model", "coupled model",
        "regional model", "hindcast", "operational forecast", "simulation framework"],
    3: ["visualization", "visualisation", "web map", "dashboard", "interactive", "gis",
        "three-dimensional", "virtual reality", "rendering", "map service"],
    4: ["quality control", "quality assurance", "qc", "anomaly detection", "outlier",
        "flag", "error", "uncertainty quantification", "validation", "calibration",
        "data integrity", "intercomparison"],
    5: ["reprocess", "data fusion", "interpolation", "regridding", "gap filling",
        "reconstruction", "downscaling", "blending", "merging", "bias correction"],
    6: ["fair", "metadata", "data sharing", "open data", "data policy", "data management",
        "interoperability", "standard", "data infrastructure", "open science", "doi"],
    7: ["cruise", "expedition", "research vessel", "glider", "auv", "rov", "float",
        "mooring", "survey", "shipboard", "sea ice camp", "drone"],
    8: ["data center", "data centre", "archive", "repository", "database", "data portal",
        "ncEI", "pangaea", "copernicus", "data service", "catalogue", "catalog"],
    9: ["open-source", "open source", "software package", "toolbox", "python", "library",
        "framework release", "codebase", "api", "docker", "workflow", "notebook"],
}
DIR_NAMES = dict(tier_engine.load_registry() and {})  # placeholder, filled below

DIR_TITLE = {
    1: "一、海洋人工智能", 2: "二、海洋数字孪生", 3: "三、海洋可视化", 4: "四、海洋数据质量",
    5: "五、海洋数据处理", 6: "六、数据管理与共享", 7: "七、开放航次与科考",
    8: "八、海洋数据中心", 9: "九、工具与代码资源",
}

OCEAN_WORDS = ["ocean", "marine", "sea", "seawater", "seafloor", "sea-ice", "sea ice",
               "bathymetry", "plankton", "coral", "coastal", "estuar", "underwater",
               "oceanograph", "arctic", "antarctic", "polar", "wave", "tide", "tidal"]


def history_ids():
    """从 posts/ 全量存档提取历史 DOI / arXiv ID 集合（规则 4c）。"""
    dois, arx = set(), set()
    for f in sorted((ROOT / "posts").glob("*.html")):
        src = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"doi\.org/(10\.[^\s\"'<>]+)", src):
            dois.add(m.group(1).rstrip(".。，,").lower())
        for m in re.finditer(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", src):
            arx.add(m.group(1))
        for m in re.finditer(r"(\d{4}\.\d{4,5})", src):
            arx.add(m.group(1))
    return dois, arx


def score(rec, tier, rel, days_ago):
    tw = tier_engine.load_registry()["policy"]["weights"].get(tier, 0)
    s = tw * 100 + rel * 8
    if 0 <= days_ago <= 14:
        s += (14 - days_ago) * 2
        if days_ago <= 7:
            s += 12          # 近 7 天排序优先权
    s += min(12, math.log1p(rec.get("cited_by") or 0) * 4)
    if tier == "D":
        s = min(s, 60)       # 预警/受限刊强制置底，但保留可见
    return round(s, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="")
    ap.add_argument("--top", type=int, default=200, help="每方向保留条数（看板用）")
    ap.add_argument("--board-cap", type=int, default=1500, help="看板总条数上限")
    a = ap.parse_args()

    files = sorted(POOL.glob("*.jsonl"))
    if not files:
        print("没有池文件，请先运行 harvest.py")
        return
    pool = POOL / (f"{a.date}.jsonl") if a.date else files[-1]
    date = pool.stem
    day = datetime.date.fromisoformat(date)

    hist_doi, hist_arx = history_ids()
    seen_doi, seen_fp = set(), set()
    rows, unknown = [], defaultdict(lambda: {"n": 0, "pub": set()})

    for line in pool.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except Exception:
            continue
        title = r.get("title") or ""
        if not title:
            continue
        fp = re.sub(r"[^a-z0-9]+", "", title.lower())[:80]
        doi = (r.get("doi") or "").lower()
        if fp in seen_fp or (doi and doi in seen_doi):
            continue
        seen_fp.add(fp)
        if doi:
            seen_doi.add(doi)

        is_pre = bool(r.get("is_preprint"))
        pub = r.get("publisher") or ""
        if not pub or pub.startswith("http"):
            m = tier_engine.load_metrics().get(r.get("issn") or "")
            if m:
                pub = m.get("publisher") or ""
                r["publisher"] = pub
        ti = tier_engine.classify(r.get("journal"), pub,
                                  is_preprint=is_pre, issn=r.get("issn"))
        tier = ti["tier"]
        if tier == "?":
            key = r.get("journal") or "(未知刊)"
            unknown[key]["n"] += 1
            unknown[key]["pub"].add(pub or "")
            tier_engine.add_pending(r.get("journal"), pub,
                                    DIR_TITLE.get(r.get("direction_id"), ""), 1, title[:120])

        blob = (title + " " + (r.get("abstract") or "")).lower()
        if not any(w in blob for w in OCEAN_WORDS):
            continue
        title_l = title.lower()
        ocean_in_title = any(w in title_l for w in OCEAN_WORDS)
        rel, hit_dir, hit_n = 0, r.get("direction_id"), 0
        for did, terms in REL_TERMS.items():
            n = sum(1 for t in terms if t in blob)
            if n > hit_n:
                rel, hit_dir, hit_n = n, did, n
        if hit_n == 0:
            continue
        t_hits = sum(1 for t in REL_TERMS.get(hit_dir, []) if t in title_l)
        if t_hits == 0 and hit_n < 2:
            continue
        # 收紧：标题不含海洋词时，要求相关度更高（避免"橄榄叶面积预测"类混入）
        if not ocean_in_title and hit_n < 3:
            continue

        wd = abs((day - datetime.date.fromisoformat(r["date"])).days) if r.get("date") else 99
        is_new = not (doi in hist_doi or (r.get("arxiv_id") and r["arxiv_id"] in hist_arx))
        s = score(r, tier, hit_n, wd)
        s += 10 if ocean_in_title else -20   # 标题不含海洋词：降权（保留可见，不删除）
        r.update({
            "tier": tier, "tier_label": ti["label"], "flags": ti["flags"], "tier_note": ti["note"],
            "direction_id": hit_dir, "direction": DIR_TITLE.get(hit_dir, ""),
            "rel": hit_n, "score": round(s, 2), "days_ago": wd, "ocean_in_title": ocean_in_title,
            "is_new": is_new, "fp": fp,
        })
        rows.append(r)

    rows.sort(key=lambda x: -x["score"])

    # SQLite 全量池
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS works(
        date TEXT, fp TEXT, title TEXT, journal TEXT, publisher TEXT, tier TEXT,
        direction TEXT, doi TEXT, url TEXT, pub_date TEXT, score REAL, rel INTEGER,
        cited_by INTEGER, is_preprint INTEGER, flags TEXT, is_new INTEGER,
        PRIMARY KEY(date, fp))""")
    con.execute(f"DELETE FROM works WHERE date='{date}'")
    con.executemany("""INSERT OR REPLACE INTO works VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", [
        (date, r["fp"], r["title"][:300], r.get("journal", ""), r.get("publisher", ""), r["tier"],
         r["direction"], r.get("doi", ""), r.get("url", ""), r.get("date", ""), r["score"],
         r["rel"], r.get("cited_by") or 0, 1 if r.get("is_preprint") else 0,
         "；".join(r["flags"]), 1 if r["is_new"] else 0) for r in rows])
    con.commit()

    # 看板数据：每方向 top N + 总量上限
    per_dir = defaultdict(int)
    board = []
    for r in rows:
        did = r["direction_id"]
        if per_dir[did] >= a.top:
            continue
        per_dir[did] += 1
        if len(board) >= a.board_cap:
            break
        board.append({
            "t": r["title"][:220], "j": r.get("journal", "") or ("arXiv 预印本" if r.get("is_preprint") else "—"),
            "p": r.get("publisher", ""), "tier": r["tier"], "dir": did, "d": r.get("date", ""),
            "doi": r.get("doi", ""), "url": r.get("url", ""), "score": r["score"],
            "rel": r["rel"], "cited": r.get("cited_by") or 0, "oa": r.get("oa", ""),
            "flags": r["flags"], "new": r["is_new"],
            "inst": "、".join((r.get("institutions") or [])[:2]),
        })
    INDEX.write_text(json.dumps({
        "generated": date, "window_days": 14, "total_pool": len(rows),
        "board_count": len(board), "countries_note": "分级口径见 data/journal_tiers.json",
        "items": board,
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    # 待确认期刊清单（问答式校准）
    if unknown:
        lines = [f"# 待确认期刊（{date}，按命中篇数降序）", ""]
        for k, v in sorted(unknown.items(), key=lambda x: -x[1]["n"]):
            pubs = "、".join(sorted(x for x in v["pub"] if x))
            lines.append(f"[{v['n']:>3} 篇] {k}" + (f" · {pubs}" if pubs else ""))
        PENDING_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    tier_cnt = defaultdict(int)
    for r in rows:
        tier_cnt[r["tier"]] += 1
    print(f"池文件 {pool.name} · 原始 {sum(1 for _ in pool.open(encoding='utf-8'))} 条"
          f" → 池内 {len(rows)} 条（看板 {len(board)} 条）")
    print("分级分布：", dict(sorted(tier_cnt.items())))
    print("方向分布：", {DIR_TITLE[k]: v for k, v in sorted(per_dir.items())})
    print(f"待确认期刊 {len(unknown)} 本 → {PENDING_TXT if unknown else '（无）'}")
    con.close()


if __name__ == "__main__":
    main()
