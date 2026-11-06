# -*- coding: utf-8 -*-
"""发布 2026-11-06 日报：复制 posts + 用 AST 抽条目生成 index 卡片 / archive 条目。

铁律：一律用 ast.literal_eval 取 SECTIONS，禁用正则跨节抽条目（11-05 事故）。
"""
import ast, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DATE, DATE_CN, WEEKDAY, PREV = '2026-11-06', '2026年11月6日', '周五', '2026-11-05'


def load_sections(fname):
    with open(os.path.join(ROOT, fname), encoding='utf-8') as f:
        tree = ast.parse(f.read())
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and any(getattr(t, 'id', '') == 'SECTIONS' for t in n.targets):
            return ast.literal_eval(n.value)
    raise SystemExit('SECTIONS not found in ' + fname)


sections = load_sections('build_daily_1106.py')
parts = []
for s in sections:
    for i in s['items']:
        if i.get('badge') == '[备注]' or not i.get('url'):
            continue
        parts.append(f"{i['title']}（{i.get('source','')} {i.get('date','')[5:]}）")
N = len(parts)
print('items:', N)
assert N == 36, N
assert len(sections) == 9, len(sections)

excerpt = f'9 个研究方向 · {N} 条精选资讯（期刊 15 条，占比 41.7%）。' + '；'.join(parts) + '。'

# ---------- 1) 复制到 posts/ ----------
src = os.path.join(ROOT, 'daily_reports', f'海洋AI简报_{DATE}.html')
dst = os.path.join(ROOT, 'posts', f'{DATE}.html')
shutil.copyfile(src, dst)
print('COPIED -> posts/%s.html' % DATE)

TAGS = ['海洋AI', '数字孪生', '可视化', '数据质量', '数据处理', '数据共享', '开放航次', '数据中心', '工具资源']


def card():
    tags = '\n'.join(f'                    <span class="tag">{t}</span>' for t in TAGS)
    return f'''    <div class="post-card">
                <div class="post-header">
                    <a href="posts/{DATE}.html" class="post-title">海洋AI技术日报 · {DATE}（{WEEKDAY}）</a>
                    <span class="post-date">{DATE}</span>
                </div>
                <p class="post-excerpt">{excerpt}</p>
                <div class="post-tags">
{tags}
                </div>
    </div>


'''


# ---------- 2) index.html 插入新卡片 ----------
ip = os.path.join(ROOT, 'index.html')
html = open(ip, encoding='utf-8').read()
assert "'badge':" not in html, 'index.html 存在源码污染，先修复再发布'
anchor = (f'    <div class="post-card">\n                <div class="post-header">\n'
          f'                    <a href="posts/{PREV}.html"')
if anchor not in html:
    raise SystemExit('INDEX ANCHOR NOT FOUND')
if f'posts/{DATE}.html' in html:
    raise SystemExit('本期卡片已存在，禁止重复插入')
html = html.replace(anchor, card() + anchor, 1)
open(ip, 'w', encoding='utf-8').write(html)
print('INDEX card inserted')

# ---------- 3) archive.html 插入 11 月首个条目 ----------
ap = os.path.join(ROOT, 'archive.html')
ahtml = open(ap, encoding='utf-8').read()
assert "'badge':" not in ahtml, 'archive.html 存在源码污染，先修复再发布'
head = '<h2>📅 2026年11月</h2>'
if head not in ahtml:
    raise SystemExit('ARCHIVE MONTH HEADING NOT FOUND')
if f'posts/{DATE}.html' in ahtml:
    raise SystemExit('本期归档条目已存在，禁止重复插入')
li = (f'<li><a href="posts/{DATE}.html"><strong>{DATE}</strong></a>（{WEEKDAY}） · '
      f'9个方向 · {N}条动态 · 重点：' + '；'.join(parts) + '。</li>')
ahtml = ahtml.replace(head + '\n      <ul>', head + '\n      <ul>' + li, 1)
open(ap, 'w', encoding='utf-8').write(ahtml)
print('ARCHIVE entry inserted')
print('DONE')
