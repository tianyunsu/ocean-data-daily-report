#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
today = datetime.now()
one_month_ago = today - timedelta(days=30)
one_week_ago = today - timedelta(days=7)

from feishu_write_doc import SECTIONS
violations = []
for sec in SECTIONS:
    for item in sec['items']:
        try:
            item_date = datetime.strptime(item['date'], '%Y-%m-%d')
            if item_date < one_month_ago:
                violations.append(f'{sec["title"]} | {item["title"]} ({item["date"]})')
            elif item_date < one_week_ago:
                print(f'[1周~1月] {sec["title"]} | {item["date"]} | {item["title"]}')
        except Exception as e:
            print(f'[日期错误] {item["title"]}: {e}')

if violations:
    print(f'超期: {len(violations)} 条:')
    for v in violations:
        print(f'  {v}')
else:
    print('全部日期合规')
total = sum(len(s['items']) for s in SECTIONS)
print(f'共 {len(SECTIONS)} 方向，{total} 条')
