# -*- coding: utf-8 -*-
"""修复 11-04 遗留的 index/archive 污染（Python 源码串入 HTML），并发布 2026-11-05 日报"""
import ast, os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DATE, DATE_CN, WEEKDAY, PREV = '2026-11-05', '2026年11月5日', '周四', '2026-11-04'


def load_sections(fname):
    with open(os.path.join(ROOT, fname), encoding='utf-8') as f:
        tree = ast.parse(f.read())
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and any(getattr(t, 'id', '') == 'SECTIONS' for t in n.targets):
            return ast.literal_eval(n.value)
    raise SystemExit('SECTIONS not found in ' + fname)


def parts_of(sections):
    out = []
    for s in sections:
        for i in s['items']:
            if i.get('badge') == '[备注]' or not i.get('url'):
                continue
            out.append(f"{i['title']}（{i.get('source','')} {i.get('date','')[5:]}）")
    return out


sec05 = load_sections('build_daily_1105.py')
sec04 = load_sections('build_daily_1104.py')
p05, p04 = parts_of(sec05), parts_of(sec04)
n05, n04 = len(p05), len(p04)
print('items: 11-05 =', n05, '| 11-04 =', n04)
assert n05 == 32, n05
assert n04 == 42, n04

ex05 = f'9 个研究方向 · {n05} 条精选资讯（期刊 14 条，占比 43.8%）。' + '；'.join(p05) + '。'
ex04 = f'9 个研究方向 · {n04} 条精选资讯（含补录 2 条）。' + '；'.join(p04) + '。'

# ---------- 1) 复制到 posts/ ----------
src = os.path.join(ROOT, 'daily_reports', f'海洋AI简报_{DATE}.html')
dst = os.path.join(ROOT, 'posts', f'{DATE}.html')
shutil.copyfile(src, dst)
print('COPIED -> posts/%s.html' % DATE)

TAGS = ['海洋AI', '数字孪生', '可视化', '数据质量', '数据处理', '数据共享', '开放航次', '数据中心', '工具资源']


def card(d, wd, excerpt):
    tags = '\n'.join(f'                    <span class="tag">{t}</span>' for t in TAGS)
    return f'''    <div class="post-card">
                <div class="post-header">
                    <a href="posts/{d}.html" class="post-title">海洋AI技术日报 · {d}（{wd}）</a>
                    <span class="post-date">{d}</span>
                </div>
                <p class="post-excerpt">{excerpt}</p>
                <div class="post-tags">
{tags}
                </div>
    </div>


'''

# ---------- 2) 修复 index.html 并插入 11-05 卡片 ----------
ip = os.path.join(ROOT, 'index.html')
lines = open(ip, encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(lines) if 'post-excerpt' in l and '42 条精选资讯' in l)
end = next(i for i, l in enumerate(lines[start:], start) if l.strip().startswith('<div class="post-tags">'))
print('index repair range:', start + 1, '->', end, '(will drop', end - start - 1, 'polluted lines)')
assert "'badge':" in '\n'.join(lines[start:end]), '未在预期区间发现污染，终止以免误删'
lines[start:end] = ['                <p class="post-excerpt">' + ex04 + '</p>']
html = '\n'.join(lines)

anchor = f'    <div class="post-card">\n                <div class="post-header">\n                    <a href="posts/{PREV}.html"'
if anchor not in html:
    raise SystemExit('INDEX ANCHOR NOT FOUND')
html = html.replace(anchor, card(DATE, WEEKDAY, ex05) + anchor, 1)
open(ip, 'w', encoding='utf-8').write(html)
print('INDEX repaired + 11-05 card inserted')

# ---------- 3) 修复 archive.html 并插入 11-05 条目 ----------
ap = os.path.join(ROOT, 'archive.html')
alines = open(ap, encoding='utf-8').read().split('\n')
a_start = next(i for i, l in enumerate(alines) if '<h2>📅 2026年11月</h2>' in l) + 1
a_end = next(i for i, l in enumerate(alines[a_start:], a_start) if l.strip().endswith('</li></ul>'))
print('archive repair range:', a_start + 1, '->', a_end + 1)
assert "'badge':" in '\n'.join(alines[a_start:a_end + 1]), '未在预期区间发现污染，终止'
li05 = f'<li><a href="posts/{DATE}.html"><strong>{DATE}</strong></a>（{WEEKDAY}） · 9个方向 · {n05}条动态 · 重点：' + '；'.join(p05) + '。</li>'
li04 = f'<li><a href="posts/{PREV}.html"><strong>{PREV}</strong></a>（周三） · 9个方向 · {n04}条动态（含补录2条） · 重点：' + '；'.join(p04) + '。</li>'
alines[a_start:a_end + 1] = ['      <ul>' + li05 + li04 + '</ul>']
open(ap, 'w', encoding='utf-8').write('\n'.join(alines))
print('ARCHIVE repaired + 11-05 entry inserted')
print('DONE')
