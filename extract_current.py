import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find SECTIONS start and end
sections_start = content.find("SECTIONS = [")
# Find end using bracket counting
depth = 0
in_sections = False
sections_end = 0
for i in range(sections_start, len(content)):
    c = content[i]
    if c == '[':
        depth += 1
        in_sections = True
    elif c == ']':
        depth -= 1
        if in_sections and depth == 0:
            sections_end = i
            break

sections_data = content[sections_start:sections_end+1]
print(f"SECTIONS length: {len(sections_data)} chars")
print(f"SECTIONS preview (first 2000 chars):")
print(repr(sections_data[:2000]))
