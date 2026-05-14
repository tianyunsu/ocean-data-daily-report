#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request, json, base64, re
from datetime import datetime

url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts/2026-04-24.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())

content = base64.b64decode(data['content']).decode('utf-8')

# Find all date patterns in the HTML
date_pattern = r"20\d{2}-\d{2}-\d{2}"
dates = re.findall(date_pattern, content)
print(f"Total dates found in HTML: {len(dates)}")

# Filter unique dates
unique_dates = list(dict.fromkeys(dates))
print(f"Unique dates: {len(unique_dates)}")
for d in sorted(unique_dates):
    dt = datetime.strptime(d, '%Y-%m-%d')
    days_old = (datetime(2026, 4, 24) - dt).days
    marker = ' *** EXPIRED ***' if days_old > 30 else ''
    print(f"  {d} ({days_old} days old){marker}")

# Check for violations
cutoff = datetime(2026, 3, 25)
today = datetime(2026, 4, 24)
violations = []
for d in unique_dates:
    dt = datetime.strptime(d, '%Y-%m-%d')
    if dt < cutoff:
        violations.append(f'{d}')
if violations:
    print(f"\nVIOLATIONS ({len(violations)}): {violations}")
else:
    print(f"\nAll dates OK - 0 violations!")
