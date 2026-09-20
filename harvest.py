# -*- coding: utf-8 -*-
"""
harvest.py — L0 采集层：9 方向全量抓取（海洋AI研究日报专用）

产出：data/pool/YYYY-MM-DD.jsonl  每行一条文献记录（含元数据，不含中文摘要）
数据源：OpenAlex（主，覆盖 Elsevier/Wiley/Springer/IEEE/MDPI 等全部期刊）、arXiv（预印本）
特点：T+1 可达；去重（DOI / arXiv ID / 标题指纹）；礼貌池 mailto；断点续跑（已抓方向跳过）

用法：
  py -3 harvest.py                       # 默认窗口 = 最近 14 天
  py -3 harvest.py --days 7
  py -3 harvest.py --date 2026-09-20 --days 14
  py -3 harvest.py --dirs 1,2,9          # 只抓指定方向
  py -3 harvest.py --resume              # 跳过已抓过的方向（断点续跑）
"""
import json
import re
import ssl
import sys
import time
import argparse
import datetime
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
POOL = ROOT / "data" / "pool"
MAILTO = "sutiany@163.com"
UA = f"OceanAIDailyReport/1.0 (mailto:{MAILTO})"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

DIRECTIONS = {
    1: {"name": "海洋人工智能", "oa": '("machine learning" OR "deep learning" OR "neural network" OR "artificial intelligence")',
        "ar": 'all:"machine learning" OR all:"deep learning"'},
    2: {"name": "海洋数字孪生", "oa": '("digital twin" OR "data assimilation" OR "reanalysis" OR "numerical model")',
        "ar": 'all:"digital twin" OR all:"data assimilation"'},
    3: {"name": "海洋可视化", "oa": '("visualization" OR "web mapping" OR "dashboard" OR "interactive map" OR "GIS")',
        "ar": 'all:"visualization" OR all:"GIS"'},
    4: {"name": "海洋数据质量", "oa": '("quality control" OR "quality assurance" OR "anomaly detection" OR "flagging")',
        "ar": 'all:"quality control" OR all:"anomaly detection"'},
    5: {"name": "海洋数据处理", "oa": '("reprocessing" OR "data fusion" OR "interpolation" OR "regridding" OR "gap filling")',
        "ar": 'all:"data fusion" OR all:"gap filling"'},
    6: {"name": "数据管理与共享", "oa": '("FAIR" OR "metadata" OR "data sharing" OR "open data" OR "data policy")',
        "ar": 'all:"data sharing" OR all:"metadata"'},
    7: {"name": "开放航次与科考", "oa": '("cruise" OR "expedition" OR "research vessel" OR "glider" OR "AUV" OR "ROV")',
        "ar": 'all:"autonomous underwater vehicle" OR all:"glider"'},
    8: {"name": "海洋数据中心", "oa": '("data center" OR "archive" OR "repository" OR "database" OR "data portal")',
        "ar": 'all:"database" OR all:"archive"'},
    9: {"name": "工具与代码资源", "oa": '("open-source" OR "software package" OR "toolbox" OR "python package")',
        "ar": 'all:"open source" OR all:"toolbox"'},
}
OCEAN_TERMS = "(ocean OR marine OR sea OR seawater OR seafloor OR sea-ice OR bathymetry OR plankton OR coral OR coastal OR estuarine OR underwater)"

SELECT = ("id,doi,title,publication_date,type,primary_location,authorships,"
          "abstract_inverted_index,cited_by_count,open_access,language")


def _get(url, timeout=40, retries=3, backoff=2.0):
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            last = e
            if i < retries:
                time.sleep(backoff * (i + 1))
    raise last


def _get_text(url, timeout=40, retries=3):
    """arXiv 限流严格（429），退避需更长。"""
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            if i < retries:
                time.sleep(10 * (i + 1))
    raise last


def _abstract(inv):
    """OpenAlex abstract_inverted_index -> 文本（截断 600 字）。"""
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    txt = " ".join(pos[i] for i in sorted(pos))
    return txt[:600]


def fetch_openalex(d, start, end, want_conf=False, max_pages=4):
    """返回该方向的 OpenAlex 记录列表。"""
    terms = d["oa"]
    expr = f"{terms} AND {OCEAN_TERMS}"
    filters = [f"from_publication_date:{start}", f"to_publication_date:{end}"]
    if want_conf:
        filters.append("type:proceedings-article")
    else:
        filters += ["type:article", "primary_location.source.type:journal"]
    out, cursor = [], "*"
    for _ in range(max_pages):
        url = ("https://api.openalex.org/works?filter=" + ",".join(filters)
               + "&search=" + urllib.parse.quote(expr)
               + f"&per-page=200&cursor={urllib.parse.quote(cursor)}"
               + f"&select={SELECT}&mailto={MAILTO}")
        data = _get(url)
        res = data.get("results", [])
        out.extend(res)
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor or len(res) < 200:
            break
        time.sleep(1.0)
    return out


def norm_rec(w, direction_id, direction_name):
    src = (w.get("primary_location") or {}).get("source") or {}
    doi = (w.get("doi") or "").replace("https://doi.org/", "")
    host = src.get("host_organization_name") or ""
    insts = []
    for a in (w.get("authorships") or [])[:40]:
        for i in (a.get("institutions") or []):
            nm = i.get("display_name")
            if nm and nm not in insts:
                insts.append(nm)
    return {
        "id": w.get("id"),
        "source": "openalex",
        "doi": doi,
        "title": (w.get("title") or "").strip(),
        "abstract": _abstract(w.get("abstract_inverted_index")),
        "date": w.get("publication_date") or "",
        "type": w.get("type") or "",
        "journal": src.get("display_name") or "",
        "publisher": src.get("host_organization_name") or host or "",
        "source_id": src.get("id") or "",
        "issn": (src.get("issn_l") or ""),
        "url": wide_url(w, doi),
        "institutions": insts[:4],
        "cited_by": w.get("cited_by_count") or 0,
        "oa": (w.get("open_access") or {}).get("oa_status") or "",
        "lang": w.get("language") or "",
        "direction_id": direction_id,
        "direction": direction_name,
        "is_preprint": False,
    }


def wide_url(w, doi):
    loc = w.get("primary_location") or {}
    if loc.get("landing_page_url"):
        return loc["landing_page_url"]
    for l in (w.get("locations") or []):
        if l.get("landing_page_url"):
            return l["landing_page_url"]
    return f"https://doi.org/{doi}" if doi else (w.get("id") or "")


ARXIV_NS = {"a": "http://www.w3.org/2005/Atom"}


def fetch_arxiv(d, start, end, max_results=150):
    cats = "(cat:physics.ao-ph OR cat:cs.CV OR cat:cs.LG OR cat:cs.RO OR cat:eess.SP)"
    q = f"{cats} AND ({d['ar']}) AND (all:ocean OR all:marine OR all:underwater OR all:sea)"
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q)
           + f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}")
    xml = _get_text(url)
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", ARXIV_NS):
        pid = (e.findtext("a:id", "", ARXIV_NS) or "").strip()
        aid = pid.rsplit("/", 1)[-1]
        base = aid.split("v")[0]
        pub = (e.findtext("a:published", "", ARXIV_NS) or "")[:10]
        upd = (e.findtext("a:updated", "", ARXIV_NS) or "")[:10]
        if not (start <= pub <= end):
            continue
        out.append({
            "id": f"https://arxiv.org/abs/{base}", "source": "arxiv",
            "doi": (e.findtext("a:doi", "", ARXIV_NS) or "").replace("https://doi.org/", ""),
            "arxiv_id": base, "title": " ".join((e.findtext("a:title", "", ARXIV_NS) or "").split()),
            "abstract": " ".join((e.findtext("a:summary", "", ARXIV_NS) or "").split())[:600],
            "date": pub, "updated": upd, "type": "preprint", "journal": "arXiv",
            "publisher": "arXiv", "issn": "", "url": pid,
            "institutions": [], "cited_by": 0, "oa": "green", "lang": "en",
            "direction_id": d["id"], "direction": d["name"], "is_preprint": True,
        })
    return out


def fingerprint(t):
    return re.sub(r"[^a-z0-9]+", "", (t or "").lower())[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--dirs", default="")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--skip-arxiv", action="store_true")
    a = ap.parse_args()

    day = datetime.date.fromisoformat(a.date)
    start = (day - datetime.timedelta(days=a.days)).isoformat()
    end = day.isoformat()
    POOL.mkdir(parents=True, exist_ok=True)
    outfile = POOL / f"{a.date}.jsonl"

    done_dirs = set()
    if a.resume and outfile.exists():
        for line in outfile.read_text(encoding="utf-8").splitlines():
            try:
                done_dirs.add(json.loads(line)["direction_id"])
            except Exception:
                pass

    ids = [int(x) for x in a.dirs.split(",") if x.strip()] or sorted(DIRECTIONS)
    seen, rows = set(), []
    for did in ids:
        d = dict(DIRECTIONS[did], id=did)
        if did in done_dirs:
            print(f"[跳过] 方向{did} {d['name']}（断点续跑）")
            continue
        cnt = 0
        try:
            recs = fetch_openalex(d, start, end)
        except Exception as e:
            print(f"!! 方向{did} OpenAlex 失败：{e}")
            recs = []
        for w in recs:
            r = norm_rec(w, did, d["name"])
            fp = fingerprint(r["title"])
            key = r["doi"] or r["id"] or fp
            if key in seen or fp in seen:
                continue
            seen.update([key, fp])
            rows.append(r)
            cnt += 1
        time.sleep(0.5)
        if did == 1 and not a.skip_arxiv:
            try:
                for r in fetch_arxiv(d, start, end):
                    fp = fingerprint(r["title"])
                    if r["arxiv_id"] in seen or fp in seen:
                        continue
                    seen.update([r["arxiv_id"], fp])
                    rows.append(r)
                    cnt += 1
            except Exception as e:
                print(f"!! 方向{did} arXiv 失败：{e}")
            time.sleep(3)
        conf = 0
        if did == 1:
            try:
                for w in fetch_openalex(d, start, end, want_conf=True, max_pages=2):
                    r = norm_rec(w, did, d["name"])
                    fp = fingerprint(r["title"])
                    key = r["doi"] or r["id"]
                    if key in seen or fp in seen:
                        continue
                    seen.update([key, fp])
                    rows.append(r)
                    conf += 1
            except Exception as e:
                print(f"!! 方向{did} 会议论文失败：{e}")
        print(f"[完成] 方向{did} {d['name']}: {cnt} 条（其中会议论文 {conf}）")

    mode = "a" if a.resume else "w"
    with outfile.open(mode, encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    total = sum(1 for _ in outfile.open(encoding="utf-8"))
    print(f"\n窗口 {start} ~ {end} · 本次新增 {len(rows)} 条 · 池文件累计 {total} 行 → {outfile}")


if __name__ == "__main__":
    main()
