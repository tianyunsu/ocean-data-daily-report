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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '混合 Mamba-Transformer 网络重思水下图像增强', 'badge': '[论文]', 'abstract': '水下图像常因光散射与波长相关衰减而出现色偏、低对比与细节模糊，阻碍水下视觉任务。研究提出一种混合 Mamba-Transformer 网络用于水下图像增强，把状态空间模型的长程依赖建模与 Transformer 的全局注意力相结合，在保持计算效率的同时改善颜色恢复与纹理细节，为水下感知与机器人视觉提供更稳健的预处理手段。（Nature Portfolio / Scientific Reports）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-73332-x', 'date': '2026-10-05'}, {'title': '深海采矿履带车主动悬架的耦合自适应神经网络控制', 'badge': '[论文]', 'abstract': '深海采矿履带车在软底质上作业时需在复杂扰动下维持姿态稳定。研究针对其主动悬架提出耦合自适应神经网络控制方法，通过在线补偿模型不确定性与外部扰动，改善车辆在不平海底与复杂水力环境下的姿态控制与行驶平顺性，为深海采矿装备自主控制提供方案。（Elsevier / Ocean Engineering）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128631', 'date': '2026-10-07'}, {'title': '水下深度与表面法线估计的实用方法', 'badge': '[论文]', 'abstract': '单目水下图像的深度与表面法线估计对三维重建、机器人感知与海底测绘意义重大，但水下成像退化使该任务困难。研究提出一种实用性方法，联合估计水下场景的深度与表面法线，以应对浑浊、低对比与颜色衰减等退化，提升水下三维几何感知的准确性与鲁棒性。（Elsevier / CVIU）', 'source': 'Computer Vision and Image Understanding', 'url': 'https://doi.org/10.1016/j.cviu.2026.104971', 'date': '2026-10-05'}, {'title': 'Sentinel-2 联合多源重力数据的浅水海底地形精细反演（深度分层 XGBoost）', 'badge': '[论文]', 'abstract': '浅水区海底地形对航行安全与海洋工程十分重要，但传统测深成本高、覆盖有限。研究融合 Sentinel-2 光学影像与多源重力数据，采用按水深分层的 XGBoost 模型反演浅水海底地形，缓解不同水深下反演误差分布不均的问题，提升了浅水测深的精度与空间覆盖。（Oxford / Geophysical Journal International）', 'source': 'Geophysical Journal International', 'url': 'https://doi.org/10.1093/gji/ggag421', 'date': '2026-10-07'}, {'title': '通用深度学习框架实现海洋海盐气溶胶全球时空预报', 'badge': '[论文]', 'abstract': '海盐气溶胶是海气相互作用与气候辐射收支的重要组分。研究提出可推广的深度学习框架，对海洋海盐气溶胶进行全球时空预报，刻画其时空演变规律，为海气交换研究与气候模式的气溶胶参数化提供数据驱动的预报手段。（Elsevier / JASTP）', 'source': 'Journal of Atmospheric and Solar-Terrestrial Physics', 'url': 'https://doi.org/10.1016/j.jastp.2026.106988', 'date': '2026-10-05'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': 'EDITO 携手 UN Ocean Decade 举办「迈向全球海洋数字孪生网络」边会（DITTO Summit 2026）', 'badge': '[动态]', 'abstract': '作为 DITTO Summit 2026 的边会，欧洲数字孪生海洋（EDITO）联合 Mercator Ocean International、VLIZ、Seascape Belgium，并协同 UN Ocean Decade 数据共享协调办公室（DCO-ODS）等机构，于 10 月 28-29 日举办两场在线对话，汇聚全球海洋社区就数字孪生海洋（DTO）的区域需求、期望、机遇与挑战展开交流，推动构建互联互通的全球数字海洋。', 'source': 'EDITO / EMODnet', 'url': 'https://www.edito.eu/event/edito-side-event-ditto-summit/', 'date': '2026-10-08'}, {'title': 'DTO-BioFlow：SUBSIM 海底图像分析服务与海洋数字孪生集成', 'badge': '[动态]', 'abstract': 'DTO-BioFlow 举办「海底图像分析服务」技术展示，介绍面向海洋数字孪生（DTO）的 SUBSIM 图像分析服务组合，内容涵盖其架构与功能、代码库，以及如何集成进欧洲数字孪生海洋基础设施，面向开发者、基础设施方与科研人员，支撑自主观测与计算机视觉方法在海洋生物多样性监测中的应用。', 'source': 'DTO-BioFlow', 'url': 'https://dto-bioflow.eu/', 'date': '2026-10-05'}, {'title': '欧洲数字孪生海洋（EDITO）与社会仿真社区对接（SSC 2026）', 'badge': '[动态]', 'abstract': 'EDITO 与 SEAtwins 项目 SURIMI、SEADOTs 在 Social Simulation Conference 2026 上举办专题，展示社会仿真研究者如何借助 EDITO 公共平台获取海洋数据、协作空间、免费算力与存储，从而降低社会-生态建模门槛，把 agent-based 建模与数字孪生海洋基础设施相连，服务可持续海洋治理。', 'source': 'EDITO', 'url': 'https://www.edito.eu/news/european-digital-twin-ocean-engages-the-social-simulation-community-at-ssc-2026/', 'date': '2026-10-05'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': 'SA-SRDC-Loc：单 AUV 辅助的三维水下定位', 'badge': '[论文]', 'abstract': '水下定位是海洋观测与作业的基础。研究提出 SA-SRDC-Loc，利用单台自主水下航行器（AUV）辅助实现三维水下定位，通过稀疏表示与深度约束提升在多径、浑浊等复杂水下环境中的定位精度与稳健性，为低成本水下定位与协同导航提供新思路。（Elsevier / Ocean Engineering）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128641', 'date': '2026-10-08'}, {'title': 'Copernicus Marine 产品路线图：MyOcean Pro 3D 可视化工具与 EDITO 全量集成', 'badge': '[动态]', 'abstract': 'Copernicus Marine Service 公布产品路线图：2026 年 12 月将在 MyOcean Pro 中完成对 EDITO 的全面集成，使用户可在同一环境内访问与可视化 EDITO 上存储的全部数据集（含公私数据）；2027 年 1 月将推出沉浸式 3D Viewer，除数字地球外还渲染高分辨率地形与水深数据，为海洋变量提供空间上下文；同期 MyOcean Light 将把降尺度可视化能力从模式输出扩展到观测数据。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information', 'date': '2026-10-05'}, {'title': 'ParaView 6.2.0 发布：开源科学可视化增强（延续 ONNX/AI 集成）', 'badge': '[工具]', 'abstract': 'Kitware 发布开源科学可视化软件 ParaView 6.2.0，面向大规模并行数据的交互式分析与可视化，广泛用于海洋、气候与流体仿真数据的后处理，原生支持 NetCDF/HDF 等格式并可通过 Python（pvpython）脚本化。6.x 系列引入 ANARI 多渲染后端与 ONNX 机器学习集成，本次 6.2.0 由 38 位开发者贡献。', 'source': 'Kitware / ParaView', 'url': 'https://discourse.paraview.org/t/paraview-6-2-0-is-now-available/17753/1', 'date': '2026-10-01'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA-QC', 'items': [{'title': '高效液相色谱浮游植物色素分析的精密度评估（NASA 全球水色验证数据集）', 'badge': '[论文]', 'abstract': '浮游植物色素的高效液相色谱（HPLC）分析是海洋生物地球化学研究与水色遥感定标的基础。研究针对由 NASA 分析处理的全球水色验证数据集，系统评估 HPLC 色素测定的精密度，量化不同色素与操作环节的误差来源，为色素数据的质量控制与多实验室可比性提供依据。（Copernicus / Biogeosciences）', 'source': 'Biogeosciences', 'url': 'https://doi.org/10.5194/bg-23-7043-2026', 'date': '2026-10-08'}, {'title': 'UAV 与 USV 多模态数据融合的沿岸带水深监测方法验证', 'badge': '[论文]', 'abstract': '沿岸带水深变化监测对海岸管理与防灾意义重大。研究在一次综合测量活动中，融合无人机（UAV）与无人水面艇（USV）获取的多模态地理空间数据，验证一种沿岸带水深监测方法，评估其在近岸浅水环境中的精度与适用性，为沿岸地形变化提供低成本、高频次的监测路径。（SAGE / Progress in Physical Geography）', 'source': 'Progress in Physical Geography: Earth and Environment', 'url': 'https://doi.org/10.1177/03091333261488345', 'date': '2026-10-07'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'LADDIE v2.0：南极冰-海交换动力降尺度的单层模式', 'badge': '[论文]', 'abstract': '南极冰架-海洋交换的精细模拟对海平面预估至关重要。研究发布 LADDIE v2.0（One-Layer Antarctic model for Dynamical Downscaling of Ice-ocean Exchanges），以单层垂向结构实现冰-海交换的高效动力降尺度，提升对冰架底部融化与热盐交换的模拟能力，为冰川-海洋耦合模式提供可复现的降尺度工具。（Copernicus / GMD）', 'source': 'Geoscientific Model Development', 'url': 'https://doi.org/10.5194/gmd-19-9441-2026', 'date': '2026-10-07'}, {'title': 'XRF 岩芯扫描仪高分辨率重建沉积物氧化还原变化', 'badge': '[论文]', 'abstract': '沉积岩芯的氧化还原记录是古海洋环境重建的重要载体。研究展示利用 XRF 岩芯扫描仪数据并结合深度-年龄校正，对沉积物氧化还原变化进行高分辨率重建的方法，提升古氧化还原条件代用指标的时空分辨率与可解释性，为古海洋研究提供数据处理范式。（Springer / Progress in Earth and Planetary Science）', 'source': 'Progress in Earth and Planetary Science', 'url': 'https://doi.org/10.1186/s40645-026-00851-6', 'date': '2026-10-08'}, {'title': '弱监督多源遥感的海水入侵制图', 'badge': '[论文]', 'abstract': '海水入侵威胁沿海地下水与生态安全。研究提出弱监督的多源遥感数据融合方法用于海水入侵范围制图，缓解高密度实地标签稀缺的问题，在缺乏充分采样的区域提升海水入侵识别的空间覆盖与精度。（Taylor & Francis / International Journal of Remote Sensing）', 'source': 'International Journal of Remote Sensing', 'url': 'https://doi.org/10.1080/01431161.2026.2742387', 'date': '2026-10-04'}]}, {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'NFDI4Microbiota 第二阶段资助提案：面向微生物组研究的国家研究数据基础设施', 'badge': '[论文]', 'abstract': 'NFDI4Microbiota 公布其第二阶段资助提案，规划面向微生物组研究的德国国家研究数据基础设施，涵盖数据标准、工具建设与跨机构协作，推动微生物组（含海洋微生物）数据的可发现、可互操作与可复用，为微生物多样性数据的长期管理与共享提供基础设施支撑。（Pensoft / RIO）', 'source': 'Research Ideas and Outcomes', 'url': 'https://doi.org/10.3897/rio.12.e215133', 'date': '2026-10-05'}, {'title': '整合分子方法实现北海生物多样性与生态系统动态的标准化监测', 'badge': '[论文]', 'abstract': '传统形态学监测难以满足高频、大范围的生物多样性监测需求。研究整合 eDNA 等分子方法，提出面向北海生物多样性与生态系统动态的标准化监测框架，讨论采样、质控与数据共享流程，为跨区域海洋生物多样性数据的可比性、可复用性与共享提供路径。（Springer / BMC Marine Science）', 'source': 'BMC Marine Science', 'url': 'https://doi.org/10.1186/s44479-026-00009-w', 'date': '2026-09-30'}, {'title': '海洋数据：从愿景到行动——UN Ocean Decade 数据共享指南体系', 'badge': '[报告]', 'abstract': 'UN Ocean Decade 发布「Ocean data: from vision to action」，系统梳理其数据与信息战略及配套指南体系，包括数据管理计划指南、数据出版手册，以及水深、公民科学、海洋巨型动物和社会经济数据共享指南等，为 Decade 各类行动提供负责任、开放、透明的数据共享与引用框架。', 'source': 'UN Ocean Decade', 'url': 'https://oceandecade.org/?p=24941/', 'date': '2026-10-05'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises / Scientific Expeditions', 'items': [{'title': '「蛟龙」号首赴南太平洋：中国大洋100航次第二航段起航', 'badge': '[航次]', 'abstract': '搭载「蛟龙」号载人潜水器的「深海一号」船从福建厦门起航，赴南太平洋执行中国大洋100航次第二航段科考，这是「蛟龙」号首次在南太平洋开展调查作业。本航段聚焦「数字化深海典型生境」大科学计划，通过载人深潜、CTD 采水与表层浮游生物拖网等手段开展水体与海底生态调查，预计 91 天，将获取生境分布规律与生态基线数据、填补该区域公海生态数据空白，并邀请南太平洋岛国科学家参航。（新华社）', 'source': '新华社 / 天津日报', 'url': 'https://epaper.tianjinwe.com/tjrb/html/2026-10/10/content_143082_3904097.htm', 'date': '2026-10-10'}, {'title': '「蛟龙」号第466次下潜：抵达西太平洋东加罗林海盆作业区', 'badge': '[航次]', 'abstract': '10 月 10 日，搭载「蛟龙」号载人潜水器的「深海一号」船抵达西太平洋东加罗林海盆作业区开展深海科考，实施「蛟龙」号第 466 次下潜，也是中国大洋100航次第二航段在该区域的首个潜次，计划下潜深度约 4500 米。（央视新闻 / 光明网）', 'source': '央视新闻 / 光明网', 'url': 'https://m.gmw.cn/2026-10/11/content_1304574115.htm', 'date': '2026-10-11'}, {'title': '阿根廷马德普拉塔海底初步确认发现57种海洋新物种', 'badge': '[动态]', 'abstract': '阿根廷国家科学与技术研究理事会表示，科研人员已完成「4号陆坡」科考活动样品的分析与归类，初步鉴定出 57 种可能为科学界此前未知的海洋物种，含 20 种桡足类、22 种棘皮动物、14 种刺胞动物和 1 种掘足类软体动物，并发现 5 个新属。该航次历时 21 天，对马德普拉塔海底峡谷进行考察并对水下科考进行直播。（新华社）', 'source': '新华社', 'url': 'https://www.163.com/dy/article/L88GJ77O0514R9KQ.html', 'date': '2026-10-01'}, {'title': '中国工程院「海洋装备绿色智能融合发展」研讨会在烟台召开', 'badge': '[动态]', 'abstract': '由中国工程院机械与运载工程学部主办的中国工程院工程科技学术研讨会「海洋装备绿色智能融合发展」在山东烟台召开，130 余家单位、400 余名专家现场参会。会议围绕海洋装备绿色智能制造与数字化转型、海洋信息感知获取与通信定位、海洋数据融合赋能、全球海洋数字治理等设 6 个专题论坛，李家彪等院士就深海装备与人工智能融合等作主旨报告。（中国科学报 / 科学网）', 'source': '中国科学报 / 科学网', 'url': 'https://wap.sciencenet.cn/mobile.php?cat=T&id=572507&mobile=1&type=detail', 'date': '2026-10-05'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers / Archives', 'items': [{'title': '基于 GlobColour/Copernicus Marine 产品的全球海洋透明度趋势评估（含不确定性）', 'badge': '[论文]', 'abstract': '海洋透明度（水体清澈度）是重要的生态与气候指标。研究基于 Copernicus Marine Service 的 GlobColour 产品评估全球海洋透明度的长期趋势，并系统处理与量化相关的不确定性，提升对海洋生态与碳循环变化趋势判读的可信度（收录于 Copernicus Ocean State Report）。（Copernicus / State of the Planet）', 'source': 'State of the Planet (Copernicus OSR)', 'url': 'https://doi.org/10.5194/sp-7-osr10-10-2026', 'date': '2026-09-30'}, {'title': '泛南极 NSIDC 海冰漂移产品的高分辨率 SAR 与浮标评估', 'badge': '[论文]', 'abstract': '海冰漂移产品是极区海冰与海气相互作用研究的关键数据。研究利用高分辨率 SAR 与浮标数据，对 NSIDC 海冰漂移产品开展泛南极范围的评估，检验其在不同季节与冰情下的精度与偏差，为数据产品的质量把关与改进指明方向。（Copernicus / Earth Observation）', 'source': 'Earth Observation', 'url': 'https://doi.org/10.5194/eo-1-129-2026', 'date': '2026-09-30'}]}, {'title': '九、工具与代码资源调研', 'en': 'Tools & Code Resources', 'items': [{'title': 'xCDAT v0.11.5：面向海洋/气候数据的 xarray 分析扩展库更新', 'badge': '[工具]', 'abstract': 'xCDAT 是一个基于 xarray 的气候与海洋数据分析扩展库，围绕 CF 规范提供时空坐标处理、气候学计算与水平/垂直重网格等功能，广泛用于地球系统模式与观测数据分析。项目于 2026 年 10 月 8 日发布 v0.11.5，持续修复问题并提升数据处理效率与一致性。（GitHub）', 'source': 'GitHub (xcdat/xcdat)', 'url': 'https://github.com/xcdat/xcdat/releases/tag/v0.11.5', 'date': '2026-10-08'}, {'title': 'IOOS compliance-checker 与 ioos_qc：海洋数据合规检查与质量控制开源工具更新', 'badge': '[开源]', 'abstract': '美国综合海洋观测系统（IOOS）维护的开源工具近期更新：compliance-checker 用于按 CF/ACDD 等标准检查数据集合规性，ioos_qc 实现 QARTOD 等海洋观测数据质量控制测试。二者帮助数据提供方在入库前完成合规与质控，提升海洋数据的互操作性与可复用性。（GitHub）', 'source': 'GitHub (ioos)', 'url': 'https://github.com/ioos/compliance-checker', 'date': '2026-10-09'}, {'title': 'SW1D：一维弹性介质地震面波求解的 Python 包', 'badge': '[开源]', 'abstract': '研究发布 SW1D，一个用于求解一维弹性介质中地震面波（频散/本征）解的 Python 包，面向海洋地球物理与地壳结构反演等场景，提供可复现、易集成的开源实现，便于研究者开展面波频散正演与反演分析。（arXiv）', 'source': 'arXiv', 'url': 'https://arxiv.org/abs/2610.02194', 'date': '2026-10-01'}]}]



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
