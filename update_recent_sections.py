#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新SECTIONS数据，确保只包含最近一周（3月23日-3月30日）的内容
并删除重复内容，重新编号
"""

import sys
import os
from datetime import datetime, timedelta
import re

# 导入现有SECTIONS数据
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from feishu_write_doc import SECTIONS as old_sections

def get_recent_week_dates():
    """获取最近一周的日期范围（2026-03-23 到 2026-03-30）"""
    today = datetime(2026, 3, 30)  # 固定今天为2026-03-30
    week_ago = today - timedelta(days=7)
    return week_ago.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d')

def is_recent_date(date_str, start_date, end_date):
    """检查日期是否在最近一周内"""
    # 处理各种日期格式
    if not date_str:
        return False
    
    # 提取YYYY-MM-DD格式的日期
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', date_str)
    if date_match:
        date_part = date_match.group(1)
        return start_date <= date_part <= end_date
    
    # 检查是否包含"持续更新"、"征稿中"等字样
    if any(keyword in date_str for keyword in ['持续', '征稿', '进行中', '运营', '更新']):
        return True
    
    return False

def extract_title_keywords(title):
    """从标题中提取关键词用于去重"""
    # 移除序号和特殊字符
    clean_title = re.sub(r'^\d+\.\s*', '', title)
    # 移除括号内容
    clean_title = re.sub(r'\[.*?\]', '', clean_title)
    # 提取前5个词作为关键词
    words = clean_title.split()
    return ' '.join(words[:5]).lower()

def deduplicate_and_renumber(sections, start_date, end_date):
    """去重并重新编号"""
    seen_titles = set()
    new_sections = []
    
    for section in sections:
        new_items = []
        for item in section['items']:
            # 检查日期是否符合要求
            if not is_recent_date(item['date'], start_date, end_date):
                continue
            
            # 提取关键词进行去重
            keywords = extract_title_keywords(item['title'])
            if keywords in seen_titles:
                continue
            seen_titles.add(keywords)
            
            new_items.append(item)
        
        # 重新编号
        for i, item in enumerate(new_items, 1):
            # 移除原有序号
            title = re.sub(r'^\d+\.\s*', '', item['title'])
            # 添加新序号
            item['title'] = f'{i}. {title}'
        
        if new_items:  # 只保留有内容的section
            new_section = section.copy()
            new_section['items'] = new_items
            new_sections.append(new_section)
    
    return new_sections

def main():
    start_date, end_date = get_recent_week_dates()
    print(f"筛选日期范围: {start_date} 到 {end_date}")
    
    # 去重并重新编号
    new_sections = deduplicate_and_renumber(old_sections, start_date, end_date)
    
    # 统计信息
    total_items = sum(len(s['items']) for s in new_sections)
    print(f"处理后: {len(new_sections)} 个方向，{total_items} 条动态")
    
    # 生成新的SECTIONS代码
    sections_code = "SECTIONS = [\n"
    for i, section in enumerate(new_sections):
        sections_code += f"    {{\n"
        sections_code += f"        'title': '{section['title']}',\n"
        sections_code += f"        'en': '{section['en']}',\n"
        sections_code += f"        'items': [\n"
        
        for item in section['items']:
            sections_code += f"            {{\n"
            sections_code += f"                'title': '{item['title']}',\n"
            sections_code += f"                'badge': '{item['badge']}',\n"
            sections_code += f"                'abstract': (\n"
            # 处理多行摘要
            abstract_lines = item['abstract'].split('\n')
            for line in abstract_lines:
                sections_code += f"                    '{line.strip()}'\n"
            sections_code += f"                ),\n"
            sections_code += f"                'source': '{item['source']}',\n"
            sections_code += f"                'date': '{item['date']}',\n"
            sections_code += f"                'url': '{item['url']}'\n"
            sections_code += f"            }},\n"
        
        sections_code += f"        ]\n"
        sections_code += f"    }},\n" if i < len(new_sections) - 1 else "    }\n"
    
    sections_code += "]\n"
    
    # 写入新文件
    output_file = "feishu_write_doc_updated.py"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sections_code)
    
    print(f"\n[OK] 已生成更新后的SECTIONS数据到: {output_file}")
    print(f"   请手动替换 feishu_write_doc.py 中的SECTIONS部分")

if __name__ == "__main__":
    main()