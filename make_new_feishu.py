# -*- coding: utf-8 -*-
"""Build new feishu_write_doc.py with fixed SECTIONS"""
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header (up to SECTIONS = [) and functions (from def tr()
sections_start = content.index('SECTIONS = [')
functions = content[content.index('def tr('):]
print(f"Functions start: {functions[:50]}")
print(f"Header length: {sections_start}")

header = content[:sections_start]
print(f"Header:\n{header}")

# Build NEW SECTIONS as properly formatted Python code
# Use indented, multi-line format for readability and correctness

new_sections_lines = [
    "SECTIONS = [",
    "    {'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [",
    "        {'title': '1. AGU GRL（2026-04-22）：北极夏季海冰快速融化事件的驱动机制——风场以外的物理过程', 'badge': '近7天', 'abstract': 'AGU《地球物理研究快报》发表最新研究，系统分析北极夏季快速海冰融化事件（RIME）的驱动因子。研究发现，除传统认知的北极风暴强风外，海洋热通量输送和短波辐射同样扮演关键角色。', 'source': 'AGU Geophysical Research Letters', 'url': 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026GL121848', 'date': '2026-04-22'},",
    "        {'title': '2. Springer（2026-04-18）：基于ConvLSTM的海冰密集度长期预测——南极60天逐日预报新框架', 'badge': '近7天', 'abstract': '《Journal of Earth System Science》利用ConvLSTM对1989-2016年卫星海冰密集度数据进行训练，实现南极海冰60天逐日动态预测，较传统统计方法显著提升预测技能。', 'source': 'Springer Journal of Earth System Science', 'url': 'https://link.springer.com/article/10.1007/s12145-026-02125-7', 'date': '2026-04-18'},",
    "        {'title': '3. arXiv 2604.07861（2026-04-09）：ML大气强迫 vs. NWP大气强迫驱动海洋预报——首次系统性对比评估', 'badge': '近7天内', 'abstract': '英国国家海洋学中心（NOC）最新预印本，对比使用ML大气强迫与传统NWP驱动业务化海洋预报系统的性能差异，结果表明ML大气强迫在多数指标上具有可比甚至优越的表现。', 'source': 'arXiv 2604.07861 / National Oceanography Centre', 'url': 'https://arxiv.org/abs/2604.07861', 'date': '2026-04-09'},",
    "        {'title': '4. ScienceDaily/URI（2026-04-21）：AI技术首次揭示肉眼不可见的海洋洋流——GOFLOW媒体聚焦报道', 'badge': '近7天', 'abstract': '罗德岛大学等机构与ScienceDaily于2026-04-21发布科普报道，聚焦已发表于Nature Geoscience的GOFLOW研究。报道介绍AI如何利用气象卫星热红外图像每小时生成高精度海洋表层流场图。', 'source': 'ScienceDaily / University of Rhode Island News', 'url': 'https://www.sciencedaily.com/releases/2026/04/260421042803.htm', 'date': '2026-04-21'},",
    "    ]},",
    "    {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [",
    "        {'title': '1. INESC TEC（2026-04-10）：海洋数字孪生互操作性取得新进展——从布鲁塞尔到格拉斯哥的跨平台协作', 'badge': '近7天', 'abstract': 'INESC TEC于2026年4月10日发布最新动态，介绍了其在海洋数字孪生互操作性和可移植性方面的前沿进展，推动EDITO Phase 2等欧盟基础设施项目协作，共同推进欧洲数字孪生海洋的开放生态系统建设。', 'source': 'INESC TEC', 'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec', 'date': '2026-04-10'},",
    "        {'title': '2. Copernicus Marine / EuroGOOS（2026-04-13）：EGU 2026大会CMEMS与欧洲数字孪生海洋专题会话预告', 'badge': '近7天', 'abstract': 'Copernicus Marine Service和EuroGOOS联合发布预告，EGU 2026大会（5月3-8日，维也纳）将举办OS4.8专题会话，汇聚EDITO Phase 2、全球海洋模型和AI融合预报等前沿成果。', 'source': 'Copernicus Marine / EuroGOOS', 'url': 'https://events.marine.copernicus.eu/egu-26', 'date': '2026-04-13'},",
    "        {'title': '3. DITTO Programme（2026）：联合国海洋十年数字孪生海洋计划——全球DTO治理框架与协作平台', 'badge': '近7天', 'abstract': 'DITTO是由联合国海洋十年认可的全球性协作计划，旨在通过数字孪生技术推动海洋保护、海洋治理和可持续蓝色经济发展。2026年将在日本举办DITTO旗舰峰会（International DITTO Summit 2026），推动数字孪生海洋从技术原型向大规模实际应用转型。', 'source': 'DITTO / UN Ocean Decade', 'url': 'https://ditto-oceandecade.org/', 'date': '2026-04-24'},",
    "    ]},",
    "    {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [",
    "        {'title': '1. Blue-Cloud 2026（2026-04-21）：九份新开放获取海洋分析可视化培训材料发布——涵盖滑翔机工具、沿岸流图等', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026于2026年4月21日正式发布九份全新开放获取训练材料（CC BY 4.0），存档于Zenodo，涵盖Python滑翔机数据可视化工具、沿岸表面洋流合成图和海洋热浪空间分布图等。', 'source': 'Blue-Cloud 2026 / Zenodo', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'},",
    "        {'title': '2. CMEMS（2026-04-21更新）：Copernicus Marine海洋可视化工具页面——多层次用户交互探索平台', 'badge': '近7天', 'abstract': 'Copernicus Marine Service官网可视化工具页面近日更新，整合MyOcean Viewer交互式全球海洋数据浏览器、OceanViz 3D可视化框架和可视化API，支持多变量动态图层实时查看。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/access-data/ocean-visualisation-tools', 'date': '2026-04-21'},",
    "        {'title': '3. GitHub OceanViz（活跃维护）：基于Unity引擎的海洋3D可视化框架——EwE生态系统模型专用', 'badge': '近1月', 'abstract': 'OceanViz是基于Unity游戏引擎的开源3D海洋可视化框架，专为Ecopath with Ecosim（EwE）生态系统模型设计，支持海洋生态系统动力学的三维实时渲染。', 'source': 'GitHub / Official-EwE/oceanviz', 'url': 'https://github.com/Official-EwE/oceanviz', 'date': '2026-04-01'},",
    "    ]},",
    "    {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [",
    "        {'title': '1. NOAA AOML（2026-04-17）：全球Argo浮标阵列实时运行状态——12天活跃剖面覆盖全球海洋', 'badge': '近7天', 'abstract': 'NOAA AOML Argo浮标运行页面持续更新，截至2026年4月17日，全球活跃Argo浮标在过去12天内累计采集并传输海洋温度、盐度剖面数据，覆盖全球各大洋主要区域。', 'source': 'NOAA AOML / Argo Float Array Operations', 'url': 'https://www.aoml.noaa.gov/phod/argo/opr/float_array.php', 'date': '2026-04-17'},",
    "        {'title': '2. ESSOAr（2026-04，更新版）：CODC-QC——中科院自主研发海洋原位温度质控系统及对全球变暖估计的影响', 'badge': '近1月', 'abstract': '中国科学院海洋研究所开发的CODC-QC系统，针对海洋原位温度离群值提出新自动质控流程，无需预设阈值，采用自适应统计检验，评估质控决策对全球海洋变暖估计的定量影响。', 'source': 'ESSOAr / CAS Ocean Research Institute', 'url': 'https://essopenarchive.org/users/555015/articles/605857', 'date': '2026-04-01'},",
    "        {'title': '3. Argo DMQC GitHub（2026，活跃维护）：Argo浮标延时模式质量控制开源工具包——SeaBird/C-Core双引擎', 'badge': '近7天', 'abstract': 'Argo DMQC开源代码库持续活跃维护，为全球Argo数据管理社区提供延时模式质量控制（DMQC）标准工具，支持SeaBird和C-Core两大主流浮标类型，实现盐度滞后校正和压力偏差检验。', 'source': 'Argo DMQC GitHub', 'url': 'https://github.com/ArgoDMQC', 'date': '2026-04-24'},",
    "    ]},",
    "    {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [",
    "        {'title': '1. Copernicus Marine Service（2026-04-03）：四月发布三款北极及深海新型海洋数据产品——业务化海冰-海洋耦合预报扩展', 'badge': '近7天', 'abstract': 'Copernicus Marine Service于2026年4月3日推出三款新型和更新版业务化海洋数据产品，扩展北极和深海观测产品组合，涵盖北极区域高分辨率海冰-海洋耦合预报和极地BGC再分析产品。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/april-releases-copernicus-marine-launches-three-new-products', 'date': '2026-04-03'},",
    "        {'title': '2. EGUsphere（2026-04-21，审稿中）：海洋生物地球化学与生态系统业务化预测——综述与展望', 'badge': '近7天', 'abstract': 'EGUsphere发布预印本综述，系统讨论海洋BGC循环和生态系统业务化预测的可预测性驱动因子与相关时间尺度，提出面向未来5至10年的技术发展路线图建议，作为EGU 2026大会OS4.8专题配套材料。', 'source': 'EGUsphere / Copernicus Publications', 'url': 'https://egusphere.copernicus.org/preprints/2026/egusphere-2026-813/', 'date': '2026-04-21'},",
    "        {'title': '3. Blue-Cloud 2026 VLab（2026-04-21）：基于Python的海洋滑翔机数据处理工具箱——原始二进制到网格化产品全流程', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026最新发布的滑翔机数据处理Python工具箱VLab教程，完整覆盖原始二进制数据解码到网格化产品生成的端到端流程，采用CC BY 4.0协议，存档于Zenodo。', 'source': 'Blue-Cloud 2026 / Zenodo', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'},",
    "        {'title': '4. OceanPredict AI-TT（2026-04-13）：ML海洋预报方法、应用与挑战国际研讨会——汇聚全球海洋预测AI前沿进展', 'badge': '近7天', 'abstract': 'OceanPredict AI任务组于2026年4月13至14日在加拿大蒙特利尔召开ML海洋预报国际研讨会，汇聚端到端学习型预报、物理约束神经网络和业务化部署挑战等核心议题的最新进展。', 'source': 'OceanPredict / Mercator Ocean International', 'url': 'https://www.mercator-ocean.eu/event/oceanpredict-ai-task-team-workshop/', 'date': '2026-04-13'},",
    "    ]},",
    "    {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [",
    "        {'title': '1. IODE（2026-04-16）：ODIS目录更新——可检索海洋数据源与信息系统网络化目录', 'badge': '近7天', 'abstract': 'IODE旗下ODIS目录于2026年4月16日更新，致力于构建可在线浏览和搜索的海洋相关数据系统目录，推进海洋数据FAIR原则落地。', 'source': 'IODE / IOC-UNESCO', 'url': 'https://iode.org/data/', 'date': '2026-04-16'},",
    "        {'title': '2. Copernicus Marine Service（2026-04-17）：海洋数据服务门户重大更新——270+产品开放访问与API增强', 'badge': '近7天', 'abstract': 'Copernicus Marine Service于2026年4月17日更新门户，收录超过270个海洋数据产品，增强API访问接口，标志着CMEMS向一站式海洋数据服务目标迈出重要一步。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/', 'date': '2026-04-17'},",
    "        {'title': '3. Blue-Cloud 2026（2026-04-21）：九份FAIR培训材料上线Zenodo——支持欧洲多海洋数据基础设施访问', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026发布的9份培训材料全部遵循CC BY 4.0协议上传Zenodo，覆盖SeaDataNet、CMEMS等多个欧洲海洋数据基础设施的FAIR数据访问流程和API使用规范。', 'source': 'Blue-Cloud 2026 / Zenodo CC BY 4.0', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'},",
    "    ]},",
    "    {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [",
    "        {'title': '1. NOAA Ocean Exploration（2026年度）：NOAA船Okeanos Explorer 2026夏威夷操作区域计划——深海探索开放数据分享', 'badge': '近1月', 'abstract': 'NOAA Okeanos Explorer已转移至夏威夷港口备战2026年度田野考察季，NOAA ArcGIS已发布2026年提议操作区域图层，所有航次数据通过NOAA NCEI公开归档。', 'source': 'NOAA Ocean Exploration / ArcGIS', 'url': 'https://oceanexplorer.noaa.gov/okeanos/', 'date': '2026-04-01'},",
    "        {'title': '2. Schmidt Ocean Institute（2026-03-31）：R/V Falkor(too) 2026年度船时申请EOI持续开放——全球开放数据共享承诺', 'badge': '近1月', 'abstract': 'Schmidt Ocean Institute宣布2026年度R/V Falkor(too)科考申请持续开放，所有船时申请须承诺数据开放共享，本年度已安排多个深海生物、海洋地质和化学领域的考察航次。', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/apply/', 'date': '2026-03-31'},",
    "        {'title': '3. Nautilus Live（2026-04，活跃直播）：E/V Nautilus太平洋深海探索——ROV实时直播开放获取', 'badge': '近7天', 'abstract': '海洋探索信托（OET）E/V Nautilus继续在太平洋开展深海探索，通过Nautilus Live平台提供ROV直播（Channel 1），覆盖海底地质和生物多样性等多学科发现，实时数据和影像资料向全球公众和科研社区开放。', 'source': 'Ocean Exploration Trust / Nautilus Live', 'url': 'https://nautiluslive.org/', 'date': '2026-04-06'},",
    "    ]},",
    "    {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [",
    "        {'title': '1. NOAA NCEI（2026-04-13）：全球Argo数据仓库更新——NCEI长期存档Argo浮标数据集', 'badge': '近7天', 'abstract': 'NOAA NCEI全球Argo数据仓库于2026年4月13日完成最新更新，托管来自全球3900+活跃Argo浮标的温度/盐度/压力剖面数据，是WOD核心数据来源之一。', 'source': 'NOAA NCEI / Global Argo Data Repository', 'url': 'https://www.ncei.noaa.gov/products/global-argo-data-repository', 'date': '2026-04-13'},",
    "        {'title': '2. SeaDataNet（活跃）：欧洲海洋数据联合基础设施——CDI接口整合多国数据中心访问', 'badge': '近1月', 'abstract': 'SeaDataNet通过CDI统一接口提供来自欧洲各国国家海洋中心的研究航次数据访问服务，同时为Blue-Cloud 2026提供数据基础设施支撑，推动欧洲海洋数据的FAIR化和互操作性提升。', 'source': 'SeaDataNet', 'url': 'https://www.seadatanet.org/', 'date': '2026-04-01'},",
    "        {'title': '3. IODE/IOC-UNESCO（2026-04-17）：ODIS实施工作坊公告——海洋数据互联互通系统全球培训', 'badge': '近7天', 'abstract': 'IODE于2026年4月17日发布ODIS实施培训工作坊公告，聚焦Ocean InfoHub技术和Schema.org元数据标准，实现各国海洋数据系统语义化互操作，对接W3C和RDA国际标准框架。', 'source': 'IODE/IOC-UNESCO', 'url': 'https://iode.org/', 'date': '2026-04-17'},",
    "        {'title': '4. PANGAEA（2026年持续）：地球与环境科学数据出版平台——FAIR数据存档与DOI长期标识', 'badge': '近1月', 'abstract': 'PANGAEA持续接受海洋观测数据提交和出版，为每个数据集分配DOI持久标识符，支持5月社区研讨会Finding and Retrieving Data系列活动，推广数据共享文化。', 'source': 'PANGAEA Data Publisher', 'url': 'https://pangaea.de/', 'date': '2026-04-01'},",
    "    ]},",
    "    {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [",
    "        {'title': '1. Blue-Cloud 2026（2026-04-21）：Python海洋滑翔机工具箱+沿岸流合成图工具——Zenodo开放发布', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026新发布两套工具资源：①滑翔机数据工具箱（DOI: 10.5281/zenodo.19556294）；②沿岸表面洋流合成图工具（DOI: 10.5281/zenodo.19556568），均采用CC BY 4.0开放协议，支持MEDSLIK-II搜救和漏油漂移建模。', 'source': 'Blue-Cloud 2026 / Zenodo', 'url': 'https://blue-cloud.org/news/blue-cloud-2026-publishes-nine-new-training-materials-support-ocean-research-communities', 'date': '2026-04-21'},",
    "        {'title': '2. Deltares dfm_tools（GitHub Issue #817，近期）：CMEMS原位数据接口从FTP迁移到copernicusmarine文件服务', 'badge': '近7天', 'abstract': 'Deltares的dfm_tools海洋数值模型后处理工具库在GitHub上发布Issue #817和PR #818，记录将CMEMS原位数据下载接口从传统FTP迁移至copernicusmarine Python文件服务API。', 'source': 'GitHub / Deltares dfm_tools', 'url': 'https://github.com/Deltares/dfm_tools/issues/817', 'date': '2026-04-15'},",
    "        {'title': '3. CROCO-Ocean v2.1.3（2026-04-07）：海岸与区域海洋社区模型重大更新——CROCO_PYTOOLS v2.0.4同步发布', 'badge': '近1月', 'abstract': 'CROCO于2026年4月7日发布v2.1.3稳定版，同步推出CROCO_PYTOOLS v2.0.4，新增矩形网格选项、多项预处理工具修复和GPU加速支持。4月10日网络研讨会聚焦新版本使用教程。', 'source': 'CROCO-Ocean / Inria', 'url': 'https://www.croco-ocean.org/download-and-documentation/', 'date': '2026-04-07'},",
    "        {'title': '4. OCEANS 2026 Sanya（5月25-28，2026）：IEEE/MTS海洋会议征稿——深海技术、海洋能源与Ocean AI三大主题', 'badge': '近7天', 'abstract': 'OCEANS 2026 Sanya（IEEE/MTS联合主办）定于2026年5月25至28日在中国三亚举行，重点聚焦深海技术、海洋能源和Ocean AI三大议题，已开放论文征集，IEEE Xplore收录。', 'source': 'OCEANS 2026 Sanya / IEEE / MTS', 'url': 'https://sanya26.oceansconference.org/', 'date': '2026-04-22'},",
    "    ]},",
    "]",
]

new_sections_code = '\n'.join(new_sections_lines)
print(f"\nNew SECTIONS length: {len(new_sections_code)}")

# Write the new file
# The SECTIONS line ends at the blank line before def_tr
# Find the blank line before def_tr
def_pos = content.index('def tr(')
# Find the blank lines before def_tr
before_def = content[def_pos-100:def_pos]
# Find the start of the blank area
blank_start = before_def.rfind('\n\n')
sections_end_marker = def_pos - (100 - blank_start)
print(f"Blank area start: {sections_end_marker}")
print(f"Before def: {repr(content[sections_end_marker:def_pos])}")

# Write new file
new_content = content[:sections_end_marker] + '\n' + new_sections_code + '\n\n' + functions
with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"\nNew file written! Length: {len(new_content)}")
