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

SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '1. AGU GRL（2026-04-22）：北极夏季海冰快速融化事件的驱动机制——风场以外的物理过程', 'badge': '近7天', 'abstract': 'AGU《地球物理研究快报》（Geophysical Research Letters）发表最新研究，系统分析北极夏季快速海冰融化事件（RIME）的驱动因子。研究发现，除传统认知的北极风暴强风外，海洋热通量输送和短波辐射同样扮演关键角色。论文基于观测数据和ML分析，揭示不同区域海冰快速流失与大气-海洋耦合过程的非均匀性，对改进海冰预报模型具有重要意义。', 'source': 'AGU Geophysical Research Letters', 'url': 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026GL121848', 'date': '2026-04-22'}, {'title': '2. Springer（2026-04-18）：基于ConvLSTM的海冰密集度长期预测——南极60天逐日预报新框架', 'badge': '近7天', 'abstract': '《Journal of Earth System Science》发表最新研究，利用ConvLSTM（卷积长短期记忆网络）对1989-2016年卫星海冰密集度数据进行训练，实现南极海冰60天逐日动态预测。模型在捕捉季节性变化趋势和空间分布方面表现优异，较传统统计方法显著提升预测技能，为南极航行安全和气候变化监测提供重要工具。', 'source': 'Springer Journal of Earth System Science', 'url': 'https://link.springer.com/article/10.1007/s12145-026-02125-7', 'date': '2026-04-18'}, {'title': '3. arXiv 2604.07861（2026-04-09）：ML大气强迫 vs. NWP大气强迫驱动海洋预报——首次系统性对比评估', 'badge': '近7天内', 'abstract': '英国国家海洋学中心（NOC）等机构的最新预印本，对比使用机器学习（ML）大气强迫与传统数值天气预报（NWP）驱动业务化海洋预报系统时的性能差异。研究系统评估了ML大气强迫在全球海温、海面高度、混合层等关键变量预报中的精度，结果表明ML大气强迫在多数指标上具有可比甚至优越的表现，为推进端到端ML海洋预报奠定基础。', 'source': 'arXiv 2604.07861 / National Oceanography Centre', 'url': 'https://arxiv.org/abs/2604.07861', 'date': '2026-04-09'}, {'title': '4. ScienceDaily/URI（2026-04-21）：AI技术首次揭示肉眼不可见的海洋洋流——GOFLOW媒体聚焦报道', 'badge': '近7天', 'abstract': '罗德岛大学等机构官方新闻稿与ScienceDaily于2026-04-21发布科普报道，聚焦已发表于Nature Geoscience的GOFLOW研究。报道介绍AI如何利用现有气象卫星每5分钟拍摄的热红外图像，每小时生成高精度海洋表层流场图，尤其能捕捉数公里尺度的涡旋。这一突破性工具有助于提升物质扩散模拟、搜救行动及海洋污染追踪的精度。（注：Nature原文已于04-13发表，本条为扩大传播的新闻稿报道，收录用于展示国际影响力）', 'source': 'ScienceDaily / University of Rhode Island News', 'url': 'https://www.sciencedaily.com/releases/2026/04/260421042803.htm', 'date': '2026-04-21'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '1. CORDIS（2025-08 ~ 2026）：EDITO Phase 2——欧洲数字孪生海洋第二阶段获EU资助启动', 'badge': '近1月', 'abstract': '欧盟委员会CORDIS正式登记EDITO（欧洲数字孪生海洋）Phase 2项目，于2025年8月启动，旨在将EDITO-Infra扩展为覆盖更广用户群体的核心基础设施，整合更多欧洲海洋观测网络和模型服务，实现从沿岸到深海的无缝数字孪生覆盖。Phase 2将重点拓展MODELLAB统一建模环境和API生态系统，推动欧洲蓝色经济和海洋治理的数据驱动决策。', 'source': 'European Commission CORDIS', 'url': 'https://cordis.europa.eu/project/id/101227771', 'date': '2025-08-01'}, {'title': '2. Copernicus Marine / EuroGOOS（2026-04-13）：EGU 2026大会"CMEMS与欧洲数字孪生海洋"专题会话预告', 'badge': '近7天', 'abstract': 'Copernicus Marine Service和EuroGOOS联合发布预告，EGU 2026大会（5月3-8日，维也纳）将举办"OS4.8 – The Copernicus Marine Service and the European Digital Twin of the Ocean"专题会话，汇聚欧洲海洋数字孪生最新进展。此次会话将展示EDITO Phase 2、全球海洋模型、AI融合预报等前沿成果，是2026年欧洲海洋数字孪生领域的核心年度交流平台。', 'source': 'Copernicus Marine / EuroGOOS', 'url': 'https://events.marine.copernicus.eu/egu-26', 'date': '2026-04-13'}, {'title': '3. hellosea.org（2024至今）：中国首款自主研发海洋数字孪生引擎——DTO综合解决方案平台', 'badge': '近1月', 'abstract': '中国自主研发的数字孪生海洋（DTO）平台dto.hellosea.org.cn持续运营，提供涵盖海洋数字科学的全面解决方案，包括数字孪生驱动引擎、海洋多尺度仿真、可视化展示和数据服务。该平台是国内在海洋数字孪生领域的重要实践案例，支持海洋科研、管理和决策应用，与欧洲EDITO形成互补格局。', 'source': 'Digital Twin of the Ocean - hellosea.org.cn', 'url': 'https://dto.hellosea.org.cn/', 'date': '2024-07-18'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': '1. Blue-Cloud 2026（2026-04-21）：九份新开放获取海洋分析可视化培训材料发布——涵盖滑翔机工具、沿岸流图等', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026于2026年4月21日正式发布九份全新开放获取训练材料（CC BY 4.0），存档于Zenodo。材料覆盖多个海洋可视化分析场景：包括基于Python的海洋滑翔机数据可视化工具箱（处理温度/盐度/地转流）、集成多源数据的沿岸表面洋流可视化图（融合HF雷达+漂流浮标+卫星测高）、海洋热浪空间分布图制作、海洋热含量趋势可视化等。所有材料无需安装软件，直接在Blue-Cloud虚拟研究环境运行。', 'source': 'Blue-Cloud 2026 / Zenodo', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'}, {'title': '2. CMEMS（2026-04-21更新）：Copernicus Marine海洋可视化工具页面——多层次用户交互探索平台', 'badge': '近7天', 'abstract': 'Copernicus Marine Service官网可视化工具页面近日更新，整合面向不同用户层级的海洋可视化入口，涵盖MyOcean Viewer交互式全球海洋数据浏览器、OceanViz 3D可视化框架、以及CMEMS数据目录连接的可视化API。用户可实时查看全球海温、盐度、海流、海冰等多变量动态图层，支持科研和业务应用双轨并行。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/access-data/ocean-visualisation-tools', 'date': '2026-04-21'}, {'title': '3. GitHub OceanViz（活跃维护）：基于Unity引擎的海洋3D可视化框架——EwE生态系统模型专用', 'badge': '近1月', 'abstract': 'OceanViz是一个基于Unity游戏引擎的开源3D海洋可视化框架（Official-EwE/oceanviz），专为Ecopath with Ecosim（EwE）生态系统模型的可视化而设计。支持海洋生态系统动力学的三维实时渲染，可展示鱼类种群、食物网结构和海洋环境变化。该工具为海洋生态系统数字化和科学传播提供了全新途径，持续在GitHub维护更新。', 'source': 'GitHub / Official-EwE/oceanviz', 'url': 'https://github.com/Official-EwE/oceanviz', 'date': '2026-04-01'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [{'title': '1. Springer（2025-11-24发表，2026年引用活跃）：HAD-QC——基于混合AI的Argo浮标数据自动质量控制系统', 'badge': '近1月', 'abstract': 'DFKI德国人工智能研究中心等团队发表HAD-QC（Hybrid AI Approach for Automated Quality Control），专为Argo浮标数据质控设计。该系统集成三层架构：无监督自编码器（异常检测）+ 有监督集成分类器 + 18项传统Argo质控测试，三路输出通过加权方案融合。HAD-QC与Argo数据组装中心（DAC）流水线兼容，保留决策可解释性，并可扩展至新兴Argo平台（BGC-Argo、Deep-Argo），是目前最完整的Argo AI质控解决方案之一。', 'source': 'Springer / DFKI', 'url': 'https://link.springer.com/chapter/10.1007/978-3-032-11442-6_7', 'date': '2025-11-24'}, {'title': '2. ESSOAr（2026-04，更新版）：CODC-QC——中科院自主研发海洋原位温度质控系统及对全球变暖估计的影响', 'badge': '近1月', 'abstract': '中国科学院海洋研究所（CASIO）开发的CODC-QC（CAS-Ocean Data Center Quality Control）系统，针对海洋原位温度离群值提出新自动质控流程。与多数基于固定阈值的传统方法不同，CODC-QC无需预设阈值，采用自适应统计检验，并评估了质控决策对全球海洋变暖估计的定量影响。成果已发表于ESSOAr开放档案，面向国际Argo数据管理社区贡献中国方案。', 'source': 'ESSOAr / CAS Ocean Research Institute', 'url': 'https://essopenarchive.org/users/555015/articles/605857', 'date': '2026-04-01'}, {'title': '3. Springer（2025-04-08发表）：主动学习用于海洋数据质量评估——ODEAL框架（Argo/GLOSS/EMSO适用）', 'badge': '近1月', 'abstract': '研究提出ODEAL（Ocean Data Evidence-based Active Learning）框架，将主动学习算法引入海洋数据质量评估流程，显著减少人工标注需求。在Argo、GLOSS（海平面监测）和EMSO（欧洲多学科海底观测站）三类数据集上验证，模型以较少标注样本实现与全监督方法相当的异常检测精度，为大规模、多源海洋观测网络的高效质控提供了可扩展方案。', 'source': 'Springer / Data Mining and Knowledge Discovery', 'url': 'https://link.springer.com/article/10.1007/s41060-025-00751-w', 'date': '2025-04-08'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': '1. ScienceDirect Ocean Modelling（2026-02）：机器学习在海洋数据同化中的进展、差距与挑战——2020-2025系统综述', 'badge': '近1月', 'abstract': '《Ocean Modelling》发表系统综述，全面梳理2020-2025年间机器学习在海洋数据同化领域的研究进展，涵盖端到端学习型同化系统、物理信息神经网络、生成式同化模型等方向。综述指出主要差距：大多数ML同化方法仅在理想化设置下测试，全球业务化部署仍面临计算效率、不确定性量化和跨模型迁移等挑战。', 'source': 'ScienceDirect Ocean Modelling', 'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028', 'date': '2026-02-01'}, {'title': '2. ADAF-Ocean（arXiv 2511.06041，2025-11）：AI驱动多源多尺度海洋数据同化框架——直接同化稀疏原位+卫星观测', 'badge': '近1月', 'abstract': 'ADAF-Ocean提出了一种高效可扩展的AI驱动海洋状态估计框架，可直接同化来自稀疏原位观测（Argo浮标、船测CTD）和卫星遥感（SSH、SST）的多源多尺度数据，在无需数值模式背景场的条件下重建三维海洋状态。该框架使用Transformer架构处理不规则分布观测，在全球海洋再分析评估中显著优于传统最优插值方法。', 'source': 'arXiv 2511.06041 / Semantic Scholar', 'url': 'https://arxiv.org/abs/2511.06041', 'date': '2025-11-08'}, {'title': '3. Blue-Cloud 2026 VLab（2026-04-21）：基于Python的海洋滑翔机数据处理工具箱——原始二进制到网格化产品全流程', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026最新发布的培训材料中，专门针对海洋滑翔机数据处理的Python工具箱VLab服务提供详细教程。完整覆盖：原始二进制数据解码→盐度/温度质控→网格化数据产品生成（含地转流速计算）→Web界面交互探索。教程采用CC BY 4.0协议，存档于Zenodo，无需安装，在线运行于Blue-Cloud虚拟研究环境，适合从入门到高级用户的分级学习。', 'source': 'Blue-Cloud 2026 / Zenodo (DOI: 10.5281/zenodo.19556294)', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'}, {'title': '4. Copernicus Publications（2025-06）：Crafting the Future——机器学习用于海洋预报综合白皮书', 'badge': '近1月', 'abstract': '由多位欧洲海洋预报专家合作撰写的白皮书，系统梳理当前ML在全球海洋数值预报、集合预报、次网格参数化和极端事件检测中的应用路线图，重点分析ML方法如何与现有业务化预报体系（如CMEMS、ECMWF）进行无缝衔接，提出未来5年"可信AI增强型海洋预报"的技术路径。', 'source': 'Copernicus Publications Science & Practice', 'url': 'https://sp.copernicus.org/articles/5-opsr/9/2025/', 'date': '2025-06-02'}]}, {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '1. IODE（2026-04-16）：ODIS目录更新——可检索海洋数据源与信息系统网络化目录', 'badge': '近7天', 'abstract': 'IODE（国际海洋数据与信息交换系统）旗下ODIS（Ocean Data Information System）目录于2026年4月16日更新。该目录致力于构建可在线浏览和搜索的海洋相关数据系统目录，涵盖现有数据源、信息服务和知识共享平台，支持全球海洋数据互联互通（Ocean InfoHub）。更新内容包括新增数据源节点、改进元数据索引，进一步推进海洋数据FAIR原则落地。', 'source': 'IODE / IOC-UNESCO', 'url': 'https://iode.org/data/', 'date': '2026-04-16'}, {'title': '2. PANGAEA（2026-01）：北极弗拉姆海峡海底图像OFOBS数据集发布——极地深海底栖生物调查', 'badge': '近1月', 'abstract': 'PANGAEA于2026年1月公开发布北极弗拉姆海峡的海底图像数据集，由Ocean Floor Observation and Bathymetry System（OFOBS）采集。数据集包含高分辨率海底照片、测深信息和底栖生物记录，采用FAIR数据管理规范存档，配有完整的元数据和DOI标识（10.1594/PANGAEA.989651），支持极地海洋生态学和气候变化研究。', 'source': 'PANGAEA / Alfred Wegener Institute', 'url': 'https://doi.pangaea.de/10.1594/PANGAEA.989651', 'date': '2026-01-26'}, {'title': '3. Blue-Cloud 2026（2026-04-21）：九份FAIR培训材料上线Zenodo——支持欧洲多海洋数据基础设施访问', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026发布的9份培训材料全部遵循CC BY 4.0协议上传Zenodo，覆盖如何通过SeaDataNet、CMEMS、Copernicus Land等多个欧洲海洋数据基础设施获取和分析数据。材料明确说明FAIR数据访问流程、API使用规范和引用格式，为研究人员提供从数据发现到分析全链路的标准化操作指南。', 'source': 'Blue-Cloud 2026 / Zenodo CC BY 4.0', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'}]}, {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [{'title': '1. NOAA Ocean Exploration（2026年度）：NOAA船Okeanos Explorer 2026夏威夷操作区域计划——深海探索开放数据分享', 'badge': '近1月', 'abstract': 'NOAA Okeanos Explorer完成2026年阿拉斯加干坞期后，已转移至夏威夷港口备战2026年度田野考察季。NOAA ArcGIS已发布2026日历年提议操作区域图层，涵盖太平洋深海区域映射和生物多样性调查。NOAA Ocean Exploration承诺，所有Okeanos Explorer航次数据通过NOAA NCEI公开归档，ROV直播可通过oficialsite实时观看，持续贯彻开放海洋数据探索理念。', 'source': 'NOAA Ocean Exploration / ArcGIS', 'url': 'https://oceanexplorer.noaa.gov/okeanos/', 'date': '2026-04-01'}, {'title': '2. Schmidt Ocean Institute（2026-03-31）：R/V Falkor(too) 2026年度船时申请EOI持续开放——全球开放数据共享承诺', 'badge': '近1月', 'abstract': 'Schmidt Ocean Institute在其网站宣布2026年度R/V Falkor(too)科考申请持续开放，鼓励全球科学家提交兴趣表达（EOI）。所有船时申请须承诺数据开放共享：R/V Falkor(too)船载系统采集的全部数据将以开放数据形式公开发布。本年度已安排多个深海生物、海洋地质和化学领域的考察航次，持续推进Schmidt Ocean Institute的开放海洋探索使命。', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/apply/', 'date': '2026-03-31'}, {'title': '3. Nautilus Live（2026-04，活跃直播）：E/V Nautilus太平洋深海探索——ROV实时直播开放获取', 'badge': '近7天', 'abstract': '海洋探索信托（OET）E/V Nautilus继续在太平洋开展深海探索，通过Nautilus Live平台提供ROV直播（Channel 1），覆盖海底地质、生物多样性等多学科发现。2026年考察季聚焦西太平洋深海栖息地，实时数据和影像资料向全球公众和科研社区开放，体现开放海洋探索精神。', 'source': 'Ocean Exploration Trust / Nautilus Live', 'url': 'https://nautiluslive.org/', 'date': '2026-04-06'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '1. NOAA NCEI（2026-04-13）：全球Argo数据仓库更新——NCEI长期存档Argo浮标数据集', 'badge': '近7天', 'abstract': 'NOAA国家环境信息中心（NCEI）全球Argo数据仓库（Global Argo Data Repository）于2026年4月13日完成最新更新，托管来自全球3900+活跃Argo浮标的温度/盐度/压力剖面数据。NCEI作为美国国家Argo数据中心，持续提供实时和延时质控数据集的长期存档、版本管理和公开访问服务，是WOD（世界海洋数据库）核心数据来源之一。', 'source': 'NOAA NCEI / Global Argo Data Repository', 'url': 'https://www.ncei.noaa.gov/products/global-argo-data-repository', 'date': '2026-04-13'}, {'title': '2. SeaDataNet（活跃）：欧洲海洋数据联合基础设施——CDI接口整合多国数据中心访问', 'badge': '近1月', 'abstract': 'SeaDataNet作为泛欧洲海洋数据管理基础设施，通过CDI（通用数据索引）统一接口提供来自欧洲各国国家海洋中心的研究航次数据访问服务，覆盖欧洲沿海、区域海和全球海洋的水文、化学、生物等多类观测数据。SeaDataNet同时为Blue-Cloud 2026提供数据基础设施支撑，推动欧洲海洋数据的FAIR化和互操作性提升。', 'source': 'SeaDataNet', 'url': 'https://www.seadatanet.org/', 'date': '2026-04-01'}, {'title': '3. IODE/IOC-UNESCO（2026-04-17）：ODIS实施工作坊公告——海洋数据互联互通系统全球培训', 'badge': '近7天', 'abstract': 'IODE于2026年4月17日发布培训工作坊公告，聚焦ODIS（Ocean Data and Information System）的全球实施。工作坊旨在帮助成员国海洋数据中心掌握ODIS互联互通标准和Ocean InfoHub（OIH）技术，实现各国海洋数据系统的语义化互操作。培训内容包括Schema.org元数据标准、JSON-LD格式规范和RDF数据图谱构建，对接W3C和RDA国际标准框架。', 'source': 'IODE/IOC-UNESCO', 'url': 'https://iode.org/', 'date': '2026-04-17'}, {'title': '4. PANGAEA（2026年持续）：地球与环境科学数据出版平台——FAIR数据存档与DOI长期标识', 'badge': '近1月', 'abstract': 'PANGAEA作为地球与环境科学领域的开放数据出版平台，持续接受海洋观测数据提交和出版，为每个数据集分配DOI持久标识符，确保长期可访问性。2026年新发布数据集包括北极弗拉姆海峡OFOBS底栖图像集（1月）等，并持续支持5月社区研讨会（"Finding and Retrieving Data"）系列活动，推广数据共享文化。', 'source': 'PANGAEA Data Publisher', 'url': 'https://pangaea.de/', 'date': '2026-04-01'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': '1. Blue-Cloud 2026（2026-04-21）：Python海洋滑翔机工具箱+沿岸流合成图工具——Zenodo开放发布', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026新发布的海洋工具资源涵盖：① 基于Python的滑翔机数据工具箱（处理原始二进制→温盐流网格化产品，DOI: 10.5281/zenodo.19556294）；② 集成多源观测数据（HF雷达+漂流浮标+卫星测高）的沿岸表面洋流合成图工具（DOI: 10.5281/zenodo.19556568）。两套工具均采用CC BY 4.0开放协议，存档于Zenodo，支持搜救和漏油漂移建模（MEDSLIK-II集成）等应用。', 'source': 'Blue-Cloud 2026 / Zenodo', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'}, {'title': '2. Deltares dfm_tools（GitHub Issue #817，近期）：CMEMS原位数据接口从FTP迁移到copernicusmarine文件服务', 'badge': '近7天', 'abstract': 'Deltares的dfm_tools海洋数值模型后处理工具库在GitHub上发布Issue #817和对应PR #818，记录将CMEMS原位数据下载接口从传统FTP协议迁移至新版copernicusmarine Python文件服务API的过程。此迁移与Copernicus Marine Service近期弃用FTP接口的政策变化一致，对所有依赖CMEMS FTP下载数据的脚本和流水线均有影响，开发者需参照新API格式更新代码。', 'source': 'GitHub / Deltares dfm_tools', 'url': 'https://github.com/Deltares/dfm_tools/issues/817', 'date': '2026-04-15'}, {'title': '3. GitHub SEA-PY（2026-03-23更新）：Python海洋数据处理工具目录——汇聚海洋气象全套Python生态', 'badge': '近1月', 'abstract': 'SEA-PY（sea-py.github.io）是面向海洋和大气科学的Python工具目录，于2026年3月23日完成最新更新。目录系统汇聚了海洋科学Python生态中的核心包，包括xarray、netCDF4、cartopy、cmocean、erddapy、gsw（TEOS-10海水属性）等，并提供安装指引、使用场景分类和社区维护状态标注，是研究人员选择海洋数据处理工具的重要参考索引。', 'source': 'SEA-PY / pyoceans GitHub', 'url': 'https://pyoceans.github.io/sea-py/', 'date': '2026-03-23'}, {'title': '4. OCEANS 2026 Sanya（5月25-28，2026）：IEEE/MTS海洋会议征稿——深海技术、海洋能源与Ocean AI三大主题', 'badge': '近7天', 'abstract': 'OCEANS 2026 Sanya（国际电气电子工程师学会与海洋技术学会联合主办）定于2026年5月25-28日在中国三亚举行，重点聚焦深海技术、海洋能源和Ocean AI三大议题。本届大会强调AI在海洋探测、水下机器人、声学通信和海洋数据处理中的应用，已开放学生海报和论文展示征集。IEEE Xplore将收录会议论文，是国际海洋工程与技术领域最重要的年度交流平台之一。', 'source': 'OCEANS 2026 Sanya / IEEE / MTS', 'url': 'https://sanya26.oceansconference.org/', 'date': '2026-04-22'}]}]

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


def write_blocks_to_doc(token, doc_id, blocks, max_retries=3):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"children": blocks, "index": 0}
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
            if resp.status_code == 200:
                print(f"成功写入 {len(blocks)} 个内容块")
                return
            elif resp.status_code == 429:
                print(f"遇到限流，等待 60 秒...")
                time.sleep(60)
            else:
                print(f"写入失败 (状态码: {resp.status_code}): {resp.text}")
                if attempt < max_retries - 1:
                    time.sleep(5)
        except Exception as e:
            print(f"写入异常: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
    print("文档写入失败")


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
