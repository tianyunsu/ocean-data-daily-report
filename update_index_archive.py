#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 index.html 和 archive.html 添加 2026-05-18 日报
"""

DATE_SLUG = '2026-05-18'
DATE_DISPLAY = '2026-05-18 · 周一'
DATE_TITLE = '2026年05月18日 海洋AI技术日报'
EXCERPT = '本期涵盖9个方向，共22条动态。近7天亮点：Njord——首个概率性图神经网络海洋集成预报模型（arXiv 05-14，突破确定性预报局限，OceanBench全球基准上层变量误差最低）；南加州海带森林连续海洋热浪群落变化（Comm E&E 05-16）；美国东北陆架浮游植物温度敏感性主导NPP季节变化（Comm E&E 05-16）；AMOC减弱驱动热带辐合带向南迁移（Nature Comm 05-16）；地面沉降使人口密集海岸海平面上升速率翻倍（Nature Comm 05-16）；Eos观点：失去美国海平面科学的全球影响（05-15）；Copernicus Marine Toolbox v2.4.1发布修复climatology子集Bug（05-11）；Okeanos Explorer EX2603 ROV系统测试航次正式启动（05-16）；NOAA NCEI史上最大规模云迁移FAQ发布（05-12）等。'

# 更新 index.html
with open('C:/Users/Administrator/WorkBuddy/Claw/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 替换第一条的日期和内容
old_first = '''    <div class="post-card">
      <div class="post-date">2026-05-15 · 周五</div>
      <h2><a href="posts/2026-05-15.html">2026年05月15日 海洋AI技术日报</a></h2>
      <div class="post-excerpt">本期涵盖9个方向，共21条动态。近7天亮点：AxiomOcean全球AI海洋预报模型——保留上层海洋三维垂直结构（arXiv 05-11）、CMEMS AI驱动下一代业务化海洋产品（05-04）、南海SST多因子ML预测研究（Frontiers 05-13）、王军成院士AI海洋观测走向智能化（05-13）、复旦大学GEOXYGEN全球长期溶解氧数据集ESSD发表（05-12）、BGC-Argo+二次QC预印本（05-12）、Argo叶绿素6月全面再处理预告（Euro-Argo）、中科院深海所奋斗者号156天太平洋穿越航次完成（05-12）、MCC 2026海洋计算挑战赛启动（05-14）、NCEI史上最大规模云迁移至AWS（05-12）、Nature Communications热带气旋次表层信使（05-07）、低云反馈不可逆海平面上升（05-11）、GDAL 3.13.0 Iowa City发布（05-08）等。</div>
      <a href="posts/2026-05-15.html" class="read-more">阅读全文 →</a>
    </div>'''

new_first = f'''    <div class="post-card">
      <div class="post-date">{DATE_DISPLAY}</div>
      <h2><a href="posts/{DATE_SLUG}.html">{DATE_TITLE}</a></h2>
      <div class="post-excerpt">{EXCERPT}</div>
      <a href="posts/{DATE_SLUG}.html" class="read-more">阅读全文 →</a>
    </div>

        <div class="post-card">
      <div class="post-date">2026-05-15 · 周五</div>
      <h2><a href="posts/2026-05-15.html">2026年05月15日 海洋AI技术日报</a></h2>
      <div class="post-excerpt">本期涵盖9个方向，共21条动态。近7天亮点：AxiomOcean全球AI海洋预报模型——保留上层海洋三维垂直结构（arXiv 05-11）、CMEMS AI驱动下一代业务化海洋产品（05-04）、南海SST多因子ML预测研究（Frontiers 05-13）、王军成院士AI海洋观测走向智能化（05-13）、复旦大学GEOXYGEN全球长期溶解氧数据集ESSD发表（05-12）、BGC-Argo+二次QC预印本（05-12）、Argo叶绿素6月全面再处理预告（Euro-Argo）、中科院深海所奋斗者号156天太平洋穿越航次完成（05-12）、MCC 2026海洋计算挑战赛启动（05-14）、NCEI史上最大规模云迁移至AWS（05-12）、Nature Communications热带气旋次表层信使（05-07）、低云反馈不可逆海平面上升（05-11）、GDAL 3.13.0 Iowa City发布（05-08）等。</div>
      <a href="posts/2026-05-15.html" class="read-more">阅读全文 →</a>
    </div>'''

index_content = index_content.replace(old_first, new_first, 1)

with open('C:/Users/Administrator/WorkBuddy/Claw/index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print('index.html 已更新')

# 更新 archive.html
with open('C:/Users/Administrator/WorkBuddy/Claw/archive.html', 'r', encoding='utf-8') as f:
    archive_content = f.read()

old_archive_first = '''<li><a href="posts/2026-05-15.html"><strong>2026-05-15</strong></a>（周五） · 9个方向 · 21条动态 · 重点：AxiomOcean保留上层海洋三维垂直结构（arXiv 05-11）、CMEMS AI下一代业务化海洋产品（05-04）、南海SST多因子ML预测（Frontiers 05-13）、王军成院士AI海洋观测智能化（05-13）、GEOXYGEN全球长期溶解氧数据集ESSD发表（05-12）、BGC-Argo+二次QC预印本（05-12）、Argo叶绿素6月再处理预告（Euro-Argo）、奋斗者号156天太平洋穿越完成（05-12）、MCC 2026海洋计算挑战赛启动（05-14）、NCEI史上最大规模云迁移至AWS（05-12）、热带气旋次表层信使NC（05-07）、低云反馈不可逆海平面上升NC（05-11）、GDAL 3.13.0 Iowa City（05-08）等。</li>'''

new_archive_first = f'''<li><a href="posts/{DATE_SLUG}.html"><strong>{DATE_SLUG}</strong></a>（周一） · 9个方向 · 22条动态 · 重点：Njord概率GNN海洋集成预报arXiv（05-14）；南加州海带森林热浪群落变化Comm E&E（05-16）；浮游植物温度敏感性主导NPP季节变化Comm E&E（05-16）；AMOC减弱驱动ITCZ南移Nature Comm（05-16）；地面沉降使海岸海平面上升翻倍Nature Comm（05-16）；Eos失去美国海平面科学全球影响观点（05-15）；CMT v2.4.1修复climatology Bug（05-11）；Okeanos EX2603 ROV系统测试启动（05-16）；NCEI史上最大云迁移FAQ（05-12）；BGC-Argo+二次QC预印本（05-12）；GEOXYGEN全球溶解氧ESSD（05-12）等。</li>
{old_archive_first}'''

archive_content = archive_content.replace(old_archive_first, new_archive_first, 1)

with open('C:/Users/Administrator/WorkBuddy/Claw/archive.html', 'w', encoding='utf-8') as f:
    f.write(archive_content)
print('archive.html 已更新')
