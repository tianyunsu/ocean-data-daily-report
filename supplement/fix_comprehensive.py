#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性修复feishu_write_doc.py中所有嵌套半角双引号的语法错误"""
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 手动修复已知的问题行
fixes = {
    # line 69 (0-indexed: 68)
    68: '                    "论文《Deep Learning for Ocean Forecasting: A Comprehensive Review》系统梳理了"\n',
    # line 143 (0-indexed: 142) - if still exists
}

for idx, new_line in fixes.items():
    print(f"Fixing line {idx+1}:")
    print(f"  OLD: {repr(lines[idx][:100])}")
    lines[idx] = new_line
    print(f"  NEW: {repr(lines[idx][:100])}")

content = ''.join(lines)

# Now iteratively fix any remaining double-quote nesting issues
max_iter = 30
for i in range(max_iter):
    try:
        ast.parse(content)
        print(f"\nSyntax OK after all fixes ✅")
        break
    except SyntaxError as e:
        lineno = e.lineno
        cur_lines = content.splitlines(keepends=True)
        bad_line = cur_lines[lineno - 1]
        print(f"Error at line {lineno}: {repr(bad_line[:120])}")
        
        # Strategy: find any "Title" pattern within the string and replace with 《Title》
        import re
        # Match: "...text..."text inside"...text..."
        # The inner quotes break the outer string
        # Try to find pattern: 论文"<english content>"  or  题为"<content>"
        new_line = re.sub(r'论文"([^"]+)"', r'论文《\1》', bad_line)
        if new_line == bad_line:
            new_line = re.sub(r'题为"([^"]+)"', r'题为《\1》', bad_line)
        if new_line == bad_line:
            new_line = re.sub(r'"([A-Za-z][A-Za-z0-9 \-:,&/+.\'\(\)!?]{5,}[A-Za-z.?!])"', r'《\1》', bad_line)
        
        if new_line != bad_line:
            cur_lines[lineno - 1] = new_line
            content = ''.join(cur_lines)
            print(f"  -> Fixed!")
        else:
            print(f"  -> Cannot auto-fix, breaking")
            break

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
