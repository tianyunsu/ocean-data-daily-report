# -*- coding: utf-8 -*-
"""deploy_0902b.py — 更新 archive.html：新建 2026年09月 分组并插入 09-02 条目"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'archive.html'
s = open(p, encoding='utf-8').read()

# 1) 头部描述同步
s = s.replace('· 9 个研究方向 · 21 条精选资讯', '· 9 个研究方向 · 16 条精选资讯', 1)

# 2) 构造 2026年09月 分组
SUMMARY = ('北极海冰遥感深度学习综述（IEEE GRSM, 08-26）；3D-USE场景级水下增强（arXiv 08-28）；'
           'RGI-Net水下图像复原（JMSE 08-31）；西电"深海勇士"号智慧眼海试（09-01）；'
           '南科大海洋超算与数字孪生联合实验室（08-28）；SWOT重力Transformer U-Net海底地形反演（JGR 08-27）；'
           'MambaIR-MSP微波SST超分（JGR 08-28）；CIM-TTDA SAR海岸水淹智能提取（JGR: MLC 08-19）；'
           '辽宁海洋数据治理7项规范（08-26）；OBIS执委会第8次会议（09-01）；'
           '中国第16次北冰洋科考冰站作业（08-07/08-09）；"嘉庚"号马来西亚开放日（08-27）；'
           'EMSO EVOLVE启动（09-01）；Argo Australia 20周年（08-26）；'
           'bluertopo v0.0.2与CopernicusMarine v0.4.9（CRAN 08-27/08-28）等。')

GROUP = (
    '    <div class="archive-group">\n'
    '      <h2>\U0001f4c5 2026年09月</h2>\n'
    '      <ul>\n'
    '        <li><a href="posts/2026-09-02.html"><strong>2026-09-02</strong></a>'
    '（周三） · 9个方向 · 16条动态 · 重点：' + SUMMARY + '</li>\n'
    '      </ul>\n'
    '    </div>\n\n'
)

anchor = '    <div class="archive-group">\n      <h2>\U0001f4c5 2026年08月</h2>'
assert anchor in s, 'archive.html 未找到 2026年08月 分组锚点'
s = s.replace(anchor, GROUP + anchor, 1)

open(p, 'w', encoding='utf-8').write(s)
print('archive.html updated')

# 校验
chk = open(p, encoding='utf-8').read()
i = chk.find('2026年09月')
print(chk[i - 60:i + 700])
