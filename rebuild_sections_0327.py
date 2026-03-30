#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
恢复feishu_write_doc.py：用三引号格式重建SECTIONS，彻底避免引号嵌套
"""
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 先找SECTIONS开始
sections_start = content.find('SECTIONS = [')
# 找到SECTIONS之前的内容（头部代码）
before_sections = content[:sections_start]

# 找SECTIONS结尾
depth = 0
i = sections_start
sections_end_idx = sections_start
while i < len(content):
    if content[i] == '[':
        depth += 1
    elif content[i] == ']':
        depth -= 1
        if depth == 0:
            sections_end_idx = i
            break
    i += 1

# 找SECTIONS之后的内容（函数代码）
after_sections = content[sections_end_idx+1:]

# 新的SECTIONS内容，使用单引号避免双引号冲突
# 所有字符串用单引号包裹，内部可以自由使用双引号
new_sections = """SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. SeaCast：图神经网络驱动的高分辨率区域海洋预报模型——20秒完成15天预报',
                'badge': '[新发]',
                'abstract': (
                    'SeaCast 是芬兰赫尔辛基大学、地中海气候变化研究中心与意大利萨伦托大学联合研发的图神经网络模型，'
                    '专为区域海洋预报设计。训练完成后，在单块 GPU 上仅需20秒，即可完成 1/24° 网格下18个垂向层次的15天预报，'
                    '远快于在 CPU 集群上运行的数值物理模型（后者需89个CPU核心耗时约70分钟）。'
                    'SeaCast 采用图神经网络捕获不规则海洋网格上的空间依赖关系，'
                    '在地中海预报系统中验证效果显著，为高时效业务化海洋预报提供了新范式。'
                    '相关论文发表于 Scientific Reports（2025-03），腾讯科学 2026-02-27 进行了深度报道。'
                ),
                'source': '腾讯新闻 / Scientific Reports',
                'date': '2026-02-27',
                'url': 'https://new.qq.com/rain/a/20260227A035B900'
            },
            {
                'title': '2. 中科院突破跨域船只识别难题：让光学卫星与SAR雷达卫星识别同一艘船',
                'badge': '[新发]',
                'abstract': (
                    '中国科学院空间应用工程与技术中心领导的研究团队于2026年3月在 IEEE 地球科学与遥感汇刊发表研究成果（arXiv:2603.12588v1），'
                    '提出新方法解决光学卫星与合成孔径雷达（SAR）卫星的跨模态船只识别难题。'
                    '光学图像呈现船只纹理颜色，SAR 图像显示微波反射强度分布，两者外观差异巨大，'
                    '该研究通过跨域特征对齐和对比学习方法实现高精度匹配，'
                    '为海上安全监控、违规捕捞稽查和军事侦察提供了重要技术支撑，于腾讯新闻 2026-03-24 报道。'
                ),
                'source': '腾讯新闻 / IEEE TGRS / arXiv:2603.12588',
                'date': '2026-03-24',
                'url': 'https://new.qq.com/rain/a/20260324A03M8400'
            },
            {
                'title': '3. EBA-AI：面向珊瑚礁监测的伦理引导偏差感知 AI 水下图像增强框架',
                'badge': '[论文]',
                'abstract': (
                    'Springer Nature 于2026年1月出版专著章节 EBA-AI: Ethics-Guided Bias-Aware AI，'
                    '提出将伦理约束与偏差感知机制融入水下图像增强的 AI 框架。'
                    '该方法针对复杂水下光学条件（散射、吸收、色偏），'
                    '构建面向珊瑚礁生态系统多时空监测的多标签分类模型，'
                    '实现高效、低偏差的珊瑚礁健康状态自动识别，'
                    '对海洋生物多样性评估和气候变化响应研究具有重要意义。'
                ),
                'source': 'Springer Nature / CCIS Volume 2721',
                'date': '2026-01-02',
                'url': 'https://link.springer.com/chapter/10.1007/978-3-032-12313-8_35'
            },
            {
                'title': '4. 水下物联网机器学习综述：从基础原理到工程实现（arXiv:2603.07413）',
                'badge': '[综述]',
                'abstract': (
                    'arXiv 预印本（编号 2603.07413）发布综述论文，系统梳理机器学习在水下物联网（IoUT）的应用，'
                    '涵盖声学衰减、传播延迟、能耗约束、动态网络拓扑等核心挑战。'
                    '水下物联网是海洋观测、海洋资源管理和气候科学的关键基础设施，'
                    '该综述覆盖从强化学习优化路径规划，到联邦学习保护数据隐私，'
                    '再到深度神经网络实现实时目标识别等多种机器学习范式，'
                    '为海洋传感器网络智能化提供了全面参考。'
                ),
                'source': 'arXiv / ADS Harvard',
                'date': '2026-03（近期）',
                'url': 'https://ui.adsabs.harvard.edu/abs/arXiv:2603.07413'
            },
            {
                'title': '5. 双教师框架用于浮游动物显微图像半监督分割（MDPI Remote Sensing）',
                'badge': '[论文]',
                'abstract': (
                    '石油大学（华东）海洋信息学院与国家海洋局北海环境监测中心联合发表论文，'
                    '提出一致性驱动的双教师框架（Consistency-Driven Dual-Teacher Framework），'
                    '用于浮游动物显微图像的半监督语义分割。'
                    '该方法充分利用少量标注数据和大量未标注图像，'
                    '在降低人工标注成本的同时显著提升浮游生物识别精度，'
                    '发表于 MDPI Remote Sensing（2026年3月，12卷3期，论文编号125），'
                    '对海洋生态系统监测和渔业资源评估具有实际应用价值。'
                ),
                'source': 'MDPI Remote Sensing / 中国石油大学（华东）',
                'date': '2026-03',
                'url': 'https://www.mdpi.com/2313-433X/12/3/125'
            }
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. 富士通与巴塞罗那港创新基金会：联合开发巴塞罗那港数字孪生 PoC',
                'badge': '[新发]',
                'abstract': (
                    '2026年3月3日，富士通西班牙公司与 BCN 巴塞罗那港创新基金会宣布合作协议，'
                    '联合开发海洋数字孪生概念验证（PoC），专注港口生态系统再生。'
                    '该 PoC 将整合海洋环境实时数据，构建巴塞罗那港沿海生态的高精度数字镜像，'
                    '支持水质监测、生物多样性评估、港口碳中和目标管理，'
                    '是工业界推动海洋数字孪生走向实际港口管理应用的重要里程碑。'
                ),
                'source': 'JCN Newswire / IndonesiaFolk / SeaPRWire',
                'date': '2026-03-03',
                'url': 'https://indonesiafolk.com/jcn-newswire/fujitsu-and-bcn-port-innovation-foundation-leverage-ocean-digital-twin-technology-to-drive-the-regeneration-of-the-port-of-barcelona/'
            },
            {
                'title': '2. EDITO2（2025-2028）：欧洲数字孪生海洋平台正式进入第二阶段，获1400万欧元资助',
                'badge': '[项目]',
                'abstract': (
                    '欧洲数字孪生海洋（EDITO）平台在完成初始孵化阶段后，'
                    '以1400万欧元投入正式启动 EDITO2 第二期项目（2025-2028），'
                    '由 Mercator Ocean International 和比利时海洋研究所（VLIZ）联合领衔。'
                    'EDITO 作为欧洲数字孪生海洋的核心基础设施平台，'
                    '整合国家数字孪生和欧洲研究项目，承载着 EU 使命"恢复我们的海洋和水域"。'
                    'EDITO2 将深化技术能力，扩大社区规模，推动开放协作，'
                    '并在2025年联合国海洋大会上获得冯德莱恩主席盛赞。'
                ),
                'source': 'VLIZ / EDITO.eu / Mercator Ocean',
                'date': '2025-2026进行中',
                'url': 'https://www.vliz.be/nl/news/european-digital-twin-ocean-nieuwe-fase-om-open-samenwerking-binnen-de-maritieme'
            },
            {
                'title': '3. HKUST WavyOcean 2.0：香港科技大学发布下一代三维沉浸式海洋数字孪生平台',
                'badge': '[新发]',
                'abstract': (
                    '香港科技大学（HKUST）正式推出 WavyOcean 2.0，'
                    '这是一个融合数字孪生技术的下一代区域地球系统沉浸式海洋平台。'
                    '该平台深度集成数字技术与海洋科学，提供三维可视化溶解氧、流场等多变量场景，'
                    '支持大湾区及香港周边海域的立体展示，'
                    '面向海洋研究、可持续发展管理和公众教育三大场景设计，'
                    '是区域海洋数字孪生在亚洲地区的重要实践案例。'
                ),
                'source': 'EurekAlert! / HKUST',
                'date': '2026近期',
                'url': 'https://sciencesources.eurekalert.org/news-releases/1090958'
            },
            {
                'title': '4. Mercator Ocean：EDITO 平台持续对外开放，汇聚欧洲海洋数据资产与数字孪生工具',
                'badge': '[平台]',
                'abstract': (
                    'Mercator Ocean International 维护的欧洲数字孪生海洋平台持续向研究人员、政策制定者、企业和公民开放，'
                    '整合欧洲海洋数字资产，包括各国国家数字孪生和欧洲研究项目成果，'
                    '形成统一的业务化社区驱动系统。'
                    '作为 EU 使命海洋恢复战略的技术支柱，'
                    '用户可通过该平台访问尖端数字孪生开发工具，做出科学决策并最大化研究影响。'
                ),
                'source': 'Mercator Ocean International',
                'date': '2026持续运营',
                'url': 'https://www.mercator-ocean.eu/en/digital-twin-ocean/'
            }
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization',
        'items': [
            {
                'title': '1. Copernicus Marine MyOcean 可定制仪表板（Beta）：交互式海洋数据可视化工作台',
                'badge': '[新功能]',
                'abstract': (
                    'Copernicus Marine Service 于2025年11月发布 MyOcean Dashboards Beta 版，'
                    '提供交互式、可定制的海洋数据探索工作台。'
                    '用户可自由搭配地图、图表和注释构建个性化视图，'
                    '跨时间、空间、深度和变量维度探索海洋状况，'
                    '以 ENSO 厄尔尼诺事件仪表板为样例，展示海温异常时序分析能力。'
                    'MyOcean Viewer 于2026年3月11日完成最新一次更新，'
                    '相关培训资源于2026年2月22日在线发布，是海洋数据可视化的重要免费工具。'
                ),
                'source': 'Copernicus Marine Service',
                'date': '2025-11-26 发布 / 2026-03-11 更新',
                'url': 'https://marine.copernicus.eu/news/new-way-explore-ocean-data-copernicus-marine-customisable-dashboards-beta'
            },
            {
                'title': '2. NOAA OceanReports：面向美国 EEZ 的综合海洋空间数据评估工具',
                'badge': '[新工具]',
                'abstract': (
                    '美国国家海洋和大气管理局（NOAA）与合作伙伴联合发布 OceanReports 工具，'
                    '这是迄今最全面的美国海洋水域网络端空间评估工具，'
                    '覆盖专属经济区（EEZ）内100多个权威数据集，'
                    '支持能源与矿产资源、自然资源（物种与栖息地）、水域条件等专题分析，'
                    '用户可对指定区域进行定制化空间分析，是海洋规划和监管决策的重要可视化平台。'
                ),
                'source': 'NOAA Coastal Science',
                'date': '2026近期发布',
                'url': 'https://coastalscience.noaa.gov/news/noaa-partners-launch-oceanreports-tool/'
            },
            {
                'title': '3. Cape Cod OceanWatch：近实时沿岸海洋条件交互地图仪表板',
                'badge': '[工具]',
                'abstract': (
                    '海洋观测系统效益目录（BOOC）收录 Cape Cod OceanWatch 仪表板，'
                    '这是一个基于地图的交互数据可视化平台，'
                    '为美国东北大陆架和缅因湾地区提供近实时沿岸海洋状况信息，'
                    '集成水文剖面、卫星海洋观测和合作研究多来源数据，'
                    '服务商业渔业、海洋规划和气候监测应用，'
                    '是海洋可视化仪表板与实际社区应用结合的典范案例。'
                ),
                'source': 'BOOC / Middlebury Institute',
                'date': '2026发布',
                'url': 'https://cbe.miis.edu/booc/vol4/iss1/1'
            },
            {
                'title': '4. AOOS Ocean Data Explorer：阿拉斯加海洋数据浏览器（NOAA研讨会2026-02-19介绍）',
                'badge': '[工具]',
                'abstract': (
                    '2026年2月19日，NOAA 科学研讨会系列邀请阿拉斯加海洋观测系统（AOOS）'
                    '介绍其 Ocean Data Explorer 平台，展示如何利用交互式数据可视化工具支持海洋研究和决策。'
                    '该平台集成多源北极及阿拉斯加海洋观测数据，提供地图浏览、时序图、剖面可视化等功能，'
                    '是当前极地海洋数据可视化工具的代表性案例，'
                    '相关视频教程可在 NOAA 官网回放观看。'
                ),
                'source': 'NOAA Science Seminar / AOOS',
                'date': '2026-02-19',
                'url': 'https://www.star.nesdis.noaa.gov/star/OneNOAASeminars.php'
            }
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. QARTOD 实时海洋数据质控手册：OceanBestPractices 平台最新引用（2026-03-07）',
                'badge': '[标准]',
                'abstract': (
                    '美国综合海洋观测系统（IOOS）QARTOD 项目的实时海洋学数据质量保障/质量控制手册，'
                    '于2026年3月7日在 OceanBestPractices 知识库中获得最新引用记录。'
                    'QARTOD 是2003年启动的实时数据质控规范体系，现已成为众多海洋观测站网的认证要求，'
                    '涵盖温度盐度、海流、波浪、海平面等多要素实时数据的自动质控算法规范。'
                    'QARTOD 项目2022-2026路线图持续推进，是全球海洋实时数据质量管理的核心标准。'
                ),
                'source': 'OceanBestPractices / NOAA IOOS',
                'date': '2026-03-07（最新引用）',
                'url': 'https://repository.oceanbestpractices.org/handle/11329/336'
            },
            {
                'title': '2. 机器学习在海洋数据同化中的进展综述：Ocean Modelling 2026年2月发表',
                'badge': '[综述]',
                'abstract': (
                    'ScienceDirect Ocean Modelling 于2026年2月发表综述论文，'
                    '系统梳理2020-2025年间机器学习在海洋数据同化中的应用进展，'
                    '识别新兴趋势、反复出现的挑战与尚未填补的研究空白。'
                    '综述覆盖数据驱动的背景误差协方差估计、混合物理-AI同化框架、'
                    '深度学习观测算子构建等前沿方向，'
                    '为海洋数据质量评估与同化算法改进提供了全面参考。'
                ),
                'source': 'Ocean Modelling / ScienceDirect',
                'date': '2026-02-01',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028'
            },
            {
                'title': '3. 混合机器学习海洋生物地球化学数据同化（Biogeosciences 2026-01）',
                'badge': '[论文]',
                'abstract': (
                    'Copernicus Biogeosciences 于2026年1月12日在线发表论文，'
                    '提出混合机器学习数据同化方法（Hybrid ML-DA），'
                    '应用于海洋生物地球化学模型的关键参数估计与预报校正。'
                    '该方法结合物理约束的生物地球化学模型和机器学习的拟合能力，'
                    '在气候变化背景下提高了生态系统响应预报精度，'
                    '为碳循环评估、富营养化预测等重要环境问题的数据质量改善提供新思路。'
                ),
                'source': 'Copernicus Biogeosciences',
                'date': '2026-01-12',
                'url': 'https://bg.copernicus.org/articles/23/315/2026/'
            },
            {
                'title': '4. IODE 国际海洋数据管理在线培训课程：2026年3月开放报名',
                'badge': '[培训]',
                'abstract': (
                    'UNESCO IOC IOCARIBE 于2026年3月19日在线发布通知，'
                    '开放 IODE 国际海洋数据管理在线自主学习课程（Ocean Data Management Online Training Course）。'
                    '课程涵盖海洋数据管理指导原则、数据质量控制流程、元数据标准、数据共享规范等核心内容，'
                    '完全在线、自定步调，面向全球海洋数据管理从业者开放，'
                    '是提升海洋数据质量管理能力的重要免费培训资源。'
                ),
                'source': 'IOC-UNESCO / IOCARIBE',
                'date': '2026-03-19',
                'url': 'https://iocaribe.ioc-unesco.org/en/event/292'
            }
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '1. xarray 2026.2.0 正式发布：多维海洋数据处理核心库2月更新',
                'badge': '[新发]',
                'abstract': (
                    'xarray 于2026年2月16日发布 2026.2.0 版本，'
                    '这是科学计算中最重要的多维标注数组处理 Python 库之一，'
                    '广泛用于 NetCDF 格式海洋气候数据的读取、处理和分析。'
                    '最新版本在 NaN 跳过聚合、滚动窗口计算、云存储直接读取等方面持续优化，'
                    '配合 Dask 可实现海量海洋数据集的并行云端处理，'
                    '是当前海洋数据科学生态的基础工具。'
                ),
                'source': 'xarray.dev / GitHub',
                'date': '2026-02-16',
                'url': 'https://docs.xarray.dev/en/stable/index.html'
            },
            {
                'title': '2. 高效可扩展 AI 驱动海洋状态估计（arXiv:2511.06041）：解决计算可扩展性瓶颈',
                'badge': '[论文]',
                'abstract': (
                    'arXiv 预印本（2511.06041）提出面向全球海洋状态估计的高效可扩展 AI 方法，'
                    '同时解决计算可扩展性和精度退化两个核心瓶颈。'
                    '通过神经算子和多尺度处理架构，实现了大规模海洋格点数据的高精度状态重建，'
                    '在全球海洋环流模型输出的后处理和数据同化中展现出显著的效率优势，'
                    '为构建覆盖全球的实时海洋数据处理管道提供了技术基础。'
                ),
                'source': 'arXiv',
                'date': '2025-11-08',
                'url': 'https://arxiv.org/abs/2511.06041'
            },
            {
                'title': '3. 深度学习融合 GAN 部分卷积：实现缺失海洋观测数据重建（Nature Machine Intelligence）',
                'badge': '[论文]',
                'abstract': (
                    'Nature Machine Intelligence 2024年发表研究，'
                    '提出基于部分卷积生成对抗网络（Partial-Conv GAN）的海洋数据同化系统，'
                    '可最优融合数值模型预报与实际海洋观测数据，填补观测空白区域。'
                    '该方法在卫星高度计数据缺失区域重建海面高度异常场，'
                    '在南大洋等观测稀疏区表现优于传统最优插值方法，'
                    '为海洋数据再分析产品质量提升提供了深度学习新途径。'
                ),
                'source': 'Nature Machine Intelligence',
                'date': '2024-07-22',
                'url': 'https://www.nature.com/articles/s42256-024-00867-x'
            },
            {
                'title': '4. 数据同化方案综述：支撑海洋预报的观测-模式融合体系（Copernicus Ocean State Report）',
                'badge': '[综述]',
                'abstract': (
                    'Copernicus State of the Planet (OPSR) 第5期综述论文系统梳理支撑海洋预报的数据同化方案，'
                    '涵盖集合卡尔曼滤波（EnKF）、四维变分（4D-Var）等经典方法，'
                    '以及基于机器学习的混合数据同化新进展。'
                    '论文从精度、计算效率、可扩展性等角度比较各方案优劣，'
                    '为海洋数据处理管道的算法选型提供了权威参考，'
                    '面向下一代全球海洋预报系统的研发提出技术路线建议。'
                ),
                'source': 'Copernicus / State of Planet OPSR',
                'date': '2025',
                'url': 'https://sp.copernicus.org/articles/5-opsr/9/2025/sp-5-opsr-9-2025.html'
            }
        ]
    },
    {
        'title': '六、海洋数据管理与共享',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. IODE 国际海洋数据信息交换：全球100+国家海洋数据中心网络（4天前更新）',
                'badge': '[平台]',
                'abstract': (
                    'UNESCO IOC 国际海洋数据信息交换（IODE）项目协调着全球100多个国家海洋数据中心（NODC）'
                    '及关联数据单元（ADU）的数据交换网络，'
                    '覆盖物理海洋、海洋化学、海洋生物、海洋地质等多学科数据。'
                    'IODE 官网 4 天前（约2026年3月23日）完成最新更新，'
                    '持续推进全球海洋数据互操作和开放共享，'
                    '是全球海洋数据基础设施的核心治理节点。'
                ),
                'source': 'IODE / IOC-UNESCO',
                'date': '2026-03-23（更新）',
                'url': 'https://iode.org/'
            },
            {
                'title': '2. IOC-UNESCO 海洋数据与信息：信息服务持续更新（4天前更新）',
                'badge': '[平台]',
                'abstract': (
                    'UNESCO 政府间海洋学委员会（IOC）数据与信息专页于4天前（约2026年3月23日）更新，'
                    '集中展示 IODE 全球数据中心网络、OceanTeacher 培训平台、'
                    '海洋数据标准与互操作规范等最新进展。'
                    'IOC 战略计划2023-2029 中，海洋数据信息管理被列为支撑海洋科学的核心能力，'
                    '此次更新体现了 IOC 对全球海洋数据基础设施持续投入的承诺。'
                ),
                'source': 'IOC-UNESCO',
                'date': '2026-03-23（更新）',
                'url': 'https://www.ioc.unesco.org/en/data-information'
            },
            {
                'title': '3. SeaDataNet 欧洲海洋研究数据共享基础设施：持续推进泛欧数据互联',
                'badge': '[平台]',
                'abstract': (
                    'SeaDataNet 作为欧洲海洋研究基础设施，'
                    '通过 SeaDataCloud、SeaDataNet2 等欧盟项目持续推进泛欧海洋数据互操作与共享。'
                    '平台整合欧洲各国海洋研究机构的历史和实时观测数据，'
                    '提供统一元数据目录、标准化数据格式和共享 API，'
                    '在海洋地质样品库、水文观测档案、生物多样性数据共享方面发挥关键作用，'
                    '是欧洲乃至全球海洋数据共享的重要基础设施节点。'
                ),
                'source': 'SeaDataNet',
                'date': '2026持续运营',
                'url': 'https://www.seadatanet.org/'
            },
            {
                'title': '4. Copernicus Marine Service（CMEMS）：4天前持续更新，全球海洋数据产品服务',
                'badge': '[服务]',
                'abstract': (
                    'Copernicus Marine Service 官网于 4 天前（约2026年3月23日）完成最新更新，'
                    '持续提供覆盖物理、生物地球化学、海冰等要素的全球和区域海洋数据产品，'
                    '包括实时观测、预报模型输出和再分析数据集。'
                    '2026年3月产品路线图涵盖 Sentinel-1C 数据集上线、原位数据库更新至 WOA23、'
                    '多个区域预报系统精度提升等重要内容，'
                    '为科研、政策和商业用户提供一站式海洋数据访问服务。'
                ),
                'source': 'Copernicus Marine / Copernicus.eu',
                'date': '2026-03-23（更新）',
                'url': 'https://www.copernicus.eu/en/copernicus-services/marine'
            },
            {
                'title': '5. OceanTeacher Global Academy：IODE 全球海洋数据人才培训平台持续开放',
                'badge': '[培训]',
                'abstract': (
                    'IODE OceanTeacher Global Academy（OTGA）提供综合性互联网培训平台，'
                    '支持课堂培训、混合培训和在线远程学习三种模式，'
                    '覆盖海洋数据管理、质量控制、元数据标准、数据产品开发等多个专业方向。'
                    '作为 IOC 能力建设的核心载体，OTGA 面向发展中国家海洋数据人才提供免费课程，'
                    '对提升全球海洋数据共享与管理整体水平发挥了关键作用。'
                ),
                'source': 'IODE / OceanTeacher',
                'date': '2026持续开放',
                'url': 'https://iode.org/actions/capacity-development/'
            }
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. 「深蓝梦想2035」环球科考正在太平洋航段执行中——向阳红10号现役',
                'badge': '[动态]',
                'abstract': (
                    '「深蓝梦想2035」是中国首个以全民参与模式开展的环球海洋科考行动，'
                    '由张占海总召集人、林间院士首席科学家，于2025年10月31日从深圳蛇口码头起航。'
                    '依托「向阳红10」号科考船，覆盖太平洋、南大洋、大西洋、印度洋200天科考方案，'
                    '整合南科大、中科院等多机构参与，实施无人集群智能科考。'
                    '截至2026年3月，行动正在太平洋航段执行中，'
                    '是目前中国规模最大的开放共享科考航次实践。'
                ),
                'source': '搜狐 / 今日头条 / 南科大',
                'date': '2025-10-31启航，2026年3月执行中',
                'url': 'https://www.sohu.com/a/949980447_726570'
            },
            {
                'title': '2. 深蓝智能i3航次：南科大无人集群挺进深蓝，全球开放参与海洋科考',
                'badge': '[航次]',
                'abstract': (
                    '2025年7月7日，南方科技大学海洋高等研究院牵头，'
                    '联合科研院所、高新企业及科普机构启动「深蓝智能i3航次」，'
                    '作为「深蓝梦想2035」环球科考十年计划的试验航次，'
                    '部署空、海、潜三栖无人集群系统，'
                    '探索人工智能辅助科学考察的新范式。'
                    '该航次开创性地采用全球开放、全民参与的共享科考模式，'
                    '邀请社会公众参与海洋科考全过程，'
                    '是中国船时共享和开放科考的标志性实践。'
                ),
                'source': '腾讯新闻 / 南科大 / 今日头条',
                'date': '2025-07-07启航',
                'url': 'https://news.qq.com/rain/a/20250708A06P4000'
            },
            {
                'title': '3. 「深蓝梦想2035」科考规划：200天覆盖四大洋，研讨会推进分航段召集',
                'badge': '[规划]',
                'abstract': (
                    '上海海洋大学等10家机构专家联合制定「深蓝梦想2035」200天科考方案，'
                    '覆盖太平洋（已执行）、南大洋、大西洋、印度洋四大洋，'
                    '分别召集各航段首席科学家和参与机构。'
                    '2025年7-9月间召开多次航次研讨会，明确任务目标、仪器配置和数据共享机制。'
                    '该方案是迄今中国最系统化的长期开放航次规划，'
                    '对推动中国海洋科考数据开放共享、提升国际影响力具有战略意义。'
                ),
                'source': '上海海洋大学海洋学院',
                'date': '2025年规划，2026年执行中',
                'url': 'https://hkxy.shou.edu.cn/dome/2025/1103/c18107a347792/page.htm'
            },
            {
                'title': '4. 「向阳红10」号2026年1月开放日：寒假公众开放体验国之重器',
                'badge': '[开放]',
                'abstract': (
                    '「向阳红10」号科考船于2026年1月9日前后举办公众开放日活动，'
                    '面向寒假期间青少年和公众开放参观，'
                    '推广海洋科普教育，提升公众对科考船及海洋科学的认知。'
                    '该船作为中国首艘由国家海洋研究机构与民营企业共建的科考船，'
                    '以全球开放、全民参与理念积极响应联合国「海洋十年」倡议，'
                    '是中国开放船时共享模式的代表性平台。'
                ),
                'source': '大数网 / 10100.com',
                'date': '2026-01-09',
                'url': 'https://www.10100.com/article/86924164'
            }
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Archives / Repositories',
        'items': [
            {
                'title': '1. Argo GDAC AWS 开放数据集：2天前更新，覆盖全球浮标数据与元数据',
                'badge': '[数据]',
                'abstract': (
                    'Argo GDAC（全球数据集成中心）在 AWS Open Data Registry 上维护的'
                    'Argo 浮标海洋数据集于2天前（2026年3月25日）完成最新更新，'
                    '提供全球 Argo 剖面浮标的温度、盐度等实时和延时模式数据及完整元数据。'
                    '数据集包含化学生物学、气候、数据中心、数字资产等多维标签，'
                    '支持直接通过 AWS S3 云存储访问，'
                    '是全球海洋气候研究最重要的开放数据档案之一。'
                ),
                'source': 'AWS Open Data / Argo GDAC',
                'date': '2026-03-25（最新更新）',
                'url': 'https://registry.opendata.aws/argo-gdac-marinedata/'
            },
            {
                'title': '2. PANGAEA：2026年1月6日更新，地球环境科学开放数据发布平台',
                'badge': '[数据]',
                'abstract': (
                    'PANGAEA 数据发布系统（地球与环境科学数据出版商）于2026年1月6日完成网站更新，'
                    '提供地球系统研究地理参考数据的归档、发布和分发服务，'
                    '已运营近30年，存储海量海洋地质、海洋化学、古海洋和物理海洋等多学科数据集。'
                    '作为世界数据中心之一，PANGAEA 与 IODP、AWI、MARUM 等重要研究机构深度合作，'
                    '是海洋沉积、地质样品数据共享的核心开放仓库。'
                ),
                'source': 'PANGAEA.de',
                'date': '2026-01-06',
                'url': 'https://pangaea.de/'
            },
            {
                'title': '3. NOAA NCEI Argo 全球数据仓库：美国国家环境信息中心海洋档案',
                'badge': '[档案]',
                'abstract': (
                    'NOAA 国家环境信息中心（NCEI）是美国最重要的环境数据档案机构，'
                    '托管 Argo 全球数据仓库（Global Argo Data Repository），'
                    '负责 Argo 浮标温盐剖面数据的国家级存档与公开访问服务。'
                    'NCEI 存储超过20亿条环境数据记录，'
                    '涵盖海洋温度、盐度、化学组分、海冰范围等多类型海洋气候数据，'
                    '是全球规模最大的环境数据档案系统之一，支持气候变化研究和海洋政策决策。'
                ),
                'source': 'NOAA NCEI',
                'date': '持续运营',
                'url': 'https://www.nodc.noaa.gov/argo/'
            },
            {
                'title': '4. Euro-Argo ERIC：欧洲 Argo 数据系统——观测后数小时内免费公开数据',
                'badge': '[系统]',
                'abstract': (
                    'Euro-Argo ERIC 介绍 Argo 数据系统，'
                    '所有 Argo 国际计划数据在采集后数小时内通过卫星传输并公开发布，'
                    '通过两个全球数据集成中心（美国 GDAC 和法国 GDAC）向全球免费开放。'
                    'Euro-Argo ERIC 作为欧洲 Argo 研究基础设施联合体，'
                    '协调欧洲 Argo 浮标部署、数据管理和质量控制，'
                    '目前全球 Argo 网络拥有约4000个活跃浮标，每年新增约150万条剖面数据。'
                ),
                'source': 'Euro-Argo ERIC',
                'date': '2026持续运营',
                'url': 'https://www.euro-argo.eu/Activities/Data-Management/Argo-Data-System'
            }
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources (GitHub etc.)',
        'items': [
            {
                'title': '1. xarray 2026.2.0：多维海洋数据处理Python核心库2月正式发布',
                'badge': '[发布]',
                'abstract': (
                    'xarray 于2026年2月16日发布 2026.2.0 新版本，'
                    '是科学计算和海洋数据处理生态的核心工具，'
                    '提供带标签的多维数组（DataArray）和数据集（Dataset）操作接口。'
                    '新版本优化了 NaN 跳过统计、滚动聚合、坐标系插值等关键功能，'
                    '完善了 Dask 懒计算和云存储集成，'
                    '广泛应用于 NetCDF/Zarr 格式海洋气候数据的读取、处理、可视化和共享管道。'
                ),
                'source': 'xarray.dev / GitHub / PyPI',
                'date': '2026-02-16',
                'url': 'https://docs.xarray.dev/en/stable/index.html'
            },
            {
                'title': '2. CloudDrift：专为 Argo 和漂流浮标拉格朗日数据设计的 Python 分析工具包',
                'badge': '[工具]',
                'abstract': (
                    'CloudDrift 是 NSF EarthCube 资助的开源 Python 包，'
                    '专为大气、海洋和气候科学拉格朗日数据处理而设计，'
                    '适用于 Argo 浮标轨迹、表层漂流浮标、动物追踪等不规则时序数据。'
                    '工具采用 awkward-array 实现不规则数组高效处理，'
                    '支持 AWS S3/GCS 云存储直接读取，提供完整的轨迹分析、统计聚合和可视化功能，'
                    '是当前海洋拉格朗日数据云原生处理的最佳实践工具。'
                ),
                'source': 'CloudDrift / GitHub',
                'date': '2025-09（最新文档）',
                'url': 'https://github.com/Cloud-Drift/clouddrift'
            },
            {
                'title': '3. NASA Earthdata Sentinel-3B OLCI 海洋颜色数据产品：1天前更新',
                'badge': '[数据]',
                'abstract': (
                    'NASA Earthdata 目录于1天前（2026年3月26日）更新 Sentinel-3B OLCI Level-2'
                    ' Regional Earth-observation Full Resolution（EFR）海洋颜色（OC）数据套件，'
                    '提供经过大气校正的海洋光学测量和生物地球物理产品，'
                    '包括叶绿素浓度、悬浮颗粒物、有色溶解有机物等关键海洋水色参数。'
                    '数据可通过 Earthdata Search 免费下载，'
                    '是近岸和开阔大洋水质监测的重要遥感数据源。'
                ),
                'source': 'NASA Earthdata',
                'date': '2026-03-26（最新更新）',
                'url': 'https://www.earthdata.nasa.gov/data/catalog/ob-cloud-olcis3b-l2-efr-oc-2022.0'
            },
            {
                'title': '4. QARTOD GitHub 开源实现：实时海洋质控算法 Python 代码库（physoce/qartod）',
                'badge': '[工具]',
                'abstract': (
                    'GitHub 仓库 physoce/qartod 提供 QARTOD 实时海洋数据质控算法的 Python 开源实现，'
                    '基于 NOAA IOOS QARTOD 手册的规范，'
                    '实现温度盐度原位数据的一系列自动质控测试，'
                    '包括范围检查、突变检测、坡度检测、平坦剖面检测等核心算法。'
                    '该库可作为构建海洋观测数据质控流水线的基础组件，'
                    '适合集成到海洋数据中心的实时数据处理管道中。'
                ),
                'source': 'GitHub / physoce/qartod',
                'date': '持续维护',
                'url': 'https://github.com/physoce/qartod'
            },
            {
                'title': '5. LibHunt 海洋学开源项目 Top 榜：iris、VIAME、PlanktoScope、clouddrift 等工具汇总',
                'badge': '[工具集]',
                'abstract': (
                    'LibHunt 整理发布了海洋学领域最受关注的开源项目 Top 列表，包括：'
                    'iris（MetOffice 出品，支持 NetCDF/GRIB 格式科学数据分析）；'
                    'VIAME（海洋视觉分析与识别工具，支持鱼类和海洋生物目标检测）；'
                    'PlanktoScope（低成本开源浮游生物成像仪）；'
                    'clouddrift（拉格朗日浮标轨迹数据分析）；'
                    'pyobis（OBIS 海洋生物多样性数据库 Python 访问接口）。'
                    '该列表是了解海洋学开源工具生态全貌的快速参考。'
                ),
                'source': 'LibHunt / libhunt.com',
                'date': '持续维护',
                'url': 'https://www.libhunt.com/topic/oceanography'
            }
        ]
    }
]"""

# 找SECTIONS开始位置
sections_start = content.find('SECTIONS = [')
if sections_start == -1:
    print('ERROR: 找不到 SECTIONS = [')
    exit(1)

# 找结尾
depth = 0
i = sections_start
sections_end_idx = sections_start
while i < len(content):
    if content[i] == '[':
        depth += 1
    elif content[i] == ']':
        depth -= 1
        if depth == 0:
            sections_end_idx = i
            break
    i += 1

before = content[:sections_start]
after = content[sections_end_idx+1:]

new_content = before + new_sections + after

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

try:
    ast.parse(new_content)
    print('语法验证通过 ✅')
except SyntaxError as e:
    print(f'语法错误 ❌ 第 {e.lineno} 行: {e.msg}')
    lines = new_content.splitlines()
    for j in range(max(0, e.lineno-3), min(len(lines), e.lineno+2)):
        print(f'  {j+1}: {repr(lines[j][:120])}')
