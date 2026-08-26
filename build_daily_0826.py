# -*- coding: utf-8 -*-
"""
build_daily_0826.py — 将 2026-08-26 日报 SECTIONS 写入 feishu_write_doc.py
修订版：去除与 08-21/08-24/08-25 重复条目（DLESyM-Ocean/OceanLight/DINOv2声呐/EX2606/Argo GDAC快照/CMEMS 8月更新）
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': 'IJCAI-ECAI 2026 AI4G：#AI4G39 论文提出AI-海洋动力学协同的海洋热极端事件早期预警系统（2026-08-20, Bremen）',
                'badge': '[论文]',
                'abstract': '第35届IJCAI暨第29届ECAI大会（德国不来梅）"AI for Social Good"专题track录用论文《Towards an Early Warning System for Ocean Heat Extremes Through AI-Ocean Dynamics Synergy》（编号#AI4G39，口头报告+海报展示）。该工作针对海洋热浪、ENSO等海洋热极端事件，通过物理信息神经网络（PINN）合成多源观测数据，使预测受基本物理定律约束，可预报事件发生、强度、持续时间和空间范围，并建立专门基准评估预测技巧与归因可靠性。引入增量学习机制持续适应长期气候演变，为政策制定与海洋决策提供可靠、可解释、自适应的预警工具。',
                'source': 'IJCAI-ECAI 2026 AI4G Special Track（Bremen）',
                'url': 'https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-social-good',
                'date': '2026-08-20',
            },
            {
                'title': '世界模型接地LLM规划用于AUV/ASV近海风电场导航：GazeboSim误差降70-93%（arXiv, 2026-08-20, IEEE IROS 2026录用）',
                'badge': '[论文]',
                'abstract': '大语言模型可将自然语言任务转化为机器人动作序列，但缺乏物理感知。本文提出世界模型（World Model）扩展LLM规划能力的三组件框架：物理约束神经世界模型、三阶段梯度轨迹优化器、带信任域保护的MPC式闭环重规划器——LLM决定"做什么"，世界模型决定"做多久"。在近海风电场场景对6自由度AUV与3自由度差速ASV进行5项基准任务评估，两平台全部达成目标且预测零碰撞；迁移至含海流、波浪与推进器动力学的GazeboSim仿真后，目标距离误差较无物理基础基线降低70-82%（ASV）和约93%（AUV）。ASV端还展示了VLM辅助语义建图管线，从卫星影像、海图与预报API提取障碍物与环境上下文，导航精度达96%。',
                'source': 'arXiv / cs.RO（IEEE IROS 2026 AQ2UASIM Workshop）',
                'url': 'https://arxiv.org/abs/2608.19661',
                'date': '2026-08-20',
            },
            {
                'title': '利用历史稀疏点标注驱动底栖影像密集分割：SAM2点提示过滤机制（arXiv, 2026-08-18）',
                'badge': '[论文]',
                'abstract': '海洋生态系统健康是全球环境变化的关键指标，但水下观测的物理限制与海洋影像处理的内在困难严重制约系统化监测的规模化。研究团队提出弥合SAM系列视觉基础模型与现有稀疏监督之间的鸿沟：历史底栖调查通常每张影像仅有少量专家稀疏点标注，该方法将这些遗留点标签作为SAM2的视觉提示，并创新性地提出自动识别哪些点适合传播、哪些点会带来危害的机制——通过过滤不可靠点，提取高质量伪真值掩码，用于训练更精确的细粒度语义分割模型。在公开底栖数据集上验证有效性，并发布包含真实世界稀疏专家标注的新挑战性基准，为可扩展的生态分析铺平道路。',
                'source': 'arXiv / cs.CV（Univ. Washington等）',
                'url': 'https://arxiv.org/abs/2608.17561',
                'date': '2026-08-18',
            },
            {
                'title': '生成式资料同化揭示锋面是海洋能量级联的关键调控者（arXiv, 2026-08-15, 审稿中Comms Earth&Environment）',
                'badge': '[论文]',
                'abstract': '中尺度涡旋是海洋环流的基础，但亚中尺度运动（数公里尺度）如何通过动能级联影响中尺度涡旋能量学仍不确定。本文通过将多源卫星观测与生成式深度学习框架相结合，重建无缝隙、公里级分辨率的海表流场，绘制海洋亚中尺度能量级联图谱。应用于涡旋丰富的Agulhas流系发现：亚中尺度在10km以上通过上尺度级联为中尺度供能，贡献中尺度涡旋的季节性；10km以下亚中尺度锋面的辐合驱动向下尺度级联直至耗散。上、下尺度两条路径均集中于锋面内，跨尺度能量输运效率高一个数量级。尽管锋面区域有限，却承担了区域积分级联的相当份额，确立其为下一代涡旋参数化的关键目标。',
                'source': 'arXiv / physics.ao-ph（Caltech等，审稿中）',
                'url': 'https://arxiv.org/abs/2608.14955',
                'date': '2026-08-15',
            },
            {
                'title': '浑浊水下图像分割噪声与不确定性的多标注者研究：超100名参与者（arXiv, 2026-08-15, ECCVW 2026 Marine Vision录用）',
                'badge': '[论文]',
                'abstract': '标注不确定性与标注者分歧是计算机视觉的常见挑战，但相关研究多局限于医学领域或通用图像识别数据集。水下数据集因需要领域专家知识、能见度退化以及难以建立可靠真值而尤为脆弱，但水下标注不确定性此前几乎未被探索。本文开展了首个针对真实水下场景分割的系统性多标注者研究：超过100名参与者在不同受控浑浊度水平下进行标注，证明水下数据集面临与其他视觉任务类似的标注挑战，而浑浊度会引入额外的系统性误差。研究进一步分析了驱动标注噪声的主要因素，并探索了改善浑浊水下标注质量的方法（特权信息、个体努力、标注者集成）。全部（元）数据将公开于项目主页。',
                'source': 'arXiv / cs.CV（Aalborg University，ECCVW 2026 第2届Marine Vision研讨会）',
                'url': 'https://arxiv.org/abs/2608.15363',
                'date': '2026-08-15',
            },
        ],
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': 'Digital Twins of the Ocean：架构、使能技术与挑战综述（Ocean-Land-Atmosphere Research, 2026-08-17）',
                'badge': '[论文]',
                'abstract': '发表在OLAR（Science Partner Journal）的综述论文系统梳理近二十年海洋数字孪生（DTO）技术：从"数字海洋"（数据基础设施）到"透明海洋"（3D观测与实时预报框架）再到"智能海洋"（AI驱动预测与决策支持）的演进脉络。DTO系统架构一般包含4层：物理实体层、数据层、模型层与可视化层，由海洋物联网、大数据、人工智能、预测模型、高性能计算与可视化技术支撑。核心功能包括与海洋环境实时同步（what-now）、高精度预报（what-next）与"what-if"情景模拟。论文指出当前面临数据稀疏、缺乏标准化、数字素养差距等挑战，并梳理了区域与国际倡议，为DTO从概念走向业务化提供路线图。',
                'source': 'Ocean-Land-Atmosphere Research (OLAR) Vol.5, DOI: 10.34133/olar.0160',
                'url': 'https://spj.science.org/doi/10.34133/olar.0160',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': 'NERACOOS推出新版Mariner\'s Dashboard beta：区域海洋数据一站式可视化（IOOS, 2026-08-25）',
                'badge': '[动态]',
                'abstract': '美国东北区域沿海海洋观测系统（NERACOOS）发布升级后的 Mariner\'s Dashboard beta 版本，响应用户与利益相关方反馈进行交互优化。该仪表板整合浮标地图最受用户喜爱的组件与站点其他核心功能，将当前实况、观测、后报和预报集成于单一面板，用户无需访问多个页面即可获取完整信息。点击地图点位可查看该资产最新记录，右侧表格始终显示最新观测，下方图表展示12小时趋势，并支持7天历史与预报标签页切换。为美国东北部海域航运、渔业和防灾决策提供一体化数据可视化入口。',
                'source': 'NERACOOS / IOOS Newsletter',
                'url': 'https://mariners.neracoos.org/',
                'date': '2026-08-25',
            },
            {
                'title': 'IOOS Model Viewer新增USF西佛罗里达沿海海洋模型WFCOM预报图层（IOOS, 2026-08-25）',
                'badge': '[动态]',
                'abstract': '美国综合海洋观测系统（IOOS）在8月通讯中宣布，南佛罗里达大学（USF）西佛罗里达沿海海洋模型（WFCOM）的海流、温度、盐度预报现已可通过IOOS Model Viewer在线查看。该模型覆盖墨西哥湾东部的西佛罗里达陆架，为区域渔业、航运和灾害响应提供高分辨率海洋状态预报的可视化入口。IOOS Model Viewer作为跨区域海洋模型聚合可视化平台，持续扩展东南沿海区域预报能力的开放访问。同期，五大湖WebCOOS网络新增两处近实时海岸网络摄像头（绿湾河口与印第安纳沙丘州立公园），进一步丰富海岸观测可视化。',
                'source': 'IOOS Eyes on the Ocean Newsletter（2026-08）',
                'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-august-2026/',
                'date': '2026-08-25',
            },
        ],
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality",
        "items": [
            {
                'title': '中大西洋高频雷达数据质量显著提升：SeaSonde R25更新引入自动质控（IOOS, 2026-08-25）',
                'badge': '[动态]',
                'abstract': 'IOOS中大西洋高频雷达（HFR）网络在安装 SeaSonde Radial Suite R25 更新后实现数据质量显著提升。新版软件引入新的自动质量控制功能：自动剔除离群速度并标记可疑数据，并在排查中发现并解决了天线与频率调谐问题，进一步提升数据精度并扩大有效覆盖范围。该更新还暴露了此前未被发现的多站点天线/频率配置问题并逐一修复。IOOS HFR国家网络的数据贡献者可免费升级其站点软件。这一案例展示了软件级自动QC在岸基海洋观测网络质量保障中的直接价值。',
                'source': 'IOOS Eyes on the Ocean Newsletter（2026-08）',
                'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-august-2026/',
                'date': '2026-08-25',
            },
        ],
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': '本周暂无明显新进展（CMEMS 2026年8月产品更新 08-25 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据处理方向近一周无独立的新方法或新流程发布。CMEMS 2026年8月产品路线图更新（北极潮汐3km新数据集、北极多年度波浪后报扩展至1960年、波罗的海测深更新、北极BGC中尺度浮游动物垂直迁移模拟等）已在08-25日报完整收录，本期不重复。SWOT尺度分离资料同化（Ocean Modelling, 10月卷）为高质量候选，但正式在线发表日期尚无法核实，留待后续确认后收录。',
                'source': '-',
                'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information?roadmap_category=product',
                'date': '2026-08-26',
            },
        ],
    },
    {
        "title": "六、海洋数据管理与共享",
        "en": "Ocean Data Management & Sharing",
        "items": [
            {
                'title': 'PANGAEA完成元数据架构现代化：移除XML遗留兼容元素，服务基础设施全面切换（2026-08-17）',
                'badge': '[数据]',
                'abstract': '地球科学数据出版平台PANGAEA于8月17日宣布完成数据库架构现代化转型的最后一步：基于XML的原生PANGAEA元数据模式中的全部废弃元素已从服务基础设施中移除，自即日起新增和更新的数据集不再包含"向后兼容元素"，并在未来数周内重构大小信息以更好报告数据矩阵与二进制附件规模。此次元数据清理是PANGAEA数月架构迁移的收官动作，旨在支撑跨学科全球研究社区对元数据标准化、可追溯性的更高要求，为海洋与极地数据集的长期可发现性与可复用性提供基础设施保障。',
                'source': 'PANGAEA Data Publisher',
                'url': 'https://pangaea.de/',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Research Expeditions",
        "items": [
            {
                'title': '第10次中俄海洋联合科考航次起航：62天西北太平洋-东北冰洋多要素综合调查（2026-08-20）',
                'badge': '[航次]',
                'abstract': '8月20日，第10次中俄海洋联合科考航次从俄罗斯符拉迪沃斯托克港起航。航次由自然资源部第一海洋研究所、山东科技大学与俄罗斯科学院远东分院太平洋海洋研究所联合组织实施，调查船为俄罗斯"拉夫任捷夫院士号"，中俄双方25名科学家参航，海上作业周期62天。本航次将在西北太平洋和东北冰洋典型海域开展多要素海洋环境综合调查，旨在揭示快速变化背景下研究区海洋环境对气候变化的响应过程与反馈机理。山东科技大学海洋学院教授石洪华担任共同首席科学家，重点围绕"冰上丝绸之路"典型海域生态系统健康时空演变与驱动机制开展现场调查，为北冰洋生态保护提供基础支撑。',
                'source': '澎湃新闻 / 青岛日报（观海新闻）',
                'url': 'https://www.thepaper.cn/newsDetail_forward_33834636',
                'date': '2026-08-20',
            },
            {
                'title': '库克群岛政府为Okeanos Explorer举行正式欢迎仪式：EX2605航次确认多处意外多金属结核场（2026-08-17）',
                'badge': '[航次]',
                'abstract': '8月17日，库克群岛政府在拉罗通加阿瓦蒂乌港举行正式仪式，欢迎NOAA船Okeanos Explorer完成2026年库克群岛ROV探险（EX2605，7月19日至8月13日）。该航次完成14次ROV下潜、采集400余份样本，并确认了科学家此前未预期到的多处大面积多金属结核场，收集23个疑似新种的生物标本。总理布朗表示"小国最大的优势不是海洋面积，而是理解海洋的自信"，强调库克岛民不仅参与观测，更参与制定研究优先事项。美国宣布将通过新西兰大使馆在库克群岛设立NOAA科学研究员职位，超6万人观看了航次直播。',
                'source': 'Cook Islands Seabed Minerals Authority',
                'url': 'https://www.sbma.gov.ck/news-3/article-279',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': '本周暂无明显新进展（GEBCO_2026 WMS、Argo GDAC快照 08-25 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据中心方向近一周无重大新发布。GEBCO_2026网格WMS图层上线（08-04收录）、Argo GDAC 2026-08-08全球快照（08-08收录）、PANGAEA元数据架构更新（本期收录于数据管理方向）均已覆盖。CMEMS 8月产品更新（本期收录于数据处理方向关注项）为近期主要动态。',
                'source': '-',
                'url': 'https://argo.ucsd.edu/data/argo-data-management/',
                'date': '2026-08-26',
            },
        ],
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources",
        "items": [
            {
                'title': 'uxarray v2026.08.0发布：球面几何EFT补偿算术+自定义错误类型+面面积向量化（2026-08-18）',
                'badge': '[工具]',
                'abstract': '非结构化网格气候与全球天气数据分析的Xarray扩展库uxarray发布v2026.08.0版本。核心更新包括：(1)引入基于误差自由变换（EFT）的补偿算术，显著改善球面几何中GCA相交、点-面测试和面部边界在近退化构型下的数值鲁棒性；(2)全面清理和向量化face_areas API，恢复calculate_total_face_area的缓存快速路径；(3)建立专用异常层次结构，替代代码库中误导性和不一致的错误类型。此外修复了calculate_face_area中的雅可比矩阵错误、拓扑聚合中坐标属性保留等问题，并提升文档对新手的友好度。',
                'source': 'UXARRAY / GitHub / conda-forge',
                'url': 'https://github.com/UXARRAY/uxarray/releases/tag/v2026.08.0',
                'date': '2026-08-18',
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
