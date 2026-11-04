# -*- coding: utf-8 -*-
"""阶段一补充：抓取全部会议论文候选 + 摘要，落盘 JSON"""
import json, sys, time, urllib.parse, urllib.request
sys.path.insert(0, '.')
import harvest

KEY = harvest._oa_key()
BASE = 'https://api.openalex.org/works'
FROM, TO = '2026-10-21', '2026-11-04'
OCEAN = '(ocean OR marine OR underwater OR sea-ice OR seafloor OR bathymetry OR "sea surface temperature" OR "ocean current" OR Arctic OR "coral reef" OR plankton OR sonar OR AUV)'

def fetch_all(extra, maxpages=10):
    out = []
    cursor = '*'
    for p in range(maxpages):
        params = {
            'filter': f'from_publication_date:{FROM},to_publication_date:{TO},{extra}',
            'search': OCEAN,
            'per-page': 50,
            'cursor': cursor,
            'api_key': KEY,
        }
        url = BASE + '?' + urllib.parse.urlencode(params)
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                d = json.loads(r.read().decode())
        except Exception as e:
            print('ERR', e); break
        res = d.get('results', [])
        out.extend(res)
        cursor = d.get('meta', {}).get('next_cursor')
        if not res or not cursor:
            break
        time.sleep(1)
    return out

def inv2abs(inv):
    if not inv: return ''
    pos = []
    for w, idxs in inv.items():
        for i in idxs: pos.append((i, w))
    pos.sort()
    return ' '.join(w for _, w in pos)

def pack(works, tag):
    rows = []
    for w in works:
        src = ''
        try:
            s = (w.get('primary_location') or {}).get('source') or {}
            src = s.get('display_name') or ''
        except Exception:
            pass
        rows.append({
            'tag': tag,
            'date': w.get('publication_date'),
            'title': w.get('title') or '',
            'doi': (w.get('doi') or '').replace('https://doi.org/', ''),
            'src': src,
            'type': w.get('type'),
            'abs': inv2abs(w.get('abstract_inverted_index'))[:900],
            'url': (w.get('primary_location') or {}).get('landing_page_url') or w.get('doi') or '',
        })
    return rows

allrows = []
c = fetch_all('type:conference-paper')
print('conf total fetched', len(c))
allrows += pack(c, 'conf')

# IEEE 期刊逐个（部分期刊日期塌缩，仍尝试）
ieee = {
 'JOE': '0364-9059', 'TGRS': '0196-2892', 'GRSL': '1545-598X', 'JSTARS': '1939-1404',
 'GRSM': '2168-6831', 'RA-L': '2377-3766', 'T-RO': '1552-3098', 'TNNLS': '2162-237X', 'TIP': '1057-7149',
}
for name, issn in ieee.items():
    rows = fetch_all(f'primary_location.source.issn:{issn}', maxpages=3)
    print('IEEE', name, len(rows))
    allrows += pack(rows, 'ieee:' + name)
    time.sleep(1)

json.dump(allrows, open('_stage1_1104.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('total', len(allrows), '| with abs', sum(1 for r in allrows if r['abs']))
