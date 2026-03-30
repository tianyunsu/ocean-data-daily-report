#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.splitlines(keepends=True)

# 修复第69行（0-indexed: 68）
line = lines[68]
# 替换嵌套的半角双引号包围的论文标题
old_part = '"Deep Learning for Ocean Forecasting: A Comprehensive Review"'
new_part = '《Deep Learning for Ocean Forecasting: A Comprehensive Review》'
if old_part in line:
    lines[68] = line.replace(old_part, new_part)
    print(f"Fixed line 69")
else:
    print(f"Not found in line 69, current: {repr(line[:100])}")

content2 = ''.join(lines)

# 验证语法
try:
    ast.parse(content2)
    print("Syntax OK ✅")
    with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
        f.write(content2)
    print("File saved")
except SyntaxError as e:
    print(f"Still error at line {e.lineno}: {e.msg}")
    err_lines = content2.splitlines()
    for i in range(max(0, e.lineno-3), min(len(err_lines), e.lineno+3)):
        print(f"  {i+1}: {repr(err_lines[i][:120])}")
