# -*- coding: utf-8 -*-
"""deploy_0902c.py — 补齐 D1 两条后，同步 index/archive 的条数与摘要"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

IDX_OLD_EXCERPT_START = '本期覆盖9个方向，共16条有效动态。亮点：'
IDX_NEW = ('本期覆盖9个方向，共18条有效动态。亮点：中科院海洋所联合10余家单位在 IEEE GRSM（IF 13.7）'
           '发表北极海冰遥感深度学习综述，梳理五类任务与三阶段演进路径（08-26）；'
           '3D-USE 将水下增强从图像级提升到3D高斯场景级（arXiv 08-28，南开+东南大学）；'
           'RGI-Net 递归门控注入网络用于海洋检测水下图像复原（JMSE 08-31）；'
           '西电团队为"深海勇士"号装上多相机双景拼接"智慧眼"完成1500米海试（09-01）；'
           'HFQI-YOLO 轻量化水下目标检测，参数量与计算量分别降41.7%与31.7%（MST 09-01）；'
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

ARC_OLD = '（周三） · 9个方向 · 16条动态 · 重点：'
ARC_NEW = ('（周三） · 9个方向 · 18条动态 · 重点：')

EXTRA = ('西电"深海勇士"号智慧眼海试（09-01）；HFQI-YOLO轻量化水下目标检测（MST 09-01）；')

# ---------- index.html ----------
p = 'index.html'
s = open(p, encoding='utf-8').read()
s = s.replace('· 9 个研究方向 · 16 条精选资讯', '· 9 个研究方向 · 18 条精选资讯', 1)

i = s.find(IDX_OLD_EXCERPT_START)
assert i >= 0, 'index.html 未找到 09-02 摘要'
j = s.find('</div>', i)
s = s[:i] + IDX_NEW + s[j:]
open(p, 'w', encoding='utf-8').write(s)
print('index.html updated')

# ---------- archive.html ----------
p = 'archive.html'
s = open(p, encoding='utf-8').read()
s = s.replace('· 9 个研究方向 · 16 条精选资讯', '· 9 个研究方向 · 18 条精选资讯', 1)
s = s.replace(ARC_OLD, ARC_NEW, 1)
# 在"嘉庚"前插入两条新条目
anchor = '"嘉庚"号马来西亚开放日（08-27）；'
assert anchor in s, 'archive 未找到插入锚点'
s = s.replace(anchor, EXTRA + anchor, 1)
open(p, 'w', encoding='utf-8').write(s)
print('archive.html updated')

# ---------- 校验 ----------
for p, key in [('index.html', '2026-09-02'), ('archive.html', '2026-09-02')]:
    t = open(p, encoding='utf-8').read()
    k = t.find(key)
    print('---', p, '---')
    print(t[k - 40:k + 700].replace('\n', ' ')[:730])
    print()
