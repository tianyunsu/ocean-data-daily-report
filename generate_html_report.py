#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate HTML report from feishu_write_doc.py SECTIONS data"""
import sys
sys.path.insert(0, r'C:\Users\Administrator\WorkBuddy\Claw')

from datetime import datetime
import importlib.util

# Load SECTIONS from feishu_write_doc.py
spec = importlib.util.spec_from_file_location('fw', r'C:\Users\Administrator\WorkBuddy\Claw\feishu_write_doc.py')
fw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fw)

sections = fw.SECTIONS
icons = ['\U0001f916','\U0001f310','\U0001f4ca','\u2705','\u2699\ufe0f','\U0001f5c4\ufe0f','\U0001f6a2','\U0001f3db\ufe0f','\U0001f6e0\ufe0f']
total = sum(len(s['items']) for s in sections)
today = datetime.now()
date_str = today.strftime('%Y\u5e74%m\u6708%d\u65e5')
date_iso = today.strftime('%Y-%m-%d')
time_str = today.strftime('%Y-%m-%d %H:%M:%S')

# Read template CSS from existing file
template_path = r'C:\Users\Administrator\WorkBuddy\Claw\daily_reports\海洋AI简报_2026-05-09.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Extract CSS from template
css_start = template.find('<style>') + 7
css_end = template.find('</style>')
css = template[css_start:css_end]

# Build nav chips
nav_chips = ''
for i, s in enumerate(sections):
    nav_chips += f'<a href="#section-{i+1}" class="nav-chip">{icons[i]} {s["title"]}</a>'

# Build sections
sections_html = ''
for idx, section in enumerate(sections):
    icon = icons[idx]
    count = len(section['items'])
    items_html = ''
    for j, item in enumerate(section['items'], 1):
        title_text = item['title']
        abstract_text = item['abstract']
        source_text = item['source']
        date_text = item['date']
        url_text = item['url']
        badge = item.get('badge', '')
        items_html += f'''        <div class="item-card">
          <div class="item-title">
            <span class="item-badge">{badge}</span>
            <a href="{url_text}" target="_blank" rel="noopener">{j}. {title_text}</a>
          </div>
          <div class="item-abstract">{abstract_text}</div>
          <div class="item-meta">
            <span class="meta-source">{source_text}</span>
            <span class="meta-date">{date_text}</span>
            <a href="{url_text}" target="_blank" class="meta-link" rel="noopener">原文链接</a>
          </div>
        </div>
'''
    sections_html += f'''  <section class="section" id="section-{idx+1}">
    <div class="section-header">
      <span class="section-icon">{icon}</span>
      <div>
        <div class="section-title">{section['title']}</div>
        <div class="section-en">{section.get('en', '')}</div>
      </div>
      <div class="section-count">{count} 条</div>
    </div>
    <div class="section-items">
      {items_html}
    </div>
  </section>
'''

final_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI技术日报 · {date_str}</title>
<style>{css}</style>
</head>
<body>
<div class="header">
  <div class="header-badge">OCEAN AI DAILY</div>
  <h1>海洋AI技术<span>日报</span></h1>
  <div class="subtitle">报告日期：{date_str} | 来源：科学网 / 腾讯新闻 / Springer / ESSD / Copernicus / NOAA / NCEI / IOCCG 等 | 自动生成</div>
  <div class="summary-bar">
    <div class="summary-chip"><strong>9</strong> 个研究方向</div>
    <div class="summary-chip"><strong>{total}</strong> 条精选动态</div>
    <div class="summary-chip">覆盖 AI · 数字孪生 · 可视化 · 数据质量 · 数据处理 · 共享服务 · 开放航次 · 数据中心 · 工具</div>
  </div>
</div>
<nav class="nav-bar">{nav_chips}</nav>
<div class="container">
{sections_html}
  <div class="footer">
    本简报每日自动生成，仅供学术参考。版权归原作者/机构所有。<br>
    生成时间：{time_str}
  </div>
</div>
</body>
</html>'''

outpath = rf'C:\Users\Administrator\WorkBuddy\Claw\daily_reports\海洋AI简报_{date_iso}.html'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(final_html)
print(f'HTML generated: {outpath}')
print(f'Total items: {total}')
for i, s in enumerate(sections):
    print(f'  Section {i+1}: {s["title"][:10]}... - {len(s["items"])} items')
