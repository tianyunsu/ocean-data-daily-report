# -*- coding: utf-8 -*-
"""Republish 2026-09-24 (40 条): posts + 替换既有 index 卡片 / archive 条目。"""
import re, shutil, pathlib

shutil.copyfile('daily_reports/海洋AI简报_2026-09-24.html', 'posts/2026-09-24.html')

EXCERPT = ('9 个研究方向 · 40 条精选资讯。滑动 EOF 耦合深度学习预报风浪场、抑制未来信息泄漏（Ocean Engineering 09-22）；'
           '图神经网络改进南极海冰密集度周尺度预报（Sci Rep 09-16）；ECHO 用稀疏新观测按状态自适应修正已发布海冰预报、'
           '96 组设置全面优于固定传播（arXiv 09-21）；分布感知深度学习订正西北太平洋有效波高偏差（JGR:MLC 09-17）；'
           '深度强化学习实现多 AUV 编队控制（EAAI 09-22）；海洋所揭示西太平洋季节内海流累积"海洋记忆"、可提前 8 个月预示厄尔尼诺'
           '（npj Clim Atmos Sci 09-16）；海洋所证实印度洋偶极子经跨洋联动加剧美国东岸高潮位洪涝（Commun Earth Environ 09-23）；'
           '数字孪生渔场耦合水下视觉与多变量水质预报、缺氧预警提前 28.7 分钟（Aquacultural Engineering 09-16）；'
           '全球有效波高融合格网数据集发布（ESSD 09-16）；相干结构数据同化的结构失真研究（NPG 09-21）；'
           'MyOcean Pro v17 新增三维地球视图与多图轴对齐（CMEMS 09-23）；南海内孤立波潜体沉浸式仿真（Ocean Engineering 09-15）；'
           '多波束测深绘制大加那利岛海底地貌图（Journal of Maps 09-22）；挑战者深渊全海深测深不确定性溯源、'
           '航速 4→15 节测深保留率由 87% 降至 78%（Scientific Data 09-16）；Niño3.4 海温异常达 3.05℃ 破纪录（09-22）；'
           'GGM 反演水深异方差不确定性量化（Comput Geosci 09-17）；CYGNSS 星间与通道间一致性检验（RSL 09-20）；'
           'OcDiffSR 条件扩散模型实现亚得里亚海海洋场超分（arXiv 09-18）；考虑海浪状态的风应力新参数化方案提升风暴潮与海浪模拟'
           '（JPO 09-11）；语义子原型网络实现遥感溢油检测（Marine Pollution Bulletin 09-18）；'
           'OceanEye 国际联盟启动、为 GOOS 募集逾 2.11 亿欧元（09-23）；ABLOS"海洋数据共享与海洋法"研讨会（09-16）；'
           '北极海冰厚度无人机 LiDAR 快速反演流程（RSL 09-16）；PlanktonFlow 浮游生物深度学习分类流水线获 PCI 推荐（09-22）；'
           'Det-LIME 海洋哺乳动物检测可解释性工具（MMS 09-20）；Copernicus Marine Toolbox 发布 2.5.0b1（09-15）；'
           'OCEANS 2026 Monterey 会议举行（09-21—24）；第四届海洋内波与混合研讨会在青岛举办（09-18）等。')

CARD = f'''    <div class="post-card">
                <div class="post-header">
                    <a href="posts/2026-09-24.html" class="post-title">海洋AI技术日报 · 2026-09-24（周四）</a>
                    <span class="post-date">2026-09-24</span>
                </div>
                <p class="post-excerpt">{EXCERPT}</p>
                <div class="post-tags">
                    <span class="tag">海洋AI</span>
                    <span class="tag">数字孪生</span>
                    <span class="tag">可视化</span>
                    <span class="tag">数据质量</span>
                    <span class="tag">数据处理</span>
                    <span class="tag">数据共享</span>
                    <span class="tag">开放航次</span>
                    <span class="tag">数据中心</span>
                    <span class="tag">工具资源</span>
                </div>
            </div>
'''

idx = pathlib.Path('index.html')
s = idx.read_text(encoding='utf-8')
# 删除既有 09-24 卡片
pat = re.compile(r'\s*<div class="post-card">(?:(?!</div>\s*</div>).)*?posts/2026-09-24\.html.*?</div>\s*</div>', re.DOTALL)
m = pat.search(s)
if m:
    s = s[:m.start()] + '\n' + s[m.end():]
anchor = '    <div class="post-card">'
pos = s.find(anchor)
assert pos > 0
s = s[:pos] + CARD + s[pos:]
idx.write_text(s, encoding='utf-8')

arch = pathlib.Path('archive.html')
a = arch.read_text(encoding='utf-8')
ali = '<li><a href="posts/2026-09-24.html">'
i0 = a.find(ali)
if i0 >= 0:
    i1 = a.find('</li>', i0) + len('</li>')
    a = a[:i0] + a[i1:]
li = ('<li><a href="posts/2026-09-24.html"><strong>2026-09-24</strong></a>（周四） · 9个方向 · 40条动态 · 重点：'
      '滑动 EOF 耦合深度学习预报风浪场（Ocean Engineering 09-22）；图神经网络改进南极海冰密集度周预报（Sci Rep 09-16）；'
      'ECHO 稀疏观测自适应修正海冰预报、96 组设置全面占优（arXiv 09-21）；分布感知深度学习订正有效波高偏差（JGR:MLC 09-17）；'
      '深度强化学习多 AUV 编队控制（EAAI 09-22）；海洋所揭示"海洋记忆"机制、可提前 8 个月预示厄尔尼诺（npj Clim Atmos Sci 09-16）；'
      '海洋所证实印度洋波动经跨洋联动加剧美国东岸洪涝（Commun Earth Environ 09-23）；数字孪生渔场耦合水下视觉与水质预报、'
      '缺氧预警提前 28.7 分钟（Aquacultural Engineering 09-16）；全球有效波高融合格网数据集（ESSD 09-16）；相干结构数据同化结构失真研究（NPG 09-21）；'
      'MyOcean Pro v17 三维地球视图（CMEMS 09-23）；南海内孤立波潜体沉浸式仿真（Ocean Engineering 09-15）；大加那利岛海底地貌图（Journal of Maps 09-22）；'
      '挑战者深渊全海深测深不确定性溯源（Scientific Data 09-16）；Niño3.4 海温异常 3.05℃ 破纪录（09-22）；GGM 水深异方差不确定性量化（Comput Geosci 09-17）；'
      'OcDiffSR 扩散模型海洋场超分（arXiv 09-18）；考虑海浪状态的风应力新参数化方案（JPO 09-11）；语义子原型遥感溢油检测（Marine Pollution Bulletin 09-18）；'
      'OceanEye 联盟为 GOOS 募集逾 2.11 亿欧元（09-23）；ABLOS 海洋数据共享与海洋法研讨会（09-16）；北极海冰厚度无人机 LiDAR 快速反演（RSL 09-16）；'
      'PlanktonFlow 浮游生物分类流水线（PCI 09-22）；Det-LIME 检测可解释性工具（MMS 09-20）；Copernicus Marine Toolbox 2.5.0b1（09-15）；'
      'OCEANS 2026 Monterey 会议（09-21—24）；第四届海洋内波与混合研讨会（09-18）等。</li>\n      ')
mk = '<ul><li><a href="posts/2026-09-20.html">'
mp = a.find(mk)
assert mp > 0
a = a[:mp + len('<ul>')] + li + a[mp + len('<ul>'):]
arch.write_text(a, encoding='utf-8')
print('republished: posts/2026-09-24.html (40 条) + index.html + archive.html')
