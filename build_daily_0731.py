#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build today's SECTIONS data and HTML for 2026-07-31"""
import json, sys, os, re
from datetime import datetime

TODAY = '2026-07-31'
TODAY_CN = '2026年07月31日'

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'badge': '[论文]',
                'title': 'Energy Constrained Hierarchical Underwater Monitoring via Local Multi-Agent RAG——低功耗多智能体RAG水下分层监测架构（arXiv 2026-07-27）',
                'abstract': '海洋生物监测长期受限于严格的能源约束和水下通信困难。本文提出分层主-卫星设计架构：超低功耗MAX78000/MAX78002微控制器持续感知视听信号，NVIDIA Jetson Orin NX仅在计划处理或事件驱动时激活。激活后执行全本地多模态流水线——数据摄入、视觉目标提取、基于BioCLIP/OpenCLIP嵌入的ChromaDB索引、物种识别、RAG推理与自动报告生成。LangChain多智能体框架协调查询路由、结构分析、能源管理和报告生成。该架构桥接超低功耗连续感知与本地多模态智能，将原始多模态数据压缩后通过声学/光学/卫星灵活传输，大幅降低能耗和通信开销。',
                'source': 'arXiv:2607.24313',
                'url': 'https://arxiv.org/abs/2607.24313',
                'date': '2026-07-27'
            },
            {
                'badge': '[论文]',
                'title': 'CLUIE：聚类感知的RWKV递归传播与暗响应局部补偿——水下图像增强新SOTA（arXiv 2026-07-23）',
                'abstract': '水下图像增强因波长依赖性光吸收、散射和后向散射导致颜色失真与细节损失。本文提出聚类感知RWKV框架CRWKV，将传统固定扫描路径重构为内容自适应的token轨迹：聚类感知语义动态重排序（CSDR）按语义特征相似性分组token并从簇间上下文导出动态遍历顺序；暗响应调制局部传播（DMLP）通过深度卷积提取局部结构响应并使用邻域感知伪暗响应图自适应调制传播强度。创新点在于让WKV状态沿语义相关区域而非固定空间顺序累积。在多个水下图像增强基准上达到SOTA定量性能与视觉质量。',
                'source': 'arXiv:2607.21467',
                'url': 'https://arxiv.org/abs/2607.21467',
                'date': '2026-07-23'
            },
            {
                'badge': '[动态]',
                'title': 'NOAA与Brightband签署CRADA合作——将海量观测数据AI就绪化用于天气预报（2026-07-28）',
                'abstract': 'NOAA与Brightband公司签署为期两年的合作研发协议（CRADA），目标是优化NOAA管理的大规模观测天气数据档案，使其适用于训练基于人工智能的天气预报应用。该合作将推动将NOAA数十年的气象与海洋观测数据转换为机器学习就绪格式，支持新一代AI天气预报模型的开发和验证，是NOAA推动AI赋能业务化预报的重要举措。',
                'source': 'NOAA Climate.gov',
                'url': 'https://www.climate.gov/news-features/feed/noaa-partners-brightband-make-observational-data-ai-ready-0',
                'date': '2026-07-28'
            }
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'badge': '[动态]',
                'title': '海南省海洋厅宣布2026年为"孪生海洋"年——"孪生三湾"平台联动荷兰Oceanz 3D数字制造（2026-07-28）',
                'abstract': '海南省海洋厅厅长李东屿率团访荷，正式宣布2026年为海南"孪生海洋"年。基于龙栖湾-崖州湾-三亚湾21座海基站点实时动态数据构建的"孪生三湾"平台将作为海洋综合调查观监测技能大赛初赛平台，并与荷兰Oceanz公司YourOceanz线上一体化3D数字制造服务平台对接，联动AM-Flow智能自动化后处理质控产线和DNV船级社国际认证体系，构建"数字建模—智能智造—自动化质检—国际合规认证"一体化技术闭环。此举标志着海南从"物联海洋"向"孪生海洋"的战略升级。',
                'source': '南海网/海南省海洋厅',
                'url': 'https://www.hinews.cn/page?n=2837230&m=1&s=1044',
                'date': '2026-07-28'
            },
            {
                'badge': '[论文]',
                'title': '海水颜色预测助力海洋数字孪生构建——融合可微物理模型与Secchi盘观测（J-STAGE 2026-07-27）',
                'abstract': '日本研究者开展海水颜色与水质的定量关系研究，通过融合可微物理模型与Secchi盘观测结果，初步证实海水颜色可从水质变量中预测。研究发现即使在同一海域，不同波长光的衰减特性也存在差异，这一发现对藻类、海草和海藻等依赖不同光频段生长的光合生物具有重要意义。该研究旨在为构建忠实于科学证据的海洋数字孪生提供方法论基础，同时为更精确的海洋生物生长环境观测与评估提出新方案。',
                'source': 'J-STAGE / JSCE AI & Data Science',
                'url': 'https://doi.org/10.11532/jsceiii.7.2_98',
                'date': '2026-07-27'
            }
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization',
        'items': [
            {
                'badge': '[要闻]',
                'title': '我国首次发布东部海域"海底化学元素图"——填补海洋地球化学系统性编图空白（人民日报 2026-07-31）',
                'abstract': '中国地质调查局青岛海洋地质研究所完成我国首套《中国东部海域沉积物地球化学图集》，首次系统性地编制了连接亚欧大陆与太平洋关键海域的海底化学元素分布图。该图集填补了我国东部海域沉积物地球化学系统性编图的空白，有力提升了我国在全球边缘海相关研究领域的学术话语权。此前国内陆域地球化学填图已取得丰硕成果，但海洋地球化学调查存在海域覆盖不均衡、数据规范不统一、系统性集成不足等问题。图集覆盖约20%此前缺乏实地沉积物样品的海域，通过数值模拟填补数据空白。',
                'source': '人民日报',
                'url': 'https://paper.people.com.cn/rmrb/pc/content/202607/31/content_30172379.html',
                'date': '2026-07-31'
            }
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'badge': '[论文]',
                'title': 'VAE无监督检测BGC-Argo浮标生物附着漂移——首个大规模ML基准（EarthArXiv 2026-07-11）',
                'abstract': '自主海洋观测平台上的光学传感器因生物附着导致渐进式偏差，污染气候记录。本文提出基于变分自编码器（VAE）的无监督异常检测方法，在86个地中海BGC-Argo浮标数据上训练并评估。VAE仅在早期部署清洁剖面上训练，然后在每个浮标的完整时间轨迹上评估——重建误差随部署时间增加而上升（40%浮标显著），平均晚期/早期误差比1.70。这是首个面向自主海洋传感器生物附着检测的大规模ML基准，证明无监督形状基VAE可跨异构浮标舰队检测漂移，为BGC-Argo数据质量自动化提供新路径。',
                'source': 'EarthArXiv',
                'url': 'https://doi.org/10.31223/X5W506',
                'date': '2026-07-11'
            },
            {
                'badge': '[论文]',
                'title': '时空图神经网络实现水下滑翔机遥测自主异常检测——F1达0.986（IEEE JOE 2026）',
                'abstract': '水下滑翔机对持续海洋监测至关重要，但有限卫星通信和依赖熟练操作员限制了舰队扩展。本文提出适配水下滑翔机遥测的时空图神经网络（STGNN），将每个传感器建模为图节点并耦合固定传感器间结构与时间动态以检测异常窗口。实验在Slocum G2部署数据上注入合成故障，STGNN在评估套件中表现最强——F1分数达0.986，并包含显式延迟和假报警报告。代码和评估协议已公开，为滑翔机舰队的自动化质量控制和规模扩展提供可操作的异常检测方案。',
                'source': 'IEEE Journal of Oceanic Engineering',
                'url': 'https://doi.org/10.1109/JOE.2026.3702319',
                'date': '2026-07-01'
            }
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'badge': '[论文]',
                'title': 'MSFA多策略融合架构清洗海洋环境时间序列数据——AUPRC提升12-25%，NRMSE降低40%+（MDPI BDCC 2026-07-17）',
                'abstract': '海洋浮标和近岸传感器采集的监测数据常受缺失值、突变尖峰和短期波动影响。本文提出多策略融合架构MSFA：将时间索引和测量值归一化到公共特征空间后进行DBSCAN局部密度异常检测，IQR筛选识别全局极值，异常标记后结合线性插值和仅基于相邻有效观测的移动平均进行修复。修复后使用组合残差度量（CRM）与中位数/MAD阈值二次核查。在东营近海浮标数据集和自采近岸数据集上，AUROC/AUPRC/NRMSE分别达0.896/0.855/0.066和0.986/0.915/0.0653，NRMSE降低超40%，同时保持清洗过程可解释。',
                'source': 'MDPI Big Data and Cognitive Computing',
                'url': 'https://doi.org/10.3390/bdcc10070242',
                'date': '2026-07-17'
            }
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'badge': '[动态]',
                'title': 'IOOS 2026年7月双周通讯亮点：Darwin Core数据包指南获批、NOAA AI政策发布、切萨皮克湾环境预报系统建成（2026-07-28）',
                'abstract': 'IOOS 7月通讯报道多项进展：(1) 生物多样性信息标准（TDWG）执行委员会批准Darwin Core数据包概念模型与指南——使复杂生物多样性数据的结构化发布成为可能，突破现有Darwin Core Archive星型模式限制；(2) NOAA发布人工智能政策（NAO 216-128），要求所有AI应用必须牢固根植于科学诚信、问责制、透明度和风险管理；(3) VIMS完成5年切萨皮克湾环境��报系统建设——预报从2天扩展到5天并加入HAB概率机器学习预报及40年物理-生物地球化学数字图集；(4) IOOS建模实践社区研讨会于7月28-30日在华盛顿举行。',
                'source': 'IOOS / NOAA',
                'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-july-2026/',
                'date': '2026-07-28'
            }
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'badge': '[要闻]',
                'title': '"东方红2"海洋科考船焕新再出发——可同步开展多学科一体化海洋综合探测，稳定再服役30年（科技日报 2026-07-29）',
                'abstract': '由中船集团武昌造船为中国海洋大学倾力改造的"东方红2"海洋综合科学考察实习船完成全部改造施工任务并正式交付。该船能同步开展水文、气象、地质、生物、地球物理等多学科一体化海洋综合探测，实现"一站式全域科考"。船舶整体性能与结构状态大幅优化，可稳定再服役30年。"东方红2"的改造交付将大幅提升我国海洋科学考察能力，为深远海多学科综合研究提供关键平台支撑。',
                'source': '科技日��',
                'url': 'https://www.163.com/dy/article/L32UL7T80556L592.html',
                'date': '2026-07-29'
            },
            {
                'badge': '[航次]',
                'title': '中科院烟台海岸带研究所完成2026年渤海海水样品采集航次——"创新一"科考船执行（2026-07-30）',
                'abstract': '中国科学院烟台海岸带研究所"创新一"号科考船于7月17日至30日在渤海海域完成2026年度海水样品采集活动。作业覆盖24个站位中心（半径200米水域），系统采集海水样品用于海岸带环境监测与科学研究。该航次是中国科学院海岸带环境观测网络的重要组成部分，为渤海海洋生态环境变化评估提供基础数据支撑。',
                'source': '中国海事局 / 中科院烟台海岸带所',
                'url': 'https://www.msa.gov.cn/html/cnmsa/hxaq/article/2026/da74d17597b14f8ca79074075bb37f58.html',
                'date': '2026-07-30'
            }
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'badge': '[动态]',
                'title': 'CMEMS 2026年7月服务发布：SWH空间分辨率提至0.5°、Sentinel-6B数据接入准备、FY-3E WindRAD新数据集（2026-07）',
                'abstract': 'Copernicus Marine Service于7月发布多项产品更新：(1) WAVE产品MIOST瞬时数据集空间分辨率从2°提升至0.5°、时间分辨率从每日提升至6小时；(2) 为Sentinel-6B测高任务新增L3数据集目录条目（数据将于2026年底开始产出）；(3) 新增中国FY-3E WindRAD散射计L3近实时风场数据集（0.25°和0.5°两种分辨率）；(4) SMOS海表盐度上游数据流从CATDS L3Q切换至MULTIOBS L3 MYNRT产品；(5) Sentinel-1C融入L3 NRT Fireworks产品，风暴检测能力提升。双传播期持续至8月11日。',
                'source': 'CMEMS',
                'url': 'https://marine.copernicus.eu/user-corner/user-notification-service',
                'date': '2026-07-07'
            },
            {
                'badge': '[数据]',
                'title': 'NCEI发布OOI海底观测阵列新数据——Axial Seamount海底压力/倾斜与Oregon Offshore pH传感器数据（2026-07-14）',
                'abstract': 'NOAA NCEI分别发布两组来自Ocean Observatories Initiative（OOI）的最新数据：Accession 0316761包含Axial Seamount中央破火山口JBox的纳米级海底压力、海底隆起/沉降和高分辨率倾斜数据（2026-06-27至07-11）；Accession 0316760包含Oregon Offshore有线浅层剖面仪200m平台的pH、电导率和密度数据（2026-06-28至07-12）。两组数据均通过NCEI公开访问、免费下载，为海底地质活动和水体化学长期监测提供关键观测支持。',
                'source': 'NOAA NCEI',
                'url': 'https://www.ncei.noaa.gov/archive/accession/0316761',
                'date': '2026-07-14'
            }
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Open Source Code',
        'items': [
            {
                'badge': '[工具]',
                'title': 'Nauticus Robotics完成AUV电动机械臂首个原型——水下自主操作能力突破（OceanNews 2026-07-28）',
                'abstract': 'Nauticus Robotics宣布完成其自主水下航行器（AUV）电动机械臂的首个原型研制。该电动机械臂专为AUV设计，旨在实现水下自主操作——包括物体抓取、采样和阀门操作等任务，无需人工遥控干预。这标志着水下机器人从"观测"向"操作"的能力跃迁，将显著拓展AUV在深海勘探、水下设施维护和海洋科学研究中的应用场景。',
                'source': 'Ocean News & Technology',
                'url': 'https://oceannews.com/featured-stories/nauticus-robotics-completes-first-prototype-of-electric-manipulator-for-auvs/',
                'date': '2026-07-28'
            },
            {
                'badge': '[工具]',
                'title': 'Ulysses加入Seabed 2030——扩大自主测绘舰队加速全球海底测图（OceanNews 2026-07-27）',
                'abstract': '自主海洋测绘公司Ulysses宣布加入Seabed 2030全球海底测绘倡议。Seabed 2030致力于在2030年前完成全球海底的高分辨率测图，目前已完成约28.7%。Ulysses将贡献其自主水面和水下航行器舰队，通过规模化自主测绘加速深水区域数据采集。此举将显著扩大Seabed 2030的自主测绘能力，推动全球海底地形数据库的建设与完善。',
                'source': 'Ocean News & Technology',
                'url': 'https://oceannews.com/featured-stories/ulysses-joins-seabed-2030-to-scale-autonomous-mapping-fleet/',
                'date': '2026-07-27'
            }
        ]
    }
]

def update_feishu_sections():
    """Update SECTIONS in feishu_write_doc.py using bracket-counting method."""
    src_file = 'feishu_write_doc.py'
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find SECTIONS = [
    marker = 'SECTIONS = ['
    start_idx = content.find(marker)
    if start_idx == -1:
        print("ERROR: Cannot find SECTIONS = [")
        return False
    
    # Bracket counting from SECTIONS = [
    idx = start_idx + len(marker) - 1  # position of opening [
    depth = 0
    sections_end = -1
    for i in range(idx, len(content)):
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
            if depth == 0:
                sections_end = i + 1
                break
    
    if sections_end == -1:
        print("ERROR: Cannot find closing ]")
        return False
    
    # Build new SECTIONS string
    new_sections_str = 'SECTIONS = ' + repr(SECTIONS)
    
    # Replace
    new_content = content[:start_idx] + new_sections_str + content[sections_end:]
    
    # Validate syntax
    try:
        compile(new_content, src_file, 'exec')
        print("Syntax validation PASSED")
    except SyntaxError as e:
        print(f"Syntax validation FAILED: {e}")
        return False
    
    with open(src_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"SECTIONS updated successfully ({len(SECTIONS)} sections)")
    
    # Count items
    total = sum(len(s['items']) for s in SECTIONS)
    for s in SECTIONS:
        print(f"  {s['title']}: {len(s['items'])} items")
    print(f"  Total: {total} items")
    return True

if __name__ == '__main__':
    update_feishu_sections()
