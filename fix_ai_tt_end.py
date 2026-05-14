# -*- coding: utf-8 -*-
content = open('feishu_write_doc.py', encoding='utf-8').read()

# The AI-TT item is missing its }} closing.
# Find it and add }} after the date
old_ai_tt_end = "'date': '2026-04-13'}"
new_ai_tt_end = "'date': '2026-04-13'}}}"

if old_ai_tt_end in content:
    content = content.replace(old_ai_tt_end, new_ai_tt_end, 1)
    with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed!')
else:
    # Check what's actually there
    date_str = "'date': '2026-04-13'"
    idx = content.index(date_str)
    print(f'Found date at: {idx}')
    print(f'Context: {repr(content[idx:idx+20])}')
    # What we expect vs what's there
    after = content[idx+len(date_str):idx+len(date_str)+5]
    print(f'After date: {repr(after)}')
