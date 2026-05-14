with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where sections actually start (indented block)
marker = "    {'title':"
sections_start = content.find(marker)
# Find the blank line before sections
preceding = content[:sections_start]

# Strip trailing newlines from header
header_clean = preceding.rstrip()
sections_text_raw = content[sections_start:]

# Reconstruct
new_content = header_clean + '\nSECTIONS = [\n' + sections_text_raw

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Fixed!')

# Verify syntax
try:
    compile(new_content, 'feishu_write_doc.py', 'exec')
    print('SYNTAX OK')
except SyntaxError as e:
    print(f'SYNTAX ERROR: {e}')
    # Show context around error
    import re
    lines = new_content.split('\n')
    err_line = e.lineno or 1
    for i in range(max(0, err_line-3), min(len(lines), err_line+2)):
        mark = '>>>' if i+1 == err_line else '   '
        print(f'{mark} L{i+1}: {repr(lines[i])}')
