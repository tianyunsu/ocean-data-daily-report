#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
精确修复feishu_write_doc.py中的SECTIONS数据
只修复abstract内容中的嵌套双引号，不修改dict key或其他结构
"""
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 精确替换已知的嵌套引号问题
# 1. EDITO 第127行问题：承载着 EU 使命"恢复我们的海洋和水域"
old1 = '承载着 EU 使命"恢复我们的海洋和水域"。'
new1 = '承载着 EU 使命《恢复我们的海洋和水域》。'

# 2. EDITO 第129行问题：盛赞为"不可思议的工具"
old2 = '盛赞为"不可思议的工具"。'
new2 = '盛赞为《不可思议的工具》。'

content = content.replace(old1, new1)
content = content.replace(old2, new2)

print(f'替换1: {"成功" if old1 not in content else "未替换"}')
print(f'替换2: {"成功" if old2 not in content else "未替换"}')

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)

# 验证语法
try:
    ast.parse(content)
    print('语法验证通过 ✅')
except SyntaxError as e:
    print(f'仍有语法错误 第 {e.lineno} 行: {e.msg}')
    lines = content.splitlines()
    for j in range(max(0, e.lineno-3), min(len(lines), e.lineno+2)):
        print(f'  {j+1}: {repr(lines[j][:120])}')
