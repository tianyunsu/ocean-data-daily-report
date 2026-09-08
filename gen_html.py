# -*- coding: utf-8 -*-
"""Generate ocean daily report HTML from feishu_write_doc.py SECTIONS"""
import re, os, ast
from datetime import date

today = date.today()
date_str = today.strftime("%Y-%m-%d")
date_cn = today.strftime("%Y年%m月%d日")

# Read SECTIONS from feishu_write_doc.py - extract only the SECTIONS block
target = r"C:\Users\Administrator\WorkBuddy\Claw\feishu_write_doc.py"
with open(target, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract SECTIONS using bracket counting
pattern = re.compile(r'SECTIONS\s*=\s*\[')
match = pattern.search(content)
if not match:
    print("ERROR: SECTIONS not found")
    exit(1)

bracket_start = match.end() - 1
depth = 0
i = bracket_start
while i < len(content):
    if content[i] == '[':
        depth += 1
    elif content[i] == ']':
        depth -= 1
        if depth == 0:
            break
    i += 1

sections_str = content[match.start():i+1]
# Extract just the list literal
list_match = re.search(r'=\s*(\[.*\])', sections_str, re.DOTALL)
sections = ast.literal_eval(list_match.group(1))

total_items = sum(len(s.get('items', [])) for s in sections)
section_counts = [(s['title'], len(s.get('items', []))) for s in sections]

# Generate HTML
html_parts = []
html_parts.append(f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海洋AI研究日报 - {date_cn}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif; background: #f0f4f8; color: #1a202c; line-height: 1.7; }}
.container {{ max-width: 960px; margin: 0 auto; padding: 20px; }}
.header {{ background: linear-gradient(135deg, #0c4a6e 0%, #0369a1 50%, #0284c7 100%); color: white; padding: 32px 24px; border-radius: 12px; margin-bottom: 24px; text-align: center; }}
.header h1 {{ font-size: 1.8em; font-weight: 700; margin-bottom: 8px; }}
.header p {{ font-size: 0.95em; opacity: 0.9; }}
.header .stats {{ display: inline-block; background: rgba(255,255,255,0.15); padding: 4px 16px; border-radius: 20px; margin-top: 10px; font-size: 0.85em; }}
.section {{ background: white; border-radius: 10px; padding: 24px; margin-bottom: 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); border-left: 4px solid #0284c7; }}
.section h2 {{ font-size: 1.25em; color: #0c4a6e; margin-bottom: 6px; }}
.section .en {{ font-size: 0.82em; color: #64748b; margin-bottom: 16px; }}
.item {{ padding: 14px 0; border-bottom: 1px solid #e2e8f0; }}
.item:last-child {{ border-bottom: none; }}
.item h3 {{ font-size: 1.02em; color: #1e293b; margin-bottom: 6px; line-height: 1.5; }}
.item .meta {{ font-size: 0.8em; color: #64748b; margin-bottom: 8px; display: flex; gap: 12px; flex-wrap: wrap; }}
.item .meta span {{ background: #f1f5f9; padding: 2px 8px; border-radius: 4px; }}
.item .badge {{ display: inline-block; background: #0284c7; color: white; font-size: 0.75em; padding: 1px 8px; border-radius: 4px; margin-right: 6px; font-weight: 600; }}
.item .abstract {{ font-size: 0.9em; color: #475569; margin-bottom: 6px; }}
.item .source {{ font-size: 0.8em; color: #94a3b8; }}
.item a {{ color: #0369a1; text-decoration: none; font-size: 0.82em; word-break: break-all; }}
.item a:hover {{ text-decoration: underline; }}
.footer {{ text-align: center; padding: 30px 20px; color: #94a3b8; font-size: 0.85em; }}
@media (max-width: 640px) {{ .container {{ padding: 10px; }} .header {{ padding: 20px 16px; }} .section {{ padding: 16px; }} }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>海洋AI研究日报</h1>
<p>{date_cn}</p>
<div class="stats">共 {total_items} 条 · 覆盖 {sum(1 for _, c in section_counts if c > 0)}/{len(sections)} 个方向</div>
</div>
''')

for s in sections:
    items = s.get('items', [])
    html_parts.append(f'<div class="section">')
    html_parts.append(f'<h2>{s["title"]}</h2>')
    html_parts.append(f'<div class="en">{s.get("en", "")}</div>')
    for item in items:
        badge = item.get('badge', '')
        html_parts.append('<div class="item">')
        html_parts.append(f'<h3><span class="badge">{badge}</span> {item["title"]}</h3>')
        html_parts.append(f'<div class="meta"><span>{item.get("source", "")}</span><span>{item.get("date", "")}</span></div>')
        html_parts.append(f'<div class="abstract">{item.get("abstract", "")}</div>')
        url = item.get('url', '')
        if url:
            html_parts.append(f'<div><a href="{url}" target="_blank" rel="noopener">{url}</a></div>')
        html_parts.append('</div>')
    html_parts.append('</div>')

html_parts.append(f'''
<div class="footer">
<p>海洋AI研究日报 · {date_cn} · 自动生成</p>
<p>本日报覆盖海洋AI、数字孪生、可视化、数据质量、数据处理、数据管理与共享、开放航次、数据中心、工具资源9大方向</p>
</div>
</div>
</body>
</html>''')

html_content = '\n'.join(html_parts)

output_dir = r"C:\Users\Administrator\WorkBuddy\Claw\daily_reports"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, f"海洋AI简报_{date_str}.html")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML generated: {output_path}")
print(f"Total: {total_items} items across {len(sections)} sections")
for title, cnt in section_counts:
    print(f"  {title}: {cnt} items")
