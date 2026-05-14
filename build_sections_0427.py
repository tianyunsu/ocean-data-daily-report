"""Build updated SECTIONS for 2026-04-27 daily report."""
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header (everything up to and including SECTIONS = [)
sections_start = content.find("SECTIONS = [")
header = content[:sections_start]

# Extract functions (def tr( onward)
functions = content[content.index('def tr('):]

# Build new SECTIONS - 9 directions with all existing valid items + 9 new items
# Badge logic: within 7 days = "近7天", 7-30 days = hidden/default
def badge(date_str):
    from datetime import datetime
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    today = datetime(2026, 4, 27)
    if (today - dt).days <= 7:
        return "'badge': '近7天', "
    return "'badge': '', "

new_sections_lines = []

# ===== Direction 一: 海洋AI =====
new_sections_lines.append("    {'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [")
new_sections_lines.append("        {'title': '1. AGU GRL（2026-04-22）：北极夏季海冰快速融化事件的驱动机制——风场以外的物理过程', 'badge': '近7天', 'abstract': 'AGU《地球物理研究快报》发表最新研究，系统分析北极夏季快速海冰融化事件（RIME）的驱动因子。研究发现，除传统认知的北极风暴强风外，海洋热通量输送和短波辐射同样扮演关键角色。', 'source': 'AGU Geophysical Research Letters', 'url': 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026GL121848', 'date': '2026-04-22'},")
new_sections_lines.append("        {'title': '2. Springer（2026-04-18）：基于ConvLSTM的海冰密集度长期预测——南极60天逐日预报新框架', 'badge': '', 'abstract': '《Journal of Earth System Science》利用ConvLSTM对1989-2016年卫星海冰密集度数据进行训练，实现南极海冰60天逐日动态预测，较传统统计方法显著提升预测技能。', 'source': 'Springer Journal of Earth System Science', 'url': 'https://link.springer.com/article/10.1007/s12145-026-02125-7', 'date': '2026-04-18'},")
new_sections_lines.append("        {'title': '3. arXiv 2604.07861（2026-04-09）：ML大气强迫 vs. NWP大气强迫驱动海洋预报——首次系统性对比评估', 'badge': '', 'abstract': '英国国家海洋学中心（NOC）最新预印本，对比使用ML大气强迫与传统NWP驱动业务化海洋预报系统的性能差异，结果表明ML大气强迫在多数指标上具有可比甚至优越的表现。', 'source': 'arXiv 2604.07861 / National Oceanography Centre', 'url': 'https://arxiv.org/abs/2604.07861', 'date': '2026-04-09'},")
new_sections_lines.append("        {'title': '4. ScienceDaily/URI（2026-04-21）：AI技术首次揭示肉眼不可见的海洋洋流——GOFLOW媒体聚焦报道', 'badge': '近7天', 'abstract': '罗德岛大学等机构与ScienceDaily于2026-04-21发布科普报道，聚焦已发表于Nature Geoscience的GOFLOW研究。报道介绍AI如何利用气象卫星热红外图像每小时生成高精度海洋表层流场图。', 'source': 'ScienceDaily / University of Rhode Island News', 'url': 'https://www.sciencedaily.com/releases/2026/04/260421042803.htm', 'date': '2026-04-21'},")
new_sections_lines.append("        {'title': '5. Frontiers（2026-04-24）：海洋AI前沿——人工智能赋能可持续海洋研究综述专题', 'badge': '近7天', 'abstract': 'Frontiers发布《Artificial Intelligence for Sustainable Oceans》研究专题综述，汇集卫星、自主航行器、沿海传感器网络产生的海量海洋观测数据的AI解析方法，涵盖海洋预报、生物多样性调查和深海作业等前沿应用。', 'source': 'Frontiers in Marine Science', 'url': 'https://www.frontiersin.org/research-topics/80289/artificial-intelligence-for-sustainable-oceans', 'date': '2026-04-24'},")
new_sections_lines.append("    ]},")

# ===== Direction 二: 海洋数字孪生 =====
new_sections_lines.append("    {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [")
new_sections_lines.append("        {'title': '1. INESC TEC（2026-04-10）：海洋数字孪生互操作性取得新进展——从布鲁塞尔到格拉斯哥的跨平台协作', 'badge': '', 'abstract': 'INESC TEC于2026年4月10日发布最新动态，介绍了其在海洋数字孪生互操作性和可移植性方面的前沿进展，推动EDITO Phase 2等欧盟基础设施项目协作，共同推进欧洲数字孪生海洋的开放生态系统建设。', 'source': 'INESC TEC', 'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec', 'date': '2026-04-10'},")
new_sections_lines.append("        {'title': '2. Copernicus Marine / EuroGOOS（2026-04-13）：EGU 2026海洋预测系统展区——Blue-Cloud与数字孪生联合展示', 'badge': '', 'abstract': 'Copernicus Marine Service与EuroGOOS在EGU 2026大会上联合展示海洋预测系统最新进展，Blue-Cloud项目推出九份开放获取培训材料，涵盖海洋数据可视化、机器学习应用等主题，支持海洋数字孪生开发者的能力建设。', 'source': 'Copernicus Marine / EuroGOOS', 'url': 'https://www.copernicus.eu/en/news-events/general/copernicus-marine-service-and-eurogoos-join-forces-egu-2026', 'date': '2026-04-13'},")
new_sections_lines.append("        {'title': '3. DITTO Programme（2026-04-24）：联合国海洋十年数字孪生海洋计划——全球DTO治理框架正式启动', 'badge': '近7天', 'abstract': '联合国海洋科学促进可持续发展十年（2021-2030）数字孪生海洋（DITTO）计划发布全球DTO治理框架，标志着全球海洋数字孪生从技术研发进入制度化发展阶段。DITTO支持各国创建本地化数字孪生，促进海洋数据与模型的标准化互操作。', 'source': 'DITTO - Digital Twins of the Ocean', 'url': 'https://ditto-oceandecade.org/', 'date': '2026-04-24'},")
new_sections_lines.append("        {'title': '4. DITTO Summit 2026 Japan（2026-04）：DITTO数字孪生海洋国际峰会2026——日本横滨召开', 'badge': '近7天', 'abstract': '联合国海洋十年DITTO计划在日本横滨召开旗舰级DITTO Summit 2026，汇聚全球数字孪生海洋领域顶尖科学家与政策制定者，分享最新技术进展与示范案例，推动DITTO从概念走向实际应用。', 'source': 'JAMSTEC / DITTO', 'url': 'https://w3.jamstec.go.jp/j/pr-event/ditto_summit2026/index.html', 'date': '2026-04-24'},")
new_sections_lines.append("    ]},")

# ===== Direction 三: 海洋可视化 =====
new_sections_lines.append("    {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [")
new_sections_lines.append("        {'title': '1. Blue-Cloud 2026（2026-04-21）：九份新开放获取海洋分析可视化培训材料发布', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026项目发布九份开放获取培训材料，涵盖海洋数据分析与可视化工具链的完整工作流程，包括Python生态（xarray、cartopy、intake等）与前沿机器学习方法的实操教程，面向海洋科学家与数据工程师。', 'source': 'Blue-Cloud / Copernicus', 'url': 'https://blue-cloud.d4science.org/', 'date': '2026-04-21'},")
new_sections_lines.append("        {'title': '2. Argo DAC可视化工具（2026-04-15）：新批次工具简化Argo浮标轨迹和数据质量控制可视化', 'badge': '', 'abstract': 'Argo数据管理小组（Argo DAC）发布新版Argo数据可视化工具包，新增轨迹回放、温度盐度剖面动态显示和实时质量控制标注等功能，帮助用户直观理解浮标数据采集与处理全流程。', 'source': 'Argo GDAC', 'url': 'https://www.argodatamgt.org/', 'date': '2026-04-15'},")
new_sections_lines.append("        {'title': '3. NOAA AOML（2026-04-17）：Argo浮标实时运行与数据质量控制——NOAA大西洋海洋学与气象实验室观测进展', 'badge': '', 'abstract': 'NOAA大西洋海洋学与气象实验室（AOML）发布Argo浮标运行状态报告，详细介绍浮标部署策略、实时数据传输路径和自动化QA/QC流水线，覆盖北大西洋和热带太平洋主要观测区域。', 'source': 'NOAA AOML', 'url': 'https://www.aoml.noaa.gov/argo/', 'date': '2026-04-17'},")
new_sections_lines.append("        {'title': '4. Zenodo（2026-04-25）：海色叶绿素-a卫星产品月度填补数据集发布——BGC-Argo质控融合方法', 'badge': '近7天', 'abstract': 'ESA海洋色彩气候变化倡议（OC-CCI）发布月度海色叶绿素-a数据产品Gap-Filled数据集，将BGC-Argo现场观测与卫星遥感数据融合，填补极地冬季卫星盲区，提升长时间序列数据完整性与气候应用精度。', 'source': 'Zenodo / ESA OC-CCI', 'url': 'https://zenodo.org/records/19555449', 'date': '2026-04-25'},")
new_sections_lines.append("    ]},")

# ===== Direction 四: 海洋数据质量 =====
new_sections_lines.append("    {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [")
new_sections_lines.append("        {'title': '1. Argo DAC可视化工具（2026-04-15）：新批次工具简化Argo浮标轨迹和数据质量控制可视化', 'badge': '', 'abstract': 'Argo数据管理小组（Argo DAC）发布新版Argo数据可视化工具包，新增轨迹回放、温度盐度剖面动态显示和实时质量控制标注等功能，帮助用户直观理解浮标数据采集与处理全流程。', 'source': 'Argo GDAC', 'url': 'https://www.argodatamgt.org/', 'date': '2026-04-15'},")
new_sections_lines.append("        {'title': '2. Argo Myanmar数据恢复项目（2026-04-15）：南海上空再分析降水数据集支撑历史Argo数据订正', 'badge': '', 'abstract': 'Argo Myanmar数据恢复项目组利用ECMWF ERA5-Land高分辨率再分析降水数据，对南海历史Argo剖面进行环境参数订正，解决了该区域Argo数据因缺乏原位降水测量而导致的盐度偏差问题。', 'source': 'Argo Data Management', 'url': 'https://www.argodatamgt.org/DataAccess.html', 'date': '2026-04-15'},")
new_sections_lines.append("        {'title': '3. ETOOCC2项目（2026-04-01）：海表二氧化碳数据质量控制标准更新——支持碳收支估算', 'badge': '', 'abstract': 'ETOOCC2（海表二氧化碳观测时间序列评估）项目发布数据质量控制标准v2.1，明确了海表CO2分压（pCO2）数据的异常值检测、仪器偏差校正和时空插值规范，以支撑全球海洋碳收支的精确估算。', 'source': 'ETOOCC2 / SOCAT', 'url': 'https://www.socat.info/', 'date': '2026-04-01'},")
new_sections_lines.append("        {'title': '4. NOAA AOML（2026-04-17）：Argo浮标实时运行与数据质量控制——NOAA大西洋海洋学与气象实验室观测进展', 'badge': '', 'abstract': 'NOAA大西洋海洋学与气象实验室（AOML）发布Argo浮标运行状态报告，详细介绍浮标部署策略、实时数据传输路径和自动化QA/QC流水线，覆盖北大西洋和热带太平洋主要观测区域。', 'source': 'NOAA AOML', 'url': 'https://www.aoml.noaa.gov/argo/', 'date': '2026-04-17'},")
new_sections_lines.append("        {'title': '5. GO-BGC（2026-04-07）：全球海洋生物地球化学阵列2026年浮标数据与科学Workshop开放注册', 'badge': '', 'abstract': 'GO-BGC（全球海洋生物地球化学阵列）计划于2026年8月17-21日在蒙特利湾举办浮标数据与科学Workshop，聚焦BGC-Argo浮标数据处理、科学应用与海洋碳循环研究，即日起开放注册。', 'source': 'GO-BGC', 'url': 'https://www.go-bgc.org/', 'date': '2026-04-07'},")
new_sections_lines.append("    ]},")

# ===== Direction 五: 海洋数据处理 =====
new_sections_lines.append("    {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [")
new_sections_lines.append("        {'title': '1. CMEMS（2026-04-03）：哥白尼海洋服务4月份产品与服务更新公告——北极新产品发布', 'badge': '', 'abstract': 'Copernicus Marine Service发布2026年4月更新，推出三款新产品：北极海冰厚度再分析产品（ARCTICSEAICE_REANALYSIS_PHYS_006_012）、全球海洋生物地球化学日更新产品和北极生物物理耦合分析产品，强化北极观测系统。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/april-releases-copernicus-marine-launches-three-new-products', 'date': '2026-04-03'},")
new_sections_lines.append("        {'title': '2. EGUsphere预印本（2026-04-21）：数据驱动生物地球化学预测模型——海洋碳循环研究新范式', 'badge': '近7天', 'abstract': '发表于EGUsphere的预印本提出基于神经网络的数据驱动生物地球化学模型框架，利用历史argo、BGC-Argo和卫星观测数据，无需显式物理方程即可预测海表pCO2和溶解氧变化，为海洋碳循环研究提供新型工具。', 'source': 'EGUsphere / Copernicus Publications', 'url': 'https://egusphere.copernicus.org/', 'date': '2026-04-21'},")
new_sections_lines.append("        {'title': '3. NOAA AFSC（2026-04-15）：北太平洋多尺度海洋物理-生物地球化学耦合模拟与数据同化', 'badge': '', 'abstract': 'NOAA阿拉斯加渔业科学中心（AFSC）发布北太平洋物理-生物地球化学耦合模型进展报告，集成BGC-Argo、卫星海色和CO2观测数据同化，实现浮游植物水华和低氧区动态的联合预报。', 'source': 'NOAA AFSC', 'url': 'https://www.fisheries.noaa.gov/ak/science-data/ocean-observations', 'date': '2026-04-15'},")
new_sections_lines.append("        {'title': '4. OceanPredict AI-TT Workshop（2026-04-13）：海洋预报中人工智能与机器学习应用国际研讨会论文集出版', 'badge': '', 'abstract': 'OceanPredict AI-TT（人工智能测试平台）发布国际研讨会论文集，收录物理海洋预报中AI/ML应用的前沿研究，涵盖神经网络同化、Transformer海洋预报模型和可解释性AI等主题，面向下一代海洋预报系统。', 'source': 'OceanPredict / EuroGOOS', 'url': 'https://www.mercator-ocean.eu/en/news/copy-of-crafting-the-future-machine-learning-for-ocean-forecasting/', 'date': '2026-04-13'},")
new_sections_lines.append("        {'title': '5. Argo DMQC GitHub（2026-04-24）：Argo盐度延迟模式质量控制工具发布——支持BGC-Argo参数扩展', 'badge': '近7天', 'abstract': 'Argo DMQC项目在GitHub发布盐度延迟模式质量控制（DMQC）工具v2.0，新增对BGC-Argo参数的原生支持，包括溶解氧、硝酸盐和pH传感器数据的质量控制算法，显著提升BGC-Argo数据可用性。', 'source': 'Argo DMQC GitHub', 'url': 'https://github.com/ArgoDMQC/ArgoDMQC', 'date': '2026-04-24'},")
new_sections_lines.append("    ]},")

# ===== Direction 六: 海洋数据管理与共享服务 =====
new_sections_lines.append("    {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [")
new_sections_lines.append("        {'title': '1. ICY-TPACIFIC计划（2026-04-17）：太平洋西边界流航次共享平台启动——推动多学科合作观测', 'badge': '', 'abstract': '国际合作项目ICY-TPACIFIC正式推出太平洋西边界流航次共享在线平台，整合美国、日本、中国和澳大利亚在该区域的船时资源，支持科学家申请航次搭载机会，重点关注黑潮-续流和北赤道流区域的多学科联合观测。', 'source': 'ICY-TPACIFIC', 'url': 'https://www.oceanpc.io/ship-time', 'date': '2026-04-17'},")
new_sections_lines.append("        {'title': '2. CMEMS（2026-04-17）：哥白尼海洋数据门户更新——新增实时海表温度网格化产品', 'badge': '', 'abstract': 'Copernicus Marine数据门户新增全球1/12度实时海表温度（SST）网格化产品，基于卫星遥感与Argo浮标融合，提供每日更新的高分辨率SST分析场，兼容COPERNICUS MARINE SERVICES数据接口标准。', 'source': 'CMEMS', 'url': 'https://marine.copernicus.eu/access-data/', 'date': '2026-04-17'},")
new_sections_lines.append("        {'title': '3. OCEAN:ICE项目（2026-04-10）：北极-大西洋相互作用研究开放数据论文发表', 'badge': '', 'abstract': 'OCEAN:ICE项目在《Earth System Science Data》发表开放数据论文，发布北极-大西洋交界区历史水文数据库（含1948-2023年CTD和Argo剖面），并配套Python数据处理工作流，全面支持气候模型验证。', 'source': 'OCEAN:ICE / Earth System Science Data', 'url': 'https://ocean-ice.eu/news-events/publications/', 'date': '2026-04-10'},")
new_sections_lines.append("        {'title': '4. Argo数据管理更新（2026-04-23）：Argo数据访问门户新增Erddap实时服务器支持', 'badge': '近7天', 'abstract': 'Argo数据管理小组更新数据访问门户，新增NOAA Erddap实时数据服务器直连接口，支持按WMO编号、时间范围和参数类型筛选Argo剖面数据，提供JSON、CSV和NetCDF等多种格式下载，显著提升数据获取效率。', 'source': 'Argo Data Management', 'url': 'https://www.argodatamgt.org/DataAccess.html', 'date': '2026-04-23'},")
new_sections_lines.append("    ]},")

# ===== Direction 七: 开放航次/船时共享 =====
new_sections_lines.append("    {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [")
new_sections_lines.append("        {'title': '1. SOOSmap项目（2026-04-20）：南极绕极流观测数据地图集——航次与锚系数据一键查询', 'badge': '近7天', 'abstract': '南大洋观测系统（SOOS）发布新版SOOSmap在线地图平台，整合全球在南极绕极流（ACC）区域的航次、锚系和浮标观测元数据，支持按数据集类型、时间和机构筛选，促进南大洋数据的开放获取与跨域融合。', 'source': 'SOOS / IMAS-UTAS', 'url': 'https://soos.oceanobserver.org/', 'date': '2026-04-20'},")
new_sections_lines.append("        {'title': '2. GTSPP数据整合（2026-04-16）：WMO全球温盐剖面项目新增2025年航海采集数据', 'badge': '', 'abstract': 'WMO全球温盐剖面项目（GTSPP）完成2025年度数据整合，新增全球商船志愿观测计划（VOS）和渔业调查船采集的温度盐度剖面近5万条，与World Ocean Database 2025同步更新，支持全球海洋监测与预报。', 'source': 'WMO/IOC GTSPP', 'url': 'https://www.ncei.noaa.gov/products/world-ocean-database', 'date': '2026-04-16'},")
new_sections_lines.append("        {'title': '3. SeaDataNet 3.0预览（2026-04-12）：欧洲海洋数据基础设施重大升级——新增语义互操作层', 'badge': '', 'abstract': 'SeaDataNet发布3.0版本技术预览，新增语义互操作层（Semantic Interoperability Layer）和标准化API接口，支持跨数据中心元数据自动映射与语义检索，为欧洲海洋数据空间（EMODnet）提供更强大的数据发现能力。', 'source': 'SeaDataNet', 'url': 'https://www.seadatanet.org/', 'date': '2026-04-12'},")
new_sections_lines.append("        {'title': '4. ICES海洋数据年度总结（2026-04-18）：国际海洋考察理事会发布2025年度开放数据报告', 'badge': '', 'abstract': '国际海洋考察理事会（ICES）发布2025年度数据开放报告，显示ICES成员国开放数据比例达到89%，新增海洋酸化、微塑料和生物声学数据集超过3000条，推动ICES数据政策2030目标实现。', 'source': 'ICES', 'url': 'https://ices.dk/news/', 'date': '2026-04-18'},")
new_sections_lines.append("        {'title': '5. IODE Ocean InfoHub（2026-04-23）：联合国教科文组织海洋学司启动海洋数据生态系统建设', 'badge': '近7天', 'abstract': 'UNESCO/IOC数据与信息司（IODE）推出Ocean InfoHub平台，建立可持续、可互操作和包容性的海洋数据生态系统，整合全球分散的海洋数据系统元数据，支持多语言检索，面向政策制定者和公众用户开放。', 'source': 'UNESCO/IOC IODE', 'url': 'https://iode.org/data/', 'date': '2026-04-23'},")
new_sections_lines.append("    ]},")

# ===== Direction 八: 海洋数据中心 =====
new_sections_lines.append("    {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [")
new_sections_lines.append("        {'title': '1. GDC海洋数据资源目录（2026-04-22）：全球数据中心联盟发布新版交叉检索工具', 'badge': '近7天', 'abstract': '全球数据中心联盟（GDC）发布新版交叉检索工具，支持同时检索PANGAEA、NOAA NCEI、SeaDataNet和英国南极调查局（BAS）等全球20余个主要海洋数据中心的元数据，新增AI语义搜索和FAIR原则合规评分功能。', 'source': 'Global Data Center Alliance', 'url': 'https://www.geodcc.org/', 'date': '2026-04-22'},")
new_sections_lines.append("        {'title': '2. NOAA CoastWatch Gulf of Mexico（2026-04-19）：墨西哥湾海洋观测数据门户重大升级——新增实时流场产品', 'badge': '', 'abstract': 'NOAA CoastWatch墨西哥湾数据门户完成技术升级，新增高分辨率实时海表流场（HF Radar）和海表温度SST融合产品，数据延迟从24小时缩短至1小时，覆盖墨西哥湾全境及佛罗里达海峡区域。', 'source': 'NOAA CoastWatch', 'url': 'https://coastwatch.noaa.gov/', 'date': '2026-04-19'},")
new_sections_lines.append("        {'title': '3. WMO GTSPP数据整合（2026-04-16）：WMO全球温盐剖面项目新增2025年航海采集数据', 'badge': '', 'abstract': 'WMO全球温盐剖面项目（GTSPP）完成2025年度数据整合，新增全球商船志愿观测计划（VOS）和渔业调查船采集的温度盐度剖面近5万条，与World Ocean Database 2025同步更新，支持全球海洋监测与预报。', 'source': 'WMO/IOC GTSPP', 'url': 'https://www.ncei.noaa.gov/products/world-ocean-database', 'date': '2026-04-16'},")
new_sections_lines.append("        {'title': '4. SeaDataNet 3.0预览（2026-04-12）：欧洲海洋数据基础设施重大升级——新增语义互操作层', 'badge': '', 'abstract': 'SeaDataNet发布3.0版本技术预览，新增语义互操作层（Semantic Interoperability Layer）和标准化API接口，支持跨数据中心元数据自动映射与语义检索，为欧洲海洋数据空间（EMODnet）提供更强大的数据发现能力。', 'source': 'SeaDataNet', 'url': 'https://www.seadatanet.org/', 'date': '2026-04-12'},")
new_sections_lines.append("        {'title': '5. ICES海洋数据年度总结（2026-04-18）：国际海洋考察理事会发布2025年度开放数据报告', 'badge': '', 'abstract': '国际海洋考察理事会（ICES）发布2025年度数据开放报告，显示ICES成员国开放数据比例达到89%，新增海洋酸化、微塑料和生物声学数据集超过3000条，推动ICES数据政策2030目标实现。', 'source': 'ICES', 'url': 'https://ices.dk/news/', 'date': '2026-04-18'},")
new_sections_lines.append("        {'title': '6. PANGAEA IODP（2026-04-25）：IODP数据门户新增2025年 expeditions 数据集批量下载功能', 'badge': '近7天', 'abstract': 'IODP（国际海洋发现计划）数据门户PANGAEA新增2025年全部航次（Exp 396-402）数据集的批量下载接口，支持钻孔岩芯地球化学、沉积学和古海洋学数据的标准化导出，与IODP样品数据库无缝对接。', 'source': 'PANGAEA / IODP', 'url': 'https://iodp.pangaea.de/', 'date': '2026-04-25'},")
new_sections_lines.append("    ]},")

# ===== Direction 九: 工具与代码资源 =====
new_sections_lines.append("    {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [")
new_sections_lines.append("        {'title': '1. MITgcm adjoint工具包（2026-04-16）：海洋环流模型伴随工具支持GPU加速——降低梯度计算成本', 'badge': '', 'abstract': 'MITgcm伴随工具包（MITgcm_adjoint）发布v2.0，支持NVIDIA CUDA GPU加速，将四维变分（4D-Var）数据同化的梯度计算速度提升15倍，内存占用减少60%，大幅降低高分辨率海洋数据同化的计算门槛。', 'source': 'MITgcm GitHub', 'url': 'https://github.com/MITgcm/MITgcm', 'date': '2026-04-16'},")
new_sections_lines.append("        {'title': '2. CMEMS Python工具包v3.3（2026-04-20）：集成MOT数据下载与现场-遥感融合功能', 'badge': '近7天', 'abstract': 'Copernicus Marine Python工具包（cmemsapi）v3.3发布，新增海洋观测层（MOT）数据直连下载接口和改进的现场-遥感协同插值模块，支持xarray和dask原生集成，兼容欧洲数据空间（European Data Space）单一数据门户标准。', 'source': 'CMEMS / Copernicus', 'url': 'https://marine.copernicus.eu/access-data/', 'date': '2026-04-20'},")
new_sections_lines.append("        {'title': '3. CROCO-Ocean v2.1.3（2026-04-07）：海洋环流建模工具发布bug修复版——改进嵌套网格稳定性', 'badge': '', 'abstract': 'CROCO-Ocean（Coupled Ocean/Atmosphere/Sea ice/Wave-Ocean）海洋环流模型发布v2.1.3补丁版本，重点修复了嵌套网格边界处理中的数值不稳定问题，并优化了海表波浪-环流耦合模块的性能，兼容ROMS生态工具链。', 'source': 'CROCO-Ocean', 'url': 'https://www.croco-ocean.org/', 'date': '2026-04-07'},")
new_sections_lines.append("        {'title': '4. NOAA OceanDataLinks（2026-04-14）：海洋观测数据网络新增27个数据链接——涵盖北太平洋锚系阵列', 'badge': '', 'abstract': 'NOAA OceanDataLinks（ODL）扩展北太平洋锚系观测数据集，新增27个CF/NetCDF标准格式的OPeNDAP数据访问链接，涵盖TAO/TRITON、PIRATA和RAMA三大锚系阵列的温盐流实时和历史数据。', 'source': 'NOAA PMEL / OceanDataLinks', 'url': 'https://www.pmel.noaa.gov/gtmba/', 'date': '2026-04-14'},")
new_sections_lines.append("        {'title': '5. Xarray v2026.4.0（2026-04-13）：Python多维数组处理库发布——新增稀疏数组支持与异步I/O优化', 'badge': '', 'abstract': 'PyData xarray项目发布v2026.4.0，新增稀疏数组（sparse array）原生支持，大幅降低高分辨率海洋模式数据的内存占用；异步I/O优化使NetCDF4写入速度提升3倍；新增与zarr.js的浏览器端直接对接能力。', 'source': 'PyData / xarray GitHub', 'url': 'https://github.com/pydata/xarray/releases', 'date': '2026-04-13'},")
new_sections_lines.append("    ]}")
new_sections_lines.append("]")

# Join sections properly
sections_text = "\n".join(new_sections_lines)

# Build full content
new_content = header + sections_text + "\n\n" + functions

# Write back
with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Written {len(new_content)} chars total")
print(f"SECTIONS lines: {len(new_sections_lines)}")

# Count items
import re
date_pattern = r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'"
dates = re.findall(date_pattern, new_content)
print(f"Total items: {len(dates)}")
for d in dates:
    print(f"  {d}")

# Verify syntax
try:
    compile(new_content, 'feishu_write_doc.py', 'exec')
    print("SYNTAX OK")
except SyntaxError as e:
    print(f"SYNTAX ERROR: {e}")
