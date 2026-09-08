# -*- coding: utf-8 -*-
"""
verify_paper.py — 学术元数据核实工具（海洋AI研究日报专用）

用途：在不抓取网页、不绕过反爬的前提下，用官方开放 API 核实论文的
      标题 / 期刊 / 作者 / 发表日期 / 摘要 / OA 状态，并做时效判定。

数据源（均免费、公开、合法，无需 API key）：
  - Crossref  REST API  https://api.crossref.org/works/{doi}
  - OpenAlex  API       https://api.openalex.org/works/doi:{doi}
  - （可选）Semantic Scholar / Unpaywall 见 --s2 / --oa 参数

用法：
  python verify_paper.py 10.3390/su18178986
  python verify_paper.py https://www.mdpi.com/2072-4292/18/17/2991
  python verify_paper.py 10.3390/su18178986 10.1029/2026JH001279 --today 2026-09-07
  python verify_paper.py 10.3390/su18178986 --json

退出码：0 = 全部核实成功；1 = 至少一个 DOI 核实失败
"""
import sys
import re
import json
import ssl
import time
import argparse
import datetime
import urllib.request

UA = "OceanAIDailyReport/1.0 (mailto:sutiany@163.com)"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

FRESH_DAYS = 14      # 日报时效红线
EXEMPT_DAYS = 60     # 豁免上限（须顶级来源 + 不重复 + 标注原始日期）


def _get(url, timeout=25, retries=2):
    """带重试的 JSON 拉取。OpenAlex 偶发 SSL 握手超时，重试一次通常即恢复。"""
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return json.loads(r.read().decode("utf-8", "ignore"))
        except Exception as e:
            last = e
            if i < retries:
                time.sleep(1.5)
    raise last


def norm_date(s):
    """统一为 YYYY-MM-DD 便于比较；缺月/日补 01，并返回精度(3=日,2=月,1=年)。"""
    if not s:
        return None, 0
    parts = [int(x) for x in str(s).split("-") if str(x).isdigit()]
    if not parts:
        return None, 0
    prec = len(parts)
    while len(parts) < 3:
        parts.append(1)
    try:
        return datetime.date(parts[0], parts[1], parts[2]).isoformat(), prec
    except ValueError:
        return None, 0


def extract_doi(user_input):
    """从 DOI 字符串或含 DOI 的 URL 中抽取 DOI。"""
    s = user_input.strip()
    m = re.search(r"(10\.\d{4,9}/[^\s\"'<>?#]+)", s)
    if m:
        return m.group(1).rstrip(".,;)")
    return None


def inv_to_text(inv):
    """OpenAlex 的 abstract_inverted_index 还原为文本。"""
    if not inv:
        return None
    pos = {}
    for word, places in inv.items():
        for p in places:
            pos[p] = word
    return " ".join(pos[k] for k in sorted(pos))


def from_crossref(doi):
    try:
        m = _get("https://api.crossref.org/works/" + doi)["message"]
    except Exception as e:
        return {"ok": False, "err": "%s: %s" % (type(e).__name__, str(e)[:80])}
    title = (m.get("title") or ["?"])[0]
    container = (m.get("container-title") or ["?"])[0]
    authors = []
    for a in (m.get("author") or [])[:6]:
        authors.append(("%s %s" % (a.get("given", ""), a.get("family", ""))).strip())
    date = None
    for key in ("published", "published-online", "published-print", "issued", "created"):
        parts = (m.get(key) or {}).get("date-parts") or [[None]]
        if parts and parts[0] and parts[0][0]:
            date = parts[0]
            break
    return {
        "ok": True,
        "title": title,
        "journal": container,
        "authors": authors,
        "date": "-".join(str(x) for x in date) if date else None,
        "date_precision": len(date) if date else 0,   # 3=日, 2=月, 1=年
        "abstract": re.sub(r"<[^>]+>", " ", m.get("abstract") or "") or None,
        "url": m.get("URL"),
    }


def from_openalex(doi):
    try:
        w = _get("https://api.openalex.org/works/doi:" + doi)
    except Exception as e:
        return {"ok": False, "err": "%s: %s" % (type(e).__name__, str(e)[:80])}
    loc = w.get("primary_location") or {}
    src = loc.get("source") or {}
    oa = w.get("open_access") or {}
    return {
        "ok": True,
        "title": w.get("title"),
        "journal": src.get("display_name"),
        "date": w.get("publication_date"),
        "type": w.get("type"),
        "abstract": inv_to_text(w.get("abstract_inverted_index")),
        "oa_status": oa.get("oa_status"),
        "oa_url": oa.get("oa_url"),
        "cited_by": w.get("cited_by_count"),
    }


def judge(date_str, today):
    """时效判定：<=14 合格；15-60 需豁免；>60 禁收。"""
    if not date_str:
        return "无日期", None, "须人工核实"
    parts = [int(x) for x in date_str.split("-") if x.isdigit()]
    if not parts:
        return "无日期", None, "须人工核实"
    while len(parts) < 3:
        parts.append(1)                      # 缺月/日按当月 1 号估算
    try:
        d = datetime.date(parts[0], parts[1], parts[2])
    except ValueError:
        return "日期异常", None, "须人工核实"
    age = (today - d).days
    if age <= FRESH_DAYS:
        flag = "OK"
    elif age <= EXEMPT_DAYS:
        flag = "需豁免"
    else:
        flag = "超期"
    return flag, age, "%d 天" % age


def verify(doi, today, want_json=False):
    cr = from_crossref(doi)
    oa = from_openalex(doi)

    # 日期以 Crossref 优先（出版方注册数据），OpenAlex 作为交叉校验；两者都规范化后再比较
    date_raw = (cr.get("date") if cr.get("ok") else None) or (oa.get("date") if oa.get("ok") else None)
    date, prec = norm_date(date_raw)
    alt_date, _ = norm_date(oa.get("date") if oa.get("ok") else None)

    title = (cr.get("title") if cr.get("ok") else None) or (oa.get("title") if oa.get("ok") else None)
    journal = (cr.get("journal") if cr.get("ok") else None) or (oa.get("journal") if oa.get("ok") else None)

    flag, age, age_txt = judge(date, today)

    out = {
        "doi": doi,
        "title": title,
        "journal": journal,
        "authors": cr.get("authors") if cr.get("ok") else None,
        "date_crossref": norm_date(cr.get("date") if cr.get("ok") else None)[0],
        "date_openalex": alt_date,
        "date_used": date,
        "date_precision": prec,          # 3=精确到日, 2=仅到月, 1=仅到年
        "age_days": age,
        "timeliness": flag,
        "abstract": (oa.get("abstract") if oa.get("ok") else None) or (cr.get("abstract") if cr.get("ok") else None),
        "oa_status": oa.get("oa_status") if oa.get("ok") else None,
        "cited_by": oa.get("cited_by") if oa.get("ok") else None,
        "crossref_ok": cr.get("ok"),
        "openalex_ok": oa.get("ok"),
        "errors": [x for x in [cr.get("err"), oa.get("err")] if x],
    }

    if want_json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return out

    print("=" * 72)
    print("DOI      :", doi)
    print("标题     :", (title or "(未获取)")[:88])
    print("期刊     :", journal or "(未获取)")
    if out["authors"]:
        print("作者     :", ", ".join(out["authors"][:5]))
    print("发表日期 : Crossref = %s | OpenAlex = %s" % (out["date_crossref"], out["date_openalex"]))
    if out["date_crossref"] and out["date_openalex"] and out["date_crossref"] != out["date_openalex"]:
        print("           !! 两源日期不一致，按规则须以出版方/首次公开日为准并人工复核")
    if prec and prec < 3:
        print("           !! 日期仅精确到%s，本工具按当月 1 号估算，须 WebFetch 原文补准确日"
              % ("月" if prec == 2 else "年"))
    print("时效     : %s（%s）" % (flag, age_txt))
    if out["oa_status"]:
        print("开放获取 :", out["oa_status"])
    if out["cited_by"] is not None:
        print("被引     :", out["cited_by"])
    ab = out["abstract"]
    if ab:
        print("摘要     :", ab[:300].replace("\n", " ") + ("..." if len(ab) > 300 else ""))
    else:
        print("摘要     : (API 未提供，需 WebFetch 原文补)")
    if out["errors"]:
        print("错误     :", " | ".join(out["errors"]))
    print()
    return out


def main():
    ap = argparse.ArgumentParser(description="用 Crossref/OpenAlex 官方 API 核实论文元数据（不抓网页、不绕反爬）")
    ap.add_argument("dois", nargs="+", help="DOI 或含 DOI 的 URL，可传多个")
    ap.add_argument("--today", default=None, help="基准日期 YYYY-MM-DD，默认今天")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出，便于脚本消费")
    args = ap.parse_args()

    today = (datetime.date(*[int(x) for x in args.today.split("-")])
             if args.today else datetime.date.today())

    ok_all = True
    for raw in args.dois:
        doi = extract_doi(raw)
        if not doi:
            print("!! 无法从输入解析 DOI：%s" % raw)
            ok_all = False
            continue
        r = verify(doi, today, want_json=args.json)
        if not (r["crossref_ok"] or r["openalex_ok"]):
            ok_all = False
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
