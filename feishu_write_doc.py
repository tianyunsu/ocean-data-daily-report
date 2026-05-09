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
    {'title': '1. arXiv（2026-05-06）：OceanPile——大规模多模态海洋语料库发布，填补海洋AI基础模型数据空白', 'badge': '近7天', 'abstract': '国际团队发布OceanPile大规模多模态海洋语料库，专为海洋AI基础模型设计，包含三大核心组件：OceanCorpus（整合声纳数据、水下图像、海洋科学可视化和科学文本的统一语料库）、OceanInstruction（基于层级海洋概念知识图谱合成的指令数据集）和OceanBenchmark（严格评估的手动策划基准测试）。研究解决了海洋数据高度碎片化、多模态、高噪声、弱标注等根本问题，使多模态大语言模型（MLLMs）能够应用于海洋科学。所有数据集已公开发布。arXiv:2605.00877', 'source': 'arXiv / cs.AI / cs.CL / cs.MM', 'url': 'https://arxiv.org/abs/2605.00877', 'date': '2026-05-06'},
    {'title': '2. Nature Geoscience（2026-04-13）：GOFLOW——利用静止卫星热红外影像实现前所未见的海洋表面流场观测', 'badge': '近7天', 'abstract': 'GOFLOW（Geostationary Ocean Flow）是一种深度学习框架，利用已在轨的静止气象卫星连续热红外影像序列，首次实现了大范围海洋表面流场的高分辨率观测。该方法无需新增硬件，利用GOES和Himawari等卫星的SST梯度数据训练神经网络推断海洋表面速度场，填补了传统漂流浮标和卫星高度计的空间覆盖空白，研究成果发表于Nature Geoscience。Science Daily对此进行了专题报道，代码和数据已开源。', 'source': 'Nature Geoscience / ScienceDaily', 'url': 'https://www.nature.com/articles/s41561-026-01943-0', 'date': '2026-04-13'},
  ]},
  {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
    {'title': '1. EGU 2026 / Copernicus Marine（2026-05-03-08）：EGU大会OS4.8专题——哥白尼海洋服务与欧洲海洋数字孪生最新成果', 'badge': '近7天', 'abstract': '在EGU 2026大会OS4.8专题会话中，Copernicus Marine Service联合EuroGOOS展示了海洋建模、数据同化、卫星与原位观测系统、不确定性估计及AI集成等方面的最新研究进展。会话汇聚EDITO Phase 2、全球海洋模型和AI融合预报等前沿成果，关注下一代海洋监测与预报系统的沿海与生态应用。大会于5月8日闭幕，海洋科学分部亮点包括DestinE数字孪生展示、Copernicus Marine AI增强产品等。', 'source': 'Copernicus Marine Service / EGU 2026', 'url': 'https://events.marine.copernicus.eu/egu-26', 'date': '2026-05-05'},
    {'title': '2. Destination Earth / ECMWF（2026-04-29）：DestinE气候数字孪生能力论文在GMD正式发表——5~10km分辨率多十年气候预测', 'badge': '近7天', 'abstract': '100余位科学家协作在《地球科学模型发展》（GMD）期刊发表论文，记录DestinE气候变化适应数字孪生的首次业务化实施成果，实现5~10km分辨率、多十年时间尺度的全球气候预测，支持能源、水资源等行业决策。使用ICON、IFS-FESOM、IFS-NEMO三大地球系统模型，集成AI/ML技术进行气候信息生产。该成果在EGU 2026期间进行了专题展示（ESSI1.8会话）。GMD论文DOI: 10.5194/gmd-19-2821-2026', 'source': 'Destination Earth / ECMWF / Geoscientific Model Development', 'url': 'https://gmd.copernicus.org/articles/19/2821/2026/gmd-19-2821-2026.pdf', 'date': '2026-04-29'},
    {'title': '3. JMAR（2026-05-01）：DSON-DT——深海观测网络数字孪生原型发布', 'badge': '近7天', 'abstract': '发表于Journal of Marine Science and Engineering的DSON-DT深海观测网络数字孪生框架，采用虚幻引擎5（UE5）进行高保真海洋环境3D渲染（60FPS、延迟<100ms），并设计改进型AR-LSTM模型用于电量状态（SoC）预测（R²=0.9981），通过MQTT+WebSocket+HTTP全栈架构实现实时遥测与远程控制，为深海观测网络的数字化管理提供了可复制的技术方案。DOI: 10.3390/jmse13050379', 'source': 'Journal of Marine Science and Engineering / MDPI', 'url': 'https://www.mdpi.com/2077-1312/13/5/379', 'date': '2026-05-01'},
  ]},
  {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [
    {'title': '1. NOAA（2026-05-06）：NOAA授予2,160万美元合同采购无人海洋系统——支持新一代测绘船Surveyor和Navigator', 'badge': '近7天', 'abstract': 'NOAA宣布向Chance Maritime Technologies公司授予2,160万美元合同，未来五年内采购最多8套无人海洋系统。系统具备直接操控、半自主（碰撞规避+动态航迹跟踪）和全自主三种运行模式，将装备于新一代测绘船Surveyor和Navigator，支持海底测绘和渔业声学调查。NOAA局长Neil Jacobs表示，无人系统将使美国保持在海洋科学创新前沿。', 'source': 'Seapower Magazine / NOAA', 'url': 'https://seapowermagazine.org/noaa-awards-21-6m-for-uncrewed-systems-to-support-new-charting-and-mapping-vessels/', 'date': '2026-05-06'},
    {'title': '2. Marine Technology News / NOAA（2026-05-07）：NOAA Thomas Jefferson号重返五大湖测绘——DriX无人艇加速海底制图', 'badge': '近7天', 'abstract': 'NOAA Thomas Jefferson号调查船时隔四年重返五大湖，将测绘伊利湖西部和中北部（自1940年代以来首次系统测绘）及安大略湖东部。今年夏天将部署DriX无人水面艇（搭载高分辨率多波束声呐，可在"监督自主"模式下连续作业4天以上）在纽约奥斯威戈附近加速测绘。该项目贡献于Lakebed 2030合作计划——目前五大湖仅17%完成测绘，是美国测绘最不充分的区域。', 'source': 'Marine Technology News / NOAA', 'url': 'https://www.marinetechnologynews.com/news/thomas-jefferson-returns-great-661991', 'date': '2026-05-07'},
    {'title': '3. EMODnet（2026-04-30）：EMODnet首次新增滨海旅游数据主题，拓展社会经济数据维度', 'badge': '近7天', 'abstract': '欧洲海洋观测与数据网络（EMODnet）自成立以来首次推出滨海旅游（Coastal Tourism）数据主题，标志着其从传统物理/生物海洋数据向社会经济数据领域拓展。滨海旅游是欧洲蓝色经济的重要支柱，新主题提供协调统一、高分辨率的沿海旅游活动数据，支持循证沿海管理决策。', 'source': 'EMODnet / European Commission', 'url': 'https://emodnet.ec.europa.eu/en/new-coastal-tourism-data-theme-expands-emodnets-support-sustainable-coastal-management', 'date': '2026-04-30'},
  ]},
  {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [
    {'title': '1. WMO（2026-04-24）：WMO全球季节性气候更新——厄尔尼诺很可能于2026年5-7月回归', 'badge': '近7天', 'abstract': '世界气象组织（WMO）发布最新全球季节性气候更新，赤道太平洋海表温度正在快速上升，气候模型"高度一致"预测厄尔尼诺条件很可能于2026年5-7月发展。WMO气候预测负责人表示"高置信度"。预期影响包括：几乎全球陆地气温偏高，南美南部和美国南部降雨增加，澳大利亚和印度尼西亚干旱风险上升，太平洋飓风增强而大西洋飓风受抑。下一次更新将于5月底发布。', 'source': 'World Meteorological Organization / WMO', 'url': 'https://wmo.int/media/news/wmo-likelihood-increases-of-el-nino', 'date': '2026-04-24'},
    {'title': '2. Nature Communications（2026-05-07）：热带气旋年最大强度存在次表层"信使"——可提前数年预测', 'badge': '近7天', 'abstract': '中国海洋大学倪欣宁、张宇、王伟团队在Nature Communications发表研究，揭示西北太平洋热带气旋年最大生命周期最大强度（LMI）与一个次表层水团的温度存在强烈关联，呈多年代际V型结构。该水团在北太平洋高压中心下形成并经约4年次表层路径输运至西边界，其高变异热含量调制风暴下方的海表温度。基于北太平洋高压强度可提前数年预测年最大LMI。DOI: 10.1038/s41467-026-72770-5', 'source': 'Nature Communications / Ocean University of China', 'url': 'https://www.nature.com/articles/s41467-026-72770-5', 'date': '2026-05-07'},
    {'title': '3. Journal of Oceanography（2026-04-29）：基于路径签名的Argo剖面自动质量控制方法改进', 'badge': '近7天', 'abstract': '日本JAMSTEC团队在Journal of Oceanography发表论文，改进了基于路径签名（path-signature）的Argo自动质量控制方法。新方法结合机器学习技术，使用2016年数据集训练的模型在2017至2021年间表现稳健，能够快速生成中等质量数据集，成功学习QC通用特征，准确率接近Argo数据中心水平。DOI: 10.1007/s10872-026-00791-1', 'source': 'Journal of Oceanography / JAMSTEC', 'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1', 'date': '2026-04-29'},
  ]},
  {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [
    {'title': '1. IOCCG（2026-05-05）：NASA PACE任务多仪器数据重新处理正式启动', 'badge': '近7天', 'abstract': 'NASA PACE（浮游生物、气溶胶、云和海洋生态系统）卫星任务正在进行大规模数据重新处理，包括OCI Version 3.0.2 Level-1B和Level-1C数据、OCI Version 3.2 Level-2/3水生地球物理产品，以及HARP2和SPEXone Version 4.0全级别产品。此外，第6届PACE应用研讨会录像已存档，5月14日将举行实践社区季度电话会议。', 'source': 'IOCCG / NASA PACE Mission', 'url': 'https://ioccg.org/2026/05/may-2026/', 'date': '2026-05-05'},
    {'title': '2. IOCCG / NASA（2026-03-17）：HyperInSPACE社区处理器HyperCP v1.2.15发布——引入全面不确定性预算系统', 'badge': '近7天', 'abstract': 'HyperCP发布v1.2.15重大更新，核心亮点是引入了按仪器类别和传感器分类的不确定性预算系统，包括辐射校准表征、噪声、环境扰动、波段卷积、耀斑校正模型误差等各项贡献的分解报告。新版本还新增耀斑校正和BRDF校正功能，以及SolarTracker、pySAS、DALEC等自主观测平台的支持，显著提升了海洋光学遥感数据处理的标准化水平。', 'source': 'IOCCG / HyperInSPACE / NASA', 'url': 'https://github.com/nasa/HyperCP/releases/tag/v1.2.15', 'date': '2026-03-17'},
    {'title': '3. arXiv（2026-05-06）：地中海海表温度热区识别——基于卷积协方差框架的统计建模方法', 'badge': '近7天', 'abstract': 'Leonardo Marchesin等在arXiv发表论文（2605.04921），提出一种基于卷积协方差框架的新方法用于地中海海表温度（SST）热区识别。通过将海洋域离散化为保留洋流方向的定向线性网络，构建基于马尔可夫转移概率矩阵的移动平均随机过程，为生态风险评估和环境监测提供统计严谨的方法论。stat.ME/stat.AP分类。arXiv:2605.04921', 'source': 'arXiv / stat.ME / stat.AP', 'url': 'https://arxiv.org/abs/2605.04921', 'date': '2026-05-06'},
  ]},
  {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [
    {'title': '1. NOAA Ocean Explorer / AOML（2026-05-05）：NOAA发布首套Okeanos Explorer号深海eDNA数据集——NCBI+OBIS+GBIF全覆盖共享', 'badge': '近7天', 'abstract': 'NOAA海洋探索办公室联合AOML、国家系统学实验室（史密森尼）和北部湾研究所，正式发布来自Okeanos Explorer号2021-2023年太平洋和大西洋探险的深海环境DNA数据集。原始序列可在NCBI BioProject（PRJNA1284389）获取，物种鉴定信息通过OBIS发布，数据集同时在GBIF正式注册（数据集ID: 9806a672-b859-4175-8432-f805b5ce8f30），实现NCBI、OBIS和GBIF三大国际数据库的全覆盖共享。NOAA将于5月28日中午EDT举办专题网络研讨会。', 'source': 'NOAA Ocean Explorer / NOAA AOML', 'url': 'https://oceanexplorer.noaa.gov/news/from-seawater-to-sequences-exploring-noaas-new-deep-sea-environmental-dna-dataset/', 'date': '2026-05-05'},
    {'title': '2. Seabed 2030（2026-04-20）：全球海底测绘达到新里程碑——28.7%海底已完成测绘', 'badge': '近7天', 'abstract': '日本财团-GEBCO Seabed 2030项目宣布全球海底已测绘面积已达28.7%，过去一年新增近500万平方公里数据（创年度纪录）。220个组织参与贡献，新增15个贡献者。区域亮点包括ROPME海域覆盖率从6.4%增长至20.5%。主要数据贡献来自NOAA-NCEI、PANGAEA、JAMSTEC、巴西海军水道测量局以及卫星测深数据。累计约1.04亿平方公里海底数据已整合至免费GEBCO网格。GEBCO_2026 Grid于4月27日正式发布可下载。', 'source': 'Seabed 2030 / The Nippon Foundation-GEBCO / GEBCO', 'url': 'https://seabed2030.org/2026/04/20/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year/', 'date': '2026-04-20'},
    {'title': '3. EMODnet Biology（2026-05-06）：EMODnet Biology数据下载新增物种缺失记录', 'badge': '近7天', 'abstract': 'EMODnet Biology改进了海洋生物多样性数据访问方式，允许用户在数据下载中包含分类单元的缺失记录（absence data）。这是生物多样性评估方法精细化的关键进展，缺失数据的引入能够显著降低物种分布模型的假阳性率，提升海洋生物多样性空间格局分析的准确性和可靠性，支持更科学的海洋保护区规划决策。', 'source': 'EMODnet Biology / VLIZ', 'url': 'https://emodnet.ec.europa.eu/en/inclusion-absence-data-emodnet-biology-downloads', 'date': '2026-05-06'},
  ]},
  {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
    {'title': '1. Schmidt Ocean Institute（2026-05-06）：亚马逊峡谷水下雪崩研究航次启航倒计时——5月17日出征', 'badge': '近7天', 'abstract': 'Schmidt Ocean Institute研究船Falkor(too)将于2026年5月17日启航，赴亚马逊峡谷开展为期35天的浊流（水下雪崩）研究，由MBARI与摩德纳大学联合团队主导，评估浊流频率、速度、地貌影响及有机碳/微塑料迁移，属联合国海洋十年认可项目。DriX无人水面艇和SuBastian ROV将参与作业，实现浊流过程的直接观测。', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/', 'date': '2026-05-06'},
    {'title': '2. OCEANS 2026 IEEE/MTS（2026-05-25-28）：三亚大会注册开放——深海技术、海洋能源与海洋AI', 'badge': '近7天', 'abstract': 'OCEANS 2026三亚大会将于5月25-28日在海南三亚海棠湾红树林度假酒店举行，由IEEE海洋工程学会和MTS联合主办。大会涵盖深海技术、海洋能源、自主水下航行器、海洋观测、海洋AI、水下声学等前沿领域，是国际海洋科技界的旗舰双年会议。注册和摘要提交已开放，来自全球的海洋科技专业者将汇聚交流最新成果。', 'source': 'OCEANS 2026 / IEEE OES / MTS', 'url': 'https://sanya26.oceansconference.org/', 'date': '2026-05-01'},
    {'title': '3. Astrobiology Magazine（2026-05-06）：Water World Genomics——eDNA技术如何解锁深海生物多样性秘密', 'badge': '近7天', 'abstract': 'Astrobiology Magazine报道NOAA Ocean Exploration的eDNA计划，介绍Okeanos Explorer号自2021年起将环境DNA纳入常规探测作业的决策历程。通过与史密森尼国家自然历史博物馆海洋DNA计划、NOAA渔业国家系统学实验室和AOML合作，NOAA已建立从样品采集到数据共享的完整eDNA工作流程，数据通过NCBI和OBIS向全球开放，为深海生物多样性研究和海洋保护区管理提供关键支撑。', 'source': 'Astrobiology Magazine / NOAA Ocean Exploration', 'url': 'https://astrobiology.com/2026/05/water-world-genomics-unlocking-ocean-secrets-with-edna.html', 'date': '2026-05-06'},
  ]},
  {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [
    {'title': '1. Copernicus Marine Service（2026-05-03）：第9版哥白尼海洋状况报告（OSR 9）正式发布', 'badge': '近7天', 'abstract': '第9版哥白尼海洋状况报告（OSR 9）揭示了破纪录的海洋极端事件、加速的变化趋势以及对海洋生态系统和社会日益增长的影响。报告重点关注2023和2024年极端事件，提供过去几十年海洋变化和变异的全面评估，并附有交互式摘要。OSR 9是全球海洋环境状况最权威的定期评估报告之一。报告可免费获取，并将于6月3-4日在布鲁塞尔举行发布会。', 'source': 'Copernicus Marine Service / Mercator Ocean International', 'url': 'https://marine.copernicus.eu/access-data/ocean-state-report/ocean-state-report-9', 'date': '2026-05-03'},
    {'title': '2. GEBCO / Seabed 2030（2026-04-27）：GEBCO_2026 Grid正式发布——15弧秒分辨率全球海底地形可下载', 'badge': '近7天', 'abstract': 'GEBCO于2026年4月27日正式发布2026版全球海底地形网格（GEBCO_2026 Grid），提供15弧秒分辨率全球海洋与陆地高程数据，支持netCDF、GeoTiff、ASCII格式下载及OPeNDAP在线访问，属公共领域免费数据，是全球海洋测绘的最新基准产品，可通过NOAA NCEI、EMODnet和GEBCO官网多渠道获取。', 'source': 'GEBCO / IHO / Nippon Foundation', 'url': 'https://www.gebco.net/news/release-gebco2026-grid', 'date': '2026-04-27'},
    {'title': '3. PANGAEA（2026-05-07/08）：EGU大会期间社区研讨会——数据发现与获取实操培训', 'badge': '近7天', 'abstract': 'PANGAEA地球与环境科学数据平台于5月7-8日在EGU 2026大会期间举行为期两天的社区研讨会（CEST 10:30-12:30），主题为"从PANGAEA发现和获取数据"。课程涵盖系统性数据发现策略、数据获取与Jupyter Notebooks集成工作流、编程工具与标准实践。PANGAEA作为全球最大的地球科学数据仓库之一，拥有数十万条已发布数据集。同时，PANGAEA Event-Campaign Merge数据库架构现代化升级持续推进中。', 'source': 'PANGAEA / AWI / MARUM', 'url': 'https://wiki.pangaea.de/wiki/PANGAEA_Community_Workshops', 'date': '2026-05-07'},
  ]},
  {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [
    {'title': '1. pydata/xarray（2026-04-13）：xarray v2026.04.0正式发布——支持zarr v3和全新绘图功能', 'badge': '近7天', 'abstract': 'xarray于2026年4月13日发布v2026.04.0版本，主要更新包括：最低zarr版本提升至3.0（与海洋大数据处理密切相关）、完成decode_timedelta弃用流程、新增col_wrap=\'auto\'绘图支持、DataTree.to_dataset新增inherit=\'all_coords\'选项、全局配置新增facetgrid_figsize选项等。22位贡献者参与该版本开发，包括多项dask数组编码修复和Dataset.interp对datetime变量的改进。xarray是Python海洋科学数据分析的核心工具库，广泛用于海洋模式输出处理和卫星数据操作。', 'source': 'xarray / PyPI / conda-forge / GitHub', 'url': 'https://github.com/pydata/xarray/releases/tag/v2026.04.0', 'date': '2026-04-13'},
    {'title': '2. Copernicus Marine Toolbox（2026-04-20）：copernicusmarine v2.4.0正式发布——支持Python 3.10-3.14', 'badge': '近7天', 'abstract': 'copernicusmarine Python工具箱v2.4.0于2026年4月20日正式发布（当前最新稳定版），主要更新：支持Python 3.10-3.14、新增稀疏数据集NetCDF子集提取、密集数据集CSV导出、优化登录凭证复用流程、兼容pandas>=3.0.0，修复了稀疏数据集下载和空文件生成问题。copernicusmarine是访问哥白尼海洋数据的官方Python客户端工具。', 'source': 'Mercator Ocean International / Copernicus Marine / PyPI', 'url': 'https://pypi.org/project/copernicusmarine/', 'date': '2026-04-20'},
    {'title': '3. NOAA Omics（2026-05-28）：NOAA Omics系列研讨会——从海水到序列：探索NOAA首套深海eDNA数据集', 'badge': '近7天', 'abstract': 'NOAA Omics研讨会系列联合NOAA图书馆将于5月28日中午EDT（北京时间5月28日24:00）举办专题研讨会"From Seawater to Sequences: Exploring NOAA\'s New Deep-Sea Environmental DNA Dataset"，介绍首套来自Okeanos Explorer号的深海eDNA数据集。研讨会将通过Vimeo平台直播，向全球研究者展示数据获取流程、分析方法和科学应用前景。同时，POGO-SCOR奖学金计划2026申请截止日期已延长至5月13日，面向发展中国家早期职业科学家。', 'source': 'NOAA Omics / NOAA Library / IOCCG', 'url': 'https://oceanexplorer.noaa.gov/news/from-data-to-discovery-unlocking-ocean-secrets-with-edna/', 'date': '2026-05-05'},
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
