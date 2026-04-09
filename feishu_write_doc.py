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

yesterday_cn = (datetime.now() - timedelta(days=1)).strftime('%Y\u5e74%m\u6708%d\u65e5')
today_date = (datetime.now()).strftime('%Y-%m-%d')

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. Proceedings of IEEE综述:AI赋能海洋卫星遥感——参数反演、数据重建与模式发现',
                'badge': '[综述]',
                'abstract': (
                    '中科院海洋研究所李晓峰团队联合多单位在Proceedings of the IEEE（IF 25.9）于2026年2月25日发表综述"AI in Satellite Remote Sensing of the Ocean"，系统总结AI技术在海洋卫星遥感中的最新进展，聚焦三大核心应用：海洋参数反演（SST、SSH、盐度、海冰等）、多源数据融合重建，以及海洋现象（涡旋、锋面、内波）的自动检测与识别。综述展望了AI海洋遥感向大型海洋基础模型演进的路径，是AI与卫星海洋学交叉领域的权威参考。DOI: 10.1109/JPROC.2026.11413853'
                ),
                'source': 'Proceedings of the IEEE / IEEE Xplore',
                'date': '2026-02-25',
                'url': 'https://ieeexplore.ieee.org/document/11413853'
            },
            {
                'title': '2. ScienceDirect:南海"神针"——AI驱动区域海洋预报基础模型的探索路径',
                'badge': '[论文]',
                'abstract': (
                    'Ocean Modelling于2026年4月1日在线发表"South China Sea \'神针(Trident)\' — Solution for Ocean Forecast Foundation Models"，深入分析了全球AI海洋预报模型在区域尺度的局限性，以南海为例提出区域AI海洋基础模型的实用化路径。研究揭示全球模型在热带浅海、强潮汐和季风驱动区域的系统性偏差，论证了专注区域模型不仅在科学上更有效，也是推进AI驱动海洋预报的更可行策略。为区域海洋数字孪生和智能预报系统提供理论依据。'
                ),
                'source': 'Ocean Modelling / ScienceDirect',
                'date': '2026-04-01',
                'url': 'https://www.sciencedirect.com/science/article/pii/S2666675826001116'
            },
            {
                'title': '3. Springer综述:AI赋能可持续蓝色生物技术——海洋资源可持续管理新范式',
                'badge': '[综述]',
                'abstract': (
                    'Springer Blue Biotechnology于2026年4月2日发表综述"Leveraging artificial intelligence (AI) techniques for sustainable marine resources management"，系统评述AI技术在海洋生物资源评估与可持续管理中的最新应用。研究覆盖深度学习在渔业资源监测、海洋生物多样性普查、生态系统模拟和气候变化适应性管理等场景的最新进展，为蓝色经济与海洋AI的交叉融合提供了全面的文献基础。'
                ),
                'source': 'Springer Blue Biotechnology',
                'date': '2026-04-02',
                'url': 'https://link.springer.com/article/10.1186/s44315-026-00054-0'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '1. DITTO峰会2026:JAMSTEC官方主页上线，注册开放——11月横滨湾旗舰大会',
                'badge': '[会议]',
                'abstract': (
                    'JAMSTEC（日本海洋研究开发机构）正式上线"DITTO International Summit 2026"官方会议主页，注册通道开放。本次峰会作为UN海洋十年认可的数字孪生海洋（DITTO）计划旗舰活动，将于2026年11月在日本横滨湾举行，重点议题包括：DTO共享框架与互操作协议、"假设情景"分析能力建设、服务于海洋保护与蓝色经济的实际应用案例，以及下一代海洋数字孪生基础设施。国际合作伙伴ANERIS等已同步推广。'
                ),
                'source': 'JAMSTEC / DITTO / UN Ocean Decade',
                'date': '2026-04(更新)',
                'url': 'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/'
            },
            {
                'title': '2. 厦大海洋所综述:海洋数字孪生赋能蓝色经济——核心架构与应用进展',
                'badge': '[综述]',
                'abstract': (
                    '厦门大学海洋生物地球化学全国重点实验室柴扉教授团队于2026年2月在国际期刊发表综述，系统梳理海洋数字孪生核心架构，深度解析其如何整合物理模型、AI推断和多源实时观测数据，推动蓝色经济创新应用。研究覆盖从近岸水产管理、港口运营优化到深海探测的多元场景，探讨了数据互操作、实时同步和不确定性量化等关键技术挑战，为我国海洋数字孪生发展路径提供战略参考。'
                ),
                'source': '厦门大学海洋与地球学院 / MEL',
                'date': '2026-02-26',
                'url': 'https://mel.xmu.edu.cn/info/1012/61071.htm'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '1. IJDE论文:协同传递函数驱动的海洋流场与温盐场交互可视化',
                'badge': '[论文]',
                'abstract': (
                    'International Journal of Digital Earth于2026年2月9日发表"Interactive visualization of ocean flow and thermohaline field based on collaborative transfer function"，提出一种融合标量场（温盐）与矢量场（流速）的协同传递函数设计方法，实现对海洋温盐流场交互关系的直观可视化。研究标准化了传递函数设计流程，简化了海洋特征提取操作，为理解海洋能量/物质循环机制提供高效的可视化分析工具，适用于海洋数字孪生展示和科学传播场景。'
                ),
                'source': 'International Journal of Digital Earth / Taylor & Francis',
                'date': '2026-02-09',
                'url': 'https://www.tandfonline.com/doi/full/10.1080/17538947.2026.2624176'
            },
            {
                'title': '2. VAPOR平台更新（2026年2月）:大气-海洋-太阳三域三维交互可视化平台',
                'badge': '[工具]',
                'abstract': (
                    'VAPOR（Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers）于2026年2月25日发布更新版本，提供支持大气、海洋和太阳多领域科学数据的交互式三维可视化环境。VAPOR由NCAR主导开发，支持体绘制、流线追踪、粒子动画等高级可视化功能，可生成发表级科学图像，并与Python脚本无缝集成实现批处理可视化，适用于海洋模式输出的时空动态展示与分析。'
                ),
                'source': 'VAPOR / NCAR',
                'date': '2026-02-25',
                'url': 'https://www.vapor.ucar.edu/'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / Marine Data Quality Control',
        'items': [
            {
                'title': '1. IOOS QARTOD更新:实时海洋观测数据QC国际规范持续迭代（2026年4月）',
                'badge': '[标准]',
                'abstract': (
                    'NOAA IOOS于2026年4月更新QARTOD（Quality Assurance of Real-Time Oceanographic Data）系列手册，包含实时海洋数据质量控制标志使用手册和多类仪器（水位、浪高、海流、溶解氧等）的专项QC规程。QARTOD是当前国际上应用最广泛的实时海洋观测数据质量控制标准之一，通过多级QC标志（良好/可疑/坏数据/缺失）规范了自动化质量检查流程，为全球沿海观测网提供统一的数据质量基础设施。'
                ),
                'source': 'NOAA IOOS / QARTOD',
                'date': '2026-04(更新)',
                'url': 'https://ioos.noaa.gov/project/qartod/'
            },
            {
                'title': '2. HAD-QC:混合AI方法实现Argo浮标数据自动化质量控制',
                'badge': '[论文]',
                'abstract': (
                    '2025年11月发表的"HAD-QC: A Hybrid AI Approach for Automated Quality Control of Argo Float Data"提出混合异常检测-质量控制（HAD-QC）框架，将机器学习与现有Argo QC规则结合，提高质控精度并增强解释性。该方法针对Argo海洋观测数据的异常检测问题，通过半监督学习解决标注数据不足和类别不平衡的挑战，为全球Argo数据中心的自动化实时QC提供了可扩展的技术方案，可降低人工审查负担。'
                ),
                'source': 'Springer / ACM DL',
                'date': '2025-11-24',
                'url': 'https://link.springer.com/chapter/10.1007/978-3-032-11442-6_7'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Marine Data Processing',
        'items': [
            {
                'title': '1. Nature Scientific Data:CODC-S全球质控海洋盐度剖面数据集',
                'badge': '[数据集]',
                'abstract': (
                    'Nature Scientific Data于2025年5月发表"CODC-S: A quality-controlled global ocean salinity profiles dataset"，介绍由中国科学院海洋学数据中心（CAS CODC）构建的全球高质量海洋盐度剖面数据库。该数据集融合Argo、CTD、XBT等多源历史观测，涵盖近80年全球盐度剖面数据，经过严格的多级质量控制，统一格式并提供完整元数据。CODC-S为全球海洋盐度变化、水文循环演变研究提供了重要数据基础，已在PANGAEA等平台公开发布。'
                ),
                'source': 'Nature Scientific Data / PMC',
                'date': '2025-05-30',
                'url': 'https://www.nature.com/articles/s41597-025-05172-9'
            },
            {
                'title': '2. MDPI:两阶段智能反演模型——卫星观测重建次表层温盐结构',
                'badge': '[论文]',
                'abstract': (
                    'Journal of Marine Science and Engineering于2026年4月发表"A Two-Stage Intelligent Inversion Model for Subsurface Ocean Temperature and Salinity"，提出利用卫星观测重建次表层温盐三维结构的两阶段深度学习反演框架。该方法突破了传统现场观测高成本、低时空覆盖的局限，融合海表参数与历史剖面数据，高效重建全球次表层温盐分布，为海洋环流分析、热盐输送研究和数值模式数据同化提供低成本替代方案。'
                ),
                'source': 'MDPI / Journal of Marine Science and Engineering',
                'date': '2026-04(在线)',
                'url': 'https://www.mdpi.com/2077-1312/14/7/677'
            },
            {
                'title': '3. GO-BGC全球海洋生物地球化学浮标阵列:2026年3月更新——400+在役BGC浮标',
                'badge': '[进展]',
                'abstract': (
                    'GO-BGC（Global Ocean Biogeochemistry Array）于2026年3月20日更新，持续扩展全球生物地球化学Argo浮标观测网络，目前全球活跃部署超过400个携带化学/生物传感器的BGC-Argo浮标，实时测量溶解氧、pH、硝酸盐、叶绿素、颗粒物和光辐照度六类参数。这一规模化观测网络产生的海量连续剖面数据，为碳循环量化、富营养化监测和气候模型验证提供了前所未有的数据基础，也是深度学习海洋处理算法的重要训练数据源。'
                ),
                'source': 'GO-BGC / PMEL NOAA',
                'date': '2026-03-20',
                'url': 'https://www.go-bgc.org/'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. OBIS 2026-2027工作规划:IODE指导委员会发布社区优先行动路线',
                'badge': '[规划]',
                'abstract': (
                    'IODE OBIS指导委员会第13次会议于2025年12月发布OBIS 2026-2027工作规划，确定以"社区优先"为核心导向，重点推进：扩大全球数据覆盖（重点补强非洲、东南亚和极地区域数据贡献）、完善深海生物多样性数据体系、发展eDNA数据集成标准、提升用户服务能力。该规划将OBIS定位为全球海洋生物多样性监测、昆明-蒙特利尔全球生物多样性框架（GBF）实施和"30×30"保护地目标评估的核心数据支柱。'
                ),
                'source': 'OBIS / IODE / IOC-UNESCO',
                'date': '2025-12-22',
                'url': 'https://portal.obis.org/2025/12/22/obis-workplan-2026-2027/'
            },
            {
                'title': '2. PANGAEA全球海洋地球数据库:持续接收新数据集，支持"数据出版"与DOI引用',
                'badge': '[平台]',
                'abstract': (
                    'PANGAEA（海洋与陆地科学数据发布者）持续作为全球最重要的海洋地球科学数据开放存储库运行，接收并发布来自全球科考航次、Argo浮标、卫星遥感和实验室分析的原始与处理后数据。PANGAEA提供标准化数据引用DOI，支持数据版本控制和引用追踪，与主流学术期刊实施强制数据共享政策联动，是海洋数据FAIR原则落地的标杆平台。其数据发布服务与国际Argo、GO-SHIP、GEOTRACES等大型计划紧密整合。'
                ),
                'source': 'PANGAEA / AWI / MARUM',
                'date': '2026-04(持续更新)',
                'url': 'https://www.pangaea.de/'
            },
            {
                'title': '3. NSF FY2026 IOOS实施资助:4月13日截止——支持区域海洋观测系统互操作与数据共享',
                'badge': '[资助]',
                'abstract': (
                    'NOAA发布FY2026年度IOOS实施资助计划，申请截止日期为2026年4月13日，重点资助美国综合海洋观测系统（IOOS）11个区域协会的运营、数据共享服务和技术互操作能力建设。资助方向包括：区域海洋观测网络运维、ERDDAP/THREDDS数据服务升级、高频雷达和实时浮标数据标准化，以及与CMEMS、Argo等国际系统的数据互操作对接，为沿海海洋数据中心提供重要资金支持。'
                ),
                'source': 'NOAA IOOS / Grantable',
                'date': '2026-04-13(截止)',
                'url': 'https://grantable.co/grants/fy-2026-implementation-of-the-u-s-integrated-ocean-observing-system-ioos-4448efb7741b'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. Schmidt Ocean Institute 2026年度全球航次计划:南大西洋深海探索为核心',
                'badge': '[航次]',
                'abstract': (
                    'Schmidt Ocean Institute于2026年2月22日公布R/V Falkor（too）全年航次计划，重点聚焦南大西洋深海生物多样性普查与海底测绘。2026年多个航次将探索巴西近海深水区和中大西洋洋中脊海山群，记录生物多样性、研究物理化学地质现象并绘制海底地形图。研究所向全球科研团队免费提供船时，所有数据和视频在航次结束后及时公开发布，秉承开放科学精神，是国际海洋开放航次合作的标杆项目。'
                ),
                'source': 'Schmidt Ocean Institute',
                'date': '2026-02-22',
                'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/'
            },
            {
                'title': '2. One Ocean Week 2026(4月18-24日):卑尔根海洋开放科学周——科考船Statsraad Lehmkuhl回港',
                'badge': '[活动]',
                'abstract': (
                    '2026年One Ocean Week将于4月18-24日在挪威卑尔根举行，标志性亮点是完成12个月全球航行的帆船科考船Statsraad Lehmkuhl将于活动开幕日（4月18日）驶入卑尔根港。本届活动议程已上线，涵盖海洋数字孪生、数据开放共享、蓝色经济和海洋气候适应等核心专题，卑尔根大学（UiB）组织多场免费公开活动。此活动为参与国际海洋开放科学合作、建立开放航次数据共享联系的重要窗口。'
                ),
                'source': 'One Ocean Week / UiB / UN Ocean Prediction',
                'date': '2026-04-18(即将)',
                'url': 'https://oneoceanweek.no/en/program/'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Marine Data Centers',
        'items': [
            {
                'title': '1. NOAA IOOS 4月简报:太平洋西北低成本溶氧传感器部署——实时数据向渔业开放',
                'badge': '[新动态]',
                'abstract': (
                    'NOAA IOOS于2026年4月4日发布"Eyes on the Ocean"双周简报，报道当前技术转化（OTT）项目在太平洋西北地区的蟹笼上部署低成本溶解氧传感器，为渔民提供近实时海洋溶氧状况数据，帮助规避贫氧区风险。此举是IOOS将实时海洋数据直接赋能渔业生产决策的典型案例，体现了海洋数据中心从科研服务向社会应用延伸的战略方向，也是低成本海洋传感器网络与数据共享基础设施结合的创新实践。'
                ),
                'source': 'NOAA IOOS / Eyes on the Ocean Newsletter',
                'date': '2026-04-04',
                'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-april-2026/'
            },
            {
                'title': '2. 中科院海洋科学大数据中心(MSDC):数据资源持续扩充，4月1日最新更新',
                'badge': '[更新]',
                'abstract': (
                    '中科院海洋科学大数据中心（MSDC）于2026年4月1日发布最新数据资源更新，持续汇聚中科院海洋研究所科考船队获取的多源西太平洋实测数据，涵盖海洋水文、化学、生物和地质等多学科数据集。MSDC数据门户提供数据可视化、AI分析工具集和在线下载服务，支持全球生物多样性数据和全球观测数据的统一管理与共享。数据DOI/CSTR引用规范的完善推动了数据资产的标准化管理与引用追踪。'
                ),
                'source': '中科院海洋科学大数据中心 / MSDC',
                'date': '2026-04-01',
                'url': 'http://msdc.qdio.ac.cn/'
            },
            {
                'title': '3. Copernicus数据空间生态系统（CDSE）:3月底更新，提供哨兵卫星数据即时开放访问',
                'badge': '[平台]',
                'abstract': (
                    'Copernicus数据空间生态系统（CDSE）于2026年3月31日完成新一轮更新，持续提供对哨兵系列卫星海洋观测数据（Sentinel-3 SST/海冰/海色、Sentinel-1/2海洋SAR）的即时免费开放访问。CDSE作为欧洲哨兵数据的核心分发平台，每天提供超过20TB的新数据，配备交互式浏览器、JupyterHub分析环境和REST API，全面支持海洋遥感数据处理流水线建设，是CMEMS等海洋数据中心的重要上游数据来源。'
                ),
                'source': 'Copernicus Data Space Ecosystem / ESA',
                'date': '2026-03-31',
                'url': 'https://dataspace.copernicus.eu/'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources / Ocean Tools & Software',
        'items': [
            {
                'title': '1. xoa 2026.2.1发布:基于xarray的专业海洋分析库持续迭代',
                'badge': '[工具]',
                'abstract': (
                    'xoa（xarray-based ocean analysis library）于2026年3月3日发布2026.2.1版本，专为处理观测和模式海洋数据设计，深度整合xarray生态系统。xoa提供海洋特有的坐标变换（如sigma坐标到深度）、海洋插值方法（双线性、垂向插值）和标准化绘图工具，与CROCO、NEMO等区域海洋模式输出兼容，是Python海洋数据后处理的重要专业工具库，文档齐全且活跃维护。'
                ),
                'source': 'xoa / Read the Docs / PyPI',
                'date': '2026-03-03',
                'url': 'https://xoa.readthedocs.io/'
            },
            {
                'title': '2. OceanographyWithPython:海洋数据分析Python开源教程仓库持续更新',
                'badge': '[开源]',
                'abstract': (
                    'GitHub上的"OceanographyWithPython"教程仓库（LijoDXL维护）于5天前更新，作为面向海洋科学家的Python数据分析实践教程集，提供从数据读取、可视化到统计分析的完整教学链路，涵盖xarray、cartopy、matplotlib、scipy等核心工具的海洋应用实例。该仓库适合海洋学研究生入门级学习，也是构建海洋AI数据预处理流水线的参考资源，已积累活跃的用户社区。'
                ),
                'source': 'GitHub / OceanographyWithPython',
                'date': '2026-04-04(更新)',
                'url': 'https://github.com/LijoDXL/OceanographyWithPython'
            },
            {
                'title': '3. Norwegian Polar Institute kval:极地海洋数据处理Python工具包',
                'badge': '[开源]',
                'abstract': (
                    'Norwegian Polar Institute（NPI）海洋学组开发的"kval"工具包（GitHub: NPIOcean/kval）提供针对极地海洋观测数据处理与分析的专业Python工具集，覆盖CTD数据QC、时间序列处理、剖面可视化和标准化输出功能。kval专为南极和北极海洋学数据工作流设计，采用xarray/pandas数据模型，并提供符合CF-conventions的NetCDF输出，是极地海洋AI训练数据预处理的重要工具，代码开源且附完整使用文档。'
                ),
                'source': 'GitHub / Norwegian Polar Institute',
                'date': '2026-04(活跃)',
                'url': 'https://github.com/NPIOcean/kval'
            },
        ]
    },
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


def build_all_blocks():
    blocks = []
    blocks.append(paragraph([tr(
        f"\u62a5\u544a\u65e5\u671f\uff1a{yesterday_cn}    "
        "\u6765\u6e90\uff1aarXiv / ScienceDirect / \u4e2d\u79d1\u9662 / IOC-UNESCO / \u817e\u8baf\u65b0\u95fb\u7b49    "
        "\u81ea\u52a8\u751f\u6210"
    )]))
    blocks.append(divider())
    blocks.append(paragraph([tr("")]))

    for sec in SECTIONS:
        blocks.append(heading(sec["title"], level=1))
        blocks.append(paragraph([tr(sec["en"])]))
        blocks.append(paragraph([tr("")]))

        for item in sec["items"]:
            title_full = (item["badge"] + " " + item["title"]) if item.get("badge") else item["title"]
            blocks.append(heading(title_full, level=2))
            blocks.append(paragraph([tr("\u6458\u8981\uff1a", bold=True), tr(item["abstract"])]))
            blocks.append(paragraph([
                tr("\u6765\u6e90\uff1a", bold=True), tr(item["source"]),
                tr("    \u53d1\u5e03\u65f6\u95f4\uff1a", bold=True), tr(item["date"]),
                tr("    \u539f\u6587\u94fe\u63a5\uff1a", bold=True),
                tr(item["url"], link=item["url"])
            ]))
            blocks.append(paragraph([tr("")]))

        blocks.append(divider())
        blocks.append(paragraph([tr("")]))

    blocks.append(paragraph([tr(
        "\u672c\u7b80\u62a5\u6bcf\u65e5\u81ea\u52a8\u751f\u6210\uff0c\u4ec5\u4f9b\u5b66\u672f\u53c2\u8003\u3002\u7248\u6743\u5f52\u539f\u4f5c\u8005/\u673a\u6784\u6240\u6709\u3002"
    )]))
    return blocks


# ── 主流程 ────────────────────────────────────────────────────
def get_token():
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
    )
    if r.status_code != 200:
        raise Exception(f"获取token失败: {r.text}")
    return r.json()["tenant_access_token"]


def create_doc(token):
    r = requests.post(
        "https://open.feishu.cn/open-apis/docx/v1/documents",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": f"\u6d77\u6d0b\u7814\u7a76\u65e5\u62a5_{today_date}"},
        timeout=15
    )
    if r.status_code != 200:
        raise Exception(f"\u521b\u5efa\u6587\u6863\u5931\u8d25: {r.text}")
    data = r.json()["data"]
    return data["document"]["document_id"], data["document"]["title"]


def write_blocks(token, doc_id, blocks):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    # Split into batches of 50 to avoid payload limits
    batch_size = 50
    for i in range(0, len(blocks), batch_size):
        batch = blocks[i:i + batch_size]
        payload = {"children": batch, "index": -1}
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        if r.status_code != 200:
            raise Exception(f"\u5199\u5165\u5757\u5931\u8d25 (batch {i//batch_size}): {r.text}")
        time.sleep(0.3)
    return True


def main():
    token = get_token()
    print("[INFO] token ok")
    doc_id, title = create_doc(token)
    print(f"[INFO] \u6587\u6863\u5df2\u521b\u5efa: {title} (id={doc_id})")
    blocks = build_all_blocks()
    write_blocks(token, doc_id, blocks)
    print(f"[OK] \u5df2\u5199\u5165 {len(blocks)} \u4e2a\u5757")
    doc_url = f"https://{TENANT_DOMAIN}/docx/{doc_id}"
    with open("feishu_doc_url.txt", "w", encoding="utf-8") as f:
        f.write(doc_url)
    print(f"[OK] \u6587\u6863URL: {doc_url}")


if __name__ == "__main__":
    main()
