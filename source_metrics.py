# -*- coding: utf-8 -*-
"""
source_metrics.py — 期刊指标缓存（分级自动评级的数据底座）

做法：按 ISSN 逐个查询 OpenAlex Sources API，缓存 display_name / 出版方 /
      h_index / 两年均被引 / 是否 DOAJ 开放获取 / 年发文量，
      用于 tier_engine 在"人工登记表未覆盖"时自动评级（标记 auto=true，待苏老师校准）。

用法：
  py -3 source_metrics.py                # 补齐池内所有未缓存 ISSN
  py -3 source_metrics.py --limit 200    # 只补前 200 个（分批跑）
  py -3 source_metrics.py --stats
"""
import json
import ssl
import time
import argparse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POOL = ROOT / "data" / "pool"
CACHE = ROOT / "data" / "source_metrics.json"
MAILTO = "sutiany@163.com"
UA = f"OceanAIDailyReport/1.0 (mailto:{MAILTO})"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def load_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(c):
    CACHE.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")


def fetch_issn(issn):
    url = f"https://api.openalex.org/sources/issn:{issn}?mailto={MAILTO}"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for i in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
                d = json.loads(r.read().decode("utf-8", "replace"))
            ss = d.get("summary_stats") or {}
            return {
                "name": d.get("display_name") or "",
                "publisher": d.get("host_organization_name") or "",
                "h_index": ss.get("h_index") or 0,
                "citedness": round(ss.get("2yr_mean_citedness") or 0, 3),
                "i10": ss.get("i10_index") or 0,
                "works": d.get("works_count") or 0,
                "is_oa": bool(d.get("is_oa")),
                "in_doaj": bool(d.get("is_in_doaj")),
                "type": d.get("type") or "",
            }
        except Exception:
            if i == 0:
                time.sleep(3)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=400)
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()

    cache = load_cache()
    if a.stats:
        tiers = {}
        for v in cache.values():
            tiers[v.get("publisher", "")] = tiers.get(v.get("publisher", ""), 0) + 1
        print("已缓存期刊：", len(cache))
        return

    issns = set()
    for f in POOL.glob("*.jsonl"):
        for line in f.read_text(encoding="utf-8").splitlines():
            try:
                i = json.loads(line).get("issn")
            except Exception:
                continue
            if i:
                issns.add(i)
    todo = sorted(x for x in issns if x not in cache)[: a.limit]
    print(f"池内期刊 ISSN {len(issns)} 个 · 未缓存 {len(issns) - len(cache)} 个 · 本次补 {len(todo)} 个")
    ok = 0
    for i, issn in enumerate(todo, 1):
        m = fetch_issn(issn)
        cache[issn] = m if m else {"name": "", "publisher": "", "h_index": 0,
                                   "citedness": 0, "i10": 0, "works": 0,
                                   "is_oa": False, "in_doaj": False, "type": "", "miss": True}
        if m:
            ok += 1
        if i % 25 == 0:
            save_cache(cache)
            print(f"  ... {i}/{len(todo)}")
        time.sleep(0.35)
    save_cache(cache)
    print(f"完成：命中 {ok}/{len(todo)} · 缓存共 {len(cache)} 条 → {CACHE}")


if __name__ == "__main__":
    main()
