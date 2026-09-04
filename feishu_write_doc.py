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

yesterday_cn = (datetime.now()).strftime('%Y年%m月%d日')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '合成孔径声呐自动目标识别：CNN 与 Transformer 的大规模对比与训练路线图', 'badge': '[论文]', 'abstract': '针对合成孔径声呐（SAS）自动目标识别（ATR）长期由 CNN 架构主导、Transformer 代表性不足的现状，作者系统比较了现代 CNN 与 Transformer 两类深度网络在 SAS-ATR 上的表现，考察网络规模、架构、预训练方式、数据增强与正则化等因素的影响，目标是给出达到当前最优性能的训练配置路线图。研究同时回应了标注训练数据稀缺场景下数据增强与跨模态预训练权重效果不稳定这一长期争议，为水下声学目标识别的模型选型提供了可复现的实证基线。', 'source': 'arXiv (cs.CV) · arXiv:2609.01800', 'url': 'https://arxiv.org/abs/2609.01800', 'date': '2026-09-01'}, {'title': 'ICE-3D：卫星驱动的时空多尺度感知学习逐日估计北极海冰厚度', 'badge': '[论文]', 'abstract': '天津大学团队提出机器学习框架 ICE-3D，直接产出逐日格点化泛北极海冰厚度（SIT）产品，并设计“时空多尺度融合窗口（STMFW）”训练策略，融合不同尺度的物理协变信息以改善夏季海冰厚度反演。经 CryoSat-2 卫星测高与 BGEP 原位观测验证，流域尺度 SIT 整体相关系数超过 0.75，夏季 MAE 小于 0.38 m，优于 TOPAZ4 再分析并与 PIOMAS 精度相当；在线学习模块使边缘冰区的厚度高估偏差降低约 16%。基于该产品重建的海冰体积显示 1991—2020 年泛北极海冰体积损失 38%，近十年消融速率趋于稳定，指示多年冰储量已严重枯竭。', 'source': 'Remote Sensing 18(17):2991（AI for Ocean Remote Sensing 专刊）', 'url': 'https://www.mdpi.com/2072-4292/18/17/2991', 'date': '2026-09-03'}, {'title': 'SHIP-AID：面向浅水沉船隐患识别的 GeoAI 增强图像检测框架', 'badge': '[论文]', 'abstract': '研究构建模块化 GeoAI 评测框架 SHIP-AID，用于高分 RGB 影像中光学可见的浅水/潮间带沉船及伴生残骸识别。经站点级质量控制，独立源数据集含 403 个沉船点的 695 幅影像，分组不相交的留出集含 88 个站点 150 幅影像、184 个标注目标。在 10 组匹配训练种子下评测五种检测骨干与一种任务感知水下增强基线：最佳配置在锁定留出集上 mAP@50 达 0.927、mAP@50–95 为 0.668，精确率 0.896、召回率 0.861。物理驱动的水体衰减与后向散射增强可提升严格 IoU 下的表现，而全局 Otsu 阈值化反而降低召回与定位精度；性能在轻度水体退化下稳定，严重低能见度下不可靠，因此定位为“优先排序”决策支持工具，确认仍依赖声呐或现场调查。', 'source': 'Remote Sensing 18(17):2884', 'url': 'https://www.mdpi.com/2072-4292/18/17/2884', 'date': '2026-08-26'}, {'title': '基于残差—状态空间模型混合架构的北极海冰分割网络', 'badge': '[论文]', 'abstract': '针对北极海冰多任务分割中局部细节与全局上下文难以兼顾的问题，提出残差网络与视觉状态空间模型融合的混合架构：以残差网络为编码器提取多尺度局部特征，解码器采用增强型视觉状态空间模块，通过二维选择性扫描与双重注意力实现全局上下文建模；跳跃连接处设计跨尺度上下文融合模块整合编码器多层特征，训练阶段引入解码器分级监督策略优化损失，最后由并行分割头同步输出海冰密集度、发展阶段与浮冰尺寸。在 AI4Arctic 数据集上综合评分达 84.014，三项任务均优于 Swin Transformer、SegFormer 等主流方法，可为北极航道规划与通航水域划定提供技术支撑。', 'source': '《中国航海》2026, 49(4): 164-174 · DOI: 10.3969/j.issn.1000-4653.2026.04.018', 'url': 'https://d.wanfangdata.com.cn/periodical/zghh202604018', 'date': '2026-08-31'}, {'title': '厦门“文鳐”船舶与海洋工程大模型入选省级优质垂直模型，“海嘉”船舶智能化数字中枢平台全球首发', 'badge': '[要闻]', 'abstract': '据东南网报道，众数信科联合厦门理工学院研发的国内首个船舶与海洋工程大模型“文鳐”入选《2026 年福建省人工智能项目名单》，获评省级人工智能优质行业垂直模型；厦门大学科考船运行管理中心自主研发的“海嘉船舶智能化数字中枢平台”在首届厦门国际智能交通运输产业博览会面向全球首发，并入选《智能交通科技创新成果推荐目录（2026 版）》。同期，厦门珍稀海洋物种国家级自然保护区“GIS+AI”立体监测系统落地运行，获评“2026 智慧城市先锋榜”年度智慧城市应用案例一等奖，显示涉海 AI 正从单点算法走向行业垂直模型与业务中枢平台。', 'source': '东南网（厦门站）', 'url': 'https://xm.fjsen.com/2026-09/04/content_32247360_0.htm', 'date': '2026-09-04'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': 'Fugro 在新加坡建设 AI 驱动的海洋数字孪生能力，获新加坡经发局支持', 'badge': '[要闻]', 'abstract': 'Fugro 宣布通过建设 AI 驱动的海洋数字孪生（marine digital twin）能力扩展其新加坡创新业务，并获得新加坡经济发展局（EDB）支持，将新加坡打造为其亚太海洋地质数据（Geo-data）创新枢纽。该平台把地球物理调查数据、岩土工程勘察结果、实验室数据与影像统一到单一数字分析环境，用 AI/机器学习自动完成数据整合、解译与分析，替代当前碎片化、劳动密集且依赖人工判读的海洋场址表征流程，从而为海上与海岸工程提供更快的预测性“地基情报”，并以新加坡为起点向亚太及全球推广。', 'source': 'Fugro', 'url': 'https://www.fugro.com/news/business-news/2026/fugro-strengthens-singapore-innovation-hub-with-new-ai-driven-marine-digital-twin', 'date': '2026-09-03'}, {'title': '自然资源部北海预报减灾中心启动“近岸淹没精细化数字孪生”研发外协采购', 'badge': '[动态]', 'abstract': '中国政府采购网发布竞争性磋商公告，自然资源部北海预报减灾中心就“近岸淹没精细化数字孪生外协”项目公开采购，预算 50 万元，采购需求为近岸淹没精细化数字孪生技术研发，专门面向中小企业。供应商须于 2027 年 1 月 31 日前在青岛完成数字孪生系统的开发、部署、培训与验收交付，响应文件递交与开启时间为 2026 年 9 月 14 日。该公告反映近岸风暴潮淹没精细化模拟已从科研示范进入业务化建设阶段。', 'source': '中国政府采购网（北海预报减灾中心）', 'url': 'https://www.ccgp.gov.cn/cggg/zygg//jzxcs/202609/t20260902_27255814.htm', 'date': '2026-09-02'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Data Visualization', 'items': [{'title': 'NEODAAS 上线面向科考航次的卫星海洋观测可视化门户', 'badge': '[工具]', 'abstract': '英国 NEODAAS 发布基于 Syntool 框架构建的全新可视化门户（data.neodaas.ac.uk/cruise/），在一个交互界面中集成其自主处理的增强海色、叶绿素浓度、热锋等特色产品与 Copernicus 公开数据，供科考船在航次中实时浏览与分析。以往受船载带宽限制只能提供低分辨率静态图，随着海上互联网条件改善，该门户可按单个航次需求定制，帮助科考队以卫星大尺度视野规划 targeted 原位采样，节省搜寻时间与燃油。该门户已在东北大西洋 Porcupine Abyssal Plain（PAP）观测站年度航次中试用并获科考队正面反馈。', 'source': 'NEODAAS（NERC/National Oceanography Centre）', 'url': 'https://neodaas.ac.uk/news/neodaas-launches-new-portal-to-enhance-access-to-satellite-ocean-observations-onboard-research-cruises', 'date': '2026-08-26'}, {'title': 'IMOS Live 平台升级：新增 AusTemp 海表温度产品与 75+ 岸基波浪浮标', 'badge': '[动态]', 'abstract': '澳大利亚综合海洋观测系统（IMOS）发布 IMOS Live 更新版本，新增近实时（NRT）锚系数据流与图层：用户可追踪 AusTemp 产品的海表温度及其距平、查看修订后的海洋增温指标组，并展示 Rottnest 岛与 Maria 岛升级后锚系的逐小时温盐剖面。沿海波浪浮标网络扩展至 75 个以上站点。平台核心能力是在同一界面并排显示卫星空间影像与局地时间序列，界面针对小屏优化以服务现场作业，地图与时间序列图均可带图例与图框导出，直接用于正式报告或论文配图。', 'source': 'IMOS', 'url': 'https://imos.org.au/news/imos-live-upgraded', 'date': '2026-08-27'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA-QC', 'items': [{'title': '迄今最大规模的全球多传感器融合海洋水色叶绿素产品精度评估', 'badge': '[数据]', 'abstract': '普利茅斯海洋实验室（PML）领衔在 Frontiers in Remote Sensing 发表研究，利用大西洋经向断面（AMT）航次自主光学系统每分钟一次的连续观测，结合美国团队同类数据，构建超过 13,000 组可直接与卫星过境匹配的全球实测数据集，系统评估七套多任务融合海洋水色叶绿素 a 产品的精度。结果显示各产品精度总体接近，OC-CCI 与 CMEMS CCI 版本略优；七套产品全部满足航天机构设定的叶绿素 a 反演误差低于 35% 的目标，平均误差仅 30%。研究同时指出，随着卫星任务增多，仍需持续投入支持在关键偏远海域、宽叶绿素浓度范围内开展高基准（FRM）实测“海上真值”验证。', 'source': 'Plymouth Marine Laboratory / Frontiers in Remote Sensing', 'url': 'https://www.frontiersin.org/journals/remote-sensing/articles/10.3389/frsen.2026.1825086/full', 'date': '2026-08-26'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing / Reconstruction', 'items': [{'title': '注意力增强 3D-U-Net++ 实现西太平洋三维温盐场实时智能重构并发布长时序数据集', 'badge': '[论文]', 'abstract': '中国科学院海洋研究所大洋西边界流动力学研究组构建注意力增强 3D-U-Net++ 智能重构框架，在嵌套密集跳跃连接的三维编解码网络中嵌入 CBAM 卷积注意力模块，通过通道与空间双重注意力实现跨尺度特征聚合，自动强化与次表层变化强相关的时序表层特征，抑制噪声扩散与过度平滑，保留垂向温盐梯度与锋面结构；模型以连续时序海表温度与海面高度联合输入降低三维反演非唯一性，并采用两阶段迁移学习策略同时学习大尺度季节背景与涡旋、锋面等高频中尺度过程。与 GLORYS2V4、HYCOM、ORAS5 等主流同化产品相比，该产品全时段全深度更接近现场观测，误差较公认最优的 GLORYS2V4 降低逾 10%。团队已公开发布 1993—2023 年西太平洋逐日三维温盐重构数据集。（注：论文正式出版日 2026-07-06，属顶级期刊与国家级院所成果，中科院海洋所 09-04 发布新闻稿并同步开放数据集，按重要性豁免收录）', 'source': 'Earth System Science Data 18: 4617-4638 / 中国科学院海洋研究所', 'url': 'https://essd.copernicus.org/articles/18/4617/2026/', 'date': '2026-09-04'}]}, {'title': '六、数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'BBNJ 协定信息交换机制（CHM）的数据治理基础研究', 'badge': '[论文]', 'abstract': '由世界海事大学 Sasakawa 全球海洋研究所“海洋生物多样性观测数据工作组”联合 MBON 与 AIR Centre 完成、发表于 Frontiers in Marine Science 的研究指出，2026 年 1 月生效的 BBNJ（公海）协定的落地取决于海洋数据与海洋遗传资源如何被采集、管理与共享，其信息交换机制（Clearing-House Mechanism）必须建立在全球一致、可互操作的数据实践之上，而不应另起炉灶复制或取代既有全球数据基础设施。论文提出的关键条件包括：通过互操作标准与稳健的溯源元数据实现对接、让海洋遗传资源可从采样追踪到再利用、仓储库之间的互操作与标识符传播，以及跨国际协定规则协调；同时强调需提升学术界、公共与私营机构的数据素养。', 'source': 'Frontiers in Marine Science 13 · DOI: 10.3389/fmars.2026.1840546', 'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1840546/full', 'date': '2026-08-31'}, {'title': 'EMODnet 数据吸纳（Data Ingestion）服务进入新阶段，由意大利 CMCC 牵头', 'badge': '[动态]', 'abstract': '欧洲海洋观测与数据网络（EMODnet）宣布其数据吸纳服务（Data Ingestion, DI）于 2026 年夏季启动新阶段，由更新后的机构与专家联盟承担、意大利 CMCC 牵头，在延续既有服务的同时依据 EMODnet 2035 愿景进行战略性演进。新阶段将重点吸纳此前缺乏（或渠道有限）数据汇交通道的提供方数据，包括蓝色经济与更广泛私营部门的海洋环境与人类活动数据、海岸与海上许可活动数据、公民科学及其他代表性不足的公共来源与新兴观测系统；并通过技术开发、数据管理支持、利益相关方参与、能力建设与传播，简化贡献流程、提升透明度，强化与 EMODnet 主题领域及可信仓储的连接。', 'source': 'EMODnet', 'url': 'https://emodnet.ec.europa.eu/en/new-phase-emodnet-data-ingestion-service-kicks', 'date': '2026-08-31'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expedition', 'items': [{'title': '海南省 2026 年下半年共享航次启航，“深海科创积分”全链条闭环跑通', 'badge': '[航次]', 'abstract': '“深海科创积分”赋分仪式暨 2026 年下半年共享航次启航仪式 9 月 3 日在三亚崖州湾科技城举行，由海南省海洋厅、海南海事局指导，海南省海洋监测预报中心等主办。上半年首期共享航次已统筹调度科考船舶完成多家单位海上科考任务，完成水下连接器、无人平台、投弃式浮标等国产海洋装备实海验证，搭建海洋环境样本库与专题数据集，并探索“科考+执法”协同模式。深海科创积分依托国家创新积分制框架增设 100 分海洋特色专项、总分 230 分，参加单位按试验组织实施、科研产出成效、海洋数据汇交三个维度获分，两年内可兑换共享航次科考席位、科研装备使用权限、海洋数据产品等，海南大学已用首期积分成功兑换，标志“参与—贡献—回报—再参与”闭环落地。下半年航次聚焦深海材料与深海探测装备研发。', 'source': '海南省海洋厅 / 椰网', 'url': 'https://www.hndnews.com/p/757938.html', 'date': '2026-09-04'}, {'title': '上海海洋大学中西印度洋公海渔业资源综合科学调查船租赁项目落标，9 月起实施 100 个调查站点', 'badge': '[航次]', 'abstract': '中国政府采购网公布中标（成交）结果，上海海洋大学“中西印度洋公海渔业资源综合科学调查船租赁”项目由中国水产科学研究院黄海水产研究所中标，成交金额 1948.1696 万元。航次计划自 2026 年 9 月起实施，完成调查站点 100 个，具体时间视渔场海况等按最终航次执行需求确定；服务时间为包干制，航次期间因船舶与仪器故障、恶劣天气海况等不可抗力产生的相关费用由供应商承担。该航次将支撑中西印度洋公海渔业资源的综合性科学调查。', 'source': '中国政府采购网（上海海洋大学）', 'url': 'https://www.ccgp.gov.cn/cggg/dfgg/zbgg/202608/t20260831_27236192.htm', 'date': '2026-08-31'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '第十一次国家科学数据中心主任联席会在舟山召开，国家海洋科学数据中心主办', 'badge': '[动态]', 'abstract': '2026 年 8 月 21—22 日，第十一次国家科学数据中心主任联席会在浙江舟山召开，由国家海洋科学数据中心主办、国家材料腐蚀与防护科学数据中心承办，来自科技部国家科技基础条件平台中心、自然资源部科技发展司、国家海洋信息中心及各国家科学数据中心代表参会。会议围绕对接国家战略与绩效评估、人工智能时代科学数据中心的角色重塑与能力建设、开放共享与高效流通、面向智能就绪的数据质量评价模型与可信认证等议题研讨。其中，海洋科学数据中心介绍了差异化数据处置与一体化分级共享服务体系的实践经验（会议本身 8 月 21—22 日召开，国家海洋信息中心 09-03 发布报道）。', 'source': '国家海洋信息中心 / 中国海洋信息网', 'url': 'https://www.nmdis.org.cn/c/2026-09-03/85805.shtml', 'date': '2026-09-03'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'OpenDrift 海洋轨迹模拟框架发布 v1.14.12', 'badge': '[开源]', 'abstract': '开源海洋轨迹建模框架 OpenDrift 发布 1.14.12 版本（PyPI 发布日 2026-08-31，conda-forge 同步更新）。OpenDrift 由挪威气象研究所维护，是海洋拉格朗日粒子追踪的通用框架，广泛用于溢油漂移、搜救漂移、微塑料输运、鱼类与浮游生物输运、有害藻华扩散等场景，支持接入多种海洋与大气模式/再分析场，并以模块化方式定义被追踪对象行为。本次版本为该系列常规迭代更新，可通过 pip install opendrift 或 conda 安装，要求 Python ≥3.9。', 'source': 'PyPI / conda-forge（OpenDrift, MET Norway）', 'url': 'https://pypi.org/project/opendrift/', 'date': '2026-08-31'}]}]

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


def item_block(num, title, badge, abstract, source, date, url):
    blocks = []
    badge_text = badge if badge else ""
    title_text = f"{badge_text} {title}" if badge_text else title
    blocks.append(paragraph([tr(f"  {num}. ", bold=True), tr(title_text, bold=True, link=url)]))
    blocks.append(paragraph([tr(abstract)]))
    meta_parts = []
    if source:
        meta_parts.append(f"来源：{source}")
    if date:
        meta_parts.append(f"日期：{date}")
    if url:
        meta_parts.append(f"链接：{url}")
    blocks.append(paragraph([tr(" | ".join(meta_parts), bold=False)]))
    blocks.append(divider())
    return blocks


def section_block(title, en_title, items):
    blocks = []
    blocks.append(heading(title, 1))
    blocks.append(paragraph([tr(en_title, bold=False)]))
    blocks.append(divider())
    for i, item in enumerate(items, 1):
        blocks.extend(item_block(
            i,
            item.get('title', ''),
            item.get('badge', ''),
            item.get('abstract', ''),
            item.get('source', ''),
            item.get('date', ''),
            item.get('url', '')
        ))
    return blocks


def build_blocks():
    blocks = []
    blocks.append(heading(f"海洋AI技术日报 · {datetime.now().strftime('%Y年%m月%d日')}", 1))
    blocks.append(divider())
    for section in SECTIONS:
        blocks.extend(section_block(
            section['title'],
            section.get('en', ''),
            section.get('items', [])
        ))
    return blocks


def create_document_and_write(tenant_access_token):
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    payload = {"title": f"海洋AI技术日报 {datetime.now().strftime('%Y-%m-%d')}"}
    headers = {
        "Authorization": f"Bearer {tenant_access_token}",
        "Content-Type": "application/json"
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    doc_id = resp.json()["data"]["document"]["document_id"]
    print(f"文档创建成功: {doc_id}")
    return doc_id


def write_blocks_to_doc(token, doc_id, blocks, max_retries=3, batch_size=30):
    """分批写入内容块到飞书文档"""
    base_url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 分批处理
    total_batches = (len(blocks) + batch_size - 1) // batch_size
    for batch_idx in range(total_batches):
        batch_start = batch_idx * batch_size
        batch_end = min((batch_idx + 1) * batch_size, len(blocks))
        batch_blocks = blocks[batch_start:batch_end]
        
        for attempt in range(max_retries):
            try:
                payload = {
                    "blocks": batch_blocks
                }
                resp = requests.post(base_url, headers=headers, json=payload)
                resp.raise_for_status()
                print(f"Batch {batch_idx + 1}/{total_batches}: blocks {batch_start}-{batch_end-1} written successfully")
                break
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Batch {batch_idx + 1} attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"Batch {batch_idx + 1} failed after {max_retries} attempts: {e}")
                    raise
    print(f"All {len(blocks)} blocks written to document {doc_id}")


def main():
    resp = requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal", json={
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    })
    resp.raise_for_status()
    token = resp.json()["tenant_access_token"]

    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)

    print(f"Document URL: https://{TENANT_DOMAIN}/docx/{doc_id}")


if __name__ == "__main__":
    main()
