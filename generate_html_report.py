#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基于 feishu_write_doc.py 的 SECTIONS 数据生成 HTML 日报
"""
import sys
import os
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from feishu_write_doc import SECTIONS

yesterday = datetime.now().strftime('%Y年%m月%d日')
date_str = datetime.now().strftime('%Y-%m-%d')
today_str = datetime.now().strftime('%Y-%m-%d')

output_path = f"C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_{today_str}.html"

# 统计总条目数
total_items = sum(len(s['items']) for s in SECTIONS)

# 图标映射
SECTION_ICONS = ['🤖', '🌐', '📊', '✅', '⚙️', '🗄️', '🚢', '🏛️', '🛠️']

def badge_color(badge):
    if not badge:
        return ''
    b = badge.lower()
    if '新发' in b or '新动' in b:
        return 'badge-new'
    elif '综述' in b or '论文' in b:
        return 'badge-review'
    elif '会议' in b:
        return 'badge-conf'
    elif '政策' in b:
        return 'badge-policy'
    elif '重磅' in b:
        return 'badge-hot'
    elif '进展' in b:
        return 'badge-progress'
    elif '持续更新' in b:
        return 'badge-update'
    elif '标准' in b:
        return 'badge-standard'
    elif '开源' in b:
        return 'badge-open'
    else:
        return 'badge-default'

# 构建 HTML
items_html_list = []
for idx, sec in enumerate(SECTIONS):
    icon = SECTION_ICONS[idx] if idx < len(SECTION_ICONS) else '📌'
    items_html = ''
    for item in sec['items']:
        badge = item.get('badge', '').strip('[]').strip()
        badge_cls = badge_color(item.get('badge', ''))
        badge_html = f'<span class="item-badge {badge_cls}">{badge}</span>' if badge else ''
        abstract = item['abstract']
        source = item['source']
        date = item['date']
        url = item['url']
        title_text = item['title']
        items_html += f'''
        <div class="item-card">
          <div class="item-title">
            {badge_html}
            <a href="{url}" target="_blank" rel="noopener">{title_text}</a>
          </div>
          <div class="item-abstract">{abstract}</div>
          <div class="item-meta">
            <span class="meta-source">📰 {source}</span>
            <span class="meta-date">📅 {date}</span>
            <a href="{url}" target="_blank" class="meta-link" rel="noopener">🔗 原文链接</a>
          </div>
        </div>'''

    items_html_list.append(f'''
  <section class="section" id="section-{idx+1}">
    <div class="section-header">
      <span class="section-icon">{icon}</span>
      <div>
        <div class="section-title">{sec['title']}</div>
        <div class="section-en">{sec['en']}</div>
      </div>
      <div class="section-count">{len(sec['items'])} 条</div>
    </div>
    <div class="section-items">
      {items_html}
    </div>
  </section>''')

nav_items = ''.join(
    f'<a href="#section-{i+1}" class="nav-chip">{SECTION_ICONS[i] if i < len(SECTION_ICONS) else "📌"} {s["title"].split("、")[1] if "、" in s["title"] else s["title"]}</a>'
    for i, s in enumerate(SECTIONS)
)

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI技术日报 · {yesterday}</title>
<style>
  :root {{
    --ocean-deep: #003366;
    --ocean-mid: #005b9a;
    --ocean-light: #0082c8;
    --ocean-teal: #00a8b5;
    --ocean-foam: #e8f6fa;
    --accent-gold: #f0a500;
    --text-dark: #1a2a3a;
    --text-muted: #5a6a7a;
    --card-bg: #ffffff;
    --border-light: #c8e0ee;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #001a33 0%, #003366 40%, #004d80 100%);
    min-height: 100vh;
    color: var(--text-dark);
  }}
  .header {{
    background: linear-gradient(135deg, #001428 0%, #003366 50%, #00254d 100%);
    padding: 40px 20px 30px;
    text-align: center;
    border-bottom: 3px solid var(--ocean-teal);
    position: relative;
    overflow: hidden;
  }}
  .header::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 100'%3E%3Cpath fill='%2300a8b5' fill-opacity='0.07' d='M0,50 C360,100 720,0 1080,50 C1260,75 1350,62 1440,50 L1440,100 L0,100 Z'/%3E%3C/svg%3E") bottom / cover no-repeat;
  }}
  .header-badge {{
    display: inline-block;
    background: rgba(0,168,181,0.2);
    border: 1px solid var(--ocean-teal);
    color: var(--ocean-teal);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 14px;
    text-transform: uppercase;
  }}
  .header h1 {{
    color: #ffffff;
    font-size: 2.2em;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 8px;
    text-shadow: 0 2px 20px rgba(0,168,181,0.4);
    position: relative;
    z-index: 1;
  }}
  .header h1 span {{ color: var(--ocean-teal); }}
  .header .subtitle {{
    color: rgba(255,255,255,0.65);
    font-size: 0.95em;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
  }}
  .summary-bar {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    margin-top: 16px;
    position: relative;
    z-index: 1;
  }}
  .summary-chip {{
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.25);
    color: #e0f0ff;
    font-size: 0.82em;
    padding: 5px 14px;
    border-radius: 20px;
    font-weight: 500;
  }}
  .summary-chip strong {{ color: var(--ocean-teal); }}
  .nav-bar {{
    background: rgba(0,30,60,0.95);
    padding: 12px 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    border-bottom: 1px solid rgba(0,168,181,0.3);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
  }}
  .nav-chip {{
    background: rgba(0,91,154,0.4);
    border: 1px solid rgba(0,168,181,0.4);
    color: #a0d8ef;
    font-size: 0.78em;
    padding: 4px 12px;
    border-radius: 16px;
    text-decoration: none;
    transition: all 0.2s;
    white-space: nowrap;
  }}
  .nav-chip:hover {{
    background: rgba(0,168,181,0.3);
    color: #fff;
    border-color: var(--ocean-teal);
  }}
  .container {{
    max-width: 900px;
    margin: 0 auto;
    padding: 24px 16px 40px;
  }}
  .section {{
    background: var(--card-bg);
    border-radius: 16px;
    margin-bottom: 28px;
    box-shadow: 0 4px 24px rgba(0,30,60,0.18);
    overflow: hidden;
  }}
  .section-header {{
    background: linear-gradient(135deg, var(--ocean-deep) 0%, var(--ocean-mid) 100%);
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .section-icon {{
    font-size: 1.8em;
    flex-shrink: 0;
  }}
  .section-title {{
    color: #fff;
    font-size: 1.15em;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}
  .section-en {{
    color: rgba(255,255,255,0.55);
    font-size: 0.78em;
    margin-top: 3px;
  }}
  .section-count {{
    margin-left: auto;
    background: rgba(255,255,255,0.15);
    color: #a0d8ef;
    font-size: 0.82em;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    flex-shrink: 0;
  }}
  .section-items {{
    padding: 8px 0;
  }}
  .item-card {{
    padding: 18px 24px;
    border-bottom: 1px solid var(--border-light);
    transition: background 0.15s;
  }}
  .item-card:last-child {{ border-bottom: none; }}
  .item-card:hover {{ background: #f5faff; }}
  .item-title {{
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 8px;
    flex-wrap: wrap;
  }}
  .item-title a {{
    color: var(--ocean-mid);
    font-weight: 600;
    font-size: 0.96em;
    text-decoration: none;
    line-height: 1.5;
    flex: 1;
    min-width: 0;
  }}
  .item-title a:hover {{ color: var(--ocean-teal); text-decoration: underline; }}
  .item-badge {{
    font-size: 0.72em;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 10px;
    white-space: nowrap;
    flex-shrink: 0;
    margin-top: 2px;
  }}
  .badge-new {{ background: #e8f7f0; color: #1a7a4a; border: 1px solid #a8d8c0; }}
  .badge-review {{ background: #e8f0ff; color: #2a4aaa; border: 1px solid #a8b8e8; }}
  .badge-conf {{ background: #fff0e8; color: #a03000; border: 1px solid #e8c8a0; }}
  .badge-policy {{ background: #f8f0ff; color: #6a1a9a; border: 1px solid #d0a8e8; }}
  .badge-hot {{ background: #fff0e8; color: #c03000; border: 1px solid #f0c0a0; }}
  .badge-progress {{ background: #e8f6fa; color: #005b9a; border: 1px solid #a0d0e8; }}
  .badge-update {{ background: #f5f5f5; color: #555; border: 1px solid #ccc; }}
  .badge-standard {{ background: #fffbe8; color: #8a6000; border: 1px solid #e0d090; }}
  .badge-open {{ background: #e8ffe8; color: #1a6a1a; border: 1px solid #a0d8a0; }}
  .badge-default {{ background: #f0f4f8; color: #4a6a8a; border: 1px solid #c0d0e0; }}
  .item-abstract {{
    color: #3a4a5a;
    font-size: 0.9em;
    line-height: 1.75;
    margin-bottom: 10px;
  }}
  .item-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    font-size: 0.8em;
    color: var(--text-muted);
    align-items: center;
  }}
  .meta-source {{ color: var(--ocean-mid); font-weight: 500; }}
  .meta-date {{ color: #7a8a9a; }}
  .meta-link {{
    color: var(--ocean-teal);
    text-decoration: none;
    font-weight: 500;
    margin-left: auto;
  }}
  .meta-link:hover {{ text-decoration: underline; }}
  .footer {{
    text-align: center;
    color: rgba(255,255,255,0.45);
    font-size: 0.82em;
    padding: 20px 0 32px;
  }}
</style>
</head>
<body>
<div class="header">
  <div class="header-badge">OCEAN AI DAILY · AUTO-GENERATED</div>
  <h1>海洋AI技术<span>日报</span></h1>
  <div class="subtitle">报告日期：{yesterday} &nbsp;|&nbsp; 来源：arXiv / ScienceDirect / IOC-UNESCO / Copernicus / NSFC 等 &nbsp;|&nbsp; 自动生成</div>
  <div class="summary-bar">
    <div class="summary-chip"><strong>{len(SECTIONS)}</strong> 个研究方向</div>
    <div class="summary-chip"><strong>{total_items}</strong> 条精选动态</div>
    <div class="summary-chip">🌊 覆盖 AI · 数字孪生 · 可视化 · 数据质量 · 数据处理 · 共享服务 · 开放航次 · 数据中心 · 工具</div>
  </div>
</div>
<nav class="nav-bar">
  {nav_items}
</nav>
<div class="container">
  {''.join(items_html_list)}
  <div class="footer">
    本简报每日自动生成，仅供学术参考。版权归原作者/机构所有。<br>
    生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  </div>
</div>
</body>
</html>'''

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"[OK] HTML报告已生成: {output_path}")
print(f"     共 {len(SECTIONS)} 个方向，{total_items} 条动态")
