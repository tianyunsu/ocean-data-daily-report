# -*- coding: utf-8 -*-
"""阶段一：顶会论文 + IEEE 期刊检索（2026-11-04）"""
import json, sys, time, urllib.parse, urllib.request
sys.path.insert(0, '.')
import harvest

KEY = harvest._oa_key()
BASE = 'https://api.openalex.org/works'
FROM, TO = '2026-10-21', '2026-11-04'

OCEAN = '(ocean OR marine OR underwater OR sea-ice OR seafloor OR bathymetry OR "sea surface temperature" OR "ocean current" OR Arctic OR "coral reef" OR plankton OR sonar OR AUV OR "remote sensing" OR typhoon OR estuary OR coastal)'

def q(extra, per=50):
    params = {
        'filter': f'from_publication_date:{FROM},to_publication_date:{TO}' + (',' + extra if extra else ''),
        'search': OCEAN,
        'per-page': per,
        'api_key': KEY,
    }
    url = BASE + '?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            print('  retry', attempt, e)
            time.sleep(3)
    return {'results': [], 'meta': {'count': 0}}

def show(tag, d, limit=25):
    print(f'=== {tag} | count={d.get("meta",{}).get("count")}')
    for w in d.get('results', [])[:limit]:
        src = ''
        try:
            src = (w.get('primary_location') or {}).get('source') or {}
            src = src.get('display_name') or ''
        except Exception:
            pass
        print(f'  [{w.get("publication_date")}] {w.get("title","")[:95]} | {src[:55]} | {(w.get("doi") or "")[:60]} | abs={"Y" if w.get("abstract_inverted_index") else "N"}')

# 1) 会议论文（正确类型值 conference-paper）
show('CONFERENCE-PAPER', q('type:conference-paper'))
time.sleep(1)

# 2) IEEE 高相关期刊
ieee = {
 'JOE(JOE)': 'primary_location.source.issn:0364-9059',
 'TGRS': 'primary_location.source.issn:0196-2892',
 'GRSL': 'primary_location.source.issn:1545-598X',
 'JSTARS': 'primary_location.source.issn:1939-1404',
 'GRSM': 'primary_location.source.issn:2168-6831',
 'RA-L': 'primary_location.source.issn:2377-3766',
 'TRO': 'primary_location.source.issn:1552-3098',
 'TNNLS': 'primary_location.source.issn:2162-237X',
 'TIP': 'primary_location.source.issn:1057-7149',
}
for name, f in ieee.items():
    show('IEEE ' + name, q(f))
    time.sleep(1)
