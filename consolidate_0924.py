# -*- coding: utf-8 -*-
"""Consolidate 2026-09-24: 去重+去超期 → 重写 SECTIONS → 重新生成/发布 HTML。"""
import ast, re, shutil, pathlib

SRC = pathlib.Path('feishu_write_doc.py')
s = SRC.read_text(encoding='utf-8')
tree = ast.parse(s)
sec = None
for n in ast.walk(tree):
    if isinstance(n, ast.Assign) and any(getattr(t, 'id', None) == 'SECTIONS' for t in n.targets):
        sec = ast.literal_eval(n.value)
        break
assert sec, 'SECTIONS not found'

DROP = ['LeadNet 与 80 米分辨率泛北极冬季冰间水道数据集',   # 已在 09-15 期收录（跨期重复）
        '广州海洋地质调查局 AUV 在南海超深水完成失联设备搜寻',   # 15 天，超 14 天窗口
        'Argo 全球数据汇编中心发布最新全球数据快照',            # 16 天，超 14 天窗口
        'GEBCO_2026 全球水深网格']                        # 网格为 2026-04 发布，日期站不住

removed = []
for d in sec:
    keep = []
    for it in d['items']:
        if any(it['title'].startswith(k) for k in DROP):
            removed.append(it['title'])
            continue
        # 工具版本链接不得指向总览页（陷阱 13）
        if 'copernicusmarine' in it['title'] or 'Copernicus Marine Toolbox' in it['title']:
            it['url'] = 'https://pypi.org/project/copernicusmarine/2.5.0b1/'
            it['source'] = 'PyPI / copernicusmarine 2.5.0b1'
            if '2.5.0b1' not in it['title']:
                it['title'] = 'Copernicus Marine Toolbox 发布 2.5.0b1'
        keep.append(it)
    d['items'] = keep

new_repr = repr(sec).replace('\\x27', "'")
pattern = re.compile(r'SECTIONS = \[.*?(?=\ndef tr\(|\n# ---|\Z)', re.DOTALL)
s = pattern.sub('SECTIONS = ' + new_repr + '\n\n\n', s, count=1)
SRC.write_text(s, encoding='utf-8')

total = sum(len(x['items']) for x in sec)
print('删除:', removed)
print('最终条数:', total)
for d in sec:
    print(f'  {d["title"]}: {len(d["items"])}')
