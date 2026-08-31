# -*- coding: utf-8 -*-
"""
build_daily_0831.py — 将 2026-08-31 日报 SECTIONS 写入 feishu_write_doc.py
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': 'AquaFlow：单目3D高斯溅射SLAM水下流式重建框架（arXiv, 2026-08-25）',
                'badge': '[论文]',
                'abstract': '浙江大学、上海人工智能实验室、上海交通大学、清华大学等六机构联合提出 AquaFlow，面向水下场景的单目3D高斯溅射（3DGS）流式重建框架：先在大规模水下数据上微调3D视觉基础模型以获取鲁棒的相机位姿与点图估计，再通过介质引导的增量高斯初始化将新帧可靠区域加入场景，并构建融合结构化距离条件神经高斯与物理光学模型的混合场景表示，补偿水下成像衰减与散射。在62条水下轨迹（公开基准+网络视频）上，平均定位误差较 WaterSplat-SLAM 降低13.2%、PSNR提高4.74 dB，为水下实时三维重建与SLAM提供新工具。',
                'source': 'arXiv / cs.CV（浙大+上海AI实验室等）',
                'url': 'https://arxiv.org/abs/2608.22906',
                'date': '2026-08-25',
            },
            {
                'title': 'NemoSplat：前馈4D高斯溅射的介质感知水下动态重建（arXiv, 2026-08-24）',
                'badge': '[论文]',
                'abstract': '香港科技大学与北京理工大学团队提出 NemoSplat——首个面向无标定海洋视频的前馈4D高斯溅射介质感知动态重建框架：可提示动态解缠器（Promptable Dynamic Disentangler）利用置信感知融合与语义文本先验隔离海量瞬态物体，介质感知高斯预测器联合估计3D高斯属性与物理介质参数，单次前向即可恢复纯净场景外观；同时构建含大规模动态元素的水下数据集用于训练与评估，实现SOTA级跟踪精度与高保真渲染，为水下动态场景重建与海洋生态监测提供支撑。',
                'source': 'arXiv / cs.CV（香港科技大学+北理工）',
                'url': 'https://arxiv.org/abs/2608.22888',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': '本周暂无明显进展（日照港数字孪生 08-14、OLAR DTO综述 08-17 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数字孪生方向近一周无重大新平台或新框架发布。山东港口日照港集装箱数字孪生系统（08-14收录）、OLAR DTO四层架构综述（08-17收录）、WavyOcean 3.0（07-13收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://www.edito.eu/',
                'date': '2026-08-31',
            },
        ],
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': '本周暂无明显进展（MyOcean Health 07-01、MyOcean Pro 3D 08-03 已收录）',
                'badge': '[关注]',
                'abstract': '海洋可视化方向近一周无重大新工具或平台发布。Copernicus MyOcean Health（07-01收录）、MyOcean Pro 3D可视化路线图（08-03收录）、IOOS Model Viewer WFCOM（08-25收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://data.marine.copernicus.eu/',
                'date': '2026-08-31',
            },
        ],
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality",
        "items": [
            {
                'title': '本周暂无明显进展（DTF-Net 08-07、ML辅助事件感知QC 08-08 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据质量方向近一周无重大新方法或新进展发布。DTF-Net 深度学习风数据质控（08-07收录）、ML辅助事件感知QC框架（08-08收录）、中大西洋HFR SeaSonde R25自动QC（08-25收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://www.euro-argo.eu/',
                'date': '2026-08-31',
            },
        ],
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': 'BenthicFlow：基于流匹配生成可扩展水下底栖3D环境（arXiv, 2026-08-24, ECCV 2026 Marine Vision）',
                'badge': '[论文]',
                'abstract': '埃因霍温理工大学团队提出 BenthicFlow——基于单一条件流匹配模型的水下3D底栖环境生成框架：联合生成对齐的纹理与深度图，通过受MultiDiffusion启发的采样过程在生成轨迹中协调重叠窗口，无需独立拼接模型即可生成空间可扩展的RGBD镶嵌图，再经表面对齐高斯曲面元提升为显式3D底栖环境。在不同地理位置的勘测站点上保持站点特定外观并生成连贯的大规模3D场景，为缺乏高质量3D数据的水下场景理解提供数据域弥合新路径，已录用 ECCV 2026 海洋视觉研讨会。',
                'source': 'arXiv / cs.CV（埃因霍温理工大学, ECCV 2026）',
                'url': 'https://arxiv.org/abs/2608.23173',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "六、海洋数据管理与共享",
        "en": "Ocean Data Management & Sharing",
        "items": [
            {
                'title': '全国首份《AI+海洋协同发展共识》在深圳发布，深珠湛共建跨区域产业闭环（2026-08-26）',
                'badge': '[政策]',
                'abstract': '8月26日，深珠湛"AI+海洋"产业协同发展大会在深圳举办，三市海洋主管部门联合发布全国首份《AI+海洋协同发展共识》与《AI+海洋场景需求清单》。《共识》确立"创新引领、开放共享、市场导向、安全合规、协同共治"五大理念，明确支持AI企业攻关海洋垂直大模型与数字孪生技术、有序开放智慧海洋牧场与港口物流等重点场景、推进海洋数据规范开放与可信数据空间试点，构建"技术策源—装备制造—实景验证"跨区域闭环，为大湾区乃至全国海洋AI跨域协同提供可复制范式。',
                'source': '深圳新闻网 / 深圳市海洋发展局',
                'url': 'https://www.sznews.com/news/content/2026-08/29/content_32159333.htm',
                'date': '2026-08-26',
            },
        ],
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Research Expeditions",
        "items": [
            {
                'title': 'E/V Nautilus NA181 威克岛航次进行中：发现小飞象章鱼、探索二战沉船（2026-08-27，更新）',
                'badge': '[航次]',
                'abstract': '海洋探索信托的 E/V Nautilus（NA181）正于威克岛周边执行30天航次（8月20日至9月中旬）：ROV 团队在约5000米深海底完成多次下潜，一次下潜即观测到三只小飞象章鱼（dumbo octopuses），并利用 Hercules/Little Hercules/Atalanta 机器人、多波束测绘系统搜索与威克岛战役（1941）相关的二战沉船遗址；航次还布放特殊浮标监测大洋健康状况。该区域大部分海床从未测绘，是美属管辖下勘测最薄弱区域之一，全程通过 Nautilus Live 直播。（更新：NA181 由启航转入实质下潜阶段）',
                'source': 'Ocean Exploration Trust / Nautilus Live',
                'url': 'https://brant.one/2026/08/27/deep-sea-detectives-probe-remote-pacific-abyss-in-hunt-for-lost-wwii-wrecks-and-alien-like-creatures/',
                'date': '2026-08-27',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': '本周暂无明显进展（GEBCO_2026 WMS 08-04、CMEMS 8月产品更新 08-25 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据中心方向近一周无重大新发布。GEBCO_2026 网格 WMS 图层（08-04收录）、CMEMS 8月产品更新（北极波浪/Arctic潮汐3km等，08-25收录）、PANGAEA 元数据架构现代化（08-17收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://www.emodnet.eu/',
                'date': '2026-08-31',
            },
        ],
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources",
        "items": [
            {
                'title': 'Beyond Shallow-Water Photorealism：Stonefish 深水物理与传感器仿真扩展（arXiv, 2026-08-27）',
                'badge': '[开源]',
                'abstract': '赫瑞瓦特大学团队发布 Stonefish 水下模拟器的深水物理与传感器增强扩展：在现有流体动力学模型基础上增加随机 IMU 与 DVL 漂移、磁力计扰动、高阶水动力、terramechanics、压力驱动环境变化与基于物理的水下光学模型，更真实地刻画深海 AUV/ROV/着陆器/ASV/滑翔机的受力与测量特征，同时保持实时仿真兼容。该框架面向长时导航与基于学习的自主性研究，弥补现有模拟器过度乐观的浅水仿真局限，为深海机器人感知与自主作业提供更可靠的仿真基础。',
                'source': 'arXiv / cs.RO（赫瑞瓦特大学）',
                'url': 'https://arxiv.org/abs/2608.26888',
                'date': '2026-08-27',
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
