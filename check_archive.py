#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('archive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the 2026-04-24 entry
idx = content.find('2026-04-24')
if idx >= 0:
    snippet = content[idx-10:idx+500]
    print("Archive 2026-04-24 entry:")
    print(snippet)
else:
    print("NOT FOUND in archive.html")
