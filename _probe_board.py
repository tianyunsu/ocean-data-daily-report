import json
d = json.load(open('data/pool_index.json', encoding='utf-8'))
print('池内', d['total_pool'], '| 看板', d['board_count'])
for it in d['items'][:14]:
    print("[%s] %s | %-38s | %s" % (it['tier'], it['d'], it['j'][:38], it['t'][:70]))
print('--- 预警刊条目 ---')
for it in d['items']:
    if it['tier'] == 'D':
        fl = (it['flags'][0] if it['flags'] else '')[:30]
        print("[D] %-32s | %s | %s" % (it['j'][:32], it['t'][:52], fl))
print('--- 各方向 Top3 ---')
seen = {}
for it in d['items']:
    seen.setdefault(it['dir'], 0)
    if seen[it['dir']] < 3:
        seen[it['dir']] += 1
        print("D%s [%s] %s | %s" % (it['dir'], it['tier'], it['j'][:30], it['t'][:62]))
