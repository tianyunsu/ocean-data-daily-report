#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate HTML from feishu_write_doc.py SECTIONS (by AST parsing, avoids import)"""
import ast, json, sys, os

# Parse SECTIONS from feishu_write_doc.py
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()
tree = ast.parse(content)
sections = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == 'SECTIONS':
                sections = ast.literal_eval(node.value)
                break
    if sections:
        break

if not sections:
    print('ERROR: SECTIONS not found')
    sys.exit(1)

TODAY = '2026-09-04'
TODAY_CN = '2026年09月04日'

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI技术日报 · ''' + TODAY_CN + '''</title>
<style>
  :root {
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
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #001a33 0%, #003366 40%, #004d80 100%);
    min-height: 100vh;
    color: var(--text-dark);
  }
  .header {
    background: linear-gradient(135deg, #001428 0%, #003366 50%, #00254d 100%);
    padding: 40px 20px 30px;
    text-align: center;
    border-bottom: 3px solid var(--ocean-teal);
    position: relative;
    overflow: hidden;
  }
  .header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 100'%3E%3Cpath fill='%2300a8b5' fill-opacity='0.07' d='M0,50 C360,100 720,0 1080,50 C1260,75 1350,62 1440,50 L1440,100 L0,100 Z'/%3E%3C/svg%3E") bottom / cover no-repeat;
  }
  .header-badge {
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
  }
  .header h1 {
    color: white;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 1px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.3);
  }
  .header .date-line {
    color: #80c8e0;
    font-size: 13px;
    margin-top: 8px;
    letter-spacing: 0.5px;
  }
  .container {
    max-width: 880px;
    margin: 0 auto;
    padding: 24px 20px 40px;
  }
  .section {
    background: var(--card-bg);
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.15);
    overflow: hidden;
  }
  .section-header {
    background: linear-gradient(135deg, var(--ocean-deep), var(--ocean-mid));
    padding: 16px 22px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-num {
    background: var(--ocean-teal);
    color: white;
    width: 36px; height: 36px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 16px;
    flex-shrink: 0;
  }
  .section-title-cn {
    color: white;
    font-size: 17px;
    font-weight: 700;
  }
  .section-title-en {
    color: #80c8e0;
    font-size: 11px;
    margin-top: 2px;
  }
  .section-items { padding: 8px 22px 16px; }
  .section-items p { font-size: 13px; color: var(--text-muted); line-height: 1.75; }
  .item {
    border-bottom: 1px solid var(--border-light);
    padding: 14px 0;
  }
  .item:last-child { border-bottom: none; }
  .item-badge {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    margin-right: 8px;
    vertical-align: middle;
  }
  .badge-paper { background: #e3f2fd; color: #1565c0; }
  .badge-news { background: #e8f5e9; color: #2e7d32; }
  .badge-dynamic { background: #fff3e0; color: #e65100; }
  .badge-tool { background: #f3e5f5; color: #7b1fa2; }
  .badge-data { background: #e0f7fa; color: #00695c; }
  .badge-cruise { background: #fce4ec; color: #c62828; }
  .badge-report { background: #fff8e1; color: #f57f17; }
  .badge-default { background: #eceff1; color: #546e7a; }
  .item-title {
    font-size: 15px;
    font-weight: 600;
    color: var(--text-dark);
    line-height: 1.5;
    margin-bottom: 6px;
  }
  .item-title a {
    color: var(--ocean-mid);
    text-decoration: none;
    transition: color 0.2s;
  }
  .item-title a:hover { color: var(--ocean-teal); text-decoration: underline; }
  .item-abstract {
    font-size: 13px;
    color: var(--text-muted);
    line-height: 1.75;
    margin-bottom: 6px;
  }
  .item-meta {
    font-size: 11px;
    color: #90a4ae;
  }
  .item-meta span { margin-right: 12px; }
  .footer {
    text-align: center;
    padding: 24px;
    color: #80b0c8;
    font-size: 11px;
  }
  .summary-bar {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 14px 22px;
    margin-bottom: 20px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.15);
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    font-size: 12px;
    color: var(--text-muted);
  }
  .summary-bar strong { color: var(--ocean-mid); }
</style>
</head>
<body>
<div class="header">
  <div class="header-badge">Marine AI Daily Brief</div>
  <h1>海洋AI技术日报</h1>
  <div class="date-line">''' + TODAY_CN + ''' · 周五</div>
</div>
<div class="container">
<div class="summary-bar">
  <span>本期共 <strong>''' + str(sum(len(s['items']) for s in sections)) + '''</strong> 条动态</span>
  <span>|</span>
  <span>覆盖 <strong>''' + str(sum(1 for s in sections if s['items'])) + '''</strong> 个方向</span>
  <span>|</span>
  <span>日期范围：''' + TODAY_CN + '''</span>
</div>
'''

badge_map = {
    '[论文]': 'badge-paper',
    '[要闻]': 'badge-news',
    '[动态]': 'badge-dynamic',
    '[工具]': 'badge-tool',
    '[数据]': 'badge-data',
    '[航次]': 'badge-cruise',
    '[报告]': 'badge-report',
    '[开源]': 'badge-tool',
}

for si, section in enumerate(sections, 1):
    if not section['items']:
        continue
    html += '<div class="section">\n'
    html += '  <div class="section-header">\n'
    html += f'    <div class="section-num">{si}</div>\n'
    html += '    <div>\n'
    html += f'      <div class="section-title-cn">{section["title"]}</div>\n'
    html += f'      <div class="section-title-en">{section.get("en", "")}</div>\n'
    html += '    </div>\n  </div>\n'
    html += '  <div class="section-items">\n'
    
    for item in section['items']:
        badge = item.get('badge', '')
        badge_cls = badge_map.get(badge, 'badge-default')
        html += '    <div class="item">\n'
        html += f'      <div class="item-title"><span class="item-badge {badge_cls}">{badge}</span> '
        if item.get('url'):
            html += f'<a href="{item["url"]}" target="_blank">{item["title"]}</a>'
        else:
            html += item['title']
        html += '</div>\n'
        html += f'      <div class="item-abstract">{item["abstract"]}</div>\n'
        meta = []
        if item.get('source'): meta.append(item['source'])
        if item.get('date'): meta.append(item['date'])
        html += f'      <div class="item-meta">{" · ".join(meta)}</div>\n'
        html += '    </div>\n'
    
    html += '  </div>\n</div>\n'

html += '''</div>
<div class="footer">
  <p>海洋AI技术日报 · 自动生成于 ''' + TODAY_CN + '''</p>
  <p>Powered by WorkBuddy AI · Data sources: arXiv, GitHub, CMEMS, NOAA, CNKI and more</p>
</div>
</body>
</html>'''

import os
os.makedirs('daily_reports', exist_ok=True)
out_path = f'daily_reports/海洋AI简报_{TODAY}.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"HTML generated: {out_path}")
effective_items = sum(1 for s in sections for item in s['items'] if item.get('badge') != '[备注]')
note_items = sum(1 for s in sections for item in s['items'] if item.get('badge') == '[备注]')
print(f"Effective items: {effective_items} (+ {note_items} direction notes)")
print(f"Sections with content: {sum(1 for s in sections if s['items'])}")
