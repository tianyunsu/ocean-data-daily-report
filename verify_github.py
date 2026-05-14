#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request, json, base64, re
from datetime import datetime

url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts/2026-04-24.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())

content = base64.b64decode(data['content']).decode('utf-8')
date_pattern = r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'"
dates = re.findall(date_pattern, content)
print(f'Items in GitHub posts/2026-04-24.html: {len(dates)}')

cutoff = datetime(2026, 3, 25)
today = datetime(2026, 4, 24)
violations = []
for d in dates:
    dt = datetime.strptime(d, '%Y-%m-%d')
    days_old = (today - dt).days
    if dt < cutoff:
        violations.append(f'{d} ({days_old} days old)')
if violations:
    print(f'VIOLATIONS: {violations}')
else:
    print('All dates OK - 0 violations')
    for d in dates:
        dt = datetime.strptime(d, '%Y-%m-%d')
        print(f'  {d} ({(today-dt).days} days old)')
