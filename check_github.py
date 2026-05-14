#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request, json

# Check file existence
url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts/2026-04-24.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    print(f"File found: sha={data['sha']}, size={data.get('size', 'N/A')}")
    # Check the HTML content
    import base64
    content = base64.b64decode(data['content']).decode('utf-8')
    print(f"Content length: {len(content)} chars")
    print(f"Content preview (first 500): {content[:500]}")
except Exception as e:
    print(f"Error: {e}")
