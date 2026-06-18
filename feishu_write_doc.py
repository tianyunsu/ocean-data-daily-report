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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '中国新型海洋AI模型取得突破——琅琊2.0海洋大模型发布，珊瑚监测+船体清洁机器人出海（China Daily, 2026-06-16）', 'badge': '[要闻]', 'abstract': '中国在海洋AI领域取得多项突破：中国科学院海洋研究所在数字地球大会上发布LangYa 2.0（琅琊2.0）海洋大模型，可预报台风、降水、海冰和风暴潮等多种海洋现象，24小时预报精度提升超10%，并支持轻量化版本部署服务发展中地区。海南大学与Robotfish合作部署水下机器人对珊瑚礁进行全天候监测，替代传统人工潜水。威海智真海洋科技研发的第四代水下清洁机器人可在150米深度作业，每小时清洁2000平方米船体，2025年已在马六甲海峡服务逾1000艘船只。海洋科技已被列为"十五五"规划（2026-2030）战略重点。', 'source': 'China Daily', 'url': 'https://www.chinadaily.com.cn/a/202606/16/WS6a30abe0a310986e2b460302.html', 'date': '2026-06-16'}, {'title': 'arXiv: KFTD——Koopman-傅里叶时间可微网络实现连续海洋时空预测（2026-06-06）', 'badge': '[论文]', 'abstract': '提出KFTD（Koopman-Fourier Time-Differentiable）网络，一种时间连续的两阶段范式，将插值与预测解耦实现高效时空建模。方法将复杂非线性海洋动力学映射至Koopman线性空间，利用傅里叶分析实现任意子步长的连续时间插值，轻量残差网络利用高保真中间状态生成最终预报。相比扩散模型消除了多步噪声采样，计算速度提升4倍。引入DPP Loss支持任意PDE约束端到端训练。在四个海洋数据集实验表明，连续时间框架平均降低5.6%MSE，海表温度SST降低高达12.7%，效率相较MCVD提升76.25%。arXiv: 2606.17070。', 'source': 'arXiv (physics.ao-ph)', 'url': 'https://arxiv.org/abs/2606.17070', 'date': '2026-06-06'}, {'title': 'arXiv: CMIP-Forge——自主体系统实现气候与海洋科学文献检索、计算与自我审查（2026-06-10）', 'badge': '[论文]', 'abstract': '提出CMIP-Forge混合检索增强生成（RAG）与自主分析系统，桥接科学文献与ESGF数据档案间的鸿沟。系统在6581篇CMIP6相关开放获取论文（101828个索引块）语料库上构建智能体流水线：由工具增强的工作器规划并执行基于实时气候数据的Python工作流，独立审稿模型对方法论进行端到端审计。引入多层"纵深防御"架构，通过AST静态分析、经审计的科学原语和自主对抗性同行评审协议强制实施物理和方法论不变量。系统展示了涵盖大气遥相关、海洋动力学、区域极端事件和全球变暖预估的端到端自主研究能力。arXiv: 2606.17076。', 'source': 'arXiv (physics.ao-ph)', 'url': 'https://arxiv.org/abs/2606.17076', 'date': '2026-06-10'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin / Marine Digital Twin', 'items': [{'title': 'Copernicus Marine完整发布"理解我们的海洋"系列I-V——从数据采集到数字孪生的全链条科普（CMEMS, 2026年5-6月）', 'badge': '[科普]', 'abstract': '哥白尼海洋服务（CMEMS）自5月下旬起连续发布五篇科普系列"理解我们的海洋"（Understanding Our Ocean），从海洋数据采集（II，5月26日）、海洋预测（III，5月29日）、海洋数据产品、"理解我们的海洋 IV"数字孪生海洋（6月8日）到全球合作扩展（6月5日），完整呈现从卫星观测-原位数据-AI预测-数字孪生-全球服务的全链条技术路径。其中数字孪生篇系统介绍了欧洲数字孪生海洋（EU DTO）架构：融合卫星数据+多源传感器+AI，目标2030年全面运行。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/news', 'date': '2026-06-08'}, {'title': 'DITTO 2026国际峰会摘要提交进行中——六大主题推动可互操作数字孪生（截止7月20日，11月横滨）', 'badge': '[会议]', 'abstract': '联合国海洋十年DITTO计划第三届国际峰会摘要提交已开放逾两周（6月5日起），截止7月20日。六大核心主题：数据观测与建模、数字基础设施与互操作性、AI自动化与优化、跨行业应用、运营系统与工业部署、集成地球-社会系统框架。峰会将于2026年11月11-13日在日本横滨举行，汇集全球研究人员、政策制定者和行业领袖。目前摘要提交持续进行中，是海洋数字孪生社区年度最重要学术交流平台。', 'source': 'JAMSTEC / DITTO / UN Ocean Decade', 'url': 'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/', 'date': '2026-06-05'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization / Geospatial Display', 'items': [{'title': 'Ocean Virtual Laboratory (OVL)——基于Syntool开源Web引擎的实时海洋卫星+模型+原位数据可视化平台（OceanDataLab, 持续运行）', 'badge': '[工具]', 'abstract': 'Ocean Virtual Laboratory门户基于Syntool开源Web查看器，由OceanDataLab维护，提供海洋卫星数据（Sentinel-1/2/3、MODIS、VIIRS等）、模型输出（CMEMS等）和原位观测的实时交互式可视化服务。Syntool采用GNU AGPL开源许可，支持多源数据叠加显示，用户可直接在浏览器中探索全球海洋温度、盐度、叶绿素、海面高度等状态参数，为海洋遥感数据的快速浏览和科学分析提供了便捷入口。', 'source': 'OceanDataLab', 'url': 'https://ovl.oceandatalab.com/', 'date': '2026-06-17'}, {'title': 'DiDiT 2026分布式数字孪生研讨会联合IISE举行——数字孪生可视化与智能环境前沿（6月15-18日，里斯本）', 'badge': '[会议]', 'abstract': '第六届分布式数字孪生（DiDiT 2026）研讨会于6月15-18日在葡萄牙里斯本举行，与第22届智能环境国际会议（IISE）联合举办。研讨会聚焦数字孪生的分布式架构、交互式可视化以及跨系统互操作性。虽然DiDiT面向通用数字孪生，但其讨论的分布式可视化框架和数据流架构对海洋数字孪生（DTO）的可视化呈现具有重要参考价值，特别是在多源异构海洋数据的实时融合展示方面。', 'source': 'DiDiT 2026 / IISE', 'url': 'https://distributeddigitaltwins.github.io/', 'date': '2026-06-15'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality Control', 'items': [{'title': 'npj Ocean Sustainability：全球海洋观测的五种未来情景——威胁与新生机遇并存（Nature旗下, 2026-06-17）', 'badge': '[论文]', 'abstract': 'Lehman等人基于2025年6月联合国第三届海洋大会（法国尼斯）民族志调查数据，提出了全球海洋观测未来发展的五种情景，发表在Nature旗下npj Ocean Sustainability期刊。文章指出，海洋观测对科学和蓝色经济至关重要，但美国政府对关键项目的预算削减提案正威胁其稳健性。研究强调当前海洋观测正面临威胁与不稳定，但同时也可能出现新参与者和新优先事项的机遇窗口。开放获取（CC BY 4.0），由美国国家科学基金会等机构资助。', 'source': 'npj Ocean Sustainability (Nature)', 'url': 'https://www.nature.com/articles/s44183-026-00219-9', 'date': '2026-06-17'}, {'title': 'IOOS QARTOD实时海洋数据质量控制手册体系——覆盖从pH到海流的13类全变量QC标准（NOAA, 持续更新）', 'badge': '[标准]', 'abstract': '美国综合海洋观测系统（IOOS）QARTOD项目已建立覆盖13类主要海洋变量的实时数据质量控制手册体系，包括pH、溶解氧、温度/盐度、波浪、海流、高频雷达、被动声学、海洋光学、浮游植物、水位、风、营养盐和河流流量等。配套QARTOD数据标志手册v1.2提供标准化质量控制标志体系。2026年项目计划继续推进碳系统参数（pCO2）等新变量的QC标准制定，为全球Argo、Glider等自主观测平台的自动化数据质量控制提供标准化方法。', 'source': 'NOAA IOOS / QARTOD', 'url': 'https://ioos.noaa.gov/project/qartod/', 'date': '2026-06-05'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing / Computing', 'items': [{'title': '第六届国际遥感电子会议（ECRS 2026）——AI遥感+SAR+环境遥感八大专场，摘要截止今日6月18日（MDPI, 10月在线举行）', 'badge': '[会议]', 'abstract': '第六届国际遥感电子会议（ECRS 2026）将于2026年10月19-21日在线举行，主题为"下一代地球观测的全球视角"，免注册费。设八大专场：AI在遥感中的应用（主席：武汉大学邵振峰）、SAR遥感、半干旱地区遥感、热带地区遥感、城市地区遥感、环境遥感、文化遗产保护遥感、遥感视觉问答（RSVQA）。摘要提交截止今日6月18日，7月17日接收通知。最佳口头/海报报告奖各6名（CHF 200+证书）。会议论文集可免版面费发表在Environmental and Earth Sciences Proceedings。', 'source': 'MDPI Remote Sensing (IF=4.1)', 'url': 'https://sciforum.net/event/ECRS2026', 'date': '2026-06-18'}, {'title': 'Ocean Engineering: SAR图像船舰检测深度学习综述——全天候全天时海洋目标识别最新进展（ScienceDirect, 2026-05）', 'badge': '[综述]', 'abstract': '发表在Ocean Engineering的综述系统回顾了合成孔径雷达（SAR）图像中深度学习船舰检测的最新进展。SAR具备全天候全天时海洋观测能力，船舰检测是海洋工程的关键任务。论文涵盖从经典CFAR到现代YOLO系列、Faster R-CNN、Transformer等方法的完整发展脉络。同期arXiv预印本OceanSAR-2（arXiv: 2601.07392）提出通用SAR海洋特征提取器，在海面风场、有效波高等下游任务中表现优异，为海洋遥感数据处理提供了统一框架。', 'source': 'ScienceDirect / Ocean Engineering', 'url': 'https://www.sciencedirect.com/science/article/pii/S0029801826008796', 'date': '2026-05-15'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'IOC海洋数据与信息管理战略计划（2023-2029）持续实施——构建"数字海洋生态系统"（IODE / UNESCO, 持续推进）', 'badge': '[战略]', 'abstract': '联合国教科文组织政府间海洋学委员会（IOC）的海洋数据与信息管理战略计划（2023-2029）持续推进实施。该计划收录于IOC手册与指南第92号，自2008年首次发布以来定期修订。核心目标：建设可互操作的"数字海洋生态系统"，实现数据共享与管理标准化，利用历史、实时和模型数据描述海洋状况并支持预测，识别知识空白优化数据利用。计划与联合国海洋科学十年（2021-2030）密切协作，推动全球海洋数据基础设施显著提升。', 'source': 'IOC / IODE / UNESCO', 'url': 'https://iode.org/ioc-strategic-plan-for-ocean-data-and-information-management/', 'date': '2026-06-17'}, {'title': '欧盟Blue-Cloud 2026项目——构建FAIR与开放海洋数据的联邦欧洲生态系统（Horizon Europe, 持续推进）', 'badge': '[项目]', 'abstract': '欧盟Horizon Europe资助的Blue-Cloud 2026项目旨在将Blue-Cloud试点项目进一步发展成联邦化欧洲生态系统，提供FAIR（可查找、可访问、可互操作、可复用）和开放的海洋数据及分析服务。项目围绕三大支柱：构建由分布式数据基础设施组成的蓝色数据基础设施联邦、开发协作式分析环境、建立Open Science实践社区。通过连接EMODnet、Copernicus Marine、SeaDataNet等现有欧洲海洋数据管理基础设施，推动海洋数据的无缝发现、访问和重用。', 'source': 'European Commission / CORDIS', 'url': 'https://cordis.europa.eu/project/id/101094227', 'date': '2026-06-05'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises / Research Expeditions', 'items': [{'title': 'NOAA EX2604太平洋岛屿深海测绘制图航次——Okeanos Explorer，6月16日-7月9日，夏威夷至库克群岛（NOAA Ocean Exploration）', 'badge': '[航次]', 'abstract': 'NOAA Ocean Exploration旗舰航次EX2604于6月16日从夏威夷出发，执行太平洋岛屿深海测绘制图任务，持续至7月9日。使用NOAA Ship Okeanos Explorer，航线覆盖夏威夷群岛、金曼礁与帕尔米拉环礁、贾维斯岛及库克群岛的深水区域。该航次是2026年度Okeanos Explorer继4-5月测绘设备试航和5-6月ROV试航后的首次正式科学测绘任务。同期，E/V Nautilus 2026年野外作业季也在6月至10月开展，覆盖中太平洋和西太平洋深海栖息地。', 'source': 'NOAA Ocean Exploration', 'url': 'https://oceanexplorer.noaa.gov/explorations/explorations.html', 'date': '2026-06-16'}, {'title': 'SOI"特立尼达和多巴哥深海奇观"科考——Falkor (too)探索加勒比未知深海生态系统（6月29日-7月28日）', 'badge': '[航次]', 'abstract': '施密特海洋研究所（SOI）2026年西南大西洋系列航次第五航段将在特立尼达和多巴哥周边水域及邻近公海开展。该国有93%的海域位于休闲潜水深度以下，大部分从未被探索过。团队将寻找化能合成栖息地（甲烷渗漏、泥火山）和中深层珊瑚礁，同时测试一种新型低温保存技术（-20°C冷冻保护剂），验证其作为海洋无脊椎动物冷冻保存标准方法的可行性。特别装备低成本深海成像系统DORIS。首席科学家为Dr. Diva Amon。', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/', 'date': '2026-06-29'}, {'title': 'AEROSE 2026大气溶胶与海洋科学航次启航——6月15日-8月，跨大西洋研究气溶胶-海洋相互作用（ASU / NOAA）', 'badge': '[航次]', 'abstract': '2026年气溶胶与海洋科学航次（AEROSE）于6月15日出发，持续至8月，跨大西洋作业。AEROSE致力于研究撒哈拉沙尘等大气溶胶对海洋生态系统的影响。航次搭载学生培训计划，由亚利桑那州立大学（ASU）联合NOAA等机构组织。航次收集的海洋化学、生物光学和气溶胶数据将用于改进卫星海洋颜色反演算法和海洋碳循环模型，同时承担研究生和早期科研人员的海上培训任务。', 'source': 'Arizona State University / NOAA', 'url': 'https://newcollege.asu.edu/sites/g/files/litvpz266/files/2026-02/2026%20AEROSE%20%20Student%20Opp.pdf', 'date': '2026-06-15'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers / Infrastructure', 'items': [{'title': 'GEBCO_2026全球海底地形网格正式发布——15弧秒分辨率，新增冰下地形/测深版本（2026年4月23日）', 'badge': '[数据]', 'abstract': '全球海洋通用测深图（GEBCO）于2026年4月23日发布GEBCO_2026 Grid，以15弧秒（约400m）全球网格分辨率提供海洋和陆地高程数据。新增亮点：首次提供格陵兰和南极地区冰下地形/测深版本（sub-ice topo/bathy），配合类型标识符网格（TID Grid）标注源数据类型，并提供测试版多分辨率网格产品。数据支持netCDF、GeoTiff和ASCII格式下载，可通过NERC CEDA平台的OPeNDAP协议访问。GEBCO Grid每年发布一次，置于公共领域免费使用。', 'source': 'GEBCO / Nippon Foundation / NERC', 'url': 'https://www.gebco.net/data_and_products/gridded_bathymetry_data/', 'date': '2026-04-23'}, {'title': '中国首个风电驱动海底数据中心在上海附近海域启用——应对AI能耗挑战的海洋基础设施新范式（2026年6月9日）', 'badge': '[设施]', 'abstract': '中国在AI能耗需求增长背景下，正式启用首个风电驱动的海底数据中心，位于上海附近海域。该海底数据中心利用海水自然冷却和海上风电供电，比传统陆地数据中心节能约30-40%。海底部署还带来更低的网络延迟（靠近沿海城市）和更高的物理安全性。这一创新标志着海洋空间利用从传统科研观测扩展到支撑数字经济的海底基础设施领域，为全球应对AI时代的数据中心能耗挑战提供了海洋方案。', 'source': 'Creati.ai / RaillyNews', 'url': 'https://creati.ai/ai-news/2026-06-09/wind-powered-underwater-data-center-opens-in-china/', 'date': '2026-06-09'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'Open Ocean Software——NSF资助的海洋机器人开源软件生态系统正式启动（AUV/Glider/Mooring全栈工具, 2026年6月）', 'badge': '[开源]', 'abstract': 'Open Ocean Software是美国NSF"Pathways to Enable Open-Source Ecosystems"计划资助的海洋机器人开源软件项目，聚焦自主水下航行器（AUV）、水面无人艇（USV）、系泊浮标、漂流器及相关传感器、数据采集和仿真软件的开发与标准化。项目于2026年6月建立社区论坛（forum.oceansoft.org），汇集海洋机器人开源开发者，推动仿真环境选择、传感器标准化等议题。GitHub开源仓库（github.com/openocean-software）持续更新中。', 'source': 'Open Ocean Software / NSF', 'url': 'https://oceansoft.org/', 'date': '2026-06-08'}, {'title': 'Pangeo地球科学大数据生态系统——Python开源工具栈服务海洋/大气/气候数据处理与分析（持续更新）', 'badge': '[工具]', 'abstract': 'Pangeo项目提供面向地球科学大数据的Python开源工具生态系统，涵盖海洋、大气、陆地和气候科学领域。核心组件包括Xarray（多维数组分析）、Dask（并行计算）、Jupyter（交互式分析环境）和Zarr（云原生数据存储）。Pangeo通过Binder/JupyterHub提供云基础设施支持，允许用户在不下载数据的情况下直接在云端分析和可视化大规模海洋数据集（如CMIP、Argo、卫星数据等），是海洋数据分析的首选工具栈之一。', 'source': 'Pangeo Project / EarthCube', 'url': 'https://www.earthcube.org/products', 'date': '2026-06-17'}]}]

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
