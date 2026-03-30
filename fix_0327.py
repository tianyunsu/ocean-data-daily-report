#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 先检查语法错误位置
try:
    ast.parse(content)
    print('语法已正确 ✅')
    exit(0)
except SyntaxError as e:
    print(f'语法错误第 {e.lineno} 行: {e.msg}')
    lines = content.splitlines()
    for i in range(max(0, e.lineno-3), min(len(lines), e.lineno+2)):
        print(f'  {i+1}: {repr(lines[i][:120])}')

# 修复所有中文引号嵌套问题（在Python字符串内部）
# 这些中文引号 \u201c 和 \u201d 导致字符串提前结束
import re

def fix_nested_quotes_in_strings(content):
    lines = content.splitlines(keepends=True)
    fixed_lines = []
    for line in lines:
        # 检测行是以字符串内容开始的（以4个空格+引号开始）
        stripped = line.strip()
        # 如果该行是纯字符串内容（以 " 开始和结束，中间有中文引号嵌套）
        if stripped.startswith('"') and stripped.endswith('",'):
            inner = stripped[1:-2]  # 去掉首尾引号和逗号
            # 检查内部是否有未转义的半角双引号
            # 用书名号替换内部的中文引号（左引号\u201c 和右引号\u201d）
            new_inner = inner.replace('\u201c', '\u300a').replace('\u201d', '\u300b')
            if new_inner != inner:
                indent = line[:len(line) - len(line.lstrip())]
                line = indent + '"' + new_inner + '",\n'
        elif stripped.startswith('"') and stripped.endswith('"'):
            inner = stripped[1:-1]
            new_inner = inner.replace('\u201c', '\u300a').replace('\u201d', '\u300b')
            if new_inner != inner:
                indent = line[:len(line) - len(line.lstrip())]
                line = indent + '"' + new_inner + '"\n'
        fixed_lines.append(line)
    return ''.join(fixed_lines)

content2 = fix_nested_quotes_in_strings(content)
if content2 != content:
    print(f'替换了中文引号')
    content = content2

# 修复半角双引号嵌套
def fix_half_nested_quotes(content):
    lines = content.splitlines(keepends=True)
    fixed_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        # 字符串内容行：以 " 开始，以 ", 结束
        if stripped.startswith('"') and (stripped.endswith('",') or stripped.endswith('"')):
            # 去掉首尾
            if stripped.endswith('",'):
                inner = stripped[1:-2]
                suffix = '",\n'
            else:
                inner = stripped[1:-1]
                suffix = '"\n'
            # 检查inner中是否有裸的 " (未转义)
            # 统计引号：偶数个是成对的，奇数个说明有问题
            quote_count = inner.count('"')
            if quote_count > 0:
                # 有嵌套引号，替换为书名号
                new_inner = inner.replace('"', '《', 1)
                # 如果还有 " 再替换
                idx = new_inner.find('"')
                while idx != -1:
                    new_inner = new_inner[:idx] + '》' + new_inner[idx+1:]
                    idx = new_inner.find('"')
                if new_inner != inner:
                    indent = line[:len(line) - len(line.lstrip())]
                    line = indent + '"' + new_inner + suffix
        fixed_lines.append(line)
    return ''.join(fixed_lines)

# 只对 SECTIONS 内容区应用半角引号修复
# 找到 SECTIONS 开始和结束位置
sections_start = content.find('SECTIONS = [')
sections_end_idx = sections_start
depth = 0
i = sections_start
while i < len(content):
    if content[i] == '[':
        depth += 1
    elif content[i] == ']':
        depth -= 1
        if depth == 0:
            sections_end_idx = i
            break
    i += 1

sections_part = content[sections_start:sections_end_idx+1]
rest_after = content[sections_end_idx+1:]
before = content[:sections_start]

sections_fixed = fix_half_nested_quotes(sections_part)
if sections_fixed != sections_part:
    print('修复了SECTIONS中的半角引号嵌套')
    content = before + sections_fixed + rest_after

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)

try:
    ast.parse(content)
    print('语法验证通过 ✅')
except SyntaxError as e:
    print(f'仍有语法错误 ❌ 第 {e.lineno} 行: {e.msg}')
    lines = content.splitlines()
    for j in range(max(0, e.lineno-3), min(len(lines), e.lineno+2)):
        print(f'  {j+1}: {repr(lines[j][:120])}')
