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
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. Nature Geoscience：GOFLOW——静止卫星热成像深度学习框架，首次实现卫星级次中尺度海流观测',
                'badge': '[重磅论文]',
                'abstract': (
                    'Nature Geoscience（2026-04-13，开放获取）发表来自Scripps海洋研究所等机构的重大成果，研究团队提出GOFLOW（Geostationary Ocean Flow）深度学习框架，利用静止卫星连续热成像数据生成每小时、高空间分辨率的海面流速场，不依赖地转平衡假设，并能内在滤除内波噪声。应用于墨西哥湾流区域后，首次从卫星角度提供了次中尺度（submesoscale）流统计，揭示了此前仅在高分辨率数值模型中观察到的涡度-散度不对称性，为地球系统预报、海洋污染监测和气候模型提供了变革性数据来源。'
                ),
                'source': 'Nature Geoscience / Scripps Institution of Oceanography',
                'url': 'https://www.nature.com/articles/s41561-026-01943-0',
                'date': '2026-04-13',
            },
            {
                'title': '2. arXiv预印本：神经网络海洋闭合方案校准——改善粗分辨率全球海洋模型均态与变率',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2026-04-08）发表预印本，提出对神经网络海洋闭合方案（neural network ocean closure）进行系统校准的方法，针对粗分辨率全球海洋模型中中尺度涡未分辨导致的均态偏差与变率问题，通过数据驱动方式训练神经网络代替经验参数化方案，在NEMO等业务化海洋模型的离线测试中显著改善了混合层深度、SST和流场结构，为下一代基于AI的海洋模型参数化提供了可移植框架。'
                ),
                'source': 'arXiv / 海洋模型神经网络参数化',
                'url': 'https://arxiv.org/abs/2604.06398',
                'date': '2026-04-08',
            },
            {
                'title': '3. 中国科学院海洋研究所：AI赋能海洋卫星遥感研究进展综述——系统总结遥感智能解析新进展',
                'badge': '[综述]',
                'abstract': (
                    '科学网（2026-03-27）报道，中国科学院海洋研究所人工智能海洋学研究组联合中国海洋大学、福州大学等机构，在国际学术期刊系统发表AI赋能海洋卫星遥感综述，涵盖SST反演、海面风场估算、内波识别、海底地形推断等典型任务，总结了卷积神经网络、Transformer和物理引导机器学习在遥感图像智能解析中的应用进展与挑战，是国内海洋AI遥感领域的权威综述文献。'
                ),
                'source': '中国科学院海洋研究所 / 科学网',
                'url': 'https://news.sciencenet.cn/htmlnews/2026/3/562156.shtm',
                'date': '2026-03-27',
            },
            {
                'title': '4. Technology Networks：AI揭示前所未有的海洋次中尺度流动细节——GOFLOW成果科普报道',
                'badge': '[进展]',
                'abstract': (
                    'Technology Networks（2026-04-14）对Nature Geoscience发表的GOFLOW成果进行科普报道，指出新方法将气象卫星（如GOES）转化为高分辨率海洋流场观测平台，无需昂贵的专用海洋卫星即可实现近实时次中尺度流监测，成果对海洋污染扩散预测、渔业资源管理和海洋热量输运研究具有重要应用价值，是AI在物理海洋学观测领域的里程碑进展。'
                ),
                'source': 'Technology Networks / Nature Geoscience',
                'url': 'https://www.technologynetworks.com/analysis/news/new-ai-approach-reveals-ocean-currents-in-unprecedented-detail-411632',
                'date': '2026-04-14',
            },
        ],
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. EDITO 2期项目（EDITO 2）正式立项（CORDIS）：欧洲数字孪生海洋进入扩展阶段',
                'badge': '[进展]',
                'abstract': (
                    'EU CORDIS平台显示，EDITO（European Digital Twin Ocean）第二期项目（项目ID 101227771）已于2025年8月正式启动，旨在大幅扩展EDITO基础设施能力、拓宽用户群体，并确立其作为欧洲数字孪生海洋共创核心平台的地位。项目引入更多数字孪生建构工具、支持基于科学的决策制定，并强化与国家和区域DTO计划的互联，是欧洲海洋数字孪生从原型向全规模业务化演进的关键里程碑，将在EGU2026期间集中发布进展。'
                ),
                'source': 'CORDIS / EDITO 2 / 欧盟地平线计划',
                'url': 'https://cordis.europa.eu/project/id/101227771',
                'date': '2026-04-17',
            },
            {
                'title': '2. National Science Review：海洋数字孪生作为蓝色经济创新催化剂——系统回顾与展望',
                'badge': '[综述]',
                'abstract': (
                    'National Science Review（2026-01-20，开放获取）发表题为"Digital twin of the ocean as a catalyst for blue economy innovation"的综述，深入分析海洋数字孪生（DTO）如何通过创建海洋动态虚拟副本推动蓝色经济各子领域创新，包括近海能源开发、港口物流优化、海洋灾害预警和生态系统监测，提出DTO从数字化到克隆（from digitalization to cloning）的技术演进路径，并讨论数据同化、多尺度耦合和实时更新等关键技术瓶颈，是近期最系统的DTO综述之一。'
                ),
                'source': 'National Science Review / Oxford Academic',
                'url': 'https://academic.oup.com/nsr/article/13/3/nwag012/8431396',
                'date': '2026-01-20',
            },
            {
                'title': '3. INESC TEC（2026-04-10）：海洋数字孪生互操作性新进展——EDITO论坛与AGU Ocean Sciences双会展示',
                'badge': '[进展]',
                'abstract': (
                    'INESC TEC官网（2026-04-10）报道，其研究团队在EDITO Digital Ocean Forum和AGU Ocean Sciences Meeting 2026上集中展示了Iliad项目在海洋数字孪生互操作性方面的最新成果，包括跨平台DTO架构标准化、数字孪生节点间数据协议兼容性测试以及多源观测数据实时接入接口设计，推动欧洲各海洋孪生项目向统一互联的DTO生态系统演进，具有重要的工程参考价值。'
                ),
                'source': 'INESC TEC / Iliad Project / EDITO',
                'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec',
                'date': '2026-04-10',
            },
        ],
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Data Visualization',
        'items': [
            {
                'title': '1. Ocean Virtual Laboratory（OVL）：ESA开放卫星与现场综合数据可视化平台（2026-04-10更新）',
                'badge': '[更新]',
                'abstract': (
                    'ESA支持的Ocean Virtual Laboratory（OVL）平台（2026-04-10更新）基于OceanDataLab开源的Syntool可视化引擎，为海洋学家提供卫星遥感、数值模型和现场观测数据的多源综合在线可视化能力，支持SST、海色、海面高度、散射计风场等多类产品的交互展示与比对，平台代码以GNU AGPL协议开放，是推动卫星海洋遥感数据综合可视化的重要开放工具。'
                ),
                'source': 'ESA / OceanDataLab / Ocean Virtual Laboratory',
                'url': 'https://ovl.oceandatalab.com/',
                'date': '2026-04-10',
            },
            {
                'title': '2. Taylor & Francis：交互式海洋流场与标量场可视化——整合矢量-标量耦合的新框架',
                'badge': '[新论文]',
                'abstract': (
                    'Taylor & Francis International Journal of Digital Earth（2026-02-09在线）发表研究，提出整合海洋流场（矢量）与温度/盐度（标量）的交互式可视化框架，突破传统仅展示流线或仅显示标量的局限，实现了标量-矢量耦合的动态可视化，在典型海洋环流区域（如湾流、赤道流）测试中有效揭示了能量-物质耦合输运过程，为海洋动力学交互分析提供了新的可视化工具参考。'
                ),
                'source': 'Taylor & Francis / International Journal of Digital Earth',
                'url': 'https://www.tandfonline.com/doi/full/10.1080/17538947.2026.2624176',
                'date': '2026-02-09',
            },
            {
                'title': '3. 国家海洋科学数据中心：在线数据可视化平台支持海流、海温等多要素实时展示',
                'badge': '[进展]',
                'abstract': (
                    '国家海洋科学数据中心（NMDIS）官网可视化页面提供海流、海温、盐度等多要素实时与历史数据的在线可视化，支持矢量底图、地形底图和影像底图切换，用户可在浏览器内直接交互查看全球及近海区域的多层次海洋环境数据，平台面向科研、业务和公众三类用户开放，是国内海洋数据可视化共享服务的重要入口，近期持续更新数据接入范围和界面功能。'
                ),
                'source': '国家海洋科学数据中心（NMDIS）',
                'url': 'https://mds.nmdis.org.cn/pages/visualization.html',
                'date': '2026-04-18',
            },
        ],
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. GO-BGC全球海洋生物地球化学阵列（2026-04-07更新）：BGC-Argo浮标大规模部署与实时QC系统进展',
                'badge': '[进展]',
                'abstract': (
                    'GO-BGC（Global Ocean Biogeochemistry Array）官网（2026-04-07更新）报告BGC-Argo浮标全球部署规模持续扩大，覆盖氧气、硝酸盐、pH、叶绿素、后向散射和辐射率六类生物地球化学传感器，配套实时质控（RTQC）系统对各参数实施自动异常检测与质量标志，针对深海、极地和赤道等特殊海域环境的QC规则已进行专项优化，成果将支持海洋碳循环监测和全球气候变化评估。'
                ),
                'source': 'GO-BGC / PMEL NOAA / BGC-Argo',
                'url': 'https://www.go-bgc.org/',
                'date': '2026-04-07',
            },
            {
                'title': '2. ASLO L&O Methods：BGC-Argo辐射传感器实时质量评估——超50,000条垂直剖面的系统研究',
                'badge': '[新论文]',
                'abstract': (
                    'Limnology and Oceanography Methods（ASLO，2025-06-21在线）发表BGC-Argo辐射传感器实时质量评估方法研究，系统分析超50,000条BGC-Argo辐射剖面的实时QC表现，提出基于太阳天顶角阈值和辐射传递模型的自动异常检测改进算法，识别出传感器漂移、生物污损和卡值等典型失效模式，研究成果已被纳入Euro-Argo和GO-BGC的RTQC操作流程更新，是BGC数据质量自动化的重要参考。'
                ),
                'source': 'ASLO / Limnology and Oceanography Methods / BGC-Argo',
                'url': 'https://aslopubs.onlinelibrary.wiley.com/doi/10.1002/lom3.10701',
                'date': '2025-06-21',
            },
            {
                'title': '3. GitHub ArgoDMQC：Argo延时模式质控脚本库持续更新——涵盖SBE和RBR传感器双平台',
                'badge': '[工具]',
                'abstract': (
                    'GitHub ArgoDMQC组织仓库持续维护用于Argo延时模式质量控制（DMQC）的脚本集，覆盖SeaBird（SBE）和RBR传感器两类主流Argo浮标平台的数据处理，包括盐度漂移检测、压力校正和温度剖面比对等核心DMQC流程，脚本以开源方式提供，被全球多个国家Argo数据中心（DAC）用于日常业务质控，是全球Argo DMQC社区的核心代码基础设施。'
                ),
                'source': 'GitHub / ArgoDMQC / Argo DMQC',
                'url': 'https://github.com/ArgoDMQC',
                'date': '2026-04-15',
            },
        ],
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '1. Nature Geoscience：GOFLOW静止卫星深度学习框架——实时生成海面次中尺度流场的数据处理新范式',
                'badge': '[重磅论文]',
                'abstract': (
                    'Nature Geoscience（2026-04-13）发表的GOFLOW研究代表海洋遥感数据处理的重大突破，通过深度学习将静止气象卫星（GOES）连续热成像序列转化为每小时级别高分辨率海面流场，处理流程融合时序光流分析、内波噪声滤除和物理一致性约束，无需昂贵的专用海洋卫星，在墨西哥湾流区域应用中实现了真正意义上的次中尺度流场实时生成，是卫星数据处理与深度学习融合的里程碑性工作。'
                ),
                'source': 'Nature Geoscience / GOFLOW / Scripps',
                'url': 'https://www.nature.com/articles/s41561-026-01943-0',
                'date': '2026-04-13',
            },
            {
                'title': '2. Frontiers in Marine Science：物理增强SST深度学习预测——知识引导模型克服纯数据驱动的外推局限',
                'badge': '[新论文]',
                'abstract': (
                    'Frontiers in Marine Science（2026-03-25）在线发表基于物理增强深度学习的海表温度精确预测研究，通过在深度学习损失函数中嵌入海洋热力学能量守恒约束，克服了纯数据驱动模型在极端气候条件下的外推失准问题，在多个典型海域（含热带、温带和高纬度海域）的预测实验中，均优于基准LSTM和MLP模型，实现了物理约束与统计学习的有效融合，为构建气候一致的AI海洋预报系统提供了重要参考。'
                ),
                'source': 'Frontiers in Marine Science',
                'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1775896/full',
                'date': '2026-03-25',
            },
            {
                'title': '3. IOC-UNESCO海洋数据共享培训（2026-04-10）：赋能社区掌握海洋数据处理与共享实践',
                'badge': '[进展]',
                'abstract': (
                    'IOC-UNESCO与海洋十年数据共享协调办公室（DCO-ODS）联合举办培训（2026-04-10，IOC IOCARIBE）"From Observation to Action: Empowering communities towards ocean data sharing"，聚焦提升科研社区海洋观测数据处理、元数据标准化和平台上传共享能力，涵盖ODIS、WODselect和OceanTeacher Global Academy平台的实操培训，是推动海洋观测数据从采集到开放共享全链条能力建设的重要举措。'
                ),
                'source': 'IOC-UNESCO / DCO-ODS / OceanTeacher',
                'url': 'https://iocaribe.ioc-unesco.org/en/event/3081',
                'date': '2026-04-10',
            },
        ],
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. IOC-UNESCO：海平面上升应对中的海洋科学——IOC向联合国提交最新倡议（2026-04-09）',
                'badge': '[政策]',
                'abstract': (
                    'IOC-UNESCO（2026-04-09）在纽约联合国任务代表团研讨会上介绍了海洋科学在支撑海平面上升应对中的关键作用，重申海洋十年框架下数据共享、长期海平面观测网络维护和多国协作数据治理的重要性，倡议建立基于FAIR原则的全球海平面数据开放体系，推动海洋数据服务与国际气候政策直接对接，是IOC在联合国层面推进海洋数据开放共享的重要政策行动。'
                ),
                'source': 'IOC-UNESCO / 联合国海洋科学',
                'url': 'https://www.ioc.unesco.org/en/articles/ioc-brings-ocean-science-forefront-un-declaration-sea-level-rise',
                'date': '2026-04-09',
            },
            {
                'title': '2. IODE官网（2026-04-18更新）：IOC战略计划落地推进——ODIS系统扩展与全球海洋数据发现能力提升',
                'badge': '[进展]',
                'abstract': (
                    'IODE（国际海洋学数据信息交换体系）官网（2026-04-18更新）介绍IOC战略计划中ODIS（Ocean Data and Information System）的实施进展，系统覆盖全球各国家海洋数据中心及相关机构的元数据目录，通过联合索引提升海洋数据全球可发现性，重点推进数据服务标准化（CF Conventions、OceanBestPractices）和跨机构互操作能力建设，是联合国海洋十年数据共享目标落地的核心技术平台。'
                ),
                'source': 'IODE / IOC-UNESCO / ODIS',
                'url': 'https://iode.org/',
                'date': '2026-04-18',
            },
            {
                'title': '3. HUB Ocean蓝色云数据平台：汇聚千余个海洋、气候与生物多样性数据集实现一站式检索',
                'badge': '[进展]',
                'abstract': (
                    'HUB Ocean（独立非营利基金会）旗下Blue-Cloud 2026数据平台持续整合来自CMEMS、PANGAEA、NOAA、EMODnet等全球权威机构的海洋、气候和生物多样性数据集，提供跨机构统一的搜索、筛选和可视化入口，支持FAIR原则和开放数据共享，是欧盟Blue-Cloud计划推进联合联邦式欧洲海洋数据生态系统的核心基础设施，当前平台已收录数千个数据集，持续新增数据来源。'
                ),
                'source': 'HUB Ocean / Blue-Cloud 2026 / 欧盟',
                'url': 'https://www.hubocean.earth/',
                'date': '2026-04-15',
            },
        ],
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. POGO官网（2026-04-12更新）：Ocean Training Partnership 2026船上培训项目开放申请',
                'badge': '[进展]',
                'abstract': (
                    'Partnership for Observation of the Global Ocean（POGO）官网（2026-04-12更新）发布Ocean Training Partnership（OTP）2026年度船上培训最新进展，介绍当前可申请航次机会和已开放申请名额，OTP是由NF-POGO、SMART和多家国际海洋机构联合运营的全球船上培训协调平台，为来自发展中国家的早期职业海洋学家提供实船培训机会，培训期间收集的数据须按开放原则提交相关数据中心共享。'
                ),
                'source': 'POGO / Ocean Training Partnership',
                'url': 'https://pogo-ocean.org/capacity-development/shipboard-training/',
                'date': '2026-04-12',
            },
            {
                'title': '2. OTP申请页（2026-03-30更新）：2026年船上培训推荐信规范与申请流程说明',
                'badge': '[开放申请]',
                'abstract': (
                    'Ocean Training Partnership官网申请页（2026-03-30更新）详细说明了2026年度船上培训申请中推荐信的具体要求和提交规范，明确要求推荐信必须针对本次培训机会专项撰写，并在"Closed Calls"区域提供历届培训信息参考。OTP项目旨在通过搭载全球多艘顶级科考船（包括R/V Falkor、RRS Discovery等），系统提升低收入国家海洋科学人才的实地观测和数据处理能力，推动开放航次数据共享。'
                ),
                'source': 'Ocean Training Partnership / OTP',
                'url': 'https://oceantrainingpartnership.org/apply-for-shipboard-training/',
                'date': '2026-03-30',
            },
            {
                'title': '3. LSSF中科院船时开放计划：中国科学院海洋考察共享船时申请第一轮公告（2025-08-19）',
                'badge': '[开放申请]',
                'abstract': (
                    '中科院重大科技基础设施共享服务平台（LSSF）发布中国科学院海洋考察共享船时第一轮开放申请公告，面向国内海洋科研机构提供中国科学院海洋研究所（IOCAS）考察船搭载名额，着力响应国家海洋科研需求，进一步推进考察船资源开放共享。船时共享制度要求用户数据按规定时间内提交IOCAS数据管理系统，并在合理期限内向全球开放，是国内开放航次制度化建设的重要案例。'
                ),
                'source': 'LSSF / 中国科学院海洋研究所（IOCAS）',
                'url': 'https://lssf.cas.cn/en/facilities/ese/morv/notice/202508/t20250825_5080362.html',
                'date': '2025-08-19',
            },
        ],
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '1. NCEI全球Argo数据存储库（2026-04-13更新）：全球最大Argo数据存档持续扩充',
                'badge': '[更新]',
                'abstract': (
                    'NOAA NCEI全球Argo数据存储库（Global Argo Data Repository）页面（6天前更新，2026-04-13）介绍了Argo海洋剖面观测网络的最新数据存档规模与服务进展，NCEI作为美国Argo GDAC镜像节点，持续存档全球Argo浮标实时与延时模式数据，覆盖温度、盐度及BGC参数，数据通过NCEI数据门户和OPeNDAP接口向全球用户开放访问，是全球海洋观测基础设施数据服务的重要组成。'
                ),
                'source': 'NOAA NCEI / Global Argo Data Repository',
                'url': 'https://www.ncei.noaa.gov/products/global-argo-data-repository',
                'date': '2026-04-13',
            },
            {
                'title': '2. NOAA NCEI WOD页面（2026-04-18更新）：WOD提供全球最大质控公开海洋剖面数据服务',
                'badge': '[更新]',
                'abstract': (
                    'NOAA NCEI World Ocean Database产品页（2026-04-18更新）介绍WOD作为全球最大统一格式、质量控制、公开海洋剖面数据集合的最新服务状态，涵盖温度、盐度、溶解氧、营养盐等变量的历史剖面观测记录，数据通过WODselect系统按需检索下载，Nature Scientific Data（2026-04-16）已发表WOD2023正式数据论文，进一步确立其作为全球海洋气候研究核心数据资源的地位。'
                ),
                'source': 'NOAA NCEI / World Ocean Database (WOD)',
                'url': 'https://www.ncei.noaa.gov/products/world-ocean-database',
                'date': '2026-04-18',
            },
            {
                'title': '3. IOC海洋数据与信息系统战略计划（ODIS）：IOC推进联合国海洋数据治理体系升级',
                'badge': '[政策]',
                'abstract': (
                    'UNESCO IODE发布IOC海洋数据与信息系统战略计划文件（UNESCO文档号385113，3天前被引），详细阐述IOC/IODE ODIS系统（Ocean Data and Information System）的战略实施路径，包括全球海洋数据发现能力升级、国家海洋数据中心能力建设、标准化元数据体系推广和跨机构数据协议协同，支持联合国海洋十年"数据共享"旗舰项目目标，是指导全球海洋数据中心建设与治理的核心政策框架文件。'
                ),
                'source': 'IOC-UNESCO / IODE / ODIS',
                'url': 'https://unesdoc.unesco.org/ark:/48223/pf0000385113',
                'date': '2026-04-16',
            },
        ],
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '1. xarray 文档（2026-04-13发布）：v2026.04.0 维护稳定——海洋数据处理工具链近期持续活跃',
                'badge': '[工具]',
                'abstract': (
                    'xarray官方文档站（2026-04-13，6天前更新）显示v2026.04.0稳定运行，本版本已完成zarr v3迁移、timedelta弃用迁移及新索引API引入，对海洋气候领域使用zarr后端存储的大规模数据处理流水线影响显著。结合PyPI同步更新，xarray持续作为海洋科学NetCDF/zarr多维数组处理的首选Python工具，argopy、climpred、OceanSpy等下游海洋包均依赖xarray核心接口，建议用户保持最新版本以获得最佳兼容性。'
                ),
                'source': 'xarray / PyData / PyPI',
                'url': 'https://docs.xarray.dev/en/stable/',
                'date': '2026-04-13',
            },
            {
                'title': '2. argopy v0.1.x（PyPI，2026-01-05更新）：Python Argo数据访问工具库——支持多数据源与QC标志筛选',
                'badge': '[工具]',
                'abstract': (
                    'argopy是Euro-Argo ERIC官方维护的Python库，专为海洋学家提供对Argo浮标数据的标准化访问接口，支持erddap、ftp、local、argovis等多种数据源，提供标准/专家用户两种模式，支持按QC标志、数据模式自动筛选，提供轨迹可视化、地形叠加、直方图分析等功能，PyPI版本（2026-01-05更新）已适配最新Argo GDAC数据格式变更，CSDN技术博文（2026-03-01）详细介绍了BGC-Argo数据自动化下载与分析实战流程。'
                ),
                'source': 'Euro-Argo ERIC / argopy / PyPI',
                'url': 'https://github.com/euroargodev/argopy',
                'date': '2026-01-05',
            },
            {
                'title': '3. OceanPython.org（2026-04-15更新）：海洋与海洋科学Python代码学习与分享社区持续活跃',
                'badge': '[工具]',
                'abstract': (
                    'OceanPython.org（4天前更新，2026-04-15）是专注于海洋与海洋科学Python应用的学习与代码共享社区，涵盖海洋数据获取、处理、分析与可视化的实用代码示例，近期更新了针对xarray v2026.04.0和cartopy最新版本的教程内容，并新增了argopy BGC-Argo数据处理案例，是海洋Python用户学习新工具、共享实战代码的活跃社区平台。'
                ),
                'source': 'OceanPython.org / Python海洋科学社区',
                'url': 'https://oceanpython.org/',
                'date': '2026-04-15',
            },
            {
                'title': '4. GitHub Jesse Cusack/ocean_data_tools：海洋数据工具汇总——覆盖主流编程语言与数据格式',
                'badge': '[工具]',
                'abstract': (
                    'GitHub仓库ocean_data_tools（Jesse Cusack维护）是海洋数据处理软件的综合索引，汇集了用于读取、处理和分析Argo、WOD、CMEMS、Glider、ADCP等多源海洋数据的开源软件包，覆盖Python、MATLAB、R、Julia等主流语言，按功能分类（数据获取、QC、可视化、模型输入输出等），是快速找到海洋数据处理工具的高效入口，适合任何正在构建海洋数据分析工作流的研究者参考使用。'
                ),
                'source': 'GitHub / Jesse Cusack / ocean_data_tools',
                'url': 'https://github.com/jessecusack/ocean_data_tools',
                'date': '2026-04-16',
            },
        ],
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
