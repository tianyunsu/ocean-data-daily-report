#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publish_daily_report.py - 一键发布海洋AI技术日报到网站

功能：
1. 从 Claw/daily_reports/ 复制最新日报到网站 posts/
2. 自动更新首页 index.html（添加最新日报卡片）
3. 自动更新归档页 archive.html（添加归档条目）
4. git commit + push 到 GitHub

用法：
    python publish_daily_report.py              # 发布今日日报
    python publish_daily_report.py 2026-03-27   # 发布指定日期日报
"""

import os
import sys
import shutil
import re
from datetime import datetime, timedelta

# ============ 路径配置 ============
CLAW_DIR = r"C:\Users\Administrator\WorkBuddy\Claw"
SITE_DIR = r"C:\Users\Administrator\WorkBuddy\20260327163052\ocean-data-daily-report"
POSTS_DIR = os.path.join(SITE_DIR, "posts")
DAILY_REPORTS_DIR = os.path.join(CLAW_DIR, "daily_reports")

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def get_report_info(date_str):
    """从日期字符串解析信息"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = WEEKDAYS[dt.weekday()]
    date_cn = dt.strftime("%Y年%m月%d日")
    return dt, weekday, date_cn


def generate_post_card(date_str, dt, weekday, excerpt=""):
    """生成首页日报卡片 HTML"""
    return f'''
    <div class="post-card">
      <div class="post-date">{date_str} · {weekday}</div>
      <h2><a href="posts/{date_str}.html">{dt.strftime("%Y年%m月%d日")} 海洋AI技术日报</a></h2>
      <div class="post-excerpt">{excerpt}</div>
      <a href="posts/{date_str}.html" class="read-more">阅读全文 →</a>
    </div>'''


def generate_archive_item(date_str, weekday):
    """生成归档条目 HTML"""
    return f'        <li><a href="posts/{date_str}.html">{datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y年%m月%d日")} 海洋AI技术日报</a><span class="date">{date_str[5:]} · {weekday}</span></li>'


def extract_excerpt_from_html(html_path, max_len=120):
    """从日报 HTML 中提取摘要（取第一个 item-abstract）"""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'<div class="item-abstract">(.*?)</div>', content, re.DOTALL)
        if match:
            text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
            if len(text) > max_len:
                text = text[:max_len] + "..."
            return text
    except Exception:
        pass
    return "海洋AI · 数字孪生 · 可视化 · 数据质量 · 数据处理 · 共享服务 · 开放航次 · 数据中心 · 工具代码"


def update_index_html(date_str, dt, weekday, excerpt):
    """更新首页，在第一个 post-card 前插入新卡片"""
    index_path = os.path.join(SITE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否已存在该日期
    if f'posts/{date_str}.html' in content:
        print(f"  [跳过] 首页已包含 {date_str} 的链接")
        return False

    new_card = generate_post_card(date_str, dt, weekday, excerpt)

    # 在第一个 post-card 前插入
    if "<div class=\"post-card\">" in content:
        content = content.replace("<div class=\"post-card\">", new_card, 1)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] 首页已更新，添加 {date_str} 卡片")
        return True
    else:
        print("  [错误] 未找到 post-card 插入点")
        return False


def update_archive_html(date_str, weekday):
    """更新归档页"""
    archive_path = os.path.join(SITE_DIR, "archive.html")
    with open(archive_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否已存在
    if f'posts/{date_str}.html' in content:
        print(f"  [跳过] 归档页已包含 {date_str}")
        return False

    new_item = generate_archive_item(date_str, weekday)

    # 获取月份分组
    month_label = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y年%m月")

    # 查找对应月份分组
    month_pattern = rf'<h2>📅 {month_label}</h2>\s*<ul>'
    match = re.search(month_pattern, content)
    if match:
        # 在该月的 </ul> 前插入
        insert_pos = content.find("</ul>", match.start())
        if insert_pos != -1:
            content = content[:insert_pos].rstrip() + "\n" + new_item + "\n      </ul>" + content[insert_pos + 5:]
            with open(archive_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [OK] 归档页已更新，添加 {date_str} 到 {month_label}")
            return True

    # 如果月份分组不存在，创建新的
    new_group = f'''
    <div class="archive-group">
      <h2>📅 {month_label}</h2>
      <ul>
{new_item}
      </ul>
    </div>'''
    content = content.replace('<main class="container">', f'<main class="container">\n\n{new_group}', 1)
    with open(archive_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] 归档页已更新，创建新分组 {month_label}")
    return True


def publish(date_str):
    """主发布流程"""
    print(f"\n{'='*50}")
    print(f"  发布海洋AI技术日报: {date_str}")
    print(f"{'='*50}\n")

    dt, weekday, date_cn = get_report_info(date_str)

    # 1. 查找源文件
    src_candidates = [
        os.path.join(DAILY_REPORTS_DIR, f"海洋AI简报_{date_str}.html"),
        os.path.join(DAILY_REPORTS_DIR, f"海洋AI简报_{dt.strftime('%Y年%m月%d日')}.html"),
    ]

    src_file = None
    for candidate in src_candidates:
        if os.path.exists(candidate):
            src_file = candidate
            break

    if not src_file:
        print(f"  [错误] 未找到日报源文件")
        print(f"  搜索路径:")
        for c in src_candidates:
            print(f"    - {c}")
        print(f"\n  daily_reports 目录内容:")
        if os.path.exists(DAILY_REPORTS_DIR):
            for f in sorted(os.listdir(DAILY_REPORTS_DIR)):
                if f.endswith(".html"):
                    print(f"    - {f}")
        return False

    print(f"  [OK] 源文件: {src_file}")

    # 2. 复制到网站 posts 目录
    dst_file = os.path.join(POSTS_DIR, f"{date_str}.html")
    shutil.copy2(src_file, dst_file)
    print(f"  [OK] 复制到: {dst_file}")

    # 3. 提取摘要
    excerpt = extract_excerpt_from_html(dst_file)
    print(f"  [OK] 摘要: {excerpt[:60]}...")

    # 4. 更新首页
    update_index_html(date_str, dt, weekday, excerpt)

    # 5. 更新归档页
    update_archive_html(date_str, weekday)

    # 6. Git commit
    print(f"\n  --- Git 提交 ---")
    os.chdir(SITE_DIR)
    os.system(f'git add -A')
    os.system(f'git commit -m "publish: {date_cn} 海洋AI技术日报"')
    os.system(f'git push origin main')

    print(f"\n  [OK] 发布完成!")
    print(f"  预览: file:///{dst_file.replace(os.sep, '/')}")
    print(f"  线上: https://tianyunsu.github.io/ocean-data-daily-report/posts/{date_str}.html")
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        date_arg = sys.argv[1]
    else:
        date_arg = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    publish(date_arg)
