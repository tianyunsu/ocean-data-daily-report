#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 feishu_write_doc.py 的 SECTIONS 数据
"""
from datetime import datetime

today_date = datetime.now().strftime('%Y-%m-%d')
print(f"今日日期: {today_date}")

# ============================
# 步骤0: 日期预检 - 今日基准
# ============================
today = datetime.now()
cutoff_1month = today.replace(day=1)  # 近似1个月前
from datetime import timedelta
one_month_ago = today - timedelta(days=30)
one_week_ago = today - timedelta(days=7)
print(f"超1个月截止: {one_month_ago.strftime('%Y-%m-%d')}")
print(f"超1周截止: {one_week_ago.strftime('%Y-%m-%d')}")

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. Science Bulletin:海洋所发布海洋现象智能预报OP-LOM大模型框架',
                'badge': '[论文]',
                'abstract': (
                    '中国科学院海洋研究所李晓峰、王凡团队在《Science Bulletin》（2026-04-10）发表论文，首次系统区分OSV预报（温盐流等状态变量）与OP预报（台风、涡旋、ENSO等现象）的概念框架，提出面向三类时间尺度的海洋现象大模型架构OP-LOM，整合多源多模态图像处理、通用特征提取和现象预测生成三大模块，推动海洋预报从"环境场"向"事件演化预警"跨越。DOI: 10.1016/j.scib.2026.04.002'
                ),
                'source': 'Science Bulletin / 中国科学院海洋研究所',
                'date': '2026-04-10',
                'url': 'https://siottp.shou.edu.cn/2026/0410/c16574a351801/page.htm'
            },
            {
                'title': '2. OceanPredict AI-TT工作坊本周末在蒙特利尔开幕',
                'badge': '[会议]',
                'abstract': (
                    'OceanPredict人工智能任务小组（AI-TT）首届工作坊于2026年4月13–14日在加拿大蒙特利尔举行，主题为"机器学习海洋预报：方法、应用与挑战"。来自NOAA、ECMWF、日本气象厅、CMCC、赫尔辛基大学等机构的30篇研究涵盖ML替代物理模型、混合物理-ML预报、深度学习数据同化、沿海风暴潮预报等方向。'
                ),
                'source': 'OceanPredict',
                'date': '2026-04-13',
                'url': 'https://oceanpredict.org/events/ai-tt-workshop/'
            },
            {
                'title': '3. JAMES:深度学习预测耦合GCM系统性海洋误差',
                'badge': '[论文]',
                'abstract': (
                    'NYU Zanna研究团队（Verma et al.）在JAMES（2026-04-10在线）发表研究，利用深度学习从数据同化增量中学习耦合环流模式系统性海洋误差。在表层20米处可解释每日温度增量方差40–50%（基准仅20%），能精细捕捉西边界流、赤道潜流、南大洋等关键区域误差空间模式。'
                ),
                'source': 'JAMES / NYU Zanna Research Team',
                'date': '2026-04-10',
                'url': 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025MS005155'
            },
            {
                'title': '4. Communications Earth & Environ.:BGC-Argo浮标揭示深海氮碳循环动态',
                'badge': '[论文]',
                'abstract': (
                    'Bif et al. 在Communications Earth & Environment（2026-04-06）发表，利用东热带太平洋BGC-Argo浮标（含氧、硝酸盐、pH等传感器）近三年高频自主观测，首次解析ODZ中反硝化/anammox/亚硝酸盐氧化等氮转化途径时空动态，揭示缺氧区生物地球化学的非稳态动态本质，为海洋氮损失监测和高精度BGC传感器QC实践提供重要支撑。'
                ),
                'source': 'Communications Earth & Environment',
                'date': '2026-04-06',
                'url': 'https://www.nature.com/articles/s43247-026-03410-5'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / DTO',
        'items': [
            {
                'title': '1. Mercator Ocean官网本周更新：支持PIRATA预测计划启航',
                'badge': '[项目动态]',
                'abstract': (
                    'Mercator Ocean International本周（2026-04-08）在官网宣布支持PIRATA（Prediction and Research Moored Array in the Atlantic）大西洋预测锚系阵列计划正式启航，进一步强化其全球海洋实时预报体系。同时，Digital Twin Ocean平台本周维持稳定运营，整合全球数千个海洋传感器和卫星连续观测数据，为海洋治理、栖息地恢复和灾害风险管理提供近实时决策支撑。'
                ),
                'source': 'Mercator Ocean International',
                'date': '2026-04-08',
                'url': 'https://www.mercator-ocean.eu/en/'
            },
            {
                'title': '2. DITTO计划持续推进全球数字孪生海洋最佳实践框架建设',
                'badge': '[进展]',
                'abstract': (
                    'GEOMAR主导的联合国海洋十年DITTO计划持续推进，聚焦建立DTO公共理解框架和全球最佳实践标准，支持海洋保护与可持续蓝色经济。计划整合欧洲与国际机构数字孪生资产，与EU DTO、DestinE等项目形成互补生态，推动全球DTO互操作性标准体系建设。'
                ),
                'source': 'DITTO / 联合国海洋十年',
                'date': '2026-04',
                'url': 'https://ditto-oceandecade.org/'
            },
            {
                'title': '3. 数字海洋周2026将于6月8日世界海洋日开幕',
                'badge': '[活动预告]',
                'abstract': (
                    'Mercator Ocean International联合多方机构宣布，数字海洋周2026（Digital Ocean Week 2026）将于6月8日世界海洋日正式开幕，旨在汇聚全球海洋数字孪生研究者、数据科学家和政策制定者，分享最新技术进展和海洋可持续发展应用案例。'
                ),
                'source': 'Mercator Ocean International',
                'date': '2026-04',
                'url': 'https://www.mercator-ocean.eu/en/'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Dashboard',
        'items': [
            {
                'title': '1. CMEMS产品路线图重大更新：5Hz海浪、Sentinel-1C风场、VIIRS海色产品',
                'badge': '[产品更新]',
                'abstract': (
                    'CMEMS 2026年3月发布产品路线图重大更新：①海浪产品新增5Hz超高分辨率（~1km）显著波高数据集；②风场产品引入Sentinel-1C卫星L3数据；③全球海洋预报产品引入表面波强迫，提升近表层模拟精度；④生物地球化学海色产品从MODIS过渡至VIIRS-NOAA21传感器。双轨并行期至2026年5月5日。'
                ),
                'source': 'Copernicus Marine Service (CMEMS)',
                'date': '2026-03-25',
                'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information'
            },
            {
                'title': '2. ESSD预印本:OceanTACO——整合SWOT/SST/SSS/Argo的多传感器全球海面状态云优化数据集',
                'badge': '[新数据集]',
                'abstract': (
                    '慕尼黑工业大学Lehmann et al. 在ESSD发布OceanTACO预印本（DOI:10.5194/essd-2026-232，2026-04-10），构建整合卫星高度计、SWOT宽幅测高、SST、SSS、海面风、ERA5再分析和Argo原位观测的全球统一云优化数据集。代码已开源于GitHub（nilsleh/oceanTACO）。'
                ),
                'source': 'ESSD / 慕尼黑工业大学',
                'date': '2026-04-10',
                'url': 'https://essd.copernicus.org/preprints/essd-2026-232/'
            },
            {
                'title': '3. arXiv:OceanBench v2——海洋预报ML基准平台新增多变量时序预测任务',
                'badge': '[基准工具]',
                'abstract': (
                    '研究团队在arXiv（2026-04-12，arXiv:2604.07301）发布OceanBench v2，系统评估海洋状态估计和预报的机器学习方法，新增多变量时空预测任务和物理一致性约束评估。平台整合SST、SLP、海流等多源数据，涵盖Pangu-Weather、ClimaX等主流模型对比，为海洋AI模型标准化评估提供基础设施。'
                ),
                'source': 'arXiv:2604.07301',
                'date': '2026-04-12',
                'url': 'https://arxiv.org/abs/2604.07301'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. IODE联合海洋十年DCO-ODS推出海洋数据QA/QC系统培训课程',
                'badge': '[新课程]',
                'abstract': (
                    'UNESCO/IOC海洋数据信息交换（IODE）与海洋十年数据共享协调办公室（DCO-ODS）本周联合上线新版培训课程，系统涵盖数据质量保证（QA）与质量控制（QC）理论与实操，重点包括：实时数据QARTOD旗帜规范、多参数QC流程、数据发布前质量验证方法，面向全球海洋数据管理人员开放注册。'
                ),
                'source': 'IODE / UNESCO / DCO-ODS',
                'date': '2026-04-08',
                'url': 'https://iode.org/'
            },
            {
                'title': '2. IOOS QARTOD更新《实时海洋数据质量控制旗帜手册》',
                'badge': '[标准更新]',
                'abstract': (
                    '美国综合海洋观测系统（IOOS）QARTOD项目本周（2026-04-09）发布新版《实时海洋数据质量控制旗帜使用手册》，完善跨参数（物理、化学、生物）统一QC标志体系，为海洋传感器实时数据提供自动化质控标准化框架，适用于浮标、AUV、船载和岸站等多种观测平台。'
                ),
                'source': 'NOAA / IOOS QARTOD',
                'date': '2026-04-09',
                'url': 'https://ioos.noaa.gov/project/qartod/'
            },
            {
                'title': '3. Argo数据管理文档本周更新：BGC-Argo多参数QC手册体系完善',
                'badge': '[文档更新]',
                'abstract': (
                    'Argo数据管理官方网站本周（6天前）更新文档索引页面，系统列出BGC-Argo各参数质量控制手册，包括pH（DOI:10.13155/97828）、硝酸盐（DOI:10.13155/84370）、颗粒后向散射（DOI:10.13155/60262）等6类参数QC规范，标志着BGC-Argo传感器类型覆盖和质量控制流程持续完善。'
                ),
                'source': 'Argo Data Management / OneArgo',
                'date': '2026-04-08',
                'url': 'https://www.argodatamgt.org/Documentation'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Pipeline',
        'items': [
            {
                'title': '1. NOPP/IOOS发布FY2026海洋技术转化计划（OTT）——750万美元资助8方向',
                'badge': '[资助公告]',
                'abstract': (
                    '美国国家海洋伙伴关系计划（NOPP）与IOOS联合发布FY2026海洋技术转化计划（2026-04-06），总资助750万美元，最多6个项目。优先支持：云端平台与AI质控分析、低成本物理/化学/生物传感器、有害藻华与环境DNA传感器、新型数据管理与集成技术。意向书截止4月27日，完整申请截止7月15日。'
                ),
                'source': 'NOPP / NOAA IOOS',
                'date': '2026-04-06',
                'url': 'https://nopp.org/2026/new-funding-opportunity-for-ocean-technology-innovation/'
            },
            {
                'title': '2. 中科院海洋科学大数据中心持续更新——科学号船队全海域全要素观测',
                'badge': '[数据动态]',
                'abstract': (
                    '中科院海洋科学大数据中心本周（2026-04-01起）持续更新数据集汇交，依托"科学"号等旗舰科考船队，形成全海域全水深全要素空天海一体化观测体系，汇聚海洋环流、海洋生物、海洋化学等多学科数据资源，为海洋科学研究提供基础设施支撑。'
                ),
                'source': '中科院海洋研究所 / 海洋科学大数据中心',
                'date': '2026-04-01',
                'url': 'http://msdc.qdio.ac.cn/collection/'
            },
            {
                'title': '3. NSF OOI完成2026财年系统升级——900+台仪器实时数据稳定在线',
                'badge': '[进展]',
                'abstract': (
                    'NSF资助的海洋观测倡议（OOI）2026年4月初完成年度维护，Regional Cabled Array等多阵列超900台仪器实时数据流稳定在线，新增海底火山地震监测与浮游生物多样性实时追踪两项重要应用案例。'
                ),
                'source': 'Ocean Observatories Initiative / NSF',
                'date': '2026-04-02',
                'url': 'https://oceanobservatories.org/'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing / Sample Sharing',
        'items': [
            {
                'title': '1. IODE海洋十年数据协调办公室进入Adam Leadbetter博士新任领导阶段',
                'badge': '[组织动态]',
                'abstract': (
                    'Adam Leadbetter博士自2025年2月接任IODE海洋十年数据共享协调办公室（DCO-ODS）负责人以来，持续推进ODISCat全球海洋数据资源目录完善和海洋十年Challenge 8（公平开放数据获取）落地，重点加强小岛屿发展中国家和最不发达国家的数据获取能力建设。IODE官网本周（2天前）确认持续运营状态。'
                ),
                'source': 'IODE / UNESCO-IOC',
                'date': '2026-04-12',
                'url': 'https://iode.org/ocean-decade/'
            },
            {
                'title': '2. IOC/UNESCO推进国家管辖海域数据共享政策——填补EEZ数据治理缺口',
                'badge': '[政策]',
                'abstract': (
                    'IOC/UNESCO数据信息门户本周（2026-04-08）更新，推广国家管辖海域（EEZ以内）数据开放共享政策建议，敦促成员国支持本国涉海数据开放获取，弥补国际深海与沿海国数据获取鸿沟，为全球海洋科学数据治理框架提供制度性支撑。'
                ),
                'source': 'IOC / UNESCO',
                'date': '2026-04-08',
                'url': 'https://www.ioc.unesco.org/en/data-information'
            },
            {
                'title': '3. UNESCO/IOC-RTRC-ODC第15期海洋动力学与模式培训班开放申请',
                'badge': '[开放申请]',
                'abstract': (
                    'UNESCO/IOC区域培训研究中心（ODC中心）本周（6天前）宣布，第15期海洋动力学与海洋模式培训班将于2026年9月1–11日在青岛举办，面向全球海洋科研人员和学生开放申请，涵盖物理海洋学数据处理、数值模式原理与实践等内容。'
                ),
                'source': 'UNESCO/IOC-RTRC-ODC / 中国自然资源部',
                'date': '2026-04-08',
                'url': 'https://fiocom.fio.org.cn/a/news/ANNOUNCEMENT/2026/0403/492.html'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. Schmidt Ocean Institute发布2026年完整航次计划——涵盖9次深海探索',
                'badge': '[开放航次]',
                'abstract': (
                    'Schmidt Ocean Institute本周（2026-04-06）发布2026年完整航次计划，R/V Falkor(too)将执行9次深海探索任务，重点探索南大西洋等地球上被探索最少的海洋区域。最新航次"设计未来3"（4月15–30日）将利用DeepPIV、EyeRIS成像系统和RAD采样器2等前沿原型技术，探索海洋中层生物多样性，创建透明生物4D计算机渲染图。'
                ),
                'source': 'Schmidt Ocean Institute',
                'date': '2026-04-06',
                'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/'
            },
            {
                'title': '2. E/V Nautilus 2026太平洋探险持续推进——新增海底测绘面积44000平方海里',
                'badge': '[开放探索]',
                'abstract': (
                    'Ocean Exploration Trust宣布E/V Nautilus 2026年太平洋探险持续推进，重点区域覆盖夏威夷群岛、约翰斯顿环礁、霍兰德贝克岛等美属太平洋海域。OET在2025年为全球海底测绘工作新增约44,000平方海里数据，美国未测绘海域比例降至44%，成果通过Nautilus Live向公众开放。'
                ),
                'source': 'Ocean Exploration Trust / NOAA',
                'date': '2026-04-06',
                'url': 'https://nautiluslive.org/'
            },
            {
                'title': '3. IAPS OECS发布R/V Thomas G. Thompson研究船航次参与机会',
                'badge': '[航次机会]',
                'abstract': (
                    '国际海洋物理科学协会（IAPS OECS）本周发布R/V Thomas G. Thompson科考船I09N航次参与邀请，正在招募科学家参与，航次将赴西北太平洋重点海域开展物理海洋学联合调查，为研究人员提供共享科考船时的开放机会。'
                ),
                'source': 'IAPS OECS',
                'date': '2026-04-08',
                'url': 'https://www.iapsoecs.org/career/cruises/'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Archives / Repositories',
        'items': [
            {
                'title': '1. PANGAEA社区工作坊5月开放注册——在线培训助力用户高效检索地球环境数据',
                'badge': '[活动]',
                'abstract': (
                    'PANGAEA地球与环境科学数据平台（CoreTrustSeal认证）本周（2026-04-07）宣布5月7–8日举办"社区工作坊26/05：PANGAEA数据查找与获取"在线培训（每天10:30–12:30 CEST），涵盖高级搜索策略和跨学科数据集发现方法，面向地球科学、生物多样性和环境研究人员开放注册。'
                ),
                'source': 'PANGAEA / de.NBI',
                'date': '2026-04-07',
                'url': 'https://www.denbi.de/training-courses-2026/1962-pangaea-community-workshop-may-2026-finding-and-retrieving-data-from-pangaea'
            },
            {
                'title': '2. NOAA世界海洋数据库（WOD）完成季度更新——全球最大公开海洋剖面数据集持续扩充',
                'badge': '[数据更新]',
                'abstract': (
                    'NOAA NCEI世界海洋数据库（WOD）完成新一轮季度数据更新，持续扩充全球最大统一格式、质量控制海洋剖面数据集，涵盖温度、盐度、氧气、营养盐等多参数历史观测，支持通过WODselect系统在线检索，为气候研究、海洋模型验证和科学再分析提供核心数据资产。'
                ),
                'source': 'NOAA NCEI',
                'date': '2026-04',
                'url': 'https://www.ncei.noaa.gov/products/world-ocean-database'
            },
            {
                'title': '3. SeaDataNet联邦化数据基础设施持续运营——覆盖欧洲30+国家海洋观测数据汇聚',
                'badge': '[持续运营]',
                'abstract': (
                    'SeaDataNet作为欧洲海洋数据基础设施骨干，汇聚30多个国家的海洋学舰队和自动观测系统历史及近实时数据，通过CDI接口提供多格式标准化下载，与EMODnet深度整合。本周完成例行维护，保障用户稳定获取欧洲海洋观测数据。'
                ),
                'source': 'SeaDataNet / EuroGOOS',
                'date': '2026-04',
                'url': 'https://cdi.seadatanet.org/search'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources / GitHub',
        'items': [
            {
                'title': '1. GitHub:oceanTACO代码开源——支持SWOT/SST/SSS/Argo的云优化多传感器数据集生成',
                'badge': '[新开源]',
                'abstract': (
                    '配合OceanTACO数据集（ESSD预印本），慕尼黑工业大学在GitHub开源oceanTACO代码库（nilsleh/oceanTACO），实现从多源卫星和原位观测自动生成云优化格式数据集完整流程，包括SWOT宽幅测高、L3/L4 SST/SSS/风场及Argo剖面数据的统一化处理，配套ReadTheDocs文档和Jupyter示例。'
                ),
                'source': 'GitHub / 慕尼黑工业大学',
                'date': '2026-04-10',
                'url': 'https://github.com/nilsleh/oceanTACO'
            },
            {
                'title': '2. GO-BGC宣布2026年浮标数据与科学研讨会——8月在美国举行',
                'badge': '[会议通知]',
                'abstract': (
                    '全球海洋生物地球化学阵列（GO-BGC）本周（2026-04-07）宣布，将于2026年8月17–21日在美国举办浮标数据与科学研讨会，届时将汇聚BGC-Argo浮标数据用户、模式研发人员和海洋科学家，探讨浮标数据在生物地球化学研究和海洋碳循环分析中的应用。'
                ),
                'source': 'GO-BGC',
                'date': '2026-04-07',
                'url': 'https://www.go-bgc.org/'
            },
            {
                'title': '3. erddapy：Python访问ERDDAP数据服务器官方接口库——持续活跃维护',
                'badge': '[活跃项目]',
                'abstract': (
                    'IOOS官方维护的erddapy库提供Python原生方式访问全球任意ERDDAP服务器，支持数据集搜索、元数据获取、子集下载和图表生成，自动构建RESTful请求URL，是连接NOAA、CMEMS、Argo等主流ERDDAP数据服务与Python数据科学生态的关键桥梁工具。'
                ),
                'source': 'GitHub / IOOS',
                'date': '2026-04',
                'url': 'https://github.com/ioos/erddapy'
            },
            {
                'title': '4. xarray 2026.2.0发布——多维海洋数据处理核心库持续演进',
                'badge': '[版本更新]',
                'abstract': (
                    '海洋科学数据处理核心库xarray发布2026.2.0版本（2026-02-16），进一步优化大型NetCDF/Zarr数据集懒加载与并行计算性能，增强与Dask、cubed等分布式计算框架兼容性，是CMEMS、Argo、OOI数据处理流水线的基础工具之一。'
                ),
                'source': 'xarray / PyData社区',
                'date': '2026-02-16',
                'url': 'https://docs.xarray.dev/en/stable/'
            },
        ]
    },
]

# 日期预检
print("\n=== 步骤0: 日期预检 ===")
violations = []
for sec in SECTIONS:
    for item in sec['items']:
        try:
            item_date = datetime.strptime(item['date'], '%Y-%m-%d')
            if item_date < one_month_ago:
                violations.append(f"[{sec['title']}] {item['title']} ({item['date']}) - 超1个月!")
            elif item_date < one_week_ago:
                print(f"[注意] {sec['title']} | {item['title']} ({item['date']}) - 1周~1个月")
        except Exception as e:
            print(f"[日期解析错误] {item['title']}: {e}")

if violations:
    print(f"\n❌ 超期内容共 {len(violations)} 条:")
    for v in violations:
        print(f"  {v}")
else:
    print("\n✅ 所有内容日期合规!")

# 统计
total = sum(len(s['items']) for s in SECTIONS)
print(f"\n共 {len(SECTIONS)} 个方向，{total} 条内容")
