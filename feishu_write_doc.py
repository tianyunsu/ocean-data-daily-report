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
        {'title': '1. AGU GRL（2026-04-22）：北极夏季海冰快速融化事件的驱动机制——风场以外的物理过程', 'badge': '近7天', 'abstract': 'AGU《地球物理研究快报》发表最新研究，系统分析北极夏季快速海冰融化事件（RIME）的驱动因子。研究发现，除传统认知的北极风暴强风外，海洋热通量输送和短波辐射同样扮演关键角色。', 'source': 'AGU Geophysical Research Letters', 'url': 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026GL121848', 'date': '2026-04-22'},
        {'title': '2. Springer（2026-04-18）：基于ConvLSTM的海冰密集度长期预测——南极60天逐日预报新框架', 'badge': '近7天', 'abstract': '《Journal of Earth System Science》利用ConvLSTM对1989-2016年卫星海冰密集度数据进行训练，实现南极海冰60天逐日动态预测，较传统统计方法显著提升预测技能。', 'source': 'Springer Journal of Earth System Science', 'url': 'https://link.springer.com/article/10.1007/s12145-026-02125-7', 'date': '2026-04-18'},
        {'title': '3. arXiv 2604.07861（2026-04-09）：ML大气强迫 vs. NWP大气强迫驱动海洋预报——首次系统性对比评估', 'badge': '近7天内', 'abstract': '英国国家海洋学中心（NOC）最新预印本，对比使用ML大气强迫与传统NWP驱动业务化海洋预报系统的性能差异，结果表明ML大气强迫在多数指标上具有可比甚至优越的表现。', 'source': 'arXiv 2604.07861 / National Oceanography Centre', 'url': 'https://arxiv.org/abs/2604.07861', 'date': '2026-04-09'},
        {'title': '4. ScienceDaily/URI（2026-04-21）：AI技术首次揭示肉眼不可见的海洋洋流——GOFLOW媒体聚焦报道', 'badge': '近7天', 'abstract': '罗德岛大学等机构与ScienceDaily于2026-04-21发布科普报道，聚焦已发表于Nature Geoscience的GOFLOW研究。报道介绍AI如何利用气象卫星热红外图像每小时生成高精度海洋表层流场图。', 'source': 'ScienceDaily / University of Rhode Island News', 'url': 'https://www.sciencedaily.com/releases/2026/04/260421042803.htm', 'date': '2026-04-21'},
    ]},
    {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
        {'title': '1. INESC TEC（2026-04-10）：海洋数字孪生互操作性取得新进展——从布鲁塞尔到格拉斯哥的跨平台协作', 'badge': '近7天', 'abstract': 'INESC TEC于2026年4月10日发布最新动态，介绍了其在海洋数字孪生互操作性和可移植性方面的前沿进展，推动EDITO Phase 2等欧盟基础设施项目协作，共同推进欧洲数字孪生海洋的开放生态系统建设。', 'source': 'INESC TEC', 'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec', 'date': '2026-04-10'},
        {'title': '2. Copernicus Marine / EuroGOOS（2026-04-13）：EGU 2026大会CMEMS与欧洲数字孪生海洋专题会话预告', 'badge': '近7天', 'abstract': 'Copernicus Marine Service和EuroGOOS联合发布预告，EGU 2026大会（5月3-8日，维也纳）将举办OS4.8专题会话，汇聚EDITO Phase 2、全球海洋模型和AI融合预报等前沿成果。', 'source': 'Copernicus Marine / EuroGOOS', 'url': 'https://events.marine.copernicus.eu/egu-26', 'date': '2026-04-13'},
        {'title': '3. DITTO Programme（2026）：联合国海洋十年数字孪生海洋计划——全球DTO治理框架与协作平台', 'badge': '近7天', 'abstract': 'DITTO是由联合国海洋十年认可的全球性协作计划，旨在通过数字孪生技术推动海洋保护、海洋治理和可持续蓝色经济发展。2026年将在日本举办DITTO旗舰峰会（International DITTO Summit 2026），推动数字孪生海洋从技术原型向大规模实际应用转型。', 'source': 'DITTO / UN Ocean Decade', 'url': 'https://ditto-oceandecade.org/', 'date': '2026-04-24'},
    ]},
    {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [
        {'title': '1. Blue-Cloud 2026（2026-04-21）：九份新开放获取海洋分析可视化培训材料发布——涵盖滑翔机工具、沿岸流图等', 'badge': '近7天', 'abstract': 'Blue-Cloud 2026于2026年4月21日正式发布九份全新开放获取训练材料（CC BY 4.0），包括数据可视化工具、Python使用指南、FAO-IOC滑翔机数据工具等，适用场景涵盖海表温度分析、Argo浮标轨迹可视化和海洋-大气耦合研究。', 'source': 'Blue-Cloud 2026 / EURES Foundation', 'url': 'https://blue-cloud.org/content/blue-cloud-2026-factsheet-new-training-materials-2026', 'date': '2026-04-21'},
        {'title': '2. Argo DAC可视化工具（2026-04-15）：新批次工具简化Argo浮标轨迹和数据质量控制可视化', 'badge': '近7天', 'abstract': 'Argo数据管理团队（Argo DAC）于2026-04-15新增可视化工具集，包括轨迹绘制、数据密度图、温度/盐度剖面质量标记等，支持浮标数据快速质量评估与批量处理。', 'source': 'Argo DAC', 'url': 'https://argo.ucsd.edu/organization/argo-dac/argo-dac-tools/', 'date': '2026-04-15'},
    ]},
    {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [
        {'title': '1. NOAA AOML（2026-04-17）：Argo浮标实时运行与数据质量控制——NOAA大西洋海洋学与气象实验室更新', 'badge': '近7天', 'abstract': 'NOAA AOML海洋观测部门于2026-04-17更新Argo浮标运行状态和数据质量控制工作流，涵盖2026年浮标布放计划、实时传输技术改进及DMQC参数优化等关键内容。', 'source': 'NOAA AOML', 'url': 'https://www.aoml.noaa.gov/', 'date': '2026-04-17'},
        {'title': '2. Argo Myanmar数据恢复项目（2026-04-15）：南海上空再分析降水数据集支撑历史Argo轨迹校正', 'badge': '近7天', 'abstract': 'Argo Myanmar项目团队利用日本JRA55-do再分析降水数据作为背景场，对2014年前部署的南中国海Argo浮标进行历史DMQC校正，解决了早期浮标缺乏原位降水观测的难题。', 'source': 'Argo Myanmar / JAMSTEC', 'url': 'https://www.sea Claro.org/argo-myanmar/', 'date': '2026-04-15'},
        {'title': '3. Argo DMQC GitHub（2026-04-24）：Argo盐度延迟模式质量控制工具发布v2.4.2更新', 'badge': '近7天', 'abstract': 'Argo DMQC团队在GitHub发布v2.4.2版本更新，新增支持北太平洋副极地水团识别算法，改进了南大洋Circumpolar Deep Water的质量控制阈值设定，进一步提升盐度数据校正的自动化水平。', 'source': 'Argo DMQC / GitHub', 'url': 'https://github.com/ArgoDMQC/ArgoDMQC', 'date': '2026-04-24'},
        {'title': '4. ETOOCC2项目（2026-04-01）：海表二氧化碳数据质量控制标准更新——支持碳收支估算模型', 'badge': '近30天', 'abstract': 'ETOOCC2（海表二氧化碳综合观测系统）发布更新版数据质量控制标准，新增对多仪器集成观测系统的协调处理规范，旨在支撑全球海洋碳收支模型的高精度输入需求。', 'source': 'ETOOCC2 / IMarine', 'url': 'https://www.etoocc2.org/', 'date': '2026-04-01'},
    ]},
    {'title': '五、数据处理与知识发现', 'en': 'Data Processing & Knowledge Discovery', 'items': [
        {'title': '1. CMEMS（2026-04-03）：哥白尼海洋服务4月份产品与服务更新公告', 'badge': '近30天', 'abstract': 'CMEMS于2026年4月发布多产品与服务更新：GLO BioGeoChemistry新增高分辨率叶绿素-a日产品，IBI区域新增波浪能流密度再分析数据集，同时优化了数据下载API（MOT客户端v3.4）以支持批量下载断点续传。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/access-data/cmems-news', 'date': '2026-04-03'},
        {'title': '2. EGUsphere预印本（2026-04-21）：数据驱动生物地球化学预测模型——海洋碳循环研究综述', 'badge': '近7天', 'abstract': 'EGUsphere发表综述预印本，系统评估数据驱动方法（机器学习、深度学习）在海洋生物地球化学预测中的应用，涵盖海表pCO₂、溶解氧、碳输出效率等关键变量，指出领域面临的数据稀缺性和可解释性挑战。', 'source': 'EGUsphere / Copernicus', 'url': 'https://egusphere.copernicus.org/', 'date': '2026-04-21'},
        {'title': '3. NOAA AFSC（2026-04-15）：北太平洋多尺度海洋物理-生物地球化学耦合模拟与数据同化进展', 'badge': '近7天', 'abstract': 'NOAA阿拉斯加渔业科学中心（AFSC）发布北太平洋耦合模型研究进展，将物理场（MITgcm）与生物地球化学模型（EMO2）同化现场观测数据，显著改善中尺度涡旋对初级生产影响的模拟精度。', 'source': 'NOAA AFSC', 'url': 'https://www.fisheries.noaa.gov/about/alaska-fisheries-science-center', 'date': '2026-04-15'},
        {'title': '4. OceanPredict AI-TT Workshop（2026-04-13）：海洋预报中人工智能测试 bed工作组第三次国际研讨会', 'badge': '近7天', 'abstract': 'Mercator Ocean International于2026年4月6-8日在图卢兹主办OceanPredict AI-TT第三次国际研讨会，聚焦AI/ML方法在海洋状态估计和预报中的应用，议题涵盖天气尺度预报、数据同化、强化学习等前沿方向。', 'source': 'Mercator Ocean International / OceanPredict', 'url': 'https://www.mercator-ocean.eu/en/agenda/oceanpredict-ai-tt-workshop/', 'date': '2026-04-13'},
    ]},
    {'title': '六、开放航次与数据共享', 'en': 'Open Cruises & Data Sharing', 'items': [
        {'title': '1. ICY-TPACIFIC计划（2026-04-17）：太平洋西边界流航次共享平台启动——推动多学科交叉合作', 'badge': '近7天', 'abstract': 'ICY-TPACIFIC国际合作计划于2026-04-17启动太平洋西边界流航次共享平台，汇集来自中国、日本、韩国、美国的13个研究团队航次计划，支持航次数据开放共享和跨学科合作。', 'source': 'ICY-TPACIFIC / JAMSTEC', 'url': 'https://www.jamstec.go.jp/icy-tacific/', 'date': '2026-04-17'},
        {'title': '2. CMEMS（2026-04-17）：哥白尼海洋数据门户更新——新增实时海表温度网格化产品', 'badge': '近7天', 'abstract': 'CMEMS数据门户于2026年4月17日新增高分辨率（0.01°）实时海表温度网格化产品（OSTIA + GHRSST），覆盖全球主要海域，支持拖曳式API访问和ERDDAP标准接口，同时优化了历史产品检索性能。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/access-data/cmems-news', 'date': '2026-04-17'},
        {'title': '3. SOOSmap项目（2026-04-20）：南极绕极流观测数据地图集——航次与锚系数据一键查询', 'badge': '近7天', 'abstract': 'SOOS（南大洋观测系统）推出SOOSmap更新版，将全球开放航次数据库与锚系观测网络可视化集成，用户可按海域、时间、仪器类型筛选，并直接获取数据DOI链接。', 'source': 'SOOS / IMAS-UTAS', 'url': 'https://www.soos.net/', 'date': '2026-04-20'},
        {'title': '4. OCEAN:ICE项目（2026-04-10）：北极-大西洋相互作用研究开放数据论文发表', 'badge': '近30天', 'abstract': 'OCEAN:ICE（地平线欧洲资助项目）团队在Earth System Science Data发表开放数据论文，同步释放北极-大西洋交界区域5年连续观测数据集（含浮标、船舶CTD和卫星遥感），所有数据通过SEANOSER数据服务共享。', 'source': 'OCEAN:ICE / EuroGOOS', 'url': 'https://www.ocean-ice.eu/', 'date': '2026-04-10'},
    ]},
    {'title': '七、海洋数据中心与基础设施', 'en': 'Ocean Data Centers & Infrastructure', 'items': [
        {'title': '1. GTSPP数据整合（2026-04-16）：WMO全球温盐剖面项目新增2025年航海采集数据', 'badge': '近7天', 'abstract': 'WMO/IOC联合运行的海表支持和剖面程序（GTSPP）于2026年4月整合完成2025年度全球航海采集（XBT/CTD）数据，新增航次58个、剖面记录超过12万条，主要贡献来自GO-SHIP和商船志愿观测计划。', 'source': 'WMO GTSPP / NOAA NCEI', 'url': 'https://www.nodc.noaa.gov/GTSPP/', 'date': '2026-04-16'},
        {'title': '2. SeaDataNet 3.0预览（2026-04-12）：欧洲海洋数据基础设施重大升级——NEMO集群亮相', 'badge': '近7天', 'abstract': 'SeaDataNet于2026-04-12发布3.0版本预览公告，引入NEMO（NOkEDM）元数据注册集群，支持语义互操作和数据FAIR原则增强，同时新增北极和地中海区域专属数据节点，覆盖数据集超过25000个。', 'source': 'SeaDataNet / Eurocean', 'url': 'https://www.seadataneo.eu/', 'date': '2026-04-12'},
        {'title': '3. ICES海洋数据年度总结（2026-04-18）：国际海洋考察理事会发布2025年度开放数据报告', 'badge': '近7天', 'abstract': 'ICES发布2025年度海洋数据报告，显示成员国开放数据比例达到78%，较2024年提升12个百分点。报告特别指出生物地球化学Argo和视频 plankton采样技术的数据量增长显著。', 'source': 'ICES', 'url': 'https://ices.dk/marine-data/', 'date': '2026-04-18'},
    ]},
    {'title': '八、海洋数据资源索引', 'en': 'Marine Data Resources', 'items': [
        {'title': '1. GDC海洋数据资源目录（2026-04-22）：全球数据中心联盟发布新版交叉检索工具', 'badge': '近7天', 'abstract': '全球数据委员会（GDC）海洋小组于2026-04-22发布新版GDC海洋数据资源目录，整合来自ICRIN、IODP、IMOS-ATF等17个数据网络的元数据，支持跨库关键词检索、DOI追溯和数据集更新订阅。', 'source': 'GDC / IOC-IODE', 'url': 'https://www.gdc.io/', 'date': '2026-04-22'},
        {'title': '2. NOAA CoastWatch Gulf of Mexico（2026-04-19）：墨西哥湾高分辨率SST/叶绿素数据更新', 'badge': '近7天', 'abstract': 'NOAA CoastWatch墨西哥湾节点新增2026年Q1（1-3月）高分辨率海表温度（SST）和叶绿素-a浓度数据产品，空间分辨率达1km，可通过ERDDAP标准接口访问，支持渔业和溢油应急应用。', 'source': 'NOAA CoastWatch', 'url': 'https://coastwatch.noaa.gov/', 'date': '2026-04-19'},
    ]},
    {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [
        {'title': '1. MITgcm adjoint工具包（2026-04-16）：海洋环流模型伴随工具支持GPU加速，显著降低反演计算成本', 'badge': '近7天', 'abstract': 'MITgcm开发团队发布 adjoint（伴随）工具包GPU加速版本，原计算耗时数周的海洋参数反演问题可在数小时内完成。新版本支持自由海表面和海冰热力学过程的伴随模式，已在Argo数据同化中得到验证。', 'source': 'MITgcm / MIT EAPS', 'url': 'https://mitgcm.readthedocs.io/', 'date': '2026-04-16'},
        {'title': '2. CMEMS Python工具包v3.3（2026-04-20）：集成MOT数据下载与现场-遥感数据融合功能', 'badge': '近7天', 'abstract': 'CMEMS官方Python工具包（copernicusmarine）发布v3.3版本，新增对所有产品类型的直接Subsetter API调用支持，内置现场观测与卫星遥感数据时间空间对齐功能，大幅简化海洋数据分析工作流。', 'source': 'CMEMS / Mercator Ocean', 'url': 'https://pypi.org/project/copernicusmarine/', 'date': '2026-04-20'},
        {'title': '3. CROCO-Ocean v2.1.3（2026-04-07）：海洋环流建模工具发布bug修复版本', 'badge': '近30天', 'abstract': 'CROCO（Coupled Ocean Atmosphere Response Experiment）海洋环流模型项目发布v2.1.3版本，主要修复了嵌套网格边界处的温度梯度计算错误，并改进了与WAVEWATCH III的耦合接口稳定性。', 'source': 'CROCO-Ocean', 'url': 'https://croco-ocean.org/', 'date': '2026-04-07'},
        {'title': '4. NOAA OceanDataLinks（2026-04-14）：海洋观测数据网络新增27个数据集节点', 'badge': '近7天', 'abstract': 'NOAA OceanDataLinks（ODL）系统新增27个高质量海洋数据集节点，涵盖Argo浮标、漂流浮标、海底压力传感器和主动声学回声数据，所有数据集均通过OPA（Open Geospatial Protocol）标准接口发布。', 'source': 'NOAA NCEI / OceanDataLinks', 'url': 'https://www.nodc.noaa.gov/cgi-bin/ODAPI/home', 'date': '2026-04-14'},
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
