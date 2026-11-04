# -*- coding: utf-8 -*-
import json, sys, collections
idx = json.load(open('data/pool_index.json', encoding='utf-8'))['items']
# 读池 jsonl 的 abstract
abs_map = {}
for line in open('data/pool/2026-11-04.jsonl', encoding='utf-8'):
    try:
        r = json.loads(line)
    except Exception:
        continue
    for k in ('doi', 'title'):
        pass
    key = (r.get('doi') or '').lower() or (r.get('title') or '')[:80]
    abs_map[key] = r.get('abstract') or ''

def get_abs(it):
    k = (it.get('doi') or '').lower()
    if k in abs_map and abs_map[k]:
        return abs_map[k]
    k2 = (it.get('t') or '')[:80]
    return abs_map.get(k2, '')

by = collections.defaultdict(list)
for it in idx:
    it['_abs'] = get_abs(it)
    by[it['dir']].append(it)

for d in sorted(by):
    rows = sorted(by[d], key=lambda x: -x['score'])
    print(f"\n########## 方向 {d} 共 {len(rows)} 条（有摘要 {sum(1 for r in rows if r['_abs'])}）")
    n = 0
    for r in rows:
        if not r['_abs']:
            continue
        n += 1
        if n > 26: break
        print(f"[{r['tier']}] {r['d']} | {r['t'][:100]}")
        print(f"    {r['j'][:60]} | doi={r['doi']} | score={r['score']:.0f} | fit={r.get('fit')}")
        print(f"    ABS: {r['_abs'][:420]}")
