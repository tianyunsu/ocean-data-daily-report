# -*- coding: utf-8 -*-
import io

p = 'archive.html'
s = io.open(p, encoding='utf-8').read()

new_li = (
    '      <ul><li><a href="posts/2026-09-04.html"><strong>2026-09-04</strong></a>'
    '（周五） · 9个方向 · 17条动态 · 重点：'
    '合成孔径声呐ATR的CNN/Transformer大规模对比（arXiv 09-01）；'
    'ICE-3D时空多尺度感知学习逐日估计北极海冰厚度（Remote Sensing 09-03）；'
    'SHIP-AID浅水沉船隐患GeoAI检测框架（Remote Sensing 08-26）；'
    '残差-状态空间混合架构北极海冰分割网络（《中国航海》08-31）；'
    '厦门“文鳐”船舶与海洋工程大模型入选省级优质垂直模型、“海嘉”数字中枢平台全球首发（09-04）；'
    'Fugro在新加坡建设AI驱动海洋数字孪生（09-03）；'
    '自然资源部北海预报减灾中心近岸淹没精细化数字孪生外协采购（09-02）；'
    'NEODAAS上线航次卫星海洋观测可视化门户（08-26）；'
    'IMOS Live升级新增AusTemp与75+岸基波浪浮标（08-27）；'
    'PML完成迄今最大规模多传感器融合海洋水色叶绿素产品精度评估（08-26）；'
    '注意力增强3D-U-Net++西太平洋三维温盐场智能重构并发布1993-2023数据集（ESSD，中科院海洋所09-04）；'
    'BBNJ协定信息交换机制数据治理基础研究（Front. Mar. Sci. 08-31）；'
    'EMODnet数据吸纳服务进入新阶段（08-31）；'
    '海南省2026年下半年共享航次启航、“深海科创积分”闭环跑通（09-04）；'
    '上海海洋大学中西印度洋公海渔业资源调查船租赁落标、9月起实施100个站点（08-31）；'
    '第十一次国家科学数据中心主任联席会召开（09-03）；'
    'OpenDrift v1.14.12发布（PyPI 08-31）。'
    '</li>\n'
    '<li><a href="posts/2026-09-03.html"><strong>2026-09-03</strong></a>'
)

old = ('      <ul><li><a href="posts/2026-09-03.html"><strong>2026-09-03</strong></a>')
assert old in s, 'anchor not found'
s = s.replace(old, new_li, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('archive.html updated')
