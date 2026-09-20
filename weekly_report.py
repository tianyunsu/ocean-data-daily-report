# -*- coding: utf-8 -*-
"""
weekly_report.py — L3 周报：池内统计 + 各领域综述（海洋AI研究日报专用）

输入：data/library.db（screen.py 累积的池）
      weekly/synth/YYYY-Www.md（可选：人工/模型撰写的「本期综述」，自动注入页面顶部）
输出：weekly/YYYY-Www.html  —— 综述板块（深度综述 + 数据驱动各领域自动综述）+ 统计图表
      weekly/YYYY-Www.json  —— 结构化统计（供后续比对）
      weekly/synth/YYYY-Www.draft.md —— 综述写作草稿（逐方向主题簇 + 代表文献 + 期刊分布）

用法：
  py -3 weekly_report.py                                   # 以今天为结束日，回看 7 天
  py -3 weekly_report.py --end 2026-09-20 --days 14
  py -3 weekly_report.py --end 2026-09-20 --synth weekly/synth/2026-W38.md

综述板块的两层结构（缺一层也能出页面）：
  ① 深度综述：weekly/synth/<tag>.md 存在则渲染在最前，标题为「本期综述 · 各领域主要进展」；
  ② 自动综述：始终生成，逐方向给出主题簇（标题关键词聚类）+ 代表文献（带链接）+ 期刊分布，
     口径与看板一致：预警刊(D)与「海洋介质型/弱相关」降权项不计入综述，但计数单列。
"""
import json
import sqlite3
import argparse
import datetime
import html as _html
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent
DB = ROOT / "data" / "library.db"
OUTDIR = ROOT / "weekly"
SYNTHDIR = OUTDIR / "synth"

DIR_NAMES = {1: "海洋人工智能", 2: "海洋数字孪生", 3: "海洋可视化", 4: "海洋数据质量",
             5: "海洋数据处理", 6: "数据管理与共享", 7: "开放航次与科考",
             8: "海洋数据中心", 9: "工具与代码资源"}
DIR_ORDER = ["一、海洋人工智能", "二、海洋数字孪生", "三、海洋可视化", "四、海洋数据质量",
             "五、海洋数据处理", "六、数据管理与共享", "七、开放航次与科考",
             "八、海洋数据中心", "九、工具与代码资源"]
TIER_ORDER = ["S", "A", "B", "C", "P", "D", "?"]
STOP = set("the a an of and or for with on in to using based via from by new study analysis "
           "model models data ocean marine sea coastal global deep learning approach method "
           "results case review research system systems their its into over under between "
           "toward towards enhanced improved improving evaluation assessment impacts impact "
           "effects effect role high low long short first two three using used can not "
           "more most other such than that this these those are was were has have been "
           "analysis-based near real time large small scale multi through across within "
           "without among during after before both each also well better best higher lower "
           "potential future current recent novel effective efficient accurate robust "
           "area areas region regions site sites level levels".split())

# 标题关键词 → 中文主题簇名（未收录的词汇直接以英文词作簇名）
TERM_CN = {
    "machine": "机器学习建模", "learning": "机器学习建模", "neural": "神经网络",
    "artificial": "机器学习建模", "intelligence": "机器学习建模", "intelligent": "机器学习建模",
    "networks": "网络模型", "network": "网络模型", "transformer": "Transformer 架构",
    "attention": "注意力机制", "graph": "图神经网络", "physics-informed": "物理约束学习",
    "coupled": "耦合模式", "gis-based": "GIS 与空间分析", "survey": "调查与普查",
    "emerging": "新兴议题", "rapid": "快速方法与应急", "sustainable": "可持续治理",
    "physics": "物理机理约束", "physicsbased": "物理机理约束", "prediction": "预测建模",
    "predicting": "预测建模", "forecasting": "预报能力", "predictions": "预测建模",
    "reconstruction": "时空重构", "interpolation": "插值重构", "assimilation": "数据同化",
    "uncertainty": "不确定性量化", "quantification": "不确定性量化", "probabilistic": "概率化建模",
    "segmentation": "分割识别", "detection": "目标检测", "classification": "分类识别",
    "recognition": "识别任务", "tracking": "目标跟踪", "optimization": "优化方法",
    "wave": "海浪", "waves": "海浪", "significant": "有效波高", "swell": "涌浪",
    "ice": "海冰", "arctic": "北极", "antarctic": "南极", "polar": "极地",
    "sea": "海洋环境", "level": "海平面", "temperature": "温度与热力", "salinity": "盐度",
    "circulation": "环流", "current": "流场", "currents": "流场", "tide": "潮汐",
    "tidal": "潮汐", "estuar": "河口", "coastal": "海岸带", "shoreline": "岸线",
    "bathymetry": "水深与海底地形", "seafloor": "海底", "seabed": "海底",
    "sediment": "沉积物", "sediments": "沉积物", "coral": "珊瑚礁", "reef": "珊瑚礁",
    "mangrove": "红树林", "edna": "eDNA 监测", "environmental": "环境DNA与监测",
    "biodiversity": "生物多样性", "plankton": "浮游生物", "fisheries": "渔业",
    "fishery": "渔业", "aquaculture": "水产养殖", "fish": "鱼类资源",
    "satellite": "卫星遥感", "remote": "遥感观测", "sensing": "遥感观测",
    "radar": "雷达观测", "hyperspectral": "高光谱", "imagery": "影像分析",
    "underwater": "水下感知与作业", "acoustic": "水声", "sonar": "声呐",
    "quality": "数据质量", "control": "质量控制", "validation": "验证评估",
    "calibration": "标定校准", "benchmark": "基准评测", "monitoring": "监测体系",
    "dataset": "数据集建设", "datasets": "数据集建设", "database": "数据库构建",
    "digital": "数字孪生", "twin": "数字孪生", "twins": "数字孪生",
    "simulation": "仿真模拟", "modelling": "数值建模", "modeling": "数值建模",
    "general": "通用模式", "framework": "框架方法", "energy": "海洋能",
    "wind": "海上风电", "offshore": "海上工程", "turbine": "风机装备",
    "glider": "滑翔机", "autonomous": "自主平台", "vehicle": "水下航行器",
    "vehicles": "水下航行器", "robotic": "机器人", "drone": "无人平台",
    "cruise": "航次考察", "voyage": "航次考察", "expedition": "科学考察",
    "sampling": "采样方案", "observation": "观测系统", "observations": "观测系统",
    "reanalysis": "再分析资料", "era5": "再分析资料", "erosion": "侵蚀演变",
    "carbon": "碳循环", "nutrient": "营养盐", "pollution": "污染与溢油",
    "oil": "溢油", "spill": "溢油", "microplastic": "微塑料", "contaminant": "污染物",
    "eutrophication": "富营养化", "hypoxia": "缺氧", "warming": "增暖",
    "heatwave": "海洋热浪", "acidification": "酸化", "typhoon": "台风",
    "cyclone": "热带气旋", "storm": "风暴", "surge": "风暴潮", "tsunami": "海啸",
    "geological": "地质过程", "volcanic": "火山活动", "hydrothermal": "热液",
    "seismic": "地震勘探", "gravity": "重力场", "geodesy": "大地测量",
    "wind-driven": "风驱动", "turbulence": "湍流混合", "mixing": "混合过程",
    "deep-sea": "深海", "deep": "深海与深水", "vent": "热液喷口",
    "spatial": "空间分析", "gis": "GIS 分析", "mapping": "制图",
    "visualization": "可视化表达", "virtual": "虚拟现实", "immersive": "沉浸式交互",
    "knowledge": "知识组织", "ontology": "本体建模", "fair": "FAIR 数据治理",
    "sharing": "数据共享", "open": "开放科学", "repository": "数据仓储",
    "cloud": "云端平台", "web": "Web 服务", "pipeline": "处理流水线",
    "workflow": "工作流", "toolbox": "工具集", "python": "Python 工具",
    "software": "软件工具", "code": "代码工具", "api": "接口服务",
    "graphics": "图形渲染", "rendering": "图形渲染", "gaussian": "高斯泼溅",
    "slam": "SLAM 定位", "navigation": "导航定位", "positioning": "导航定位",
    "trajectory": "轨迹分析", "drift": "漂移轨迹", "lagrangian": "拉格朗日",
    "policy": "政策治理", "governance": "治理机制", "management": "管理策略",
    "conservation": "保护恢复", "blue": "蓝色经济", "sustainability": "可持续性",
}


def esc(s):
    return _html.escape(str(s or ""))


def load_rows(start, end):
    con = sqlite3.connect(DB)
    cur = con.execute("""SELECT title, journal, publisher, tier, direction, doi, url,
                                pub_date, score, cited_by, is_preprint, flags
                         FROM works WHERE date BETWEEN ? AND ?""",
                      (start.isoformat(), end.isoformat()))
    cols = ["title", "journal", "publisher", "tier", "direction", "doi", "url",
            "pub_date", "score", "cited_by", "is_preprint", "flags"]
    rows = [dict(zip(cols, r)) for r in cur]
    con.close()
    return rows


def is_off(r):
    """海洋介质型/弱相关 → 已在 screen.py 降权，综述不计入"""
    return "已降权" in (r["flags"] or "")


def link(r):
    u = r["url"] or ("https://doi.org/" + r["doi"] if r["doi"] else "")
    return u


def clusters(rows, max_terms=12, min_count=2):
    """标题关键词聚类：返回 [(簇名, 篇数, [代表条目...]), ...]、未归类条目、词频表"""
    words = Counter()
    for r in rows:
        for w in re.findall(r"[a-z][a-z-]{3,}", (r["title"] or "").lower()):
            if w not in STOP:
                words[w] += 1
    terms = [w for w, n in words.most_common(40) if n >= min_count][:max_terms]
    buckets = defaultdict(list)
    unassigned = []
    for r in rows:
        t = (r["title"] or "").lower()
        hit = next((w for w in terms if w in t), None)
        if hit:
            buckets[hit].append(r)
        else:
            unassigned.append(r)
    merged = {}          # 中文簇名 -> [条目]
    for w in terms:
        items = buckets.get(w)
        if not items:
            continue
        merged.setdefault(TERM_CN.get(w, w), []).extend(items)
    out = []
    for name, items in merged.items():
        seen, uniq = set(), []
        for r in items:                      # 同一条可能命中多个近义簇，去重
            if r["title"] not in seen:
                uniq.append(r); seen.add(r["title"])
        if len(uniq) < min_count:
            continue
        uniq.sort(key=lambda x: -x["score"])
        out.append((name, len(uniq), uniq))
    out.sort(key=lambda x: -x[1])
    return out, unassigned, words


def rep_li(items, k=3):
    li = ""
    for r in items[:k]:
        u = link(r)
        t = esc(r["title"][:120] + ("…" if len(r["title"]) > 120 else ""))
        jn = esc(r["journal"] or "—")
        ttl = f'<a href="{esc(u)}" target="_blank" rel="noopener">{t}</a>' if u else t
        li += (f'<li>{ttl}<span class="sub"> · {jn} · {esc(r["pub_date"])} · '
               f'{esc(r["tier"])} 级</span></li>')
    return li


def md_to_html(md):
    """极简 Markdown 渲染：##/### 标题、- 列表、**加粗**、[文字](链接)、段落"""
    def inline(s):
        s = esc(s)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
                   r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    out, buf, in_ul = [], [], False

    def flush_p():
        nonlocal buf
        if buf:
            out.append("<p>" + inline(" ".join(buf)) + "</p>")
            buf = []

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_p(); close_ul(); continue
        if line.startswith("### "):
            flush_p(); close_ul(); out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush_p(); close_ul(); out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush_p(); close_ul(); out.append(f"<h2>{inline(line[2:])}</h2>")
        elif line.startswith("> "):
            flush_p(); close_ul()
            out.append(f'<p class="syn-quote">{inline(line[2:])}</p>')
        elif re.match(r"^\s*[-*] ", line):
            flush_p()
            if not in_ul:
                out.append('<ul class="syn-ul">'); in_ul = True
            out.append(f"<li>{inline(re.sub(r'^\s*[-*] ', '', line))}</li>")
        else:
            close_ul(); buf.append(line.strip())
    flush_p(); close_ul()
    return "\n".join(out)


def write_index():
    """重建 weekly/index.html —— 周报索引页（自动扫描 weekly/*.json）"""
    items = []
    for j in sorted(OUTDIR.glob("*.json"), reverse=True):
        try:
            d = json.loads(j.read_text(encoding="utf-8"))
        except Exception:
            continue
        if "week" not in d:
            continue
        items.append(d)
    if not items:
        return None
    rows = ""
    for d in items:
        t = d.get("tiers") or {}
        hi = d.get("high_tier_count", 0)
        rows += (
            f'<li class="wk-li"><a class="wk-link" href="{esc(d["week"])}.html">'
            f'<b>{esc(d["week"])}</b>'
            f'<span class="sub"> · {esc(d["start"])} 至 {esc(d["end"])}</span></a>'
            f'<div class="sub wk-sum">池内 {d.get("pool_total", 0)} 条 · S/A {hi} · '
            f'预印本 {d.get("preprints", 0)} · 预警/受限 {d.get("warned", 0)} · '
            f'降权 {d.get("off_penalized", 0)} · '
            f'分级 {" / ".join(f"{k}{v}" for k, v in sorted((t or {}).items()))}'
            f'{" · 深度综述" if "深度综述" in (d.get("synthesis_source") or "") else " · 自动综述"}</div></li>')
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>前沿周报 - 海洋AI技术日报</title>
<link rel="stylesheet" href="../style.css">
<style>
 .wk-wrap{{max-width:920px;margin:0 auto;padding:0 18px 60px;}}
 .wk-card{{border:1px solid #e6e9ee;border-radius:12px;padding:16px 18px;margin:16px 0;background:#fff;}}
 .wk-card h2{{font-size:16px;margin:0 0 10px;}}
 ul.wk-ul{{list-style:none;margin:0;padding:0;}}
 li.wk-li{{padding:12px 0;border-bottom:1px solid #f0f2f5;}}
 li.wk-li:last-child{{border-bottom:none;}}
 .wk-link{{font-size:15px;color:#12457a;text-decoration:none;}}
 .wk-link:hover{{text-decoration:underline;}}
 .wk-sum{{margin-top:4px;line-height:1.6;}}
</style></head><body>
<header class="site-header">
  <h1><a href="../index.html">🌊 海洋AI技术日报</a></h1>
  <p>前沿周报 · 逐周汇总池内文献，含各领域主要进展综述</p>
  <nav><a href="../index.html">首页</a><a href="../frontier.html">前沿跟踪</a>
  <a href="index.html" class="active">前沿周报</a>
  <a href="../archive.html">全部归档</a></nav>
</header>
<main class="wk-wrap">
  <div class="wk-card"><h2>全部周报（共 {len(items)} 期）</h2>
    <ul class="wk-ul">{rows}</ul>
  </div>
  <div class="wk-card"><h2>如何生成综述</h2>
    <p class="sub" style="line-height:1.8">
    周报综述分两层：<br>
    ① <b>自动综述</b>——由 weekly_report.py 直接生成，逐方向列出主题簇、代表文献与主要期刊，始终可用；<br>
    ② <b>深度综述</b>——把逐方向解读写入 <code>weekly/synth/YYYY-Www.md</code>，再运行
    <code>py -3 weekly_report.py --end YYYY-MM-DD --days 14</code>，页面顶部即出现「本期综述 · 各领域主要进展」。
    运行脚本时还会同时产出 <code>weekly/synth/YYYY-Www.draft.md</code> 写作草稿（含各方向主题簇与代表文献）。</p>
  </div>
</main>
<footer class="site-footer"><p>© 2026 海洋AI技术日报 · Powered by GitHub Pages</p></footer>
</body></html>"""
    (OUTDIR / "index.html").write_text(html, encoding="utf-8")
    return OUTDIR / "index.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--end", default=datetime.date.today().isoformat())
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--synth", default=None, help="人工/模型撰写的综述 md，路径")
    ap.add_argument("--no-draft", action="store_true", help="不输出综述写作草稿")
    a = ap.parse_args()
    end = datetime.date.fromisoformat(a.end)
    start = end - datetime.timedelta(days=a.days - 1)
    wk = end.isocalendar()
    tag = f"{wk[0]}-W{wk[1]:02d}"

    if not DB.exists():
        print("没有 library.db，请先运行 harvest.py + screen.py")
        return
    rows = load_rows(start, end)
    if not rows:
        print(f"{start} ~ {end} 池内无记录")
        return

    # ---------- 统计（全量口径，不剔除任何项） ----------
    tiers = Counter(r["tier"] for r in rows)
    dirs = Counter(r["direction"] for r in rows)
    journals = Counter(r["journal"] for r in rows if r["journal"] and r["tier"] != "D")
    warn_journals = Counter(r["journal"] for r in rows if r["tier"] == "D")
    warned = sum(1 for r in rows if r["tier"] == "D")
    preprints = sum(1 for r in rows if r["is_preprint"])
    offs = [r for r in rows if is_off(r)]
    high = [r for r in rows if r["tier"] in ("S", "A")]

    # ---------- 综述样本：剔除 D 级预警刊与降权项 ----------
    clean = [r for r in rows if r["tier"] != "D" and not is_off(r)]
    bydir = defaultdict(list)
    for r in clean:
        bydir[r["direction"]].append(r)

    # 全文主题词（原「标题主题词」，保留在统计区）
    all_words = Counter()
    for r in rows:
        if r["tier"] == "D":
            continue
        for w in re.findall(r"[a-z][a-z-]{3,}", (r["title"] or "").lower()):
            if w not in STOP:
                all_words[w] += 1
    top_words = all_words.most_common(18)

    top_scored = sorted(rows, key=lambda x: -x["score"])[:15]
    OUTDIR.mkdir(parents=True, exist_ok=True)
    SYNTHDIR.mkdir(parents=True, exist_ok=True)

    # ---------- 自动综述：逐方向主题簇 + 代表文献 + 期刊分布 ----------
    dir_blocks = []
    dir_digest = {}
    for d in DIR_ORDER:
        items = bydir.get(d) or []
        if not items:
            dir_blocks.append(f'<div class="syn-dir"><h3>{esc(d)}</h3>'
                              f'<p class="sub">本期该方向池内无新增条目。</p></div>')
            dir_digest[d] = {"n": 0}
            continue
        total_dir = dirs.get(d, 0)
        sa = sum(1 for r in items if r["tier"] in ("S", "A"))
        pre = sum(1 for r in items if r["is_preprint"])
        offn = sum(1 for r in rows if r["direction"] == d and is_off(r))
        dn = sum(1 for r in rows if r["direction"] == d and r["tier"] == "D")
        cl, unassigned, words = clusters(items)
        top_j = Counter(r["journal"] for r in items if r["journal"]).most_common(4)
        jline = "、".join(f"{esc(j)} {n} 篇" for j, n in top_j) or "—"
        cl_rows = "".join(
            f'<div class="syn-clu"><div class="syn-clu-h"><b>{esc(name)}</b>'
            f'<span class="sub"> · {n} 篇</span></div><ul class="syn-ul">{rep_li(it)}</ul></div>'
            for name, n, it in cl[:5])
        misc = ""
        if unassigned:
            misc = (f'<div class="syn-clu"><div class="syn-clu-h"><b>其他单篇进展</b>'
                    f'<span class="sub"> · {len(unassigned)} 篇</span></div>'
                    f'<ul class="syn-ul">{rep_li(sorted(unassigned, key=lambda x: -x["score"]), 3)}</ul></div>')
        notes = []
        if dn:
            notes.append(f"{dn} 条来自预警/受限期刊（D 级），已计入统计但不进入综述")
        if offn:
            notes.append(f"{offn} 条判定为海洋介质型/弱相关，已降权不计入综述")
        note_html = f'<p class="sub syn-note">注：{"；".join(notes)}。</p>' if notes else ""
        dir_blocks.append(
            f'<div class="syn-dir"><h3>{esc(d)}'
            f'<span class="sub"> · 池内 {total_dir} 条 · 综述样本 {len(items)} 条'
            f'（S/A {sa} · 预印本 {pre}）</span></h3>'
            f'<p class="syn-meta">主要期刊：{jline}</p>'
            f'{cl_rows}{misc}{note_html}</div>')
        dir_digest[d] = {
            "n": total_dir, "sample": len(items), "sa": sa, "preprint": pre,
            "journals": [{"j": j, "n": n} for j, n in top_j],
            "clusters": [{"name": cname, "n": cn,
                          "rep": [{"title": p["title"], "url": link(p), "journal": p["journal"],
                                   "tier": p["tier"]} for p in bitems[:3]]}
                         for cname, cn, bitems in cl[:5]],
            "top": [{"title": r["title"], "url": link(r), "journal": r["journal"],
                     "tier": r["tier"], "date": r["pub_date"], "score": r["score"]}
                    for r in sorted(items, key=lambda x: -x["score"])[:5]],
        }
    auto_html = "\n".join(dir_blocks)

    # ---------- 深度综述（可选注入） ----------
    synth_path = Path(a.synth) if a.synth else (SYNTHDIR / f"{tag}.md")
    if not synth_path.is_absolute():
        synth_path = ROOT / synth_path
    if synth_path.exists():
        body = md_to_html(synth_path.read_text(encoding="utf-8"))
        deep_html = (f'<div class="wk-card syn-deep"><h2>本期综述 · 各领域主要进展</h2>'
                     f'<div class="syn-body">{body}</div>'
                     f'<p class="sub" style="margin-top:12px">下方为数据驱动的自动综述，'
                     f'按池内条目逐方向列出主题簇与代表文献，与上文互为印证。</p></div>')
        synth_src = f"深度综述来源：{esc(synth_path.name)}"
    else:
        deep_html = ('<div class="wk-card"><h2>本期综述 · 各领域主要进展</h2>'
                     '<p class="sub">本期未提供人工/模型撰写的深度综述，'
                     f'以下为自动综述。撰写方式：编辑 <code>weekly/synth/{tag}.md</code> 后'
                     '运行 <code>py -3 weekly_report.py --end '
                     f'{end.isoformat()} --days {a.days}</code> 即可注入。</p></div>')
        synth_src = "本期仅有自动综述"

    # ---------- 写作草稿 ----------
    if not a.no_draft:
        lines = [f"# {tag} 综述写作草稿（数据驱动，供撰写 weekly/synth/{tag}.md）", "",
                 f"窗口 {start} ~ {end} · 池内 {len(rows)} 条 · 综述样本 {len(clean)} 条",
                 f"S/A {len(high)} · 预印本 {preprints} · 预警/受限 {warned} · 降权 {len(offs)}", ""]
        for d in DIR_ORDER:
            g = dir_digest.get(d) or {}
            if not g.get("n"):
                lines += [f"## {d}（0 条）", ""]
                continue
            lines.append(f"## {d}（池内 {g['n']} 条 · 样本 {g['sample']} · S/A {g['sa']}）")
            lines.append("期刊：" + "、".join(f"{x['j']}({x['n']})" for x in g["journals"]))
            lines.append("主题簇：" + "、".join(f"{c['name']}({c['n']})" for c in g["clusters"]))
            lines.append("代表文献：")
            for r in g["top"]:
                lines.append(f"- [{r['tier']}] {r['title']} — {r['journal']}（{r['date']}）{r['url']}")
            lines.append("")
        (SYNTHDIR / f"{tag}.draft.md").write_text("\n".join(lines), encoding="utf-8")

    # ---------- 统计页渲染 ----------
    def bars_html(counter, color="#378ADD"):
        if not counter:
            return ""
        mx = max(counter.values())
        return "".join(
            f'<tr><td>{k}</td><td style="text-align:right">{v}</td>'
            f'<td><span style="display:inline-block;height:9px;width:{round(v*100/mx)}%;'
            f'background:{color};border-radius:2px"></span></td></tr>' for k, v in counter)

    dir_rows = bars_html(Counter({DIR_NAMES.get(int(k), k): v for k, v in sorted(dirs.items())
                                  if k and str(k).isdigit()}))
    tier_rows = "".join(
        f'<tr><td>{t}</td><td style="text-align:right">{tiers.get(t,0)}</td>'
        f'<td><span style="display:inline-block;height:9px;width:'
        f'{round(tiers.get(t,0)*100/max(tiers.values()))}%;background:#1D9E75;border-radius:2px">'
        f'</span></td></tr>' for t in TIER_ORDER if tiers.get(t))
    journal_rows = "".join(f'<tr><td>{esc(j) or "—"}</td><td style="text-align:right">{n}</td></tr>'
                           for j, n in journals.most_common(15))
    warn_rows = "".join(f'<tr><td>{esc(j) or "—"}</td><td style="text-align:right">{n}</td></tr>'
                        for j, n in warn_journals.most_common(10))
    top_rows = "".join(
        f'<li><a href="{esc(link(r) or "#")}" target="_blank" rel="noopener">'
        f'{esc(r["title"][:150])}</a><br><span class="sub">{esc(r["journal"] or "—")} · '
        f'{esc(r["pub_date"])} · 等级 {esc(r["tier"])} · 评分 {r["score"]}</span></li>'
        for r in top_scored)
    word_cloud = " · ".join(f'{esc(w)}<span class="sub">({n})</span>' for w, n in top_words)

    stats = {
        "week": tag, "start": start.isoformat(), "end": end.isoformat(),
        "pool_total": len(rows), "tiers": dict(tiers), "directions": dict(dirs),
        "warned": warned, "preprints": preprints, "off_penalized": len(offs),
        "top_journals": journals.most_common(20), "top_words": top_words,
        "high_tier_count": len(high), "synthesis_source": synth_src,
        "dir_digest": dir_digest,
    }
    (OUTDIR / f"{tag}.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1),
                                        encoding="utf-8")

    nav = ('<nav><a href="../index.html">首页</a><a href="../frontier.html">前沿跟踪</a>'
           '<a href="index.html" class="active">前沿周报</a>'
           '<a href="../archive.html">全部归档</a></nav>')
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
 .syn-deep{{border-color:#cfd9e6;background:#fbfdff;}}
 .syn-deep h2{{color:#12457a;}}
 .syn-body h2{{font-size:15px;margin:16px 0 6px;color:#12457a;}}
 .syn-body h3{{font-size:14px;margin:13px 0 5px;color:#1f2937;}}
 .syn-body p{{font-size:13.5px;line-height:1.75;margin:6px 0;}}
 .syn-body a{{color:#12457a;}}
 .syn-quote{{background:#f6f8fa;border-left:3px solid #378ADD;border-radius:6px;
   padding:8px 12px;color:#3b4653;font-size:13px;line-height:1.7;}}
 .syn-dir{{border-top:1px solid #eef1f5;padding:12px 0 6px;}}
 .syn-dir:first-child{{border-top:none;padding-top:0;}}
 .syn-dir h3{{font-size:14.5px;margin:0 0 4px;color:#1f2937;}}
 .syn-meta{{font-size:13px;color:#445261;margin:2px 0 8px;}}
 .syn-clu{{margin:6px 0 10px;}}
 .syn-clu-h{{font-size:13.5px;color:#12457a;}}
 .syn-clu-h b{{font-weight:600;}}
 ul.syn-ul{{margin:3px 0 0;padding-left:20px;font-size:13px;line-height:1.6;color:#3b4653;}}
 ul.syn-ul a{{color:#12457a;text-decoration:none;}}
 ul.syn-ul a:hover{{text-decoration:underline;}}
 .syn-note{{margin-top:6px;}}
</style></head><body>
<header class="site-header">
  <h1><a href="../index.html">🌊 海洋AI技术日报</a></h1>
  <p>前沿周报 · {start} 至 {end} · 池内 {len(rows)} 条</p>
  {nav}
</header>
<main class="wk-wrap">
  <div class="wk-card"><h2>本周概览</h2>
    <div class="kv">
      <div><span class="sub">池内总量</span><b>{len(rows)}</b></div>
      <div><span class="sub">S/A 级</span><b>{len(high)}</b></div>
      <div><span class="sub">预印本</span><b>{preprints}</b></div>
      <div><span class="sub">预警/受限刊</span><b>{warned}</b></div>
      <div><span class="sub">降权项</span><b>{len(offs)}</b></div>
    </div>
    <p class="sub" style="margin-top:10px">预印本与预警刊均计入池内并标注，未从统计中剔除，便于观察占比变化；
    综述板块仅采用非预警、非降权条目（样本 {len(clean)} 条），口径与前沿看板一致。</p>
  </div>

  {deep_html}

  <div class="wk-card"><h2>自动综述 · 逐方向主题簇与代表文献</h2>
    <p class="sub">按标题关键词聚类，仅列出现 ≥2 篇的主题簇；每条最多列 3 篇代表文献（按评分排序）。</p>
    {auto_html}
  </div>

  <div class="wk-card"><h2>方向分布</h2><table class="wk">{dir_rows}</table></div>
  <div class="wk-card"><h2>期刊分级分布</h2><table class="wk">{tier_rows}</table>
    <p class="sub">S = Nature/Science/PNAS 正刊及顶级子刊；A = 领域权威；B = 主流 SCI；C = 一般/新刊；P = 预印本；D = 预警/受限。</p></div>
  <div class="wk-card"><h2>高频期刊（已排除预警刊）</h2><table class="wk">{journal_rows}</table></div>
  <div class="wk-card"><h2>预警/受限期刊（仅供取舍，不代表否定其成果）</h2><table class="wk">{warn_rows or '<tr><td>本周无</td><td></td></tr>'}</table></div>
  <div class="wk-card"><h2>标题主题词</h2><p style="font-size:13.5px;line-height:1.9">{word_cloud}</p></div>
  <div class="wk-card"><h2>本周高评分条目（Top 15）</h2><ol>{top_rows}</ol></div>
</main></body></html>"""
    (OUTDIR / f"{tag}.html").write_text(html, encoding="utf-8")
    idx = write_index()
    print(f"周报已生成：weekly/{tag}.html（池内 {len(rows)} 条 · S/A {len(high)} · 预警 {warned} "
          f"· 综述样本 {len(clean)} 条 · {synth_src}）")
    print(f"统计摘要：weekly/{tag}.json")
    if idx:
        print(f"索引页已更新：weekly/index.html")
    if not a.no_draft:
        print(f"综述草稿：weekly/synth/{tag}.draft.md")


if __name__ == "__main__":
    main()
