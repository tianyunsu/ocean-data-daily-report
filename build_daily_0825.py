# -*- coding: utf-8 -*-
"""
build_daily_0825.py — 将 2026-08-25 日报 SECTIONS 写入 feishu_write_doc.py
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': '"盘古"海洋智能预报大模型工程化落地：海洋预报从"天级"到"分钟级"（CCTV, 2026-08-13）',
                'badge': '[要闻]',
                'abstract': '全国首个深度融合AI技术、全栈国产算力支撑的"盘古"海洋智能预报大模型实现工程化落地，将海洋预报频次从"天级"颠覆性提升至"分钟级"。该模型基于华为昇腾算力与MindSpore框架，已接入自然资源部第一海洋研究所业务预报系统，每天固定时间点输出预报结果，支撑远洋船舶航线决策。同期，Ocean AI海洋时空智能大模型、海境AI大模型、海洋数字孪生引擎DTO Engine 2.0相继发布，攻克通用大模型落地海洋场景的"水土不服"问题，覆盖海洋生态保护、海洋牧场、海上风电等多场景应用。',
                'source': '央视网 / 海洋CCTV',
                'url': 'https://ocean.cctv.com/2026/08/13/ARTIPg7BMSzEiN429IM7JB5e260813.shtml',
                'date': '2026-08-13',
            },
            {
                'title': 'WaveGraph：图神经网络地中海十年波浪重建（arXiv, 2026-08-17）',
                'badge': '[论文]',
                'abstract': '意大利CMCC基金会与博洛尼亚大学团队提出 WaveGraph——基于图神经网络（GNN）的盆地尺度波浪动力学仿真模型。该模型直接在非结构化网格上运行（沿岸分辨率达2-3 km），采用多尺度架构结合非结构化模型网格与均匀图，同时表征局部海岸相互作用与大尺度波浪动力学。模型自回归运行17年无需重新初始化或产生漂移，对浮标和卫星观测验证显示其技巧与输入数据集相当，风强迫驱动长期稳定性而波浪历史改善涌浪驱动动力学，为光谱波浪模型的高效稳定仿真器提供新范式。',
                'source': 'arXiv / physics.ao-ph（CMCC + Univ. Bologna）',
                'url': 'https://arxiv.org/abs/2608.16449',
                'date': '2026-08-17',
            },
            {
                'title': 'RCNN：深度学习残差校正网络海表温度统计降尺度（arXiv, 2026-08-12）',
                'badge': '[论文]',
                'abstract': '西澳大利亚大学团队提出残差校正神经网络（RCNN）框架，用于海表温度（SST）统计降尺度。该框架先用U-Net创建初始高分辨率SST估计，再通过整合动态缩放的残差进行精炼，有效捕捉SST宏观模式及涡流和锋面等精细特征。案例研究显示该方法在澳大利亚西海岸将SST分辨率从25 km提高到2 km，改进了海洋热浪预测，在准确性和计算效率方面优于传统方法，有望改进沿海影响评估和海洋生态系统研究。',
                'source': 'arXiv / cs.LG（Univ. Western Australia）',
                'url': 'https://arxiv.org/abs/2608.10022',
                'date': '2026-08-12',
            },
            {
                'title': 'CORAL-AUV：MIT-WHOI水下机器人自主科学探索学习框架（CoRL 2026, arXiv 2607.09557）',
                'badge': '[论文]',
                'abstract': 'MIT-WHOI联合团队提出 CORAL-AUV 框架，将强化学习与科学先验知识结合，使自主水下航行器（AUV）能够在深海科学考察中自主决策采样策略。该框架融合科学目标驱动的奖励函数与物理约束的运动规划，使AUV在有限能源预算下最大化科学信息采集量。在CoRL 2026（机器人学习顶会）发表，为深海自主观测从"预编程路径"向"智能自适应探索"转变提供方法论基础，对深海热液、冷泉等极端环境调查具有重要意义。',
                'source': 'CoRL 2026 / arXiv（MIT-WHOI）',
                'url': 'https://arxiv.org/abs/2607.09557',
                'date': '2026-07-15',
            },
            {
                'title': 'GNN-BiLSTM韩国海水养殖海洋热浪AI预警系统：提前38小时预警（Tech Times, 2026-08-04）',
                'badge': '[要闻]',
                'abstract': '韩国国立水产科学院开发基于混合图神经网络-双向LSTM（GNN-BiLSTM）的海洋热浪AI预警系统，为韩国南部30个网箱养殖监测站提供提前38小时的致命热浪预警。GNN空间图将30个监测站作为节点、313条无向边表征站点间热耦合结构，当离岸站检测到升温时自动将信息传播至近岸养殖区。系统在28°C预警阈值实现 timely advisory，而精度更高的CNN-LSTM反而错过该阈值。该系统2026年发表于npj Ocean Sustainability，预计韩国养殖气候损失将达483M-1.14B USD。',
                'source': 'Tech Times / npj Ocean Sustainability',
                'url': 'https://www.techtimes.com/articles/323073/20260804/ai-early-warning-system-buys-korean-fish-farms-38-hours-before-lethal-heatwaves-strike.htm',
                'date': '2026-08-04',
            },
        ],
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': '广州南沙海洋经济产业科技创新交流对接会：AquaLink水下数字孪生平台+HKUST(GZ)海洋数字孪生+DeepMatrix多智能体系统（2026-08-13）',
                'badge': '[动态]',
                'abstract': '8月13日，海洋经济产业科技创新交流对接会在广州南沙举行。香港科技大学（广州）刘易团队展示了覆盖近岸环境诊断、海岸带生态修复、养殖区环境容量评估及海洋数字孪生四大应用场景的综合解决方案，在珠江口缺氧区治理、红树林碳汇评估、生蚝养殖水质净化方面取得典型案例。AquaLink水下平台融合水下机器人、AI视觉识别和数字孪生技术，已在香港桥嘴洲海岸公园完成示范应用。深海智人DeepMatrix以多智能体决策大模型为核心，结合全系列水下机器人硬件矩阵，推动从"单机替代"向"体系协同"的范式升级。',
                'source': '花城网 / 广州南沙',
                'url': 'https://huacheng.gz-cmc.com/pages/2026/08/13/eb0991b00d634b91ba0453bb3ccead9e.html',
                'date': '2026-08-13',
            },
            {
                'title': '本周暂无明显新进展（DITTO Summit 2026 07-30、WavyOcean 3.0 07-13 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数字孪生方向近一周无重大新平台或新框架发布。DITTO Summit 2026横滨（07-30收录）、WavyOcean 3.0（07-13/07-28收录）、广州南沙AquaLink+DeepMatrix（本期收录）为近期主要动态，本期不重复收录。',
                'source': '-',
                'url': 'https://www.ocean-digital-twin.org/',
                'date': '2026-08-25',
            },
        ],
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': 'CMEMS MyOcean Viewer发布"洋流：地球隐形引擎"交互式可视化（2026-08-25）',
                'badge': '[动态]',
                'abstract': 'Copernicus Marine Service发布"Ocean Currents: Earth\'s Invisible Engine"交互式可视化专题，通过MyOcean Pro Viewer展示全球海洋表层流与深层热盐环流的三维动态。用户可查看洋流的实时状态、过去两年历史以及10天预报，可视化覆盖南极绕极流、湾流等关键环流系统。该专题科普洋流作为地球"循环系统"运输热量、营养盐和生命的作用，并关联AMOC对西欧温和气候的影响，结合GLORYS12再分析数据与GLO12预报产品，为海洋环流研究提供直观可视化工具。',
                'source': 'Copernicus Marine Service (CMEMS)',
                'url': 'https://marine.copernicus.eu/news/ocean-currents-earths-invisible-engine',
                'date': '2026-08-25',
            },
            {
                'title': '本周暂无明显新工具发布（MyOcean Pro 3D 08-03、SeaDAS v10.0 已收录）',
                'badge': '[关注]',
                'abstract': '海洋可视化方向近一周无重大新工具发布。CMEMS MyOcean Pro 3D可视化路线图（08-03收录）、MyOcean Stories科普叙事功能（06-01收录）均已在此前日报覆盖。CMEMS洋流交互式可视化（本期收录）为近期主要动态。',
                'source': '-',
                'url': 'https://viewer.emodnet.eu/',
                'date': '2026-08-25',
            },
        ],
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality",
        "items": [
            {
                'title': '本周暂无明显新进展（ML辅助事件感知QC 08-08、DTF-Net 08-07 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据质量方向近一周无重大新方法发布。ML辅助事件感知QC框架（JMSE 08-08收录）、DTF-Net深度学习风数据质控（08-07收录）、BGC-Argo CHLA大规模再处理（07-11收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://www.argo.org.cn/',
                'date': '2026-08-25',
            },
        ],
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': 'SIREN-TV：基于隐式神经表示的卫星高度计海面高度连续重建框架（GMD, 2026）',
                'badge': '[论文]',
                'abstract': '研究团队提出 SIREN-TV 框架，将海面高度（SSH）表示为空间-时间的连续函数，使用基于SIREN的坐标网络从稀疏沿轨观测中学习连续SSH表示，并引入全变差（TV）空间梯度正则化抑制不受支撑的局部变化。该框架在多任务卫星高度计观测和高分辨率数值模拟上评估，显示其能重建主要SSH变异和主导中尺度模式，全球精度与现有插值和数据同化方法相当且有效特征分辨率有所提升。连续全可微表示可直接计算空间导数，支持高阶海洋学诊断，为稀疏不规则采样下的SSH插值提供新途径。',
                'source': 'Geoscientific Model Development (GMD)',
                'url': 'https://gmd.copernicus.org/articles/19/7349/2026/gmd-19-7349-2026.html',
                'date': '2026-08-14',
            },
            {
                'title': 'SGD-SST 2.0：跨传感器无缝全球日均SST产品（2003-2025, Expert Systems with Applications, 2026-08-06）',
                'badge': '[论文]',
                'abstract': '研究团队开发自适应ConvLSTM时空重建模型，通过贝叶斯优化生成无缝全球日均SST产品（SGD-SST 2.0），空间分辨率9 km，覆盖2003-2025年。模型采用动态时间步选择机制（由缺失率驱动）和自适应后处理策略（考虑纬度效应），并开发VIIRS预训练模型迁移学习策略，解决MODIS数据高缺失率问题，实现跨传感器多源产品无缝重建。验证显示相关系数0.994、RMSE 0.916 K、MAE 0.602 K，较SGD-SST 1.0在中低纬度精度显著提升。数据集已在HuggingFace开放下载。',
                'source': 'Expert Systems with Applications (Elsevier)',
                'url': 'https://dl.acm.org/doi/10.1016/j.eswa.2026.132259',
                'date': '2026-08-06',
            },
            {
                'title': 'U-Net地中海SST云遮挡重建：深度学习优于最优插值（EGU26, 2026-08-18）',
                'badge': '[论文]',
                'abstract': 'CMCC基金会与博洛尼亚大学团队将基于U-Net的深度学习方法扩展至整个地中海SST重建，解决红外遥感云遮挡导致的数据缺失。训练策略为将随机日期的云掩膜叠加到输入SST上以提供损失计算的ground truth。模型在地中海全域技巧与先前意大利海域模型相当，在云遮挡区域仅产生有限附加误差。与基于最优插值的Level 4产品相比，U-Net在无云区域保留Level 3产品相对漂流浮标的误差和偏差特性，重建区域技巧退化轻微，独立验证显示重建引入的附加误差有限。',
                'source': 'EGU General Assembly 2026 (CMCC + Univ. Bologna)',
                'url': 'https://meetingorganizer.copernicus.org/EGU26/EGU26-21240.html',
                'date': '2026-08-18',
            },
        ],
    },
    {
        "title": "六、海洋数据管理与共享",
        "en": "Ocean Data Management & Sharing",
        "items": [
            {
                'title': '全国首个海洋公共数据团体标准在青岛发布：分类分级+资源目录编制规则（2026-08-12）',
                'badge': '[要闻]',
                'abstract': '《海洋公共数据分类分级指南》《海洋公共数据资源目录编制规则》两项团体标准在2026年第二期青岛市数据要素成果发布会上重磅发布，为全国首个针对海洋公共数据领域的专项标准化成果。《分类分级指南》构建"行业领域-业务职能-内容主题"三级分类体系，将海洋公共数据从高到低划分为核心、重要、一般共六个级别，配套分级安全保护要求与共享、开放、授权运营三类开发利用规则。《目录编制规则》搭建覆盖六大类核心要素的完整元数据体系，统一编制口径、字段规范与技术要求，形成"分类分级定规则、目录编制明底数"的海洋公共数据治理闭环。',
                'source': '人民网山东频道 / 今日头条',
                'url': 'https://www.toutiao.com/article/7673061404434022912/',
                'date': '2026-08-12',
            },
            {
                'title': '国家数据局发布会：涉海公共数据"制度先行+场景牵引+多方协同"开发利用路径（2026-08-25）',
                'badge': '[要闻]',
                'abstract': '8月25日，国家数据局举办"数据价值化我们在行动"系列新闻发布会第五场。辽宁省数据和政务服务局副局长于冰介绍涉海公共数据开发利用路径：(1)建立分级分类标准制度体系——率先出台海洋科学数据管理、汇交、共享、安全等7项规范，明确数据分级存储、分类授权规则；(2)打造"政校企"协同模式——依托大连海洋大学建成省级海洋与极地科学数据中心，推进海洋行业可信数据空间试点，通过"数据可用不可见"隐私计算技术破解安全与流通矛盾；(3)打通数据要素价值化闭环——推动海洋数据产品进场交易和知识产权登记，形成"数据治理-产品研发-市场交易-价值反哺"闭环路径。',
                'source': '新京报贝壳财经 / 东方财富网',
                'url': 'https://finance.eastmoney.com/a/202608253852757325.html',
                'date': '2026-08-25',
            },
            {
                'title': 'ROSA发布海上风电渔业科学数据治理指南（ROSA, 2026-08）',
                'badge': '[动态]',
                'abstract': 'Responsible Offshore Science Alliance (ROSA)发布 Data Governance Guidance，旨在标准化美国东海岸海上风电渔业与海洋数据的采集、共享和使用。该指南为研究人员、资助者和海上开发商提供通用框架，确保数据保持可访问、可互操作和可信赖，同时尊重数据生成者和管理者的权利。内容涵盖数据管理与共享计划(DMSP)建议时间线、元数据与数据发布、仓库选择指南、敏感或受限数据处理、最低元数据标准与版本控制最佳实践，反映ROSA研究伙伴和顾问的广泛意见，将随领域发展持续更新。',
                'source': 'ROSA (Responsible Offshore Science Alliance)',
                'url': 'https://www.rosascience.org/rosa-releases-data-governance-guidance-for-offshore-wind-fisheries-science/',
                'date': '2026-08-15',
            },
        ],
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Research Expeditions",
        "items": [
            {
                'title': '"探索6000" AUV南海冷泉区航次实现首次商业化应用（2026-07-28至08-07）',
                'badge': '[航次]',
                'abstract': '由广东智能无人系统研究院（南沙）和中科院沈阳自动化研究所牵头研制的"探索6000" AUV搭乘"实验6"科考船执行国家自然科学基金共享航次任务，实现首次商业化应用。作为航次核心探测装备，"探索6000"执行了近海底精细光学与化学融合探测任务，6天内完成5个潜次作业，累计水下有效作业超30小时，获取近海底3米光学全覆盖测线长度近26000米，成功获取多类型环境化学与光学探测数据，为冷泉区生境调查与生物多样性研究提供关键支撑。团队实现探测载荷模块化搭载与快速集成，验证了从装备研制到商业化运营的全链条服务能力。',
                'source': '广州市南沙区人民政府',
                'url': 'https://www.gzns.gov.cn/zwgk/zwdt/content/post_10970782.html',
                'date': '2026-08-07',
            },
            {
                'title': 'NOAA Okeanos Explorer完成库克群岛26天深潜航次：14次ROV下潜（2026-08-19）',
                'badge': '[航次]',
                'abstract': 'NOAA船Okeanos Explorer完成为期26天的库克群岛深潜考察后返回拉罗通加。航次在西部库克群岛几乎没有先前数据的水域进行了14次遥控潜水器（ROV）下潜，采集400余个样本，探索了海山、深海平原和Manihiki高原区域，收集23个生物标本（部分疑为新物种）。航次还确认了库克群岛海洋领土内大面积多金属结核场的存在，甚至出现在科学家未预期的区域。超过6万人通过直播观看ROV下潜。美国宣布将在库克群岛设立NOAA科学研究员职位，支持科学与监管过程。',
                'source': 'RNZ Pacific / NOAA Ocean Exploration',
                'url': 'https://www.rnz.co.nz/news/pacific/1057866/teeming-with-life-cook-islands-officials-enthuse-over-noaa-deep-dive',
                'date': '2026-08-19',
            },
            {
                'title': 'E/V Nautilus AUV Sentry马里亚纳群岛深海生境调查（NA179/NA180, 2026-08-03）',
                'badge': '[航次]',
                'abstract': 'E/V Nautilus在马里亚纳群岛深海生境考察航次（NA179和NA180）中与WHOI AUV Sentry团队合作。Sentry设计用于在低高度和复杂地形下进行海底调查，沿预编程航线收集海底测绘数据，并在500×500米区域进行详细测绘调查，随后下降至距海底6米内使用频闪和相机进行底栖照片调查。该调查方法平衡了大距离覆盖与精细观察。AUV Sentry已有6次部署，其中5次成功收集图像。所有数据将公开存档，无禁运或访问限制，确保深海数据永久可用。第二期航次为期22天。',
                'source': 'Nautilus Live / WHOI',
                'url': 'https://nautiluslive.org/album/2026/08/03/abyssal-sentry-survey-updates',
                'date': '2026-08-03',
            },
            {
                'title': 'NOAA EX2606美属萨摩亚ROV+测绘航次启动：关键矿产与深海生态（2026-08-20至09-17）',
                'badge': '[航次]',
                'abstract': '8月20日至9月17日，NOAA Ocean Exploration在NOAA船Okeanos Explorer上开展2026年美属萨摩亚ROV+测绘航次（EX2606），探索美属萨摩亚深海水域。航次包括ROV下潜（深度2000-6000米）探索海底和水柱、夜间测绘操作和通过远程参与技术的持续岸基参与。航次聚焦建立海洋关键矿产（特别是多金属结核）基线评估，以及海山生境、深水珊瑚和海绵群落、鱼类生境和水柱。潜水每日直播（8AM-8PM SST）。美属萨摩亚被指定为美国专属经济区内最高优先区域，因显著的产业兴趣和多金属结核潜在存在。',
                'source': 'NOAA Ocean Exploration',
                'url': 'https://oceanexplorer.noaa.gov/expedition/ex2606',
                'date': '2026-08-20',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': 'CMEMS 2026年8月产品更新：北极波浪/波罗的海物理/北极潮汐/北极生物地球化学（CMEMS, 2026-08）',
                'badge': '[数据]',
                'abstract': 'Copernicus Marine Service 2026年8月发布多项产品更新：(1)北极多年波浪回溯（ARCTIC_MULTIYEAR_WAV_002_013）时间扩展至1960年；(2)波罗的海物理分析与预报（BALTICSEA_ANALYSISFORECAST_PHY_003_006）更新模型测深（基于EMODnet测深2020版+区域修正）并新增冰漂移参数usi/vsi；(3)新增北极海洋潮汐分析与预报产品（ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015），3km分辨率15层垂直，TOPAZ6确定性潮汐系统受TOPAZ5 EnKF 6km系统约束；(4)北极生物地球化学分析与预报改进中层浮游动物昼夜垂直迁移与碳输出过程，新增POC变量。多项更新采用双重发布期。',
                'source': 'Copernicus Marine Service (CMEMS)',
                'url': 'https://marine.copernicus.eu/mt/user-corner/product-roadmap/transition-information?page=4',
                'date': '2026-08-13',
            },
            {
                'title': '本周暂无明显新进展（GEBCO_2026 WMS 08-04、Argo GDAC快照 08-08 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据中心方向近一周无重大新发布。GEBCO_2026网格WMS图层上线（08-04收录）、Argo GDAC全球快照（08-08收录）、PANGAEA新增GEOMAR锚系数据（08-06）均已在此前日报覆盖。CMEMS 8月产品更新（本期收录）为近期主要动态。',
                'source': '-',
                'url': 'https://www.gebco.net/data_and_products/gridded_bathymetry_data/',
                'date': '2026-08-25',
            },
        ],
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources",
        "items": [
            {
                'title': 'NOAA Next-Gen NOS OFS Skill Assessment v1.7.1：Python海洋预报模型技巧评估（GitHub, 2026-08-04）',
                'badge': '[工具]',
                'abstract': 'NOAA CO-OPS和OCS开发的Next Gen NOS海洋预报模型技巧评估与处理软件更新至v1.7.1。该Python工具替代现有Fortran工具，对NOAA业务化预报系统(OFS)进行近实时技巧评估，在特定点位（1D）和整个二维海面（2D,遥感产品）比较模型预报与观测。新增潮汐分析子包、ADCP安装类型分类与侧视bin处理修复、CHS基准面崩溃修复。OFS支撑航运航道导航、搜救、休闲航行和渔业及风暴效应追踪。v1.7.1更新了README和wiki文档。',
                'source': 'NOAA CO-OPS / GitHub',
                'url': 'https://github.com/NOAA-CO-OPS/Next-Gen-NOS-OFS-Skill-Assessment',
                'date': '2026-08-04',
            },
            {
                'title': 'earthlens v0.14.0：多源遥感与气候数据下载Python包（conda-forge, 2026-08-08）',
                'badge': '[工具]',
                'abstract': 'earthlens发布v0.14.0版本，是用于从多个数据提供商下载卫星和气候数据的Python包，采用延迟加载后端架构。自v0.11.0起拆分为六个可安装发行版加一个元包：earthlens-core（facade、CLI、抽象与共享传输，无提供商SDK）、earthlens-atmosphere（天气/气候/空气质量/太阳能风能）、earthlens-ocean（海洋/水文/海洋后端）、earthlens-imagery（光学/SAR影像与EO档案）、earthlens-land（陆地/人口/地形）、earthlens-hazards（灾害/人道主义/基础设施）。许可证为GPL-3.0-only，支持conda-forge安装。',
                'source': 'conda-forge / GitHub (serapeum-org)',
                'url': 'https://anaconda.org/conda-forge/earthlens',
                'date': '2026-08-08',
            },
            {
                'title': 'MDOcean v1.4.4：海洋波浪能转换器多学科设计优化开源工具（Zenodo, 2026-08-17）',
                'badge': '[工具]',
                'abstract': 'Cornell University与University of Michigan团队发布MDOcean v1.4.4，使用多学科设计优化(MDO)优化海洋波浪能转换器的开源代码库。该工具结合多学科设计优化方法与海洋工程应用，支持波浪能转换器的系统级优化设计。v1.4.4版本于8月17日发布，此前在8月5日至17日内连续发布v1.4.0至v1.4.4共5个版本，迭代频繁。许可证为MIT License，代码托管于GitHub (symbiotic-engineering/MDOcean)。',
                'source': 'Zenodo / Cornell Univ. + Univ. Michigan',
                'url': 'https://zenodo.org/records/21699291/latest',
                'date': '2026-08-17',
            },
        ],
    },
]

# Read feishu_write_doc.py and replace SECTIONS
DATA_SOURCE = r'C:\Users\Administrator\WorkBuddy\Claw\feishu_write_doc.py'
with open(DATA_SOURCE, encoding='utf-8') as f:
    content = f.read()

new_block = 'SECTIONS = ' + repr(SECTIONS)
pattern = re.compile(r'SECTIONS\s*=\s*\[', re.S)
match = pattern.search(content)
if match:
    # Find the end of the SECTIONS list using bracket counting
    bracket_start = content.index('[', match.end() - 1)
    depth = 0
    i = bracket_start
    while i < len(content):
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
            if depth == 0:
                break
        i += 1
    # Find the newline after the closing bracket
    end_pos = i + 1
    # Replace from SECTIONS = [ to the matching ]
    content = content[:match.start()] + new_block + content[end_pos:]
else:
    raise RuntimeError('SECTIONS not found in feishu_write_doc.py')

with open(DATA_SOURCE, 'w', encoding='utf-8') as f:
    f.write(content)

n_items = sum(len(s['items']) for s in SECTIONS)
effective_items = sum(1 for s in SECTIONS for item in s['items'] if item.get('badge') not in ['[关注]', '[备注]'])
print(f'OK: SECTIONS written, {len(SECTIONS)} sections, {n_items} total items, {effective_items} effective')
for s in SECTIONS:
    eff = sum(1 for item in s['items'] if item.get('badge') not in ['[关注]', '[备注]'])
    print(f'  {s["title"]}: {len(s["items"])} items ({eff} effective)')
