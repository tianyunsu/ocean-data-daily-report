#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分析 make_new_feishu.py 脚本，看看它到底生成了什么

with open('make_new_feishu.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"make_new_feishu.py length: {len(content)} chars")

# Find the new_sections_lines definition
pos = content.find('new_sections_lines')
if pos >= 0:
    # Extract the section around new_sections_lines
    snippet = content[pos:pos+5000]
    print("\nFirst 3000 chars of new_sections_lines area:")
    print(snippet[:3000])
