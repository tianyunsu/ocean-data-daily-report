# -*- coding: utf-8 -*-
"""Publish 2026-09-24 daily report (idempotent): copy to posts/, update index.html + archive.html.

If a 2026-09-24 card/li already exists it is REPLACED (safe to re-run).
"""
import shutil, re
from pathlib import Path

SRC = 'daily_reports/海洋AI简报_2026-09-24.html'
DST = 'posts/2026-09-24.html'
shutil.copyfile(SRC, DST)

N = 44
EXCERPT = (f'9 个研究方向 · {N} 条精选资讯。滑动 EOF 耦合深度学习预报风浪场、'
           '抑制未来信息泄漏（Ocean Engineering 09-22）；图神经网络改进南极海冰密集度周尺度预报（Sci Rep 09-16）；'
           'ECHO 用稀疏新观测按状态自适应修正已发布海冰预报，96 组设置全面优于固定传播（arXiv 09-21）；'
           '分布感知深度学习订正西北太平洋有效波高偏差（JGR:MLC 09-17）；深度强化学习实现多 AUV 编队控制（EAAI 09-22）；'
           '海洋所揭示西太平洋季节内海流累积"海洋记忆"、可提前 8 个月预示厄尔尼诺（npj Clim Atmos Sci 09-16）；'
           '海洋所证实印度洋偶极子经跨洋联动加剧美国东岸高潮位洪涝（Commun Earth Environ 09-23）；'
           '数字孪生渔场耦合水下视觉与多变量水质预报、缺氧预警提前 28.7 分钟（Aquacultural Engineering 09-16）；'
           '全球有效波高融合格网数据集发布（ESSD 09-16）；相干结构数据同化的结构失真研究（NPG 09-21）；'
           'MyOcean Pro v17 新增三维地球视图与多图轴对齐（CMEMS 09-23）；南海内孤立波潜体沉浸式仿真（Ocean Engineering 09-15）；'
           'GIS-AHP 东非海岸带热带气旋脆弱性评估（09-21）；多波束测深绘制大加那利岛海底地貌图（Journal of Maps 09-22）；'
           'LeadNet 与 80 米泛北极冬季冰间水道数据集（RSL 09-19）；挑战者深渊全海深测深不确定性溯源、'
           '航速 4→15 节测深保留率由 87% 降至 78%（Scientific Data 09-16）；Niño3.4 海温异常达 3.05℃ 破纪录（09-22）；'
           'GGM 反演水深异方差不确定性量化（Comput Geosci 09-17）；CYGNSS 星间与通道间一致性检验（RSL 09-20）；'
           'OcDiffSR 条件扩散模型实现亚得里亚海海洋场超分（arXiv 09-18）；新兴经济体卫星-模式业务化监测框架（Frontiers 09-22）；'
           '智能手机便携监测海水营养盐与重金属综述（09-17）；考虑海浪状态的风应力新参数化提升风暴潮与海浪模拟（JPO 09-16）；'
           '语义子原型网络遥感影像溢油检测（Marine Pollution Bulletin 09-18）；OceanEye 国际联盟启动、为 GOOS 募集逾 2.11 亿欧元（09-23）；'
           'ABLOS"海洋数据共享与海洋法"研讨会（09-16）；eDNA 成本-灵敏度权衡的过滤与重复策略（09-17）；'
           '公海深海底层渔业生态系统管理标准（09-15）；CF 公约社区研讨会 2026 推进环境数据标准与互操作（09-21）；'
           '原住民知识提升北冰洋模式能力（09-19）；OCEANS 2026 Monterey 会议举行（09-21—24）；'
           '11 对引物巡测中太平洋珊瑚礁全生命之树多样性（09-16）；广海局 AUV 南海超深水完成失联设备搜寻（09-09）；'
           '双稳态金属壳水下滑翔机 0.82 秒完成浮力切换（09-19）；CASPROD 环北极沉积物物源数据库（ESSD 09-10）；'
           'BAMS 全球海洋预报中心十余年业务预报评估（09-15）；水下数据中心对 AI 条约核查的风险（09-19）；'
           'GEBCO_2026 全球水深网格（15 弧秒）持续开放获取（09-18）；Argo 全球数据汇编中心发布最新数据快照（09-08）；'
           'PlanktonFlow 浮游生物深度学习分类流水线获 PCI 推荐（09-22）；Det-LIME 海洋哺乳动物检测可解释性工具（MMS 09-20）；'
           '无人机 LiDAR 快速反演北极海冰厚度（RSL 09-16）；eDNA 宏条形码方法评估与开源流程 MVeM（09-17）；'
           'Copernicus Marine Toolbox 发布 2.5.0b1（09-22）等。')

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

# ---- index.html: replace existing 09-24 card, else insert before first card
idx = Path('index.html')
s = idx.read_text(encoding='utf-8')
existing = re.search(r'    <div class="post-card">\s*<div class="post-header">\s*<a href="posts/2026-09-24\.html".*?</div>\s*</div>', s, re.S)
if existing:
    s = s[:existing.start()] + CARD.rstrip('\n') + s[existing.end():]
    print('index.html: 09-24 card REPLACED')
else:
    anchor = '    <div class="post-card">'
    pos = s.find(anchor)
    assert pos > 0 and '2026-09-20' in s[pos:pos + 900], 'index anchor not found'
    s = s[:pos] + CARD + s[pos:]
    print('index.html: 09-24 card INSERTED')
idx.write_text(s, encoding='utf-8')

# ---- archive.html: replace existing 09-24 li, else insert at top of 2026年09月 group
ARCH = (f'<li><a href="posts/2026-09-24.html"><strong>2026-09-24</strong></a>（周四） · 9个方向 · {N}条动态 · 重点：'
        '滑动 EOF 耦合深度学习预报风浪场（Ocean Engineering 09-22）；图神经网络改进南极海冰密集度周预报（Sci Rep 09-16）；'
        'ECHO 稀疏观测自适应修正海冰预报（arXiv 09-21）；分布感知深度学习订正有效波高偏差（JGR:MLC 09-17）；'
        '深度强化学习多 AUV 编队控制（EAAI 09-22）；海洋所揭示"海洋记忆"机制、可提前 8 个月预示厄尔尼诺（npj Clim Atmos Sci 09-16）；'
        '海洋所证实印度洋波动经跨洋联动加剧美国东岸洪涝（Commun Earth Environ 09-23）；数字孪生渔场缺氧预警提前 28.7 分钟（Aquacultural Engineering 09-16）；'
        '全球有效波高融合格网数据集（ESSD 09-16）；相干结构数据同化结构失真研究（NPG 09-21）；MyOcean Pro v17 三维地球视图（CMEMS 09-23）；'
        'GIS-AHP 东非海岸带气旋脆弱性评估（09-21）；大加那利岛海底地貌图（Journal of Maps 09-22）；LeadNet 泛北极冬季冰间水道数据集（RSL 09-19）；'
        '挑战者深渊全海深测深不确定性溯源（Scientific Data 09-16）；Niño3.4 海温异常 3.05℃ 破纪录（09-22）；GGM 水深异方差不确定性量化（Comput Geosci 09-17）；'
        'CYGNSS 一致性检验（RSL 09-20）；OcDiffSR 扩散模型海洋场超分（arXiv 09-18）；智能手机便携监测营养盐与重金属综述（09-17）；'
        '海浪状态风应力新参数化（JPO 09-16）；语义子原型网络溢油检测（Marine Pollution Bulletin 09-18）；OceanEye 联盟为 GOOS 募集逾 2.11 亿欧元（09-23）；'
        'ABLOS 海洋数据共享与海洋法研讨会（09-16）；CF 公约社区研讨会 2026（09-21）；OCEANS 2026 Monterey 会议（09-21—24）；'
        '广海局 AUV 南海超深水搜寻失联设备（09-09）；双稳态金属壳水下滑翔机（09-19）；CASPROD 环北极沉积物物源数据库（ESSD 09-10）；'
        'BAMS 全球海洋预报业务评估（09-15）；GEBCO_2026 全球水深网格开放获取（09-18）；Argo 全球数据快照（09-08）；'
        'PlanktonFlow 浮游生物分类流水线（PCI 09-22）；Det-LIME 检测可解释性工具（MMS 09-20）；Copernicus Marine Toolbox 2.5.0b1（09-22）等。</li>\n      ')

arch = Path('archive.html')
a = arch.read_text(encoding='utf-8')
ex_li = re.search(r'<li><a href="posts/2026-09-24\.html">.*?</li>\s*', a, re.S)
if ex_li:
    a = a[:ex_li.start()] + ARCH + a[ex_li.end():]
    print('archive.html: 09-24 li REPLACED')
else:
    marker = '<ul><li><a href="posts/2026-09-20.html">'
    mp = a.find(marker)
    assert mp > 0, 'archive anchor not found'
    a = a[:mp] + '<ul>' + ARCH + a[mp + len('<ul>'):]
    print('archive.html: 09-24 li INSERTED')
arch.write_text(a, encoding='utf-8')

print('published:', DST)
print('index.html + archive.html updated')
