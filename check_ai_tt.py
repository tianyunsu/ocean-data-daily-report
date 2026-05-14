# -*- coding: utf-8 -*-
content = open('feishu_write_doc.py', encoding='utf-8').read()
idx = content.find('AI-TT')
print(f'Found AI-TT at: {idx}')

# Find the end of the date string for AI-TT
date_literal = "'date': '2026-04-13'"
date_end = content.index(date_literal) + len(date_literal)
print(f'Date ends at: {date_end}')
print(f'After date: {repr(content[date_end:date_end+30])}')

# Find the next section (starts with 六、海洋数据管理与共享服务)
# Search for 'title': followed by a section number pattern
next_sec_pattern = "'title': '"
next_pos = date_end
found_section6 = False
while next_pos < len(content):
    pos = content.find(next_sec_pattern, next_pos)
    if pos < 0:
        break
    # Check if this is section 6 by looking ahead
    snippet = content[pos:pos+100]
    if '\u516d' in snippet or '6.' in snippet:
        print(f'Next section found at: {pos}')
        print(f'Context: {repr(snippet[:80])}')
        print(f'Between AI-TT and section 6: {repr(content[date_end:pos])}')
        found_section6 = True
        break
    next_pos = pos + 1

if not found_section6:
    print('Section 6 not found')
