#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

cutoff = datetime(2026, 3, 25)
today = datetime(2026, 4, 24)

date_pattern = r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'"
dates = re.findall(date_pattern, content)

violations = []
for d in dates:
    dt = datetime.strptime(d, '%Y-%m-%d')
    days_old = (today - dt).days
    if dt < cutoff:
        violations.append((d, days_old))

if violations:
    print(f'VIOLATIONS ({len(violations)}):')
    for v in sorted(violations, key=lambda x: x[0]):
        print(f'  {v[0]} ({v[1]} days old)')
else:
    print(f'ALL OK - {len(dates)} items, 0 violations (cutoff: 2026-03-25)')
