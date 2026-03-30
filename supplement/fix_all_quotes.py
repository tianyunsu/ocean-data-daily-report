#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自动修复feishu_write_doc.py中所有嵌套半角双引号的语法错误"""
import ast
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

max_iter = 20
for i in range(max_iter):
    try:
        ast.parse(content)
        print(f"Syntax OK after {i} fixes ✅")
        break
    except SyntaxError as e:
        lineno = e.lineno
        lines = content.splitlines(keepends=True)
        bad_line = lines[lineno - 1]
        # 找到该行中嵌套的英文论文标题（被双引号包围）
        # 模式：在 "...  "Title Here"  ... " 中，内层双引号是问题
        # 策略：查找 "字符串中嵌套的 "标题" 格式，替换为《标题》
        # 使用正则：找到 "..."...内层双引号..."  这样的模式
        # 简单策略：如果行中有 \" 后紧跟英文字母（title内容），就替换为《》
        
        # 找出行中所有被 " 包围的英文字符串片段
        # 用正则匹配 "([A-Za-z][^"]{5,}[A-Za-z.?!])"
        new_line = re.sub(
            r'"([A-Za-z][A-Za-z0-9 \-:,&/+.\']+[A-Za-z.?!])"',
            r'《\1》',
            bad_line
        )
        if new_line == bad_line:
            # 尝试另一种替换：直接对该行所有内层引号对替换
            # 找到字符串边界内的双引号
            print(f"Cannot auto-fix line {lineno}: {repr(bad_line[:100])}")
            break
        lines[lineno - 1] = new_line
        content = ''.join(lines)
        print(f"Fixed line {lineno}: removed inline double quotes")

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
