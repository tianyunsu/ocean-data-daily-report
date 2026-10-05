# -*- coding: utf-8 -*-
import re, json, urllib.request, ssl, time
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
html = open('posts/2026-10-05.html', encoding='utf-8').read()
urls = re.findall(r'href="(https?://[^"]+)"', html)
urls = [u for u in urls if 'github.io' not in u and 'github.com' not in u]
seen=[]; 
for u in urls:
    if u not in seen: seen.append(u)
res={'ok':[], 'bad':[]}
for u in seen:
    code=None
    for attempt in range(2):
        try:
            req=urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                code=r.status; break
        except urllib.error.HTTPError as e:
            code=e.code; break
        except Exception as e:
            code=str(e)[:60]; time.sleep(1)
    (res['ok'] if str(code).startswith('2') else res['bad']).append((u,code))
    print(code, u, flush=True)
print('=== SUMMARY ===')
print('ok', len(res['ok']), 'bad', len(res['bad']), 'total', len(seen))
for u,c in res['bad']: print('BAD', c, u)
json.dump({u:c for u,c in res['ok']+res['bad']}, open('_link_result_1005.json','w'), ensure_ascii=False, indent=1)
