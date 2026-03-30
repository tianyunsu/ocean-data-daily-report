#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量修复feishu_write_doc.py中所有嵌套半角双引号的语法错误
   策略：把文件内所有 论文"..." 或 题为"..." 模式替换为 论文《...》 或 题为《...》
"""
import ast
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 批量替换已知的中文描述词后紧跟英文标题的双引号模式
patterns = [
    # 论文"Title"  ->  论文《Title》
    (r'论文"([^"\n]+)"', r'论文《\1》'),
    # 题为"Title"  ->  题为《Title》
    (r'题为"([^"\n]+)"', r'题为《\1》'),
    # 方法"Title"  ->  方法《Title》
    (r'方法"([^"\n]+)"', r'方法《\1》'),
    # 报告"Title"  ->  报告《Title》
    (r'报告"([^"\n]+)"', r'报告《\1》'),
]

for pattern, replacement in patterns:
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        count = len(re.findall(pattern, content))
        print(f"Pattern '{pattern[:30]}' fixed {count} occurrence(s)")
        content = new_content

# 验证语法
max_iter = 30
for i in range(max_iter):
    try:
        ast.parse(content)
        print(f"\nSyntax OK ✅")
        break
    except SyntaxError as e:
        lineno = e.lineno
        lines = content.splitlines(keepends=True)
        bad_line = lines[lineno - 1]
        print(f"Still error at line {lineno}: {repr(bad_line[:120])}")
        
        # Try to find any remaining "English Title" pattern and fix
        new_line = re.sub(r'"([A-Za-z][A-Za-z0-9 \-:,&/+.\'\(\)!?]{4,}[A-Za-z.?!])"', r'《\1》', bad_line)
        if new_line != bad_line:
            lines[lineno - 1] = new_line
            content = ''.join(lines)
            print(f"  -> Fixed with generic pattern!")
        else:
            print(f"  -> Cannot auto-fix!")
            break

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
