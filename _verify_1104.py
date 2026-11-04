# -*- coding: utf-8 -*-
import json, sys, urllib.parse, urllib.request, time
sys.path.insert(0, '.')
import harvest
KEY = harvest._oa_key()

dois = [
 '10.1038/s41612-026-01347-2',
 '10.5194/essd-2026-807',
 '10.48550/arxiv.2610.29313',
 '10.48550/arxiv.2610.36410',
 '10.48550/arxiv.2610.37731',
 '10.1177/14738716261492254',
 '10.1029/2026gl124056',
 '10.1038/s41598-026-78685-x',
 '10.5194/essd-18-7963-2026',
 '10.1016/j.oceaneng.2026.129035',
 '10.3389/fmars.2026.1998272',
 '10.1016/j.rineng.2026.113720',
]
for d in dois:
    url = 'https://api.openalex.org/works/https://doi.org/' + d + '?api_key=' + KEY
    try:
        with urllib.request.urlopen(url, timeout=40) as r:
            w = json.loads(r.read().decode())
        src = ((w.get('primary_location') or {}).get('source') or {}).get('display_name')
        print(f"OK  {d} | {w.get('publication_date')} | {w.get('type')} | {src} | {w.get('title','')[:80]}")
    except Exception as e:
        print(f"ERR {d} | {e}")
    time.sleep(0.4)
