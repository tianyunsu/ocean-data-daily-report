import urllib.request
import sys

urls = [
    'https://mp.weixin.qq.com/s/0kjTWsbhrNyWKquDF5Tj6g',
    'https://mp.weixin.qq.com/s/ez-eFuUj350VzWZR5mvO3g'
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

for i, url in enumerate(urls):
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=20)
        html = resp.read().decode('utf-8')
        fname = f'wx_article_{i+1}.html'
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Article {i+1} saved: {fname}, length: {len(html)}')
    except Exception as e:
        print(f'Error for article {i+1}: {e}')
