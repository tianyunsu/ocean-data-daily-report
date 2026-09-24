# -*- coding: utf-8 -*-
"""Append the CF Conventions Workshop item to 六 and rewrite build_daily_0924.py"""
import ast
import re

SRC = 'build_daily_0924.py'
raw = open(SRC, encoding='utf-8').read()
S = None
for n in ast.walk(ast.parse(raw)):
    if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'SECTIONS':
        S = ast.literal_eval(n.value)
        break
assert S
m = re.search(r'\n\ndef main\(\):', raw)
tail = raw[m.start():] if m else ''

by_title = {s['title']: s for s in S}
sec = by_title['六、数据管理与共享']
if any('CF 公约社区研讨会' in i['title'] for i in sec['items']):
    raise SystemExit('already added')
sec['items'].append({
    'title': 'CF 公约社区研讨会 2026：推进环境数据标准与互操作',
    'badge': '[动态]',
    'abstract': 'CF（Climate and Forecast）公约社区研讨会 2026 于 9 月 21—24 日在德国波恩 ECMWF 以线上线下混合方式举行，由 Copernicus 气候变化服务等支持。会议汇聚全球 CF 社区的研究者、开发者与数据专家，围绕气候与预报元数据标准的最新进展开展全体会议、特邀报告与互动讨论，并设置实操黑客松与分组专题，旨在推进环境数据的标准、协作与互操作性。CF 公约是海洋与大气数据共享中应用最广的自描述元数据规范之一，其演进直接影响海洋观测与模式数据的可发现性与可互操作程度。',
    'source': 'Copernicus Climate Change Service (C3S)',
    'url': 'https://climate.copernicus.eu/cf-conventions-community-workshop-2026',
    'date': '2026-09-21',
})

new_repr = repr(S).replace('\\x27', "'")
out = ('# -*- coding: utf-8 -*-\n'
       '"""Write SECTIONS for 2026-09-24 into feishu_write_doc.py (regex replace)."""\n'
       'import re\n\n'
       'SECTIONS = ' + new_repr + '\n' + tail)
open(SRC, 'w', encoding='utf-8').write(out)
print('per-direction:', {s['title'][:2]: len(s['items']) for s in S})
print('TOTAL', sum(len(s['items']) for s in S))
