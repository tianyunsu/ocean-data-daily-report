# -*- coding: utf-8 -*-
"""Publish 2026-10-05 daily report: posts/ + index.html + archive.html (idempotent)."""
import ast, re, shutil, os

TODAY = '2026-10-05'
WEEKDAY = '周一'
SRC = f'daily_reports/海洋AI简报_{TODAY}.html'
DST = f'posts/{TODAY}.html'

# --- 1. copy report to posts/
os.makedirs('posts', exist_ok=True)
shutil.copyfile(SRC, DST)
print('copied ->', DST)

# --- 2. build excerpt from SECTIONS
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    tree = ast.parse(f.read())
sections = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == 'SECTIONS':
                sections = ast.literal_eval(node.value)
    if sections:
        break

parts = []
for s in sections:
    for it in s['items']:
        src = (it.get('source') or '').split('（')[0].split('/')[0].strip()
        parts.append(f"{it['title']}（{src} {it['date'][5:]}）")
n_items = len(parts)
excerpt = f"9 个研究方向 · {n_items} 条精选资讯。" + "；".join(parts) + "。"

# --- 3. index.html : insert post-card
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

if f'posts/{TODAY}.html' in idx:
    print('index.html already contains today, skip')
else:
    tags = ''.join(f'                    <span class="tag">{t}</span>\n' for t in
                   ['海洋AI', '数字孪生', '可视化', '数据质量', '数据处理',
                    '数据共享', '开放航次', '数据中心', '工具资源'])
    card = (
        '    <div class="post-card">\n'
        '                <div class="post-header">\n'
        f'                    <a href="posts/{TODAY}.html" class="post-title">海洋AI技术日报 · {TODAY}（{WEEKDAY}）</a>\n'
        f'                    <span class="post-date">{TODAY}</span>\n'
        '                </div>\n'
        f'                <p class="post-excerpt">{excerpt}</p>\n'
        '                <div class="post-tags">\n'
        + tags +
        '                </div>\n'
        '    </div>\n\n'
    )
    marker = '<main class="container">\n'
    assert marker in idx, 'index marker missing'
    idx = idx.replace(marker, marker + '\n' + card, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('index.html updated')

# --- 4. archive.html : insert li (create 2026年10月 group if missing)
with open('archive.html', 'r', encoding='utf-8') as f:
    arc = f.read()

if f'posts/{TODAY}.html' in arc:
    print('archive.html already contains today, skip')
else:
    li = (f'<li><a href="posts/{TODAY}.html"><strong>{TODAY}</strong></a>（{WEEKDAY}） · '
          f'9个方向 · {n_items}条动态 · 重点：' + '；'.join(parts) + '。</li>')
    if '2026年10月' in arc:
        m = re.search(r'(<div class="archive-group">\s*<h2>[^<]*2026年10月</h2>\s*<ul>)', arc)
        assert m, 'archive 2026年10月 ul not found'
        arc = arc[:m.end(1)] + li + arc[m.end(1):]
    else:
        m = re.search(r'(\s*)(<div class="archive-group">\s*<h2>[^<]*2026年09月</h2>)', arc)
        assert m, 'archive 2026年09月 group not found'
        block = ('\n    <div class="archive-group">\n'
                 '      <h2>📅 2026年10月</h2>\n'
                 '      <ul>' + li + '</ul>\n'
                 '    </div>\n')
        arc = arc[:m.start(1)] + block + arc[m.start(1):]
    with open('archive.html', 'w', encoding='utf-8') as f:
        f.write(arc)
    print('archive.html updated')

print('items:', n_items)
