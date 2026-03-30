#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复feishu_write_doc.py中在Python字符串中嵌套的中文引号"""

import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 全局替换所有中文引号为书名号（在字符串内部使用）
# 先找出所有SyntaxError
while True:
    try:
        ast.parse(content)
        print("语法验证通过 ✅")
        break
    except SyntaxError as e:
        lineno = e.lineno
        lines = content.splitlines()
        bad_line = lines[lineno - 1]
        print(f"Error at line {lineno}: {bad_line[:80]}")
        # 找到该行中的中文引号并替换
        new_line = bad_line.replace('\u201c', '《').replace('\u201d', '》')
        if new_line == bad_line:
            print(f"无法自动修复，请手动检查：{bad_line}")
            break
        lines[lineno - 1] = new_line
        content = '\n'.join(lines)
        print(f"  -> 已修复第{lineno}行")

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("文件已保存")
