#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新feishu_write_doc.py的SECTIONS为2026-04-16内容"""

NEW_SECTIONS = '''SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. OceanPredict AI-TT研讨会（4月13-14日，蒙特利尔）圆满落幕——机器学习海洋预测最新进展汇聚',
                'badge': '[重磅活动]',
                'abstract': (
                    'OceanPredict AI Task Team研讨会"机器学习海洋预测：方法、应用与挑战"于2026年4月13-14日在加拿大蒙特利尔大学成功举办，由NOAA Santha Akella与ECMWF Rachel Furner联合主持，30个口头报告涵盖ML仿真器、物理-AI混合方法、深度学习数据同化、降尺度应用与业务化评估挑战等六大主题，Mercator Ocean等机构同步报道。研讨会成果将推动AI方法在全球业务化海洋预测中的标准化应用。'
                ),
                'source': 'OceanPredict / NOAA / ECMWF / Mercator Ocean',
                'date': '2026-04-14',
                'url': 'https://oceanpredict.org/events/ai-tt-workshop/'
            },
            {
                'title': '2. arXiv: FuXi-ONS——首个机器学习全球海洋集合预报系统，预报期达365天',
                'badge': '[预印本]',
                'abstract': (
                    'arXiv:2603.19591（2026-03-20，复旦大学等团队）介绍FuXi-ONS，全球首个数据驱动海洋集合预报系统，基于1°分辨率全球网格提供海表温度、盐度、海平面异常和海流5天至365天集合预报，通过随机条件模拟实现概率化不确定性量化，相较确定性AI预报显著提升极端事件预警能力，为气候预测和海洋服务提供新范式。'
                ),
                'source': 'arXiv / 复旦大学',
                'date': '2026-03-23',
                'url': 'https://arxiv.org/abs/2603.19591'
            },
            {
                'title': '3. Springer Marine Systems综述：深度学习在海洋视觉系统目标检测与图像增强中的最新进展',
                'badge': '[综述]',
                'abstract': (
                    'Springer Marine Systems & Ocean Technology（2026-04-14，DOI: 10.1007/s40868-026-00223-1）发表综述，回顾2015-2025年70篇论文，全面分析CNN、Transformer与混合方法在水下目标检测（生物多样性监测、管道巡检、AUV导航）和图像增强的应用。发现单阶段检测器在实时性上优于其他架构，但跨域泛化仍是主要挑战，提出混合Transformer模型、自监督学习和边缘部署为关键未来方向。'
                ),
                'source': 'Springer / Marine Systems & Ocean Technology',
                'date': '2026-04-14',
                'url': 'https://link.springer.com/article/10.1007/s40868-026-00223-1'
            },
            {
                'title': '4. Springer Ocean Dynamics: ATT-LSTM近岸有效波高深度学习降尺度预报新方法',
                'badge': '[论文]',
                'abstract': (
                    'Springer Ocean Dynamics（2026-04-14在线，DOI: 10.1007/s10236-026-01804-9）发表基于注意力长短时记忆网络（ATT-LSTM）的统计降尺度方法，从粗分辨率全球波浪场生成近岸高分辨率有效波高预报，相较直接深度学习和传统统计方法显著提升近岸波高预报精度，为沿海工程与导航提供轻量高效替代方案。'
                ),
                'source': 'Springer / Ocean Dynamics',
                'date': '2026-04-14',
                'url': 'https://link.springer.com/article/10.1007/s10236-026-01804-9'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / DTO',
        'items': [
            {
                'title': '1. DITTO Summit 2026确认——11月11-13日横滨，聚焦"连接技术与治理"核心议题',
                'badge': '[峰会预告]',
                'abstract': (
                    'UN海洋十年DITTO（数字孪生海洋）官方网站本周更新，确认DITTO Summit 2026将于11月11-13日在日本横滨湾举办，JAMSTEC协办。五大工作组（可持续观测网络、综合数字孪生模型、互操作性架构、社区接口、能力建设）持续推进，SEAtwins（社会生态集成）、AtlanticSENSE（多危害信息系统）等附属项目正式发布。峰会征集海洋数字孪生最佳实践案例，是2026年最重要的DTO年度活动。'
                ),
                'source': 'DITTO / JAMSTEC / UN Ocean Decade',
                'date': '2026-04-15',
                'url': 'https://ditto-oceandecade.org/'
            },
            {
                'title': '2. Biogeosciences: 混合机器学习数据同化改善海洋生物地球化学预测',
                'badge': '[论文]',
                'abstract': (
                    'Biogeosciences（EGU，bg-23-315-2026，2026年发表）研究展示ML如何通过学习观测变量与未观测变量之间统计关系改善海洋生物地球化学数据同化，构建物理模型+ML的混合DA框架，以叶绿素同化为例显著提升海洋初级生产力和营养盐剖面的模拟精度，为建设更精确的海洋生物地球化学数字孪生提供关键方法支撑。'
                ),
                'source': 'EGU / Biogeosciences',
                'date': '2026-04-10',
                'url': 'https://bg.copernicus.org/articles/23/315/2026/bg-23-315-2026.html'
            },
            {
                'title': '3. INESC TEC推进欧洲海洋数字孪生EDITO互操作性——从布鲁塞尔到格拉斯哥',
                'badge': '[项目动态]',
                'abstract': (
                    'INESC TEC（2026-04-10）发布进展报告，汇报在EDITO数字孪生峰会（布鲁塞尔）和格拉斯哥两大活动中推进欧洲数字孪生海洋（DTO）互操作性工作，重点推动模型、服务、流程和数据跨平台无缝迁移能力建设，为欧洲DTO基础设施标准化提供关键技术支撑，有效推进Destination Earth海洋分量落地。'
                ),
                'source': 'INESC TEC / EDITO',
                'date': '2026-04-10',
                'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Dashboard',
        'items': [
            {
                'title': '1. NECCTON Ocean Viewer正式上线——下一代海洋生态系统交互可视化平台开放获取',
                'badge': '[新工具]',
                'abstract': (
                    'Copernicus Marine Service（2026-03-12）宣布NECCTON Ocean Viewer正式发布，基于Copernicus Viewer框架构建，支持AI增强海洋生态系统模型数据的交互探索，涵盖低营养级浮游生物、高营养级鱼类、底栖生境及汞/微塑料污染等变量，面向研究人员、政策制定者和渔业管理者开放，强化CMEMS"绿海"生态系统服务能力，是欧盟Horizon Europe NECCTON项目核心成果。'
                ),
                'source': 'Copernicus Marine Service / NECCTON / EU Horizon Europe',
                'date': '2026-03-12',
                'url': 'https://marine.copernicus.eu/news/new-neccton-ocean-viewer-opens-access-next-generation-marine-ecosystem-data'
            },
            {
                'title': '2. Ocean Virtual Laboratory（OVL）卫星+现场+模型多源融合交互可视化平台持续更新',
                'badge': '[平台动态]',
                'abstract': (
                    'OceanDataLab的Ocean Virtual Laboratory（ovl.oceandatalab.com，本周更新）提供Sentinel系列、Jason高度计、SST产品与Argo浮标数据的多源融合交互可视化，支持时间序列动画与剖面展示，基于开源Syntool框架（GNU AGPL授权），是海洋遥感和模型数据联合探索的重要免费平台，近期新增多卫星融合显示模式。'
                ),
                'source': 'OceanDataLab / ESA',
                'date': '2026-04-10',
                'url': 'https://ovl.oceandatalab.com/'
            },
            {
                'title': '3. CMEMS可视化工具矩阵更新——MyOcean Viewer与OceanMaps持续升级',
                'badge': '[服务更新]',
                'abstract': (
                    'Copernicus Marine Service（marine.copernicus.eu/access-data/ocean-visualisation-tools，2026-04-13）更新可视化工具矩阵，MyOcean Viewer支持全球15+变量的近实时与预报场地图展示，OceanMaps为运营用户提供专业Met-Ocean可视化分析，NECCTON Ocean Viewer专攻生态系统变量，三大工具覆盖不同用户群体需求，均免费开放。'
                ),
                'source': 'Copernicus Marine Service / CMEMS',
                'date': '2026-04-13',
                'url': 'https://marine.copernicus.eu/access-data/ocean-visualisation-tools'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '1. Euro-Argo ERIC报道第二届BGC-Argo DMQC研讨会——60位专家能力建设',
                'badge': '[重要活动]',
                'abstract': (
                    'Euro-Argo ERIC（2026-04-08报道）回顾2026年1月26-30日在法国滨海自由城IMEV举办的第二届BGC-Argo延时模式质量控制（DMQC）研讨会，约60名欧美亚专家参加，历时五天分别聚焦光学（辐射/叶绿素a）、溶解氧、硝酸盐/pH值传感器质控，并介绍基于Python等灵活编程语言的新一代QC工具，填补BGC-Argo全球数据质量能力缺口，Euro-Argo ONE项目支持。'
                ),
                'source': 'Euro-Argo ERIC / BGC-Argo / CNRS / Sorbonne',
                'date': '2026-04-08',
                'url': 'https://www.euro-argo.eu/News-Meetings/News/News-archives/2026/2nd-BGC-Argo-DMQC-workshop-2026'
            },
            {
                'title': '2. IOOS QARTOD实时质控旗标手册持续更新——ioos_qc Python库支撑标准化实施',
                'badge': '[标准更新]',
                'abstract': (
                    'NOAA IOOS QARTOD官方页面（2026-04-09更新）《实时海洋数据质量控制旗帜手册》持续修订，规范温盐、海流、波浪等实时观测数据的QC旗标体系，配套ioos_qc开源Python库（GitHub: ioos/ioos_qc）实现自动化质控测试，是美国区域海洋观测系统（IOOS）数据标准化的核心规范，被全球多个数据中心采纳参考。'
                ),
                'source': 'NOAA / IOOS QARTOD',
                'date': '2026-04-09',
                'url': 'https://ioos.noaa.gov/project/qartod/'
            },
            {
                'title': '3. NOAA NCEI世界海洋数据库（WOD）季度更新完成——历史剖面数据持续扩充',
                'badge': '[数据更新]',
                'abstract': (
                    'NOAA NCEI WOD Select（2026-04-09更新完成）完成最新季度数据批次入库，可通过在线检索工具获取1772年至今全球历史海洋剖面数据（温度、盐度、溶解氧、营养盐等），是全球最大公开海洋in-situ历史数据集，为海洋气候变化分析、再分析产品和数值模型验证提供权威质控数据基础。'
                ),
                'source': 'NOAA NCEI / World Ocean Database',
                'date': '2026-04-09',
                'url': 'https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Pipeline',
        'items': [
            {
                'title': '1. IEEE TGRS综述：AI在卫星海洋遥感参数反演中的系统性进展',
                'badge': '[综述]',
                'abstract': (
                    'IEEE Transactions on Geoscience and Remote Sensing（2026-02-27，DOI: 10.1109/TGRS.2026.11413853）发表AI在卫星海洋遥感中的系统综述，涵盖海洋物理/生物参数反演、数据重建与图像增强三大应用领域，重点分析卷积神经网络、图神经网络和基础模型在多传感器海洋遥感数据处理流水线中的最新进展及挑战，为构建下一代AI卫星遥感处理系统提供方向。'
                ),
                'source': 'IEEE TGRS / XPlore',
                'date': '2026-02-27',
                'url': 'https://ieeexplore.ieee.org/document/11413853'
            },
            {
                'title': '2. MDPI Drones: 异构UAV-USV集群跨域协同路径规划——多平台海洋数据采集调度新框架',
                'badge': '[论文]',
                'abstract': (
                    'MDPI Drones（2026-04-15在线，DOI: 10.3390/drones10040287）发表面向异构无人机-无人艇（UAV-USV）集群的协同跨域路径规划（CCPP）方法，基于分布式态势感知协同图与分解优化算法，实现多智能体海洋数据采集路径快速求解，为海洋无人集群多源数据处理工作流提供高效协同调度方案，降低计算资源消耗。'
                ),
                'source': 'MDPI / Drones',
                'date': '2026-04-15',
                'url': 'https://www.mdpi.com/2504-446X/10/4/287'
            },
            {
                'title': '3. ESSD: 改进的卫星海洋遥感陆地掩膜——支持沿海区域数据处理精度提升',
                'badge': '[数据论文]',
                'abstract': (
                    'Earth System Science Data（EGU/Copernicus，essd-18-231-2026，2026-01-09）发表改进的卫星海洋遥感陆地掩膜方法，基于多时相清晰大气遥感影像自动识别水面覆盖变化，有效解决沿海区域卫星海洋参数反演中的陆地污染问题，提升近岸海洋遥感数据处理质量，数据集已在PANGAEA开放获取。'
                ),
                'source': 'EGU / ESSD / Copernicus Publications',
                'date': '2026-01-09',
                'url': 'https://essd.copernicus.org/articles/18/231/2026/essd-18-231-2026.html'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing / Sample Sharing',
        'items': [
            {
                'title': '1. "海洋地质二号"完成第33航次深海科考共享任务——首套万米级超洁净采样绞车成功试验',
                'badge': '[国内动态]',
                'abstract': (
                    '2026年4月13日，自然资源部中国地质调查局广州海洋地质调查局宣布，联合16家单位、100名科学家的"海洋地质二号"第33航次历时30天圆满完成，回收海底设备41台套，完成首套万米级超洁净海水采样绞车（电缆长11000米）海试，是2026年首个国家自然科学基金规范化海试科考共享航次，创新"船时共享、多方参与、多目标协同"模式，实现一次出航完成4大类10余项科研任务。'
                ),
                'source': '中国地质调查局广州海洋地质调查局 / 光明日报',
                'date': '2026-04-13',
                'url': 'https://www.cgs.gov.cn/xwl/ddyw/202604/t20260413_853125.html'
            },
            {
                'title': '2. NSFC共享航次2026年度项目指南发布——4月27日起开放NSFC系统申请',
                'badge': '[政策]',
                'abstract': (
                    '国家自然科学基金共享航次计划2026年度项目指南（2026-03-19通过grants.nsfc.gov.cn正式发布），NSFC系统申请接收期为2026年4月27日起，NORC官网（norc.com.cn，04-13更新）同步发布规范文件与材料下载通道，多艘科考船持续开放搭载申请，是中国海洋科学开放数据采集体系的重要年度政策支撑。'
                ),
                'source': '国家自然科学基金委 / NORC',
                'date': '2026-04-13',
                'url': 'https://www.norc.com.cn/'
            },
            {
                'title': '3. GeoBlueplanet渔业工作坊（4月21-22日，伦敦）——海洋数据支撑全球可持续渔业管理',
                'badge': '[活动预告]',
                'abstract': (
                    'GeoBlueplanet将于2026年4月21-22日在伦敦NEAFC召开"海洋数据支撑全球可持续渔业"专题工作坊，汇聚ICES、FAO等代表，探讨卫星遥感、Argo观测和数值预报产品在渔业管理中的共享与应用，推动海洋环境数据与渔业资源评估数据协同共享机制建设，是本周最重要的海洋数据治理专业活动。'
                ),
                'source': 'GeoBlueplanet / NEAFC / London',
                'date': '2026-04-21',
                'url': 'https://geoblueplanet.org/wp-content/uploads/2026/03/Fisheries-Workshop-Concept-Note.pdf'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. Schmidt Ocean R/V Falkor(too)"设计未来3"航次正在进行——深海透明生物4D成像',
                'badge': '[正在进行]',
                'abstract': (
                    'Schmidt Ocean Institute R/V Falkor(too) 于2026年4月15日启动"设计未来3"（Designing the Future 3）深海航次，今日（04-16）持续执行。利用DeepPIV激光成像、EyeRIS系统和RAD采样器2等原型技术，深入研究海洋中层（200-1000m）透明生物多样性，计划创建4D计算机渲染图，结果将免费开放共享，可通过Schmidt Ocean网站追踪实时进展。'
                ),
                'source': 'Schmidt Ocean Institute',
                'date': '2026-04-15',
                'url': 'https://schmidtocean.org/cruises/'
            },
            {
                'title': '2. 夏威夷海洋时间序列（HOT）SS-1航次近日完成——长期开放监测持续',
                'badge': '[长期航次]',
                'abstract': (
                    '夏威夷海洋时间序列（HOT，SOEST）SS-1航次（2026-03-03至04-06）已近日完成，后续HOT-364（7月）等计划航次将继续开放，持续提供热带北太平洋生物地球化学和物理观测的长期时间序列数据，是全球历史最长的开放获取海洋观测计划之一，数据公开于HAHANA数据库。'
                ),
                'source': 'SOEST / HAHANA / HOT',
                'date': '2026-04-06',
                'url': 'https://hahana.soest.hawaii.edu/hot/'
            },
            {
                'title': '3. NOAA Ship Discoverer新船建设进展——专为深海探索开放科学直播设计',
                'badge': '[新船动态]',
                'abstract': (
                    'NOAA新一代旗舰科考船Discoverer建设持续推进（2026-04-09最新），该船于2025年3月在Louisiana造船厂下水，配备全套现代化海洋探测设备，专为深海探索和公众开放科学直播设计，建成后将显著提升NOAA开放航次接待科学家能力，与E/V Nautilus共同构成美国公开海洋探索船队核心。'
                ),
                'source': 'NOAA Ocean Exploration / Marine and Aviation Operations',
                'date': '2026-04-09',
                'url': 'https://oceanexplorer.noaa.gov/expeditions/'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Archives / Repositories',
        'items': [
            {
                'title': '1. CMEMS 4月三新产品发布——北极变化、大洋环流与全球SST观测一致性产品上线',
                'badge': '[新产品]',
                'abstract': (
                    'Copernicus Marine Service（2026-04-03）发布4月三项新产品：①北极地区新见解产品（支持海冰变化研究）；②大规模海洋环流新产品（覆盖全球环流监测）；③全球海面温度观测一致性产品（确保多源卫星SST数据一致性）。三款产品支持科学、运营和政策应用，可通过Copernicus Marine Data Store免费下载。'
                ),
                'source': 'Copernicus Marine Service / CMEMS',
                'date': '2026-04-03',
                'url': 'https://marine.copernicus.eu/news/'
            },
            {
                'title': '2. PANGAEA 5月社区研讨会开放注册——"查找与获取数据"Jupyter Notebook实操培训',
                'badge': '[培训活动]',
                'abstract': (
                    'PANGAEA地球与环境科学数据平台（2026-04-07宣布）将于5月7-8日（10:30-12:30 CEST）举办两场免费在线社区研讨会，演示新版Data Warehouse Beta版界面与编程API的数据获取方法，结合Jupyter Notebook实操练习，面向地球科学、生物多样性研究者开放注册，是掌握PANGAEA新接口批量获取海洋数据的最佳途径。'
                ),
                'source': 'PANGAEA / de.NBI',
                'date': '2026-04-07',
                'url': 'https://pangaea.de/news/'
            },
            {
                'title': '3. NOAA NCEI全球Argo数据仓库（GADR）持续归档——3900+活跃浮标实时剖面开放下载',
                'badge': '[持续更新]',
                'abstract': (
                    'NOAA NCEI全球Argo数据仓库（GADR，2026-04-13更新）持续接收归档全球Argo浮标实时剖面数据，现覆盖3900+活跃浮标，提供NetCDF格式开放下载，是全球最大历史海洋次表层剖面数据存档，气候变化监测、海洋再分析与数值预报模式初始化的核心数据来源，与国际Argo GDAC数据中心实时同步。'
                ),
                'source': 'NOAA NCEI / Global Argo Data Repository',
                'date': '2026-04-13',
                'url': 'https://www.ncei.noaa.gov/products/global-argo-data-repository'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources / GitHub',
        'items': [
            {
                'title': '1. Copernicus Marine Toolbox最新更新——CLI+Python API批量海洋数据访问能力增强',
                'badge': '[工具更新]',
                'abstract': (
                    'Copernicus Marine Toolbox（copernicusmarine，PyPI，近期最新稳定版2.3.x）持续迭代，提供覆盖CMEMS全部产品的命令行（CLI）和Python API统一访问接口，支持时间/空间子集化、多变量批量下载、OPeNDAP流式传输，与xarray/Dask原生集成，适合海洋数据处理流水线自动化，是访问哥白尼海洋数据最高效的Python工具。'
                ),
                'source': 'Copernicus Marine Service / PyPI',
                'date': '2026-04-10',
                'url': 'https://pypi.org/project/copernicusmarine/'
            },
            {
                'title': '2. PANGAEA Data Warehouse Beta——Python/R+Jupyter Notebook编程接口批量数据检索',
                'badge': '[新功能]',
                'abstract': (
                    'PANGAEA（2026-04-07）新版Data Warehouse Beta接口支持通过Python/R脚本与Jupyter Notebook直接检索并下载地球与环境科学数据集，相较旧版搜索界面大幅提升批量数据获取效率，配套5月社区研讨会提供实操培训，是海洋数据科学家将PANGAEA数据纳入自动化工作流的重要新能力。'
                ),
                'source': 'PANGAEA / de.NBI / Jupyter',
                'date': '2026-04-07',
                'url': 'https://pangaea.de/'
            },
            {
                'title': '3. GO-BGC年度浮标数据与科学研讨会（8月17-21日）开放注册——OneArgo Python工具链展示',
                'badge': '[活动预告]',
                'abstract': (
                    'GO-BGC官网（2026-04-07）宣布2026年8月17-21日在美国举办年度浮标数据与科学研讨会，展示BGC-Argo数据处理Python工具包（OneArgo-Mat/R/Python等）最新功能，覆盖数据下载、剖面可视化到海洋生物地球化学分析的完整工作流，现已开放注册，是全球BGC-Argo工具生态年度交流的重要平台。'
                ),
                'source': 'GO-BGC / WHOI',
                'date': '2026-04-07',
                'url': 'https://www.go-bgc.org/'
            },
            {
                'title': '4. SEA-PY海洋Python工具资源列表（2026-03-23更新）——最全海洋Python生态导航',
                'badge': '[资源汇总]',
                'abstract': (
                    'pyoceans社区维护的SEA-PY海洋Python工具资源列表（pyoceans.github.io/sea-py，2026-03-23更新）收录覆盖数据I/O（netCDF4、xarray、scipy）、可视化（cartopy、cmocean）、数据同化、生物地球化学（seawater/gsw）等方向的开源工具，是海洋数据科学家寻找Python生态工具的最全参考资源，持续社区维护。'
                ),
                'source': 'pyoceans / GitHub Pages',
                'date': '2026-03-23',
                'url': 'https://pyoceans.github.io/sea-py/'
            },
        ]
    },
]'''

if __name__ == '__main__':
    with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.index('SECTIONS = [')
    end_idx = content.index('\n]', start_idx) + 2

    new_content = content[:start_idx] + NEW_SECTIONS + content[end_idx:]

    with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print('SECTIONS updated successfully for 2026-04-16')
    total_items = NEW_SECTIONS.count("'title': '")
    print(f'Total items: {total_items}')
