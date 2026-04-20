#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接以数据对象形式定义，绕过字符串引号冲突
"""
import requests
import json
import sys
import time
from datetime import datetime, timedelta

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
TENANT_DOMAIN = "wcn5jx0ifkx3.feishu.cn"

yesterday_cn = (datetime.now()).strftime('%Y\u5e74%m\u6708%d\u65e5')
today_date = (datetime.now()).strftime('%Y-%m-%d')

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. OceanPredict AI-TT国际研讨会（2026-04-13~14）：机器学习用于海洋预报——方法、应用与挑战',
                'badge': '[会议]',
                'abstract': (
                    'OceanPredict AI任务团队（AI-TT）国际研讨会于2026年4月13~14日在法国图卢兹大学举办（Mercator Ocean International主办），主题为"Machine Learning for Ocean Prediction: Methods, Applications & Challenges"，汇聚来自全球顶级海洋预报中心、研究机构的AI专家，聚焦神经网络方法在海洋状态估计、季节预报和极端事件预警中的最新进展，是当前全球规模最大的海洋AI预报专题学术交流活动之一。'
                ),
                'source': 'OceanPredict / Mercator Ocean International / AI-TT',
                'url': 'https://www.mercator-ocean.eu/event/oceanpredict-ai-task-team-workshop/',
                'date': '2026-04-13',
            },
            {
                'title': '2. SciTechDaily：AI揭示全球海洋浮游藻类爆炸性增长——20年卫星图像机器学习分析',
                'badge': '[进展]',
                'abstract': (
                    'SciTechDaily（2026-04-20）报道，科学家利用AI分析20年卫星图像数据，发现全球海洋浮游大型藻类（浮游巨藻）正以前所未有的速度增长和扩张，在多个大洋区域均检测到显著异常扩张信号。该研究建立在Nature Communications（2025-12）已发表的全球浮游藻类分布综合图像基础上，利用机器学习提供了首个系统性的长时序藻类生物量变化趋势评估，成果对海洋碳循环、渔业生态和气候反馈研究具有重要意义。'
                ),
                'source': 'SciTechDaily / Nature Communications / Columbia Climate School',
                'url': 'https://scitechdaily.com/ai-reveals-explosive-growth-of-floating-algae-across-the-worlds-oceans/',
                'date': '2026-04-20',
            },
            {
                'title': '3. Springer Marine Systems：深度学习目标检测与图像增强在海洋视觉系统中的应用综述',
                'badge': '[综述]',
                'abstract': (
                    'Springer Journal of Marine Systems（2026-04-14在线）发表题为"A comprehensive review of deep learning techniques for object detection and image enhancement in marine vision systems"的综述，系统梳理深度学习目标检测（YOLO系列、Faster R-CNN、Transformer检测器）和图像增强技术在水下视觉、海洋生物识别、船舶检测和遥感目标提取中的最新进展，总结各类方法在复杂海洋光学环境下的性能表现，是海洋视觉AI领域的重要参考文献。'
                ),
                'source': 'Springer / Journal of Marine Systems',
                'url': 'https://link.springer.com/article/10.1007/s40868-026-00223-1',
                'date': '2026-04-14',
            },
            {
                'title': '4. ScienceDirect Ocean Modelling：DeepDA——基于深度学习的潜空间非线性海洋演化数据同化框架',
                'badge': '[新论文]',
                'abstract': (
                    'Ocean Modelling（ScienceDirect，2026-02-01在线）发表DeepDA研究，提出基于深度学习的数据同化框架，通过在低维潜空间中操作，解决了传统集合卡尔曼滤波在高非线性海洋系统中的性能局限，在海洋环流和中尺度涡同化实验中显著提升了预报精度，代码已开源，是AI数据同化进入实际海洋预报的重要里程碑。'
                ),
                'source': 'ScienceDirect / Ocean Modelling',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000016',
                'date': '2026-02-01',
            },
        ],
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. EGU2026大会（4月22日开幕）：Copernicus Marine Service与欧洲数字孪生海洋专题会议预告',
                'badge': '[会议]',
                'abstract': (
                    'EGU General Assembly 2026（维也纳，2026年4月22日至5月8日开幕）设置专题会议OS4.8"The Copernicus Marine Service and the European Digital Twin of the Ocean"，由Mercator Ocean International牵头主办，汇聚欧洲海洋预报、遥感和DTO研究领域的最新成果。Copernicus Marine官网（2026-04-13更新）已发布会议详情，本专题将集中展示CMEMS新产品、EDITO进展和DTO用户服务升级，是欧洲海洋数字孪生生态系统年度最重要的学术交流窗口。'
                ),
                'source': 'Copernicus Marine Service / EGU 2026 / Mercator Ocean',
                'url': 'https://events.marine.copernicus.eu/egu-26',
                'date': '2026-04-13',
            },
            {
                'title': '2. Copernicus Marine Service（2026-04-03）：4月三款新产品发布——北极、模型和海洋学产品全线升级',
                'badge': '[更新]',
                'abstract': (
                    'Copernicus Marine Service（CMEMS）官网（2026-04-03）宣布4月集中发布三款新产品和更新产品，为北极海洋观测、数值预报模型和海洋气候学产品提供新数据源，进一步丰富CMEMS数据目录。新产品已接入CMEMS数据仓（Copernicus Marine Data Store），通过统一API开放下载与在线可视化，是欧洲DTO数据基础设施持续扩充的重要组成。'
                ),
                'source': 'Copernicus Marine Service / CMEMS',
                'url': 'https://marine.copernicus.eu/news/april-releases-copernicus-marine-launches-three-new-products',
                'date': '2026-04-03',
            },
            {
                'title': '3. EuroGOOS：EGU2026海洋数字孪生摘要征集已截止——预期新成果集中亮相',
                'badge': '[动态]',
                'abstract': (
                    'EuroGOOS官网（2025-10-23发布征集公告）介绍EGU2026大会OS4.8专题（Copernicus Marine Service and EU DTO）摘要征集情况，会议汇聚了来自欧洲各国海洋研究机构、预报中心和DTO项目的最新研究成果，聚焦CMEMS新一代模型产品、DTO用户场景应用、AI辅助海洋预报和极端事件预警等前沿方向，将于4月22日起在维也纳正式召开，是全球海洋数字孪生领域的年度旗舰会议。'
                ),
                'source': 'EuroGOOS / EGU2026 / Copernicus Marine',
                'url': 'https://eurogoos.eu/news/egu-general-assembly-2026-call-for-abstracts-now-open/',
                'date': '2026-04-20',
            },
        ],
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Data Visualization',
        'items': [
            {
                'title': '1. NASA Earthdata SOTO（2026-04-15更新）：NASA海洋状态交互可视化工具——支持多变量动态地图与动画',
                'badge': '[更新]',
                'abstract': (
                    'NASA Earthdata发布的State of the Ocean（SOTO）工具（2026-04-15，5天前更新）是面向公众和研究者的交互式在线海洋状态可视化平台，支持SST、叶绿素、海面高度异常、海冰范围等多类卫星遥感和模型产品的动态地图展示与动画生成，用户可通过时间滑条浏览历史变化趋势，并导出可视化结果。SOTO是NASA EarthData生态系统中直观理解全球海洋变化的核心公众工具，近期针对移动端进行了交互优化。'
                ),
                'source': 'NASA Earthdata / SOTO / State of the Ocean',
                'url': 'https://www.earthdata.nasa.gov/data/tools/soto',
                'date': '2026-04-15',
            },
            {
                'title': '2. arXiv：pyParaOcean——专为海洋数据设计的可扩展交互式可视化系统',
                'badge': '[工具]',
                'abstract': (
                    'arXiv（2025-01-09）发表pyParaOcean系统论文，介绍专为大规模海洋模型数据设计的可扩展可视化系统，基于ParaView并行可视化引擎，提供针对海洋数据的专用模块，支持三维流场、温盐剖面、中尺度涡旋等典型海洋结构的交互式高性能可视化，系统已在多个国家级海洋预报中心的大规模数据集上验证，可有效处理PB级全球海洋模型输出，是海洋大数据可视化的重要开源工具。'
                ),
                'source': 'arXiv / pyParaOcean / ParaView',
                'url': 'https://arxiv.org/html/2501.05009v1',
                'date': '2025-01-09',
            },
            {
                'title': '3. DFO Ocean Navigator（GitHub，2026-01-19更新）：加拿大渔业海洋部开源3D海洋模型输出可视化工具',
                'badge': '[工具]',
                'abstract': (
                    '加拿大渔业与海洋部（DFO）开源项目Ocean Navigator（GitHub 2026-01-19更新）是一款用于快速发现和查看三维海洋模型输出的在线可视化工具，后端存储NetCDF4格式模型数据，支持用户在浏览器中按区域、时间和变量自由选择可视化方案，提供剖面、时间序列和地图图层等多种展示模式，是业务化海洋模型结果面向用户快速分发展示的典型开源实现案例。'
                ),
                'source': 'DFO Canada / GitHub / Ocean Navigator',
                'url': 'https://github.com/DFO-Ocean-Navigator/Ocean-Data-Map-Project',
                'date': '2026-01-19',
            },
        ],
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. Springer Data Mining and Knowledge Discovery：主动学习用于海洋数据质量评估——结合Argo、GLOSS和EMSO的方法研究',
                'badge': '[新论文]',
                'abstract': (
                    'Springer Data Mining and Knowledge Discovery（2025-04-08在线）发表论文，提出将主动学习（Active Learning）应用于海洋数据质量评估，针对Argo、GLOSS和EMSO等大型海洋观测项目产生的海量剖面数据，通过迭代式标注策略大幅减少人工标注需求，同时保持或提升自动化质控分类精度，在多个典型海洋变量和区域的QC任务中验证了方法有效性，为AI辅助海洋数据质控的规模化部署提供了实用路径。'
                ),
                'source': 'Springer / Data Mining and Knowledge Discovery / Argo QC',
                'url': 'https://link.springer.com/article/10.1007/s41060-025-00751-w',
                'date': '2025-04-08',
            },
            {
                'title': '2. Argo.ucsd.edu 数据服务（2026-04-20当前）：Argo GDAC全球海洋剖面数据实时与延时质控数据持续开放',
                'badge': '[进展]',
                'abstract': (
                    'Argo国际项目官网（argo.ucsd.edu，当前活跃）持续提供全球Argo浮标数据通过GDAC（全球数据组装中心）的开放下载服务，覆盖温度、盐度及BGC参数的实时（RTQC）与延时模式（DMQC）质控数据，采用统一的Argo NetCDF格式分发，全球已有超过4,000枚活跃浮标持续贡献观测，配套API支持按地理区域、时间范围和参数类型检索，是全球海洋次表层观测数据质量保障与开放共享的核心基础设施。'
                ),
                'source': 'Argo Program / UCSD Scripps / Argo GDAC',
                'url': 'https://argo.ucsd.edu/data/',
                'date': '2026-04-20',
            },
            {
                'title': '3. arXiv预印本（2023-12）：通过离群点检测的海洋数据质量评估——适用于Argo等大型观测网络',
                'badge': '[工具方法]',
                'abstract': (
                    'arXiv（2023-12-18）预印本提出基于离群点检测的海洋数据质量自动评估方法，针对Argo、GLOSS和EMSO等大规模海洋观测网络的质控挑战，采用无监督异常检测算法识别剖面中的可疑数据点，与传统阈值法和人工审核相比，在温度和盐度剖面的异常识别中展现出更高的召回率和可解释性，方法已对接Argo实时数据流进行验证，代码开源，是近年被引频次较高的海洋QC自动化参考论文。'
                ),
                'source': 'arXiv / Ocean Data Quality / Argo QC',
                'url': 'https://arxiv.org/abs/2312.10817',
                'date': '2023-12-18',
            },
        ],
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '1. ScienceDirect Ocean Modelling：机器学习在海洋数据同化中的进展、差距与挑战——2020-2025系统综述',
                'badge': '[综述]',
                'abstract': (
                    'Ocean Modelling（ScienceDirect，2026-02-01在线）发表系统综述，梳理2020-2025年机器学习在海洋数据同化领域的最新应用进展，识别当前主要技术差距，包括训练数据不足、模型可解释性差、与物理约束结合困难等挑战，并提出未来发展方向。综述涵盖神经网络集合滤波、生成对抗网络用于数据插补、图神经网络用于非规则网格同化等典型方向，是海洋数据处理AI化进程的权威综述文献。'
                ),
                'source': 'ScienceDirect / Ocean Modelling',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028',
                'date': '2026-02-01',
            },
            {
                'title': '2. Copernicus Publications（2025-06）：Crafting the Future——机器学习用于海洋预报综合报告',
                'badge': '[报告]',
                'abstract': (
                    'State of Planet（Copernicus/EGU，2025年6月）发布专题报告"Crafting the Future: Machine learning for ocean forecasting"，系统评估人工智能和机器学习在地球系统科学尤其是海洋预报领域的变革潜力，重点分析深度学习模型替代或增强传统数值预报模式的可行路径，探讨数据驱动方法在海洋热浪、极端降水和季节预测中的应用前景，是当前AI海洋预报领域最具参考价值的政策导向性综述报告之一。'
                ),
                'source': 'State of Planet / Copernicus Publications / EGU',
                'url': 'https://sp.copernicus.org/articles/5-opsr/22/2025/sp-5-opsr-22-2025.pdf',
                'date': '2025-06-02',
            },
            {
                'title': '3. SEA-PY（2026-03-23更新）：Python海洋数据处理工具目录——汇聚海洋气象全套Python生态',
                'badge': '[工具]',
                'abstract': (
                    'SEA-PY（pyoceans.github.io/sea-py，2026-03-23更新）是Python海洋学和海洋气象数据处理工具的综合目录，收录pyoos（气象海洋观测数据采集）、pytroll（气象卫星数据读写）、gsw（国际海洋状态方程TEOS-10）等海洋数据处理全链条工具，按数据获取、数据处理、可视化和模型接口分类组织，是快速定位合适Python海洋数据处理工具的高效索引入口，持续维护更新。'
                ),
                'source': 'SEA-PY / pyoceans / Python oceanography tools',
                'url': 'https://pyoceans.github.io/sea-py/',
                'date': '2026-03-23',
            },
        ],
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. PANGAEA数据库（2026-04-07公告）：5月举办"Finding and Retrieving Data"社区研讨会',
                'badge': '[活动]',
                'abstract': (
                    'PANGAEA（地球与环境科学数据出版商，AWI/MARUM联合运营）官网（2026-04-07发布）宣布将于2026年5月7~8日（10:30~12:30 CEST）在线举办社区培训研讨会"Finding and Retrieving Data"，面向科研人员提供PANGAEA数据检索、数据集引用、元数据管理和数据下载接口的实操培训，注册已开放。PANGAEA是全球最重要的地球科学数据开放存储和出版平台之一，为Argo、WOCE、PIRATA等多个海洋观测项目提供长期数据存档与开放分发服务。'
                ),
                'source': 'PANGAEA / AWI / MARUM',
                'url': 'https://pangaea.de/news/',
                'date': '2026-04-07',
            },
            {
                'title': '2. Copernicus Marine数据仓（2026-04-19更新）：统一平台整合全球海洋物理、生化和海冰产品',
                'badge': '[更新]',
                'abstract': (
                    'Copernicus Marine Data Store（data.marine.copernicus.eu，2026-04-19更新）持续整合全球海洋物理（蓝色）、生化（绿色）和海冰（白色）三大类数据产品，覆盖近海、极地和全球尺度，提供历史、当前和短期预报数据的统一API下载和在线可视化入口，遵循完全免费开放原则。平台最新版本进一步扩充了数据目录、优化了检索接口，是欧洲海洋数字孪生基础数据供给的核心枢纽。'
                ),
                'source': 'Copernicus Marine Service / Data Store',
                'url': 'https://data.marine.copernicus.eu/',
                'date': '2026-04-19',
            },
            {
                'title': '3. ResearchVessels.org（2025-10-31更新）：全球科考船时间表与规范数据库——连接海洋航次与数据共享',
                'badge': '[平台]',
                'abstract': (
                    'ResearchVessels.org（2025-10-31更新）是汇聚全球科考船规格参数、航次计划和联系信息的综合数据库，由oceandata.org团队维护，覆盖各国海洋研究机构和海军水文机构的科考船队，提供船只规格（甲板面积、实验室配置、传感器清单）和已发布航次时间表，是研究人员申请搭载科考船、查找合作航次和协调船时共享的重要公共信息平台，持续征集全球各科考船信息更新。'
                ),
                'source': 'ResearchVessels.org / oceandata.org',
                'url': 'https://researchvessels.org/',
                'date': '2025-10-31',
            },
        ],
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. NSFC国家自然科学基金共享航次计划（2026年度）：面向科学问题征集考察需求',
                'badge': '[申请]',
                'abstract': (
                    '国家自然科学基金委员会（NSFC）持续推进共享航次计划，2026年度征集包括年度常规航次搭载需求和重大科学技术问题考察需求两类，旨在优化海洋科考船资源配置，提升开放共享水平，航次数据须按规定提交国家海洋科学数据中心，是推动我国海洋科考数据资源有序开放共享的核心政策机制。全国各高校和研究所均可申请，鼓励交叉学科团队联合参与。'
                ),
                'source': 'NSFC / 国家自然科学基金委员会 / 共享航次计划',
                'url': 'https://www.nsfc.gov.cn/p1/3381/2824/66856.html',
                'date': '2026-04-20',
            },
            {
                'title': '2. UNOLS（2026-03-04更新）：美国海洋研究船联盟早期职业项目——研究生与早期研究者出海培训机会',
                'badge': '[进展]',
                'abstract': (
                    'UNOLS（University-National Oceanographic Laboratory System，2026-03-04更新）Early Career Program为研究生、早期职业研究人员和技术人员提供科考船实操培训机会，培训内容涵盖船载仪器操作、CTD采样规程、水下声学探测和海洋气象观测等，参与者可在美国顶级科考船上获得实际海洋调查经验，并在培训期间收集的数据须依照开放政策提交UNOLS数据中心，是美国培养下一代海洋观测人才的重要开放航次平台。'
                ),
                'source': 'UNOLS / 美国海洋研究船联盟',
                'url': 'https://www.unols.org/',
                'date': '2026-03-04',
            },
            {
                'title': '3. Schmidt Ocean Institute（活跃）：R/V Falkor(too)持续开放航次申请——ROV深潜数据全程开放共享',
                'badge': '[开放航次]',
                'abstract': (
                    'Schmidt Ocean Institute（SOI）运营的科考船R/V Falkor(too)持续开放航次申请，资助全球科学家登船开展海洋探索研究，所有航次数据（包括ROV高清影像、多波束测深、水柱声学数据等）均须在航次结束后完全开放共享至SOI数据门户。SOI官网（活跃）提供历次航次的完整数据归档和深潜视频记录开放访问，是全球深海开放探索和数据共享领域的标杆机构，航次涵盖深海生物多样性、地质构造和水下基础设施检查等多个方向。'
                ),
                'source': 'Schmidt Ocean Institute / R/V Falkor(too)',
                'url': 'https://schmidtocean.org/',
                'date': '2026-04-20',
            },
        ],
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '1. Copernicus Marine Service主页（2026-04-20当前）：免费开放海洋数据服务全球用户——政策、科研与蓝色经济三重支柱',
                'badge': '[更新]',
                'abstract': (
                    'Copernicus Marine Service（marine.copernicus.eu，2026-04-20持续更新）是欧盟资助的全球规模最大的业务化海洋数据开放服务平台，为政策制定、科学研究和蓝色经济应用提供免费、开放、系统性的海洋参考信息，产品覆盖物理海洋学（SST、SSH、流场）、生物地球化学（叶绿素、营养盐）和海冰，通过Web数据仓、Python API（motuclient/copernicusmarine）和OPeNDAP接口提供数据下载与实时访问，是欧洲DTO数据供给的核心节点。'
                ),
                'source': 'Copernicus Marine Service / 欧盟',
                'url': 'https://marine.copernicus.eu/',
                'date': '2026-04-20',
            },
            {
                'title': '2. NOAA NCEI（2026-04-20当前）：全球最大气候与海洋数据存档中心——持续提供WOD、Argo等核心数据集开放访问',
                'badge': '[更新]',
                'abstract': (
                    'NOAA国家环境信息中心（NCEI）是全球规模最大的气候与海洋观测数据存档机构，管理WOD（World Ocean Database）、GODAR（全球海洋数据存档恢复）、全球Argo GDAC镜像、热带气旋数据库等多个核心数据集，提供Web门户、WODselect检索系统、FTP批量下载和OPeNDAP接口等多种数据访问方式，是全球海洋气候研究的核心数据基础设施，近期WOD2023数据论文（Nature Scientific Data 2026-04-16）进一步提升了WOD数据集的引用规范性。'
                ),
                'source': 'NOAA NCEI / WOD / Argo GDAC',
                'url': 'https://www.ncei.noaa.gov/',
                'date': '2026-04-20',
            },
            {
                'title': '3. PANGAEA（活跃）：地球与环境科学数据出版平台——支持海洋观测数据FAIR出版与长期存档',
                'badge': '[平台]',
                'abstract': (
                    'PANGAEA（pangaea.de，由AWI和MARUM联合运营）是专注于地球与环境科学的国际权威数据出版平台，为Argo、WOCE、PIRATA、SEANOE等海洋观测计划提供数据集的DOI注册、元数据标准化（ISO 19115、Dublin Core）、长期存档和开放分发服务，遵循FAIR原则。平台近期公告（2026-04-07）提示5月社区培训研讨会开放注册，数据提交方可通过API或Web界面上传结构化数据集，PANGAEA是海洋观测数据FAIR出版的全球最重要平台之一。'
                ),
                'source': 'PANGAEA / AWI / MARUM',
                'url': 'https://pangaea.de/',
                'date': '2026-04-07',
            },
        ],
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '1. kval（GitHub/PyPI，Norwegian Polar Institute）：挪威极地研究所Python海洋数据处理工具集',
                'badge': '[工具]',
                'abstract': (
                    'kval（GitHub: NPIOcean/kval）是挪威极地研究所（NPI）海洋学组维护的Python海洋数据处理工具集，专为现场观测数据（CTD剖面、系泊数据、Glider数据等）的标准化处理与分析设计，提供数据读取、质控、插值、可视化和NetCDF输出等功能，支持CF Conventions格式规范，遵循极地海洋学典型数据处理流程，是南北极现场观测数据处理的实用开源工具参考，适合需要处理非Argo类型现场观测数据的研究团队。'
                ),
                'source': 'GitHub / Norwegian Polar Institute / kval',
                'url': 'https://github.com/NPIOcean/kval',
                'date': '2026-04-20',
            },
            {
                'title': '2. ODV（Ocean Data View）：AWI开发的海洋剖面数据交互探索与分析软件——持续更新',
                'badge': '[工具]',
                'abstract': (
                    'Ocean Data View（ODV，odv.awi.de，Alfred Wegener Institute开发维护）是海洋学界使用最广泛的桌面数据探索与可视化软件，支持剖面、时间序列、轨迹和序列等多类数据的交互分析与图形制作，能直接读取WOD、Argo、WOCE等主流海洋数据格式，内置温盐分析、散点图、断面图、地图投影等丰富功能，免费提供给科研和教育用途，是全球数万名海洋学家的日常数据分析工具，定期发布新版本修复BUG和增加功能。'
                ),
                'source': 'ODV / Alfred Wegener Institute / AWI',
                'url': 'https://odv.awi.de/',
                'date': '2026-04-20',
            },
            {
                'title': '3. OceanSpy（ReadTheDocs）：MIT海洋集群数字孪生接口Python库——专为海洋模型数据分析设计',
                'badge': '[工具]',
                'abstract': (
                    'OceanSpy（oceanspy.readthedocs.io）是由MIT等机构开发的开源Python工具包，专为海洋学家分析和可视化大规模海洋模型数据集设计，底层依托xarray和Dask实现并行计算，提供计算海洋热量输运、涡动能、流线等常用物理量的内置函数，同时支持数字孪生集群（如MITgcm大西洋高分辨率配置）的直接在线接入，是海洋数值模型输出数据标准化访问与分析的重要参考工具，适合数字孪生后处理分析场景。'
                ),
                'source': 'OceanSpy / MIT / ReadTheDocs',
                'url': 'https://oceanspy.readthedocs.io/en/latest/index.html',
                'date': '2026-04-20',
            },
            {
                'title': '4. Copernicus Marine Python API（copernicusmarine，PyPI）：一行命令下载CMEMS全球海洋数据',
                'badge': '[工具]',
                'abstract': (
                    'Copernicus Marine Service官方Python客户端库copernicusmarine（PyPI）支持通过简洁的Python API或命令行直接下载CMEMS全球海洋数据产品，覆盖数千个NetCDF变量和时间序列，支持空间子集、时间切片和变量筛选，无需注册即可访问全部免费开放数据，是目前访问CMEMS数据集最便捷的编程接口，被广泛用于海洋科研数据管道的自动化建设，结合xarray可无缝接入海洋数据分析工作流。'
                ),
                'source': 'Copernicus Marine Service / PyPI / copernicusmarine',
                'url': 'https://data.marine.copernicus.eu/',
                'date': '2026-04-20',
            },
        ],
    },
]


def tr(text, bold=False, link=None):
    element = {"text_run": {"content": text}}
    if bold:
        element["text_run"]["style"] = {"bold": True}
    if link:
        element["text_run"]["link"] = {"url": link}
    return element


def paragraph(elements):
    return {"block_type": 2, "text": {"elements": elements, "style": {}}}


def heading(text, level=1):
    prefix = {1: "\u3010", 2: "  >> "}.get(level, "    ")
    suffix = {1: "\u3011", 2: ""}.get(level, "")
    return paragraph([tr(prefix + text + suffix, bold=True)])


def divider():
    return paragraph([tr("\u2500" * 50)])


def item_block(num, title, badge, abstract, source, date, url):
    blocks = []
    badge_text = badge if badge else ""
    title_text = f"{badge_text} {title}" if badge_text else title
    blocks.append(paragraph([tr(f"  {num}. ", bold=True), tr(title_text, bold=True, link=url)]))
    blocks.append(paragraph([tr(abstract)]))
    meta_parts = []
    if source:
        meta_parts.append(f"来源：{source}")
    if date:
        meta_parts.append(f"日期：{date}")
    if url:
        meta_parts.append(f"链接：{url}")
    blocks.append(paragraph([tr(" | ".join(meta_parts), bold=False)]))
    blocks.append(divider())
    return blocks


def section_block(title, en_title, items):
    blocks = []
    blocks.append(heading(title, 1))
    blocks.append(paragraph([tr(en_title, bold=False)]))
    blocks.append(divider())
    for i, item in enumerate(items, 1):
        blocks.extend(item_block(
            i,
            item.get('title', ''),
            item.get('badge', ''),
            item.get('abstract', ''),
            item.get('source', ''),
            item.get('date', ''),
            item.get('url', '')
        ))
    return blocks


def build_blocks():
    blocks = []
    blocks.append(heading(f"海洋AI技术日报 · {datetime.now().strftime('%Y年%m月%d日')}", 1))
    blocks.append(divider())
    for section in SECTIONS:
        blocks.extend(section_block(
            section['title'],
            section.get('en', ''),
            section.get('items', [])
        ))
    return blocks


def create_document_and_write(tenant_access_token):
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    payload = {"title": f"海洋AI技术日报 {datetime.now().strftime('%Y-%m-%d')}"}
    headers = {
        "Authorization": f"Bearer {tenant_access_token}",
        "Content-Type": "application/json"
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    doc_id = resp.json()["data"]["document"]["document_id"]
    print(f"文档创建成功: {doc_id}")
    return doc_id


def write_blocks_to_doc(token, doc_id, blocks, max_retries=3):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"children": blocks, "index": 0}
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
            if resp.status_code == 200:
                print(f"成功写入 {len(blocks)} 个内容块")
                return
            elif resp.status_code == 429:
                print(f"遇到限流，等待 60 秒...")
                time.sleep(60)
            else:
                print(f"写入失败 (状态码: {resp.status_code}): {resp.text}")
                if attempt < max_retries - 1:
                    time.sleep(5)
        except Exception as e:
            print(f"写入异常: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
    print("文档写入失败")


def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["tenant_access_token"]


def main():
    print("开始推送飞书文档...")
    token = get_tenant_access_token()
    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)
    with open("feishu_doc_url.txt", "w") as f:
        f.write(f"https://wcn5jx0ifkx3.feishu.cn/docx/{doc_id}\n")
    print(f"文档地址已保存: feishu_doc_url.txt")


if __name__ == "__main__":
    main()
