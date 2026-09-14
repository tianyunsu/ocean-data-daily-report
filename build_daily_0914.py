# -*- coding: utf-8 -*-
"""
build_daily_0914.py — 将 2026-09-14 日报 SECTIONS 写入 feishu_write_doc.py
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': 'KiloDA：扩散模型从稀疏站点观测重建公里尺度近地面风场，仅需 0.24% 格点观测即可恢复局地风结构（arXiv, 2026-09-10）',
                'badge': '[论文]',
                'abstract': '公里尺度近地面风场对理解复杂地形上的大气过程至关重要，但稀疏不均匀的站点观测使重建极具挑战。研究提出 KiloDA——一个基于扩散框架的逐时公里尺度风场重建方法。KiloDA 从历史 3 km WRF 模式预报中学习风场的统计分布与空间结构，重建时无需同期 WRF 场，仅靠站点观测约束当前大气状态并引导后验采样。理想化实验中，仅 0.24% 格点被观测时即可恢复局地风结构，全面优于传统插值方法。在完全留出区域的真实观测实验中，KiloDA 相对 ERA5 再分析将风速中位 RMSE 降低 19%，在高海拔和高地形起伏区域改善最大，证明历史模式档案可为稀疏观测风场重建提供有效结构先验。',
                'source': 'arXiv (physics.ao-ph)',
                'url': 'https://arxiv.org/abs/2609.11230',
                'date': '2026-09-10',
            },
            {
                'title': 'Ocean-E2E：混合物理与数据驱动的全球极端海洋热浪预报框架，结合端到端神经同化实现 40 天预报（KDD 2026, 清华SAIL, 2026-08-09）',
                'badge': '[论文]',
                'abstract': '极端海洋热浪（MHW）对海洋生态系统有深远影响，精准预报具有重要科学与经济价值。清华大学地球系统科学系 SAIL 团队在 KDD 2026 AI for Sciences Track 作口头报告，提出 Ocean-E2E——混合物理与数据驱动的全球 MHW 预报框架。该框架基于 MHW 物理本质，显式建模海洋中尺度平流与海气相互作用（动态核），实现端到端数据同化与区域高分辨率预测，可完全脱离数值模式独立运行。实验表明 Ocean-E2E 在全球至区域、短期至长期（1-40 天）预报中均优于当前最先进的海洋数值/AI 预报-同化模型，尤其在最极端 MHW 事件上表现突出。代码已在 GitHub 开源。（注：该工作的 arXiv 预印本 v1 首次公开于 2025 年 5 月，本条以 KDD 2026 会议报告日作为新闻时点。）',
                'source': 'KDD 2026 AI for Sciences Track（清华大学 + 崂山实验室）',
                'url': 'https://arxiv.org/abs/2505.22071',
                'date': '2026-08-09',
            },
            {
                'title': '高频雷达波浪高度估计：窗口包络统计方法从时域信号提取有效波高（arXiv, 2026-09-11）',
                'badge': '[论文]',
                'abstract': '高频（HF）雷达是近岸海浪观测的重要手段，但从未校准的雷达回波中准确估计有效波高（Hs）仍面临挑战。研究提出窗口包络统计方法，利用时域回波信号的包络特征在多个时间窗口内提取波浪信息，实现 Hs 的稳健估计。该方法不依赖经验标定即可从原始雷达信号中获取波浪高度，为近岸波浪监测提供了一种新的信号处理路径，具有在现有 HF 雷达网络上部署的潜力。',
                'source': 'arXiv (physics.ao-ph)',
                'url': 'https://arxiv.org/abs/2609.10920',
                'date': '2026-09-11',
            },
            {
                'title': '机器学习天气预报模型在挪威北部的站点评估：复杂北极环境下 ML 模型 skill 检验（arXiv, 2026-09-11）',
                'badge': '[论文]',
                'abstract': '近年来基于机器学习的天气预报模型（如 Pangu-Weather、GraphCast）在全球尺度展现出与数值模式相当的预报能力，但在高纬度复杂地形下的表现尚缺乏系统评估。研究针对挪威北部——一个具有极夜、极地低层云和复杂海岸地形的高纬度区域，对多个 ML 天气预报模型进行站点级评估。使用稠密地面观测网络验证 2 m 温度、10 m 风速等要素，系统检验 ML 模型在北极环境下的预报 skill、偏差模式与季节敏感性，为 ML 天气预报在高纬度地区的业务化应用提供基准参考。',
                'source': 'arXiv (physics.ao-ph / cs.LG)（挪威科技大学等）',
                'url': 'https://arxiv.org/abs/2609.10564',
                'date': '2026-09-11',
            },
            {
                'title': '扩散先验引导稀疏观测的高分辨率温度降尺度：Steering Diffusion 实现从粗到细的温度场重建（arXiv, 2026-09-10）',
                'badge': '[论文]',
                'abstract': '从粗分辨率观测中恢复高分辨率温度场是气候与海洋研究的基础需求。研究提出一种以扩散先验引导稀疏观测的温度降尺度方法——Steering Diffusion。该方法从历史高分辨率数据中学习温度场的扩散先验分布，在推理时以稀疏观测为条件引导后验采样，生成与观测一致且物理合理的高分辨率温度场。在理想化与真实数据实验中，该方法在保留小尺度结构的同时显著降低了重建误差，为卫星 SST 降尺度、海洋剖面插值等场景提供了新的生成式建模工具。',
                'source': 'arXiv (physics.ao-ph / cs.LG)（印度统计研究所等）',
                'url': 'https://arxiv.org/abs/2609.09247',
                'date': '2026-09-09',
            },
        ],
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': 'EMODnet 全量数据集实现与 EDITO 数据湖的自动化同步：欧洲数字孪生海洋核心基础设施重大里程碑（EMODnet, 2026 Summer）',
                'badge': '[动态]',
                'abstract': 'EMODnet 宣布完成一项重要里程碑——所有 EMODnet 数据集现已通过全自动化同步机制无缝集成至 EDITO 数据湖（EDITO Data Lake）。这确保了 EDITO 生态系统中持续可获取最新、可信的 EMODnet 原位海洋数据，提升了欧洲海洋数据的可访问性与互操作性。EDITO 是欧洲数字孪生海洋（EU DTO）的核心公共基础设施，由 Mercator Ocean International 和 VLIZ 联合开发，整合了 Copernicus Marine Service 与 EMODnet 的数据和服务。此次自动化同步标志着 EU DTO 从数据汇集向实时孪生迈出关键一步。',
                'source': 'EMODnet Newsletter (Summer 2026)',
                'url': 'https://ec.europa.eu/newsroom/emodnet/newsletter-archives/78661',
                'date': '2026-09-01',
            },
        ],
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': 'WakeAtlas：基于 CesiumJS 的免费三维海洋探索平台上线，整合 AIS 船舶、沉船、Argo 剖面与 Copernicus 生物地球化学层（DEV Community, 2026-09-12）',
                'badge': '[工具]',
                'abstract': '开发者 William Carne 发布了 WakeAtlas（wakeatlas.uk），一个免费的三维海洋探索平台。该平台基于 CesiumJS 构建，将原本分散在各自目录中的海洋信息整合到一个交互式三维地球仪上。可探索内容包括：实时 AIS 船舶位置（流式更新可见区域内的位置变化）、沉船历史与历史船舶信息、美国主要港口的高分辨率影像、Argo 海洋剖面（显示随深度变化的海洋状况）、Copernicus Marine 生物地球化学层（含氧气、营养盐和浮游生物）、北极和南极海冰密集度（含不同日期对比）。平台无需注册即可免费使用，定位为探索与研究工具而非导航系统。开发者在性能优化方面采用了仅流式传输可见船舶位置变化、预缓存港口影像瓦片等策略。',
                'source': 'DEV Community / wakeatlas.uk',
                'url': 'https://dev.to/william_carne_1332c355841/building-wakeatlas-ships-shipwrecks-and-ocean-science-on-a-free-cesiumjs-globe-1e62',
                'date': '2026-09-12',
            },
        ],
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality / QA-QC",
        "items": [
            {
                'title': 'Sentinel-6 双星同轨串联飞行完成星间交叉校验：海平面基准卫星交接就绪，延续近四十年测高记录（NASA/JPL, 2026-09-09）',
                'badge': '[动态]',
                'abstract': 'NASA 与欧洲伙伴于 2025 年 11 月发射的 Sentinel-6B，目前正以约 30 秒的间隔紧随前辈 Sentinel-6 Michael Freilich 在同一轨道上串联飞行，两颗卫星先后测量同一片海面，以此交叉校验新卫星的测高系统与既有海平面基准是否一致——这正是“同一方法、每次都量得一样”的连续性保障机制。Sentinel-6B 已于 2026 年 7 月 15 日开始向预报系统输出低延迟数据。两颗卫星各载一台 Poseidon-4 雷达高度计与微波辐射计，测量海面高度、浪高与海面风速，另配 GNSS 掩星仪反演大气湿度、气压与温度。NOAA 专家评价“就数据质量而言，Sentinel-6 任务无与伦比”，并计划在年底前将该高度计数据纳入其卫星海洋热含量算法。Sentinel-6B 将于今年晚些时候接任全球海平面测量的参考卫星，延续自 1992 年 TOPEX/Poseidon 以来近四十年的海平面记录。',
                'source': 'NASA / JPL（Sentinel-6/Jason-CS 任务；ESA、EUMETSAT、NOAA、CNES 联合）',
                'url': 'https://www.nasa.gov/missions/jason-cs-sentinel-6/how-2-us-european-satellites-are-studying-hurricanes-during-el-nino/',
                'date': '2026-09-09',
            },
            {
                'title': 'CFOSAT SWIM 海浪谱产品三代版本质量评估：6.0.3 / 7.0.0 / 7.1.0 与 ERA5 时空匹配，按海况分级验证（《海洋学报》, 网络出版 2026-09-04）',
                'badge': '[论文]',
                'abstract': '中法海洋卫星 CFOSAT 搭载全球首款专门测量二维海浪谱的海浪波谱仪 SWIM，已在轨运行超过七年；随着地面处理技术持续优化，SWIM 海浪谱产品经历多次版本迭代，不同版本在数据预处理算法与观测波束校正策略上的差异，已使其公开可用的 6.0.3、7.0.0、7.1.0 三个版本在谱结构与数据质量上表现出明显分化。南京信息工程大学与国家卫星海洋应用中心等团队将各版本 SWIM 海浪谱与 ERA5 海洋再分析数据做时空匹配，并基于风浪与涌浪有效波高开展精细化海况分类验证，系统刻画了三代产品的质量演变特征。该工作为全球用户按研究目的选择合适版本、为后续版本迭代改进提供了量化依据。',
                'source': '《海洋学报》Acta Oceanologica Sinica（南京信息工程大学 + 国家卫星海洋应用中心）',
                'url': 'http://hyxbocean.cn/article/id/1bddb856-f5ac-40d6-8996-ad69bba16ae0?viewType=HTML',
                'date': '2026-09-04',
            },
        ],
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': 'MG-GCNN：多粒度图协作神经网络从稀疏观测网格重建卫星辅助三维海洋环境场，地形感知+垂直特征+多粒度聚合（RS, 2026-09-04）',
                'badge': '[论文]',
                'abstract': '海洋遥感将卫星广域面观测与稀疏水下观测结合，但从不规则采样、垂直非平稳性与水深障碍中重建连续三维环境场仍具挑战。西北工业大学提出多粒度图协作神经网络（MG-GCNN），将离散观测点抽象为拓扑图中的异质节点，融合高分辨率水深作为几何先验，通过地形感知图构建、垂直特征整合、多粒度聚合与自监督掩码节点重建，在有限观测下捕获空间与垂直依赖关系。实验表明 MG-GCNN 在不同稀疏度（含高稀疏与 Argo 采样配置）下，在温度、盐度和流场重建精度上全面优于基线插值与卷积模型，尤其在水下地形复杂与极端采样稀疏区域优势显著。重建场可为海洋声学传播建模、水下感知等后续应用提供三维环境输入。',
                'source': 'Remote Sens. 2026, 18(17), 3003（西北工业大学）',
                'url': 'https://www.mdpi.com/2072-4292/18/17/3003',
                'date': '2026-09-04',
            },
        ],
    },
    {
        "title": "六、数据管理与共享",
        "en": "Data Management & Sharing",
        "items": [
            {
                'title': '联合国海洋十年发布社会经济数据共享指南：EMODnet 参与制定，为全球社会经济海洋数据共享提供基础框架（DCO-ODS, 2026-09-10）',
                'badge': '[要闻]',
                'abstract': '联合国海洋十年数据共享协调办公室（DCO-ODS）正式发布《社会经济数据共享指南》。该指南由 DCO-ODS 与 EMODnet 及多方专家共同制定，提供高级别原则并突出相关资源，旨在促进负责任、开放、透明的社会经济数据共享实践。EMODnet 秘书处负责人 Kate Larkin 在 9 月 10 日的 DCO-ODS 网络研讨会上发表演讲，讨论推进社会经济海洋数据可及性与共享的重要性。指南覆盖数据许可、元数据标准、FAIR 原则在社会经济数据中的实施等关键议题，为加强全球社会经济数据共享实践提供了基础性框架，填补了海洋十年数据战略中社会经济维度的空白。',
                'source': 'UN Ocean Decade / DCO-ODS / EMODnet',
                'url': 'https://ec.europa.eu/newsroom/emodnet/redirection/item/952541',
                'date': '2026-09-10',
            },
            {
                'title': 'EMODnet Biology 发布北海底拖网捕捞对底栖动物影响新数据产品（EMODnet, 2026-09-11）',
                'badge': '[数据]',
                'abstract': 'EMODnet Biology 发布关于北海荷兰海域底拖网捕捞对底栖动物影响的新数据产品。产品基于 EMODnet Biology 前期开发的两个 R 包（Btrait 与 Bfiat，Soetaert & Beauchard）所构成的确定性建模框架：该框架描述拖网扰动期间底栖物种密度或生物量的衰减及其在两次捕捞事件之间的恢复过程，并以扰动状态下平均生物量或生态系统功能相对于扰动前状态的比例，定量表达捕捞影响。本产品将 Bfiat 方法应用于 EMODnet Biology 的底栖数据（荷兰所属北海部分，2009 年），量化底层捕捞如何与物种生活史性状相互作用，进而改变底栖生物量，以及底栖动物混合与生物灌溉沉积物的潜力（即沉积物的生物扰动与生物灌溉潜力，二者直接影响沉积物地球化学与全球生物地球化学循环）。理解底拖网渔具对底栖生命的影响，是正确评估渔业影响不可或缺的一步。',
                'source': 'EMODnet Biology（NIOZ；Beauchard & Soetaert, 2026, Ecological Applications）',
                'url': 'https://emodnet.ec.europa.eu/en/emodnet-biology-product-impacts-bottom-trawling-benthic-fauna-dutch-part-north-sea',
                'date': '2026-09-11',
            },
        ],
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Ship-time",
        "items": [
            {
                'title': '2026 年度东海科学考察实验研究秋季共享航次启航：向阳红 18 在长江口 10 个固定点位开展综合调查（自然资源部第一海洋研究所, 2026-09-10）',
                'badge': '[航次]',
                'abstract': '国家自然科学基金项目 2026 年度东海科学考察实验研究秋季共享航次于 9 月 10 日至 19 日在长江口以下 10 个固定点位及点位连线之间水域开展，日夜作业。作业由自然资源部第一海洋研究所负责，考察船"向阳红 18"执行。调查覆盖 31N-32N、122-30E 至 124-30E 之间的东海陆架区，进行水文、化学、生物等多学科综合观测与采样。该航次是基金委共享航次计划的年度例行任务之一，为东海物质能量输运、陆架动力过程及生态环境变化研究提供基础数据。截至 2025 年底，向阳红 18 已承担包括国家专项、基金委共享航次等 57 个航次/段，年平均出海 142 天。',
                'source': '中华人民共和国海事局 / 自然资源部第一海洋研究所',
                'url': 'https://www.msa.gov.cn/html/cnmsa/hxaq/article/2026/bf4707763896446bbe04145b2d98b066.html',
                'date': '2026-09-10',
            },
            {
                'title': '西太平洋海底热液区联合科考：向阳红 10 号起航，清华+青岛海洋地质所+上海交大联合开展（2026-09-11 报道）',
                'badge': '[航次]',
                'abstract': '清华大学、中国地质调查局青岛海洋地质研究所、上海交通大学等单位联合开展的西太平洋海底热液活动与资源科考航次取得重要突破。科考队搭乘“向阳红 10”号科考船，于 8 月 10 日自深圳起航，历时 18 天，在位于我国专属经济区的西太平洋弧后盆地内实施 7 次探测器下潜作业。团队依托自主研制的深海可控式可视采样器（DCVS，国家自然科学基金重大科学仪器研制项目，清华大学自动化系牵头），在前期十多次探测、数十处高温热液喷口的基础上，精准锁定一处全新且规模巨大的海底热液活动矿区：伴生热液硫化物矿体由 3 个大型圆锥状矿体构成，主要矿物为黄铜矿、黄铁矿、闪锌矿；喷口位于水下约 700 至 1500 米，端元流体最高温度超过 315 ℃。对部分样品的初步分析显示，矿石中伴生金最高含量达 15.4 ppm、伴生银最高含量达 1271 ppm，金银平均含量显著优于陆地矿床。',
                'source': '中国新闻网（转央视新闻客户端）',
                'url': 'https://www.hn.chinanews.com.cn/news/gnxw/2026/0911/533649.html',
                'date': '2026-09-11',
            },
            {
                'title': '第 16 次北冰洋考察：雪龙 2 号为法国塔拉极地站破冰引航 110 海里，中法北极科考合作深化（2026年9月）',
                'badge': '[航次]',
                'abstract': '在北纬 80 度以北的北冰洋中央区，执行中国第 16 次北冰洋考察任务的“雪龙 2”号，为法国“塔拉极地站”科考平台破冰引航 110 海里，助其顺利抵达并固定于目标浮冰，开启首次北极越冬漂流考察。塔拉极地站是专门用于随北冰洋浮冰漂流观测的新型科考平台，自身航行与破冰能力较弱；2025 年中法双方达成意向，2026 年经自然资源部批准纳入本次考察任务。北京时间 9 月 8 日晚，正在马卡洛夫海盆开展海洋调查的“雪龙 2”号与塔拉极地站会合，两船保持约 300 米安全距离、以 4 至 7 节速度航行约 20 小时后于 9 日抵达目标浮冰；“雪龙 2”号从事先商定方向精准破入浮冰 100 多米开辟水道，确认浮冰无碎裂后退出，塔拉极地站沿水道驶入并锚定随冰漂流。两船告别后，“雪龙 2”号在附近多块浮冰布设冰基浮标，塔拉极地站亦协助布设一套，形成阵列协同开展海冰长期观测；因塔拉极地站途经俄罗斯以北海域遭遇气旋、油料消耗较多，“雪龙 2”号还应其请求提供船用燃油补给。',
                'source': '新华社（记者温竞华）· 经川观新闻转载',
                'url': 'https://cbgc.scol.com.cn/news/7945979',
                'date': '2026-09-11',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': 'NOAA NCEI 为深海科考上线 SOUP 样品数据管理系统：覆盖采样到归档的全生命周期云端管理（NOAA Ocean Exploration, 2026-09-10）',
                'badge': '[动态]',
                'abstract': '为提升深海实物样品所关联数据的完整性，美国国家环境信息中心（NCEI）开发了新一代采样数据管理系统 SOUP（Sampling Operations User Portal），并于 2026 年科考季开始时安装到 Okeanos Explorer 号科考船，现已纳入常态化作业。SOUP 是一个带后端数据库的云端应用，用于存储、管理与维护深海样品的全部信息：经纬度、水深、温度、盐度、溶解氧以及采样时的原位影像等环境元数据随采集即录入；用户可一键导入采样元数据、打印博物馆级标签、生成汇总导出与报告。系统与船载数据记录软件集成，通过自动化与网络化管道简化采样工作流，使数据备份与远程访问更快、人为差错更少。NCEI 负责样品数据自采集、处理直至长期归档与公共访问的全生命周期管理，后续或将 SOUP 推广至其他项目以替代过时流程。',
                'source': 'NOAA Ocean Exploration / NCEI',
                'url': 'https://oceanexplorer.noaa.gov/expedition-feature/soup-a-recipe-for-managing-data-from-the-abyss-to-archive',
                'date': '2026-09-10',
            },
        ],
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources",
        "items": [
            {
                'title': '暂无新增',
                'badge': '[备注]',
                'abstract': '本期检索窗口内（2026-08-31 至 2026-09-14）未发现符合条件的海洋软件新版本发布或代码工具更新。OceanParcels v3.1.4（Zenodo 标注 2025-08-07）超出 60 天时效窗口，已剔除。',
                'source': '',
                'url': '',
                'date': '',
            },
        ],
    },
]

# ---- write to feishu_write_doc.py ----
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Regex: replace everything from "SECTIONS = [" to the line before "def tr("
new_sections_line = 'SECTIONS = ' + repr(SECTIONS).replace('\\x27', "'")  # use repr for safe serialization

# Find the old SECTIONS assignment
pattern = r'SECTIONS\s*=\s*\['
# We need to find the end - it's the line before "def tr("
idx_start = content.find('SECTIONS = [')
if idx_start == -1:
    idx_start = content.find('SECTIONS=[')
if idx_start == -1:
    print("ERROR: Could not find SECTIONS in feishu_write_doc.py")
    exit(1)

idx_end = content.find('\ndef tr(')
if idx_end == -1:
    print("ERROR: Could not find 'def tr(' after SECTIONS")
    exit(1)

new_content = content[:idx_start] + new_sections_line + '\n' + content[idx_end+1:]

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
import ast
try:
    tree = ast.parse(new_content)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'SECTIONS':
                    s = ast.literal_eval(node.value)
                    total = sum(len(sec['items']) for sec in s)
                    effective = sum(1 for sec in s for item in sec['items'] if item.get('badge') != '[备注]')
                    print(f"OK: SECTIONS written. Total items: {total} (effective: {effective})")
                    print(f"Sections with content: {sum(1 for sec in s if sec['items'])}")
                    break
            else:
                continue
            break
except SyntaxError as e:
    print(f"SYNTAX ERROR: {e}")
