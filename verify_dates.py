import re
from datetime import datetime, timedelta

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all date fields in SECTIONS
date_pattern = r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'"
matches = re.findall(date_pattern, content)

today = datetime(2026, 4, 24)
cutoff_30d = today - timedelta(days=30)

print(f"今日: {today.strftime('%Y-%m-%d')}, 近1月截止: {cutoff_30d.strftime('%Y-%m-%d')}")
print("=" * 80)

# Find item titles (those with numbered prefix like "1. " or "2. ")
item_title_pattern = r"(?:'title':\s*'((?:1|2|3|4|5|6|7|8|9)\.[^']+)')"
item_titles = re.findall(item_title_pattern, content)

violations = 0
ok_7d = 0
ok_1m = 0
for i, date_str in enumerate(matches):
    d = datetime.strptime(date_str, '%Y-%m-%d')
    age = (today - d).days
    if d < cutoff_30d:
        status = "[!!超期!!]"
        violations += 1
    elif age <= 7:
        status = "[OK  近7天]"
        ok_7d += 1
    else:
        status = "[OK  近1月]"
        ok_1m += 1
    title = item_titles[i] if i < len(item_titles) else "(section title)"
    print(f"{status} {date_str} ({age:3d}天) {title[:55]}")

print()
print("=" * 80)
print(f"总计: {len(matches)}条, 超期: {violations}条")
if violations == 0:
    print("PASS - 全部通过日期审查")
    exit(0)
else:
    print(f"FAIL - 仍有 {violations} 条超期内容")
    exit(1)
