# -*- coding: utf-8 -*-
"""Check all item URLs in daily_reports/海洋AI简报_2026-09-24.html"""
import re
import ssl
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

import sys
HTML = sys.argv[1] if len(sys.argv)>1 else 'daily_reports/海洋AI简报_2026-09-24.html'
src = open(HTML, encoding='utf-8').read()
urls = []
for m in re.finditer(r'<div class="item-title">.*?<a href="([^"]+)"', src, re.S):
    urls.append(m.group(1))
urls = list(dict.fromkeys(urls))
print(f'checking {len(urls)} urls')

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def check(u):
    req = urllib.request.Request(u, headers={'User-Agent': UA, 'Accept': '*/*'})
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            body = r.read(4000).decode('utf-8', 'ignore')
            title = ''
            tm = re.search(r'<title[^>]*>(.*?)</title>', body, re.S | re.I)
            if tm:
                title = re.sub(r'\s+', ' ', tm.group(1)).strip()[:60]
            return (u, r.status, title)
    except urllib.error.HTTPError as e:
        return (u, e.code, 'HTTPError')
    except Exception as e:
        return (u, -1, type(e).__name__ + ':' + str(e)[:60])


with ThreadPoolExecutor(max_workers=8) as ex:
    res = list(ex.map(check, urls))

bad = 0
for u, st, t in res:
    flag = 'OK ' if st == 200 else 'BAD'
    if st != 200:
        bad += 1
    print(f'{flag} {st} {u}  | {t}')
print(f'\n=== total {len(res)}, non-200 {bad} ===')
