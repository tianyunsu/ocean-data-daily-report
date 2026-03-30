#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复title字段中的嵌套中文双引号，以及其他剩余问题"""
import ast
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复 "title" 字段中的嵌套双引号（中文）
# 模式："title": "xxx"中文内容"xxx"   ->   "title": "xxx「中文内容」xxx"
def fix_title_quotes(content):
    lines = content.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if '"title":' in line:
            # 找到标题值部分
            # pattern: "title": "...\"...\"..."
            # 用更宽松的方式：找到该行的中文引号包围的中文
            # 替换模式：在标题值中，"中文"  ->  「中文」
            # 先找标题值的起始位置
            m = re.search(r'"title":\s*"(.*)"', line)
            if m:
                title_val = m.group(1)
                # 在title_val中找嵌套的双引号
                # 替换中文字符被双引号包围的模式
                fixed_title = re.sub(r'"([\u4e00-\u9fff][^"]{1,30}[\u4e00-\u9fff])"', r'「\1」', title_val)
                if fixed_title != title_val:
                    new_line = line.replace(title_val, fixed_title, 1)
                    lines[i] = new_line
                    print(f"Fixed title at line {i+1}: {repr(title_val[:60])} -> {repr(fixed_title[:60])}")
    return ''.join(lines)

content = fix_title_quotes(content)

# Also fix any remaining 《》 in code sections
# by scanning for 《xxx》 patterns that are clearly dictionary keys (short, no spaces)
import re

max_iter = 30
for iteration in range(max_iter):
    try:
        ast.parse(content)
        print(f"Syntax OK ✅ (after {iteration} iterations)")
        break
    except SyntaxError as e:
        lineno = e.lineno
        lines = content.splitlines(keepends=True)
        bad_line = lines[lineno - 1]
        print(f"Error at line {lineno}: {repr(bad_line[:140])}")
        
        # Try various patterns
        new_line = bad_line
        
        # Fix: "..."Chinese"..." in title field
        new_line = re.sub(r'"([\u4e00-\u9fff][^"]{1,30}[\u4e00-\u9fff])"', r'「\1」', new_line)
        
        if new_line == bad_line:
            # Fix: "English Title" in title field
            new_line = re.sub(r'"([A-Za-z][A-Za-z0-9 \-:,&/+.\'\(\)!?_]{4,})"', r'《\1》', new_line)
        
        if new_line != bad_line:
            lines[lineno - 1] = new_line
            content = ''.join(lines)
            print(f"  -> Fixed!")
        else:
            print(f"  -> Cannot auto-fix!")
            for j in range(max(0, lineno-3), min(len(lines), lineno+4)):
                print(f"    {j+1}: {repr(lines[j][:140])}")
            break

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
