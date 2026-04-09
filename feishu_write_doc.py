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
                'title': '1. arXiv:扩散概率模型从稀疏海面数据高分辨率重建三维海洋状态',
                'badge': '[论文]',
                'abstract': (
                    'arXiv于2026年4月3日发布预印本（arXiv:2604.02850），提出一种深度感知生成框架，基于条件去噪扩散概率模型（DDPM）从极度稀疏（99.9%缺失）的海面高度和温度观测中重建高分辨率三维海洋状态，且不依赖背景动力学模型。该框架引入连续深度嵌入，可将学习到的海洋状态表征泛化到未见过的深度层。以墨西哥湾为案例，模型成功重建了跨多深度的次表层温度、盐度和流速场，通过谱分析和热输送诊断验证了大尺度环流恢复能力。该工作确立了生成扩散模型作为数据受限场景下概率性海洋重建的可扩展范式，对气候监测和数值预报具有重要意义。'
                ),
                'source': 'arXiv / North Carolina State University',
                'date': '2026-04-03',
                'url': 'https://arxiv.org/abs/2604.02850'
            },
            {
                'title': '2. ScienceDirect:南海"神针"——AI驱动区域海洋预报基础模型的探索路径',
                'badge': '[论文]',
                'abstract': (
                    'Ocean Modelling于2026年4月1日在线发表"South China Sea \'神针(Trident)\' — Solution for Ocean Forecast Foundation Models"，深入分析了全球AI海洋预报模型在区域尺度的局限性，以南海为例提出区域AI海洋基础模型的实用化路径。研究揭示全球模型在热带浅海、强潮汐和季风驱动区域的系统性偏差，论证了专注区域模型不仅在科学上更有效，也是推进AI驱动海洋预报的更可行策略。为区域海洋数字孪生和智能预报系统提供理论依据。'
                ),
                'source': 'Ocean Modelling / ScienceDirect',
                'date': '2026-04-01',
                'url': 'https://www.sciencedirect.com/science/article/pii/S2666675826001116'
            },
            {
                'title': '3. Springer综述:AI赋能可持续蓝色生物技术——海洋资源可持续管理新范式',
                'badge': '[综述]',
                'abstract': (
                    'Springer Blue Biotechnology于2026年4月2日发表综述"Leveraging artificial intelligence (AI) techniques for sustainable marine resources management"，系统评述AI技术在海洋生物资源评估与可持续管理中的最新应用。研究覆盖深度学习在渔业资源监测、海洋生物多样性普查、生态系统模拟和气候变化适应性管理等场景的最新进展，为蓝色经济与海洋AI的交叉融合提供了全面的文献基础。'
                ),
                'source': 'Springer Blue Biotechnology',
                'date': '2026-04-02',
                'url': 'https://link.springer.com/article/10.1186/s44315-026-00054-0'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '1. DITTO峰会2026:JAMSTEC官方主页上线，注册开放——11月横滨湾旗舰大会',
                'badge': '[会议]',
                'abstract': (
                    'JAMSTEC（日本海洋研究开发机构）正式上线"DITTO International Summit 2026"官方会议主页，注册通道开放。本次峰会作为UN海洋十年认可的数字孪生海洋（DITTO）计划旗舰活动，将于2026年11月在日本横滨湾举行，重点议题包括：DTO共享框架与互操作协议、"假设情景"分析能力建设、服务于海洋保护与蓝色经济的实际应用案例，以及下一代海洋数字孪生基础设施。国际合作伙伴ANERIS等已同步推广。'
                ),
                'source': 'JAMSTEC / DITTO / UN Ocean Decade',
                'date': '2026-04(更新)',
                'url': 'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/'
            },
            {
                'title': '2. AGU JGR-Solid Earth:弱监督深度学习全球海山检测与形态表征',
                'badge': '[论文]',
                'abstract': (
                    'AGU JGR-Solid Earth于近日（5天前）在线发表"Global Detection and Morphological Characterization of Seamounts With Weakly Supervised Deep Learning"，提出整合重力和水深测量数据的弱监督深度学习框架，实现全球尺度海山的自动检测与形态特征提取。该框架解决了传统方法对大量标注数据的依赖，通过弱监督学习策略在有限标注条件下实现高精度海山识别，为海洋地形数字化建模、板块构造研究和深海生物多样性热点区定位提供技术支撑，与海洋数字孪生的底层地形数据建设高度相关。DOI: 10.1029/2025JH000848'
                ),
                'source': 'AGU / JGR-Solid Earth / Wiley',
                'date': '2026-04-04(在线)',
                'url': 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025JH000848'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '1. Nature Scientific Reports:YOLOv12融合CNN与Transformer编码器实现珊瑚形态自动检测',
                'badge': '[论文]',
                'abstract': (
                    'Nature Scientific Reports于2026年4月1日发表开放获取论文"Coral morphology detection in underwater imagery using YOLOv12 with CNN and transformer encoder fusion"，提出将YOLOv12目标检测框架与卷积神经网络（CNN）和Transformer编码器融合的方法，实现对水下图像中珊瑚形态的自动识别与分类。研究比较了多种深度学习模型在珊瑚形态检测任务上的性能，为珊瑚礁生态系统监测可视化分析提供高效工具。该方法可应用于大规模水下视频/图像数据集的自动标注与可视化，助力珊瑚礁数字孪生建设。'
                ),
                'source': 'Nature Scientific Reports',
                'date': '2026-04-01',
                'url': 'https://www.nature.com/articles/s41598-026-42591-z'
            },
            {
                'title': '2. Copernicus Marine Service:Jupyter学习环境更新——海洋数据交互可视化课程资源',
                'badge': '[工具]',
                'abstract': (
                    'Copernicus Marine Service于近日（3天前）更新其Jupyter学习环境，为用户提供最新的交互式海洋数据可视化教学资源，包括基于Python的海洋参数（SST、盐度、海冰、叶绿素）可视化Notebook、可复现的数据访问与分析流程，以及面向培训研讨会参与者的e-learning材料。该学习环境整合了copernicusmarine工具箱的最新API，支持用户通过JupyterLab直接连接CMEMS数据服务、实现交互式海洋状态可视化，是海洋数据可视化技能培训的核心平台。'
                ),
                'source': 'Copernicus Marine Service / CMEMS',
                'date': '2026-04-06(更新)',
                'url': 'https://marine.copernicus.eu/services/user-learning-services/jupyter-environment'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / Marine Data Quality Control',
        'items': [
            {
                'title': '1. IOOS QARTOD更新:实时海洋观测数据QC国际规范持续迭代（2026年4月）',
                'badge': '[标准]',
                'abstract': (
                    'NOAA IOOS于2026年4月更新QARTOD（Quality Assurance of Real-Time Oceanographic Data）系列手册，包含实时海洋数据质量控制标志使用手册和多类仪器（水位、浪高、海流、溶解氧等）的专项QC规程。QARTOD是当前国际上应用最广泛的实时海洋观测数据质量控制标准之一，通过多级QC标志（良好/可疑/坏数据/缺失）规范了自动化质量检查流程，为全球沿海观测网提供统一的数据质量基础设施。'
                ),
                'source': 'NOAA IOOS / QARTOD',
                'date': '2026-04(更新)',
                'url': 'https://ioos.noaa.gov/project/qartod/'
            },
            {
                'title': '2. ScienceDirect:机器学习在海洋数据同化中的应用进展综述（2026年2月）',
                'badge': '[综述]',
                'abstract': (
                    'ScienceDirect于2026年2月1日发表"Machine learning in ocean data assimilation: Advances, gaps and future perspectives"，系统综述2020-2025年机器学习在海洋数据同化中的最新进展，覆盖神经网络参数化、代理模型构建、误差协方差估计和观测算子学习等核心方向。综述重点分析了将ML集成到业务化海洋预报系统（如CMEMS、HYCOM）时的数据质量要求，指出观测数据的一致性QC是ML同化成功的先决条件，为数据质量控制技术与海洋预报系统的深度融合提供了方向指引。'
                ),
                'source': 'ScienceDirect / Ocean Modelling',
                'date': '2026-02-01',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Marine Data Processing',
        'items': [
            {
                'title': '1. Nature Scientific Reports:DTU海洋热动力综合数据集——多源融合逐日全球海洋要素产品',
                'badge': '[数据集]',
                'abstract': (
                    'Nature Scientific Reports近期报道多源融合逐日全球海洋要素数据集新进展，该类数据集整合卫星遥感与现场观测，涵盖海表温度（SST）、盐度（SSS）、混合层深度和海表高度等核心参数，经严格质控后提供高分辨率（1/8°~1/4°）时间序列产品。此类数据集由多个国际海洋数据处理中心（CMEMS、NOAA、ESA CCI）共同维护，是验证区域海洋模型和训练AI预报系统的核心数据基础。其处理流程涵盖多卫星轨道数据拼接、云层填补（OI/BG插值）和传感器间偏差订正等关键技术步骤。'
                ),
                'source': 'Copernicus Marine Service / CMEMS / ESA CCI',
                'date': '2026-04-07(更新)',
                'url': 'https://data.marine.copernicus.eu/product/MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013/description'
            },
            {
                'title': '2. MDPI:两阶段智能反演模型——卫星观测重建次表层温盐结构',
                'badge': '[论文]',
                'abstract': (
                    'Journal of Marine Science and Engineering于2026年4月发表"A Two-Stage Intelligent Inversion Model for Subsurface Ocean Temperature and Salinity"，提出利用卫星观测重建次表层温盐三维结构的两阶段深度学习反演框架。该方法突破了传统现场观测高成本、低时空覆盖的局限，融合海表参数与历史剖面数据，高效重建全球次表层温盐分布，为海洋环流分析、热盐输送研究和数值模式数据同化提供低成本替代方案。'
                ),
                'source': 'MDPI / Journal of Marine Science and Engineering',
                'date': '2026-04(在线)',
                'url': 'https://www.mdpi.com/2077-1312/14/7/677'
            },
            {
                'title': '3. GO-BGC全球海洋生物地球化学浮标阵列:2026年3月更新——400+在役BGC浮标',
                'badge': '[进展]',
                'abstract': (
                    'GO-BGC（Global Ocean Biogeochemistry Array）于2026年3月20日更新，持续扩展全球生物地球化学Argo浮标观测网络，目前全球活跃部署超过400个携带化学/生物传感器的BGC-Argo浮标，实时测量溶解氧、pH、硝酸盐、叶绿素、颗粒物和光辐照度六类参数。这一规模化观测网络产生的海量连续剖面数据，为碳循环量化、富营养化监测和气候模型验证提供了前所未有的数据基础，也是深度学习海洋处理算法的重要训练数据源。'
                ),
                'source': 'GO-BGC / PMEL NOAA',
                'date': '2026-03-20',
                'url': 'https://www.go-bgc.org/'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. OBIS数据集登陆AWS开放数据注册表（2026-04-02）:云端访问全球海洋生物多样性数据',
                'badge': '[平台]',
                'abstract': (
                    'OBIS（全球海洋生物多样性信息系统）于2026年4月2日在AWS开放数据注册表（registry.opendata.aws/obis）完成数据集注册，标志着其整合全球数百万条海洋物种出现记录的权威数据集正式进入云原生访问新阶段。研究者可通过AWS S3直接获取OBIS完整数据集，无需依赖API速率限制，极大提升大规模海洋生物多样性分析效率。该数据集收录来自全球各机构、历经2000年至今的海洋生物观测记录，覆盖分布地理坐标、物种分类、采集深度和环境参数，是训练海洋AI物种识别和生态预测模型的重要数据基础。'
                ),
                'source': 'OBIS / AWS Open Data Registry',
                'date': '2026-04-02',
                'url': 'https://registry.opendata.aws/obis/'
            },
            {
                'title': '2. PANGAEA全球海洋地球数据库:持续接收新数据集，支持"数据出版"与DOI引用',
                'badge': '[平台]',
                'abstract': (
                    'PANGAEA（海洋与陆地科学数据发布者）持续作为全球最重要的海洋地球科学数据开放存储库运行，接收并发布来自全球科考航次、Argo浮标、卫星遥感和实验室分析的原始与处理后数据。PANGAEA提供标准化数据引用DOI，支持数据版本控制和引用追踪，与主流学术期刊实施强制数据共享政策联动，是海洋数据FAIR原则落地的标杆平台。其数据发布服务与国际Argo、GO-SHIP、GEOTRACES等大型计划紧密整合。'
                ),
                'source': 'PANGAEA / AWI / MARUM',
                'date': '2026-04(持续更新)',
                'url': 'https://www.pangaea.de/'
            },
            {
                'title': '3. NSF FY2026 IOOS实施资助:4月13日截止——支持区域海洋观测系统互操作与数据共享',
                'badge': '[资助]',
                'abstract': (
                    'NOAA发布FY2026年度IOOS实施资助计划，申请截止日期为2026年4月13日，重点资助美国综合海洋观测系统（IOOS）11个区域协会的运营、数据共享服务和技术互操作能力建设。资助方向包括：区域海洋观测网络运维、ERDDAP/THREDDS数据服务升级、高频雷达和实时浮标数据标准化，以及与CMEMS、Argo等国际系统的数据互操作对接，为沿海海洋数据中心提供重要资金支持。'
                ),
                'source': 'NOAA IOOS / Grantable',
                'date': '2026-04-13(截止)',
                'url': 'https://grantable.co/grants/fy-2026-implementation-of-the-u-s-integrated-ocean-observing-system-ioos-4448efb7741b'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. 今日速报:中国第42次南极考察队"雪龙"号历时160天凯旋上海（2026-04-09）',
                'badge': '[要闻]',
                'abstract': (
                    '2026年4月9日，由自然资源部组织的中国第42次南极考察队暨"雪龙"号极地考察破冰船顺利返回上海并停靠中国极地考察国内基地码头。本次考察自2025年11月1日出发，历时160天，总航程约3.4万余海里，在人员规模、物资量和任务量上均创下新高，各项科考任务顺利完成。"雪龙2"号目前仍在南极普里兹湾执行"秋季南大洋生态系统"联合航次，预计5月下旬返回。本次南极科考积累了大量极地海洋观测数据，将为南极海洋生态系统变化、海冰动态及南大洋碳循环研究提供宝贵数据支撑。'
                ),
                'source': '央视新闻 / 中新网 / 新华网',
                'date': '2026-04-09',
                'url': 'https://news.cctv.com/2026/04/09/ARTIOuVpPxEe9MNQnxf9ZRGk260409.shtml'
            },
            {
                'title': '2. One Ocean Week 2026(4月18-24日):卑尔根海洋开放科学周——科考船Statsraad Lehmkuhl回港',
                'badge': '[活动]',
                'abstract': (
                    '2026年One Ocean Week将于4月18-24日在挪威卑尔根举行，标志性亮点是完成12个月全球航行的帆船科考船Statsraad Lehmkuhl将于活动开幕日（4月18日）驶入卑尔根港。本届活动议程已上线，涵盖海洋数字孪生、数据开放共享、蓝色经济和海洋气候适应等核心专题，卑尔根大学（UiB）组织多场免费公开活动。此活动为参与国际海洋开放科学合作、建立开放航次数据共享联系的重要窗口。'
                ),
                'source': 'One Ocean Week / UiB / UN Ocean Prediction',
                'date': '2026-04-18(即将)',
                'url': 'https://oneoceanweek.no/en/program/'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Marine Data Centers',
        'items': [
            {
                'title': '1. NOAA IOOS 4月简报:太平洋西北低成本溶氧传感器部署——实时数据向渔业开放',
                'badge': '[新动态]',
                'abstract': (
                    'NOAA IOOS于2026年4月4日发布"Eyes on the Ocean"双周简报，报道当前技术转化（OTT）项目在太平洋西北地区的蟹笼上部署低成本溶解氧传感器，为渔民提供近实时海洋溶氧状况数据，帮助规避贫氧区风险。此举是IOOS将实时海洋数据直接赋能渔业生产决策的典型案例，体现了海洋数据中心从科研服务向社会应用延伸的战略方向，也是低成本海洋传感器网络与数据共享基础设施结合的创新实践。'
                ),
                'source': 'NOAA IOOS / Eyes on the Ocean Newsletter',
                'date': '2026-04-04',
                'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-april-2026/'
            },
            {
                'title': '2. 中科院海洋科学大数据中心(MSDC):数据资源持续扩充，4月1日最新更新',
                'badge': '[更新]',
                'abstract': (
                    '中科院海洋科学大数据中心（MSDC）于2026年4月1日发布最新数据资源更新，持续汇聚中科院海洋研究所科考船队获取的多源西太平洋实测数据，涵盖海洋水文、化学、生物和地质等多学科数据集。MSDC数据门户提供数据可视化、AI分析工具集和在线下载服务，支持全球生物多样性数据和全球观测数据的统一管理与共享。数据DOI/CSTR引用规范的完善推动了数据资产的标准化管理与引用追踪。'
                ),
                'source': '中科院海洋科学大数据中心 / MSDC',
                'date': '2026-04-01',
                'url': 'http://msdc.qdio.ac.cn/'
            },
            {
                'title': '3. Copernicus数据空间生态系统（CDSE）:3月底更新，提供哨兵卫星数据即时开放访问',
                'badge': '[平台]',
                'abstract': (
                    'Copernicus数据空间生态系统（CDSE）于2026年3月31日完成新一轮更新，持续提供对哨兵系列卫星海洋观测数据（Sentinel-3 SST/海冰/海色、Sentinel-1/2海洋SAR）的即时免费开放访问。CDSE作为欧洲哨兵数据的核心分发平台，每天提供超过20TB的新数据，配备交互式浏览器、JupyterHub分析环境和REST API，全面支持海洋遥感数据处理流水线建设，是CMEMS等海洋数据中心的重要上游数据来源。'
                ),
                'source': 'Copernicus Data Space Ecosystem / ESA',
                'date': '2026-03-31',
                'url': 'https://dataspace.copernicus.eu/'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources / Ocean Tools & Software',
        'items': [
            {
                'title': '1. xoa 2026.2.1发布:基于xarray的专业海洋分析库持续迭代',
                'badge': '[工具]',
                'abstract': (
                    'xoa（xarray-based ocean analysis library）于2026年3月3日发布2026.2.1版本，专为处理观测和模式海洋数据设计，深度整合xarray生态系统。xoa提供海洋特有的坐标变换（如sigma坐标到深度）、海洋插值方法（双线性、垂向插值）和标准化绘图工具，与CROCO、NEMO等区域海洋模式输出兼容，是Python海洋数据后处理的重要专业工具库，文档齐全且活跃维护。'
                ),
                'source': 'xoa / Read the Docs / PyPI',
                'date': '2026-03-03',
                'url': 'https://xoa.readthedocs.io/'
            },
            {
                'title': '2. OceanographyWithPython:海洋数据分析Python开源教程仓库持续更新',
                'badge': '[开源]',
                'abstract': (
                    'GitHub上的"OceanographyWithPython"教程仓库（LijoDXL维护）于5天前更新，作为面向海洋科学家的Python数据分析实践教程集，提供从数据读取、可视化到统计分析的完整教学链路，涵盖xarray、cartopy、matplotlib、scipy等核心工具的海洋应用实例。该仓库适合海洋学研究生入门级学习，也是构建海洋AI数据预处理流水线的参考资源，已积累活跃的用户社区。'
                ),
                'source': 'GitHub / OceanographyWithPython',
                'date': '2026-04-04(更新)',
                'url': 'https://github.com/LijoDXL/OceanographyWithPython'
            },
            {
                'title': '3. Norwegian Polar Institute kval:极地海洋数据处理Python工具包',
                'badge': '[开源]',
                'abstract': (
                    'Norwegian Polar Institute（NPI）海洋学组开发的"kval"工具包（GitHub: NPIOcean/kval）提供针对极地海洋观测数据处理与分析的专业Python工具集，覆盖CTD数据QC、时间序列处理、剖面可视化和标准化输出功能。kval专为南极和北极海洋学数据工作流设计，采用xarray/pandas数据模型，并提供符合CF-conventions的NetCDF输出，是极地海洋AI训练数据预处理的重要工具，代码开源且附完整使用文档。'
                ),
                'source': 'GitHub / Norwegian Polar Institute',
                'date': '2026-04(活跃)',
                'url': 'https://github.com/NPIOcean/kval'
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
