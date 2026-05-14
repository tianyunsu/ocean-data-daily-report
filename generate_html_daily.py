# -*- coding: utf-8 -*-
from datetime import datetime
import os

# 从 feishu_write_doc.py 导入 SECTIONS
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()
exec(content.split('def tr')[0])

today = datetime.now().strftime('%Y年%m月%d日')
today_date = datetime.now().strftime('%Y-%m-%d')
total_items = sum(len(s['items']) for s in SECTIONS)

icons = ['🤖', '🌐', '📊', '✅', '⚙️', '🗄️', '🚢', '🏛️', '🛠️']

nav_links = ''
for i, s in enumerate(SECTIONS):
    title_part = s['title'].split('、')[1] if '、' in s['title'] else s['title'][1:]
    nav_links += f'    <a class="nav-link" href="#section-{i+1}">{icons[i]} {title_part}</a>\n'

sections_html = ''
for i, s in enumerate(SECTIONS):
    items_html = ''
    for item in s['items']:
        badge = item.get('badge', '')
        title = item.get('title', '')
        abstract = item.get('abstract', '')
        source = item.get('source', '')
        date = item.get('date', '')
        url = item.get('url', '')

        badge_html = f'            <span class="item-badge">{badge}</span>\n' if badge else ''
        source_html = f'            <span>📍 来源：{source}</span>\n' if source else ''
        date_html = f'            <span>📅 {date}</span>\n' if date else ''
        url_html = f'            <span>🔗 <a href="{url}" target="_blank">原文链接</a></span>\n' if url else ''

        items_html += f'''        <div class="item">
          <div class="item-header">
{badge_html}            <div class="item-title"><a href="{url}" target="_blank">{title}</a></div>
          </div>
          <div class="item-abstract">{abstract}</div>
          <div class="item-meta">
{source_html}{date_html}{url_html}          </div>
        </div>
'''

    sections_html += f'''    <div class="section" id="section-{i+1}">
      <div class="section-header">
        <span class="section-icon">{icons[i]}</span>
        <div>
          <div class="section-title">{s["title"]}</div>
          <div class="section-meta">{s["en"]}</div>
        </div>
        <span class="section-badge">{len(s["items"])} 条</span>
      </div>
      <div class="section-content">
{items_html}      </div>
    </div>
'''

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI技术日报 · {today}</title>
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
  }}
  .nav-link {{
    color: rgba(255,255,255,0.75);
    text-decoration: none;
    font-size: 0.78em;
    padding: 4px 10px;
    border-radius: 15px;
    transition: all 0.2s;
  }}
  .nav-link:hover {{
    background: rgba(0,168,181,0.3);
    color: #fff;
  }}
  .container {{
    max-width: 1000px;
    margin: 30px auto;
    padding: 0 15px;
  }}
  .section {{
    background: var(--card-bg);
    border-radius: 16px;
    margin-bottom: 24px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(0,0,0,0.12);
  }}
  .section-header {{
    background: linear-gradient(135deg, var(--ocean-deep) 0%, var(--ocean-mid) 100%);
    padding: 20px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .section-icon {{ font-size: 1.8em; }}
  .section-title {{
    color: #fff;
    font-size: 1.15em;
    font-weight: 700;
  }}
  .section-meta {{
    color: rgba(255,255,255,0.65);
    font-size: 0.78em;
    margin-top: 2px;
  }}
  .section-badge {{
    background: var(--ocean-teal);
    color: #fff;
    font-size: 0.7em;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 12px;
    margin-left: auto;
    white-space: nowrap;
  }}
  .section-content {{ padding: 0; }}
  .item {{
    padding: 18px 24px;
    border-bottom: 1px solid var(--border-light);
    transition: background 0.2s;
  }}
  .item:last-child {{ border-bottom: none; }}
  .item:hover {{ background: var(--ocean-foam); }}
  .item-header {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 8px;
  }}
  .item-badge {{
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: #fff;
    font-size: 0.68em;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 10px;
    white-space: nowrap;
  }}
  .item-title {{
    color: var(--ocean-deep);
    font-size: 0.95em;
    font-weight: 600;
    line-height: 1.45;
    flex: 1;
  }}
  .item-title a {{
    color: var(--ocean-mid);
    text-decoration: none;
    transition: color 0.2s;
  }}
  .item-title a:hover {{ color: var(--ocean-teal); text-decoration: underline; }}
  .item-abstract {{
    color: var(--text-muted);
    font-size: 0.85em;
    line-height: 1.65;
    margin: 8px 0;
  }}
  .item-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 0.75em;
    color: var(--text-muted);
  }}
  .item-meta span {{
    display: flex;
    align-items: center;
    gap: 4px;
  }}
  .item-meta a {{
    color: var(--ocean-light);
    text-decoration: none;
  }}
  .item-meta a:hover {{ text-decoration: underline; }}
  .footer {{
    text-align: center;
    padding: 30px 20px;
    color: rgba(255,255,255,0.5);
    font-size: 0.8em;
  }}
  @media (max-width: 768px) {{
    .header h1 {{ font-size: 1.6em; }}
    .nav-bar {{ gap: 5px; }}
    .nav-link {{ font-size: 0.7em; padding: 3px 8px; }}
    .item {{ padding: 14px 16px; }}
  }}
</style>
</head>
<body>
  <div class="header">
    <div class="header-badge">OCEAN AI DAILY</div>
    <h1>海洋AI技术日报</h1>
    <div class="subtitle">报告日期：{today} | 来源：Nature Communications / NOAA / Copernicus / IOCCG / Springer 等 | 自动生成</div>
    <div class="summary-bar">
      <div class="summary-chip"><strong>{len(SECTIONS)}</strong> 个研究方向</div>
      <div class="summary-chip"><strong>{total_items}</strong> 条精选动态</div>
      <div class="summary-chip">覆盖 AI · 数字孪生 · 可视化 · 数据...</div>
    </div>
  </div>
  <nav class="nav-bar">
{nav_links}  </nav>
  <div class="container">
{sections_html}  </div>
  <div class="footer">
    本简报每日自动生成，仅供学术参考。版权归原作者/机构所有。
  </div>
</body>
</html>
'''

output_path = f'daily_reports/海洋AI简报_{today_date}.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'HTML日报已生成: {output_path}')
print(f'总计: {len(SECTIONS)} 个方向, {total_items} 条内容')
