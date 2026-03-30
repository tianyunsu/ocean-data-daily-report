#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 feishu_write_doc.py 中的 SECTIONS 数据
日期：2026-03-26
"""

import re

NEW_SECTIONS_CODE = '''SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                "title": "1. 中科院南海所发布「海境AI大模型」：区域海洋环境应用多任务大模型",
                "badge": "[新发]",
                "abstract": (
                    "2026年1月20日，中国科学院南海海洋研究所正式发布海境·区域海洋环境应用AI大模型（海境AI大模型）。"
                    "该模型由中科院战略性先导科技专项资助，热带海洋环境与岛礁生态全国重点实验室牵头，"
                    "联合多家科研机构共同研制。海境AI大模型针对南海及热带海洋区域，整合温、盐、流、浪"
                    "等多变量海洋环境要素的智能预测能力，为区域海洋精细化预报和岛礁生态保护提供AI技术支撑。"
                ),
                "source": "中科院南海海洋研究所 / 科学网",
                "date": "2026-01-20",
                "url": "https://news.sciencenet.cn/htmlnews/2026/1/559236.shtm"
            },
            {
                "title": "2. 南科大SPEED项目：AI赋能深海环境模拟与预测，获批联合国「海洋十年」官方行动",
                "badge": "[重磅]",
                "abstract": (
                    "2026年3月18日报道，南方科技大学海洋高等研究院SPEED项目正式获批为联合国「海洋十年」官方行动，"
                    "成为深圳首个深海领域AI赋能的海洋十年项目，也是DITTO（数字孪生海洋）大科学计划的核心项目之一。"
                    "该项目联合中英德新加坡等多国科研力量，利用AI技术对深海环境进行全球高精度模拟与预测，"
                    "旨在通过数字孪生框架支撑海洋可持续发展决策。"
                ),
                "source": "南方科技大学 / Ocean Decade",
                "date": "2026-03-18",
                "url": "https://newshub.sustech.edu.cn/html/202603/47357.html"
            },
            {
                "title": "3. EGU26大会征集摘要：Copernicus Marine与欧洲数字孪生海洋联合议题（2026年5月）",
                "badge": "[会议]",
                "abstract": (
                    "2026年欧洲地球科学联合会大会（EGU26）将于5月3-8日在维也纳举行（含线上），"
                    "Copernicus Marine Service 与 EDITO 联合举办专题会议 OS4.8——"
                    "\"Copernicus Marine Service and the European Digital Twin of the Ocean\"，"
                    "征集涵盖海洋数据处理、AI应用、数字孪生技术、数据访问等研究方向的摘要投稿，"
                    "是当前欧洲海洋科技领域最重要的年度学术交流平台。"
                ),
                "source": "Copernicus Marine / EGU26",
                "date": "2026-01-08 公告",
                "url": "https://marine.copernicus.eu/news/call-abstracts-copernicus-marine-and-eu-dto-session-egu-2026"
            },
            {
                "title": "4. IEEE：深度学习海洋预报综合综述——数据驱动模型的方法与挑战",
                "badge": "[综述]",
                "abstract": (
                    "发表于 IEEE Transactions on Geoscience and Remote Sensing（2025年4月），"
                    "论文\"Deep Learning for Ocean Forecasting: A Comprehensive Review\"系统梳理了"
                    "数据驱动深度学习在全球和区域海洋预报中的应用进展，涵盖CNN、RNN、Transformer等模型架构，"
                    "分析了当前面临的稀疏观测数据、时空泛化、物理一致性等核心挑战，"
                    "是进入海洋AI领域的必读综述。"
                ),
                "source": "IEEE TGRS",
                "date": "2025-04-01",
                "url": "https://ieeexplore.ieee.org/document/10947107"
            },
            {
                "title": "5. AI海洋数据同化论文资源库 GitHub 持续更新：收录最新研究成果",
                "badge": "[工具]",
                "abstract": (
                    "GitHub 项目 AcWiz/ai-data-assimilation-papers 于5天前更新，"
                    "整理收录了来自 arXiv、顶级期刊和会议的 AI/深度学习 + 海洋数据同化与预报领域最新论文清单，"
                    "涵盖ScienceDirect 2026年2月最新综述《Machine learning in ocean data assimilation: Advances, gaps and prospects》等重要成果，"
                    "是跟踪该领域研究前沿的重要开放资源。"
                ),
                "source": "GitHub / AcWiz",
                "date": "2026-03-21（近期更新）",
                "url": "https://github.com/AcWiz/ai-data-assimilation-papers"
            }
        ]
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                "title": "1. EDITO-2 项目启动（2025-2028）：欧洲数字孪生海洋平台进入第二阶段",
                "badge": "[重磅]",
                "abstract": (
                    "EU Horizon 资助的 EDITO 2（European Digital Twin Ocean Phase 2）项目正式立项，"
                    "建设周期2025—2028年，目标是扩大 EDITO 平台基础设施规模、壮大用户社区。"
                    "第一阶段（2022-2025）已完成核心数字孪生基础设施建设；第二阶段将着力提升平台互操作性、"
                    "可扩展性和跨境数据共享能力，与 Copernicus Marine Service 深度融合，"
                    "打造欧盟级别的海洋数字孪生服务生态。"
                ),
                "source": "CORDIS / EDITO 2 项目",
                "date": "2025-08-01 立项",
                "url": "https://cordis.europa.eu/project/id/101227771"
            },
            {
                "title": "2. EGU26摘要：海岸数字孪生——观测-模拟一体化框架强化海岸带数字孪生建设",
                "badge": "[论文]",
                "abstract": (
                    "EGU26大会摘要 EGU26-18326 提出一套综合观测-模拟框架，"
                    "通过将 Copernicus Marine 产品与海岸带高分辨率模型融合，"
                    "显著增强欧洲数字孪生海洋（DTO）的海岸带组成部分能力。"
                    "该框架实现了海岸带 in-situ 观测数据、卫星遥感数据与数值模型的一体化融合，"
                    "是当前将数字孪生延伸到近岸复杂环境的代表性技术路线。"
                ),
                "source": "EGU26 / Copernicus",
                "date": "2026年5月大会（摘要已发布）",
                "url": "https://meetingorganizer.copernicus.org/EGU26/EGU26-18326.html"
            },
            {
                "title": "3. DITTO峰会2026日本（JAMSTEC 主办）：全球最大数字孪生海洋旗舰会议",
                "badge": "[会议]",
                "abstract": (
                    "联合国「海洋十年」支持的 DITTO（Digital Twins of the Ocean）计划"
                    "将于2026年在日本举办旗舰活动 DITTO Summit，由日本海洋研究开发机构（JAMSTEC）主办。"
                    "继2022年伦敦峰会、2023年厦门峰会及2026年1月线上会议之后，"
                    "本届日本峰会汇聚全球数字孪生海洋专家，共同讨论技术标准、跨平台互操作与应用案例，"
                    "是推动全球数字孪生海洋协同发展的核心平台。"
                ),
                "source": "JAMSTEC / DITTO / Ocean Decade",
                "date": "2026年（确认，具体日期待公布）",
                "url": "https://w3.jamstec.go.jp/j/pr-event/ditto_summit2026/"
            },
            {
                "title": "4. EGU25 EDITO 进展报告：欧洲数字孪生海洋的新发展与互补性分析",
                "badge": "[报告]",
                "abstract": (
                    "6天前发布于 Copernicus EGU25 摘要，题为\"New developments and complementarity between European Digital Twin Ocean initiatives\"，"
                    "回顾了欧盟 EDITO 自2022年布雷斯特峰会启动以来的基础设施建设进展，"
                    "分析了 EDITO、EMODnet、Copernicus Marine 等多个欧洲数字孪生倡议之间的协同与互补关系，"
                    "为下一阶段跨平台融合提供了路线图参考。"
                ),
                "source": "Copernicus / EGU25",
                "date": "2026-03-20（近期）",
                "url": "https://meetingorganizer.copernicus.org/EGU25/EGU25-12286.html"
            }
        ]
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                "title": "1. Copernicus Marine MyOcean Pro Viewer：免费4D海洋可视化工具持续活跃更新",
                "badge": "[工具]",
                "abstract": (
                    "Copernicus Marine Service 的 MyOcean Pro Viewer 于2天前再次更新，"
                    "提供无需专业工具即可动态可视化海洋数据的能力，支持温度、盐度、洋流、海浪、海冰等"
                    "多个物理/生化参数的4D交互可视化。该工具免费开放，覆盖全球任意区域，"
                    "是当前业务化海洋可视化的标杆平台，最新更新强化了时序动画和数据下载联动功能。"
                ),
                "source": "Copernicus Marine / MyOcean Pro",
                "date": "2026-03-24（近期更新）",
                "url": "https://data.marine.copernicus.eu/viewer"
            },
            {
                "title": "2. Taylor&Francis IJGIS：海洋流场涡旋交互可视化新方法——面向中尺度涡运动模式",
                "badge": "[论文]",
                "abstract": (
                    "发表于 International Journal of Geographical Information Science（2025年1月），"
                    "论文\"Interactive visualization of ocean flow field for mesoscale vortex analysis\"提出新型交互式可视化方案，"
                    "能有效揭示中尺度涡（Mesoscale Eddy）的运动模式，支持动态追踪涡旋演化过程。"
                    "该方法融合流线、粒子追踪与彩色编码技术，在海洋涡旋可视化精度与交互性上均有显著突破，"
                    "对海洋环流研究和渔业资源预测具有重要应用价值。"
                ),
                "source": "IJGIS / Taylor & Francis",
                "date": "2025-01-02",
                "url": "https://www.tandfonline.com/doi/full/10.1080/17538947.2024.2440445"
            },
            {
                "title": "3. NASA Earthdata：全球海洋主题数据可视化目录持续更新，近期发布多个卫星产品",
                "badge": "[数据]",
                "abstract": (
                    "NASA Earthdata 于3月9日更新海洋主题数据页面，涵盖海洋环流、海洋颜色、海冰、"
                    "海面温度等多个子领域数据产品的可视化与下载服务。"
                    "近期新增 Sentinel-3B OLCI Level-2 区域遥感海洋颜色全分辨率数据（2天前刷新），"
                    "同步更新了海洋颜色 Level 3/4 浏览器（3天前），为海洋初级生产力、叶绿素等"
                    "生化参数可视化分析提供了高质量数据支撑。"
                ),
                "source": "NASA Earthdata",
                "date": "2026-03-09（近期更新）",
                "url": "https://www.earthdata.nasa.gov/topics/ocean"
            },
            {
                "title": "4. ResearchGate：多变量海洋数据探索与分析交互可视化工具",
                "badge": "[工具]",
                "abstract": (
                    "发表于 Indonesian Journal of Electrical Engineering and Computer Science（2024年11月），"
                    "论文\"An interactive visualization tool for the exploration and analysis of multivariate ocean data\""
                    "提出一款支持温度、盐度、溶解氧、叶绿素等多变量联合展示的交互可视化工具，"
                    "支持剖面图、时序图、散点图等多视图联动，适用于海洋现场观测数据的快速探索分析，"
                    "为科研人员提供了低门槛的多维海洋数据可视化解决方案。"
                ),
                "source": "IJEECS / ResearchGate",
                "date": "2024-11",
                "url": "https://www.researchgate.net/publication/385457240_An_interactive_visualization_tool_for_the_exploration_and_analysis_of_multivariate_ocean_data"
            }
        ]
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality / QA/QC",
        "items": [
            {
                "title": "1. Springer：ODEAL——基于主动学习的海洋数据质量评估异常检测框架",
                "badge": "[论文]",
                "abstract": (
                    "发表于 Data Mining and Knowledge Discovery（Springer，2025年4月），"
                    "论文\"Leveraging active learning for ocean data quality assessment\"提出 ODEAL 框架，"
                    "通过主动学习策略解决海洋观测数据标注样本稀少、类别不平衡的核心挑战。"
                    "该方法在 Argo、GLOSS、EMSO 等浮标/潮位站数据集上展现出优异的异常检测能力，"
                    "能以极少标注样本获得高精度质控结果，为智能海洋数据质控提供了新思路。"
                ),
                "source": "Springer / DMKD",
                "date": "2025-04-08",
                "url": "https://link.springer.com/article/10.1007/s41060-025-00751-w"
            },
            {
                "title": "2. arXiv预印本：ODEAL海洋异常检测——机器学习解决标注数据不足与类别不均衡",
                "badge": "[预印本]",
                "abstract": (
                    "arXiv 预印本（2312.10817）\"Ocean Data Quality Assessment through Outlier Detection with Active Learning\""
                    "面向 Argo 剖面浮标数据提出基于主动学习的离群点检测方案，"
                    "解决现有机器学习方法因标注数据有限和数据集不平衡导致精度不足的问题。"
                    "论文提供了完整的实验方案和开源代码，在全球多个海区的 Argo 数据集上进行了验证，"
                    "为自动化海洋数据质量控制提供了可复现的基准方法。"
                ),
                "source": "arXiv:2312.10817",
                "date": "2023-12-18（持续引用）",
                "url": "https://arxiv.org/abs/2312.10817"
            },
            {
                "title": "3. ScienceDirect：机器学习方法自动化质控海洋学数据——精度超越传统方法",
                "badge": "[论文]",
                "abstract": (
                    "发表于 Computers & Geosciences（Elsevier，2021年10月），"
                    "论文\"A machine learning approach to quality control oceanographic data\""
                    "提出基于异常检测的机器学习自动 QC 方法，通过学习\"好数据\"的行为特征识别异常样本，"
                    "显著降低传统方法的假阳性率。该方法已在全球多个海洋观测网络的历史数据上验证，"
                    "是当前海洋数据质控ML方法领域被引用最广泛的基础性工作之一。"
                ),
                "source": "Computers & Geosciences / Elsevier",
                "date": "2021-10",
                "url": "https://www.sciencedirect.com/science/article/pii/S0098300421001035"
            },
            {
                "title": "4. autoQC：基于AI的在线海洋数据质量控制应用——北极盐度数据实证",
                "badge": "[工具]",
                "abstract": (
                    "ResearchGate 收录的工具论文\"autoQC: An AI based online app for ocean data quality control\""
                    "介绍了一个基于机器学习的在线质控应用程序。"
                    "该工具使用 UDASH（北极和亚北极水文数据统一数据库）北极盐度数据训练，"
                    "可对上传的海洋剖面数据进行快速自动质控，并提供置信度评分。"
                    "对无专业质控团队的科研机构和个人研究者尤其具有实用价值。"
                ),
                "source": "ResearchGate / autoQC",
                "date": "2024-06",
                "url": "https://www.researchgate.net/publication/385740799_autoQC_An_AI_based_online_app_for_ocean_data_quality_control"
            }
        ]
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                "title": "1. Ocean Modelling（Elsevier）：海洋数据同化中的机器学习——进展、差距与展望（最新综述）",
                "badge": "[综述]",
                "abstract": (
                    "发表于 Ocean Modelling（Elsevier，2026年2月），"
                    "论文\"Machine learning in ocean data assimilation: Advances, gaps and prospects\""
                    "系统综述了2020—2025年间机器学习在海洋数据同化领域的应用进展，"
                    "覆盖背景误差协方差估计、观测算子优化、集合卡尔曼滤波增强等核心方向，"
                    "梳理了当前存在的差距（可解释性、实时性、物理约束等）并展望未来发展路径，"
                    "是进入该领域的权威参考综述。"
                ),
                "source": "Ocean Modelling / Elsevier",
                "date": "2026-02-01",
                "url": "https://www.sciencedirect.com/science/article/pii/S1463500326000028"
            },
            {
                "title": "2. Nature Machine Intelligence：DeepDA——偏卷积生成深度学习全球海洋数据同化系统",
                "badge": "[论文]",
                "abstract": (
                    "发表于 Nature Machine Intelligence（2024年7月），"
                    "论文\"Partial-convolution-implemented generative adversarial network for global oceanic data assimilation\"提出 DeepDA，"
                    "通过引入偏卷积神经网络与生成对抗网络，构建了可处理任意分布稀疏观测的全球海洋状态估计系统。"
                    "DeepDA 在重构海洋三维温盐流场方面达到国际领先水平，"
                    "将传统数值同化系统的计算成本降低至原来的 1/100，具有强大的业务化应用前景。"
                ),
                "source": "Nature Machine Intelligence",
                "date": "2024-07-22",
                "url": "https://www.nature.com/articles/s42256-024-00867-x"
            },
            {
                "title": "3. arXiv：高效可扩展AI海洋状态估计——应对全球规模计算挑战",
                "badge": "[预印本]",
                "abstract": (
                    "arXiv 预印本（2511.06041）\"Advancing Ocean State Estimation with efficient and scalable AI\""
                    "发表于2025年11月，提出面向全球海洋状态估计的高效可扩展AI方法，"
                    "解决当前大规模计算和复杂观测数据融合两大瓶颈。"
                    "方法在计算效率和精度上均有显著提升，为未来业务化全球海洋再分析系统提供了重要技术路线参考。"
                ),
                "source": "arXiv:2511.06041",
                "date": "2025-11-08",
                "url": "https://arxiv.org/abs/2511.06041"
            },
            {
                "title": "4. AGU JGR-Oceans：深度学习重建热带太平洋上层海洋——超越线性逆模型",
                "badge": "[论文]",
                "abstract": (
                    "发表于 JGR-Oceans（AGU，2024年11月），"
                    "论文\"Reconstructing the Tropical Pacific Upper Ocean with Deep Learning\""
                    "构建深度学习（DL）模型对热带太平洋上层海洋状态进行重建，"
                    "预测技巧在热带太平洋上显著优于传统线性逆模型。"
                    "通过将数据同化与DL结合，在海面观测稀疏区域实现高精度三维温盐场重建，"
                    "为厄尔尼诺/拉尼娜预报提供了新的技术手段。"
                ),
                "source": "JGR-Oceans / AGU",
                "date": "2024-11-21",
                "url": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024MS004422"
            }
        ]
    },
    {
        "title": "六、海洋数据管理与共享服务",
        "en": "Ocean Data Management & Sharing Services",
        "items": [
            {
                "title": "1. IOC-UNESCO：《海洋数据与信息管理战略规划（2023-2029）》持续推进",
                "badge": "[政策]",
                "abstract": (
                    "IOC-UNESCO《海洋数据与信息管理战略规划》（2023-2029）于2026年3月18-19日再次更新发布，"
                    "明确愿景：建立综合一体化的海洋数据与信息系统，满足IOC成员国多元化需求。"
                    "规划强调通过IODE协调全球超过100个国家海洋数据中心（NODC）网络，"
                    "推动数据标准化、开放获取和跨境共享，是当前全球海洋数据治理的核心政策文件。"
                ),
                "source": "IOC-UNESCO / IODE",
                "date": "2026-03-18（近期更新）",
                "url": "https://iode.org/ioc-strategic-plan-for-ocean-data-and-information-management/"
            },
            {
                "title": "2. Copernicus Marine Service：2026年3月产品路线图更新——多个关键产品升级上线",
                "badge": "[更新]",
                "abstract": (
                    "Copernicus Marine Service（CMEMS）2026年3月产品路线图发布多项重要变更："
                    "① 新增 Sentinel-1C L3 NRT 风场数据集（波罗的海/北极/大西洋）；"
                    "② insitu_glo_phy_ts_oa_my 全球温盐客观分析再处理产品完成全面更新，"
                    "引入改进的一阶猜想方法并将基准气候态从WOA18升级至WOA23；"
                    "③ METOP-A ASCAT 风场历史数据集按计划退役（Mar 2026）；"
                    "④ 全球及大西洋海洋颜色Level 3/4产品完成质量改进升级。"
                ),
                "source": "Copernicus Marine / CMEMS",
                "date": "2026-03月执行",
                "url": "https://marine.copernicus.eu/user-corner/product-roadmap/transition-information"
            },
            {
                "title": "3. IOC数据信息中心：全球超过100个国家海洋数据中心网络——3天前页面更新",
                "badge": "[平台]",
                "abstract": (
                    "IOC-UNESCO 海洋数据信息（Data and Information）专题页面于3天前再次更新，"
                    "展示了 IODE 协调的全球海洋数据中心网络最新状态，"
                    "涵盖100余个国家海洋数据中心（NODCs）、关联数据单元（ADUs）的分布与功能。"
                    "网络整合了实时、延时和历史海洋观测数据，"
                    "为 OceanData.Earth、SeaDataNet、Argo 等全球海洋数据服务提供基础协调与标准支撑。"
                ),
                "source": "IOC-UNESCO / ioc.unesco.org",
                "date": "2026-03-23（近期）",
                "url": "https://www.ioc.unesco.org/en/data-information"
            },
            {
                "title": "4. UNESCO第三届国际海洋数据会议：面向"我们想要的海洋"的数据需求",
                "badge": "[会议]",
                "abstract": (
                    "2025年2月，UNESCO 报道了第三届国际海洋数据会议（IODC-3）成果，"
                    "主题为\"The Data We Need for the Ocean We Want\"，"
                    "每两年由 IODE 委员会会议主办，汇集全球海洋数据管理专家回顾进展、"
                    "评估活动提案，确定下一周期数据共享优先事项。"
                    "会议聚焦公平数据获取、可持续数据基础设施建设和全球海洋观测系统互联互通。"
                ),
                "source": "UNESCO / IODE",
                "date": "2025-02-13",
                "url": "https://www.unesco.org/en/articles/data-we-need-ocean-we-want-third-international-ocean-data-conference"
            },
            {
                "title": "5. Copernicus数据空间生态系统：免费开放获取哨兵卫星数据的统一入口平台",
                "badge": "[平台]",
                "abstract": (
                    "Copernicus 数据空间生态系统（CDSE）于3月9日更新，"
                    "提供哥白尼哨兵系列卫星任务及其他任务的数据免费即时获取服务。"
                    "平台于2024年全面升级后，在3天前再次更新数据探索与可视化功能，"
                    "支持搜索、可视化和下载海洋相关遥感数据，"
                    "是连接欧洲海洋遥感数据与 EDITO 数字孪生平台的核心数据入口。"
                ),
                "source": "Copernicus CDSE / dataspace.copernicus.eu",
                "date": "2026-03-09（近期更新）",
                "url": "https://dataspace.copernicus.eu/"
            }
        ]
    },
    {
        "title": "七、开放航次 / 船时共享",
        "en": "Open Cruises / Ship Time Sharing",
        "items": [
            {
                "title": "1. 「深蓝百万里」环球科考太平洋航段：2026年3月28日从深圳启航（确认）",
                "badge": "[重磅]",
                "abstract": (
                    "「深蓝百万里」环球海洋科考（联合国海洋十年官方行动）太平洋航段"
                    "将于2026年3月28日从深圳蛇口码头正式启航，由「向阳红10号」执行，航期至7月5日。"
                    "本航段将前往菲律宾海盆、翁通爪哇海底高原、汤加海沟等全球深海前沿研究区，"
                    "中科院南海所-南科大海高院联合国际科考团队共同参与，"
                    "重点开展深海地球与生命协同演化等领域研究，"
                    "是国内近年规模最大的共享开放国际深海科考航次之一。"
                ),
                "source": "新浪财经 / 搜狐 / 都市新闻",
                "date": "2026-03-10报道，3月28日启航",
                "url": "https://finance.sina.com.cn/jjxw/2026-03-10/doc-inhqnmhw0182252.shtml"
            },
            {
                "title": "2. NSFC 2026年度共享航次项目指南：已发布，可登录系统申请",
                "badge": "[政策]",
                "abstract": (
                    "国家自然科学基金委员会（NSFC）2026年度国家自然科学基金重大研究计划共享航次项目指南已正式发布，"
                    "支持以共享方式开展海洋科学多学科综合考察，"
                    "符合条件的科研人员可登录 NSFC 信息系统提交申请。"
                    "共享航次计划持续开放中国科考船船时资源，推动多学科协同、国际合作科考，"
                    "是国内主要的开放船时申请渠道之一。"
                ),
                "source": "国家自然科学基金委员会",
                "date": "2026年度（近期发布）",
                "url": "https://www.nsfc.gov.cn/publish/portal0/tab442/"
            },
            {
                "title": "3. GO-SHIP：全球水文和气候学研究重复断面航次数据共享（CCHDO 持续维护）",
                "badge": "[数据]",
                "abstract": (
                    "GO-SHIP（Global Ocean Ship-based Hydrographic Investigations Program）"
                    "与 CCHDO（CLIVAR & Carbon Hydrographic Data Office）持续维护全球重复断面航次数据，"
                    "提供高精度温盐化学剖面观测的开放下载服务。"
                    "GO-SHIP 数据是全球海洋热盐结构变化、深层水团追踪和碳循环研究的核心数据源，"
                    "航次计划和历史数据集可通过 CCHDO 门户统一获取。"
                ),
                "source": "GO-SHIP / CCHDO",
                "date": "持续维护",
                "url": "https://cchdo.ucsd.edu/"
            },
            {
                "title": "4. EGU26 OS2.4/OS2.5 议题：海岸韧性与海洋观测系统——联合国海洋十年框架下的航次与观测",
                "badge": "[会议]",
                "abstract": (
                    "EGU26 大会设有 OS2.4 和 OS2.5 两个专题会议，"
                    "分别聚焦海岸韧性提升和海洋观测系统推进，在联合国海洋十年框架下"
                    "征集融合现场观测（包括科考航次）、遥感与模型的前沿研究摘要。"
                    "会议特别关注如何通过多源观测数据融合增强数字孪生海洋的观测支撑能力，"
                    "是推动开放科考航次数据价值挖掘的重要学术平台。"
                ),
                "source": "EGU26 / UNIBO",
                "date": "2026年5月（EGU26大会）",
                "url": "https://centri.unibo.it/dcc-cr/en/news/call-for-abstracts-egu26-sessions-os2-5-and-os2-4-on-coastal-resilience-and-ocean-observations"
            }
        ]
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers / Data Archives / Data Repository",
        "items": [
            {
                "title": "1. AWS Registry：Argo GDAC 数据集开放云端访问——1天前刷新",
                "badge": "[数据]",
                "abstract": (
                    "AWS Open Data Registry 上的 Argo GDAC（全球数据汇集中心）数据集于1天前更新，"
                    "提供全球 Argo 浮标海洋剖面数据及元数据的 S3 直接访问。"
                    "当前全球超过4000个 Argo 浮标在运行，每年新增约15万个剖面，"
                    "数据以 NetCDF 格式分组存放，涵盖灰色浮标（Grey Floats）质控信息表，"
                    "支持云原生大规模海洋数据分析工作流。"
                ),
                "source": "AWS Registry / Argo GDAC",
                "date": "2026-03-25（1天前更新）",
                "url": "https://registry.opendata.aws/argo-gdac-marinedata/"
            },
            {
                "title": "2. NOAA NCEI：全球 Argo 数据存档库——定期更新浮标剖面与元数据",
                "badge": "[数据]",
                "abstract": (
                    "NOAA NCEI（National Centers for Environmental Information）维护的全球 Argo 数据存档库"
                    "于2025年12月4日更新，提供按浮标编号分组的剖面、元数据和技术信息文件的标准化归档服务。"
                    "NCEI 是 Argo 数据的官方美国国家级存档中心，与法国 Coriolis GDAC 构成"
                    "全球 Argo 数据的两大主镜像节点，确保数据长期保存和可靠访问。"
                ),
                "source": "NOAA NCEI",
                "date": "2025-12-04（最新存档更新）",
                "url": "https://www.ncei.noaa.gov/products/global-argo-data-repository"
            },
            {
                "title": "3. Copernicus World Heritage Hub：文化遗产监测数据平台（Copernicus生态扩展）",
                "badge": "[新发]",
                "abstract": (
                    "2026年3月18日，Copernicus 发布 World Heritage Hub，"
                    "作为专用数据平台支持利用 Copernicus 数据监测、保护全球文化与自然遗产（含海洋遗址）。"
                    "该平台是 Copernicus 数据生态向文化遗产保护延伸的重要举措，"
                    "体现了地球观测数据中心服务范畴的持续扩展——从传统气象海洋领域延伸至文化遗产治理。"
                ),
                "source": "Copernicus",
                "date": "2026-03-18",
                "url": "https://www.copernicus.eu/en"
            },
            {
                "title": "4. China Argo 实时数据中心：中国自主北斗Argo浮标数据服务",
                "badge": "[平台]",
                "abstract": (
                    "中国 Argo 实时数据中心（CARDC）于2015年建立基于北斗卫星系统的中国剖面浮标服务，"
                    "为国内外用户提供中国自主研发 Argo 浮标的实时剖面数据。"
                    "CARDC 是全球 Argo 数据体系的重要组成部分，"
                    "承担中国 Argo 浮标数据的采集、处理、质控与共享，"
                    "积极参与国际 Argo 项目的数据管理与标准制定。"
                ),
                "source": "China Argo Real-time Data Center",
                "date": "持续运行",
                "url": "https://www.argo.org.cn/"
            }
        ]
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources (GitHub etc.)",
        "items": [
            {
                "title": "1. pyAOS：大气与海洋科学 Python 包目录——持续收录活跃开发包",
                "badge": "[工具]",
                "abstract": (
                    "PyAOS（Python for Atmosphere and Ocean Science）社区维护的 Python 包目录"
                    "持续收录大气和海洋科学领域的专用 Python 库，涵盖可视化（Cartopy、Cmocean）、"
                    "数据读取（xarray、netCDF4、cfgrib）、物理计算（gsw、seapy）、"
                    "机器学习（TorchGeo）等各类工具，并持续通过 GitHub 接受社区更新提交，"
                    "是了解海洋科学 Python 工具生态的权威参考索引。"
                ),
                "source": "PyAOS / GitHub",
                "date": "2025-05（最近索引更新）",
                "url": "https://pyaos.github.io/packages/"
            },
            {
                "title": "2. CloudDrift：NSF EarthCube 资助的拉格朗日数据云端分析 Python 包",
                "badge": "[工具]",
                "abstract": (
                    "CloudDrift 是专为大气、海洋和气候科学拉格朗日数据（如 Argo 浮标、漂流浮标、"
                    "动物追踪轨迹）设计的 Python 包，由 NSF EarthCube 资助。"
                    "最新文档显示（2025年9月15日），CloudDrift 要求 Python ≥ 3.10，"
                    "依赖 awkward-array 实现不规则时序数据高效处理，支持云存储（S3/GCS）直接读取，"
                    "是当前海洋拉格朗日数据处理的最佳实践工具之一。"
                ),
                "source": "CloudDrift / GitHub / PyPI",
                "date": "2025-09（文档更新）",
                "url": "https://github.com/Cloud-Drift/clouddrift"
            },
            {
                "title": "3. xarray-EOPF：ESA EOPF Zarr 格式 xarray 后端——哨兵卫星数据云端分析新接口",
                "badge": "[新发]",
                "abstract": (
                    "ESA EOPF 数据产品的 xarray 后端扩展（xarray-eopf）正式发布，"
                    "支持以 Zarr 格式读取 ESA Earth Observation Processing Framework 卫星数据产品，"
                    "包括哨兵系列卫星的 SAR、光学和海洋颜色数据。"
                    "该工具无缝融入 xarray/dask 云计算生态，"
                    "为大规模海洋遥感数据的云端处理和可视化提供了标准化接口，"
                    "是推动海洋遥感数据云原生分析的重要技术突破。"
                ),
                "source": "ESA EOPF / Copernicus / zarr.eopf.copernicus.eu",
                "date": "2026近期发布",
                "url": "https://zarr.eopf.copernicus.eu/data-and-tools/"
            },
            {
                "title": "4. AI数据同化论文 GitHub 资源库：5天前更新，紧跟最新研究进展",
                "badge": "[工具]",
                "abstract": (
                    "GitHub 项目 AcWiz/ai-data-assimilation-papers 于5天前（2026-03-21）更新，"
                    "系统整理了 AI/深度学习 + 海洋数据同化与预报领域的论文清单（含英文 README），"
                    "涵盖 arXiv 预印本、顶级期刊和会议最新研究成果，"
                    "包括 2026年2月 Ocean Modelling 最新综述等前沿内容，"
                    "是追踪该领域动态、搜寻开源代码的高效入口。"
                ),
                "source": "GitHub / AcWiz",
                "date": "2026-03-21（5天前更新）",
                "url": "https://github.com/AcWiz/ai-data-assimilation-papers/blob/master/README_en.md"
            },
            {
                "title": "5. LibHunt 海洋学开源项目 Top 6：iris、VIAME、PlanktoScope、clouddrift 等",
                "badge": "[工具]",
                "abstract": (
                    "LibHunt 整理发布了海洋学领域最佳开源项目 Top 6，包括："
                    "① iris（MetOffice，NetCDF/GRIB数据分析）；"
                    "② VIAME（海洋视觉分析与识别）；"
                    "③ PlanktoScope（开源浮游生物成像仪）；"
                    "④ clouddrift（拉格朗日数据分析）；"
                    "⑤ pyobis（OBIS海洋生物多样性数据访问）；"
                    "⑥ pasaules-skati（海洋卫星图像处理）。"
                    "该列表是了解海洋学开源生态全貌的快速参考指南。"
                ),
                "source": "LibHunt / libhunt.com",
                "date": "持续维护",
                "url": "https://www.libhunt.com/topic/oceanography"
            }
        ]
    }
]
'''

# 读取原文件
with open("feishu_write_doc.py", "r", encoding="utf-8") as f:
    content = f.read()

# 找到 SECTIONS = [ 的位置（从第19行开始）
start_marker = "SECTIONS = ["
end_marker = "]\n\n\n"

start_idx = content.find(start_marker)
# 找到 SECTIONS 结束的位置：最后一个 ] 后跟两个换行
end_idx = content.find(end_marker, start_idx)
end_idx += len(end_marker)

if start_idx == -1:
    print("ERROR: SECTIONS start marker not found!")
    exit(1)

new_content = content[:start_idx] + NEW_SECTIONS_CODE + "\n\n" + content[end_idx:]

with open("feishu_write_doc.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SECTIONS 更新成功！")

# 验证
import ast
with open("feishu_write_doc.py", "r", encoding="utf-8") as f:
    src = f.read()
try:
    tree = ast.parse(src)
    print("Python语法验证：通过 ✅")
except SyntaxError as e:
    print(f"Python语法错误：{e}")
