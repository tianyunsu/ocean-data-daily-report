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

yesterday_cn = (datetime.now() - timedelta(days=1)).strftime('%Y\u5e74%m\u6708%d\u65e5')
today_date = (datetime.now()).strftime('%Y-%m-%d')

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. Springer专刊社论:数据科学与AI驱动海洋科学与蓝色经济',
                'badge': '[专刊]',
                'abstract': (
                    'Springer International Journal of Data Science and Analytics于2026年3月14日发表社论"Editorial: data science and AI for marine science and the blue economy"，正式推出"Data Science and AI for Marine Science and the Blue Economy"特刊合集。社论指出，数据科学与AI的融合为海洋过程监测、建模和预测开辟了新机遇，涵盖从卫星遥感到现场观测的全链条智能海洋数据分析方案，是近7天国际海洋AI领域的重要学术出版动态。'
                ),
                'source': 'Springer / IJDSA',
                'date': '2026-03-14',
                'url': 'https://link.springer.com/article/10.1007/s41060-026-01082-0'
            },
            {
                'title': '2. OCEANS 2026三亚会议摘要征集:深海技术、海洋能源与海洋AI三大主题',
                'badge': '[会议]',
                'abstract': (
                    'IEEE OCEANS 2026 Sanya会议（2026年5月25-28日，中国三亚）正式开放摘要征集，聚焦Deep-sea Technology、Marine Energy和Ocean AI三大核心主题。该会议由IEEE海洋工程学会（OES）主办，征集深海探测技术与应用、深海采矿与环境评估、海洋可再生能源、移动水下传感器网络等领域的前沿技术报告，摘要征集截止日期临近，是近期国际海洋AI与深海技术领域最重要的学术交流平台之一。'
                ),
                'source': 'IEEE OES / OCEANS 2026 Sanya',
                'date': '2026-03(征集中)',
                'url': 'https://sanya26.oceansconference.org/call-for-abstracts/'
            },
            {
                'title': '3. 求是海洋学术论坛:西湖大学范迪夏主讲"未来水下智能机器人畅想"',
                'badge': '[学术]',
                'abstract': (
                    '浙江大学求是海洋学术论坛2026年第4期（总99期）于4月2日发布预告，邀请西湖大学范迪夏研究员于4月3日在舟山校区作题为"在海洋中翱翔：未来水下智能机器人畅想"的报告。报告探讨海洋生物仿生学如何启发新一代水下机器人的设计理念，范迪夏团队此前曾成功研制世界首例仿生型潜水器"西谷I号"并下潜至海底2000米，该报告对海洋AI与智能机器人交叉研究方向具有重要参考价值。'
                ),
                'source': '浙江大学海洋学院 / 西湖大学',
                'date': '2026-04-02(预告)',
                'url': 'http://oc.zju.edu.cn/2026/0402/c29860a3147412/page.htm'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '1. DITTO"海洋十年"项目:推动全球海洋数字孪生标准化与治理能力建设',
                'badge': '[项目]',
                'abstract': (
                    '联合国"海洋十年"DITTO（Digital Twins of the Ocean）项目持续推进全球海洋数字孪生（DTO）标准化与能力建设。DITTO旨在通过数字孪生技术支持海洋保护和蓝色经济可持续发展，推动建立数字孪生海洋的通用理解与最佳实践。项目整合地球观测、建模和数字基础设施，为各成员国提供预测未来海洋发展的数字化能力，是当前全球海洋数字孪生治理的核心协调平台。'
                ),
                'source': 'DITTO / IOC-UNESCO 海洋十年',
                'date': '2026持续推进',
                'url': 'https://ditto-oceandecade.org/'
            },
            {
                'title': '2. 欧盟海洋数字孪生市场展望:2025年达5.9亿美元，2032年预计24亿美元',
                'badge': '[市场]',
                'abstract': (
                    'MarketsandMarkets最新报告显示，海洋数字孪生市场2025年估值约5.9亿美元，预计到2032年将增长至24亿美元，2026-2032年复合年增长率达23.2%。该市场快速增长的主要驱动力包括海上风电、自主船舶、深海采矿等蓝色经济产业对数字化运营管理需求的爆发式增长。报告指出，AI与物联网技术的深度融合正加速海洋数字孪生从概念验证向规模化部署转变。'
                ),
                'source': 'MarketsandMarkets',
                'date': '2026(最新报告)',
                'url': 'https://www.marketsandmarkets.com/Market-Reports/digital-twin-in-marine-market-213848743.html'
            },
            {
                'title': '3. Iliad项目:整合地球观测与建模构建海洋数字孪生虚拟表示',
                'badge': '[项目]',
                'abstract': (
                    '欧盟Iliad（Integrating data from earth observation, modelling and digital infrastructure for Digital Twins of the Ocean）项目于2025年7月发布最新进展，致力于构建整合地球观测、建模和数字基础设施的海洋数字孪生虚拟表示。Iliad作为欧盟"恢复我们的海洋和水域"使命的重要组成部分，为海洋过程预测和未来发展趋势分析提供综合数字平台，与EDITO平台协同推进欧洲数字孪生海洋生态建设。'
                ),
                'source': 'Iliad / EU Horizon Europe',
                'date': '2025-07(持续更新)',
                'url': 'https://ocean-twin.eu/'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '1. Taylor&Francis论文:基于协作传输函数的海洋流场与温盐场交互可视化',
                'badge': '[论文]',
                'abstract': (
                    'Taylor & Francis Journal of Spatial Information Science于2026年2月9日发表论文"Interactive visualization of ocean flow and thermohaline field based on collaborative transfer function"，由田丰霖、陈戈等学者完成。研究针对海洋现象中标量场（温盐）与矢量场（海流）相互作用的可视化难题，提出基于协作传输函数的交互式可视化方法，实现了多维度海洋数据的协同探索分析，对海洋环流过程和能量物质输运的科学理解具有重要价值。'
                ),
                'source': 'Taylor & Francis / JOSIS',
                'date': '2026-02-09',
                'url': 'https://www.tandfonline.com/doi/full/10.1080/17538947.2026.2624176'
            },
            {
                'title': '2. CIESM Workshop Monograph No.53:地中海高分辨率海洋数据3D映射与可视化',
                'badge': '[专刊]',
                'abstract': (
                    '地中海海洋科学委员会（CIESM）于2026年2月发布Workshop Monograph No.53"An ocean of gradients: towards a 3D mapping and visualization of high-resolution marine data"，将地中海视为由温度、盐度、营养盐、溶解氧和微生物活动塑造的动态3D马赛克。该专刊汇集多国海洋科学家最新成果，探索利用先进可视化技术呈现海洋高分辨率多参数梯度场，为区域海洋科学可视化提供了系统性方法参考。'
                ),
                'source': 'CIESM',
                'date': '2026-02',
                'url': 'https://ciesm.org/an-ocean-of-gradients-towards-a-3d-mapping-and-visualization-of-high-resolution-marine-data-ciesm-workshop-monograph-n53/'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / Marine Data Quality Control',
        'items': [
            {
                'title': '1. NOAA IOOS发布QARTOD新论文:实时海洋数据质控标准体系最新进展',
                'badge': '[标准]',
                'abstract': (
                    '美国综合海洋观测系统（IOOS）于2026年3月底发布QARTOD项目新论文，作为U.S. IOOS数据管理与网络基础设施（DMAC）核心服务的最新成果。QARTOD手册于2026年3月7日在OceanBestPractices知识库获最新更新引用，涵盖温盐、海流、波浪、海平面等多要素实时数据的标准化自动质控算法，持续为全球海洋观测站网数据质控认证提供核心规范。'
                ),
                'source': 'NOAA IOOS / OceanBestPractices',
                'date': '2026-03(最新)',
                'url': 'https://ioos.noaa.gov/project/qartod/'
            },
            {
                'title': '2. Springer主动学习海洋数据质量评估:Argo/GLOSS/EMSO数据质控新方法',
                'badge': '[论文]',
                'abstract': (
                    'Springer于2025年4月发表"Leveraging active learning for ocean data quality assessment"论文，针对Argo、GLOSS（全球海平面观测系统）、EMSO（欧洲多学科海底观测系统）等大规模海洋数据质量评估挑战，提出基于主动学习的质控方法。该方法通过智能选择最有信息量的样本进行标注，有效缓解了海洋数据中标注样本有限和数据集不均衡的问题，为大规模海洋观测数据质量评估提供了高效的机器学习方案。'
                ),
                'source': 'Springer',
                'date': '2025-04-08',
                'url': 'https://link.springer.com/article/10.1007/s41060-025-00751-w'
            },
            {
                'title': '3. JOSS开源框架:海洋学数据质量控制通用框架',
                'badge': '[工具]',
                'abstract': (
                    'Journal of Open Source Software（JOSS）发表海洋学数据质量控制通用框架论文，提供可扩展的Python质控工具。海洋环境数据采集中虚假测量不可避免，数据集质量高度依赖于质控流程。该开源框架实现了从异常值检测到自动化质控决策的完整流水线，支持多种海洋观测数据类型的灵活适配，是当前海洋数据质控开源工具领域的重要贡献。'
                ),
                'source': 'JOSS',
                'date': '持续维护',
                'url': 'https://joss.theoj.org/papers/10.21105/joss.02063.pdf'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Marine Data Processing',
        'items': [
            {
                'title': '1. Ocean Modelling综述:机器学习在海洋数据同化中的进展、差距与业务化之路',
                'badge': '[综述]',
                'abstract': (
                    'Elsevier Ocean Modelling于2026年2月1日发表重要综述"Machine learning in ocean data assimilation: Advances, gaps and the road to operations"（DOI: 10.1016/j.ocemod.2026.102678），由David Grande和Giuseppe Buizza撰写。综述系统审查了2020-2025年间机器学习在海洋数据同化领域的研究进展，识别新兴趋势、反复出现的挑战以及走向业务化的关键路径，指出物理约束与深度学习融合、不确定性量化是未来核心方向。'
                ),
                'source': 'Ocean Modelling / Elsevier',
                'date': '2026-02-01',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028'
            },
            {
                'title': '2. Ocean Modelling:深度学习潜空间数据同化生成海洋未见非线性演化',
                'badge': '[论文]',
                'abstract': (
                    'Elsevier Ocean Modelling于2026年2月1日发表"Generating unseen nonlinear evolution in the ocean using deep learning-based latent space data assimilation model"，由郑庆宇等学者完成。研究提出基于深度学习潜空间的数据同化模型，能够从有限观测中重建海洋非线性演化过程中的缺失信息。传统方法通常对非线性物理模型或观测算子进行线性化，该研究突破此限制，为海洋与大气非线性状态估计提供了新范式。'
                ),
                'source': 'Ocean Modelling / Elsevier',
                'date': '2026-02-01',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000016'
            },
            {
                'title': '3. Global Fishing Watch 2026研究路线图:AI与卫星驱动海洋透明度',
                'badge': '[报告]',
                'abstract': (
                    'Global Fishing Watch于2026年3月底发布"A Research Roadmap: How AI and Satellites Will Drive Transparency in 2026"研究路线图，系统阐述了AI与卫星技术在海洋活动监测中的最新进展。报告亮点包括：每日处理约200万平方公里海洋数据、检测小型渔船活动、部署AI智能体监测海洋保护区等。该组织持续推进海洋活动透明度建设，利用近实时可视化数据支持科学研究和政策制定。'
                ),
                'source': 'Global Fishing Watch',
                'date': '2026-03-28',
                'url': 'https://globalfishingwatch.org/article/a-research-roadmap-how-ai-and-satellites-will-drive-transparency-in-2026/'
            },
            {
                'title': '4. 中科院院刊:海洋数据再分析现状及展望',
                'badge': '[综述]',
                'abstract': (
                    '《中国科学院院刊》2026年第1期发表刘传玉（中科院海洋研究所）综述"海洋数据再分析现状及展望"，系统阐述了海洋数据再分析（ODR）技术——通过将海洋观测资料与海洋环流模式相结合，产出更高时空覆盖度的格点数据。文章梳理了全球主要再分析产品的发展历程和技术路线，分析了当前面临的观测偏差校正、多源数据融合等关键挑战，并展望了AI辅助再分析的未来发展方向。'
                ),
                'source': '中国科学院院刊',
                'date': '2026-01-11',
                'url': 'http://old2022.bulletin.cas.cn/publish_article/2026/1/20260111.htm'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. UNESCO正式发布《IOC海洋数据与信息管理战略计划》PDF文档',
                'badge': '[战略]',
                'abstract': (
                    'UNESCO于2026年3月底在官方文档库正式发布《IOC Strategic Plan for Ocean Data and Information Management》PDF文件（编号PF/0000385113），为IOC/IODE海洋数据与信息系统（ODIS）和ODIScat在线数据目录的未来发展提供战略指导。该战略文件强调在实施过程中需考虑ODIS系统的最新发展，推动开放数据、FAIR原则和互操作性数字生态系统的全面落实，是全球海洋数据治理的权威指导文件。'
                ),
                'source': 'UNESCO / IOC IODE',
                'date': '2026-03(最新发布)',
                'url': 'https://unesdoc.unesco.org/ark:/48223/pf0000385113'
            },
            {
                'title': '2. IOC/OTGA/VLIZ 2026年度海洋数据管理在线培训课程开放注册',
                'badge': '[培训]',
                'abstract': (
                    'IOC海洋培训与援助门户（OTGA）联合VLIZ（比利时海洋研究所）于2026年2月6日启动全年海洋数据管理在线培训课程（Ocean Data Management 2026），面向全球海洋数据管理从业者开放参与。课程内容涵盖开放数据、FAIR数据原则应用、海洋数据发布与引用流程等核心主题，是IOC推进全球海洋数据管理能力建设的旗舰培训项目。'
                ),
                'source': 'IOC/OTGA/VLIZ / OceanExpert',
                'date': '2026-02-06(全年开放)',
                'url': 'https://oceanexpert.org/event/4953'
            },
            {
                'title': '3. IOCARIBE海洋数据管理自定进度培训课程持续开放',
                'badge': '[培训]',
                'abstract': (
                    'IOC-UNESCO IOCARIBE于2026年3月19日更新海洋数据管理自定进度在线培训课程，提供全面的海洋数据管理入门培训，涵盖数据管理指导原则和典型工作流程。课程描述了开放获取（Open Access）、开放数据（Open Data）和FAIR数据的术语体系，并指导如何将其应用于海洋数据管理的实践，面向全球海洋从业者免费开放。'
                ),
                'source': 'IOC-UNESCO / IOCARIBE',
                'date': '2026-03-19(更新)',
                'url': 'https://iocaribe.ioc-unesco.org/en/event/725'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. POGO Ocean Training Partnership更新船载培训项目信息',
                'badge': '[培训]',
                'abstract': (
                    '全球海洋观测合作计划（POGO）Ocean Training Partnership（OTP）于2026年3月底更新船载培训项目页面。OTP作为国际海洋科学组织联盟，持续协调多艘科考船的随船培训体验。2026年NF-POGO船载培训研究员项目（3月24日开放申请）提供2026年至2027年初的多航次培训机会，面向发展中国家年轻海洋科学家开放，是推动全球海洋科考能力建设的核心机制。'
                ),
                'source': 'POGO / Ocean Training Partnership',
                'date': '2026-03-29(更新)',
                'url': 'https://pogo-ocean.org/capacity-development/shipboard-training/'
            },
            {
                'title': '2. 中科院海洋所2026年度科考船船时开放申请通知(第三轮)',
                'badge': '[通知]',
                'abstract': (
                    '中国科学院重大科技基础设施共享服务平台于2026年2月发布中科院海洋研究所2026年度科学考察船船时开放申请通知（第三轮），旨在响应国家海洋科学考察研究需求，进一步提升科考船运行船时的开放共享效率。该通知通过中科院LSSF平台发布，面向全国科研机构开放申请，是中国科学院系统内最重要的科考船时共享机制之一。'
                ),
                'source': '中科院LSSF / 中科院海洋所',
                'date': '2026-02(第三轮)',
                'url': 'https://lssf.cas.cn/sszs/gykj/hykxzhkcc/gg/'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Marine Data Centers',
        'items': [
            {
                'title': '1. NOAA WOD持续更新:全球最大海洋剖面数据集保持活跃',
                'badge': '[数据中心]',
                'abstract': (
                    'NOAA国家环境信息中心（NCEI）世界海洋数据库（WOD）于2026年4月1日完成最新更新，持续作为全球最大统一格式、质量控制、公开可用的海洋剖面数据集合。WOD整合了全球数千个数据贡献机构的历史观测记录，覆盖温度、盐度、溶解氧等多要素，为气候研究、海洋模型验证和数据处理方法学开发提供标准数据基础。NSF海洋数据与样本库页面同步更新NCEI相关数据访问信息。'
                ),
                'source': 'NOAA NCEI / NSF',
                'date': '2026-04-01(更新)',
                'url': 'https://www.ncei.noaa.gov/products/world-ocean-database'
            },
            {
                'title': '2. Copernicus Marine In Situ TAC:现场数据质量管控与分发服务更新',
                'badge': '[数据中心]',
                'abstract': (
                    'Copernicus Marine In Situ TAC（现场数据主题组装中心）于2026年3月26日完成最新更新，持续确保多源、多平台、异构海洋现场数据的一致性质控和统一格式分发。INSTAC仪表板实时监控全球海洋现场数据质量状态，提供近实时（NRT）数据产品，平均在数据采集后24-48小时内完成质控并分发，是Copernicus Marine Service数据供应链中的关键质量保障环节。'
                ),
                'source': 'Copernicus Marine In Situ TAC / INSTAC',
                'date': '2026-03-26(更新)',
                'url': 'https://marineinsitu.eu/'
            },
            {
                'title': '3. NASA GISS地表温度分析数据2026年3月重新组织发布',
                'badge': '[数据中心]',
                'abstract': (
                    'NASA GISS地表温度分析（GISS Surface Temperature Analysis, GISTEMP）于2026年3月11日重新组织了数据下载页面，将原先附加在页面底部的数据下载链接迁移至独立页面。此次更新改善了用户数据获取体验，GISTEMP作为全球地表温度变化的权威参考数据集，其数据页面优化对气候变化研究和海洋-大气耦合分析具有重要影响。'
                ),
                'source': 'NASA GISS',
                'date': '2026-03-11',
                'url': 'https://data.giss.nasa.gov/gistemp/'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources / Ocean Tools & Software',
        'items': [
            {
                'title': '1. PyOceans SEA-PY:2026年3月更新Python海洋工具协作目录',
                'badge': '[工具]',
                'abstract': (
                    'PyOceans社区于2026年3月23日更新SEA-PY（Sea-Python）协作目录，系统整理了面向海洋科学社区的Python工具生态。该目录覆盖从基础Python到专业海洋分析库（xarray、dask、Cartopy、OceanSpy等）的完整工具链，是PyOceans社区推动海洋科学Python工具标准化和可发现性的核心项目，为海洋科研人员选择合适的Python工具提供了权威参考。'
                ),
                'source': 'PyOceans / GitHub Pages',
                'date': '2026-03-23(更新)',
                'url': 'https://pyoceans.github.io/sea-py/'
            },
            {
                'title': '2. OceanHackWeek MHW项目:基于Xarray+Dask的多维海洋热浪检测器',
                'badge': '[GitHub]',
                'abstract': (
                    'OceanHackWeek社区在GitHub维护的MHW（Marine Heatwave）检测项目于2026年3月底持续活跃更新。该项目应用Hobday等（2016）标准海洋热浪定义，利用Xarray和Dask实现高性能并行计算，支持多维海洋数据矩阵的海洋热浪自动检测。项目代码开源，提供Jupyter Notebook示例，适合海洋气候变化研究人员快速部署海洋热浪分析流水线。'
                ),
                'source': 'GitHub / OceanHackWeek',
                'date': '2026-03(活跃)',
                'url': 'https://github.com/oceanhackweek/ohw20-proj-marine-heat-waves'
            },
            {
                'title': '3. OceanSpy 0.3.6:海洋模型数据交互分析与可视化Python包',
                'badge': '[工具]',
                'abstract': (
                    'OceanSpy是一个开源用户友好的Python包，用于海洋模型数据集的分析和可视化，基于xarray构建。最新版本0.3.6.dev6于2024年1月发布，持续维护中。OceanSpy提供海洋模型数据切片、剖面提取、体积输运计算等专业功能，支持MITgcm、POP、ROMS等主流海洋模型输出格式，已安装dask和xgcm等依赖以优化大规模数据处理性能，是海洋模型后处理分析的重要开源工具。'
                ),
                'source': 'OceanSpy / ReadTheDocs',
                'date': '持续维护',
                'url': 'https://oceanspy.readthedocs.io/en/latest/index.html'
            },
        ]
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


def build_all_blocks():
    blocks = []
    blocks.append(paragraph([tr(
        f"\u62a5\u544a\u65e5\u671f\uff1a{yesterday_cn}    "
        "\u6765\u6e90\uff1aarXiv / ScienceDirect / \u4e2d\u79d1\u9662 / IOC-UNESCO / \u817e\u8baf\u65b0\u95fb\u7b49    "
        "\u81ea\u52a8\u751f\u6210"
    )]))
    blocks.append(divider())
    blocks.append(paragraph([tr("")]))

    for sec in SECTIONS:
        blocks.append(heading(sec["title"], level=1))
        blocks.append(paragraph([tr(sec["en"])]))
        blocks.append(paragraph([tr("")]))

        for item in sec["items"]:
            title_full = (item["badge"] + " " + item["title"]) if item.get("badge") else item["title"]
            blocks.append(heading(title_full, level=2))
            blocks.append(paragraph([tr("\u6458\u8981\uff1a", bold=True), tr(item["abstract"])]))
            blocks.append(paragraph([
                tr("\u6765\u6e90\uff1a", bold=True), tr(item["source"]),
                tr("    \u53d1\u5e03\u65f6\u95f4\uff1a", bold=True), tr(item["date"]),
                tr("    \u539f\u6587\u94fe\u63a5\uff1a", bold=True),
                tr(item["url"], link=item["url"])
            ]))
            blocks.append(paragraph([tr("")]))

        blocks.append(divider())
        blocks.append(paragraph([tr("")]))

    blocks.append(paragraph([tr(
        "\u672c\u7b80\u62a5\u6bcf\u65e5\u81ea\u52a8\u751f\u6210\uff0c\u4ec5\u4f9b\u5b66\u672f\u53c2\u8003\u3002\u7248\u6743\u5f52\u539f\u4f5c\u8005/\u673a\u6784\u6240\u6709\u3002"
    )]))
    return blocks


# ── 主流程 ────────────────────────────────────────────────────
def get_token():
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
    )
    if r.status_code != 200:
        raise Exception(f"获取token失败: {r.text}")
    return r.json()["tenant_access_token"]


def create_doc(token):
    r = requests.post(
        "https://open.feishu.cn/open-apis/docx/v1/documents",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": f"\u6d77\u6d0b\u7814\u7a76\u65e5\u62a5_{today_date}"},
        timeout=15
    )
    if r.status_code != 200:
        raise Exception(f"\u521b\u5efa\u6587\u6863\u5931\u8d25: {r.text}")
    data = r.json()["data"]
    return data["document"]["document_id"], data["document"]["title"]


def write_blocks(token, doc_id, blocks):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    # Split into batches of 50 to avoid payload limits
    batch_size = 50
    for i in range(0, len(blocks), batch_size):
        batch = blocks[i:i + batch_size]
        payload = {"children": batch, "index": -1}
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        if r.status_code != 200:
            raise Exception(f"\u5199\u5165\u5757\u5931\u8d25 (batch {i//batch_size}): {r.text}")
        time.sleep(0.3)
    return True


def main():
    token = get_token()
    print("[INFO] token ok")
    doc_id, title = create_doc(token)
    print(f"[INFO] \u6587\u6863\u5df2\u521b\u5efa: {title} (id={doc_id})")
    blocks = build_all_blocks()
    write_blocks(token, doc_id, blocks)
    print(f"[OK] \u5df2\u5199\u5165 {len(blocks)} \u4e2a\u5757")
    doc_url = f"https://{TENANT_DOMAIN}/docx/{doc_id}"
    with open("feishu_doc_url.txt", "w", encoding="utf-8") as f:
        f.write(doc_url)
    print(f"[OK] \u6587\u6863URL: {doc_url}")


if __name__ == "__main__":
    main()
