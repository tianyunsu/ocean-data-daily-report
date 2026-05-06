#!/usr/bin/env python3
"""
自动更新 sitemap.xml 脚本
每次生成新日报后自动调用，保持 sitemap.xml 与实际文章同步
"""

import os
import glob
from datetime import datetime

SITE_URL = "https://tianyunsu.github.io/ocean-data-daily-report"
POSTS_DIR = "posts"
OUTPUT_FILE = "sitemap.xml"

def generate_sitemap():
    """生成 sitemap.xml"""

    # 获取所有日报文件
    posts_dir = os.path.join(os.path.dirname(__file__), POSTS_DIR)
    if not os.path.exists(posts_dir):
        print(f"警告: {posts_dir} 目录不存在")
        return

    # 获取所有 HTML 文件
    html_files = glob.glob(os.path.join(posts_dir, "*.html"))
    posts = []

    for f in html_files:
        basename = os.path.basename(f)
        # 提取日期 (格式: YYYY-MM-DD.html)
        date_str = basename.replace(".html", "")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            posts.append((date_str, date))
        except ValueError:
            print(f"跳过无效文件名: {basename}")

    # 按日期倒序排列
    posts.sort(key=lambda x: x[1], reverse=True)

    # 生成 sitemap
    urls = []

    # 主页
    urls.append(f"""  <url>
    <loc>{SITE_URL}/</loc>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

    # 归档页
    urls.append(f"""  <url>
    <loc>{SITE_URL}/archive.html</loc>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>""")

    # 日报文章
    for date_str, date in posts:
        urls.append(f"""  <url>
    <loc>{SITE_URL}/posts/{date_str}.html</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")

    # 组装完整 XML
    sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
'''

    # 写入文件
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ sitemap.xml 已更新，共 {len(posts)} 篇日报 + 2 个页面")

if __name__ == "__main__":
    generate_sitemap()
