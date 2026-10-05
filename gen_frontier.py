#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gen_frontier.py — 前沿跟踪看板（L3）外壳生成器

背景：`frontier.html` 是「全量文献池可检索看板」，前端 `fetch('data/pool_index.json')`
动态渲染，故其**外壳**（导航 / 筛选控件 / CSS / JS / 口径说明）长期静态。
此前该外壳由 2026-09-20 一次手工落地后即无生成脚本，存在「丢失即无法复现」的风险
（苏老师 2026-10-05 指出，要求补建）。

本脚本职责（幂等，仅在外壳内容变化时写盘）：
  1. 读取 `data/pool_index.json` 的 window_days / total_pool / board_count / generated，
     把「近 N 天」「池内共 X 条」等**动态口径**同步进外壳；
  2. 生成完整 `frontier.html`（含首页/前沿跟踪/前沿周报/全部归档四处导航）；
  3. 若 `data/pool_index.json` 缺失，给出明确提示（须先跑 harvest.py + screen.py）。

用法：
    py -3 gen_frontier.py                 # 用默认 data/pool_index.json
    py -3 gen_frontier.py --index data/pool_index.json --out frontier.html

注意：本脚本只生成「外壳」，不产出数据；数据由 L0/L1（harvest.py + screen.py）产出。
"""

import argparse
import datetime as _dt
import json
import os
import sys

TOKENS = {
    "__WINDOW__": "14",
    "__GENERATED__": "",
    "__TOTAL__": "0",
    "__BOARD__": "0",
    "__BUILT__": "",
    "__OPT_WINDOW__": "",
}

# ---------------------------------------------------------------------------
# 外壳模板（raw string：CSS 中的 `.t-\?` 等反斜杠原样保留；
# 占位符用 __XXX__ 而非 str.format，以免与 CSS/JS 的花括号冲突）
# ---------------------------------------------------------------------------
TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI前沿跟踪</title>
<link rel="stylesheet" href="style.css">
<style>
  .fw-controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:18px 0;}
  .fw-controls input[type=search]{flex:1 1 240px;min-width:200px;padding:8px 10px;border:1px solid #d9dde3;border-radius:8px;font-size:14px;}
  .fw-controls select{padding:8px 10px;border:1px solid #d9dde3;border-radius:8px;font-size:14px;background:#fff;}
  .fw-stats{display:flex;flex-wrap:wrap;gap:16px;font-size:13px;color:#5b6472;margin-bottom:10px;}
  .fw-stats b{font-weight:600;color:#1f2937;}
  .fw-list{display:flex;flex-direction:column;gap:10px;}
  .fw-item{border:1px solid #e6e9ee;border-radius:10px;padding:12px 14px;background:#fff;}
  .fw-item h3{margin:0 0 6px;font-size:15px;font-weight:600;line-height:1.45;}
  .fw-item h3 a{color:#12457a;text-decoration:none;}
  .fw-item h3 a:hover{text-decoration:underline;}
  .fw-meta{font-size:12.5px;color:#5b6472;display:flex;flex-wrap:wrap;gap:10px;}
  .fw-badge{display:inline-block;padding:1px 7px;border-radius:999px;font-size:11.5px;font-weight:600;}
  .t-S{background:#e8f0fe;color:#12457a;}
  .t-A{background:#e6f4ec;color:#1c6b41;}
  .t-B{background:#eef2f6;color:#445261;}
  .t-C{background:#f4f1ea;color:#6b5b3a;}
  .t-P{background:#f3eefc;color:#5b4a8a;}
  .t-D{background:#fdecec;color:#a52a2a;}
  .t-\?{background:#f1f1f1;color:#666;}
  .fw-warn{background:#fdecec;color:#a52a2a;}
  .fw-new{background:#e8f0fe;color:#12457a;}
  .fw-pre{background:#eaf7ef;color:#1f6b45;}
  .fw-off{background:#f2f3f5;color:#6b7280;}
  .fw-weak{background:#fdf6e3;color:#8a6d1f;}
  .fw-note{font-size:12.5px;color:#7a828e;margin:14px 0 0;line-height:1.6;}
  .fw-empty{padding:30px;text-align:center;color:#7a828e;font-size:14px;}
  .fw-built{font-size:12px;color:#8a93a0;margin-top:18px;border-top:1px solid #eef0f3;padding-top:10px;}
</style>
</head>
<body>
<header class="site-header">
  <h1><a href="index.html">🌊 海洋AI技术日报</a></h1>
  <p>海洋AI前沿跟踪看板 · 全量文献池可检索 · 分级标注预警期刊</p>
  <nav>
    <a href="index.html">首页</a>
    <a href="frontier.html" class="active">前沿跟踪</a>
    <a href="weekly/index.html">前沿周报</a>
    <a href="archive.html">全部归档</a>
  </nav>
</header>

<main class="container">
  <h2 style="font-size:18px;margin:6px 0 4px;">前沿跟踪 · 近 __WINDOW__ 天文献池</h2>
  <p style="font-size:13px;color:#5b6472;margin:0;">
    日报是精选摘要（每方向 3–5 条），这里承载<b>全部检索结果</b>，按期刊等级排序。
    预警与受限期刊强制置底并标注，仅供取舍参考，不代表否定其全部成果。
  </p>

  <div class="fw-controls">
    <input type="search" id="q" placeholder="搜索标题 / 期刊 / 机构 / DOI…">
    <select id="dir"><option value="">全部方向</option></select>
    <select id="tier">
      <option value="">全部分级</option>
      <option value="S">S 顶刊</option>
      <option value="A">A 领域权威</option>
      <option value="B">B 主流 SCI</option>
      <option value="C">C 一般/新刊</option>
      <option value="P">P 预印本</option>
      <option value="D">D 预警/受限</option>
      <option value="?">未登记</option>
    </select>
    <select id="days">
__OPT_WINDOW__
      <option value="7">近 7 天</option>
      <option value="3">近 3 天</option>
      <option value="0">全部</option>
    </select>
    <select id="fit">
      <option value="clean" selected>排除降权项（默认）</option>
      <option value="title">仅标题即海洋主题</option>
      <option value="weak">仅弱相关（需人工判断）</option>
      <option value="off">仅被降权项（复核用）</option>
      <option value="">全部（含降权项）</option>
    </select>
    <select id="sort">
      <option value="score">按综合评分</option>
      <option value="date">按日期</option>
      <option value="cited">按被引</option>
    </select>
    <label style="font-size:13px;color:#5b6472;display:flex;align-items:center;gap:5px;">
      <input type="checkbox" id="onlyNew"> 仅未收录过
    </label>
    <label style="font-size:13px;color:#5b6472;display:flex;align-items:center;gap:5px;">
      <input type="checkbox" id="hideWarn"> 隐藏预警刊
    </label>
  </div>

  <div class="fw-stats" id="stats"></div>
  <div class="fw-list" id="list"><div class="fw-empty">加载中…</div></div>
  <p class="fw-note">
    分级口径：S = Nature/Science/PNAS 正刊及顶级子刊；A = 学会旗舰刊与高影响力子刊；
    B = 主流 SCI（含中文刊学科影响因子前 25%）；C = 一般期刊/新刊/开放获取集团刊；
    P = 预印本（**若已对应期刊论文则按该刊等级排序**，标注「预印本」）；
    D = MDPI 等预警集团刊、中科院/中信所预警名单、SCI(SCIE)/EI 剔除刊（强制标注，可一键隐藏）。
    自动评级项标有「未登记，待校准」。<br>
    海洋契合度：「标题即海洋主题」= 标题含 ocean/marine/coastal/sea-ice 等研究对象词；
    「弱相关」= 仅摘要出现海洋词，需人工判断；「海洋介质型」= 海水/水仅作实验介质
    （材料、化学、医学等），已降权，默认不显示但**不删除**，可用筛选调出复核。
  </p>
  <p class="fw-built">数据日期：__GENERATED__ ｜ 池内 __TOTAL__ 条 ｜ 看板展示 __BOARD__ 条 ｜ 外壳生成于 __BUILT__</p>
</main>

<script>
const DIRS = {1:'一、海洋人工智能',2:'二、海洋数字孪生',3:'三、海洋可视化',4:'四、海洋数据质量',
  5:'五、海洋数据处理',6:'六、数据管理与共享',7:'七、开放航次与科考',8:'八、海洋数据中心',
  9:'九、工具与代码资源'};
const TIER_LABEL = {S:'S 顶刊',A:'A 领域权威',B:'B 主流 SCI',C:'C 一般/新刊',P:'P 预印本',D:'D 预警/受限','?':'未登记'};
let DATA = [], TODAY = '';

const el = id => document.getElementById(id);
const sel = el('dir');
Object.keys(DIRS).forEach(k => {
  const o = document.createElement('option'); o.value = k; o.textContent = DIRS[k]; sel.appendChild(o);
});

function daysAgo(d){
  if(!d) return 999;
  const a = new Date(d + 'T00:00:00'), b = new Date(TODAY + 'T00:00:00');
  return Math.round((b - a) / 86400000);
}
function esc(s){ return (s||'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

function render(){
  const q = el('q').value.trim().toLowerCase();
  const dir = el('dir').value, tier = el('tier').value;
  const days = parseInt(el('days').value, 10);
  const onlyNew = el('onlyNew').checked, hideWarn = el('hideWarn').checked;
  const fit = el('fit').value;
  const sort = el('sort').value;

  let rows = DATA.filter(r => {
    if(q && !((r.t+' '+(r.j||'')+' '+(r.inst||'')+' '+(r.doi||'')).toLowerCase().includes(q))) return false;
    if(dir && String(r.dir) !== dir) return false;
    if(tier && r.tier !== tier) return false;
    if(days > 0 && daysAgo(r.d) > days) return false;
    if(onlyNew && !r.new) return false;
    if(hideWarn && r.tier === 'D') return false;
    if(fit === 'clean' && (r.fit||'') !== 'title') return false;  // 默认只留"标题即海洋主题"
    if(fit === 'title' && (r.fit||'') !== 'title') return false;
    if(fit === 'weak' && (r.fit||'') !== 'weak') return false;
    if(fit === 'off' && (r.fit||'') !== 'off') return false;
    return true;
  });
  if(sort === 'date') rows.sort((a,b) => (b.d||'').localeCompare(a.d||''));
  else if(sort === 'cited') rows.sort((a,b) => (b.cited||0) - (a.cited||0));
  else rows.sort((a,b) => b.score - a.score);

  const cnt = {};
  rows.forEach(r => cnt[r.tier] = (cnt[r.tier]||0) + 1);
  el('stats').innerHTML = '共 <b>' + rows.length + '</b> 条' +
    ['S','A','B','C','P','D','?'].filter(t => cnt[t]).map(t =>
      ' · ' + TIER_LABEL[t] + ' <b>' + cnt[t] + '</b>').join('');

  if(!rows.length){ el('list').innerHTML = '<div class="fw-empty">没有符合条件的记录，试试放宽筛选条件。</div>'; return; }
  el('list').innerHTML = rows.map(r => {
    const warn = r.tier === 'D';
    const badges = ['<span class="fw-badge t-' + r.tier + '">' + TIER_LABEL[r.tier] + '</span>'];
    if(r.new) badges.push('<span class="fw-badge fw-new">未收录过</span>');
    if(r.pre) badges.push('<span class="fw-badge fw-pre">预印本·已按期刊等级</span>');
    if(r.fit === 'off') badges.push('<span class="fw-badge fw-off">海洋介质型/弱相关</span>');
    if(r.fit === 'weak') badges.push('<span class="fw-badge fw-weak">弱相关</span>');
    if(warn) badges.push('<span class="fw-badge fw-warn">' + esc((r.flags||[])[0] || '预警/受限').slice(0,26) + '</span>');
    return '<div class="fw-item"><h3><a href="' + esc(r.url || ('https://doi.org/' + r.doi)) +
      '" target="_blank" rel="noopener">' + esc(r.t) + '</a></h3><div class="fw-meta">' +
      badges.join(' ') + '<span>' + esc(r.j || '—') + (r.p ? ' · ' + esc(r.p) : '') + '</span>' +
      '<span>' + (r.d || '—') + '</span><span>' + esc(DIRS[r.dir] || '') + '</span>' +
      (r.cited ? '<span>被引 ' + r.cited + '</span>' : '') +
      (r.inst ? '<span>' + esc(r.inst) + '</span>' : '') +
      (r.doi ? '<span>DOI: ' + esc(r.doi) + '</span>' : '') + '</div></div>';
  }).join('');
}

['q','dir','tier','days','sort','onlyNew','hideWarn','fit'].forEach(id =>
  el(id).addEventListener('input', render));

fetch('data/pool_index.json').then(r => r.json()).then(d => {
  DATA = d.items || []; TODAY = d.generated || '';
  el('stats').innerHTML = '池内共 <b>' + (d.total_pool||0) + '</b> 条，看板展示 <b>' + DATA.length + '</b> 条 · 数据日期 ' + TODAY;
  render();
}).catch(() => {
  el('list').innerHTML = '<div class="fw-empty">尚未生成文献池数据，请先执行采集与筛选。</div>';
});
</script>
</body>
</html>
"""


def load_index(path):
    """读取 pool_index.json；缺失时返回 None。"""
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_html(idx):
    """依据 pool_index.json 渲染外壳。idx 可为 None（此时用占位口径）。"""
    if idx:
        window = int(idx.get("window_days") or 14)
        generated = str(idx.get("generated") or "")
        total = int(idx.get("total_pool") or 0)
        board = int(idx.get("board_count") or len(idx.get("items") or []))
    else:
        window, generated, total, board = 14, "", 0, 0

    tokens = dict(TOKENS)
    tokens["__WINDOW__"] = str(window)
    tokens["__GENERATED__"] = generated or "—"
    tokens["__TOTAL__"] = str(total)
    tokens["__BOARD__"] = str(board)
    tokens["__BUILT__"] = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    # 时间窗下拉的第一项跟随 window_days
    tokens["__OPT_WINDOW__"] = '      <option value="%d">近 %d 天</option>' % (window, window)

    html = TEMPLATE
    for k, v in tokens.items():
        html = html.replace(k, v)
    return html


def write_if_changed(path, content):
    """幂等写盘：内容相同则不写。返回 True 表示已更新。"""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
        if old == content:
            return False
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return True


def main():
    ap = argparse.ArgumentParser(description="生成前沿跟踪看板外壳 frontier.html")
    ap.add_argument("--index", default=os.path.join("data", "pool_index.json"),
                    help="pool_index.json 路径（默认 data/pool_index.json）")
    ap.add_argument("--out", default="frontier.html", help="输出 HTML 路径（默认 frontier.html）")
    args = ap.parse_args()

    idx = load_index(args.index)
    if idx is None:
        print("[warn] 未找到 %s —— 请先执行 harvest.py + screen.py 生成池数据；"
              "本次将按占位口径（近 14 天 / 0 条）生成外壳。" % args.index, file=sys.stderr)

    html = build_html(idx)
    changed = write_if_changed(args.out, html)

    w = int(idx.get("window_days") or 14) if idx else 14
    total = int(idx.get("total_pool") or 0) if idx else 0
    items = len(idx.get("items") or []) if idx else 0
    print("[ok] %s %s ｜ 时间窗 近 %d 天 ｜ 池内 %d 条 ｜ 展示 %d 条"
          % (args.out, "已更新" if changed else "无变化（幂等跳过）", w, total, items))


if __name__ == "__main__":
    main()
