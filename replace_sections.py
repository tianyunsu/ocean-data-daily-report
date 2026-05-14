# -*- coding: utf-8 -*-
"""Correct SECTIONS replacement for 2026-04-24 fix"""
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# All 9 replacements as (old_substring, new_substring)
# Pattern: replace ONLY the item dict content, keep bracket structure
# Strategy: match unique portion of title + end with } or },

replacements = []

# ---- Helper ----
def make_replacement(old_title_start, new_full_item, is_last_in_section):
    """old_title_start: unique string that identifies the old item (includes leading chars)
    new_full_item: complete new item including leading }, { (for middle) or just { (for last)
    is_last_in_section: True if item is last in its section (ends with }}})
    """
    # Find the old item in content
    idx = content.find(old_title_start)
    if idx < 0:
        print(f"NOT FOUND: {old_title_start[:50]}")
        return
    # Find where this item ends
    # For middle items: find }, { which starts next item
    # For last items: find }}} (item close + items list close + section close)
    if is_last_in_section:
        # Look for the }}]} pattern at end of this section's last item
        # The item ends at the first } that is followed by }]}
        # Find 'title': of NEXT section to know where this item ends
        # Alternative: find the closing }}}} and look for what comes after
        # Actually for last items: the item dict ends with }}
        # But in the raw file: items = [..., {item}]]}, so after item there's ]]
        # Then }, { starts next section
        # So look for '}}]}' followed by something
        search_start = idx + len(old_title_start)
        # Find the end of the item by looking for pattern '}} (item)} (section)} (SECTIONS list),'
        # Look ahead for pattern: 'date_str'}}' and then check
        pass
    else:
        # For middle items: item ends with },
        # Next item starts with }, {
        next_item = content.find("}, {'title':", search_start)
        if next_item < 0:
            print(f"Cannot find next item for: {old_title_start[:50]}")
            return
        old_item_end = next_item + 2  # include the }, before next item
        old_item = content[idx:old_item_end]
        replacements.append((old_item, new_full_item))
        print(f"Found: {old_title_start[:40]} -> ends at {old_item_end}")

# ---- ITEMS TO REPLACE ----
# Format: (unique_old_title_start, new_item_string, is_last_in_section)

items_to_replace = [
    # 二-1: EDITO Phase 2 (MIDDLE, not last in section 2)
    ("'title': '1. CORDIS\uff082025-08 ~ 2026\uff09\uff1aEDITO Phase 2\u2014\u2014\u6b27\u6d32\u6570\u5b57\u5b12\u751f\u6d77\u6d0b\u7b2c\u4e8c\u9636\u6bb5\u83b7EU\u8d44\u52a9\u542f\u52a8', 'badge': '\u8fd11\u6708', 'abstract': '\u6b27\u76df\u59d4\u5458\u4f1a",
     ", {'title': '1. INESC TEC\uff082026-04-10\uff09\uff1a\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u4e92\u64cd\u4f5c\u6027\u53d6\u5f97\u65b0\u8fdb\u5c55\u2014\u2014\u4ece\u5e03\u9c81\u585e\u5c14\u5230\u683c\u62c9\u65af\u54e5\u7684\u8de8\u5e73\u53f0\u534f\u4f5c', 'badge': '\u8fd1\u7d27\u5929', 'abstract': 'INESC TEC\u4e8e2026\u5e744\u670810\u65e5\u53d1\u5e03\u6700\u65b0\u52a8\u6001\uff0c\u4ecb\u7ecd\u5176\u5728\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u4e92\u64cd\u4f5c\u6027\u548c\u53ef\u79fb\u690d\u6027\u65b9\u9762\u7684\u524d\u6cbf\u8fdb\u5c55\u3002\u4ece\u5e03\u9c81\u585e\u5c14\u5230\u683c\u62c9\u65af\u54e5\uff0cINESC TEC\u5728\u591a\u4e2a\u56fd\u9645\u5e73\u53f0\u63a8\u52a8\u4e86\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u6a21\u578b\u3001\u670d\u52a1\u3001\u6d41\u7a0b\u548c\u6570\u636e\u7684\u4e92\u64cd\u4f5c\u6027\u6807\u51c6\u5efa\u7acb\uff0c\u5e76\u4e0eEDITO Phase 2\u7b49\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u9879\u76ee\u6df1\u5ea6\u534f\u4f5c\uff0c\u5171\u540c\u63a8\u52a8\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u6d77\u6d0b\u7684\u5f00\u653e\u751f\u6001\u7cfb\u7edf\u5efa\u8bbe\u3002', 'source': 'INESC TEC', 'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec', 'date': '2026-04-10'},",
     False),

    # 二-3: hellosea DTO (LAST in section 2)
    ("'title': '3. hellosea.org\uff082024\u81f3\u4eca\uff09\uff1a\u4e2d\u56fd\u6b63\u6b3a\u81ea\u4e3b\u7814\u53d1\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u5f15\u64ce\u2014\u2014DTO\u7efc\u5408\u89e3\u51b3\u65b9\u6848\u5e73\u53f0', 'badge': '\u8fd11\u6708', 'abstract': '\u4e2d\u56fd\u81ea\u4e3b\u7814\u53d1\u7684\u6570\u5b57\u5b12\u751f\u6d77\u6d0b\uff08DTO\uff09\u5e73\u53f0dto.hellosea.org.cn\u6301\u7eed\u8fd0\u8425\uff0c\u63d0\u4f9b\u6d89\u53ca\u6d77\u6d0b\u6570\u5b57\u79d1\u5b66\u7684\u5168\u9762\u89e3\u51b3\u65b9\u6848\uff0c\u5305\u62ec\u6570\u5b57\u5b12\u751f\u9a71\u52a8\u5f15\u64ce\u3001\u6d77\u6d0b\u591a\u5c3a\u5ea6\u4eff\u771f\u3001\u53ef\u89c6\u5316\u5c55\u793a\u548c\u6570\u636e\u670d\u52a1\u3002\u8be5\u5e73\u53f0\u662f\u56fd\u5185\u5728\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u9886\u57df\u7684\u91cd\u8981\u5b9e\u8df5\u6848\u4f8b\uff0c\u652f\u6301\u6d77\u6d0b\u79d1\u7814\u3001\u7ba1\u7406\u548c\u51b3\u7b56\u5e94\u7528\uff0c\u4e0e\u6b27\u6d32EDITO\u5f62\u6210\u4e92\u8865\u683c\u5c40\u3002', 'source': 'Digital Twin of the Ocean - hellosea.org.cn', 'url': 'https://dto.hellosea.org.cn/', 'date': '2024-07-18'",
     "{'title': '3. DITTO Programme\uff082026\uff09\uff1a\u8054\u5408\u56fd\u6d77\u6d0b\u5341\u5e74\u6570\u5b57\u5b12\u751f\u6d77\u6d0b\u8ba1\u5212\u2014\u2014\u5168\u7403DTO\u6cbb\u7406\u6846\u67b6\u4e0e\u534f\u4f5c\u5e73\u53f0', 'badge': '\u8fd1\u7d27\u5929', 'abstract': 'DITTO\uff08Digital Twins of the Ocean\uff09\u662f\u7531\u8054\u5408\u56fd\u6d77\u6d0b\u5341\u5e74\u8ba4\u53ef\u7684\u5168\u7403\u6027\u534f\u4f5c\u8ba1\u5212\uff0c\u65e8\u5728\u901a\u8fc7\u6570\u5b57\u5b12\u751f\u6280\u672f\u63a8\u52a8\u6d77\u6d0b\u4fdd\u62a4\u3001\u6d77\u6d0b\u6cbb\u7406\u548c\u53ef\u6301\u7eed\u84dd\u8272\u7ecf\u6d4e\u53d1\u5c55\u3002DITTO\u5c1a\u672f\u5efa\u7acb\u6d77\u6d0b\u6570\u5b57\u5b12\u751f\u7684\u901a\u7528\u7406\u89e3\u6846\u67b6\u3001\u4e92\u64cd\u4f5c\u6807\u51c6\u548c\u201c\u5047\u8bbe\u201d\u60c5\u666f\u6a21\u62df\u80fd\u529b\uff0c\u6c47\u805a\u5168\u7403\u79d1\u5b66\u5bb6\u3001\u653f\u7b56\u5236\u5b9a\u8005\u548c\u884c\u4e1a\u7528\u6237\u30022026\u5e74\u5c06\u5728\u65e5\u672c\u4e3e\u529eDITTO\u65d7\u8236\u5cf0\u4f1a\uff08International DITTO Summit 2026\uff09\uff0c\u63a8\u52a8\u6570\u5b57\u5b12\u751f\u6d77\u6d0b\u4ece\u6280\u672f\u539f\u578b\u5411\u5927\u89c4\u6a21\u5b9e\u9645\u5e94\u7528\u8f6c\u578b\u3002', 'source': 'DITTO / UN Ocean Decade', 'url': 'https://ditto-oceandecade.org/', 'date': '2026-04-24'}",
     True),
]

print("Starting replacements...")
for old, new, is_last in items_to_replace:
    if old in content:
        print(f"Found: {old[:60]}")
        content = content.replace(old, new, 1)
    else:
        print(f"NOT FOUND: {old[:60]}")

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
