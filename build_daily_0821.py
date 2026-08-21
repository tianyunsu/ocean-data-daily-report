# -*- coding: utf-8 -*-
"""
build_daily_0821.py — 将 2026-08-21 日报 SECTIONS 写入 feishu_write_doc.py
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': 'OceanLight：几何自适应非结构化网格表示的全球海洋智能预报框架（arXiv, 2026-08-17）',
                'badge': '[论文]',
                'abstract': '国防科技大学团队提出 OceanLight 高效全球海洋预报框架：将几何自适应非结构化网格分词与图神经网络（GNN）主干创新结合，在陆海掩码单元上避免无效计算，并按局部流动复杂度自适应分配网格分辨率。逐点预报精度与动能谱保真度超越业务化数值分析与现有AI模型，地转平衡一致性优于全部AI海洋模型，且能可靠刻画中尺度涡等相干结构；相较结构化网格基线，GPU显存消耗降低62%、FLOPs降低70%，为非结构化数据驱动海洋学建立了可推广范式。',
                'source': 'arXiv / cs.LG（国防科技大学）',
                'url': 'https://arxiv.org/abs/2608.16070',
                'date': '2026-08-17',
            },
            {
                'title': '退化感知跨模态融合：基础模型+声呐提升水下机器人退化视觉感知（arXiv, 2026-08-20）',
                'badge': '[论文]',
                'abstract': '该研究系统考察水下视觉质量退化时预训练视觉基础模型表征能否被声呐信息有效补充：以冻结 DINOv2 为视觉编码器，构建从清晰到极端退化的五级受控基准，比较传统检测、基础模型表征、声呐上下文、固定多模态融合与退化感知门控融合。极端联合退化下，退化感知视觉-声呐融合将 DINOv2 基线的平衡准确率从 0.4610 提升至 0.6152（相对提升33.5%），声呐贡献权重随退化程度从14.2%自适应升至41.3%，表明显式按模态可靠性自适应融合是提升水下多模态感知鲁棒性的关键。',
                'source': 'arXiv / cs.CV',
                'url': 'https://arxiv.org/abs/2608.19710',
                'date': '2026-08-20',
            },
            {
                'title': 'Dynamic SpectraFormer：超高清水下图像增强的频域Transformer（arXiv, 2026-08-19）',
                'badge': '[论文]',
                'abstract': '东京大学团队针对水下图像低频频段（颜色/亮度畸变）与高频频段（边缘/纹理损失）混合畸变难以同时矫正的问题，提出频域Transformer Dynamic SpectraFormer：超高分辨率稀疏频谱注意力模块在保持万能逼近能力的同时捕获长程依赖，动态频谱权重生成层作为自适应频带选择器强化关键频带、抑制无关频带，显著提升水下图像质量。多基准消融与对比实验验证了其对AUV/海洋机器人视觉作业的支持价值，源码已开源。',
                'source': 'arXiv / cs.CV（东京大学）',
                'url': 'https://arxiv.org/abs/2608.18662',
                'date': '2026-08-19',
            },
            {
                'title': 'MHE：基于到达时间差测量的水下目标跟踪移动时域估计（arXiv, 2026-08-17, IFAC WC 2026）',
                'badge': '[论文]',
                'abstract': '里斯本大学团队研究基于到达时间差（TDoA）的水下目标跟踪的移动时域估计（MHE）方法：针对非线性目标动力学与稀疏声学观测下经典递归滤波（如EKF）可靠性不足的问题，利用多步轨迹耦合与物理一致约束提升估计鲁棒性。2D海洋环境仿真表明MHE在EKF失效场景下仍能保持可靠跟踪，为基于TDoA的多智能体水下跟踪系统提供了实用可扩展的构建模块。（IFAC WC 2026录用）',
                'source': 'arXiv / eess.SY（里斯本大学）',
                'url': 'https://arxiv.org/abs/2608.16024',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': '本周暂无明显进展（日照港数字孪生 08-14 已收录；DITTO Summit 早鸟 07-30 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数字孪生方向近一周无重大新平台或新框架发布。山东港口日照港集装箱数字孪生系统（08-14收录）、DITTO Summit 2026 早鸟注册（07-30收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://ditto-oceandecade.org/',
                'date': '2026-08-21',
            },
        ],
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': '本周暂无明显进展（MyOcean Health 07-01、WavyOcean 3.0 07-13 已收录）',
                'badge': '[关注]',
                'abstract': '海洋可视化方向近一周无重大新工具或平台发布。Copernicus MyOcean Health（07-01收录）、香港科技大学 WavyOcean 3.0（07-13收录）、CMEMS MyOcean Pro 3D路线图（08-03收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://myocean.marine.copernicus.eu/',
                'date': '2026-08-21',
            },
        ],
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality",
        "items": [
            {
                'title': '本周暂无明显进展（DTF-Net 风数据QC 08-07 已收录；BGC-Argo CHLA再处理 07-11 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据质量方向近一周无重大新方法或新进展发布。DTF-Net 深度学习风数据质控（08-07收录）、BGC-Argo CHLA 首次大规模再处理（07-11收录）、ML辅助事件感知QC框架（08-08收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://biogeochemical-argo.org/',
                'date': '2026-08-21',
            },
        ],
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': 'OceanDepths：全球表层-次表层配对海洋观测AI-ready数据集（arXiv, 2026-08-17）',
                'badge': '[数据]',
                'abstract': 'ESA与学者联合发布 OceanDepths——首个开放、全球、重网格化的AI-ready海洋数据集：将卫星导出的海表温度（SST）、海表盐度（SSS）、海面高度（SSH）L4产品与EN4次表层温盐剖面配对（0.1°×0.1°、周尺度、2000-2024），并补充GLORYS12再分析数据以支持对比或多阶段学习。数据集含超950万条插值到50个标准深度层的配对剖面，次表层观测稀疏度约0.01%/层，可作为次表层状态重建、基于观测的预报方法等的标准测试床，填补了卫星-原位配对AI数据集空白。',
                'source': 'arXiv / cs.LG（ESA等）',
                'url': 'https://arxiv.org/abs/2608.16373',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "六、海洋数据管理与共享",
        "en": "Ocean Data Management & Sharing",
        "items": [
            {
                'title': 'EMODnet 第24届指导委员会（2026夏季）会议纪要发布（2026-08-03，豁免18天）',
                'badge': '[动态]',
                'abstract': '欧洲海洋观测与数据网络（EMODnet）发布第24届指导委员会（2026夏季）会议纪要与演示文稿（8月3日）。会议围绕欧洲海洋数据基础设施演进、与欧洲数字孪生海洋（EDITO）及哥白尼海洋服务的协同、海洋数据空间建设等议题展开，是EMODnet作为欧盟原位海洋数据核心服务的重要治理节点更新。（发布18天，重要国际数据基础设施动态，豁免收录）',
                'source': 'EMODnet / 欧盟海事论坛',
                'url': 'https://maritime-forum.ec.europa.eu/24th-emodnet-steering-committee-summer-2026-meeting-minutes-and-presentations_en',
                'date': '2026-08-03',
            },
        ],
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Research Expeditions",
        "items": [
            {
                'title': 'E/V Nautilus NA181 威克岛深海探索正式启航，30天远征太平洋（2026-08-20，更新）',
                'badge': '[航次]',
                'abstract': '海洋探索信托（OET）的 E/V Nautilus 于8月20日正式启航 NA181"Exploration of Wake Island\'s Deep Sea"航次（8月20日至9月18日），从关岛出发前往威克岛周边太平洋岛遗产海洋国家保护区。30天航次将利用ROV Hercules、多波束测深与远程呈现系统，探索海山、深渊平原以及与威克岛战役相关的海洋遗产遗址——该区域约40.7万平方公里海床大部分从未测绘，是美属管辖下勘测最薄弱的区域之一；航次还将在全球海洋生物地球化学阵列中布放少量Argo浮标。（更新：NA181 由预告转为正式启航）',
                'source': 'Ocean Exploration Trust / AZPM',
                'url': 'https://www.azpm.org/p/headlines/2026/8/20/230902-tucsonan-leaves-for-expedition-of-rarely-explored-parts-of-the-pacific-ocean',
                'date': '2026-08-20',
            },
            {
                'title': 'NOAA Okeanos Explorer EX2607 美属萨摩亚测绘航次预告（2026-09-23起）',
                'badge': '[航次]',
                'abstract': 'NOAA 海洋探索计划公布 2026 年美属萨摩亚测绘航次（EX2607）：9月24日至10月19日，Okeanos Explorer 自斐济苏瓦出发、终抵夏威夷檀香山，开展全天候多波束测绘作业，覆盖海床、水柱与次海床，重点补测美属萨摩亚周边（含罗斯环礁海洋国家保护区等）海床测绘数据空白。该航次与 8-9 月 EX2606 ROV 航次共同构成 NOAA 2026 美属萨摩亚 ROV+测绘组合任务，数据将为海床关键矿产评估与资源管理提供支撑。',
                'source': 'NOAA Ocean Exploration / NOAA News',
                'url': 'https://www.noaa.gov/news-release/noaa-and-partners-to-explore-map-deep-waters-of-american-samoa',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': '本周暂无明显进展（GEBCO_2026 WMS 08-04 已收录；CMEMS 8月北极产品路线图待发布）',
                'badge': '[关注]',
                'abstract': '海洋数据中心方向近一周无重大新发布。GEBCO_2026 网格 WMS 图层上线（08-04收录）、CMEMS 8月北极潮汐3km产品（路线图标注 Aug 2026，尚无精确发布日期）已纳入跟踪，本期不重复收录。',
                'source': '-',
                'url': 'https://seabed2030.org/',
                'date': '2026-08-21',
            },
        ],
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources",
        "items": [
            {
                'title': '本周暂无明显进展（gridstats v2.6.0 08-12、wavespectra 5.0 预告 08-10 已收录）',
                'badge': '[关注]',
                'abstract': '海洋工具与代码资源方向近一周无重要新版本或新开源项目发布。gridstats v2.6.0（08-12收录）、wavespectra v5.0 架构升级预告（08-10收录，实测 PyPI 最新仍为 v4.8.0）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://github.com/topics/oceanography',
                'date': '2026-08-21',
            },
        ],
    },
]

# 读入 feishu_write_doc.py 并替换 SECTIONS
DATA_SOURCE = r'C:\Users\Administrator\WorkBuddy\20260327163052\ocean-data-daily-report\feishu_write_doc.py'
with open(DATA_SOURCE, encoding='utf-8') as f:
    content = f.read()

new_block = 'SECTIONS = ' + repr(SECTIONS)
pattern = re.compile(r'SECTIONS = \[.*?\]\n', re.S)
if pattern.search(content):
    content = pattern.sub(new_block + '\n', content, count=1)
else:
    raise RuntimeError('未找到 SECTIONS 占位')

with open(DATA_SOURCE, 'w', encoding='utf-8') as f:
    f.write(content)

n_items = sum(len(s['items']) for s in SECTIONS)
print(f'OK: SECTIONS 已写入, {len(SECTIONS)} 方向, {n_items} 条')
