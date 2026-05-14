# -*- coding: utf-8 -*-
import re

content = open('feishu_write_doc.py', 'r', encoding='utf-8').read()

# Find all dates
dates = re.findall(r"'date': '([0-9-]+)'", content)
print(f"Total dates found: {len(dates)}")
print(f"Expected: 31")

# Quick syntax check: try to extract SECTIONS via subprocess
import subprocess
result = subprocess.run(
    ['python', '-c', '''
import ast, sys
content = open('feishu_write_doc.py', encoding='utf-8').read()
# Try compiling
try:
    compile(content, 'feishu_write_doc.py', 'exec')
    print("COMPILE OK")
except SyntaxError as e:
    print(f"SYNTAX ERROR: {e}")
'''],
    capture_output=True, text=True, encoding='utf-8'
)
print(result.stdout)
print(result.stderr)
