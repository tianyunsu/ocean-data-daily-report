#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build script: Replace SECTIONS in feishu_write_doc.py"""
import re, sys, os

SECTIONS_NEW = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '崂山实验室"问海"全球海洋环境高分辨率AI预报模型（WAIC 2026，2026-07-17）',
                'badge': '[要闻]',
                'abstract': 'WAIC 2026科学前沿论坛上，崂山实验室副主任吴能友披露"问海"全球海洋环境高分辨率智能预报模型。该模型基于实际海洋观测数据自动生成四维全要素预报产品，1.5分钟可完成未来15天全球海洋环境变化预测，误差显著优于国际先进数值预报系统。吴能友同时指出，AI已在海洋领域提出可解释、可检验、可推广的科学假说，但仍缺乏提出颠覆性假设的能力，科学品位尚需人类科学家主导。',
                'source': 'WAIC 2026科学前沿论坛 / 崂山实验室',
                'url': 'https://new.qq.com/rain/a/20260720A0A54W00',
                'date': '2026-07-17'
            },
            {
                'title': 'ECMWF：纯机器学习从观测中实现全球再分析，无需数值模式（arXiv，2026-07-08）',
                'badge': '[论文]',
                'abstract': 'ECMWF团队提出原型系统：仅使用地球系统观测数据训练的机器学习模型即可生成多年代全球再分析，无需依赖物理数值模式。结果显示，ML再分析捕捉了多时间尺度的大气结构和变率，强键动力学诊断指标呈现物理一致性。在与ERA5一致分辨率下，上层风场RMSE与ERA5接近，地表误差标准差介于ERA-Interim与ERA5之间。传统再分析需数年计算，而此ML方法仅需一个工作日。该研究为海洋-大气再分析提供了全新范式。',
                'source': 'arXiv:2607.07879 (ECMWF)',
                'url': 'https://arxiv.org/abs/2607.07879',
                'date': '2026-07-08'
            },
            {
                'title': '文鳐大模型入选福建省AI优质行业垂直模型，已落地20余艘船舶（2026-07-23）',
                'badge': '[要闻]',
                'abstract': '由众数信科、厦门理工学院联合研发的"文鳐"船舶与海洋工程行业垂直大模型入选福建省工信厅《2026年省人工智能优质行业垂直模型》名单。作为我国首个船舶与海洋工程行业大模型，文鳐面向船舶航运、海洋牧场、海上风电、海洋监测、港航服务等全场景提供全链路AI能力。在船舶设备预测性运维场景中，现已落地招商南油、长航集团等头部企业20余艘船，单船年维保成本节约上百万元，并正布局具身智能水上机器人。',
                'source': '台海网 / 厦门理工学院',
                'url': 'https://new.qq.com/rain/a/20260723A042VI00',
                'date': '2026-07-23'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '云锦微发布MaM-GPT实景世界模型，联手浙大落地海洋具身智能"深渊矩阵"（2026-07-23）',
                'badge': '[要闻]',
                'abstract': '宁波云锦微智能科技发布自研MaM-GPT实景进化世界模型，并宣布与浙江大学舟山海洋研究中心达成海洋具身智能深度战略合作。双方通过合资公司"深渊矩阵"承载智慧海洋全赛道商业化，规划"海上高德"与"水下大疆"两大标杆产品。MaM-GPT依托ULP统一隐空间架构，旨在解决视觉语言大模型在理解时间、空间和连续物理规律上的短板，在弱网、高复杂度海洋实体场景中表现出工程落地优势。',
                'source': '中国日报 / 云锦微',
                'url': 'https://cnews.chinadaily.com.cn/a/202607/24/WS6a6309b4a310d709c2fbf840.html',
                'date': '2026-07-23'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期海洋可视化方向暂无重大新进展。港科大WavyOcean 3.0（07-10发布）已在前期日报中详细报道（2026-07-13/07-28）。',
                'source': '',
                'url': '',
                'date': '2026-07-31'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA-QC',
        'items': [
            {
                'title': '改进全球海洋热含量估计：垂直时空联合建模降低15%不确定性（arXiv，2026-07-13）',
                'badge': '[论文]',
                'abstract': '美国科罗拉多大学团队提出基于双变量局部平稳高斯过程和条件模拟的海洋热含量（OHC）改进估计方法。传统方法将不同深度层分开映射再求和，导致不确定性难以量化。该研究联合建模两个压力层的垂直时空依赖关系，利用Argo浮标2004-2022年剖面数据实现全局OHC异常不确定性降低最多15%。该方法对ENSO等气候事件的区域与全球尺度统计显著性分析具有重要价值。',
                'source': 'arXiv:2607.11832 (Univ. of Colorado)',
                'url': 'https://arxiv.org/abs/2607.11832',
                'date': '2026-07-13'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Data Fusion',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期海洋数据处理方向暂无重大新进展。前期已报道的ECMWF ML全球再分析（07-08）本质上融合了数据处理与AI方法，已在方向一中详述。',
                'source': '',
                'url': '',
                'date': '2026-07-31'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期该方向暂无重大新进展。前期已报道的青岛海洋可信数据空间（07-24发布，联邦学习+多方安全计算架构）仍为近两周重要动态，详见2026-07-28期日报。',
                'source': '',
                'url': '',
                'date': '2026-07-31'
            },
        ]
    },
    {
        'title': '七、开放航次与船时共享',
        'en': 'Ocean Expeditions / Ship-Time Sharing',
        'items': [
            {
                'title': '"海斗一号"与"奋斗者"号完成7700米深渊协同科考，多装备联合作业（2026-07-22）',
                'badge': '[航次]',
                'abstract': '��科院沈阳自动化所主持研制的"海斗一号"全海深自主遥控潜水器近日完成西太平洋海试。航次期间，"海斗一号"与"奋斗者"��载人潜水器在7700米深渊海底实现多次会合，完成近距离互拍、地质样品联合采集、采样工具补给交换、协同抓取联合作业标识物等多项任务。单次下潜中实现与载人潜水器和着陆器的多装备、多点位水下协同作业，完整验证"广域搜索-识别查证-抵近作业"一体化工作范式。',
                'source': '中科院沈阳自动化所 / 海洋知圈',
                'url': 'https://www.163.com/dy/article/L2FS2V7R0511KMS0.html',
                'date': '2026-07-22'
            },
            {
                'title': 'NOAA Okeanos Explorer库克群岛ROV深海探测持续进行（2026-07-19起，最新Dive 09 07-29）',
                'badge': '[航次]',
                'abstract': 'NOAA Okeanos Explorer号在库克群岛专属经济区进行为期26天ROV深海探测（7月19日-8月13日）。截至7月29日已完成第9潜——Southern Boundary Abyss深渊平原5500米级探测。此前已完成B2 Seamount等海山和海底高原的生物学与地质学调查。航次期间持续进行Argo浮标部署、CTD水文测量、多波束测深和Argo浮标投放，所有数据将在120天内公开归档。',
                'source': 'NOAA Ocean Exploration',
                'url': 'https://oceanexplorer.noaa.gov/expedition/ex2605',
                'date': '2026-07-29'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Data Archives',
        'items': [
            {
                'title': 'NCEI专题：ENSO探测与监测依赖全球海洋数据体系（2026-07-16）',
                'badge': '[动态]',
                'abstract': 'NOAA NCEI发布专题文章阐述ENSO（厄尔尼诺-南方涛动）的探测与监测对全球海洋观测数据的深度依赖。文章回溯了ENSO预测从1982-83年重大事件后的起步发展，强调NCEI保存的全球海洋温度、盐度、海平面高度等长期数据集是ENSO预报模型的核心基础。同时提及NCEI 2026年6月全球地表温度分析——1.96°F（1.09°C）高于20世纪平均水平，为有记录以来第二热的6月（仅次于2024年）。',
                'source': 'NOAA NCEI',
                'url': 'https://www.ncei.noaa.gov/',
                'date': '2026-07-16'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Ocean Tools & Code Resources',
        'items': [
            {
                'title': 'pyopia v2.16.8 发布：Python海洋粒子图像分析工具箱（2026-07-11）',
                'badge': '[工具]',
                'abstract': 'PyOPIA（Python Ocean Particle Image Analysis）发布v2.16.8版本。该工具箱专为海洋粒子图像分析设计，支持从原始图像到粒子统计的完整处理流程，包括图像处理、粒子分割、统计分析和可视化。利用numpy、scikit-image、xarray等生态工具，适用于浮游生物成像、海洋微塑料等海洋粒子数据的自动化分析。',
                'source': 'PyPI (pyopia)',
                'url': 'https://pypi.org/project/pyopia/',
                'date': '2026-07-11'
            },
            {
                'title': 'PINGMapper v5.5.0 发布：开源侧扫声纳底质栖息地制图工具（2026-07-09）',
                'badge': '[工具]',
                'abstract': 'PINGMapper发布v5.5.0版本，是PING生态系统中的核心声纳处理与制图包。该开源工具可将休闲级侧扫声纳（如Humminbird、Lowrance鱼探仪）记录转换为科学数据集，支持自动化底质分类与栖息地制图。v2.0起集成机器学习底质分割模型（发表于JGR Machine Learning and Computation 2024），配套PINGInstaller、PINGWizard、PINGVerter等生态工具。',
                'source': 'PyPI (pingmapper)',
                'url': 'https://pypi.org/project/pingmapper/',
                'date': '2026-07-09'
            },
        ]
    },
]

# Read the original file
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find SECTIONS = [ and replace
start_marker = 'SECTIONS = ['
start_pos = content.find(start_marker)
if start_pos == -1:
    print("ERROR: Could not find SECTIONS = [")
    sys.exit(1)

# Find matching ]
depth = 0
end_pos = start_pos + len(start_marker)
for i in range(end_pos, len(content)):
    if content[i] == '[':
        depth += 1
    elif content[i] == ']':
        if depth == 0:
            end_pos = i + 1
            break
        depth -= 1
else:
    print("ERROR: Could not find matching ]")
    sys.exit(1)

# Construct new SECTIONS
new_sections_str = 'SECTIONS = ' + repr(SECTIONS_NEW)

# Replace
new_content = content[:start_pos] + new_sections_str + content[end_pos:]

# Verify syntax
try:
    compile(new_content, 'feishu_write_doc.py', 'exec')
    print("Syntax validation PASSED")
except SyntaxError as e:
    print(f"Syntax validation FAILED: {e}")
    sys.exit(1)

# Write
with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"SECTIONS updated successfully. {sum(len(s['items']) for s in SECTIONS_NEW)} items across {len(SECTIONS_NEW)} sections")
