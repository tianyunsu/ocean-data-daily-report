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
SECTIONS = [   {   'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [   {   'abstract': '中国科学院海洋研究所李晓峰团队研发的"琅琊"海洋大模型1.0版已在国家海洋环境预报中心部署测试运行，实现台风、降水、海冰等海洋现象预报的实景应用。在2025年北极海冰季节预测国际网络竞赛中，中科院海洋所相关模型排名全球第一，超越多所国际机构。2.0版本预计2026年6月正式发布，新增海洋极端气象AI预报能力，目标实现"算得快又算得准"。',
                         'badge': '近7天',
                         'date': '2026-05-19',
                         'source': '中国科学院 / 光明日报',
                         'title': '中科院"琅琊"海洋大模型：AI解码海洋奥秘，北极海冰预测全球第一（光明日报, 2026-05-19）',
                         'url': 'https://www.cas.cn/cm/202605/t20260519_5109954.shtml'},
                     {   'abstract': '中国信息通信研究院联合中国人工智能产业发展联盟正式发布该报告，系统梳理"AI+海洋"全链条技术体系。报告指出海洋AI已形成"感知-传输-认知-决策"完整产业链，海洋大模型从通用走向垂直细分，形成渔业、船舶、公共管理等专属模型生态。建议沿海城市构建"算力+数据+算法+场景"闭环体系，形成全栈国产化技术链条。',
                         'badge': '近7天',
                         'date': '2026-05-18',
                         'source': '中国信通院',
                         'title': '中国信通院发布《人工智能赋能海洋产业研究报告（2026年）》（2026-05-18）',
                         'url': 'https://www.smartcity.team/reports/ai_ocean/'},
                     {   'abstract': '河海大学等团队提出基于SwinIR的海面风场降尺度框架，利用移位窗口自注意力机制捕获长程空间依赖。两阶段训练策略（第一阶段MSE优化通用映射，第二阶段加权损失提升极端风速重建性能）使超过25 m/s时RMSE降低4.25%，MAE达0.11 '
                                     'm/s。以2019年热带风暴"韦帕"为案例验证，研究为南海近海风能开发提供高精度数据支撑。',
                         'badge': '1周~1个月',
                         'date': '2026-04-16',
                         'source': 'Frontiers in Marine Science',
                         'title': 'SwinIR+两阶段训练：南海海面风场深度学习降尺度新方法（Frontiers in Marine Science, 2026-04-16）',
                         'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1813336/full'},
                     {   'abstract': 'MDPI Remote Sensing发表研究，构建结合2003-2024年22年MODIS Aqua、CMEMS和C3S多传感器卫星数据的可解释机器学习框架，引入分区域SHAP分析。研究揭示东海叶绿素a浓度受盐度主导的长期生态状态转变规律，而非传统认识的温度驱动，为东海渔业管理和海洋生态预测提供新方向。',
                         'badge': '1周~1个月',
                         'date': '2026-04-30',
                         'source': 'MDPI Remote Sensing',
                         'title': '东海叶绿素a卫星预测揭示盐度主导生态状态转变：22年多传感器可解释AI分析（Remote Sensing, 2026-04-30）',
                         'url': 'https://www.mdpi.com/2072-4292/18/9/1392'}],
        'title': '一、海洋人工智能'},
    {   'en': 'Ocean Digital Twin',
        'items': [   {   'abstract': 'Destination Earth（DestinE）平台正式发布气候变化适应数字孪生（Climate DT）第二代模拟数据集，涵盖1990-2049年全球多年代际模拟和2017-2025年极端天气情节模拟（每情节5成员集合）。技术规格：大气与陆面5 km、海洋与海冰5-10 '
                                     'km、逐小时分辨率，使用ICON、IFS-FESOM、IFS-NEMO三套模型，在芬兰LUMI和西班牙MareNostrum5超算完成。数据已存储于DestinE Data Lake，并提供Jupyter Notebook使用示例。',
                         'badge': '近7天',
                         'date': '2026-05-18',
                         'source': 'Destination Earth / ECMWF',
                         'title': 'DestinE气候数字孪生新一代模拟数据集正式发布（Destination Earth, 2026-05-18）',
                         'url': 'https://destine.ecmwf.int/news/new-destine-climate-digital-twin-simulations-available/'},
                     {   'abstract': 'Maritime Technology Review报道曲阜师范大学在Frontiers in Marine Science发表的研究：海洋数字孪生（Digital Twin Ocean）正成为全球海洋治理的核心工具，功能类似"海洋版Google '
                                     'Earth"，可叠加洋流、生物、地缘热点等多维数据层，支持航运路线模拟、深海采矿影响预评估。目前已在港口和海上风电场开展测试，为海洋资源开发、合规监管和生态保护提供实时决策支撑。',
                         'badge': '近7天',
                         'date': '2026-05-21',
                         'source': 'Maritime Technology Review / Frontiers in Marine Science',
                         'title': '海洋数字孪生助力全球海洋治理：Maritime Technology Review深度解析（2026-05-21）',
                         'url': 'https://maritimetechnologyreview.com/2026/05/21/global-maritime-governance-gets-a-digital-twin-ocean-boost/'},
                     {   'abstract': '联合国海洋十年认可项目DITTO（Digital Twins of the '
                                     'Ocean）宣布，第三届国际数字孪生海洋峰会将于2026年11月11-13日在日本横滨举行，主办方为JAMSTEC、GEOMAR等机构。峰会聚焦共享框架、互操作性、假设情景推演能力及海洋保护、治理与蓝色经济实际应用，推动全球海洋数字孪生生态系统走向融合。',
                         'badge': '1周~1个月',
                         'date': '2026-05-12',
                         'source': 'JAMSTEC / DITTO',
                         'title': 'DITTO国际数字孪生海洋峰会2026将于横滨召开（2026年11月）',
                         'url': 'https://w3.jamstec.go.jp/j/pr-event/ditto_summit2026/index.html'}],
        'title': '二、海洋数字孪生'},
    {   'en': 'Ocean Visualization',
        'items': [   {   'abstract': 'Taylor & Francis旗下Big Earth '
                                     'Data发表研究，评估六边形离散全球网格系统（DGGS）作为地球科学全球尺度建模框架的潜力。相比传统经纬度网格，六边形DGGS具有各向同性和均匀采样优势，能有效减少高纬度区域的几何畸变。研究聚焦其在海洋模型输出可视化、数据插值和多源数据融合展示中的性能提升，为下一代海洋环境数据可视化平台提供方法论依据。',
                         'badge': '近7天',
                         'date': '2026-05-20',
                         'source': 'Big Earth Data / Taylor & Francis',
                         'title': '六边形离散全球网格系统增强地球科学模型可视化性能（Big Earth Data, 2026-05-20）',
                         'url': 'https://www.tandfonline.com/doi/full/10.1080/20964471.2026.2666953'},
                     {   'abstract': 'DestinE推出DEA（Destination Earth '
                                     'Analysis）内容创作平台，用户无需编写代码即可将DestinE数据与自有素材组合，创建交互式数据故事并对外分享。平台专为科学家和决策者设计，支持海洋气候数字孪生模拟结果的可视化呈现，覆盖极端天气情节、长期气候变化趋势等场景，降低高质量海洋数据可视化的门槛。',
                         'badge': '1周~1个月',
                         'date': '2026-04-01',
                         'source': 'Destination Earth / ESA',
                         'title': 'Destination Earth Analysis平台（DEA）：无代码海洋数据故事创作工具（2026-04-01）',
                         'url': 'https://dea.destine.eu/'}],
        'title': '三、海洋可视化'},
    {   'en': 'Ocean Data Quality / QA/QC',
        'items': [   {   'abstract': 'JAMSTEC团队（Kouketsu等）在Journal of '
                                     'Oceanography发表研究，提出融合机器学习的Argo剖面自动质控新流程，在前期path-signature方法基础上改进，生成高效中间质量数据集。模型以2016年数据训练，在2017-2021年期间表现稳健，对错误剖面识别能力接近Argo数据中心人工审核水平，为快速生成近实时质控数据集提供可靠路径。',
                         'badge': '1周~1个月',
                         'date': '2026-04-29',
                         'source': 'Journal of Oceanography / Springer Nature',
                         'title': 'JAMSTEC：基于路径签名（Path-Signature）机器学习的Argo浮标剖面改进自动质控方法（J. Oceanogr., 2026-04-29）',
                         'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1'},
                     {   'abstract': 'NOAA IOOS QARTOD（Quality Assurance of Real-Time Oceanographic '
                                     'Data）项目持续发布实时海洋数据质控手册，涵盖CTD、流速计、波浪传感器等各类仪器的QC标志定义与使用规范。2026年5月最新更新包含对操作人员的指导说明，已成为全球海洋观测系统QA/QC标准化的重要参考文件，并整合至IOOS平台数据流质量管理流程中。',
                         'badge': '近7天',
                         'date': '2026-05-22',
                         'source': 'NOAA IOOS / QARTOD',
                         'title': 'IOOS QARTOD：实时海洋数据质控标志手册持续更新（2026-05）',
                         'url': 'https://ioos.noaa.gov/project/qartod/'},
                     {   'abstract': '夏威夷大学Bushinsky等团队在ESSD发布BGC-Argo+预印本，对截至2025年1月全球2,429个BGC-Argo浮标的氧气、硝酸盐、pH数据开展系统性二次质控，结合自动化与人工异常值检测。产品包含逐剖面数据和网格化数据集，支持直接观测、数据映射和模型同化，已归档至bgc-argo-plus.info，正在ESSD公开评审中（截止2026年6月19日）。',
                         'badge': '近7天',
                         'date': '2026-05-12',
                         'source': 'Earth System Science Data (ESSD)',
                         'title': 'BGC-Argo+：全球生化Argo浮标数据二次质控与衍生参数数据集（ESSD预印本, 2026-05-12）',
                         'url': 'https://essd.copernicus.org/preprints/essd-2026-311/'}],
        'title': '四、海洋数据质量'},
    {   'en': 'Ocean Data Processing',
        'items': [   {   'abstract': '研究开发基于UNet的深度学习降尺度方法，将Pangu-Weather等AI气象预报模型的海洋表面矢量风分辨率从0.25°提升至更精细区域尺度，专注台湾海峡及周边海域。时空增强型TempE-UNet通过残差学习提升细尺度海洋风场结构重建能力，为高分辨率海洋-大气耦合数值建模提供数据预处理解决方案，已在Journal '
                                     'of Oceanology and Climatology发表。',
                         'badge': '近7天',
                         'date': '2026-05-01',
                         'source': 'Journal of Oceanology and Climatology / ScienceDirect',
                         'title': 'UNet深度学习降尺度：提升台湾海峡海洋表面矢量风分辨率（Journal of Oceanology and Climatology, 2026-05-01）',
                         'url': 'https://www.sciencedirect.com/science/article/pii/S0924796326000461'},
                     {   'abstract': 'Ocean '
                                     'Modelling发表覆盖2020-2025年的综述，系统梳理机器学习在海洋数据同化（ODA）领域的最新进展：包括基于神经网络的协方差估计、深度学习代替切线线性模型、ML辅助观测算子等关键技术。综述指出当前主要差距在于物理一致性保障、跨尺度泛化能力及训练数据代表性问题，为下一代混合ML-DA海洋同化系统的发展提供路线图。',
                         'badge': '1周~1个月',
                         'date': '2026-02-01',
                         'source': 'Ocean Modelling / ScienceDirect',
                         'title': '机器学习在海洋数据同化中的进展、差距与挑战综述（Ocean Modelling, 2026-02）',
                         'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028'}],
        'title': '五、海洋数据处理'},
    {   'en': 'Ocean Data Management and Sharing Services',
        'items': [   {   'abstract': 'IOC/UNESCO通过IODE平台持续开放两门虚拟实验室在线课程：《How to use a Virtual Laboratory on Coastal Ocean Currents》和《How to use a Virtual Laboratory on Carbon Plankton '
                                     'Dynamics》，均延续至2026年7月，向全球海洋数据从业者和研究人员免费提供海洋数据处理与分析能力培训，是IODE数据能力建设"联合国海洋十年"行动计划的组成部分。',
                         'badge': '近7天',
                         'date': '2026-05-22',
                         'source': 'IOC-UNESCO / IODE',
                         'title': 'IOC-UNESCO：IODE虚拟实验室培训课程持续开放至2026年7月（2026-05）',
                         'url': 'https://iode.org/'},
                     {   'abstract': 'HUB Ocean（非营利性开放海洋数据平台）持续更新来自全球可信来源的海洋、气候与生物多样性数据集，支持搜索、筛选和可视化。平台完全开放，覆盖海表温度、海洋生物记录和水深测绘等数据门类，并基于FAIR原则持续扩展数据目录，为研究人员、政策制定者和产业界提供统一数据入口。',
                         'badge': '近7天',
                         'date': '2026-05-22',
                         'source': 'HUB Ocean',
                         'title': 'HUB Ocean数据平台：持续整合全球海洋生物多样性、气候与测绘数据集（2026-05）',
                         'url': 'https://www.hubocean.earth/'},
                     {   'abstract': 'NOAA NCEI世界海洋数据库（World Ocean Database）更新2026年Q1季度增量数据，通过WOD Select在线工具可按区域、时间、参数等多条件检索获取。WOD是全球最大的开放获取海洋剖面数据集合，收录CTD、Argo、瓶样、海洋滑翔机等多类型观测，新增数据已完成NCEI标准格式规范化处理。',
                         'badge': '1周~1个月',
                         'date': '2026-04-09',
                         'source': 'NOAA NCEI',
                         'title': 'NOAA世界海洋数据库（WOD）季度更新：2026年Q1新增数据可检索（2026-04-09）',
                         'url': 'https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html'}],
        'title': '六、海洋数据管理与共享服务'},
    {   'en': 'Open Cruises / Ship Time Sharing',
        'items': [   {   'abstract': '"探索一号"科考船搭载"奋斗者"号载人潜水器于2026年5月10日返抵广州，圆满完成历时156天（2025年12月6日-2026年5月10日）的太平洋穿越科考暨首次中国-智利阿塔卡马海沟载人深潜联合航次。总航程逾4万公里，来自中、智、德、丹麦、加拿大、西班牙6国83名科考队员共完成63个潜次（其中50次深度超6000米），首次发现南半球最深化能生态系统，为"全球化能生命长廊"假说提供关键证据。',
                         'badge': '近7天',
                         'date': '2026-05-10',
                         'source': '中国科学院深海所 / CCTV',
                         'title': '"探索一号"搭载"奋斗者"号完成"全球深渊探索计划"太平洋穿越航次（2026-05-10）',
                         'url': 'https://www.wxbh.gov.cn/doc/2026/05/21/4778931.shtml'},
                     {   'abstract': 'NOAA海洋探索项目EX2603于2026年5月16日至6月5日在夏威夷附近海域对Okeanos '
                                     'Explorer号的ROV系统实施全面测试，涵盖机械、电气和软件组件，确保潜水器在2026年正式探索季开始前处于最佳工作状态。这是NOAA延续深海探索能力建设的常规年度举措，将为后续太平洋、加勒比海及密歇根湖科考项目提供技术保障。',
                         'badge': '近7天',
                         'date': '2026-05-16',
                         'source': 'NOAA Ocean Exploration',
                         'title': 'NOAA Okeanos Explorer ROV系统整备测试（EX2603）在夏威夷近海开展（2026-05-16）',
                         'url': 'https://oceanexplorer.noaa.gov/expeditions/'},
                     {   'abstract': 'Schmidt Ocean Institute研究船R/V Falkor(too)于2026年5月17日至6月20日开展亚马逊峡谷深海浊流（水下雪崩）研究航次，由MBARI的Aaron Micallef和摩德纳大学Vittorio '
                                     'Maselli联合领队。将验证亚马逊河口322公里处是否存在现代活跃浊流，评估浊流对底栖生态系统的影响，研究有机碳和微塑料的深海埋藏通量。',
                         'badge': '近7天',
                         'date': '2026-05-17',
                         'source': 'Schmidt Ocean Institute',
                         'title': 'Schmidt海洋研究所R/V Falkor(too)：亚马逊峡谷水下雪崩科考启航（2026-05-17）',
                         'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/'},
                     {   'abstract': '西澳大利亚博物馆搭乘Schmidt Ocean Institute R/V Falkor，在Ningaloo海岸Cape Range和Cloates海底峡谷（最深4510米）采集逾千份水样开展eDNA分析，在6份独立样本中检出巨型鱿鱼（Architeuthis '
                                     'dux）——这是西澳大利亚首次通过eDNA记录该物种，也是其在东印度洋最北端的记录。共鉴定226种生物，发现数十种可能的新物种，研究发表于Environmental DNA期刊。',
                         'badge': '近7天',
                         'date': '2026-05-11',
                         'source': 'Western Australian Museum / Environmental DNA / SciTechDaily',
                         'title': 'eDNA技术在西澳大利亚深海峡谷中首次检测到巨型鱿鱼（Environmental DNA, 2026-05-11）',
                         'url': 'https://scitechdaily.com/giant-squid-detected-off-western-australia-in-stunning-deep-sea-discovery/'}],
        'title': '七、开放航次 / 船时共享'},
    {   'en': 'Ocean Data Centers / Data Archives',
        'items': [   {   'abstract': 'Copernicus Marine Service（CMEMS）发布2026年5月产品质量月报，对全球、区域海洋物理分析和预报产品的科学性能指标进行系统性评估，涵盖SST偏差、盐度误差和海流速度精度等关键参数。报告支持用户判断数据可靠性，是CMEMS服务等级协议（SLA）履行的核心组成部分，相关数据可通过Access '
                                     'Data页面直接获取。',
                         'badge': '近7天',
                         'date': '2026-05-24',
                         'source': 'Copernicus Marine Service (CMEMS)',
                         'title': 'CMEMS 5月产品质量月报发布：全球海洋物理分析预报产品性能更新（2026-05-24）',
                         'url': 'https://marine.copernicus.eu/access-data/'},
                     {   'abstract': 'NASA物理海洋学数据中心（PO.DAAC）更新ECCO V4r4（Estimating the Circulation and Climate of the Ocean）数据集的访问教程，提供完整的Jupyter Notebook演示从Earthdata '
                                     'Search检索到本地下载的全流程操作方法，涵盖79个ECCO数据集合。PO.DAAC是全球海洋卫星数据主要归档机构，管理包括SWOT、Jason系列、Aquarius等卫星数据。',
                         'badge': '近7天',
                         'date': '2026-05-12',
                         'source': 'NASA PO.DAAC / Earthdata',
                         'title': 'NASA PO.DAAC：ECCO V4r4数据集教程笔记本更新（2026-05-12）',
                         'url': 'https://podaac.github.io/tutorials/external/ECCO_download_data.html'},
                     {   'abstract': 'PANGAEA（地球与环境科学数据发布系统）2026年4月底完成最新批次数据集入库并更新工作坊预告，该平台作为Earth & Environmental '
                                     'Science数据的核心档案馆持续接收全球科考数据。PANGAEA采用开放获取原则，每条数据均分配DOI，支持数据发现与长期存档，为SEANOE、SeaDataNet等海洋数据基础设施提供底层数据服务。',
                         'badge': '1周~1个月',
                         'date': '2026-04-28',
                         'source': 'PANGAEA',
                         'title': 'PANGAEA数据发布平台：2026年5月最新数据集陆续入库（2026-04-28）',
                         'url': 'https://pangaea.de/'}],
        'title': '八、海洋数据中心'},
    {   'en': 'Tools and Code Resources',
        'items': [   {   'abstract': 'Copernicus Marine Service官方Python工具包copernicusmarine发布v2.4.1版本（2026年5月11日），较上一版本v2.4.0（2026年4月20日）进行bug修复和性能优化。该工具包提供命令行界面和Python '
                                     'API，支持从CMEMS平台下载海洋数据、无配额限制高性能访问，以及与xarray/pandas的无缝集成，要求Python >= 3.10。',
                         'badge': '近7天',
                         'date': '2026-05-11',
                         'source': 'PyPI / Copernicus Marine Service',
                         'title': 'Copernicus Marine Toolbox v2.4.1 发布（PyPI, 2026-05-11）',
                         'url': 'https://pypi.org/project/copernicusmarine/'},
                     {   'abstract': 'Parcels（Probably A Really Computationally Efficient Lagrangian '
                                     'Simulator）是高度可定制的拉格朗日粒子追踪Python库，可利用格点化海洋模型输出（如NEMO、SCHISM、ROMS）创建粒子运动仿真模拟。2026年5月最新更新持续维护，支持海洋微塑料、鱼卵、石油扩散等多类海洋传输问题的定量分析，在Github上活跃维护。',
                         'badge': '近7天',
                         'date': '2026-05-21',
                         'source': 'Parcels / GitHub',
                         'title': 'Parcels粒子追踪库：4天前最新更新（GitHub / parcels-code.org, 2026-05）',
                         'url': 'https://parcels-code.org/'},
                     {   'abstract': 'Ocean Data '
                                     'View（ODV）是AWI开发的免费海洋数据可视化和分析软件，SeaDataNet官方推荐工具，支持Argo、CCHDO、CORA、GTSPP、MEOP、世界海洋数据库等多个主要数据集的剖面、时间序列、轨迹可视化。最新版本支持地理参考数据的交互式探索分析，并与SeaDataNet云服务集成，广泛应用于全球海洋学研究。',
                         'badge': '1周~1个月',
                         'date': '2026-05-20',
                         'source': 'AWI / SeaDataNet',
                         'title': 'ODV（Ocean Data View）：海洋多维数据交互分析可视化软件持续更新（AWI/SeaDataNet）',
                         'url': 'https://odv.awi.de/'}],
        'title': '九、工具与代码资源'}]

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
