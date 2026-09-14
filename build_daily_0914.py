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
                'abstract': '极端海洋热浪（MHW）对海洋生态系统有深远影响，精准预报具有重要科学与经济价值。清华大学地球系统科学系 SAIL 团队在 KDD 2026 AI for Sciences Track 作口头报告，提出 Ocean-E2E——混合物理与数据驱动的全球 MHW 预报框架。该框架基于 MHW 物理本质，显式建模海洋中尺度平流与海气相互作用（动态核），实现端到端数据同化与区域高分辨率预测，可完全脱离数值模式独立运行。实验表明 Ocean-E2E 在全球至区域、短期至长期（1-40 天）预报中均优于当前最先进的海洋数值/AI 预报-同化模型，尤其在最极端 MHW 事件上表现突出。代码已在 GitHub 开源。',
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
                'title': 'DTF-Net：双轨信息融合网络实现无邻站条件下海洋浮标风数据深度学习质量控制（JMSE, 2026-08-07）',
                'badge': '[论文]',
                'abstract': '海洋浮标风数据质量控制传统依赖邻站空间验证，但稀疏观测网络中物理邻站往往不可用。自然资源部北海预报减灾中心提出 DTF-Net（Dual-Track Information Fusion Network），通过时间轨提取风速局部时序变化特征、全局轨挖掘温度-气压-风向等多要素物理耦合关系，在无邻站条件下实现多维度协同异常检测。结合动态三倍标准差尖峰检测与基于深度学习预测的 3δ-RMSE 空间验证，1 h/12 h/24 h 风速预报 MAE 分别为 0.217、0.398、0.462，较 AutoFormer/ITransformer/FiLM 降低 3.8-61.3%。异常检出率 0.33-9.20%，可有效识别浮标维护期、设备故障和短临天气过程中的数据异常。',
                'source': 'J. Mar. Sci. Eng. 2026, 14(16), 1453（自然资源部北海预报减灾中心）',
                'url': 'https://www.mdpi.com/2077-1312/14/16/1453',
                'date': '2026-08-07',
            },
            {
                'title': '区分传感器异常与区域海洋事件：机器学习辅助、物理引导的事件保留型海岸浮标温度 QC 框架（JMSE, 2026-08-08）',
                'badge': '[论文]',
                'abstract': '海岸上升流和台风混合可在数小时内使浮标温度下降数度，传感器故障也是如此——仅按残差大小标记异常的 QC 方案可能误删真实事件。韩国国立水产科学院与江原大学提出一种机器学习辅助、物理引导、事件保留的 QC 框架，分析韩国东海岸 6 个浮标 3 层深度 2008-2024 年的 30 分钟温度记录。该框架使用三个物理可解释轴（邻站空间一致性、层间垂直一致性、ERA5+台风最佳路径大气强迫）分类冷却事件。残差大小区分传感器异常与区域事件能力差（AUC 0.52-0.56），而物理轴分离度极高（多变量交叉验证平均 AUC 0.987）。框架保留区域事件候选，对月均值影响≤0.0005°C，但保留达 8°C 的事件尺度冷却。',
                'source': 'J. Mar. Sci. Eng. 2026, 14(16), 1462（韩国国立水产科学院 + 江原大学）',
                'url': 'https://www.mdpi.com/2077-1312/14/16/1462',
                'date': '2026-08-08',
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
                'abstract': 'EMODnet Biology 发布了关于北海荷兰部分底拖网捕捞对底栖动物影响的新数据产品。底层渔业是全球食品供应的重要贡献者，但也显著影响海洋生态系统功能——渔具与海底的物理接触会导致沉积物变化和底栖生物直接死亡。该数据产品应用了渔业影响模型于底栖动物群，评估拖网捕捞的生态影响，为渔业影响评估和管理提供数据支撑。该产品通过 EMODnet 地图查看器可视化，体现了 EMODnet 在支持基于生态系统的渔业管理方面的持续贡献。',
                'source': 'EMODnet Biology',
                'url': 'https://emodnet.ec.europa.eu/en/',
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
                'abstract': '向阳红 10 号科考船自 8 月 10 日起航赴西太平洋开展海底热液区联合科学考察。该航次由清华大学、青岛海洋地质研究所和上海交通大学联合组织，聚焦西太平洋海底热液系统的地质、化学与生物综合调查，包括热液喷口定位、流体采样、生物群落调查及海底地形测绘。航次于 9 月 11 日获媒体报道，是多方联合开展深海热液区科考的典型案例，对理解海底热液系统的成矿过程、极端环境生物多样性和深海生态系统功能具有重要意义。',
                'source': '新华社 / 青岛海洋地质研究所',
                'url': 'https://www.mnr.gov.cn/dt/hy/202609/t20260911_2830895.html',
                'date': '2026-09-11',
            },
            {
                'title': '第 16 次北冰洋考察：雪龙 2 号为法国塔拉极地站破冰引航 110 海里，中法北极科考合作深化（2026年9月）',
                'badge': '[航次]',
                'abstract': '中国第 16 次北冰洋科学考察中，"雪龙 2"号破冰船为法国塔拉极地站（Tara Polar Station）执行破冰引航任务，在北冰洋冰区开辟航道 110 海里，保障法方科考平台的安全航行与定位。此次中法北极科考合作展示了国际极地科学考察的协同精神，也体现了"雪龙 2"号的双向破冰能力在极地后勤保障中的关键作用。该任务与 9 月初雪龙 2 号冰站作业和无人机浮标投放（已见于前期简报）属同一次考察的不同任务阶段，但破冰引航法国极地站是本次考察的新亮点。',
                'source': '新华社 / 自然资源部',
                'url': 'https://www.mnr.gov.cn/dt/hy/202609/t20260911_2830896.html',
                'date': '2026-09-11',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': 'EMODnet 数据吸纳服务新阶段启动：CMCC 牵头，聚焦蓝经济与公民科学数据纳入（EMODnet, 2026-08-31）',
                'badge': '[动态]',
                'abstract': 'EMODnet 数据吸纳服务（Data Ingestion, DI）于 2026 年夏季启动新阶段，由意大利 CMCC 牵头的更新联盟负责。新阶段延续现有服务的同时，基于"EMODnet Vision 2035"战略推进数据吸纳服务的战略性演进。未来 DI 将重点关注吸纳来自蓝经济与更广泛私营部门、海岸与海洋开发许可活动、公民科学及其他代表性不足的公共来源和新兴观测系统的数据。这标志着 EMODnet 从国家海洋数据中心（NODC）为主的传统管道向更包容、更多元化数据提供者扩展，是欧洲海洋数据基础设施向全域覆盖的重要一步。',
                'source': 'EMODnet',
                'url': 'https://emodnet.ec.europa.eu/en/',
                'date': '2026-08-31',
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
