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

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                "title": '1. 南科大牵头SPEED项目获批联合国\u201c海洋十年\u201d官方行动，AI赋能深海数字孪生',
                "badge": "[头条]",
                "abstract": (
                    '2026年3月12日，联合国教科文组织政府间海洋学委员会（UNESCO-IOC）正式发布通知，'
                    '南方科技大学海洋高等研究院/深圳海洋大学（筹）牵头申报的\u201c深海环境与工程仿真与预测\u201d'
                    '（SPEED）项目成功获批联合国\u201c海洋十年\u201d（2021-2030）官方行动，成为\u201c数字孪生海洋\u201d'
                    '（DITTO）大科学计划的核心项目之一。SPEED 项目是深圳牵头获批的首个深海领域 AI 赋能的联合国'
                    '\u201c海洋十年\u201d项目，将利用 AI 技术对深海多源异构数据进行三维高精度展示，构建向全球开放的'
                    '高时空分辨率深海数字孪生系统。'
                ),
                "source": "搜狐网 / 南科大海高院",
                "date": "2026-03-16",
                "url": "https://www.sohu.com/a/997323776_726570"
            },
            {
                "title": "2. 中科院海洋所发表《Proceedings of the IEEE》综述：AI赋能海洋卫星遥感三大核心方向",
                "badge": "",
                "abstract": (
                    "中国科学院海洋研究所人工智能海洋学研究组联合国内相关单位，在顶级期刊 Proceedings of the IEEE"
                    "（影响因子 25.9）发表综述论文，系统总结 AI 在海洋卫星遥感中的关键进展：聚焦海洋参数反演"
                    "（CNN/Transformer 在海浪、海表盐度、海面风场、水色参数中的应用）、海洋数据重建以及海洋现象识别"
                    "三大核心方向，并从建模方法、应用场景与未来趋势等维度进行系统梳理，为全球海洋遥感 AI 研究提供重要参考。"
                ),
                "source": "中科院海洋研究所",
                "date": "2026-03-03",
                "url": "https://qdio.cas.cn/2019Ver/News/kyjz/202603/t20260303_8147415.html"
            },
            {
                "title": '3. \u201c飞鱼-1.0\u201d全球首个南海海-气双向耦合智能大模型正式发布',
                "badge": "",
                "abstract": (
                    '中国科学院南海海洋研究所与中国石油大学（华东）联合研发的\u201c飞鱼-1.0\u201d大模型正式发布，'
                    '这是全球首个面向南海区域的海-气双向耦合智能大模型。该模型实现三项核心技术创新：核心数据自主可控'
                    '（基于 REDOS2.0 高分辨率南海再分析数据集）、海-气双向智能耦合、\u201c即插即用\u201d低成本学习。'
                    '模型通过\u201c快慢\u201d双通道学习智能化模拟海气之间动量、热量等双向交互影响，显著提升海气关键要素预报精度，'
                    '打破国内海洋大模型对国外数据的依赖。'
                ),
                "source": "中国科学院 / 光明日报",
                "date": "2026-02-10",
                "url": "https://cas.cn/cm/202602/t20260210_5100249.shtml"
            },
            {
                "title": "4. SeaCast：图神经网络驱动区域海洋预报，单 GPU 20秒完成15天高分辨率预报",
                "badge": "",
                "abstract": (
                    "芬兰赫尔辛基大学、地中海气候变化研究中心与意大利萨伦托大学联合研发图神经网络模型 SeaCast，"
                    "专为区域海洋预报设计。训练完成后，在单块 GPU 上仅需 20 秒即可完成 1/24° 网格下 18 个垂向层次的"
                    " 15 天预报，远优于需 89 个 CPU 核心耗时 70 分钟的传统物理模型 MedFS，为航运安全、水产养殖管理等"
                    "应用提供超高时效海洋预报能力。"
                ),
                "source": "腾讯新闻 / 量子位",
                "date": "2026-02-27",
                "url": "https://news.qq.com/rain/a/20260227A035B900"
            },
            {
                "title": '5. 山东\u201cAI+海洋\u201d融合：琅琊2.0大模型进入内测，抢占蓝色AI新赛道',
                "badge": "",
                "abstract": (
                    '中国科学院海洋研究所\u201c琅琊2.0\u201d海洋预报大模型正在进行第二轮内测，预计2026年上半年发布。'
                    '该版本将进一步拓展对台风、降水、海冰等海洋现象的预报能力，覆盖海洋环境安全、气候变化、海洋资源开发'
                    '和防灾减灾等多领域。山东省正加快\u201c人工智能+海洋\u201d深度融合发展，赋能蓝色经济高质量发展，'
                    '青岛西海岸新区已成为海洋AI研究的重要聚集地。'
                ),
                "source": "闪电新闻 / 山东新闻联播",
                "date": "2026-03-01",
                "url": "https://sdxw.iqilu.com/share/YS0yMS0xNzA2NDI5MQ==.html"
            }
        ]
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin / Marine Digital Twin",
        "items": [
            {
                "title": "1. 厦大柴扉团队《国家科学评论》：海洋数字孪生赋能蓝色经济创新",
                "badge": "[新发]",
                "abstract": (
                    "厦门大学海洋生物地球化学全国重点实验室柴扉教授联合多位国际专家，在 National Science Review"
                    "（《国家科学评论》，NSR，IF~20）发表综述论文，系统梳理海洋数字孪生（DTO）核心架构，深度解析"
                    "其赋能蓝色经济的路径与挑战。论文提出 DTO 四模块架构（数据获取-模型融合-虚实映射-决策支持），"
                    "并聚焦于如何将 AI、物联网（IoT）与高性能计算整合，以构建实时、动态的海洋数字镜像。该成果为"
                    "全球海洋数字孪生标准体系建设提供了重要理论支撑。"
                ),
                "source": "厦门大学 MEL / National Science Review",
                "date": "2026-03-08",
                "url": "https://mel.xmu.edu.cn/info/1012/61071.htm"
            },
            {
                "title": "2. DigiTwin 2026 第六届数字孪生国际会议（牛津大学）征集海洋工程分论坛报告",
                "badge": "",
                "abstract": (
                    "第六届数字孪生国际会议（DigiTwin 2026）将于2026年8月4-8日在英国牛津大学举行，"
                    "设有\u201c海洋工程\u201d专题分论坛。会议面向全球征集关于数字孪生在海洋领域（海洋工程结构健康监测、"
                    "海上装备仿真、海洋环境预报）的最新研究报告，为国际海洋数字孪生研究者提供重要的交流与合作平台。"
                    "本次会议标志着海洋数字孪生已从实验室研究走向国际工程应用主流议题。"
                ),
                "source": "DigiTwin 2026 / Oxford",
                "date": "2026-03 公告",
                "url": "https://www.python88.com/topic/193421"
            },
            {
                "title": "3. 清华大学张建民院士综述《Ocean》：数字孪生在海洋领域的应用前景",
                "badge": "",
                "abstract": (
                    "清华大学张建民院士在期刊 Ocean 发表综述，通过 Web of Science 数据库检索筛选出 183 篇"
                    "海洋孪生技术（Marine Digital Twin，MDT）相关文献，梳理该领域 2018 年以来呈现的快速增长趋势"
                    "（2023年发文量达68篇）。综述系统分析了海洋数字孪生在海洋工程结构监测、海洋生态仿真、"
                    "海洋预报与决策支持等场景中的技术进展，并指出目前数据实时性与模型泛化能力仍是关键瓶颈。"
                ),
                "source": "搜狐 / 清华大学 Ocean",
                "date": "2026-01-24",
                "url": "https://www.sohu.com/a/979686491_726570"
            },
            {
                "title": "4. DTO 综述登顶《国家科学评论》：数字孪生海洋作为蓝色经济创新催化剂",
                "badge": "",
                "abstract": (
                    "厦门大学团队在 National Science Review 发表 \"Digital twin of the ocean as a catalyst for"
                    " blue economy innovation\"，从政策、技术与产业三重视角阐释 DTO 的战略价值。论文提出，DTO 不仅"
                    "是科学研究工具，更是推动蓝色经济商业化的关键基础设施，通过集成物理模型、机器学习代理模型与实时"
                    "传感器数据，可实现对海洋渔业、航运、能源等场景的精准数字化运营，助力实现联合国 2030 年可持续发展目标。"
                ),
                "source": "Oxford Academic / National Science Review",
                "date": "2026-01-20",
                "url": "https://academic.oup.com/nsr/article/13/3/nwag012/8431396"
            }
        ]
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization / Marine Data Visualization",
        "items": [
            {
                "title": "1. 《国际地理信息科学》：海洋流场与温盐场交互可视化新方法",
                "badge": "[新刊]",
                "abstract": (
                    "发表于 International Journal of Digital Earth（Taylor & Francis，2026年2月9日），"
                    "研究整合标量场（温度、盐度）与矢量场（流速、流向）的联合可视化方案，提出一种能在同一视图中"
                    "同步展示海流矢量与温盐分布的交互式可视化框架。该方法对理解大洋环流与物质能量输运过程具有重要意义，"
                    "支持用户通过交互操作实时探索洋流与热盐环流的耦合关系，填补了海洋多变量联合可视化领域的研究空白。"
                ),
                "source": "Int. J. Digital Earth / Taylor & Francis",
                "date": "2026-02-09",
                "url": "https://www.tandfonline.com/doi/full/10.1080/17538947.2026.2624176"
            },
            {
                "title": "2. 船载海洋雷达实时冰山监测系统：AI辅助高分辨率海冰可视化",
                "badge": "",
                "abstract": (
                    "发表于 GIScience & Remote Sensing（Taylor & Francis，2026年3月5日），提出基于船载海洋雷达"
                    "（MR）的海冰浮冰实时监测与可视化方案。该系统利用 AI 算法弥补卫星遥感的时间局限性，实现对海冰浮冰"
                    "的高分辨率实时探测与三维可视化展示，为北极航道与极地科考提供实时海冰态势感知能力。系统已在实船测试"
                    "中验证，相比传统卫星数据处理方式显著提升了实时性与空间精度。"
                ),
                "source": "GIScience & Remote Sensing / Taylor & Francis",
                "date": "2026-03-05",
                "url": "https://www.tandfonline.com/doi/full/10.1080/15481603.2026.2640271"
            },
            {
                "title": "3. Global Fishing Watch：AI突破实现全球船舶活动的卫星可视化监测",
                "badge": "",
                "abstract": (
                    "Global Fishing Watch 发布基于卫星图像与 AI 分析的全球船舶活动监测新数据集，实现对全球海洋中"
                    "船舶动态的前所未有的可视化监测能力。该突破性成果整合了多源卫星数据与深度学习目标检测模型，"
                    "支持通过 Skylight 平台免费获取实时船舶探测数据，对打击非法捕鱼、海洋安全监管与蓝色经济治理具有"
                    "重要价值，展示了 AI 驱动的大尺度海洋可视化监测的最新水平。"
                ),
                "source": "Global Fishing Watch",
                "date": "2025-07-10（持续更新）",
                "url": "https://globalfishingwatch.org/article/ai-breakthrough-ocean-monitoring-satellite-imagery-unprecedented-view-global-vessel-activity/"
            },
            {
                "title": "4. 国家海洋科学数据中心（NMDIS）：多要素海洋数据在线可视化平台持续升级",
                "badge": "",
                "abstract": (
                    "国家海洋科学数据中心（NMDIS）多要素海洋数据可视化平台持续更新，提供海流场、温盐场、深度地形等"
                    "多图层叠加与交互探索功能，支持矢量底图、地形底图与影像底图三种底图模式切换。平台开放面向公众与"
                    "科研用户的在线可视化分析工具，实现对中国近海及全球海洋观测数据的直观展示，并支持经纬度精确查询与"
                    "专题图层定制，是国内海洋数据可视化的重要基础设施。"
                ),
                "source": "国家海洋科学数据中心 NMDIS",
                "date": "持续更新",
                "url": "https://mds.nmdis.org.cn/pages/visualization.html"
            }
        ]
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality / Marine Data Quality Control",
        "items": [
            {
                "title": "1. IOC-UNESCO 海洋数据质量保障与质量控制（QA/QC）培训课程开展",
                "badge": "[课程]",
                "abstract": (
                    "IOC/IOCARIBE 于2026年2月26日发布通知，开展面向拉丁美洲与加勒比海地区的\u201c海洋信息系统中"
                    "数据质量保障与质量控制\u201d培训课程（线上）。课程围绕联合国\u201c海洋十年\u201d框架，涵盖 QA/QC 基础"
                    "知识、多专题（温度、盐度、生物地球化学、物理参数）质量控制实操，旨在提升区域海洋数据管理能力，"
                    "课程内容涵盖最新 AI 辅助质量控制方法，是目前全球最新的海洋数据质量专题培训之一。"
                ),
                "source": "IOC/IOCARIBE - UNESCO",
                "date": "2026-02-26",
                "url": "https://iocaribe.ioc-unesco.org/en/event/3037"
            },
            {
                "title": "2. 《Ocean Modelling》综述：机器学习在海洋数据同化中的进展、差距与业务化路径",
                "badge": "",
                "abstract": (
                    "发表于 Ocean Modelling（Elsevier，2026年2月1日），综述 2020-2025 年机器学习应用于海洋数据同化"
                    "的最新进展，梳理了包括深度学习、物理引导神经网络（PGNN）等方法在提升数据质量与同化精度方面的关键"
                    "成果，识别出当前存在的核心差距（可解释性、实时性、数据稀疏性适应），并提出业务化路径规划，"
                    "为海洋预报中心将 ML 方法从研究转向实际业务应用提供参考框架。"
                ),
                "source": "Ocean Modelling / Elsevier",
                "date": "2026-02-01",
                "url": "https://www.sciencedirect.com/science/article/pii/S1463500326000028"
            },
            {
                "title": "3. 主动学习驱动海洋数据质量评估：ODEAL框架有效减少人工标注负担",
                "badge": "",
                "abstract": (
                    "发表于 International Journal of Data Science and Analytics（Springer，2025年4月），"
                    "研究提出主动学习结合离群点检测的ODEAL框架，针对 Argo、GLOSS、EMSO 等大规模海洋观测网络中"
                    "数据量级大、异常样本稀少的质量控制难题。通过主动学习策略优先标注高信息量样本，将人工质量控制"
                    "工作量降低 60% 以上，同时保持与全量人工标注相当的质量控制精度，为未来自动化海洋数据质量管理"
                    "提供了可落地方案。"
                ),
                "source": "Int. J. Data Sci. Analytics / Springer",
                "date": "2025-04-08",
                "url": "https://link.springer.com/article/10.1007/s41060-025-00751-w"
            },
            {
                "title": "4. autoQC：基于深度神经网络的在线AI海洋数据质量控制平台",
                "badge": "",
                "abstract": (
                    "autoQC 是一款基于深度神经网络的在线 AI 应用，通过学习海洋质量控制数据专家的人工视觉判断模式，"
                    "模拟专家进行海洋数据可视化质量控制，支持 Argo 等多种海洋观测数据的自动化 QC 审核。该平台已在"
                    " ResearchGate 发布，为全球海洋数据管理机构提供低门槛的 AI 辅助质量控制工具，有效缓解海量数据"
                    "导致的人工 QC 瓶颈，是目前最具实用性的开源海洋数据质控平台之一。"
                ),
                "source": "ResearchGate",
                "date": "2024-06（持续更新）",
                "url": "https://www.researchgate.net/publication/385740799_autoQC_An_AI_based_online_app_for_ocean_data_quality_control"
            }
        ]
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing / Marine Data Processing",
        "items": [
            {
                "title": "1. IEEE综述：深度学习驱动海洋预报——大规模海洋数据处理新范式",
                "badge": "[综述]",
                "abstract": (
                    "发表于 IEEE Transactions on Geoscience and Remote Sensing（2025年4月），针对数据驱动深度学习"
                    "在海洋预报中的综合应用进行深入综述，重点梳理深度学习模型（Transformer、GraphNN、扩散模型）如何"
                    "从持续增长的海洋大数据中挖掘模式与深层规律。论文覆盖海表温度预测、海流速度场重建、ENSO预报等核心"
                    "场景，总结数据预处理、特征提取与模型训练的最新方法，为海洋数据处理领域提供权威技术参考。"
                ),
                "source": "IEEE Transactions on Geoscience and Remote Sensing",
                "date": "2025-04-01",
                "url": "https://ieeexplore.ieee.org/document/10947107"
            },
            {
                "title": "2. 混合机器学习数据同化：生物地球化学海洋模型精度大幅提升",
                "badge": "",
                "abstract": (
                    "发表于 Biogeosciences（EGU/Copernicus，2026年1月12日），提出混合机器学习数据同化（Hybrid ML-DA）"
                    "框架，将传统物理海洋模型与机器学习代理模型结合，应用于海洋表层生物地球化学数据处理与模型校正。"
                    "研究表明，Hybrid ML-DA 相比纯物理同化方案，在叶绿素 a、溶解有机碳等关键参数的重建精度上提升"
                    " 25-40%，为海洋碳循环研究提供更高精度的数据处理解决方案。"
                ),
                "source": "Biogeosciences / EGU Copernicus",
                "date": "2026-01-12",
                "url": "https://bg.copernicus.org/articles/23/315/2026/"
            },
            {
                "title": "3. 生成式数据同化（GenDA）：扩散模型重构海洋表面流速场",
                "badge": "",
                "abstract": (
                    "发表于 Journal of Advances in Modeling Earth Systems（AGU，2025年8月），提出生成式数据同化"
                    "（Generative Data Assimilation，GenDA）新方法，利用扩散模型（Diffusion Model）对稀疏海洋观测"
                    "数据进行高精度重建与数据同化。GenDA 在海表流速场重构任务中展现出优异的不确定性量化能力，能够生成"
                    "多组合理的状态集合，相比传统 EnKF 方法更准确反映海洋状态的不确定性，为海洋业务化预报系统提供"
                    "新一代数据处理范式。"
                ),
                "source": "JAMES / AGU Wiley",
                "date": "2025-08-09",
                "url": "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025MS005063"
            },
            {
                "title": "4. Copernicus系列综述：机器学习助力海洋预报——数据处理方法集成与展望",
                "badge": "",
                "abstract": (
                    "发表于 State of the Planet（Copernicus/EGU，2025年6月），汇集多位顶级海洋学家撰写的机器学习"
                    "在海洋预报与数据处理中的综合性综述，覆盖算法基础（CNN、RNN、GNN、Transformer）在海洋数据处理"
                    "流水线中的系统集成方法。报告特别关注数据标准化、多分辨率融合、实时流式处理等海洋大数据预处理技术，"
                    "并对未来基于基础模型（Foundation Model）的新一代海洋数据处理框架作出前瞻性展望。"
                ),
                "source": "State of the Planet / Copernicus",
                "date": "2025-06-02",
                "url": "https://sp.copernicus.org/articles/5-opsr/22/2025/sp-5-opsr-22-2025.pdf"
            }
        ]
    }
]


# ── 块构造函数 ────────────────────────────────────────────────
def tr(content, bold=False, link=None):
    style = {"bold": bold, "inline_code": False, "italic": False,
             "strikethrough": False, "underline": False}
    if link:
        style["link"] = {"url": link}
    return {"text_run": {"content": content, "text_element_style": style}}


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
        "\u7531 WorkBuddy \u81ea\u52a8\u751f\u6210"
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
        "\u672c\u7b80\u62a5\u7531 WorkBuddy \u6bcf\u65e5\u81ea\u52a8\u751f\u6210\uff0c\u4ec5\u4f9b\u5b66\u672f\u53c2\u8003\u3002\u7248\u6743\u5f52\u539f\u4f5c\u8005/\u673a\u6784\u6240\u6709\u3002"
    )]))
    return blocks


# ── 主流程 ────────────────────────────────────────────────────
def get_token():
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
    )
    return r.json()["tenant_access_token"]


def create_doc(token, title):
    h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    r = requests.post("https://open.feishu.cn/open-apis/docx/v1/documents",
                      headers=h, json={"title": title}, timeout=15)
    d = r.json()
    if d.get("code") != 0:
        print(f"[ERROR] create doc: {d}")
        sys.exit(1)
    doc_id = d["data"]["document"]["document_id"]
    print(f"[OK] doc created: {doc_id}")
    return doc_id


def write_blocks(token, doc_id, blocks):
    h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    BATCH = 50
    total = len(blocks)
    for i in range(0, total, BATCH):
        batch = blocks[i:i + BATCH]
        r = requests.post(
            f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
            headers=h, json={"children": batch, "index": 0}, timeout=30
        )
        d = r.json()
        if d.get("code") != 0:
            print(f"[ERROR] batch {i // BATCH + 1}: {json.dumps(d, ensure_ascii=False)[:400]}")
            return False
        n = i + len(batch)
        print(f"[OK] {n}/{total} blocks written")
        if n < total:
            time.sleep(0.4)
    return True


if __name__ == "__main__":
    print(f"=== Feishu Doc Writer (HTML-aligned) ===")
    print(f"Target date: {yesterday_cn}\n")

    token = get_token()
    print(f"[OK] token: {token[:12]}...")

    doc_id = create_doc(token, f"\u6d77\u6d0bAI\u6280\u672f\u65e5\u62a5 \u00b7 {yesterday_cn}")
    doc_url = f"https://{TENANT_DOMAIN}/docx/{doc_id}"
    print(f"[OK] doc url: {doc_url}\n")

    blocks = build_all_blocks()
    print(f"[INFO] {len(blocks)} blocks to write...\n")

    ok = write_blocks(token, doc_id, blocks)

    if ok:
        print(f"\n[SUCCESS] Done!")
        print(f"URL: {doc_url}")
    else:
        print(f"\n[WARN] Partial failure. URL: {doc_url}")

    with open("feishu_doc_url.txt", "w", encoding="utf-8") as f:
        f.write(doc_url)
    print(f"[OK] URL saved to feishu_doc_url.txt")
