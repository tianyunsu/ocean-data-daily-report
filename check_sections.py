#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all dates in the SECTIONS area (before def tr)
tr_pos = content.find('def tr(')
sections_area = content[:tr_pos]

date_pattern = r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'"
dates = re.findall(date_pattern, sections_area)

cutoff = datetime(2026, 3, 25)
today = datetime(2026, 4, 24)

print(f'Dates found in SECTIONS area: {len(dates)}')
for d in dates:
    dt = datetime.strptime(d, '%Y-%m-%d')
    days_old = (today - dt).days
    marker = ' *** VIOLATION ***' if dt < cutoff else ''
    print(f'  {d} ({days_old} days old){marker}')
