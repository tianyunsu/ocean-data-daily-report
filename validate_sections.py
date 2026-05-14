#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    src = f.read()
try:
    ast.parse(src)
    print('Syntax OK')
    exec_globals = {}
    exec(src, exec_globals)
    sections = exec_globals.get('SECTIONS', [])
    total = sum(len(s.get('items',[])) for s in sections)
    for s in sections:
        print("  {}: {} items".format(s['title'], len(s.get('items',[]))))
    print("Total items: {}".format(total))
except SyntaxError as e:
    print('SyntaxError:', e)
