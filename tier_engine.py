# -*- coding: utf-8 -*-
"""
tier_engine.py — 期刊分级引擎（海洋AI研究日报专用）

分级口径（2026-09-20 苏老师拍板）：
  S  Science / Nature / PNAS 正刊及顶级子刊（最高优先级）
  A  领域权威期刊（学会旗舰刊、高影响力子刊）
  B  主流 SCI 期刊
  C  一般期刊 / 新刊 / 开放获取集团刊
  P  预印本（未经同行评审，独立标记，排序低于 S/A 期刊论文）
  D  预警 / 受限期刊（MDPI 等集团刊、中科院与中信所预警名单，强制标注，供取舍）
  ?  未登记（自动进入待确认清单，供问答式校准）

判定顺序：预印本 → 逐刊登记表 → 最新一期预警名单 → 出版集团规则 → 待确认

用法：
  py -3 tier_engine.py "Journal of Marine Science and Engineering" --publisher MDPI
  py -3 tier_engine.py "Ocean Engineering" --publisher Elsevier
  py -3 tier_engine.py --pending          # 查看待确认期刊清单（问答式校准用）
  py -3 tier_engine.py --stats            # 查看登记表统计
"""
import json
import re
import sys
import argparse
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "data" / "journal_tiers.json"
METRICS = ROOT / "data" / "source_metrics.json"

_cache = None
_metrics = None


def load_metrics():
    global _metrics
    if _metrics is None:
        _metrics = json.loads(METRICS.read_text(encoding="utf-8")) if METRICS.exists() else {}
    return _metrics


def auto_tier(issn=None, publisher=None, journal=None):
    """
    指标自动评级（人工登记表未覆盖时使用）。依据 OpenAlex Sources：
      h_index / 两年均被引 / 是否 DOAJ。
    阈值设定（2026-09-20 初版，待苏老师按学科经验校准）：
      A : h_index ≥ 120 或 两年均被引 ≥ 6.0
      B : h_index ≥ 50  或 两年均被引 ≥ 3.0
      C : h_index ≥ 15  或 两年均被引 ≥ 1.0
    返回 (tier, note) 或 (None, None)
    """
    m = None
    if issn:
        m = load_metrics().get(issn)
    if not m or m.get("miss"):
        return None, None
    h = m.get("h_index") or 0
    c = m.get("citedness") or 0
    if h >= 120 or c >= 6.0:
        t = "A"
    elif h >= 50 or c >= 3.0:
        t = "B"
    elif h >= 15 or c >= 1.0:
        t = "C"
    else:
        t = "C"
    note = (f"自动评级（h-index {h}，两年均被引 {c}，"
            f"{'DOAJ 收录' if m.get('in_doaj') else '非 DOAJ'}，"
            f"年发文 {m.get('works')}）· 未登记，待校准")
    return t, note


def load_registry(path=None):
    global _cache
    if _cache is None or path is not None:
        p = Path(path) if path else REGISTRY
        _cache = json.loads(p.read_text(encoding="utf-8"))
    return _cache


def save_registry(reg=None, path=None):
    global _cache
    reg = reg or load_registry()
    p = Path(path) if path else REGISTRY
    p.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    _cache = reg


def norm(name):
    """归一化期刊名：小写、去标点、压空格、去前导 the。"""
    if not name:
        return ""
    s = str(name).lower().strip()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _build_index(reg):
    """建立 normalized name -> entry 索引（含别名）。"""
    idx = {}
    for key, entry in reg.get("journals", {}).items():
        idx[norm(key)] = entry
        for alias in entry.get("aliases", []) or []:
            idx[norm(alias)] = entry
    return idx


def _active_warning(reg):
    """汇总【最新一期】预警名单（官方规则：不累积使用）。"""
    hits = {}
    lists = reg.get("warning_lists", {})
    active = {k: v for k, v in lists.items() if v.get("active")}
    for lname, ldata in active.items():
        for j in ldata.get("journals", []) or []:
            hits.setdefault(norm(j), []).append(lname)
    return hits


def classify(journal=None, publisher=None, is_preprint=False, issn=None):
    """
    返回 dict: tier / label / flags[] / note / matched
    """
    reg = load_registry()
    weights = reg["policy"]["weights"]
    labels = reg["tier_labels"]
    flags = []
    note = ""
    auto = False

    if is_preprint or not journal:
        if is_preprint:
            flags.append("预印本，未经同行评审")
            return {"tier": "P", "label": labels["P"], "flags": flags,
                    "note": "预印本不计入高质量证据，排序低于 S/A 级期刊论文",
                    "weight": weights["P"], "matched": "preprint"}
        return {"tier": "?", "label": labels["?"], "flags": flags, "note": note,
                "weight": weights["?"], "matched": None}

    n = norm(journal)
    idx = _build_index(reg)
    warn = _active_warning(reg)
    matched = None

    entry = idx.get(n)
    if entry:
        tier = entry.get("tier") or "?"
        note = entry.get("note", "") or ""
        matched = "registry"
        if entry.get("publisher"):
            note = (note + " " if note else "") + f"出版方：{entry['publisher']}"
    else:
        tier = None

    if n in warn:
        tier = "D"
        flags.append("预警名单：" + "、".join(warn[n]))
        matched = matched or "warning"
        note = (note + " " if note else "") + "最新一期预警名单命中"
    elif tier is None:
        pub = norm(publisher)
        for pubkey, rule in reg.get("publisher_rules", {}).items():
            if pubkey and pubkey in pub and rule.get("tier"):
                tier = rule["tier"]
                flags.append(rule.get("flag", pubkey))
                matched = f"publisher:{pubkey}"
                break
        if tier is None and n in [norm(x) for x in reg.get("mdpi_journals_seen", [])]:
            rule = reg["publisher_rules"]["mdpi"]
            tier = rule["tier"]
            flags.append(rule["flag"] + "（按已见 MDPI 刊名清单命中）")
            matched = "mdpi_seen_list"
        if tier is None:
            # 二级兜底：OpenAlex 期刊指标自动评级（标记 auto，待校准）
            t_auto, note_auto = auto_tier(issn, publisher, journal)
            if t_auto:
                tier, auto, matched = t_auto, True, "metrics-auto"
                note = (note + " " if note else "") + (note_auto or "")
                flags.append("自动评级（未登记，待苏老师校准）")
            else:
                tier = "?"
                matched = None

    if tier == "D":
        return {"tier": "D", "label": labels["D"], "flags": flags or ["最低等级：预警/受限期刊"],
                "note": note, "weight": weights["D"], "matched": matched}
    if tier == "?":
        return {"tier": "?", "label": labels["?"], "flags": ["未登记期刊，已加入待确认清单"],
                "note": note, "weight": 0, "matched": None}
    return {"tier": tier, "label": labels[tier], "flags": flags, "note": note,
            "weight": weights[tier], "matched": matched}


def add_pending(journal, publisher=None, direction=None, count=1, example=None):
    """把未登记期刊写入待确认清单（去重累加）。"""
    reg = load_registry()
    n = norm(journal)
    for item in reg.setdefault("pending", []):
        if norm(item["journal"]) == n:
            item["count"] = item.get("count", 1) + count
            if example and example not in item.get("examples", [])[:5]:
                item.setdefault("examples", []).append(example)
            save_registry(reg)
            return False
    reg["pending"].append({
        "journal": journal, "publisher": publisher or "", "direction": direction or "",
        "count": count, "examples": [example] if example else [],
        "first_seen": datetime.date.today().isoformat(), "asked": False
    })
    save_registry(reg)
    return True


def pending_report():
    reg = load_registry()
    return reg.get("pending", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("journal", nargs="?")
    ap.add_argument("--publisher")
    ap.add_argument("--preprint", action="store_true")
    ap.add_argument("--pending", action="store_true")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()

    if a.pending:
        rows = sorted(pending_report(), key=lambda x: -x.get("count", 1))
        if not rows:
            print("待确认清单为空。")
        for r in rows:
            print(f"[{r.get('count',1):>3} 篇] {r['journal']}"
                  f"{' · ' + r['publisher'] if r.get('publisher') else ''}"
                  f"{' · ' + r['direction'] if r.get('direction') else ''}")
        return

    if a.stats:
        reg = load_registry()
        from collections import Counter
        c = Counter(v.get("tier") for v in reg["journals"].values())
        print("登记表统计：", dict(c), "共", len(reg["journals"]), "本")
        print("待确认：", len(reg.get("pending", [])), "本")
        for k, v in reg["warning_lists"].items():
            print(f"  预警名单 {k}: {'生效' if v.get('active') else '存档'} · {len(v.get('journals',[]))} 本")
        return

    if not a.journal:
        ap.print_help()
        return
    r = classify(a.journal, a.publisher, is_preprint=a.preprint)
    print(json.dumps(r, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
