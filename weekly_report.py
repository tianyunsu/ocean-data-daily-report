# -*- coding: utf-8 -*-
"""
weekly_report.py — L3 周报：池内统计驱动的趋势综述（海洋AI研究日报专用）

输入：data/library.db（screen.py 累积的池）
输出：weekly/YYYY-Www.html  —— 含统计图表 + 自动要点 + 预留"本期趋势综述"段落供人工/模型填写
      weekly/YYYY-Www.json  —— 结构化统计（供后续比对）

用法：
  py -3 weekly_report.py                 # 以今天为结束日，回看 7 天
  py -3 weekly_report.py --end 2026-09-20 --days 7
"""
import json
import math
import sqlite3
import argparse
import datetime
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent
DB = ROOT / "data" / "library.db"
OUTDIR = ROOT / "weekly"

DIR_NAMES = {1: "海洋人工智能", 2: "海洋数字孪生", 3: "海洋可视化", 4: "海洋数据质量",
             5: "海洋数据处理", 6: "数据管理与共享", 7: "开放航次与科考",
             8: "海洋数据中心", 9: "工具与代码资源"}
TIER_ORDER = ["S", "A", "B", "C", "P", "D", "?"]
STOP = set("the a an of and or for with on in to using based via from by new study analysis "
           "model models data ocean marine sea coastal global deep learning approach method "
           "results case review research system systems".split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--end", default=datetime.date.today().isoformat())
    ap.add_argument("--days", type=int, default=7)
    a = ap.parse_args()
    end = datetime.date.fromisoformat(a.end)
    start = end - datetime.timedelta(days=a.days - 1)

    if not DB.exists():
        print("没有 library.db，请先运行 harvest.py + screen.py")
        return
    con = sqlite3.connect(DB)
    cur = con.execute("""SELECT title, journal, publisher, tier, direction, doi, url,
                                pub_date, score, cited_by, is_preprint, flags
                         FROM works WHERE date BETWEEN ? AND ?""",
                      (start.isoformat(), end.isoformat()))
    rows = [dict(zip(["title", "journal", "publisher", "tier", "direction", "doi", "url",
                      "pub_date", "score", "cited_by", "is_preprint", "flags"], r)) for r in cur]
    con.close()
    if not rows:
        print(f"{start} ~ {end} 池内无记录")
        return

    tiers = Counter(r["tier"] for r in rows)
    dirs = Counter(r["direction"] for r in rows)
    journals = Counter(r["journal"] for r in rows if r["journal"] and r["tier"] not in ("D",))
    warn_journals = Counter(r["journal"] for r in rows if r["tier"] == "D")
    warned = sum(1 for r in rows if r["tier"] == "D")
    preprints = sum(1 for r in rows if r["is_preprint"])
    words = Counter()
    for r in rows:
        if r["tier"] in ("D",):
            continue
        for w in re.findall(r"[a-z][a-z-]{3,}", (r["title"] or "").lower()):
            if w not in STOP:
                words[w] += 1
    top_words = words.most_common(18)
    top_scored = sorted(rows, key=lambda x: -x["score"])[:15]
    high = [r for r in rows if r["tier"] in ("S", "A")]
    top_inst_journals = [j for j, _ in journals.most_common(12)]

    wk = end.isocalendar()
    tag = f"{wk[0]}-W{wk[1]:02d}"
    OUTDIR.mkdir(parents=True, exist_ok=True)

    stats = {
        "week": tag, "start": start.isoformat(), "end": end.isoformat(),
        "pool_total": len(rows), "tiers": dict(tiers), "directions": dict(dirs),
        "warned": warned, "preprints": preprints,
        "top_journals": journals.most_common(20), "top_words": top_words,
        "high_tier_count": len(high),
    }
    (OUTDIR / f"{tag}.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")

    def bars(counter, normalize=False):
        mx = max(counter.values()) if counter else 1
        return [(k, v, round(v * 100 / mx)) for k, v in counter.items()]

    dir_rows = "".join(
        f'<tr><td>{DIR_NAMES.get(int(k), k)}</td><td style="text-align:right">{v}</td>'
        f'<td><span style="display:inline-block;height:9px;width:{round(v*100/max(dirs.values()))}%;'
        f'background:#378ADD;border-radius:2px"></span></td></tr>'
        for k, v in sorted(dirs.items(), key=lambda x: -x[1])
        if k and str(k).isdigit())
    tier_rows = "".join(
        f'<tr><td>{t}</td><td style="text-align:right">{tiers.get(t,0)}</td>'
        f'<td><span style="display:inline-block;height:9px;width:{round(tiers.get(t,0)*100/max(tiers.values()))}%;'
        f'background:#1D9E75;border-radius:2px"></span></td></tr>' for t in TIER_ORDER if tiers.get(t))
    journal_rows = "".join(f'<tr><td>{j or "—"}</td><td style="text-align:right">{n}</td></tr>'
                           for j, n in journals.most_common(15))
    warn_rows = "".join(f'<tr><td>{j or "—"}</td><td style="text-align:right">{n}</td></tr>'
                        for j, n in warn_journals.most_common(10))
    top_rows = "".join(
        f'<li><a href="{r["url"] or ("https://doi.org/" + (r["doi"] or ""))}" target="_blank" rel="noopener">'
        f'{r["title"][:150]}</a><br><span class="sub">{r["journal"] or "—"} · {r["pub_date"]} · '
        f'等级 {r["tier"]} · 评分 {r["score"]}</span></li>' for r in top_scored)
    word_cloud = " · ".join(f'{w}<span class="sub">({n})</span>' for w, n in top_words)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI前沿周报 · {tag}</title>
<link rel="stylesheet" href="../style.css">
<style>
 .wk-wrap{{max-width:960px;margin:0 auto;padding:0 18px 60px;}}
 .wk-card{{border:1px solid #e6e9ee;border-radius:12px;padding:16px 18px;margin:16px 0;background:#fff;}}
 .wk-card h2{{font-size:16px;margin:0 0 10px;}}
 table.wk{{width:100%;border-collapse:collapse;font-size:13.5px;}}
 table.wk td{{padding:6px 6px;border-bottom:1px solid #f0f2f5;vertical-align:middle;}}
 table.wk td:nth-child(2),table.wk td:nth-child(3){{width:120px;}}
 .kv{{display:flex;flex-wrap:wrap;gap:14px;margin:6px 0 0;}}
 .kv div{{background:#f6f8fa;border-radius:8px;padding:10px 14px;min-width:120px;}}
 .kv b{{display:block;font-size:20px;}}
 .sub{{color:#7a828e;font-size:12.5px;}}
 .wk-card ol{{padding-left:20px;font-size:13.5px;line-height:1.6;}}
</style></head><body>
<header class="site-header">
  <h1><a href="../index.html">🌊 海洋AI技术日报</a></h1>
  <p>前沿周报 · {start} 至 {end} · 池内 {len(rows)} 条</p>
  <nav><a href="../index.html">首页</a><a href="../frontier.html">前沿跟踪</a>
  <a href="../archive.html">全部归档</a></nav>
</header>
<main class="wk-wrap">
  <div class="wk-card"><h2>本周概览</h2>
    <div class="kv">
      <div><span class="sub">池内总量</span><b>{len(rows)}</b></div>
      <div><span class="sub">S/A 级</span><b>{len(high)}</b></div>
      <div><span class="sub">预印本</span><b>{preprints}</b></div>
      <div><span class="sub">预警/受限刊</span><b>{warned}</b></div>
    </div>
    <p class="sub" style="margin-top:10px">预印本与预警刊均已计入池内并标注，未从统计中剔除，便于观察占比变化。</p>
  </div>
  <div class="wk-card"><h2>方向分布</h2><table class="wk">{dir_rows}</table></div>
  <div class="wk-card"><h2>期刊分级分布</h2><table class="wk">{tier_rows}</table>
    <p class="sub">S = Nature/Science/PNAS 正刊及顶级子刊；A = 领域权威；B = 主流 SCI；C = 一般/新刊；P = 预印本；D = 预警/受限。</p></div>
  <div class="wk-card"><h2>高频期刊（已排除预警刊）</h2><table class="wk">{journal_rows}</table></div>
  <div class="wk-card"><h2>预警/受限期刊（仅供取舍，不代表否定其成果）</h2><table class="wk">{warn_rows or '<tr><td>本周无</td><td></td></tr>'}</table></div>
  <div class="wk-card"><h2>标题主题词</h2><p style="font-size:13.5px;line-height:1.9">{word_cloud}</p></div>
  <div class="wk-card"><h2>本周高评分条目（Top 15）</h2><ol>{top_rows}</ol></div>
  <div class="wk-card"><h2>本期趋势综述</h2>
    <p class="sub">（此段由人工/模型在生成周报时填写：本周热点迁移、方法趋势、机构分布、值得跟进的 3–5 条线索。）</p></div>
</main></body></html>"""
    (OUTDIR / f"{tag}.html").write_text(html, encoding="utf-8")
    print(f"周报已生成：weekly/{tag}.html（池内 {len(rows)} 条 · S/A {len(high)} · 预警 {warned}）")
    print(f"统计摘要：{OUTDIR / (tag + '.json')}")


if __name__ == "__main__":
    main()
