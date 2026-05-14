#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-05-06 日报 SECTIONS 数据替换脚本
使用 bracket-counting 方法可靠替换 SECTIONS 数据
"""
import re

# 新的 SECTIONS 数据（2026-05-06）
NEW_SECTIONS = [
    {'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [
        {'title': '1. Copernicus Marine Service（2026-05-04）：AI如何推动下一代业务化海洋产品', 'badge': '近7天', 'abstract': '哥白尼海洋服务发布深度文章，揭示AI正在重塑业务化海洋学：北极海冰预报误差降低41%，全球风场ML偏差校正可延伸至预报场，大西洋波浪预报精度显著提升。四款AI增强产品预计2026至2027年间正式上线，标志着基于物理模型与机器学习深度融合的新阶段。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/how-artificial-intelligence-powering-next-generation-operational-marine-products', 'date': '2026-05-04'},
        {'title': '2. 科学网（2026-04-15）：中科院海洋研究所——海洋现象智能预报方法体系研究取得重要进展', 'badge': '近7天', 'abstract': '中国科学院海洋研究所李晓峰、王凡团队在《科学通报》发文，系统梳理海洋状态变量（OSV）预报与海洋现象（OP）预报的概念框架与AI应用进展，提出构建"海洋现象大模型（OP-LOM）"的未来方向，融合多模态数据、物理约束与持续学习，推动海洋预报从"环境场预测"向"事件演化预警"跨越。', 'source': '科学网 / 科学通报', 'url': 'https://news.sciencenet.cn/htmlpaper/2026/4/202641510930755149205.shtm', 'date': '2026-04-15'},
        {'title': '3. arXiv（2026-04-21）：基于自适应时空聚类框架的三维海洋次表层温度重建', 'badge': '近7天', 'abstract': '同济大学团队提出自适应时空聚类框架，结合DP-CNN、ViT等多种深度学习方法，仅使用海表面卫星数据（SST/SSS/SSH/SSW）即可重建三维次表层温度，RMSE相比基准方法提升12.4%～27.2%。该框架具备架构无关性，可广泛集成主流神经网络。', 'source': 'arXiv / 同济大学', 'url': 'https://arxiv.org/html/2605.00860v1', 'date': '2026-04-21'},
        {'title': '4. IEEE（2026-02-25）：AI在海洋卫星遥感中的应用综述', 'badge': '', 'abstract': '发表于IEEE Transactions on Geoscience and Remote Sensing，系统综述AI技术在海洋卫星遥感三大应用领域的进展：参数反演、数据重建和智能解译。覆盖海表温度、盐度、海浪、海流、叶绿素等核心变量，是近期该领域最全面的综述文章之一。', 'source': 'IEEE Xplore', 'url': 'https://ieeexplore.ieee.org/document/11413853', 'date': '2026-02-25'},
    ]},
    {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
        {'title': '1. Destination Earth（2026-04-29）：DestinE气候数字孪生能力论文在GMD发表', 'badge': '近7天', 'abstract': '100余位科学家合作在《地球科学模型发展》期刊发表论文，记录DestinE气候变化适应数字孪生的首次业务化实施成果，实现5~10km分辨率、多十年时间尺度的全球气候预测，支持能源、水资源等行业决策。使用ICON、IFS-FESOM、IFS-NEMO三大地球系统模型，集成AI/ML技术进行气候信息生产。', 'source': 'Destination Earth / ECMWF / Geoscientific Model Development', 'url': 'https://destine.ecmwf.int/news/paper-highlighting-destine-climate-digital-twin-capabilities-published/', 'date': '2026-04-29'},
        {'title': '2. Journal of Marine Science and Engineering（2026-05-01）：深海观测网络数字孪生原型——虚拟环境重建与数据驱动预测', 'badge': '近7天', 'abstract': '提出DSON-DT深海观测网络数字孪生框架，采用虚幻引擎5（UE5）进行高保真海洋环境3D渲染（60FPS、延迟<100ms），并设计改进型AR-LSTM模型用于电量状态（SoC）预测（R²=0.9981），通过MQTT+WebSocket+HTTP全栈架构实现实时遥测与远程控制。', 'source': 'Journal of Marine Science and Engineering / MDPI', 'url': 'https://cdn.ebiotrade.com/newsf/2026-5/20260501084512922.htm', 'date': '2026-05-01'},
    ]},
    {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [
        {'title': '1. Northeast Ocean Data Portal（2026-05-01）：数百个新增浮游生物数据图层正式上线', 'badge': '近7天', 'abstract': '东北海洋数据门户正式发布数百个浮游生物数据图层，分为浮游植物（基于MODIS/VIIRS卫星叶绿素-a）、浮游动物（NOAA EcoMon调查衍生）、鱼类浮游生物（8个物种季节性分布，2003–2021）三大类。这些数据代表海洋食物网基础，可用于物种分布模型和栖息地适宜性评估。', 'source': 'Northeast Ocean Data Portal / MDAT', 'url': 'https://www.northeastoceandata.org/hundreds-of-new-and-updated-plankton-datasets/', 'date': '2026-05-01'},
        {'title': '2. Copernicus Marine（2026-04-28）：2025年用户使用报告发布——年数据请求超110亿次', 'badge': '近7天', 'abstract': '哥白尼海洋服务发布2025年KPI亮点报告：网站访问量超160万次，数据下载量近15PB，数据请求次数突破110亿次。MyOcean可视化服务持续升级，已成为全球海洋科学、航运、能源、海岸管理等行业的核心数据基础设施。', 'source': 'Copernicus Marine Service / Mercator Ocean International', 'url': 'https://marine.copernicus.eu/news/copernicus-marine-user-uptake-2025', 'date': '2026-04-28'},
    ]},
    {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [
        {'title': '1. Scientific Data（2026-04-16）：WOD23——全球最完整海洋原位剖面数据集正式发表', 'badge': '近7天', 'abstract': '美国NOAA/NCEI团队在Scientific Data发表WOD23数据描述文章，该数据集包含约1860万个水柱剖面、36亿次测量，覆盖27个变量，时间跨度1772-2022年，遵循FAIR原则，通过多层次系统性QC（统计检验+专家审核+重复剔除），是目前全球最大的格式统一、质量受控海洋剖面数据集。', 'source': 'Scientific Data / NOAA NCEI', 'url': 'https://www.nature.com/articles/s41597-026-06957-2', 'date': '2026-04-16'},
        {'title': '2. Copernicus Marine In Situ TAC（2026-04-30）：One Ocean Expedition 2025-2026数据集成入CMEMS', 'badge': '近7天', 'abstract': '继2022年首次整合后，哥白尼海洋原位TAC再度将One Ocean Expedition 2025-2026航次的观测数据纳入Copernicus Marine数据平台，实现近实时数据共享与多模型同化使用，进一步扩展全球原位观测数据覆盖。', 'source': 'Copernicus Marine In Situ TAC', 'url': 'https://marineinsitu.eu/data-from-the-one-ocean-expedition-2025-2026-integrated-into-copernicus-marine/', 'date': '2026-04-30'},
    ]},
    {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [
        {'title': '1. ESSD / Taylor & Francis（2026-05-05）：融合卫星高度计优化全球海岸潮汐预测', 'badge': '近7天', 'abstract': '发表于International Journal of Remote Sensing，结合光学遥感与卫星高度计数据，提供全球海洋潮汐模型性能的大陆尺度新洞察，揭示现有潮汐模型在沿海区域存在的显著误差，为海岸管理和海平面监测提供改进基准。', 'source': 'International Journal of Remote Sensing / Taylor & Francis', 'url': 'https://www.tandfonline.com/doi/full/10.1080/01431161.2026.2666912', 'date': '2026-05-05'},
        {'title': '2. CMEMS（2026-05-04）：AI驱动下一代业务化海洋产品——4DVarNet算法应用于SST重建', 'badge': '近7天', 'abstract': '哥白尼海洋服务发布深度技术文章，介绍4DVarNet算法（结合数据同化概念与神经网络架构）在多传感器海表温度重建中的应用，计划于2027年7月上线新产品，在保留细尺度变率的同时降低计算需求。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/how-artificial-intelligence-powering-next-generation-operational-marine-products', 'date': '2026-05-04'},
        {'title': '3. PANGAEA（2026-05-07/08）：PANGAEA社区研讨会——数据发现与获取实操工作坊（即将举行）', 'badge': '近7天', 'abstract': 'PANGAEA即将于2026年5月7-8日举办线上实操研讨会（CEST 10:30-12:30），面向研究人员、数据管理员和分析师，聚焦三大模块：系统性数据发现策略、数据获取与Jupyter Notebooks集成工作流、编程工具与标准实践。报名已开放。', 'source': 'PANGAEA / AWI / MARUM', 'url': 'https://wiki.pangaea.de/wiki/PANGAEA_Community_Workshops#Next_Editions', 'date': '2026-05-01'},
    ]},
    {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [
        {'title': '1. Copernicus Marine（2026-04-29）：了解我们的海洋——海洋观测新系列文章首发', 'badge': '近7天', 'abstract': '哥白尼海洋服务启动"了解我们的海洋"专题系列，首篇聚焦海洋观测体系，探讨如何通过多源观测、建模和数字化手段构建对海洋的系统性理解，为推进数字海洋系统提供科普基础。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/understanding-our-ocean-ocean-observing', 'date': '2026-04-29'},
        {'title': '2. Seabed 2030（2026-04-20）：全球海底测绘新里程碑——一年内新增近500万平方公里数据', 'badge': '近7天', 'abstract': '日本财团-GEBCO Seabed 2030项目宣布全球海底已测绘面积达28.7%，一年内新增近500万平方公里海底数据（创年度记录），距2030年目标取得重大进展。强调海底测绘作为全球公共产品的战略价值，呼吁各国增加数据共享与投入。', 'source': 'Seabed 2030 / Nippon Foundation / GEBCO', 'url': 'https://seabed2030.org/2026/04/20/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year/', 'date': '2026-04-20'},
        {'title': '3. IODE/OBIS（2026-04-10）：IODE/OBIS招募OBIS数据专家——推进Marco-Bolo项目海洋生物多样性数据协调', 'badge': '', 'abstract': 'IODE/OBIS面向EU项目Marco-Bolo发布OBIS数据专家招募公告，该项目旨在加强欧洲海洋生物多样性观测能力建设，优化数据流程与共享机制，招募可帮助推进FAIR数据标准在海洋生物多样性领域落地的数据专家。', 'source': 'IODE / OBIS / IOC-UNESCO', 'url': 'https://iode.org/iode-obis-is-seeking-a-obis-data-expert/', 'date': '2026-04-10'},
    ]},
    {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
        {'title': '1. Schmidt Ocean Institute（2026-05-06）：亚马逊峡谷水下雪崩研究航次即将启航（5月17日）', 'badge': '近7天', 'abstract': 'Schmidt Ocean Institute研究船Falkor(too)将于2026年5月17日启航，赴亚马逊峡谷开展为期35天的浊流（水下雪崩）研究，由MBARI与摩德纳大学联合团队主导，评估浊流频率、速度、地貌影响及有机碳/微塑料迁移，属联合国海洋十年认可项目。', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/', 'date': '2026-05-06'},
        {'title': '2. Nautilus Live（2026-05-01）：E/V Nautilus发布管水母野外指南视频——深海探索科普', 'badge': '近7天', 'abstract': 'E/V Nautilus于2026年5月1日发布深海管水母（Siphonophores）野外指南视频，展示2026年太平洋中西部考察中捕获的深海影像，继续向全球受众实时直播深海科学探索成果。2025年度已完成7次多学科考察，覆盖马里亚纳群岛、所罗门群岛等西太平洋海域。', 'source': 'Ocean Exploration Trust / Nautilus Live', 'url': 'https://nautiluslive.org/', 'date': '2026-05-01'},
    ]},
    {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [
        {'title': '1. GEBCO / Seabed 2030（2026-04-27）：GEBCO_2026 Grid正式发布可下载', 'badge': '近7天', 'abstract': 'GEBCO于2026年4月27日正式发布2026版全球海底地形网格（GEBCO_2026 Grid），提供15弧秒分辨率全球海洋与陆地高程数据，支持netCDF、GeoTiff、ASCII格式下载及OPeNDAP在线访问，属公共领域免费数据，是全球海洋测绘的最新基准产品。', 'source': 'GEBCO / IHO / Nippon Foundation', 'url': 'https://www.gebco.net/news/release-gebco2026-grid', 'date': '2026-04-27'},
        {'title': '2. PANGAEA（2026-04-28）：PANGAEA数据库Event-Campaign Merge架构升级进行中', 'badge': '近7天', 'abstract': 'PANGAEA实施数据库架构重大现代化升级（Event-Campaign Merge），将数据采集事件元数据从固定层级升级为灵活树状层级，支持多级嵌套事件，并新增Location 2字段支持轨迹事件精确定位。升级期间数据搜索与获取服务正常运行，已有数据集与API不受影响。', 'source': 'PANGAEA / AWI / MARUM', 'url': 'https://wiki.pangaea.de/wiki/Event-Campaign-Merge', 'date': '2026-04-28'},
        {'title': '3. NOAA NCEI（2026-04-16）：WOD23发表于Scientific Data——全球海洋原位数据基础资源', 'badge': '近7天', 'abstract': 'NOAA NCEI在Scientific Data发表WOD23数据论文，确立世界海洋数据库2023版的基础数据资源地位。数据覆盖97个国家、2.7万个归档数据集、237,525次科考航次，季度持续更新，支持气候研究、地球系统模型、海洋再分析等多种应用，DOI: 10.25921/v92s-y066。', 'source': 'NOAA NCEI / Scientific Data', 'url': 'https://www.nature.com/articles/s41597-026-06957-2', 'date': '2026-04-16'},
    ]},
    {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [
        {'title': '1. Copernicus Marine Toolbox（2026-04-20）：copernicusmarine v2.4.0 正式发布', 'badge': '近7天', 'abstract': 'copernicusmarine Python工具箱v2.4.0于2026年4月20日正式发布（当前最新稳定版），主要更新：支持Python 3.10-3.14、新增稀疏数据集NetCDF子集提取、密集数据集CSV导出、优化登录凭证复用流程、兼容pandas>=3.0.0，修复了稀疏数据集下载和空文件生成问题。', 'source': 'Mercator Ocean International / Copernicus Marine', 'url': 'https://pypi.org/project/copernicusmarine/', 'date': '2026-04-20'},
        {'title': '2. arXiv（2026-04-21）：自适应时空聚类+深度学习——海洋次表层温度重建框架开源', 'badge': '近7天', 'abstract': '同济大学团队在arXiv发布开放代码研究（arXiv:2605.00860），提供针对海洋次表层温度重建的自适应时空聚类框架，兼容DP-CNN、Attention U-Net、ViT、FFNN、LSTM、OCNN等多种神经网络，实验在南海和印度洋数据上验证，RMSE平均提升12.4%-27.2%。', 'source': 'arXiv / 同济大学', 'url': 'https://arxiv.org/abs/2605.00860', 'date': '2026-04-21'},
        {'title': '3. PANGAEA（2026-05-07/08）：PANGAEA社区工作坊——Jupyter Notebooks集成海洋数据访问', 'badge': '近7天', 'abstract': '面向数据分析师的PANGAEA实操工作坊（线上，5月7-8日），重点演示如何在Jupyter Notebooks等虚拟研究环境中通过编程工具和标准接口无缝访问PANGAEA数据，涵盖数据发现、API调用和工作流集成三大模块，适合海洋数据科学入门用户。', 'source': 'PANGAEA / AWI', 'url': 'https://wiki.pangaea.de/wiki/PANGAEA_Community_Workshops#Next_Editions', 'date': '2026-05-01'},
    ]}
]

def replace_sections_in_file(filepath, new_sections):
    """用 bracket-counting 方法可靠替换 SECTIONS 数据"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 SECTIONS = [ 的位置
    start_marker = 'SECTIONS = ['
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print('ERROR: 未找到 SECTIONS = [')
        return False
    
    # 用 bracket-counting 找结束位置
    bracket_start = start_idx + len(start_marker) - 1  # 指向 [
    depth = 0
    end_idx = bracket_start
    for i, ch in enumerate(content[bracket_start:], bracket_start):
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                end_idx = i
                break
    
    # 生成新的 SECTIONS 字符串
    sections_repr = repr(new_sections)
    new_sections_block = f'SECTIONS = {sections_repr}'
    
    # 替换
    new_content = content[:start_idx] + new_sections_block + content[end_idx+1:]
    
    # 验证语法
    try:
        compile(new_content, filepath, 'exec')
    except SyntaxError as e:
        print(f'ERROR: 语法错误 {e}')
        return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('SUCCESS: SECTIONS 数据已成功替换并通过语法检查')
    return True

if __name__ == '__main__':
    import sys
    filepath = 'C:/Users/Administrator/WorkBuddy/Claw/feishu_write_doc.py'
    result = replace_sections_in_file(filepath, NEW_SECTIONS)
    sys.exit(0 if result else 1)
