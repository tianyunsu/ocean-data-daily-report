#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查当前SECTIONS中所有日期，标记超期内容"""
import re
from datetime import datetime, timedelta

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    src = f.read()

# 提取SECTIONS数据块
match = re.search(r'^SECTIONS\s*=\s*(\[.*?\n\])', src, re.MULTILINE | re.DOTALL)
if not match:
    print("ERROR: SECTIONS not found")
    exit(1)

exec(match.group(0))

today = datetime.now()
cutoff_1week = today - timedelta(days=7)
cutoff_1month = today - timedelta(days=30)

print(f"今日: {today.strftime('%Y-%m-%d')}")
print(f"7天前: {cutoff_1week.strftime('%Y-%m-%d')}  (超此日期为低优先级)")
print(f"30天前: {cutoff_1month.strftime('%Y-%m-%d')} (超此日期必须删除)")
print("=" * 60)

overdue = []
for s in SECTIONS:
    print(f"\n=== {s['title']} ===")
    for item in s['items']:
        date_raw = item.get('date', '?')
        try:
            d = datetime.strptime(date_raw, '%Y-%m-%d')
            if d < cutoff_1month:
                flag = "❌ 超1个月！必须删除"
                overdue.append((s['title'], item['title'][:50], date_raw))
            elif d < cutoff_1week:
                flag = "⚠️ 1周-1个月，需审查"
            else:
                flag = "✅ 近7天"
        except:
            flag = "❓ 日期格式异常"
        print(f"  [{date_raw}] {flag}  {item['title'][:55]}")

print("\n" + "=" * 60)
if overdue:
    print(f"❌ 共发现 {len(overdue)} 条超1个月内容，必须删除：")
    for sec, title, date in overdue:
        print(f"  [{date}] [{sec}] {title}")
else:
    print("✅ 所有内容均在1个月内，无需删除")
