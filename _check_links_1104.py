# -*- coding: utf-8 -*-
"""链接有效性检查：posts/2026-11-04.html"""
import re, ssl, time, urllib.request, collections
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36'}
html = open('posts/2026-11-04.html', encoding='utf-8').read()
urls = []
for m in re.finditer(r'href="(https?://[^"]+)"', html):
    u = m.group(1)
    if u not in urls:
        urls.append(u)
print('unique urls', len(urls))
bad = []
host_c = collections.Counter()
for u in urls:
    host_c[u.split('/')[2]] += 1
    code = 'ERR'
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=35, context=ctx)
        code = r.status
    except Exception as e:
        code = getattr(e, 'code', '') or type(e).__name__
    if str(code) != '200':
        bad.append((str(code), u))
    print(str(code), u)
    time.sleep(0.3)
print('\n--- DOMAINS ---')
for h, c in host_c.most_common():
    print(c, h)
print('\n--- NOT 200 ---')
for c, u in bad:
    print(c, u)
