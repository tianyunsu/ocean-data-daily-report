#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报数据源文件（模板）
将 SECTIONS = [...] 放在此处，gen_html.py 会读取此文件。
"""

# ↓ 占位：每日由 build_daily.py 自动替换 ↓
SECTIONS = [
    {"title": "一、海洋人工智能", "en": "Ocean AI / Marine Artificial Intelligence", "items": []},
    {"title": "二、海洋数字孪生", "en": "Ocean Digital Twin / Marine Digital Twin", "items": []},
    {"title": "三、海洋可视化", "en": "Ocean Visualization / Geospatial Display", "items": []},
    {"title": "四、海洋数据质量", "en": "Ocean Data Quality Control", "items": []},
    {"title": "五、海洋数据处理", "en": "Ocean Data Processing / Computing", "items": []},
    {"title": "六、海洋数据管理与共享", "en": "Ocean Data Management & Sharing", "items": []},
    {"title": "七、开放航次与科考", "en": "Open Cruises / Research Expeditions", "items": []},
    {"title": "八、海洋数据中心", "en": "Ocean Data Centers / Infrastructure", "items": []},
    {"title": "九、工具与代码资源", "en": "Tools & Code Resources", "items": []},
]
# ↑ 以上由脚本自动维护，勿手动编辑 ↑


# ========== 以下为 feishu/docx 写入代码（无需修改）==========
def tr(text, bold=False, link=None):
    element = {"text_run": {"content": text}}
    if bold: element["text_run"]["style"] = {"bold": True}
    if link: element["text_run"]["link"] = {"url": link}
    return element

def paragraph(elements):
    return {"block_type": 2, "text": {"elements": elements, "style": {}}}

def heading(text, level=1):
    prefix = {1: "\u3010", 2: "  >> "}.get(level, "    ")
    suffix = {1: "\u3011", 2: ""}.get(level, "")
    return paragraph([tr(prefix + text + suffix, bold=True)])

def divider():
    return paragraph([tr("\u2500" * 50)])

def item_block(num, title, badge, abstract, source, date, url):
    blocks = []
    badge_text = badge if badge else ""
    title_text = f"{badge_text} {title}" if badge_text else title
    blocks.append(paragraph([tr(f"  {num}. ", bold=True), tr(title_text, bold=True, link=url)]))
    blocks.append(paragraph([tr(abstract)]))
    meta_parts = []
    if source: meta_parts.append(f"来源：{source}")
    if date: meta_parts.append(f"日期：{date}")
    if url: meta_parts.append(f"链接：{url}")
    blocks.append(paragraph([tr(" | ".join(meta_parts), bold=False)]))
    blocks.append(divider())
    return blocks

def section_block(title, en_title, items):
    blocks = []
    blocks.append(heading(title, 1))
    blocks.append(paragraph([tr(en_title, bold=False)]))
    blocks.append(divider())
    for i, item in enumerate(items, 1):
        blocks.extend(item_block(i, item.get('title', ''), item.get('badge', ''),
                                 item.get('abstract', ''), item.get('source', ''),
                                 item.get('date', ''), item.get('url', '')))
    return blocks

# feishu API 相关函数（如不写入飞书可忽略）
# 包含: get_tenant_token, create_document_and_write, write_blocks_to_doc, main 等
# 如有需要请从原版 feishu_write_doc.py 复制
