# -*- coding: utf-8 -*-
"""补跑会议通道（type:conference-paper，修复后首次生效），追加进当日池（不覆盖）。"""
import json, sys
sys.path.insert(0, '.')
import harvest

POOL = 'data/pool/2026-10-18.jsonl'
START, END = '2026-10-04', '2026-10-18'

seen, rows = set(), []
with open(POOL, encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        rows.append(d)
        seen.add(d.get('doi') or d.get('id') or harvest.fingerprint(d.get('title', '')))
        seen.add(harvest.fingerprint(d.get('title', '')))
print('原有', len(rows))

d1 = harvest.DIRECTIONS[1]
new = []
for w in harvest.fetch_openalex(d1, START, END, want_conf=True, max_pages=3):
    r = harvest.norm_rec(w, 1, d1['name'])
    fp = harvest.fingerprint(r['title'])
    key = r['doi'] or r['id']
    if key in seen or fp in seen:
        continue
    seen.update([key, fp])
    new.append(r)

print('新增会议论文', len(new))
with open(POOL, 'a', encoding='utf-8') as f:
    for r in new:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
for r in new[:15]:
    print('·', r['date'], '|', r['title'][:75], '|', r['journal'][:35])
