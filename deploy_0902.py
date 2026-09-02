# -*- coding: utf-8 -*-
"""deploy_0902.py — 发布 2026-09-02 日报到 GitHub Pages（复制 + 更新 index/archive）"""
import shutil, sys, re

sys.stdout.reconfigure(encoding='utf-8')

SRC = 'daily_reports/海洋AI简报_2026-09-02.html'
DST = 'posts/2026-09-02.html'

shutil.copyfile(SRC, DST)
print('copied ->', DST)

EXCERPT = ('本期覆盖9个方向，共16条有效动态。亮点：中科院海洋所联合10余家单位在 IEEE GRSM（IF 13.7）'
           '发表北极海冰遥感深度学习综述，梳理五类任务与三阶段演进路径（08-26）；3D-USE 将水下增强从图像级'
           '提升到3D高斯场景级（arXiv 08-28，南开+东南大学）；RGI-Net 递归门控注入网络用于海洋检测水下图像复原'
           '（JMSE 08-31）；西电团队为"深海勇士"号装上多相机双景拼接"智慧眼"完成1500米海试（09-01）；'
           '南科大海洋高等研究院共建海洋超算与数字孪生校企联合实验室（08-28）；'
           'Transformer U-Net 从 SWOT 海洋重力产品反演短波长海底地形（JGR 08-27）；'
           'MambaIR-MSP 红外引导被动微波海表温度超分辨率（JGR 08-28）；'
           'CIM-TTDA 测试时域适应的 SAR 海岸水淹智能提取（JGR: MLC 08-19）；'
           '辽宁海洋数据治理7项规范+省级海洋与极地科学数据中心+可信数据空间试点（08-26）；'
           'OBIS 执委会第8次会议通报半年新增3200万条记录（09-01）；'
           '中国第16次北冰洋科考"雪龙"号12个冰站作业完成（08-07/08-09）；'
           '"嘉庚"号马来西亚开放日搭载四国33名师生联合观测（08-27）；'
           'EMSO EVOLVE 启动升级欧洲深海观测基础设施（09-01）；Argo Australia 20周年累计28.5万条剖面（08-26）；'
           'bluertopo v0.0.2 与 CopernicusMarine v0.4.9 发布（CRAN 08-27/08-28）。')

CARD = (
    '    <div class="post-card">\n'
    '      <div class="post-date">2026-09-02 · 周三</div>\n'
    '      <h2><a href="posts/2026-09-02.html">2026年09月02日 海洋AI研究日报</a></h2>\n'
    '      <div class="post-excerpt">' + EXCERPT + '</div>\n'
    '      <a href="posts/2026-09-02.html" class="read-more">阅读全文 →</a>\n'
    '    </div>\n\n'
)

# ---------- index.html ----------
p = 'index.html'
s = open(p, encoding='utf-8').read()

s = s.replace('· 9 个研究方向 · 10 条精选资讯', '· 9 个研究方向 · 16 条精选资讯', 1)

anchor = '    <div class="post-card">\n      <div class="post-date">2026-08-31'
assert anchor in s, 'index.html 未找到 08-31 卡片锚点'
s = s.replace(anchor, CARD + anchor, 1)
open(p, 'w', encoding='utf-8').write(s)
print('index.html updated')

# ---------- archive.html ----------
p = 'archive.html'
s = open(p, encoding='utf-8').read()
print('--- archive head ---')
print('\n'.join(s.split('\n')[:22]))

open(p, 'w', encoding='utf-8').write(s)
