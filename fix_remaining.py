#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复feishu_write_doc.py中剩余的嵌套半角双引号问题"""
import ast
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 额外修复模式
extra_patterns = [
    # 学习"好数据"的 -> 学习「好数据」的
    (r'学习"([^"\n]+)"', r'学习「\1」'),
    # 通过"..." -> 通过「...」
    (r'通过"([^"\n]+)"', r'通过「\1」'),
    # "autoQC: ..." 直接嵌入
    (r'\("([A-Za-z][^"\n]+)"\)', r'(《\1》)'),
    # 预印本（xxx）"Title" -> 预印本（xxx）《Title》
    (r'预印本（[^）]+）"([^"\n]+)"', lambda m: m.group(0).replace('"', '《', 1).replace('"', '》', 1) if m.group(0).count('"') == 2 else m.group(0)),
]

for pattern, replacement in extra_patterns:
    if callable(replacement):
        new_content = re.sub(pattern, replacement, content)
    else:
        new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        count = len(re.findall(pattern, content))
        print(f"Fixed {count} with pattern '{pattern[:40]}'")
        content = new_content

# Also fix: 通过学习"好数据" specifically
old_str = '通过学习"好数据"的行为特征识别异常样本，'
new_str = '通过学习「好数据」的行为特征识别异常样本，'
if old_str in content:
    content = content.replace(old_str, new_str)
    print("Fixed '好数据' quote")

# Iterate to fix remaining issues
max_iter = 30
for i in range(max_iter):
    try:
        ast.parse(content)
        print(f"\nSyntax OK ✅ (after {i} extra iterations)")
        break
    except SyntaxError as e:
        lineno = e.lineno
        lines = content.splitlines(keepends=True)
        bad_line = lines[lineno - 1]
        print(f"Error at line {lineno}: {repr(bad_line[:140])}")
        
        # Try generic fix: any "ASCII-title" pattern
        new_line = re.sub(r'"([A-Za-z][A-Za-z0-9 \-:,&/+.\'\(\)!?_]{4,}[A-Za-z.?!_])"', r'《\1》', bad_line)
        # Also try Chinese title
        new_line2 = re.sub(r'"([\u4e00-\u9fff][^"]{1,20}[\u4e00-\u9fff])"', r'「\1」', bad_line)
        
        if new_line != bad_line:
            lines[lineno - 1] = new_line
            content = ''.join(lines)
            print(f"  -> Fixed (English pattern)!")
        elif new_line2 != bad_line:
            lines[lineno - 1] = new_line2
            content = ''.join(lines)
            print(f"  -> Fixed (Chinese pattern)!")
        else:
            print(f"  -> Cannot auto-fix!")
            # Print more context
            for j in range(max(0, lineno-5), min(len(lines), lineno+5)):
                print(f"    {j+1}: {repr(lines[j][:100])}")
            break

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
