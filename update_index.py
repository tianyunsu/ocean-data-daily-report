#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 更新 index.html 和 archive.html 中的 2026-04-24 卡片

# === Update index.html ===
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

old_card = """    <div class="post-card">
      <div class="post-date">2026-04-24 · 周五</div>
      <h2><a href="posts/2026-04-24.html">2026年04月24日 海洋AI技术日报</a></h2>
      <div class="post-excerpt">本期涵盖9个方向，共31条最新动态。重点包括：AGU GRL发表北极快速海冰融化驱动机制研究（2026-04-22）、Springer ConvLSTM南极海冰60天预报、arXiv ML大气强迫对比NWP研究、Blue-Cloud 2026发布9份可视化与数据处理培训材料（2026-04-21，含滑翔机工具箱/沿岸流合成图）、EDITO Phase 2 EU资助启动、HAD-QC混合AI Argo质控系统、NOAA NCEI全球Argo数据仓库更新（2026-04-13）、OCEANS 2026三亚大会征稿、Deltares dfm_tools CMEMS FTP迁移PR等。</div>
      <a href="posts/2026-04-24.html" class="read-more">阅读全文 →</a>
    </div>"""

new_card = """    <div class="post-card">
      <div class="post-date">2026-04-24 · 周五（已修正）</div>
      <h2><a href="posts/2026-04-24.html">2026年04月24日 海洋AI技术日报</a></h2>
      <div class="post-excerpt">本期涵盖9个方向，共30条最新动态（已修正超期内容）。重点包括：AGU GRL北极快速海冰融化驱动机制研究（2026-04-22）、Springer ConvLSTM南极海冰60天预报（2026-04-18）、INESC TEC海洋数字孪生互操作性进展（2026-04-10）、DITTO Programme全球DTO治理框架（2026-04-24）、NOAA AOML Argo实时运行更新（2026-04-17）、Argo DMQC GitHub v2.4.2发布（2026-04-24）、CMEMS Python工具包v3.3（2026-04-20）、CROCO-Ocean v2.1.3（2026-04-07）、MITgcm adjoint GPU加速（2026-04-16）等。</div>
      <a href="posts/2026-04-24.html" class="read-more">阅读全文 →</a>
    </div>"""

idx_content = idx_content.replace(old_card, new_card)

# Update header count
idx_content = idx_content.replace(
    '共 29 条精选资讯',
    '共 30 条精选资讯'
)
# Update header count from 29 -> 30
idx_content = idx_content.replace(
    '29 条精选资讯',
    '30 条精选资讯'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("index.html updated")

# === Update archive.html ===
with open('archive.html', 'r', encoding='utf-8') as f:
    arc_content = f.read()

old_arc_entry = """<li><a href="posts/2026-04-24.html"><strong>2026-04-24</strong></a>（周五） · 9个方向 · 31条动态 · 重点：AGU GRL北极快速海冰融化驱动机制研究、Springer ConvLSTM南极海冰60天预报、arXiv ML大气强迫对比NWP研究、Blue-Cloud 2026发布9份可视化培训材料、EDITO Phase 2 EU资助启动等。</li>"""

new_arc_entry = """<li><a href="posts/2026-04-24.html"><strong>2026-04-24</strong></a>（周五） · 9个方向 · 30条动态（已修正） · 重点：AGU GRL北极快速海冰融化驱动机制研究、INESC TEC海洋数字孪生互操作性进展、DITTO Programme全球DTO治理框架、NOAA AOML Argo实时运行更新、Argo DMQC GitHub v2.4.2发布、MITgcm adjoint GPU加速等。</li>"""

if old_arc_entry in arc_content:
    arc_content = arc_content.replace(old_arc_entry, new_arc_entry)
    print("archive.html entry updated")
else:
    print("archive.html: old entry not found, trying partial match")
    # Try partial search
    if '2026-04-24' in arc_content and '31条动态' in arc_content:
        # Find and replace
        start = arc_content.find('2026-04-24')
        end = arc_content.find('</li>', start) + 5
        old = arc_content[start-50:end]
        print(f"Found partial: {old}")
        arc_content = arc_content.replace(old, new_arc_entry)
        print("archive.html updated via partial match")
    else:
        print("WARNING: could not update archive.html")

with open('archive.html', 'w', encoding='utf-8') as f:
    f.write(arc_content)

print("Done!")
