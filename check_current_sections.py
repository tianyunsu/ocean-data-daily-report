import re
from datetime import datetime, timedelta

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

tr_pos = content.find('def tr(')
sections_area = content[:tr_pos]

date_pattern = r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'"
dates = re.findall(date_pattern, sections_area)

# Find titles using a broader pattern
title_pattern = r"'title':\s*'([0-9]+\.[^']+)'"
titles = re.findall(title_pattern, sections_area)

today = datetime(2026, 4, 27)
cutoff_30 = datetime(2026, 3, 28)
cutoff_7 = datetime(2026, 4, 20)

print(f'Current SECTIONS total items: {len(dates)}')
print()
violations_30 = []
violations_7_30 = []
recent = []

for i, d in enumerate(dates):
    dt = datetime.strptime(d, '%Y-%m-%d')
    days = (today - dt).days
    t = titles[i] if i < len(titles) else 'N/A'
    if dt < cutoff_30:
        mark = 'XXX OVER30'
        violations_30.append((d, days, t[:50]))
    elif dt < cutoff_7:
        mark = '!! 7-30d'
        violations_7_30.append((d, days, t[:50]))
    else:
        mark = 'OK recent'
        recent.append((d, days, t[:50]))
    print(f'{i+1:2}. [{mark}] {d} ({days}d) {t[:50]}')

print()
print(f'Over 30 days (MUST delete): {len(violations_30)}')
for v in violations_30:
    print(f'  {v[0]} ({v[1]}d): {v[2]}')
print(f'7-30 days (high-value only): {len(violations_7_30)}')
for v in violations_7_30:
    print(f'  {v[0]} ({v[1]}d): {v[2]}')
print(f'Recent (OK): {len(recent)}')
