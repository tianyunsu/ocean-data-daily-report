#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复被错误替换的代码逻辑部分"""
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复被错误替换的代码行
bad_patterns = [
    ('item.get(《badge》)', 'item.get("badge")'),
    ('item.get(《abstract》)', 'item.get("abstract")'),
    ('item.get(《source》)', 'item.get("source")'),
    ('item.get(《date》)', 'item.get("date")'),
    ('item.get(《url》)', 'item.get("url")'),
    ('item.get(《title》)', 'item.get("title")'),
    ('item[《badge》]', 'item["badge"]'),
    ('item[《abstract》]', 'item["abstract"]'),
    ('item[《source》]', 'item["source"]'),
    ('item[《date》]', 'item["date"]'),
    ('item[《url》]', 'item["url"]'),
    ('item[《title》]', 'item["title"]'),
    ('sec[《title》]', 'sec["title"]'),
    ('sec[《en》]', 'sec["en"]'),
    ('sec[《items》]', 'sec["items"]'),
    # Also fix abstract tuple patterns that got incorrectly converted
    # "(《A machine learning approach..." -> fix back for the ones that are code not data
]

for old, new in bad_patterns:
    if old in content:
        count = content.count(old)
        content = content.replace(old, new)
        print(f"Restored {count}x: {old} -> {new}")

# Now verify
try:
    ast.parse(content)
    print("Syntax OK ✅")
except SyntaxError as e:
    lineno = e.lineno
    lines = content.splitlines()
    print(f"Still error at line {lineno}: {e.msg}")
    for i in range(max(0, lineno-3), min(len(lines), lineno+3)):
        print(f"  {i+1}: {repr(lines[i][:140])}")

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
