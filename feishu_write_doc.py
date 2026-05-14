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

yesterday_cn = (datetime.now()).strftime('%Y\u5e74%m\u6708%d\u65e5')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [
  {'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [
    {'title': 'Nature Communications（2026-05-11）：低云反馈在不可逆海平面上升中的关键作用', 'badge': '近7天', 'abstract': '发表于Nature Communications的研究揭示了海洋热量积累诱导的海表温度格局变化及相关的正反馈机制在维持数百年尺度海平面上升中的关键作用——即使在气候减排努力之后也不可逆转。研究强调了即使实现碳中和，低云反馈和海洋热吸收模式仍将继续推动长期海平面上升，对沿海规划和适应策略具有重要启示。DOI: 10.1038/s41467-026-72898-4', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72898-4', 'date': '2026-05-11'},
    {'title': 'Nature Communications（2026-05-07）：热带气旋年最大强度存在次表层"信使"——可提前数年预测', 'badge': '近7天', 'abstract': '中国海洋大学倪欣宁、张宇、王伟团队在Nature Communications发表研究，揭示西北太平洋热带气旋年最大生命周期最大强度（LMI）与一个次表层水团的温度存在强烈关联，呈多年代际V型结构。该水团在北太平洋高压中心下形成并经约4年次表层路径输运至西边界，其高变异热含量调制风暴下方的海表温度。基于北太平洋高压强度可提前数年预测年最大LMI。DOI: 10.1038/s41467-026-72770-5', 'source': 'Nature Communications / Ocean University of China', 'url': 'https://www.nature.com/articles/s41467-026-72770-5', 'date': '2026-05-07'},
    {'title': '北京大学物理学院（2026-05-13）：AI赋能海洋环流预报——中国海洋大学荆钊教授主讲', 'badge': '近7天', 'abstract': '中国海洋大学/崂山实验室荆钊教授应北京大学物理学院邀请主讲"AI赋能的海洋环流预报"。荆钊教授主要从事海洋中小尺度动力过程及其预测研究，在Nature、Nature Geoscience等国际权威期刊发表多项成果。报告聚焦人工智能技术在海洋环流预报中的前沿应用，探讨如何通过深度学习方法提升海洋中尺度过程的预测能力。', 'source': '北京大学物理学院', 'url': 'https://www.phy.pku.edu.cn/info/1348/15742.htm', 'date': '2026-05-13'},
  ]},
  {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
    {'title': 'Ocean Engineering（2026-05-01）：深度学习增强模拟推理——提升船舶数字孪生精度与效率', 'badge': '近7天', 'abstract': '发表于Ocean Engineering的研究提出深度学习增强模拟推理（DL-SBI）框架，通过神经网络逼近昂贵物理模拟器的后验分布，显著提升船舶数字孪生的精度、适应性和计算效率。研究在仿真验证环境中展示了该框架用于参数估计和状态推断的能力，旨在应用于真实数字孪生环境中，为自主航运和智能船舶运维提供技术支撑。', 'source': 'Ocean Engineering / Elsevier', 'url': 'https://www.sciencedirect.com/science/article/pii/S0141118726001677', 'date': '2026-05-01'},
    {'title': 'Journal of Marine Science and Application（2026-05-11）：数字孪生支持自主船舶智能移动的挑战与机遇', 'badge': '近7天', 'abstract': '发表于Springer旗下JMSA的综述论文系统回顾了自主船舶现行规则、导航及路径跟随系统，分析了数字孪生作为工业4.0新兴技术（融合AI、ML与大数据）在复杂海上交通环境中的应用潜力。研究指出数字孪生可通过整合宏观交通信息加速自主船舶发展，提升运营安全与效率，并为海洋脱碳提供机遇。DOI:10.1007/s11804-026-00799-5', 'source': 'Journal of Marine Science and Application / Springer', 'url': 'https://link.springer.com/article/10.1007/s11804-026-00799-5', 'date': '2026-05-11'},
  ]},
  {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [
    {'title': 'Nature Communications（2026-05-07）：南极冰架融化敏感性受渠道地形放大——海平面风险新认知', 'badge': '近7天', 'abstract': '发表于Nature Communications的研究利用高分辨率建模揭示，南极冰冷冰架可能比此前认为的更加脆弱。海底小规模渠道会困住温暖海水并放大融化效应，触发促进渠道进一步增长的正反馈，从而增加冰架弱化和海平面上升的风险。这一发现对全球海平面预测具有重要意义。DOI: 10.1038/s41467-026-71828-8', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-71828-8', 'date': '2026-05-07'},
    {'title': 'Nature Communications（2026-05-06）：南极出口冰川由表面融水输入驱动加速——原位数据验证', 'badge': '近7天', 'abstract': '研究团队在南极出口冰川接地线附近钻探钻孔，测量了冰川底部的静水压力。原位数据证实了融水驱动的底部压力上升和冰川加速现象，为理解南极冰盖稳定性提供了直接证据。这是南极东部冰川动力学研究的突破性进展。DOI: 10.1038/s41467-026-72724-x', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72724-x', 'date': '2026-05-06'},
    {'title': 'NOAA NCEI / AWS（2026-05-12）：NCEI启动史上最大规模云迁移——全部数据和服务将迁移至AWS', 'badge': '近7天', 'abstract': 'NOAA国家环境信息中心（NCEI）宣布将全部数据、产品和服务迁移至亚马逊云服务（AWS），为期10个月。NCEI拥有全球最大的环境数据库之一，每月归档超229TB数据，数据来源覆盖130+观测平台。迁移完成后，用户将可通过按需访问数据（无需下载），显著提升AI/ML应用场景下的数据利用效率。', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/cloud-migration', 'date': '2026-05-12'},
  ]},
  {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [
    {'title': 'Journal of Oceanography（2026-04-29）：基于路径签名的Argo剖面自动质量控制方法改进——ML融合提升检测稳健性', 'badge': '近7天', 'abstract': 'JAMSTEC团队在Journal of Oceanography发表研究，改进了基于路径签名（path-signature）的Argo自动质量控制方法，融入新的机器学习技术。关键发现：使用2016年数据集训练的模型在2017-2021年间表现稳健，表明方法成功学习了QC通用特征，能准确识别错误剖面，接近Argo数据中心水平。该方法可快速生成中等质量数据集，填补实时数据发布与人工QC之间的时间空白。DOI: 10.1007/s10872-026-00791-1', 'source': 'Journal of Oceanography / JAMSTEC / Springer', 'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1', 'date': '2026-04-29'},
    {'title': 'ESSD预印本（2026-05-12）：BGC-Argo+——含二次质量控制的全球生物地球化学Argo浮标数据集', 'badge': '近7天', 'abstract': '夏威夷大学团队在ESSD发表预印本，提出BGC-Argo+数据集——对截至2025年1月的2429个BGC-Argo浮标数据进行了自动与人工结合的异常值检测（重点针对O2、硝酸盐和pH值），并提供剔除异常值后的统一剖面和网格化数据存储库。该数据集是当前最大规模的经二次QC的BGC-Argo数据集合，数据可通过bgc-argo-plus.info获取，讨论截止至2026年6月19日。', 'source': 'Earth System Science Data / Copernicus', 'url': 'https://essd.copernicus.org/preprints/essd-2026-311/', 'date': '2026-05-12'},
  ]},
  {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [
    {'title': 'Copernicus Marine Service（2026-04-29）：产品路线图更新——加拿大东海岸48小时逐时海洋预报产品7月上线', 'badge': '近7天', 'abstract': 'CMEMS发布产品路线图更新，宣布7月将上线全新加拿大东海岸（NWATL）近实时海洋物理和海冰预报产品（NWATL_ANALYSISFORECAST_PHY_ICE_017_001），空间分辨率0.027度，提供48小时逐时瞬时文件，每日发布4次。同时FY-3E WindRAD风场散射计L3数据集将纳入全球风场产品序列，SWH有效波高月产品从2度提升至0.5度/6小时分辨率。Sentinel-1C将加入风暴检测联合星座。', 'source': 'Copernicus Marine Service / EUMETSAT', 'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information', 'date': '2026-04-29'},
    {'title': 'IOCCG（2026-05）：NASA PACE卫星任务OCI多级产品大规模重新处理进行中', 'badge': '近7天', 'abstract': 'NASA PACE（浮游生物、气溶胶、云和海洋生态系统）卫星任务正在推进大规模数据重新处理，涵盖OCI Version 3.0.2 Level-1B/1C数据、OCI Version 3.2 Level-2/3水生地球物理产品，以及HARP2和SPEXone Version 4.0全级别产品。这是自PACE卫星发射以来最全面的数据重新处理，将显著提升海洋水色遥感和气溶胶观测数据的产品质量。PACE应用研讨会第6届录像已存档，5月14日将举行社区季度电话会。', 'source': 'IOCCG / NASA PACE Mission', 'url': 'https://ioccg.org/2026/05/may-2026/', 'date': '2026-05-01'},
  ]},
  {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [
    {'title': 'NOAA Ocean Explorer / AOML（2026-05-05）：NOAA发布首套深海eDNA数据集——NCBI+OBIS+GBIF三库全覆盖', 'badge': '近7天', 'abstract': 'NOAA海洋探索办公室联合AOML、史密森尼国家系统学实验室等机构，正式发布来自Okeanos Explorer号2021-2023年太平洋和大西洋探险的深海环境DNA数据集。原始序列可在NCBI BioProject（PRJNA1284389）获取，物种鉴定通过OBIS发布，数据同时在GBIF注册（ID:9806a672-b859-4175-8432-f805b5ce8f30），实现三大国际生物多样性数据库的全覆盖共享。NOAA将于5月28日举办专题网络研讨会。', 'source': 'NOAA Ocean Explorer / AOML / Smithsonian', 'url': 'https://oceanexplorer.noaa.gov/news/from-seawater-to-sequences-exploring-noaas-new-deep-sea-environmental-dna-dataset/', 'date': '2026-05-05'},
    {'title': 'Seabed 2030（2026-04-20）：全球海底测绘达28.7%——年增近500万平方公里创纪录', 'badge': '近7天', 'abstract': '日本财团-GEBCO Seabed 2030项目宣布全球海底已测绘面积达28.7%，过去一年新增近500万平方公里（创年度纪录）。220个组织参与贡献，新增15个贡献者。ROPME海域覆盖率从6.4%增长至20.5%。主要数据来自NOAA-NCEI、PANGAEA、JAMSTEC、巴西海军水道测量局及卫星测深。GEBCO_2026 Grid已于4月27日正式发布可下载。累计约1.04亿平方公里海底数据整合至免费GEBCO网格。', 'source': 'Seabed 2030 / The Nippon Foundation-GEBCO', 'url': 'https://seabed2030.org/2026/04/20/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year/', 'date': '2026-04-20'},
  ]},
  {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
    {'title': 'NOAA Ocean Exploration（2026-05-14至06-05）：Okeanos Explorer号ROV系统测试航次启航——夏威夷海域', 'badge': '近7天', 'abstract': 'NOAA Ocean Exploration宣布Okeanos Explorer号将于5月16日至6月5日在夏威夷海域开展ROV系统测试航次（EX2603），对ROV系统的机械、电气和软件组件进行全面压力测试，确保2026年勘探季正常运行。在此之前，Okeanos Explorer已于4月29日至5月6日完成测绘系统测试航次（EX2602）。同时，E/V Nautilus 2026航季将于6-10月探索中太平洋和西太平洋深海栖息地。', 'source': 'NOAA Ocean Exploration / OET', 'url': 'https://oceanexplorer.noaa.gov/expeditions/', 'date': '2026-05-14'},
    {'title': '央视新闻（2026-05-10）："探索一号"搭载"奋斗者"号完成全球深渊探索计划太平洋穿越航次返回广州', 'badge': '近7天', 'abstract': '由中科院深海所牵头的"全球深渊探索计划"太平洋穿越科考航次圆满完成。"探索一号"科考船搭载"奋斗者"号载人潜水器历时156天、总航程超4万公里返回广州。航次期间完成了首次中国-智利阿塔卡马海沟载人深潜联合科考，下潜63次。这是我国深海科技力量持续挺进全球深渊、深化国际海洋科技合作的重要实践，也是推动构建海洋命运共同体的标志性成果。', 'source': '央视新闻 / 新浪财经', 'url': 'https://finance.sina.com.cn/wm/2026-05-10/doc-inhxmqsf9664638.shtml', 'date': '2026-05-10'},
    {'title': '深圳特区报（2026-05-13）："深蓝百万里"2026西太平洋航次圆满收官——首次在深圳设立深海样品库', 'badge': '近7天', 'abstract': '作为联合国"海洋十年"贡献项目，"深蓝百万里"十年计划科学考察队圆满完成2026西太平洋航次45天科考任务返回深圳。科考船"向阳红10"号于3月28日启航，32人团队来自16家单位、13个科研团队。主要成果：投放Argo浮标（数据纳入国际Argo计划共享）、CTD海水取样、重力柱/箱式沉积取样、在东菲律宾海盆哥斯拉区完成拖网岩石取样（发现全球最大海底拆离断层露面），全程走航式海气通量观测。首次在深圳设立"深海样品库"由南科大/深圳海洋大学（筹）管理。', 'source': '深圳新闻网 / 深圳特区报', 'url': 'https://www.sznews.com/news/content/2026-05/13/content_32048157.htm', 'date': '2026-05-13'},
  ]},
  {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [
    {'title': 'Nature Communications（2026-05-04）：AMOC减缓调节变暖气候中的大气河流——北加州冬季降水将显著增加', 'badge': '近7天', 'abstract': '利用21世纪气候模型预测，研究表明大西洋经向翻转环流（AMOC）的减弱将增加中纬度大气河流的频率，尤其影响北美西海岸。这将导致加州冬季降水驱动的极端降水显著增加，凸显了海洋环流变化对区域气候的深远影响及其对社会经济的影响。DOI: 10.1038/s41467-026-72555-w', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72555-w', 'date': '2026-05-04'},
    {'title': 'NCEI / NOAA（2026-05-12）：NCEI启动史上最大规模云迁移——全部数据和服务将迁移至AWS', 'badge': '近7天', 'abstract': 'NOAA国家环境信息中心（NCEI）宣布将全部数据、产品和服务迁移至亚马逊云服务（AWS），为期10个月。NCEI拥有全球最大的环境数据库之一，每月归档超229TB数据，数据来源覆盖130+观测平台。迁移完成后，用户将可通过按需访问数据（无需下载），显著提升AI/ML应用场景下的数据利用效率。迁移期间偶发数据延迟可能发生，NCEI已同步发布云迁移FAQ。', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/cloud-migration', 'date': '2026-05-12'},
    {'title': 'NCEI / NOAA（2026-05-06）：NOAA发布更新版ADT-HURSAT飓风分析数据集——扩展至2024年', 'badge': '近7天', 'abstract': 'NCEI联合威斯康星大学麦迪逊分校/CIMSS发布更新版ADT-HURSAT（Advanced Dvorak Technique-Hurricane Satellite）数据集，将HURSAT数据扩展至2024年。该数据集结合全球均质化HURSAT存档与先进Dvorak技术，提供自1978年以来跨时间和地理的标准化风暴强度信息，支持长期历史分析和行业风险评估。NCEI同步发布了配套的Python Jupyter Notebook教程，通过GitHub Data Tour Notebooks项目提供交互式数据探索环境。', 'source': 'NOAA NCEI / UW-Madison CIMSS', 'url': 'https://www.ncei.noaa.gov/news/noaa-releases-updated-dataset-hurricane-analysis', 'date': '2026-05-06'},
    {'title': 'Copernicus Marine Service（2026-05-09）：第9版哥白尼海洋状况报告（OSR 9）上线——海洋极端事件与生态系统影响全面评估', 'badge': '近7天', 'abstract': '第9版哥白尼海洋状况报告（OSR 9）已正式发布并上线交互式摘要，全面揭示了破纪录的海洋极端事件、加速的变化趋势以及对海洋生态系统和社会的日益增长影响。报告重点关注2023和2024年极端事件，涵盖海洋热浪、海平面上升、海洋酸化、冰雪覆盖变化等关键指标，附有可交互的数据可视化摘要。OSR 9是全球海洋环境状况最权威的定期评估之一，报告和交互式摘要均可免费获取。', 'source': 'Copernicus Marine Service / Mercator Ocean International', 'url': 'https://marine.copernicus.eu/osr9-summary/flipbook/', 'date': '2026-05-09'},
  ]},
  {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [
    {'title': 'OSGeo（2026-05-08）：GDAL 3.13.0 "Iowa City"发布——新增Zarr V3、COG写入、SAR CPHD驱动等多项重要功能', 'badge': '近7天', 'abstract': '开源地理空间数据抽象库GDAL发布3.13.0版本，新增10余个gdal CLI子命令（gdal vector combine/dissolve/sort、gdal driver cog/gpkg validate等）；Zarr V3支持显著增强（sharding、multiscales、空间扩展）；新增COG随机写入、E57 2D影像读取、SAR CPHD多维数据读取等驱动；S102/S104/S111新增写入能力；INTERLIS 2.4格式支持。GDAL是海洋/气象NetCDF、GeoTIFF、Shapefile等数据处理的基础工具库。', 'source': 'OSGeo / GitHub', 'url': 'https://github.com/OSGeo/gdal/releases', 'date': '2026-05-08'},
    {'title': 'IOCCG / NASA（2026-05-05）：HyperCP v1.2.15发布——PACE高光谱数据社区处理器新增完整不确定性传播', 'badge': '近7天', 'abstract': 'NASA HyperInSPACE社区处理器（HyperCP）发布v1.2.15版本，为所有L2产品引入基于仪器类别和传感器型号的不确定性预算分解（含绝对辐射定标、杂散光、线性度、偏振、热响应等贡献项）。新增海面闪烁校正和BRDF校正方法。扩展自主平台支持（SolarTracker、pySAS、DALEC）。实验室标定由FRM4SOC倡议联合爱沙尼亚塔尔图大学和英国国家物理实验室完成。GitHub: github.com/nasa/HyperCP', 'source': 'IOCCG / NASA', 'url': 'https://github.com/nasa/HyperCP', 'date': '2026-05-05'},
    {'title': 'NCEI / NOAA（2026-05-06）：Data Tour Notebooks项目——ADT-HURSAT数据集交互式Python探索教程开源', 'badge': '近7天', 'abstract': 'NOAA NCEI在GitHub发布Data Tour Notebooks项目（github.com/NCEI-NOAAGov/data-tour-notebooks），提供基于Jupyter Notebook的交互式数据探索教程，首个教程聚焦ADT-HURSAT飓风分析数据集。用户可直接在Google Colab或本地运行Notebook，学习如何用Python加载、可视化和分析飓风强度数据，无需专业平台或深厚编程背景。这是NCEI推动数据可访问性和全民数据素养的系列举措之一。', 'source': 'NOAA NCEI / GitHub', 'url': 'https://github.com/NCEI-NOAAGov/data-tour-notebooks', 'date': '2026-05-06'},
  ]},
]

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
        
        print(f"写入第 {batch_idx + 1}/{total_batches} 批 ({batch_start}-{batch_end} 共{len(blocks)}个块)...")
        
        for attempt in range(max_retries):
            try:
                resp = requests.post(
                    base_url, 
                    headers=headers, 
                    json={"children": batch_blocks, "index": batch_start},
                    timeout=120
                )
                if resp.status_code == 200:
                    print(f"  第 {batch_idx + 1} 批写入成功 ({len(batch_blocks)}个块)")
                    break
                elif resp.status_code == 429:
                    wait_time = 120
                    print(f"  遇到限流，等待 {wait_time} 秒...")
                    time.sleep(wait_time)
                else:
                    print(f"  写入失败 (状态码: {resp.status_code}): {resp.text[:200]}")
                    if attempt < max_retries - 1:
                        time.sleep(10)
            except Exception as e:
                print(f"  写入异常: {e}")
                if attempt < max_retries - 1:
                    time.sleep(10)
        else:
            print(f"  第 {batch_idx + 1} 批写入失败")
    
    print(f"文档写入完成，共 {len(blocks)} 个内容块")


def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["tenant_access_token"]


def main():
    print("开始推送飞书文档...")
    token = get_tenant_access_token()
    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)
    with open("feishu_doc_url.txt", "w") as f:
        f.write(f"https://wcn5jx0ifkx3.feishu.cn/docx/{doc_id}\n")
    print(f"文档地址已保存: feishu_doc_url.txt")


if __name__ == "__main__":
    main()
