#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全面修复：在SECTIONS数据结束之后，将所有被错误替换的《》恢复为代码中正确的双引号"""
import ast
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到SECTIONS结束的位置
sections_end = content.find(']  # END SECTIONS')
if sections_end == -1:
    # 找到 SECTIONS 结束的位置 (最后一个 ]\n\n\n 或者 ]\n\n\ndef )
    # 找到SECTIONS开始
    sections_start = content.find('SECTIONS = [')
    # 找到其后的第一个函数定义
    func_match = re.search(r'\n\ndef ', content[sections_start:])
    if func_match:
        sections_end = sections_start + func_match.start()
    else:
        sections_end = len(content)

print(f"SECTIONS ends around position: {sections_end}")
print(f"Total content length: {len(content)}")

# 将SECTIONS之后的代码部分中的《》恢复为"
code_part = content[sections_end:]
data_part = content[:sections_end]

# 在代码部分，将所有 《word》 恢复为 "word"
# 但要小心：只恢复那些原本是Python字符串键/值的
def restore_code_quotes(code):
    # 模式：d.get(《word》)  ->  d.get("word")
    code = re.sub(r'\.get\(《([^》]+)》\)', r'.get("\1")', code)
    # 模式：d[《word》]  ->  d["word"]
    code = re.sub(r'\[《([^》]+)》\]', r'["\1"]', code)
    # 模式：{《word》: ...}  ->  {"word": ...}
    code = re.sub(r'\{《([^》]+)》:', r'{"\1":', code)
    # 模式：, 《word》:  ->  , "word":
    code = re.sub(r',\s*《([^》]+)》:', lambda m: m.group(0).replace('《', '"').replace('》', '"'), code)
    return code

code_part_fixed = restore_code_quotes(code_part)
if code_part_fixed != code_part:
    print("Fixed code part 《》 -> \"\"")
content = data_part + code_part_fixed

# Verify
try:
    ast.parse(content)
    print("Syntax OK ✅")
except SyntaxError as e:
    lineno = e.lineno
    lines = content.splitlines()
    print(f"Still error at line {lineno}: {e.msg}")
    for i in range(max(0, lineno-3), min(len(lines), lineno+4)):
        print(f"  {i+1}: {repr(lines[i][:150])}")

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")
