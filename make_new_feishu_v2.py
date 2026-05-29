#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
替换 feishu_write_doc.py 中的 SECTIONS 数据（修正后版本）
使用 bracket-counting 方法精准定位
"""

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': 'OCEANS 2026国际海洋技术大会三亚开幕：海洋AI成为核心专题方向（中国日报 / IEEE OES, 2026-05-26）',
                'badge': '近7天',
                'abstract': '5月26日，全球海洋工程与科技领域旗舰会议OCEANS 2026在海南三亚启幕。大会以"走向深蓝"为主题，汇聚全球26个国家和地区近750名专家学者、行业精英。海洋人工智能（AI）被列为核心专题之一，来自美国、丹麦、中国等国的专家围绕物理驱动机器学习、AI驱动的海洋感知与预报等议题发表主旨报告。大会设深海探测、海洋AI、水下传感器网络、海上风电、极地观测等6大专题方向，51家海内外参展商集中展示。海南大学作为继上海交通大学之后第二所获得该会议主办权的中国大陆学术机构。',
                'source': '中国日报 / IEEE OES',
                'url': 'https://news.qq.com/rain/a/20260527A03QJY00',
                'date': '2026-05-26',
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': []
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization',
        'items': [
            {
                'title': 'Copernicus Marine海洋空间规划数据可视化平台v1.0-beta发布：交互式3D卫星数据可视化（GitHub, 2026-05-24）',
                'badge': '近7天',
                'abstract': '面向海洋空间规划的开源数据可视化平台v1.0-beta在GitHub发布（Copernicus Marine DataViz Challenge参赛项目）。该平台旨在降低海洋数据使用门槛，将复杂的卫星观测数据转化为直观的三维可视化，并集成对话式AI辅助分析功能。面向研究人员、学生和海洋管理者，支持Copernicus Marine等海洋数据源的可视化分析，推动海洋数据民主化与开放科学实践。',
                'source': 'GitHub / Copernicus Marine DataViz Challenge',
                'url': 'https://github.com/ROYCEFTC/Marine-Spatial-Planning-Application---DataViz-Challenge2026/releases',
                'date': '2026-05-24',
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': []
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': 'OceanSR-Prob：基于扩散模型的全球海洋风速空间降尺度方法（Neurocomputing, 2026-05-22）',
                'badge': '近7天',
                'abstract': '发表于Neurocomputing期刊，提出OceanSR-Prob生成式扩散框架，用于全球海洋风速剖面的空间降尺度。该方法通过概率建模捕捉海洋风速的多尺度空间变异性，克服传统降尺度方法过度平滑和高分辨率细节丢失的局限。在多个分辨率下（从0.25度降至更精细区域尺度）验证，优于现有插值和统计降尺度基线方法，为高分辨率海气耦合模型和海上风电评估等应用提供可靠的数据预处理工具。',
                'source': 'Neurocomputing (Elsevier)',
                'url': 'https://www.sciencedirect.com/science/article/pii/S0925231226014669',
                'date': '2026-05-22',
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'title': 'PACE Data Hackweek开放科学实践报告：两次Hackweek的经验与启示（Oceanography, 2026-05-19）',
                'badge': '1周~1个月',
                'abstract': '发表于Oceanography期刊的开放科学论文，系统总结了两届NASA PACE（浮游植物、气溶胶、云和海洋生态系统）Data Hackweek的目标、成果和参与者经验。两届Hackweek共为数百名研究人员提供了PACE卫星高光谱海洋颜色数据的实操培训，推动了开放科学协作模式在海洋遥感数据处理中的应用，并探讨了数据访问、培训基础设施和社区建设等持续挑战，为类似海洋数据培训项目提供了参考框架。',
                'source': 'Oceanography (The Oceanography Society)',
                'url': 'https://tos.org/oceanography/article/the-pace-data-hackweek-launches-a-new-wave-of-open-science-how-we-did-it-twice-and-why',
                'date': '2026-05-19',
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': []
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': 'CMEMS推出"理解我们的海洋II：收集海洋数据"科普系列（Copernicus Marine, 2026-05-26）',
                'badge': '近7天',
                'abstract': 'Copernicus Marine Service（CMEMS）发布"Understanding Our Ocean"科普系列第二篇《收集海洋数据》，系统介绍海洋数据的多种采集方式，包括卫星遥感（海面温度、海面高度、海洋颜色）、原位观测（Argo浮标、漂流浮标、锚系阵列、科考船CTD）、滑翔机和水下滑翔器等平台。文章帮助数据用户理解CMEMS数据来源和质量控制流程，是CMEMS提升全球海洋数据素养与用户服务能力的系列举措之一。',
                'source': 'Copernicus Marine Service (CMEMS)',
                'url': 'https://marine.copernicus.eu/news/understanding-our-ocean-ii-collecting-ocean-data',
                'date': '2026-05-26',
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': []
    },
]

import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# find SECTIONS
idx = content.find('SECTIONS = [')
start = idx + len('SECTIONS = ')
depth = 0
end = start
for i, ch in enumerate(content[start:], start):
    if ch == '[':
        depth += 1
    elif ch == ']':
        depth -= 1
        if depth == 0:
            end = i + 1
            break

old_sections_str = content[start:end]
new_sections_str = repr(NEW_SECTIONS)

new_content = content[:start] + new_sections_str + content[end:]

# Validate
try:
    compile(new_content, 'feishu_write_doc.py', 'exec')
    print('Syntax validation: OK')
except SyntaxError as e:
    print(f'Syntax error: {e}')
    exit(1)

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('feishu_write_doc.py updated successfully!')
print(f'Old SECTIONS size: {len(old_sections_str)} chars')
print(f'New SECTIONS size: {len(new_sections_str)} chars')

# Verify section counts
import ast as ast2
sections = ast2.literal_eval(new_sections_str)
total = 0
for s in sections:
    n = len(s['items'])
    total += n
    print(f"  {s['title']}: {n} 条")
print(f"Total: {total} 条")
