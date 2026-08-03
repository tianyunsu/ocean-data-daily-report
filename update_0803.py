# -*- coding: utf-8 -*-
"""更新 index.html 与 archive.html，插入 2026-08-03 日报"""

DATE_SLUG = '2026-08-03'
DATE_DISPLAY = '2026-08-03 · 周一'
DATE_TITLE = '2026年08月03日 海洋AI研究日报'
EXCERPT = ('本期覆盖全部9个方向，共16条动态。近7天亮点：HybridOM物理-数据混合全球海洋建模'
           '（ICML 2026）；BALLAST贝叶斯主动学习海洋漂流器布放（ICML 2026）；SWIN-DeepONet用Swin '
           'Transformer增强DeepONet学习非线性波动力学（IJCAI-ECAI 2026）；多尺度CNN+DropKey-Transformer'
           '海况估计与不确定性量化（JMSE 07-29）；V-JEPA视频海岸波浪参数估算（arXiv 07-15）；第2届'
           'ECCV 2026海洋视觉研讨会征稿；欧盟DestinE迈入第三阶段AI为核心（07）；Copernicus Marine'
           '路线图预告MyOcean Pro 3D可视化（07-27）；边缘-云协同海洋观测实时QC中国专利（07-07）；'
           'BGC-Argo叶绿素-a首次大规模再处理（07）；ODIS指导小组筹备IODE-29（07-23）；海洋十年公民科学'
           'FAIR数据共享指南；Schmidt加勒比盐指科考航次（08-06起）；我国高时效Argo数据产品智能系统'
           '研制；xarray v2026.07.0与uxarray v2026.07.0发布等。')

# ---- index.html ----
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

new_card = f'''    <div class="post-card">
      <div class="post-date">{DATE_DISPLAY}</div>
      <h2><a href="posts/{DATE_SLUG}.html">{DATE_TITLE}</a></h2>
      <div class="post-excerpt">{EXCERPT}</div>
      <a href="posts/{DATE_SLUG}.html" class="read-more">阅读全文 →</a>
    </div>

'''

marker = '    <div class="post-card">'
pos = index_content.find(marker)
if pos == -1:
    print('ERROR: post-card marker not found in index.html')
    exit(1)
index_content = index_content[:pos] + new_card + index_content[pos:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print('index.html 已更新')

# ---- archive.html ----
with open('archive.html', 'r', encoding='utf-8') as f:
    archive_content = f.read()

new_group = f'''    <div class="archive-group">
      <h2>📅 2026年08月</h2>
      <ul>
        <li><a href="posts/{DATE_SLUG}.html"><strong>{DATE_SLUG}</strong></a>（周一） · 9个方向 · 16条动态 · 重点：HybridOM物理-数据混合全球海洋建模（ICML 2026）；BALLAST贝叶斯主动学习海洋漂流器布放（ICML 2026）；SWIN-DeepONet学习非线性波动力学（IJCAI-ECAI 2026）；多尺度CNN+DropKey-Transformer海况估计（JMSE 07-29）；V-JEPA视频海岸波浪参数估算（arXiv 07-15）；第2届ECCV 2026海洋视觉研讨会；DestinE迈入第三阶段AI为核心（07）；Copernicus Marine路线图预告MyOcean Pro 3D可视化（07-27）；边缘-云协同海洋观测QC专利（07-07）；BGC-Argo CHLA首次大规模再处理（07）；ODIS指导小组筹备IODE-29（07-23）；海洋十年公民科学FAIR数据共享指南；Schmidt加勒比盐指科考航次（08-06起）；我国高时效Argo数据产品智能系统研制；xarray v2026.07.0与uxarray v2026.07.0发布等。</li>
      </ul>
    </div>

'''

marker2 = '    <div class="archive-group">'
pos2 = archive_content.find(marker2)
if pos2 == -1:
    print('ERROR: archive-group marker not found in archive.html')
    exit(1)
archive_content = archive_content[:pos2] + new_group + archive_content[pos2:]
with open('archive.html', 'w', encoding='utf-8') as f:
    f.write(archive_content)
print('archive.html 已更新')
