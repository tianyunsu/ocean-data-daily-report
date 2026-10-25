#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 日报数据源：把 SECTIONS 写入 feishu_write_doc.py（正则替换）"""
import re

SECTIONS = [
    {'title': '一、海洋人工智能',
     'en': 'Ocean AI / Marine Artificial Intelligence',
     'items': [
    {'title': 'MobiCom 2026：RollingPol 单次曝光偏振成像，破解水下后向散射',
     'badge': '[会议]',
     'abstract': '水下光学传感长期受悬浮颗粒后向散射困扰：偏振方法虽能抑制散射，但现有方案要么硬件昂贵，要么需要顺序多次成像而难以应对动态场景。哥伦比亚大学与密歇根大学团队在 MobiCom 2026 发表 RollingPol，用滚动快门式单次曝光偏振成像同时捕获多偏振态，实现动态水下场景的实时去散射增强，并配套去散射驱动的目标感知应用。作为移动计算顶会的水下感知新作，它把「偏振计算成像 + 移动平台低功耗约束」结合到一起，对水下机器人视觉前端具有直接参考价值。（ACM MobiCom 2026）',
     'source': 'ACM MobiCom 2026',
     'url': 'https://doi.org/10.1145/3795866.3844488', 'date': '2026-10-21'},
    {'title': 'imbalance-aware 跨数据集学习：海洋物种分类的分布漂移应对',
     'badge': '[会议]',
     'abstract': '水下海洋物种分类在实际部署中面临两重障碍：类别不平衡使尾部物种几乎学不到，而训练与部署数据集之间的分布漂移又让模型跨域失效。研究提出不平衡感知的学习与跨数据集评估框架，在多个水下物种基准上重新划分训练/测试以显式度量跨数据集泛化，配合重采样与损失重加权策略提升尾部类别表现。对基于水下影像的生态监测系统而言，这是一份面向真实部署条件的评估方法论样本。（Springer CCIS，会议论文）',
     'source': 'Springer CCIS（会议论文）',
     'url': 'https://doi.org/10.1007/978-3-032-42348-1_22', 'date': '2026-10-23'},
    {'title': '3D 声呐点云去噪：深度学习进入水下构筑物冲刷检测',
     'badge': '[论文]',
     'abstract': '海上风机基础、桥墩等水下构筑物的冲刷调查依赖多波束声呐点云，但悬浮物散射与声学噪声让点云毛刺丛生，传统滤波在去噪与保细节之间难以两全。研究构建面向水下冲刷场景的 3D 声呐点云深度学习去噪网络，用数据驱动方式区分真实地形特征与噪声点，在保留冲刷坑边缘等关键几何细节的同时显著提升点云质量。该工作把「AI 数据清洗」推进到海洋工程检测的最前端，对水下基础设施巡检的自动化有直接意义。（Automation in Construction）',
     'source': 'Automation in Construction',
     'url': 'https://doi.org/10.1016/j.autcon.2026.107321', 'date': '2026-10-23'},
    {'title': '台风海况下相位解析波浪预报：分层时空深度模型',
     'badge': '[论文]',
     'abstract': '极端海况下的海浪预报是海上作业安全的核心诉求，但台风环境的风场强非线性使常规数值与统计模型都难以兼顾精度与效率。中国海洋大学团队提出分层时空深度学习框架，做相位解析（phase-resolving）的波面时间演进预测：模型按空间尺度分层提取波浪传播特征，在台风过境条件下直接预报波面演化而非仅有效波高。对比常规谱模型，这类数据驱动相位解析方法在保证物理形态的同时大幅降低计算成本，对船体载荷评估与海上施工窗口预报有应用价值。（Ocean Engineering）',
     'source': 'Ocean Engineering',
     'url': 'https://doi.org/10.1016/j.oceaneng.2026.128908', 'date': '2026-10-21'},
    {'title': 'CNN–LSTM 时空预报海岸带状态：Landsat MNDWI 的多时相实践',
     'badge': '[论文]',
     'abstract': '海岸线演化预报在数据稀缺的动态环境中尤为重要。研究以巴西东北部 Icapuí 海岸为对象，构建模块化框架：用多时相 Landsat 影像计算 MNDWI 水体指数得到「海岸带状态」序列，再用 CNN–LSTM 做时空预报，把海岸变化从「事后监测」推进到「短中期预测」。对海岸管理与侵蚀预警而言，这种「遥感指数 + 时空深度学习」的轻量组合在无现场观测的地区尤其可复制。（Earth Science Informatics）',
     'source': 'Earth Science Informatics',
     'url': 'https://doi.org/10.1007/s12145-026-02283-8', 'date': '2026-10-23'},
    ]},
    {'title': '二、海洋数字孪生',
     'en': 'Ocean Digital Twin',
     'items': [
    {'title': '海洋数字孪生如何改写海洋遗传资源数字序列信息的惠益分享？',
     'badge': '[论文]',
     'abstract': '海洋数字孪生（DTO）正在改变海洋遗传资源数字序列信息（DSI on MGRs）的生成与使用方式：模型训练数据、模拟输出与衍生产品的边界越来越模糊，谁「使用」了 DSI、如何计量惠益都变得难以界定。研究系统梳理 DTO 对现行惠益分享机制（含 BBNJ 协定下的 DSI 安排）提出的挑战，并讨论治理应对路径。对关注海洋数据治理与 DTO 建设的机构而言，这是把「技术架构」与「产权/惠益规则」连起来看的重要文本。（Frontiers in Marine Science）',
     'source': 'Frontiers in Marine Science',
     'url': 'https://doi.org/10.3389/fmars.2026.1966759', 'date': '2026-10-20'},
    {'title': 'CORA v2.0 再分析产品评估：首次纳入潮汐强迫后的南海内潮表征',
     'badge': '[论文]',
     'abstract': '中国自主研发的 CORA v2.0 再分析数据集首次纳入显式潮汐强迫，国防科技大学团队据此评估其对南海内潮的表征能力：谱分析提取的内潮信号与锚系浮标观测在精度和强度上高度一致；全日内潮主要向西南传播、耗散缓慢，半日内潮分西北与西南两支且衰减较快；北部内潮夏秋季最强、中南部秋冬季最强，季节差异主要受层结调制。总体上 CORA v2.0 对全日内潮的模拟能力优于半日内潮。作为最早纳入显式潮汐强迫的再分析产品之一，这是国产海洋再分析数据质量的重要佐证。（Acta Oceanologica Sinica）',
     'source': 'Acta Oceanologica Sinica',
     'url': 'https://doi.org/10.1007/s13131-026-2690-6', 'date': '2026-10-24'},
    {'title': '船舶轴系状态评估：实测与数字孪生数据融合驱动的 MLP 方法',
     'badge': '[论文]',
     'abstract': '船舶推进轴系在变工况运行下，尾轴承磨损与基座沉降会重新分配载荷、迁移振动能量并扭曲轴心轨迹，而纯数据驱动模型受限于故障样本稀缺与可解释性不足。研究提出实测与数字孪生数据融合驱动的多层感知机（MLP）状态评估方法：构建几何、物理、规则与行为四层孪体框架，用 Timoshenko 梁有限元加模态截断降低计算成本，以孪体仿真增广稀疏的退化状态样本。该范式为海洋装备的预测性维护提供了「孪生体造样本、实测评判」的可落地路径。（Journal of Marine Science and Engineering，MDPI 集团刊，D 级，供参考）',
     'source': 'Journal of Marine Science and Engineering（MDPI 集团刊，D 级，供参考）',
     'url': 'https://doi.org/10.3390/jmse14211983', 'date': '2026-10-22'},
    ]},
    {'title': '三、海洋可视化',
     'en': 'Ocean Visualization',
     'items': [
    {'title': '3DSeaVizKit：把多学科海洋数据装进浏览器里的交互式三维视图',
     'badge': '[论文]',
     'abstract': '海洋模拟与观测产生的多变量三维场，长期依赖静态二维切面呈现，容易掩盖输运路径与中尺度结构。MIT MSEAS 团队在 Ocean Modelling 发表 3DSeaVizKit：基于 Plotly 的模块化流水线，把标量场（温盐、生物地球化学示踪物）、矢量场（流速、涡度）与拉格朗日产品（轨迹、流图、拉格朗日相干结构）处理成便携的网页交互式三维可视化，并展示了墨西哥湾涡旋相互作用、阿尔沃兰海潜沉过程、马萨诸塞湾生化-酸化耦合等案例。对海洋模式团队而言，这是一条「轻前端、重管线」的可复用可视化路径。（Ocean Modelling / MIT MSEAS）',
     'source': 'Ocean Modelling',
     'url': 'https://doi.org/10.1016/j.ocemod.2026.102841', 'date': '2026-10-15'},
    {'title': 'CHI PLAY 2026：Tidy Tide 用游戏机制做海洋保护科普',
     'badge': '[会议]',
     'abstract': 'ACM 人机交互与游戏年会 CHI PLAY 2026 收录的 Tidy Tide 探索「通过游戏实现海洋保护」：以海洋垃圾清理为核心玩法，把保护行为、反馈循环与叙事机制结合，考察严肃游戏如何影响玩家对海洋环境议题的认知与态度。对海洋科普与公众参与项目而言，游戏化交互是一条被顶会认可的传播路径，也为海洋数据/模拟结果的公众化呈现提供了设计参考。（ACM CHI PLAY 2026）',
     'source': 'ACM CHI PLAY 2026',
     'url': 'https://doi.org/10.1145/3800965.3834276', 'date': '2026-10-22'},
    ]},
    {'title': '四、海洋数据质量',
     'en': 'Ocean Data Quality',
     'items': [
    {'title': '拉格朗日剖面浮标驻留时间评估：自适应停泊深度可延长驻留数倍',
     'badge': '[论文]',
     'abstract': 'Argo 型剖面浮标被动漂移，难以留在目标观测区。研究结合观测与同化再分析流场，量化了浮标在西亚太西边界流复杂动力区的实测与潜在驻留时间（RT）：西边界流内可不足 20 天，副热带流涡内部可超 100 天。简单的「停泊在最小水平流速深度」策略即可让平均 RT 提升数十至数百个百分点，更复杂的方向感知与多次变深策略还能进一步提高。作者强调这类策略适用于任务型浮标与区域观测网，不建议改动维持中深度流速气候记录的核心 Argo 阵列。对区域观测系统设计与数据可用性规划有直接参考。（Earth and Space Science，豁免：10 月上旬在线首发）',
     'source': 'Earth and Space Science',
     'url': 'https://doi.org/10.1029/2026EA005018', 'date': '2026-10-01'},
    ]},
    {'title': '五、海洋数据处理',
     'en': 'Ocean Data Processing',
     'items': [
    {'title': '物理引导的波浪谱反演：一个浮标谱 + 风场即可做 12 小时短程预报',
     'badge': '[论文]',
     'abstract': '波浪谱的短程预报通常依赖完整的数值波浪模式。塔林理工团队的 arXiv 预印本展示了一条极简路线：用循环神经网络仅以一个浮标实测谱做初始化，辅以局地风、风区与水深，即可做 12 小时的实测波浪谱短程反演；训练数据来自波罗的海三个站位（2017–2020 训练、2021 验证、2022 测试），ERA5 提供全程风场。对比不同监督目标发现「谱方差 + 峰频」组合误差最低，叠加经验风浪边界与局地松弛约束可进一步改善。对布有浮标但缺模式支撑的近岸场景，这是低成本的谱级预报方案。（arXiv 预印本）',
     'source': 'arXiv 预印本',
     'url': 'https://arxiv.org/abs/2610.29306', 'date': '2026-10-21'},
    {'title': '海底电缆威胁检测的多源融合：AIS 欺骗不再致命',
     'badge': '[论文]',
     'abstract': '海底电缆监测主要依赖 AIS 自动识别系统，但 AIS 易受欺骗攻击（spoofing），会造成预警失效。研究提出带证据融合的自适应时空图注意力网络（Adaptive Spatio-temporal GAT with Evidence Fusion），把 AIS 轨迹与多源旁证（如雷达/其他传感器证据）融合，识别针对海底电缆的可疑船舶行为，提升欺骗场景下的早期预警稳健性。海底基础设施安全正在成为数据驱动的交叉战场，该模型给出了「多源证据融合 vs 单源依赖」的明确答案。（Discover Artificial Intelligence）',
     'source': 'Discover Artificial Intelligence',
     'url': 'https://doi.org/10.1007/s44163-026-02461-z', 'date': '2026-10-23'},
    {'title': 'DIRECT 1.0：扩散生成模型补全卫星 SST 的云下盲区',
     'badge': '[论文]',
     'abstract': '卫星海表温度（SST）观测常被云层遮挡，而同一稀疏观测可能对应多种合理完整场，确定性方法只能输出过度平滑的单一解。卢布尔雅那大学等团队在 GMD 发表 DIRECT 1.0：条件扩散生成框架（rectified flow matching），以时间上下文与季节相位为条件，从稀疏 L3 观测生成整族物理合理的 SST 场，给出均值重建与空间分辨的不确定性估计；在地中海、亚得里亚海与北大西洋三个数据集上，较此前最强方法 RMSE 降低 6%–14%，且云覆盖变化下保持稳健。模型与代码随文开源。（Geoscientific Model Development，豁免：9 月下旬在线首发，与本期 SST 重建主题直接相关）',
     'source': 'Geoscientific Model Development',
     'url': 'https://doi.org/10.5194/gmd-19-8915-2026', 'date': '2026-09-22'},
    ]},
    {'title': '六、数据管理与共享',
     'en': 'Data Management & Sharing',
     'items': [
    {'title': '末次间冰期海平面代理数据库扩展至南亚与印度洋',
     'badge': '[论文]',
     'abstract': 'ESSD 数据库论文：研究对南亚与印度洋区域（伊朗、阿曼、印度、马尔代夫及科科斯群岛）末次间冰期（132–80 ka）海平面代理指标进行系统整理与关键修订，形成标准化数据库，覆盖地貌与沉积指示物并给出质量评级。这类区域代理数据库是全球冰量-海平面重建与模型比对的底座，也为评估未来百年尺度的冰盖失稳风险提供了「高海平面时期」的历史类比。（Earth System Science Data）',
     'source': 'Earth System Science Data',
     'url': 'https://doi.org/10.5194/essd-18-7627-2026', 'date': '2026-10-20'},
    {'title': 'EMODnet Biology 数据管理方法走进亚得里亚海潟湖项目',
     'badge': '[动态]',
     'abstract': 'EMODnet 发布 10 月 13 日公告：意大利-斯洛文尼亚跨国 BioTiles 项目（保护潟湖生态系统韧性）于 9 月由牵头单位 OGS 组织海洋数据管理与整编培训，向项目成员推广 EMODnet Biology 的数据标准与汇交流程，涵盖数据从采集到入库的完整链路。同月，EMODnet Biology 的 OceanTeacher 课程亦完成改版并新增 DNA 组学数据与缺席数据两章。欧盟各资助项目间的「数据标准输出」正在成为区域海洋数据共享的主通道。（EMODnet）',
     'source': 'EMODnet',
     'url': 'https://emodnet.ec.europa.eu/en/emodnet-biology-approaches-shared-during-biotiles-training-lagoon-biodiversity-data', 'date': '2026-10-13'},
    ]},
    {'title': '七、开放航次与科考',
     'en': 'Open Cruises & Expeditions',
     'items': [
    {'title': 'MBARI 米洛斯岛热液喷口联测：便携 DAS + MOLA AUV 的三维制图组合',
     'badge': '[航次]',
     'abstract': '10 月 15—25 日，MBARI 与雅典大学在希腊米洛斯岛 Paleochori 湾执行 10 天联测，研究浅水热液喷口系统：岸基布设便携式分布式声学传感系统 Geo-Sense，700 米光纤入水至 15 米深，监测气泡喷发的声学事件并估算渗漏速率；同时用便携 MOLA AUV（六自由度矢量推进）对喷口区做高分辨率三维摄影测量制图，辅以 Bubble Cam 立体成像与水听器定量气体渗漏。「光纤阵列 + 自主平台」的组合为浅水海底过程的连续观测提供了低成本样板。（MBARI）',
     'source': 'MBARI',
     'url': 'https://www.mbari.org/expedition/multisensory-milos-3d-mapping-and-monitoring-of-gas-seeps', 'date': '2026-10-15'},
    {'title': '深蓝瞭望第 6 期：无人测量船常态化出海与深水平台「验证季」',
     'badge': '[动态]',
     'abstract': '本期行业观察（10 月 18 日）聚焦「无人」与「深水」：爱尔兰 XOCEAN 的 X-16 无人测量艇自 10 月 16 日起对西部 HVDC 海缆马恩岛以南 127 公里段执行 29 天地球物理复测，搭载多波束与拖曳侧扫声呐、卫星链路回传、岸基远程值守；澳大利亚 Ocius 同日在悉尼启用 Bluebottle 无人艇生产基地。NOAA「Okeanos Explorer」号将于 10 月 28 日—11 月 16 日执行本年度收官技术验证航次 EX2701，重点测试大航程 AUV；OET「Nautilus」号夏威夷群岛深海航次（9 月 22 日—10 月 12 日）刚收官，最深作业 6000 米并试验 Quokka 自主表层 eDNA 采样装置，地质与生物数据全部无限制开放。国内侧，中国海洋大学获批海洋智能感知与微纳生物系统实验室，云洲 L30 巡逻无人艇批量交付，深圳落地首笔把海洋观测数据纳入授信依据的「气候韧性贷」。（水德科技「深蓝瞭望」）',
     'source': '水德科技 · 深蓝瞭望',
     'url': 'http://www.watertools.cn/news/info/502.html', 'date': '2026-10-18'},
    {'title': '多 AUV 协同水下搜救：分区分配 + 自适应覆盖的两级规划',
     'badge': '[论文]',
     'abstract': '多 AUV 水下搜救任务面临区域分配复杂与搜索效率不足的双重挑战。哈尔滨工程大学团队在 Journal of Field Robotics 提出集成方法：改进麻雀搜索算法 + 深度 Q 网络（ISSA-DQN）解决多 AUV 任务分配中的区域连通性与平台异质性问题；多 AUV 边界自适应神经网络覆盖算法（MBANCP）负责分配后的协同覆盖搜索。两级架构把「谁来搜哪里」与「怎么搜」解耦，提升集群整体协同效率，对搜救、测绘与科考作业的自主化有直接借鉴。（Journal of Field Robotics）',
     'source': 'Journal of Field Robotics',
     'url': 'https://doi.org/10.1002/rob.70372', 'date': '2026-10-23'},
    ]},
    {'title': '八、海洋数据中心',
     'en': 'Ocean Data Centers',
     'items': [
    {'title': '海底数据中心的环境账：中国海底算力扩张引发生态之辩',
     'badge': '[动态]',
     'abstract': 'Dialogue Earth 10 月 20 日报道把视线投向中国海底数据中心的生态代价：上海临港海底数据中心（投资 16 亿元）把核心设施沉入海底 10 米，直接接风电、以海水冷却，据称较陆地同等算力省电 18%–28%、每年省下约 4 万吨冷却淡水；海南清水湾一期已连续运行 40 个月「零故障」，二期 30 舱、三期 70 舱在规划中。但专家提醒：废热排放可能对周边无法迁徙的底栖生物产生行为与生理影响，环境影响、透明度与商业可行性都还缺乏独立评估。算力下海的中国路线与韩日新三国的浮式路线正在分岔，环境监管框架明显滞后于部署速度。（Dialogue Earth 经 eco-business 发布）',
     'source': 'Dialogue Earth · eco-business',
     'url': 'https://www.eco-business.com/news/concerns-raised-as-data-centres-go-underwater-in-china/', 'date': '2026-10-20'},
    {'title': '韩华海洋在 Gastech 2026 首秀 60 MW 浮式数据中心，获 ABS 认证',
     'badge': '[动态]',
     'abstract': '据 IT 时代网援引韩国 Chosun 报道：韩国三大船企已全部入局海上算力赛道。韩华海洋在米兰 Gastech 2026 展会首次公开自研的 60 兆瓦级浮式数据中心，获美国船级社（ABS）认证，支持发电与供电方式、服务器类型与容量的模块化定制；三星重工正与美国开发商 Musterian 联合开发 50 MW 级方案，HD 现代重工与施耐德电气启动基础设施技术联研。对比之下，新加坡吉宝 25 MW 级项目已动工、Seatrium 30 MW 级获原则性认可，日本商船三井走「旧船改造」路线。韩媒指出，海上数据中心能否成为造船业新收入源，关键在于稳定性与运行率能否比肩陆上并实现标准化。（IT 时代网 · 经网易转载，原载 Chosun）',
     'source': 'IT 时代网（经网易转载）',
     'url': 'https://dy.163.com/article/L91NHHO805527PMU.html', 'date': '2026-10-12'},
    ]},
    {'title': '九、工具与代码资源',
     'en': 'Tools & Code Resources',
     'items': [
    {'title': 'echoregions 0.2.4：水柱声呐标注与机器学习训练集之间的双向桥梁',
     'badge': '[工具]',
     'abstract': 'NOAA 渔业声学团队维护的 echoregions 于 10 月 10 日发布 0.2.4：解析 Echoview 的 EVR/EVL 标注文件，与 echopype 生成的 xarray 水柱声呐数据集对接，可由人工标注生成 ML 训练掩膜，也可把模型预测转回标注格式供下游生物量估算使用。渔业声学数据的深度学习应用长期受「标注格式私有、与科学数据格式脱节」拖累，该工具把两个生态打通，是声学海洋数据 ML 化的实用基础设施。（PyPI）',
     'source': 'PyPI',
     'url': 'https://pypi.org/project/echoregions/', 'date': '2026-10-10'},
    {'title': 'coastsat-package 0.5.1：SAR 岸线提取进入打包版，光学云遮挡不再是死角',
     'badge': '[工具]',
     'abstract': 'USGS 海岸团队维护的 CoastSat 打包版发布 0.5.1（0.5.0 起新增）：用 U-Net + ResNet-50 的 ONNX 模型对 Sentinel-1 双极化（VV/VH）影像做语义分割提取岸线——SAR 穿云能力让光学影像失效的雨季与高云区也能制图；模型约 130 MB，首次使用自动从 Hugging Face 下载并校验，模型不可用时自动回退经典 Otsu 阈值法不会中断。另改进下载过滤（按月份/云量）、大集合下载与岸线提取报告。对全球海岸线变化监测而言，这是从光学到多源遥感的实用升级。（PyPI / GitHub）',
     'source': 'PyPI',
     'url': 'https://pypi.org/project/coastsat-package/', 'date': '2026-10-09'},
    ]},
]


def main():
    path = 'feishu_write_doc.py'
    with open(path, encoding='utf-8') as f:
        content = f.read()
    new_repr = repr(SECTIONS).replace('\\x27', "'")
    pattern = re.compile(r'SECTIONS = \[.*?(?=\ndef tr\(|\n# ---|\Z)', re.DOTALL)
    content2, n = pattern.subn('SECTIONS = ' + new_repr + '\n\n\n', content, count=1)
    if n != 1:
        raise SystemExit('ERROR: SECTIONS 替换失败 n=%d' % n)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content2)
    total = sum(len(s['items']) for s in SECTIONS)
    dist = ' / '.join('%s%d' % (s['title'][0], len(s['items'])) for s in SECTIONS)
    print('OK: SECTIONS written. Total items: %d (%s)' % (total, dist))


if __name__ == '__main__':
    main()
