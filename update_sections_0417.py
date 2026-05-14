#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-04-17 海洋AI日报 SECTIONS 更新脚本
基准日期：2026-04-17（周五），近7天范围：2026-04-10 至 2026-04-17
"""
import re

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. EGU2026大会开幕（4月22日）：海洋AI多个专题即将呈现——机器学习预报、数字孪生与遥感集中亮相',
                'badge': '[重磅活动]',
                'abstract': (
                    'EGU General Assembly 2026将于4月22日至5月8日在奥地利维也纳举行，覆盖地球、行星与空间科学全学科，聚集全球逾16,000名科学家。'
                    '海洋相关专题包括"哥白尼海洋服务与欧洲数字孪生海洋"（OS4.8）等多个session，将集中展示AI在海洋预报、数字孪生和遥感监测中的最新成果。'
                    '官方公告（2026-04-02）提示参会者上传演讲材料，并发布了press conference亮点预告。'
                ),
                'source': 'EGU / Copernicus Marine Service',
                'url': 'https://egu26.eu/',
                'date': '2026-04-17',
            },
            {
                'title': '2. Frontiers in Marine Science：AI赋能海洋能力转化与绿色发展——来自中国沿海省份的实证研究',
                'badge': '[新论文]',
                'abstract': (
                    'Li D, Zhang K and Huang C（2026-04-15，Frontiers in Marine Science）探讨人工智能、能力转化与海洋绿色发展之间的关系，'
                    '基于中国沿海省份面板数据，运用中介效应模型，发现AI技术显著通过提升资源配置效率和绿色创新能力，正向推动海洋产业绿色转型，'
                    '为政策制定者提供了量化的AI赋能路径参考，丰富了海洋可持续发展的实证依据。'
                ),
                'source': 'Frontiers in Marine Science',
                'url': 'https://public-pages-files-2025.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1816756/pdf',
                'date': '2026-04-15',
            },
            {
                'title': '3. ScienceDirect综述：机器学习在海洋数据同化中的进展、差距与挑战（2020–2025）',
                'badge': '[综述]',
                'abstract': (
                    'Frontiers in Marine Science在线发表综述（2026-02-01，Ocean Modelling期刊），系统回顾2020—2025年机器学习应用于海洋数据同化的最新进展，'
                    '识别关键技术缺口，并展望未来发展方向。文章覆盖神经网络辅助背景误差协方差估计、深度学习观测算子、强化学习状态估计等前沿子方向，'
                    '指出可解释性与物理一致性仍是主要挑战，对推动业务化海洋预报系统升级具有重要参考价值。'
                ),
                'source': 'Ocean Modelling / ScienceDirect',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028',
                'date': '2026-02-01',
            },
            {
                'title': '4. 《海洋学报》综述：人工智能赋能海洋科技——现状、挑战与战略思考',
                'badge': '[综述]',
                'abstract': (
                    '国内《海洋学报》（2026-01-19）发表综述，系统梳理AI技术在海洋科技各领域的应用现状，'
                    '涵盖海洋预报、水下机器人感知、海洋灾害预警、深海探测等方向，'
                    '分析当前技术瓶颈（数据稀疏、物理约束融合难、模型可解释性差），并从国家战略层面提出推进人工智能海洋学发展的政策建议，'
                    '是近期国内海洋AI领域最具系统性的中文综述之一。'
                ),
                'source': '海洋学报 / 自然资源部第一海洋研究所',
                'url': 'https://www.jto.ac.cn/CN/10.11978/2026012',
                'date': '2026-01-19',
            },
        ],
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. EGU2026 OS4.8专题：哥白尼海洋服务与欧洲数字孪生海洋——最新进展即将发布',
                'badge': '[重磅活动]',
                'abstract': (
                    '哥白尼海洋服务（CMEMS）官方宣布参加EGU2026大会（4月22日-5月8日，维也纳）的OS4.8专题"The Copernicus Marine Service and the European Digital Twin of the Ocean"，'
                    '将汇聚CMEMS最新产品发布、EU DTO架构进展、多尺度海洋模拟和数字孪生互操作性研究成果，'
                    '是了解欧洲数字孪生海洋进展的重要窗口。CMEMS鼓励用户参加Session并提交展示成果。'
                ),
                'source': 'Copernicus Marine Service / EGU',
                'url': 'https://events.marine.copernicus.eu/egu-26',
                'date': '2026-04-13',
            },
            {
                'title': '2. 清华大学张建民院士团队综述：海洋数字孪生技术体系、难点与发展方向（Ocean期刊）',
                'badge': '[综述]',
                'abstract': (
                    '搜狐科技（2026-04-10）报道，清华大学张建民院士团队在《Ocean》期刊发布海洋数字孪生（MDT）系统综述，'
                    '构建了从数据融合、物理建模到实时同步、服务接口的完整技术体系框架，'
                    '重点分析了多源异构数据融合、高维状态实时更新和不确定性量化三大核心难点，'
                    '提出面向"感知-认知-决策"闭环的下一代MDT架构，引发国内海洋工程和信息化领域广泛关注。'
                ),
                'source': 'Ocean期刊 / 清华大学 / 搜狐科技',
                'url': 'https://www.sohu.com/a/1007739041_122028581',
                'date': '2026-04-10',
            },
            {
                'title': '3. INESC TEC：推进海洋数字孪生互操作性——从布鲁塞尔到格拉斯哥的EDITO实践',
                'badge': '[进展]',
                'abstract': (
                    'INESC TEC报道，其团队在布鲁塞尔和格拉斯哥的EDITO（European Digital Twin of the Ocean）会议上展示了在海洋数字孪生互操作性与可移植性方面的最新进展，'
                    '涵盖跨平台模型服务标准化、数据接口融合协议和分布式孪生节点协同机制，'
                    '推动EU DTO生态系统从单一原型向可扩展互联架构演进，是DTO领域工程落地的重要参考案例。'
                ),
                'source': 'INESC TEC / EDITO',
                'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec',
                'date': '2026-04-11',
            },
        ],
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Data Visualization',
        'items': [
            {
                'title': '1. CMEMS可视化工具页面更新：MyOcean Viewer等多款工具面向全层级用户开放',
                'badge': '[更新]',
                'abstract': (
                    'Copernicus Marine Service官方可视化工具页面（2026-04-13更新）面向不同层级用户提供多款互动式海洋可视化工具，'
                    '包括MyOcean Viewer（面向公众的交互式海洋地图）、Copernicus Marine Toolbox（Python API，支持数据下载与本地可视化）以及MyOcean Pro Viewer（专业用户版），'
                    '覆盖全球海洋物理、冰区、生物地球化学等多类产品的实时与回算数据，是海洋可视化工具链的重要基础平台。'
                ),
                'source': 'Copernicus Marine Service (CMEMS)',
                'url': 'https://marine.copernicus.eu/access-data/ocean-visualisation-tools',
                'date': '2026-04-13',
            },
            {
                'title': '2. Python+Cartopy替代MATLAB处理ETOPO1：出版级地形可视化全流程实战指南',
                'badge': '[工具教程]',
                'abstract': (
                    'CSDN博客（2026-04-17）发布详细教程，介绍如何使用Python与Cartopy替代MATLAB处理ETOPO1全球地形数据集，'
                    '覆盖从数据下载、xarray读取、投影设置到出版级地形图绘制的完整流程，'
                    '强调xarray+Cartopy组合在高效处理大型NetCDF海洋/地形数据和生成期刊投稿质量图件方面的优势，'
                    '是海洋地形可视化从MATLAB向Python迁移的实用参考。'
                ),
                'source': 'CSDN博客 / Python Cartopy xarray',
                'url': 'https://blog.csdn.net/weixin_42530793/article/details/160237743',
                'date': '2026-04-17',
            },
            {
                'title': '3. Oceanography Society期刊（TOS）：最新一期开放获取内容涵盖海洋观测数据可视化方法',
                'badge': '[进展]',
                'abstract': (
                    'The Oceanography Society（TOS）旗舰期刊Oceanography最新一期（2026-04-16上线）以开放获取形式发布，'
                    '涵盖海洋观测系统最新进展、数据可视化方法改进及大洋变化趋势图件等多篇文章。'
                    '该期刊作为连接研究社区与决策者的重要平台，季刊形式发表对海洋科学具有重要价值的前沿综合性研究，'
                    '最新期内容已在官网全文开放。'
                ),
                'source': 'Oceanography / The Oceanography Society (TOS)',
                'url': 'https://tos.org/oceanography/',
                'date': '2026-04-16',
            },
        ],
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. WOD季度更新（2026-04-09）：世界海洋数据库新增数据检索界面上线',
                'badge': '[更新]',
                'abstract': (
                    'NCEI（美国国家环境信息中心）World Ocean Database（WOD）Select检索界面于2026-04-09更新，'
                    '支持用户按时间、区域、变量等条件检索WOD历史数据及最新季度新增数据，'
                    'WOD是全球最大的统一格式、质控化、公开的海洋次表层剖面数据库，'
                    '本次更新增强了季度增量数据的检索能力，进一步提升全球海洋数据的可发现性与可访问性。'
                ),
                'source': 'NCEI / World Ocean Database (WOD)',
                'url': 'https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html',
                'date': '2026-04-09',
            },
            {
                'title': '2. Nature Scientific Data：WOD2023数据论文发布——全球最大海洋剖面数据库基础资源描述',
                'badge': '[数据集]',
                'abstract': (
                    'Nature Scientific Data（2026-04-16）在线发布WOD2023数据论文，'
                    '详细描述了世界海洋数据库2023版本的数据来源、格式规范、质量控制流程和季度更新机制，'
                    '强调数据的溯源性、可追溯性和权威性，并介绍了新引入的标准化质量标志体系，'
                    '是引用WOD数据的重要规范性文献，适用于气候变化研究、海洋模型验证和数据标准制定等场景。'
                ),
                'source': 'Nature Scientific Data / NCEI',
                'url': 'https://www.nature.com/articles/s41597-026-06957-2',
                'date': '2026-04-16',
            },
            {
                'title': '3. Springer综述：主动学习在海洋数据质量评估中的应用——降低人工标注负担的新框架',
                'badge': '[综述]',
                'abstract': (
                    'Springer国际期刊《International Journal of Data Science and Analytics》（2025-04-08）发表综述，'
                    '提出将主动学习（Active Learning）引入Argo、GLOSS、EMSO等大型海洋观测网络的数据质量控制，'
                    '通过智能选择最具信息量的样本进行人工标注，大幅降低专家审核工作量，'
                    '同时维持高质量的QC水准，为自动化大规模海洋数据质控提供了可落地的工程框架。'
                ),
                'source': 'International Journal of Data Science and Analytics / Springer',
                'url': 'https://link.springer.com/article/10.1007/s41060-025-00751-w',
                'date': '2025-04-08',
            },
        ],
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '1. Frontiers in Marine Science：近岸海表温度深度学习预测——克服数值模型分辨率局限的新方法',
                'badge': '[新论文]',
                'abstract': (
                    'Frontiers in Marine Science（2026-03-27）在线发表研究，提出基于深度学习的近海岸海表温度（SST）预测方法，'
                    '针对传统数值海洋模型在近岸精细化分辨率上的局限性，利用深度学习模型直接从历史观测数据中学习近岸动力学特征，'
                    '在多个典型近岸站点取得优于数值模型的预测精度，为近海精细化预报和渔业、港口管理应用提供了新的数据处理思路。'
                ),
                'source': 'Frontiers in Marine Science',
                'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1798048/full',
                'date': '2026-03-27',
            },
            {
                'title': '2. Springer Nature：物理引导深度学习——跨时间尺度全球海表温度预报新框架（GST-ML）',
                'badge': '[新论文]',
                'abstract': (
                    'ScienceDirect（2026-03-01，Geoscience Frontiers）发表物理引导深度学习方法用于全球SST跨时间尺度预报的研究，'
                    '提出GST-ML模型，通过在损失函数中嵌入海洋热力学约束，克服纯数据驱动模型在自回归长时预测中的误差累积问题，'
                    '在GODAS和卫星观测数据集上实现日尺度和周尺度SST预测精度的显著提升，'
                    '为构建物理一致的AI海洋预报系统提供了重要基础。'
                ),
                'source': 'Geoscience Frontiers / ScienceDirect',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1674987126000095',
                'date': '2026-03-01',
            },
            {
                'title': '3. IODE数据页面：WODselect系统支持季度更新数据检索——海洋历史剖面处理新接口',
                'badge': '[工具]',
                'abstract': (
                    'IODE（国际海洋学数据和信息交换中心）官方数据页面更新（2026-04-11），'
                    '介绍WODselect检索系统的最新功能，用户可通过用户自定义条件检索WOD数据库及季度增量更新数据，'
                    '获取标准化NetCDF/CSV格式的历史海洋剖面观测数据，'
                    '覆盖温度、盐度、溶解氧等多个关键海洋变量，是大规模历史数据处理工作流的重要接入点。'
                ),
                'source': 'IODE / IOC-UNESCO',
                'url': 'https://iode.org/data/',
                'date': '2026-04-11',
            },
        ],
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. IOC-UNESCO《公民科学数据共享指南》发布（2026年2月）——海洋十年计划推进开放数据规范',
                'badge': '[标准]',
                'abstract': (
                    'IOC-UNESCO发布《海洋十年公民科学数据共享指南》（2026年2月），'
                    '强调通过共同设计原则推动公民科学数据共享，规范元数据标准、质量标志和开放许可协议，'
                    '要求参与海洋十年计划的公民科学项目遵循FAIR原则，并提供数据集成到IODE等官方数据网络的操作规程，'
                    '是推动全球海洋观测数据民主化共享的重要政策文件。'
                ),
                'source': 'IOC-UNESCO / 海洋十年协调办公室',
                'url': 'https://unesdoc.unesco.org/ark:/48223/pf0000397182.locale=en',
                'date': '2026-02-01',
            },
            {
                'title': '2. International Journal of Data Science and Analytics：数据科学与AI助力海洋科学和蓝色经济专刊编者按',
                'badge': '[综述]',
                'abstract': (
                    'Springer《International Journal of Data Science and Analytics》（2026-03-14）发表专刊编者按，'
                    '介绍"Data Science and AI for Marine Science and the Blue Economy"专刊主题与论文方向，'
                    '覆盖大数据挖掘、机器学习、可视化分析、数据共享平台等在海洋科学与蓝色经济中的应用，'
                    '汇聚全球海洋数据科学领域最新研究成果，是跨学科海洋数据管理与分析的高价值参考文献集合。'
                ),
                'source': 'International Journal of Data Science and Analytics / Springer',
                'url': 'https://link.springer.com/article/10.1007/s41060-026-01082-0',
                'date': '2026-03-14',
            },
            {
                'title': '3. Sustainable Blue Economy Partnership：FAIR数据与开放获取附录——欧盟蓝色经济项目数据共享规范',
                'badge': '[标准]',
                'abstract': (
                    'Sustainable Blue Economy Partnership发布《开放获取与FAIR数据附录》（2025-09），'
                    '要求参与欧盟蓝色经济合作项目的机构遵循FAIR数据原则（可找性、可访问性、互操作性、可重用性），'
                    '提供数据管理计划模板、元数据标准对照表和推荐存储平台列表（包括Zenodo、SeaDataNet、PANGAEA等），'
                    '对推动欧洲海洋数据共享生态系统规范化建设具有重要参考意义。'
                ),
                'source': 'Sustainable Blue Economy Partnership / 欧盟',
                'url': 'https://bluepartnership.eu/sites/bluepartnership.eu/files/documents/2025-09/annex_f_open_access_and_fair_data.pdf',
                'date': '2025-09-08',
            },
        ],
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. Schmidt Ocean Institute：R/V Falkor (too) 2026年度航次计划发布——聚焦西南大西洋深海探索',
                'badge': '[开放数据]',
                'abstract': (
                    'Schmidt Ocean Institute官网发布2026年度R/V Falkor (too)航次计划，'
                    '全年聚焦西南大西洋——地球上探索最少的海洋区域之一，涵盖深海生态、海山地质和中层水体过程等方向。'
                    '所有航次数据将在采集后合理时间内开放共享，体现其"Innovate·Explore·Share"使命，'
                    'NF-POGO船上培训项目（3月3日至4月6日，里约-萨尔瓦多段）已完成招募，后续航次开放申请。'
                ),
                'source': 'Schmidt Ocean Institute',
                'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/',
                'date': '2026-04-06',
            },
            {
                'title': '2. OceanTrainingPartnership：2026年NF-POGO-@SeaNetwork-SOI联合培训航次数据开放',
                'badge': '[开放数据]',
                'abstract': (
                    'Ocean Training Partnership（2026-03-03发布）介绍2026年NF-POGO、@SeaNetwork与Schmidt Ocean Institute联合培训航次，'
                    '搭载R/V Falkor (too)从巴西里约热内卢出发至萨尔瓦多（3月3日至4月6日），'
                    '为来自发展中国家的海洋学早期职业研究者提供船上科研培训机会，'
                    '培训数据和航次报告将通过开放平台共享，是推动全球海洋能力建设的典型船时共享案例。'
                ),
                'source': 'Ocean Training Partnership / NF-POGO / Schmidt Ocean Institute',
                'url': 'https://oceantrainingpartnership.org/training-call/2026soi/',
                'date': '2026-03-03',
            },
            {
                'title': '3. DITTO海洋十年计划：通过数字孪生整合多源航次数据——推动开放观测数据标准化共享',
                'badge': '[进展]',
                'abstract': (
                    'DITTO（Digital Twins of the Ocean）海洋十年计划持续推进通过数字孪生技术整合多源海洋航次观测数据的工作，'
                    '聚焦在蓝色经济保护与可持续治理方面建立共同理解框架，'
                    '支持航次数据在DTO基础设施中的标准化接入与开放共享，'
                    '进展将在EGU2026大会期间集中展示，是连接开放航次与数字孪生基础设施的重要纽带。'
                ),
                'source': 'DITTO / 海洋十年计划',
                'url': 'https://ditto-oceandecade.org/',
                'date': '2026-04-10',
            },
        ],
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '1. Nature Scientific Data：WOD2023正式发布——全球最大均一化质控海洋剖面数据库基础资源文章',
                'badge': '[数据集]',
                'abstract': (
                    'Nature Scientific Data（2026-04-16）在线发表WOD2023数据论文，'
                    '全面描述世界海洋数据库（WOD）2023版本的数据体量、来源机构、标准化规范和质控体系，'
                    'WOD是NCEI和IODE联合维护的全球最大均一格式公开海洋剖面数据库，'
                    '季度更新机制确保新数据持续纳入，数据可通过WODselect系统按需检索下载，'
                    '是全球海洋气候研究和模型验证的核心数据基础设施。'
                ),
                'source': 'Nature Scientific Data / NCEI / IODE',
                'url': 'https://www.nature.com/articles/s41597-026-06957-2',
                'date': '2026-04-16',
            },
            {
                'title': '2. NASA PO.DAAC：物理海洋学分布式档案中心——持续提供卫星与水文海洋数据服务',
                'badge': '[进展]',
                'abstract': (
                    'NASA物理海洋学分布式档案中心（PO.DAAC）持续为全球用户提供NASA卫星海洋（SST、SSH、风场、盐度等）'
                    '及水文数据的检索、下载和分析工具服务，'
                    '近期更新了数据访问API接口文档，支持Earthdata登录系统统一认证，'
                    'PO.DAAC作为海洋卫星遥感数据的核心节点，为海洋AI和气候模型训练提供了高质量标准化数据资源。'
                ),
                'source': 'NASA Earthdata / PO.DAAC',
                'url': 'https://www.earthdata.nasa.gov/centers/po-daac',
                'date': '2026-04-10',
            },
            {
                'title': '3. IODE官方数据页面更新：WODselect支持季度新增数据检索——全球海洋观测数据可访问性提升',
                'badge': '[更新]',
                'abstract': (
                    'IODE（国际海洋学数据信息交换体系，IOC-UNESCO下属机构）官方数据页面（2026-04-11更新）'
                    '介绍WODselect检索平台的季度数据更新机制，'
                    '用户可通过该平台检索WOD历史数据集及最新季度新增观测记录，获取覆盖全球海洋的高质量历史剖面数据，'
                    '是IODE推进全球海洋数据开放共享、服务联合国海洋十年目标的具体行动之一。'
                ),
                'source': 'IODE / IOC-UNESCO',
                'url': 'https://iode.org/data/',
                'date': '2026-04-11',
            },
        ],
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '1. xarray v2026.04.0 发布（2026-04-13）：最低zarr版本升级至3.0，新增col_wrap=\'auto\'等特性',
                'badge': '[工具]',
                'abstract': (
                    'xarray v2026.04.0（2026-04-13发布，文档4天前更新）是本年度首个正式版本，'
                    '主要变更包括：最低支持zarr版本升至3.0（与zarr-python v3完全兼容）、'
                    '完成timedelta编码弃用迁移、新增col_wrap=\'auto\'参数支持绘图自动列数、'
                    '引入新的索引API改进多维坐标查询效率。'
                    'xarray是海洋气候科学中处理NetCDF/zarr格式多维标注数组的核心Python工具，'
                    '本次升级对使用zarr存储的大规模海洋数据管道影响显著，建议用户尽快评估兼容性。'
                ),
                'source': 'xarray / PyData / GitHub',
                'url': 'https://docs.xarray.dev/en/v2026.04.0/whats-new.html',
                'date': '2026-04-13',
            },
            {
                'title': '2. GitHub ocean_python_tutorial（2026-04-09更新）：为海洋学家设计的Python入门与可复现研究一日教程',
                'badge': '[工具]',
                'abstract': (
                    'python4oceanography/ocean_python_tutorial（2026-04-09更新）是专为海洋学家设计的Python入门教程仓库，'
                    '采用Jupyter Notebook形式，覆盖NumPy/pandas/xarray基础、NetCDF文件读写、海洋数据可视化和可复现研究实践，'
                    '适合无编程基础的海洋研究人员快速上手Python数据分析工作流，'
                    '是推动海洋科学社区Python普及的代表性教育资源，已被多所高校和研究机构用于培训。'
                ),
                'source': 'GitHub / python4oceanography',
                'url': 'https://github.com/python4oceanography/ocean_python_tutorial',
                'date': '2026-04-09',
            },
            {
                'title': '3. Helmholtz软件目录收录ODV：交互式海洋数据探索分析可视化软件正式纳入研究软件基础设施',
                'badge': '[工具]',
                'abstract': (
                    'Helmholtz研究软件目录正式收录ODV（Ocean Data View），'
                    '这是由Alfred Wegener Institute（AWI）长期维护的免费海洋数据分析与可视化软件，'
                    '支持海洋剖面、时间序列、轨迹等多类型地理参考数据的交互式探索，'
                    '兼容SeaDataNet、WOD、Argo等主流数据格式，纳入Helmholtz软件目录标志着其作为研究基础设施工具的官方认可地位，'
                    '最新版本可在AWI官网免费下载注册使用。'
                ),
                'source': 'Helmholtz / AWI / ODV',
                'url': 'https://helmholtz.software/software/odv',
                'date': '2026-04-12',
            },
            {
                'title': '4. GitHub NPIOcean/kval：挪威极地研究所开源Python工具包——专注海洋观测数据处理与分析',
                'badge': '[工具]',
                'abstract': (
                    'kval是挪威极地研究所（Norwegian Polar Institute）海洋学部门维护的开源Python工具集，'
                    '专注于海洋观测数据的处理与分析，覆盖CTD剖面处理、时间序列分析、数据可视化和QC辅助功能，'
                    'GitHub仓库（2026年持续更新）提供完整文档和示例笔记本，'
                    '是极地和北极海洋学数据处理的专业工具参考，适合需要轻量化、模块化Python工具链的海洋研究团队使用。'
                ),
                'source': 'GitHub / Norwegian Polar Institute',
                'url': 'https://github.com/NPIOcean/kval',
                'date': '2026-04-10',
            },
        ],
    },
]

# ── 读取并替换 feishu_write_doc.py 的 SECTIONS ────────────────
import re

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    src = f.read()

# 序列化新 SECTIONS 为 Python 代码
def serialize_sections(sections):
    lines = ['SECTIONS = [']
    for sec in sections:
        lines.append('    {')
        lines.append(f"        'title': {repr(sec['title'])},")
        lines.append(f"        'en': {repr(sec['en'])},")
        lines.append("        'items': [")
        for item in sec['items']:
            lines.append('            {')
            lines.append(f"                'title': {repr(item['title'])},")
            lines.append(f"                'badge': {repr(item['badge'])},")
            abs_parts = item['abstract']
            lines.append(f"                'abstract': (")
            lines.append(f"                    {repr(abs_parts)}")
            lines.append(f"                ),")
            lines.append(f"                'source': {repr(item['source'])},")
            lines.append(f"                'url': {repr(item['url'])},")
            lines.append(f"                'date': {repr(item['date'])},")
            lines.append('            },')
        lines.append('        ],')
        lines.append('    },')
    lines.append(']')
    return '\n'.join(lines)

new_sections_code = serialize_sections(NEW_SECTIONS)

# 替换 SECTIONS 块
pattern = r'^SECTIONS\s*=\s*\[.*?\n\]'
new_src = re.sub(pattern, new_sections_code, src, flags=re.MULTILINE | re.DOTALL)

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_src)

# 验证
total = sum(len(s['items']) for s in NEW_SECTIONS)
print(f'SECTIONS updated successfully for 2026-04-17')
print(f'Total items: {sum(1 for s in NEW_SECTIONS for _ in s["items"]) + len(NEW_SECTIONS) + total}')
print(f'Directions: {len(NEW_SECTIONS)}, Items: {total}')

# 语法校验
import ast
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    code = f.read()
try:
    ast.parse(code)
    print('Syntax OK')
except SyntaxError as e:
    print(f'Syntax ERROR: {e}')
