#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-05-08 日报 SECTIONS 数据替换脚本
使用 bracket-counting 方法可靠替换 SECTIONS 数据
"""
import sys

# 05-06和05-07已发布URL去重基准
PUBLISHED_URLS = {
    # 05-06
    'https://marine.copernicus.eu/news/how-artificial-intelligence-powering-next-generation-operational-marine-products',
    'https://news.sciencenet.cn/htmlpaper/2026/4/202641510930755149205.shtm',
    'https://arxiv.org/html/2605.00860v1',
    'https://ieeexplore.ieee.org/document/11413853',
    'https://destine.ecmwf.int/news/paper-highlighting-destine-climate-digital-twin-capabilities-published/',
    'https://cdn.ebiotrade.com/newsf/2026-5/20260501084512922.htm',
    'https://www.northeastoceandata.org/hundreds-of-new-and-updated-plankton-datasets/',
    'https://marine.copernicus.eu/news/copernicus-marine-user-uptake-2025',
    'https://www.nature.com/articles/s41597-026-06957-2',
    'https://marineinsitu.eu/data-from-the-one-ocean-expedition-2025-2026-integrated-into-copernicus-marine/',
    'https://marine.copernicus.eu/news/understanding-our-ocean-ocean-observing',
    'https://seabed2030.org/2026/04/20/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year/',
    'https://iode.org/iode-obis-is-seeking-a-obis-data-expert/',
    'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/',
    'https://nautiluslive.org/',
    'https://www.gebco.net/news/release-gebco2026-grid',
    'https://wiki.pangaea.de/wiki/Event-Campaign-Merge',
    'https://www.tandfonline.com/doi/full/10.1080/01431161.2026.2666912',
    'https://pypi.org/project/copernicusmarine/',
    'https://arxiv.org/abs/2605.00860',
    'https://wiki.pangaea.de/wiki/PANGAEA_Community_Workshops#Next_Editions',
    # 05-07
    'https://www.nature.com/articles/s41561-026-01943-0',
    'https://www.sciencedaily.com/releases/2026/04/260421042803.htm',
    'https://ioccg.org/2026/05/may-2026/',
    'https://www.sciencedirect.com/science/article/pii/S1463500326000016',
    'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/',
    'https://svs.gsfc.nasa.gov/5620',
    'https://emodnet.ec.europa.eu/en',
    'https://link.springer.com/article/10.1007/s10872-026-00791-1',
    'https://www.geoaquawatch.org/important-update-for-argo-users-argo-chlorophyll-data-reprocessing-instructional-webinar-may-12th/',
    'https://www.linkedin.com/posts/biogeochemical-argo_important-chlorophyll-calculation-update-activity-7454806893761323008-PaDA',
    'https://oceanexplorer.noaa.gov/news/from-seawater-to-sequences-exploring-noaas-new-deep-sea-environmental-dna-dataset/',
    'https://seabed2030.org/2026/04/20/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year/',
    'https://marine.copernicus.eu/access-data/ocean-state-report/ocean-state-report-9',
    'https://registry.opendata.aws/noaa-nos-cora/',
    'https://www.pangaea.de/',
    'https://github.com/ksr-ocean/goflow',
    'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025GL115016',
    'https://events.marine.copernicus.eu/egu-26',
    'https://finance.sina.com.cn/tech/discovery/2026-05-06/doc-inhwyqhc5689241.shtml',
}

# 新的 SECTIONS 数据（2026-05-08）
NEW_SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '1. Nature Communications（2026-05-07）：南极冰架通道化地形放大融冰敏感性——冷冰架更脆弱', 'badge': '近7天', 'abstract': 'Qin Zhou、Tore Hattermann等在Nature Communications发表高分辨率FVCOM模型研究，揭示南极冰架基底通道化地形能将对海洋变暖的融冰敏感性放大一个数量级。当绕极深层水（CDW）入侵时，通道内差异融冰率异常超过10 m/yr。当前冰盖模型忽略小尺度基底地形，可能严重低估南极冰量损失和海平面上升贡献。', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-71828-8', 'date': '2026-05-07'}, {'title': '2. npj Climate Atmos Sci（2026-05-07）：大西洋海洋热浪质心向赤道偏移——人为变暖驱动', 'badge': '近7天', 'abstract': '国家海洋环境预报中心季宪亮等在npj Climate and Atmospheric Science发表研究，基于1982-2023年多源数据分析，揭示大西洋南北两侧海洋热浪质心（MHWC）以约1°纬度/十年的速率向赤道偏移，无季节相位锁定，线性独立于年际气候变率。人为变暖是主导驱动因子，热带大气-海洋正反馈和上升流减弱是关键机制。', 'source': 'npj Climate Atmos Sci / Nature Portfolio', 'url': 'https://www.nature.com/articles/s41612-026-01426-4', 'date': '2026-05-07'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '1. EGU 2026 / Copernicus Marine（2026-05-03-08）：EGU大会OS4.8专题——哥白尼海洋服务与欧洲海洋数字孪生最新成果', 'badge': '近7天', 'abstract': '在EGU 2026大会OS4.8专题会话中，Copernicus Marine Service联合EuroGOOS展示了海洋建模、数据同化、卫星与原位观测系统、不确定性估计及AI集成等方面的最新研究进展。会话汇聚EDITO Phase 2、全球海洋模型和AI融合预报等前沿成果，关注下一代海洋监测与预报系统的沿海与生态应用。', 'source': 'Copernicus Marine Service / EGU', 'url': 'https://events.marine.copernicus.eu/egu-26', 'date': '2026-05-05'}, {'title': '2. EGU 2026（2026-05-05）：DestinE气候数字孪生能力论文在EGU展示——5~10km分辨率多十年气候预测', 'badge': '近7天', 'abstract': 'EGU 2026期间，DestinE气候数字孪生（Climate DT）在ESSI1.8专题会话中展示其首次业务化实施成果。该系统由100余位科学家协作构建，使用ICON、IFS-FESOM、IFS-NEMO三大地球系统模型，实现5~10km分辨率的多十年全球气候预测，集成AI/ML技术进行气候信息生产，支持能源、水资源等行业决策。相关GMD论文于2026年4月发表。', 'source': 'Destination Earth / ECMWF / GMD', 'url': 'https://gmd.copernicus.org/articles/19/2821/2026/gmd-19-2821-2026.pdf', 'date': '2026-04-14'}]}, {'title': '三、可视化', 'en': 'Visualization', 'items': [{'title': '1. NOAA（2026-05-06/07）：NOAA授予2,160万美元合同采购无人海洋系统——支持新一代测绘船Surveyor和Navigator', 'badge': '近7天', 'abstract': 'NOAA宣布向Chance Maritime Technologies公司（路易斯安那州拉斐特）授予2,160万美元合同，未来五年内采购最多8套无人海洋系统。系统具备直接操控、半自主（碰撞规避+动态航迹跟踪）和全自主三种运行模式，将装备于新一代测绘船Surveyor和Navigator，支持海底测绘和渔业声学调查。NOAA局长Neil Jacobs表示，无人系统将使美国保持在海洋科学创新前沿。', 'source': 'Seapower Magazine / NOAA', 'url': 'https://seapowermagazine.org/noaa-awards-21-6m-for-uncrewed-systems-to-support-new-charting-and-mapping-vessels/', 'date': '2026-05-06'}, {'title': '2. Marine Technology News（2026-05-07）：NOAA Thomas Jefferson号重返五大湖测绘——DriX无人艇加速海底制图', 'badge': '近7天', 'abstract': 'NOAA Thomas Jefferson号调查船时隔四年重返五大湖，将测绘伊利湖西部和中北部（自1940年代以来首次系统测绘）及安大略湖东部。今年夏天将部署DriX无人水面艇（搭载高分辨率多波束声呐，可在"监督自主"模式下连续作业4天以上）在纽约奥斯威戈附近加速测绘。该项目贡献于Lakebed 2030合作计划——目前五大湖仅17%完成测绘，是美国测绘最不充分的区域。', 'source': 'Marine Technology News / NOAA', 'url': 'https://www.marinetechnologynews.com/news/thomas-jefferson-returns-great-661991', 'date': '2026-05-07'}]}, {'title': '四、数据质量', 'en': 'Data Quality', 'items': [{'title': '1. WMO（2026-04-24）：WMO全球季节性气候更新——厄尔尼诺很可能于2026年5-7月回归', 'badge': '近7天', 'abstract': '世界气象组织（WMO）发布最新全球季节性气候更新，赤道太平洋海表温度正在快速上升，气候模型"高度一致"预测厄尔尼诺条件很可能于2026年5-7月发展。WMO气候预测负责人表示"高置信度"。预期影响包括：几乎全球陆地气温偏高，南美南部和美国南部降雨增加，澳大利亚和印度尼西亚干旱风险上升，太平洋飓风增强而大西洋飓风受抑。下一次更新将于5月底发布。', 'source': 'World Meteorological Organization', 'url': 'https://wmo.int/media/news/wmo-likelihood-increases-of-el-nino', 'date': '2026-04-24'}, {'title': '2. Nature Communications（2026-05-07）：热带气旋年最大生命史最大强度的次表层"信使"——可提前数年预测', 'badge': '近7天', 'abstract': '中国海洋大学倪欣宁、张宇、王伟团队在Nature Communications发表研究，揭示西北太平洋热带气旋年最大生命史最大强度（LMI）与一个次表层水团的温度存在强烈关联，呈多年代际V型结构。该水团在北太平洋高压中心下形成并经约4年次表层路径输运至西边界，其高变异热含量调制风暴下方的海表温度。基于北太平洋高压强度可提前数年预测年最大LMI。', 'source': 'Nature Communications / Ocean University of China', 'url': 'https://www.nature.com/articles/s41467-026-72770-5', 'date': '2026-05-07'}]}, {'title': '五、数据处理', 'en': 'Data Processing', 'items': [{'title': '1. IOCCG（2026-05-05）：NASA PACE任务多仪器数据重新处理启动', 'badge': '近7天', 'abstract': 'NASA PACE卫星任务进行大规模数据重新处理，包括OCI V3.0.2 Level-1B/C数据、OCI V3.2 Level-2/3水生地球物理产品，以及HARP2和SPEXone V4.0全级别产品。第6届PACE应用研讨会录像已存档。', 'source': 'IOCCG / NASA', 'url': 'https://ioccg.org/2026/05/may-2026/', 'date': '2026-05-05'}, {'title': '2. IOCCG（2026-05-05）：HyperInSPACE社区处理器HyperCP v1.2.15发布', 'badge': '近7天', 'abstract': 'HyperCP发布v1.2.15重大更新，引入按仪器类别的不确定性预算系统，新增绝对辐射校准表征、耀斑和BRDF校正功能，支持SolarTracker、pySAS等自主观测平台。', 'source': 'IOCCG / HyperInSPACE', 'url': 'https://trainingevents.eumetsat.int/trui/events/2670', 'date': '2026-05-05'}]}, {'title': '六、数据管理与共享', 'en': 'Data Management & Sharing', 'items': [{'title': '1. NOAA AOML（2026-05-05）：NOAA海洋探索办公室与AOML合作发布Okeanos Explorer首套深海eDNA数据集', 'badge': '近7天', 'abstract': 'NOAA海洋探索办公室联合AOML、国家系统学实验室（史密森尼国家自然历史博物馆）和北方湾研究所，公开发布来自Okeanos Explorer号2021-2023年太平洋和大西洋探险的深海环境DNA数据集。原始序列可在NCBI BioProject（PRJNA1284389）获取，物种鉴定信息通过OBIS发布。NOAA将于5月28日中午EDT举办专题研讨会介绍该数据集的科学意义和应用前景。', 'source': 'NOAA AOML / Ocean Exploration', 'url': 'https://www.aoml.noaa.gov/noaa-ocean-exploration-and-aoml-collaborate-to-release-first-edna-data-from-okeanos-explorer/', 'date': '2026-05-05'}, {'title': '2. OCEANS 2026（2026-05-25-28）：IEEE/MTS OCEANS 2026三亚大会即将召开——深海技术、海洋能源与海洋AI', 'badge': '近7天', 'abstract': 'OCEANS 2026三亚大会将于5月25-28日在海南三亚海棠湾红树林度假酒店举行，由IEEE海洋工程学会和MTS联合主办。大会涵盖深海技术、海洋能源、自主水下航行器、海洋观测、海洋AI、水下声学等前沿领域，是国际海洋科技界的旗舰双年会议。注册和摘要提交已开放，来自全球的海洋科技专业者将汇聚交流最新成果。', 'source': 'OCEANS 2026 / IEEE OES / MTS', 'url': 'https://sanya26.oceansconference.org/', 'date': '2026-05-01'}]}, {'title': '七、开放航次/船时共享', 'en': 'Open Research Cruises / Ship-time Sharing', 'items': [{'title': '1. EGU 2026（2026-05-08）：EGU大会最后一天——海洋科学亮点总结', 'badge': '近7天', 'abstract': 'EGU 2026大会于5月8日闭幕，为期6天的会议汇聚了来自全球的地球科学家。海洋科学分部亮点包括：DestinE数字孪生展示、Copernicus Marine AI增强产品、南极冰架稳定性研究、热带气旋次表层预测因子等。EGU新闻中心发布了多份海洋相关新闻稿。', 'source': 'EGU 2026', 'url': 'https://www.egu.eu/gamedia/2026/press-releases/', 'date': '2026-05-08'}, {'title': '2. Astrobiology Magazine（2026-05-06）：Water World Genomics——eDNA解锁深海秘密', 'badge': '近7天', 'abstract': 'Astrobiology Magazine报道NOAA Ocean Exploration的eDNA计划，介绍Okeanos Explorer号自2021年起将环境DNA纳入常规探测作业的决策历程。通过与史密森尼国家自然历史博物馆海洋DNA计划、NOAA渔业国家系统学实验室和AOML合作，NOAA已建立从样品采集到数据共享的完整eDNA工作流程，数据通过NCBI和OBIS向全球开放，为深海生物多样性研究和海洋保护区管理提供关键支撑。', 'source': 'Astrobiology Magazine', 'url': 'https://astrobiology.com/2026/05/water-world-genomics-unlocking-ocean-secrets-with-edna.html', 'date': '2026-05-06'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '1. EGU 2026（2026-05-07）：PANGAEA社区研讨会第二天——数据发现与获取实操培训', 'badge': '近7天', 'abstract': 'PANGAEA地球与环境科学数据平台于5月7-8日在EGU 2026大会期间举行为期两天的社区研讨会（CEST 10:30-12:30），主题为"从PANGAEA发现和获取数据"。课程涵盖系统性数据发现策略、数据获取与Jupyter Notebooks集成工作流、编程工具与标准实践。PANGAEA作为全球最大的地球科学数据仓库之一，拥有数十万条已发布数据集，培训面向研究人员、数据管理员和分析师。', 'source': 'PANGAEA / AWI / MARUM', 'url': 'https://wiki.pangaea.de/wiki/PANGAEA_Community_Workshops#Next_Editions', 'date': '2026-05-07'}, {'title': '2. GBIF（2026-04-18）：NOAA Ocean Exploration eDNA数据集在GBIF注册发布——元数据标准化共享', 'badge': '近7天', 'abstract': '全球生物多样性信息设施（GBIF）正式注册并发布NOAA Ocean Exploration的eDNA宏条形码数据集，数据来自Okeanos Explorer号2021-2023年探险期间通过ROV Deep Discoverer采集的海水样品。该数据集的注册标志着NOAA eDNA数据实现NCBI、OBIS和GBIF三大国际数据库的全覆盖共享，促进深海生物多样性数据的FAIR化，支持全球研究者和决策者获取和利用。', 'source': 'GBIF / NOAA Ocean Exploration', 'url': 'https://www.gbif.org/dataset/9806a672-b859-4175-8432-f805b5ce8f30', 'date': '2026-04-18'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': '1. SCOR（2026-01-08）：第7届IOCCG海洋光学暑期课程开放申请——威尼斯7月5-19日', 'badge': '近7天', 'abstract': '国际海洋色彩协调组（IOCCG）第7届高级暑期讲座系列将于2026年7月5-19日在意大利威尼斯举行，由CNR-ISMAR和威尼斯国际大学主办。课程涵盖海洋光学、生物光学和海洋色彩遥感基础，面向全球学生开放申请，无地理限制。共收到105份申请。', 'source': 'SCOR / IOCCG', 'url': 'https://www.ismar.cnr.it/en/ioccg-summer-school-frontiers-in-ocean-optics-and-ocean-colour-science/', 'date': '2026-01-08'}, {'title': '2. NOAA（2026-05-28预告）：NOAA Omics系列研讨会——从海水到序列：探索NOAA深海eDNA数据集', 'badge': '近7天', 'abstract': 'NOAA Omics研讨会系列联合NOAA图书馆将于5月28日中午EDT举办专题研讨会"From Seawater to Sequences: Exploring NOAA\'s New Deep-Sea Environmental DNA Dataset"，介绍首套来自Okeanos Explorer号的深海eDNA数据集。研讨会将通过Vimeo平台直播，向全球研究者展示数据获取流程、分析方法和科学应用前景。', 'source': 'NOAA Omics / NOAA Library', 'url': 'https://oceanexplorer.noaa.gov/news/from-data-to-discovery-unlocking-ocean-secrets-with-edna/', 'date': '2026-05-05'}]}]

# 跨方向去重检查
all_urls = []
for section in NEW_SECTIONS:
    for item in section['items']:
        url = item['url']
        if url in all_urls:
            print(f"ERROR: 重复URL在同一期内: {url}")
            sys.exit(1)
        all_urls.append(url)
        if url in PUBLISHED_URLS:
            print(f"WARNING: URL已在往期发布: {url}")

# 统计
total_items = sum(len(s['items']) for s in NEW_SECTIONS)
print(f"本期总计: {total_items} 条, {len(all_urls)} 个唯一URL")
for s in NEW_SECTIONS:
    print(f"  {s['title']}: {len(s['items'])} 条")


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
        print('SUCCESS: 语法检查通过')
    except SyntaxError as e:
        print(f'ERROR: 语法错误 {e}')
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'SUCCESS: SECTIONS 数据已成功替换')
    return True


if __name__ == '__main__':
    filepath = 'C:/Users/Administrator/WorkBuddy/Claw/feishu_write_doc.py'
    result = replace_sections_in_file(filepath, NEW_SECTIONS)
    sys.exit(0 if result else 1)
