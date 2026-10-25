# -*- coding: utf-8 -*-
"""Publish 2026-10-25 daily report: copy to posts/, update index.html + archive.html."""
import re, shutil, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATE = '2026-10-25'
DATE_CN = '2026年10月25日'
WEEKDAY = '周日'

# 1) copy daily report -> posts/
src = os.path.join(ROOT, 'daily_reports', f'海洋AI简报_{DATE}.html')
dst = os.path.join(ROOT, 'posts', f'{DATE}.html')
shutil.copyfile(src, dst)
print('COPIED ->', dst)

# 2) build excerpt from build_daily_1025.py
build = open(os.path.join(ROOT, 'build_daily_1025.py'), encoding='utf-8').read()
secs = re.findall(r"'title': '([^']+)'.*?'items': \[(.*?)\]\}", build, re.DOTALL)
items = []
for name, body in secs:
    for m in re.finditer(r"\{'title': '(.*?)',\s*'badge': '[^']*',\s*'abstract': '.*?',\s*'source': '(.*?)',\s*'url': '(.*?)',\s*'date': '([0-9-]+)'\}", body, re.DOTALL):
        title, source, url, date = m.group(1), m.group(2), m.group(3), m.group(4)
        items.append((title, source, date))

n = len(items)
excerpt = f'9 个研究方向 · {n} 条精选资讯。'
parts = []
for title, source, date in items:
    parts.append(f'{title}（{source} {date[5:]}）')
excerpt += '；'.join(parts) + '。'
print('EXCERPT items:', n)
print('EXCERPT head:', excerpt[:120])

# 3) update index.html — insert card above the 2026-10-21 card
idx_path = os.path.join(ROOT, 'index.html')
idx = open(idx_path, encoding='utf-8').read()
anchor = '    <div class="post-card">\n                <div class="post-header">\n                    <a href="posts/2026-10-21.html"'
if anchor not in idx:
    raise SystemExit('INDEX ANCHOR NOT FOUND')
card = f'''    <div class="post-card">
                <div class="post-header">
                    <a href="posts/{DATE}.html" class="post-title">海洋AI技术日报 · {DATE}（{WEEKDAY}）</a>
                    <span class="post-date">{DATE}</span>
                </div>
                <p class="post-excerpt">{excerpt}</p>
                <div class="post-tags">
                    <span class="tag">海洋AI</span>
                    <span class="tag">数字孪生</span>
                    <span class="tag">可视化</span>
                    <span class="tag">数据质量</span>
                    <span class="tag">数据处理</span>
                    <span class="tag">数据共享</span>
                    <span class="tag">开放航次</span>
                    <span class="tag">数据中心</span>
                    <span class="tag">工具资源</span>
                </div>
    </div>


'''
idx = idx.replace(anchor, card + anchor, 1)
open(idx_path, 'w', encoding='utf-8').write(idx)
print('INDEX updated')

# 4) update archive.html — insert <li> at top of 2026年10月 <ul>
arc_path = os.path.join(ROOT, 'archive.html')
arc = open(arc_path, encoding='utf-8').read()
arc_anchor = '<h2>📅 2026年10月</h2>\n      <ul><li><a href="posts/2026-10-21.html">'
if arc_anchor not in arc:
    raise SystemExit('ARCHIVE ANCHOR NOT FOUND')
li = f'<li><a href="posts/{DATE}.html"><strong>{DATE}</strong></a>（{WEEKDAY}） · 9个方向 · {n}条动态 · 重点：' + '；'.join(parts) + '。</li>'
arc = arc.replace('<h2>📅 2026年10月</h2>\n      <ul>', '<h2>📅 2026年10月</h2>\n      <ul>' + li, 1)
open(arc_path, 'w', encoding='utf-8').write(arc)
print('ARCHIVE updated')
print('DONE')
