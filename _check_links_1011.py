# -*- coding: utf-8 -*-
"""Link checker with HEAD->GET fallback for the daily HTML."""
import re, sys, urllib.request, urllib.error, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

path = sys.argv[1] if len(sys.argv) > 1 else 'daily_reports/海洋AI简报_2026-10-11.html'
s = open(path, encoding='utf-8').read()
urls = []
for m in re.finditer(r'href="(https?://[^"]+)"', s):
    u = m.group(1)
    if 'github.io' in u or u.startswith('https://tianyunsu'):
        continue
    if u not in urls:
        urls.append(u)

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36'

def probe(u, method):
    req = urllib.request.Request(u, headers={'User-Agent': UA, 'Accept': '*/*'}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            return r.status, len(r.read(200))
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:
        return 'ERR', str(e)[:60]

bad = []
for u in urls:
    st, _ = probe(u, 'HEAD')
    if st in ('ERR', 403, 405, 404, 500, 502, 503) or not isinstance(st, int) or st >= 400:
        st2, info = probe(u, 'GET')
        time.sleep(0.3)
        print(f'{st:>4} -> {st2:>4}  {u[:110]}')
        if not (isinstance(st2, int) and 200 <= st2 < 400):
            bad.append((u, st, st2))
    else:
        print(f'{st:>4}        {u[:110]}')
    time.sleep(0.2)

print('\n==== SUMMARY ====')
print(f'total {len(urls)} | anomalies {len(bad)}')
for b in bad:
    print('BAD', b)
