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
                'title': '1. arXiv（2026-04-20）：次季节海洋-大气预报概率偏差校正——AI与动力学模型融合新方法',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2026-04-20，2604.16238）发表由12位作者合作（Hannah Guan等，包括Judah Cohen）提出的概率偏差校正方法，专门用于改进AI模型和动力学模型在次季节（subseasonal）尺度上的气候-海洋预报能力，通过校正AI预报的系统性偏差并量化不确定性，在S2S预报基准测试中显著优于未校正基准，是将机器学习引入业务化次季节海洋-大气预报的前沿进展，对提升中期海洋环境预报精度具有直接应用价值。'
                ),
                'source': 'arXiv / cs.LG / physics.ao-ph',
                'url': 'https://arxiv.org/abs/2604.16238',
                'date': '2026-04-20',
            },
            {
                'title': '2. arXiv（2026-04-16）：Monthly Diffusion v0.9——首个AI月度气候预测潜在扩散模型（AI-MIP基准）',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2026-04-16，2604.13481）发表Monthly Diffusion v0.9论文，由Kyle Hall和Maria Molina提出用于月度气候预测的潜在扩散模型（Latent Diffusion Model），明确服务于首次AI模型比较计划（AI-MIP），系统评估AI气候模型在月度时间尺度上的预报性能，为AI海洋-大气模型标准化比较提供了基准框架。该工作标志着AI气候模型比较从年际/季节向月度精细化方向延伸，海洋热容量和热带变率预测是其核心评估指标。'
                ),
                'source': 'arXiv / cs.LG / cs.AI / physics.ao-ph',
                'url': 'https://arxiv.org/abs/2604.13481',
                'date': '2026-04-16',
            },
            {
                'title': '3. arXiv（2026-04-14）：EMIT高光谱+深度学习——全球海洋/大气甲烷点源实时监测新范式',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2026-04-14，2604.10094）发表由Vishal Batchu、Anna Michalak等8位作者合作的长文（43页），利用NASA EMIT卫星的高光谱辐射测量数据，结合深度学习目标检测方法，实现全球甲烷点源的大规模自动监测。研究建立了覆盖全球海洋及陆地的甲烷排放热点自动识别流水线，展示了高光谱+AI在海洋环境污染监测领域的巨大应用潜力，代码已开源，是遥感AI应用于全球海洋环境监测的代表性新进展。'
                ),
                'source': 'arXiv / cs.CV / cs.LG / NASA EMIT / Stanford',
                'url': 'https://arxiv.org/abs/2604.10094',
                'date': '2026-04-14',
            },
            {
                'title': '4. arXiv（2026-04-14）：大西洋表层洋流体制转变——揭示AMOC经向翻转环流的阶梯式衰退',
                'badge': '[重磅预印本]',
                'abstract': (
                    'arXiv（2026-04-14，physics.ao-ph）发表重要预印本，分析大西洋表层洋流的体制转变（regime shift），通过综合多源卫星观测和现场数据，揭示了大西洋经向翻转环流（AMOC）呈现阶梯式衰退（stepwise decline）的新证据，打破了AMOC连续线性减弱的传统认识。研究采用机器学习时序分析方法识别突变点，成果对深入理解气候临界点（tipping point）和海洋热量输运变化具有重要科学意义，是当前物理海洋与AI方法融合的前沿成果。'
                ),
                'source': 'arXiv / physics.ao-ph / AMOC oceanography',
                'url': 'https://arxiv.org/list/physics.ao-ph/recent',
                'date': '2026-04-14',
            },
        ],
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. arXiv（2026-04月）：ILIAD项目——海洋信息模型OIM语义协调Python框架（arXiv 2604.13042）',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2604.13042，2026年4月公布，提交于2026-02-27）发表ILIAD（欧洲海洋数字孪生项目）的核心成果，由Nystad和Martin-Recuerda提出基于Python函数式方法的语义数据协调框架，核心服务于Ocean Information Model（OIM）——一套支持互操作海洋数字孪生（DTO）的模块化本体。该方法降低了数据科学家使用RML/OTTR等语义Web技术的门槛，在ILIAD水产养殖试点中完成验证，是欧洲各DTO系统实现数据互操作的关键技术工具，已接近发布。'
                ),
                'source': 'arXiv / cs.DB / ILIAD / OIM / DTO',
                'url': 'https://arxiv.org/abs/2604.13042',
                'date': '2026-04-17',
            },
            {
                'title': '2. Copernicus Marine（2026-04-09）：海洋数据助力海事空间规划——布鲁塞尔研讨会成果汇报',
                'badge': '[进展]',
                'abstract': (
                    'Copernicus Marine Service官网（2026-04-09）发布"Marine Data for Maritime Spatial Planning: Key Outcomes"报告，介绍2026年3月31日在布鲁塞尔召开的60人研讨会主要成果，展示CMEMS海洋数字孪生数据如何直接支撑欧洲海事空间规划（Marine Spatial Planning，MSP）政策制定，涵盖风电场选址、海洋保护区评估和港口规划等典型应用场景，是DTO数据服务政策应用的重要实践案例。'
                ),
                'source': 'Copernicus Marine Service / Mercator Ocean / MSP',
                'url': 'https://marine.copernicus.eu/news/marine-data-maritime-spatial-planning-key-outcomes-copernicus-marine-service-workshop',
                'date': '2026-04-09',
            },
            {
                'title': '3. Copernicus Marine（2026-03-12）：NECCTON海洋生态系统观测器——新一代海洋生态数字孪生探索工具',
                'badge': '[新工具]',
                'abstract': (
                    'Copernicus Marine Service官网（2026-03-12）宣布上线NECCTON（Next-Generation Ecosystem Services for the Coastal and Open Ocean）海洋观测器，这是由欧洲多机构联合开发的海洋生态系统数字孪生探索工具，开放了下一代生态系统模型的数据访问接口，支持浮游植物、鱼类和海洋食物网等生态系统变量的在线查询和可视化，是Copernicus Marine生态系统数字孪生服务体系的最新扩展，对海洋生物多样性监测和蓝色经济评估具有重要价值。'
                ),
                'source': 'Copernicus Marine Service / NECCTON / 欧洲海洋生态DTO',
                'url': 'https://marine.copernicus.eu/news/neccton-ocean-observatory-new-tool-explore-ocean-ecosystems',
                'date': '2026-03-12',
            },
        ],
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Data Visualization',
        'items': [
            {
                'title': '1. EMODnet（欧洲海洋观测与数据网络）：在线综合海洋数据地图——多主题、多尺度交互地图服务',
                'badge': '[平台]',
                'abstract': (
                    'EMODnet（European Marine Observation and Data Network）提供覆盖欧洲及全球海域的多主题在线交互地图可视化服务，涵盖海底地形、海洋物理、化学、生物、地质和人类活动等七大主题数据，所有数据通过统一Web地图接口（WMS/WFS）向全球用户开放，支持按时间、空间和参数自定义查询，并可下载GIS格式数据。EMODnet是欧洲海洋数据基础设施的核心前端，为海洋政策制定、科学研究和蓝色经济提供直观的多尺度可视化数据入口，持续扩充新数据集和功能更新。'
                ),
                'source': 'EMODnet / European Marine Observation and Data Network / 欧盟',
                'url': 'https://emodnet.ec.europa.eu/en',
                'date': '2026-04-21',
            },
            {
                'title': '2. Ferret（NOAA/PMEL）：海洋气候数据分析与可视化经典工具——持续维护中',
                'badge': '[工具]',
                'abstract': (
                    'Ferret是由NOAA太平洋海洋环境实验室（PMEL）开发和长期维护的海洋气候数据分析与可视化环境，专为处理大型网格化海洋和大气数据集（NetCDF/HDF格式）设计，支持交互式命令行分析、批处理脚本和图形输出，内置丰富的海洋物理量计算函数（如热通量、流线积分、混合层深度），被全球数千名海洋气候研究者持续使用。虽然Ferret以传统命令行方式运行，但其处理大规模4D海洋模型输出的能力无可替代，至今仍是遗留模型数据集分析的首选工具之一。'
                ),
                'source': 'NOAA PMEL / Ferret / 海洋数据分析',
                'url': 'https://ferret.pmel.noaa.gov/Ferret/',
                'date': '2026-04-21',
            },
            {
                'title': '3. SEANOE（海洋与环境科学开放数据平台）：可视化支持数据集在线预览——Ifremer主导',
                'badge': '[平台]',
                'abstract': (
                    'SEANOE（Sea scientific Open data Publication）是Ifremer（法国海洋开发研究院）主导的海洋数据开放发布平台，专注于海洋与环境科学数据集的DOI注册、在线可视化预览和开放下载，支持NetCDF、CSV、HDF5等多种格式，提供基于地图和时序图的数据集在线预览功能，帮助用户在下载前评估数据质量和覆盖范围。SEANOE与PANGAEA共同构成欧洲海洋科学数据开放出版的双核心平台，持续接收全球海洋科研团队的数据集提交申请。'
                ),
                'source': 'SEANOE / Ifremer / 法国海洋开发研究院',
                'url': 'https://www.seanoe.org/',
                'date': '2026-04-21',
            },
        ],
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. arXiv（2026-04-16）：SWOT卫星沿轨观测的二维滤波方法——消除白噪声谱伪影的新技术',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2026-04-16，physics.ao-ph）发表SWOT（Surface Water and Ocean Topography）卫星沿轨观测数据质量处理新研究，提出针对SWOT二维宽刈幅高度计数据的噪声滤波改进方案，系统分析二维空间滤波对白噪声谱的影响，解决了直接应用一维滤波方法时引入的谱伪影问题，为SWOT宽刈幅数据的科学分析（次中尺度动力学、河湖水位变化）提供了更可靠的数据预处理规程，成果直接服务于SWOT科学数据质量提升工作。'
                ),
                'source': 'arXiv / physics.ao-ph / SWOT / 海面高度计',
                'url': 'https://arxiv.org/list/physics.ao-ph/recent',
                'date': '2026-04-16',
            },
            {
                'title': '2. Euro-Argo ERIC：Argo实时质控（RTQC）和延时模式质控（DMQC）文档体系——全球海洋QC标准参考',
                'badge': '[标准]',
                'abstract': (
                    'Euro-Argo ERIC（欧洲Argo区域数据中心联合体）维护Argo实时质控（RTQC）和延时模式质控（DMQC）的完整文档体系，包括《Argo数据管理手册》、各参数QC手册（温度、盐度、BGC参数专项手册）及最新版本更新记录，为全球54个国家Argo数据中心（DAC）提供统一的质控规程和代码标志体系，确保全球Argo数据的一致性和可比性，是海洋现场观测数据质量标准体系的国际参考标准，近期BGC-Argo手册已更新至新版本。'
                ),
                'source': 'Euro-Argo ERIC / Argo DMQC / 海洋QC标准',
                'url': 'https://www.euro-argo.eu/Data-Argo/DMQC',
                'date': '2026-04-21',
            },
            {
                'title': '3. OceanBestPractices System（IOC-UNESCO）：海洋观测最佳实践文档库——QC方法规程全球发现平台',
                'badge': '[平台]',
                'abstract': (
                    'OceanBestPractices System（oceanbestpractices.org，IOC-UNESCO主导）是全球最系统的海洋观测最佳实践（BP）文档检索与发现平台，收录来自Argo、CTD、声学多普勒流速仪（ADCP）、生物地球化学传感器等多类观测系统的QC方法规程、传感器标定手册和数据处理流程文档，支持全文检索和语义相似性搜索，为全球海洋科研机构提供标准化QC规程参考，是联合国海洋十年数据共享目标的核心文档基础设施，持续接收新文档提交。'
                ),
                'source': 'OceanBestPractices / IOC-UNESCO / 海洋观测QC规程',
                'url': 'https://oceanbestpractices.org/',
                'date': '2026-04-21',
            },
        ],
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '1. arXiv（2026-04-17）：Generic-PCM行星气候动力板海洋模型——GMD接收，快速物理海洋数据处理框架',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv（2026-04-17，physics.ao-ph）发表已被Geoscientific Model Development（GMD）接收的Generic-PCM快速物理海洋模型论文，提出轻量级动力板海洋（slab ocean）模型，专为行星气候模拟（包括地球及系外行星场景）设计，可以极低计算成本耦合到大气环流模型，加速海洋-大气热平衡计算。该模型已开源发布，对需要快速处理大量气候情景的研究（如气候敏感性参数扫描、古气候模拟）具有重要的数据处理效率价值，代码在Github开放。'
                ),
                'source': 'arXiv / GMD / physics.ao-ph / 行星气候模型',
                'url': 'https://arxiv.org/list/physics.ao-ph/recent',
                'date': '2026-04-17',
            },
            {
                'title': '2. EGU Ocean Science 期刊（2026年4月）：Copernicus开放获取海洋数据处理方法论文持续发表',
                'badge': '[期刊]',
                'abstract': (
                    'EGU旗下Ocean Science期刊（os.copernicus.org，开放获取）是海洋数据处理与分析方法的重要发表平台，2026年4月持续发表与海洋数值模型、数据同化、卫星遥感数据处理和现场观测数据分析相关的论文，内容覆盖热带海洋数据插值、海洋边界层处理、季节性海冰模拟等典型方向。Ocean Science作为完全开放获取期刊，所有论文均经过公开互动评审，是EGU/Copernicus生态系统内海洋数据处理领域的核心期刊，读者可通过RSS订阅实时获取最新接受论文。'
                ),
                'source': 'EGU / Ocean Science / Copernicus Publications',
                'url': 'https://os.copernicus.org/articles/',
                'date': '2026-04-21',
            },
            {
                'title': '3. gsw-python（TEOS-10）：国际海洋状态方程Python库——海水热力学处理的国际标准工具',
                'badge': '[工具]',
                'abstract': (
                    'gsw-python（GitHub: TEOS-10/GSW-Python）是国际海洋学委员会（IAPSO）认定的海水热力学方程TEOS-10的官方Python实现，提供计算绝对盐度（SA）、保守温度（CT）、位密度、热容量、声速等几十个关键海洋热力学量的标准函数，是海洋CTD数据处理和海洋数值模型诊断的必备工具。gsw-python被argopy、Ocean-Data-View、CMEMS数据处理流水线等广泛调用，定期更新发布新版本，遵循TEOS-10国际标准的最新修订，代码在PyPI和conda-forge同步维护。'
                ),
                'source': 'TEOS-10 / gsw-python / IAPSO / PyPI',
                'url': 'https://github.com/TEOS-10/GSW-Python',
                'date': '2026-04-21',
            },
        ],
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. IOC-UNESCO IODE OceanTeacher全球学院（OTGA）：海洋数据管理专业培训体系持续开放',
                'badge': '[进展]',
                'abstract': (
                    'IOC-UNESCO IODE运营的OceanTeacher Global Academy（OTGA，oceanteacher.org）是全球最系统的海洋数据管理专业培训平台，提供海洋数据格式标准（NetCDF/CF Conventions）、元数据编写（ISO 19115/Dublin Core）、数据质量控制、开放数据政策（Creative Commons）和ODIS平台操作等在线/面授课程，2026年多期培训课程正在进行中（含非洲、亚洲区域课程），所有完成课程的学员可获得IODE认证证书，是提升全球海洋数据管理能力建设的核心教育资源。'
                ),
                'source': 'IOC-UNESCO / IODE / OceanTeacher / OTGA',
                'url': 'https://oceanteacher.org/',
                'date': '2026-04-21',
            },
            {
                'title': '2. SeaDataNet（欧洲海洋数据管理基础设施）：分布式海洋数据发现与访问系统——CDI目录持续扩充',
                'badge': '[平台]',
                'abstract': (
                    'SeaDataNet（seadatanet.org）是由欧洲35个国家55个数据中心参与的海洋数据管理分布式基础设施，核心服务包括CDI（Common Data Index，公共数据索引）目录检索、SDN-DISCO元数据聚合、格式标准（ODV格式、SeaDataNet NetCDF Profile）维护和MIKADO元数据编辑器提供，支持全球科研人员在线检索欧洲各国海洋历史数据并申请下载，是欧洲海洋FAIR数据管理实践的代表性基础设施，其推进的数据最佳实践（BP）也被IOC-UNESCO所采纳。'
                ),
                'source': 'SeaDataNet / 欧洲海洋数据管理 / CDI',
                'url': 'https://www.seadatanet.org/',
                'date': '2026-04-21',
            },
            {
                'title': '3. SEANOE + Ifremer SISMER（2026年活跃）：法国海洋数据双轨发布体系——科学数据出版与历史档案并重',
                'badge': '[平台]',
                'abstract': (
                    'Ifremer运营的SISMER（法国海洋数据科学信息系统）和SEANOE开放数据平台构成法国海洋数据管理双轨体系：SISMER负责Ifremer历史观测数据（温盐剖面、底栖生物、渔业资源等）的专业存档与数据服务；SEANOE则向全球科研团队开放数据集DOI出版服务。两个平台均接入SeaDataNet/PANGAEA/EMODnet数据生态，是欧洲海洋数据分布式管理网络的重要节点，近期持续新增法国历次综合海洋调查数据集，数据可通过标准接口免费下载。'
                ),
                'source': 'Ifremer / SISMER / SEANOE / SeaDataNet',
                'url': 'https://www.ifremer.fr/fr/donnees-marines',
                'date': '2026-04-21',
            },
        ],
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. ICES（国际海洋考察理事会）2026工作组航次：欧洲渔业与海洋生态综合调查协调',
                'badge': '[进展]',
                'abstract': (
                    'ICES（International Council for the Exploration of the Sea，国际海洋考察理事会）每年协调成员国开展多项联合渔业和海洋生态综合调查航次，2026年度ICES各工作组（如WGACEGG、WGBIFS等）已完成航次计划部署，科考数据须按ICES数据格式（DATRAS）提交并公开共享，成员国可通过ICES数据库检索历次底栖拖网和海洋学调查数据，是促进北大西洋和北冰洋海域开放航次协作的重要区域机构。'
                ),
                'source': 'ICES / 国际海洋考察理事会 / 欧洲渔业海洋调查',
                'url': 'https://www.ices.dk/community/groups/Pages/Symposia.aspx',
                'date': '2026-04-21',
            },
            {
                'title': '2. GOOS（全球海洋观测系统）：开放航次观测数据FAIR共享政策框架——推进全球航次数据开放',
                'badge': '[政策]',
                'abstract': (
                    'GOOS（Global Ocean Observing System，全球海洋观测系统）联合IOC-UNESCO、WMO等机构持续推进开放航次观测数据的FAIR共享政策框架，要求受公共资金支持的海洋考察航次在规定时限内向全球开放发布数据，并须附上DOI和标准格式元数据。GOOS数据基础设施指导方针（GDI）已被多个国家海洋科研基金管理机构采纳为数据共享附加条件，对推动我国共享航次制度国际接轨具有直接参考价值。'
                ),
                'source': 'GOOS / IOC-UNESCO / WMO / 开放航次数据政策',
                'url': 'https://www.goosocean.org/',
                'date': '2026-04-21',
            },
            {
                'title': '3. AWI极地科考船FS Polarstern 2026：南北极航次持续开展——数据通过PANGAEA全面开放共享',
                'badge': '[进展]',
                'abstract': (
                    '德国亥姆霍兹极地研究中心Alfred Wegener Institute（AWI）科考船FS Polarstern是欧洲最大极地综合科考船，执行南北极全年科学考察任务，所有航次数据须提交PANGAEA数据系统开放共享。AWI官网（活跃）发布2026年FS Polarstern航次计划，包括北冰洋冰层动力学、生态系统和深海底栖生物调查，数据涵盖CTD剖面、水下机器人影像、大气和冰层观测，是全球开放极地航次数据的重要来源，MOSAiC后续研究的数据集仍在持续发布。'
                ),
                'source': 'AWI / FS Polarstern / PANGAEA / 极地开放航次',
                'url': 'https://www.awi.de/expedition/ships/polarstern.html',
                'date': '2026-04-21',
            },
        ],
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '1. EMODnet数字海底（2026年活跃）：欧洲海洋观测数据网络——整合11个数据主题构建联合数据生态',
                'badge': '[平台]',
                'abstract': (
                    'EMODnet（European Marine Observation and Data Network）是欧盟资助的欧洲海洋数据整合基础设施，涵盖地形与测深、海洋物理、化学、生物、地质、人类活动和海底地形7个专题数据门户，整合了来自欧洲30余个国家百余个机构的原始海洋观测数据，通过统一门户（emodnet.ec.europa.eu）提供完全开放的数据检索、在线地图可视化和API批量下载服务，是欧洲海洋数据中心体系的核心整合平台，2026年持续扩充北冰洋和地中海数据集，并强化与CMEMS和SeaDataNet的互操作能力。'
                ),
                'source': 'EMODnet / 欧盟 / 欧洲海洋数据网络',
                'url': 'https://emodnet.ec.europa.eu/en',
                'date': '2026-04-21',
            },
            {
                'title': '2. Euro-Argo ERIC（2026年活跃）：欧洲Argo区域数据中心——提供Argo数据质控工具和技术支持',
                'badge': '[进展]',
                'abstract': (
                    'Euro-Argo ERIC（European Research Infrastructure Consortium，2026年持续活跃）是欧洲20个国家Argo数据中心和用户服务的统一协调机构，负责欧洲贡献的Argo浮标数据质控（RTQC+DMQC）、数据格式审核和GDAC提交，向科研社区提供argopy、ArgoOnline等数据工具的技术支持文档，并定期开展Argo QC培训研讨会。Euro-Argo近期持续强化BGC-Argo数据的DMQC能力，并推进与CMEMS数据仓的深度集成，是欧洲Argo数据服务的权威数据中心联合体。'
                ),
                'source': 'Euro-Argo ERIC / Argo GDAC / 欧洲Argo',
                'url': 'https://www.euro-argo.eu/',
                'date': '2026-04-21',
            },
            {
                'title': '3. SeaDataNet CDIAC（碳数据信息分析中心）镜像：全球海洋碳观测数据集成与质控数据服务',
                'badge': '[平台]',
                'abstract': (
                    '海洋碳观测数据的集成与开放分发是近年海洋数据中心能力建设的核心方向之一，NOAA NCEI、SeaDataNet和SOCAT（Surface Ocean CO2 Atlas）等机构联合维护的全球海洋碳数据中心体系，将海洋表层pCO2、总碳、碱度等变量的历史和实时观测数据标准化集成，提供全球海洋碳通量计算的关键数据支撑，SOCAT数据集（当前版本 v2024）通过Web门户和API免费开放，是气候变化研究和碳中和政策评估的核心基础数据，ICOS和GO-SHIP联合强化了欧洲和全球碳观测网络建设。'
                ),
                'source': 'SOCAT / NOAA NCEI / SeaDataNet / 全球海洋碳数据',
                'url': 'https://www.socat.info/',
                'date': '2026-04-21',
            },
        ],
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '1. erddapy（Python ERDDAP客户端）：通过Python访问全球ERDDAP数据服务器的标准接口库',
                'badge': '[工具]',
                'abstract': (
                    'erddapy（GitHub: ioos/erddapy）是IOOS（美国综合海洋观测系统）维护的Python库，提供简洁的API接口用于访问全球任意ERDDAP数据服务器（包括NOAA CoastWatch、Copernicus Marine、Euro-Argo等超过100个ERDDAP实例），支持按时间、空间和变量构造查询URL，返回xarray/pandas格式数据，是Python海洋数据工作流中访问ERDDAP数据的最推荐方式，被OceanPy、IOOS生态系统和多个海洋数值预报后处理工具广泛调用，活跃维护中。'
                ),
                'source': 'IOOS / erddapy / GitHub / ERDDAP',
                'url': 'https://github.com/ioos/erddapy',
                'date': '2026-04-21',
            },
            {
                'title': '2. cmocean（海洋学专用色图库）：感知均匀的海洋数据可视化色标——matplotlib/cartopy标准配套',
                'badge': '[工具]',
                'abstract': (
                    'cmocean（PyPI: cmocean）是专为海洋科学数据可视化设计的感知均匀色图库，收录temperature、salinity、oxygen、speed、chl、deep等20余套针对具体海洋变量优化的色图方案，符合色觉障碍友好、感知均匀和科学直觉一致的设计原则，被cartopy、hvplot、ODV、Ferret等众多可视化工具作为内置色图方案。cmocean在PyPI和conda-forge均有发布，是海洋数据可视化标准化的推荐工具，当前版本稳定维护中。'
                ),
                'source': 'cmocean / PyPI / matplotlib / 海洋可视化色图',
                'url': 'https://matplotlib.org/cmocean/',
                'date': '2026-04-21',
            },
            {
                'title': '3. intake-esm（Pangeo生态系统）：CMIP/CESM等大规模模型数据的Python目录驱动访问工具',
                'badge': '[工具]',
                'abstract': (
                    'intake-esm（GitHub: intake/intake-esm）是Pangeo生态系统中用于管理和访问大规模地球系统模型（ESM）数据集的Python目录驱动工具，支持CMIP5/6、CESM、FGOALS等多种模型输出的统一检索和按需加载，底层通过intake和fsspec实现云存储（S3/GCS）和本地文件的透明访问，与xarray/Dask无缝集成，是Pangeo海洋气候大数据处理流水线的核心组件，被多个欧美气候数据中心用于大规模海洋模型数据分发。'
                ),
                'source': 'Pangeo / intake-esm / GitHub / CMIP数据访问',
                'url': 'https://github.com/intake/intake-esm',
                'date': '2026-04-21',
            },
            {
                'title': '4. Pangeo社区（2026年活跃）：大规模海洋气候数据分析开源生态系统——定期在线研讨会与代码示例',
                'badge': '[社区]',
                'abstract': (
                    'Pangeo（pangeo.io）是专注于大规模地球科学（包括海洋）数据分析的开源社区，构建了以xarray+Dask+Jupyter+Zarr为核心的云原生海洋数据处理生态，定期举办双周在线研讨会（Pangeo Showcase）分享最新工具和海洋数据实战案例，并在GitHub维护丰富的海洋数据分析示例笔记本（pangeo-gallery），2026年社区持续活跃，近期新增对新版Zarr v3的云存储优化支持，是海洋大数据处理的最重要开源技术社区之一。'
                ),
                'source': 'Pangeo / pangeo.io / xarray / Dask / 海洋大数据',
                'url': 'https://pangeo.io/',
                'date': '2026-04-21',
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
