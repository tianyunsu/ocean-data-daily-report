# -*- coding: utf-8 -*-
"""Write SECTIONS for 2026-10-08 into feishu_write_doc.py (regex replace)."""
import re

SECTIONS = [
{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [
    {'title': '深度学习统计降尺度海表温度：残差校正神经网络让高分辨率SST更准确',
     'badge': '[论文]',
     'abstract': '准确的局地海表温度（SST）对气候与海洋预报至关重要，而卫星与再分析产品的空间分辨率往往不足。研究提出基于残差校正的神经网络统计降尺度方法，以粗分辨率SST场为输入、高分辨率观测为目标，训练网络学习系统性残差，在保持大尺度结构一致的同时改善局地细节，为高分辨率SST产品生成提供新途径。（AGU）',
     'source': 'Journal of Geophysical Research: Machine Learning and Computation',
     'url': 'https://doi.org/10.1029/2025JH000967', 'date': '2026-10-01'},
    {'title': 'LLM4SST：用大语言模型实现时空分布感知的结构一致海温预报',
     'badge': '[论文]',
     'abstract': '针对现有海表温度（SST）预报在长时序结构与空间一致性上不足的问题，研究提出LLM4SST，将大语言模型的序列建模能力与时空分布感知优化策略相结合，对SST场开展结构一致的预测，缓解预报结果的过度平滑与空间失真，提升区域海温预报的可信度。（Elsevier）',
     'source': 'Expert Systems with Applications',
     'url': 'https://doi.org/10.1016/j.eswa.2026.134587', 'date': '2026-09-29'},
    {'title': '全球海山机器学习探测：从卫星重力场中识别海底地形',
     'badge': '[论文]',
     'abstract': '海山是深海重要的地貌与生态单元，但全球尺度人工编目困难。研究利用机器学习方法，从卫星测高衍生的重力场信息中自动识别海山，构建全球海山探测流程并与既有海山编目进行比对，展示数据驱动方法在海底地形识别与空白区补全上的潜力。（Elsevier）',
     'source': 'Earth and Planetary Science Letters',
     'url': 'https://doi.org/10.1016/j.epsl.2026.120368', 'date': '2026-10-01'},
    {'title': 'OceanMind：直接耦合大语言模型与三维海洋状态的多智能体诊断系统',
     'badge': '[论文]',
     'abstract': '从三维、多变量、随时间演变的海洋状态中提取定量证据需要大量复杂分析。研究提出OceanMind，一个将大语言模型与完整三维时变海洋状态直接耦合的多智能体系统，把分析流程组织为查询路由、基于技能的计划、工具执行与基于证据的总结四个阶段，并以63个可复用的海洋分析技能作为过程手册。在240个计算工作流查询基准上，相对通用ReAct智能体在有效性上提升41.2%、效率提升21.5%，并能复现已发表的海洋诊断结论、支撑环境决策。',
     'source': 'arXiv',
     'url': 'https://arxiv.org/abs/2610.03780', 'date': '2026-10-06'},
    {'title': 'AI解码「海洋雪」：NSF资助70万美元让水下图像读出颗粒化学成分',
     'badge': '[动态]',
     'abstract': '罗德岛大学研究生海洋学学院Melissa Omand团队获美国国家科学基金会近70万美元资助，联合缅因大学开发AI工具，尝试从水下相机拍摄的「海洋雪」（沉降颗粒）图像特征（粒径、形状、透明度）推断其化学成分，以减少人工分类工作量、改进对碳与营养盐向深海输送通量的估算，并把微塑料识别纳入其中。项目计划2027年1月启动、2029年12月结束。',
     'source': 'University of Rhode Island',
     'url': 'https://www.uri.edu/news/2026/10/reading-the-oceans-snowflakes-how-ai-decodes-marine-snow', 'date': '2026-10-05'}]},

{'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
    {'title': '里海数字孪生受IOC/UNESCO支持，成为区域海洋治理关键数字工具',
     'badge': '[动态]',
     'abstract': '国际海洋研究所（IOI）与里海研究所（CSI）表示，最有价值的数字工具是能把不同形式信息整合进统一规划环境的技术；由IOC/UNESCO支持的里海数字孪生（Caspian Sea Digital Twin）尤为重要，它可将水位、盐度、生物多样性、航运、基础设施与气候等信息整合进共享分析环境，但其实际价值取决于底层数据质量与区域机构的数据交换机制，并需配套数据共享协议、机构协作与持续能力建设。',
     'source': 'Trend (Azerbaijan)',
     'url': 'https://www.trend.az/casia/4230715.html', 'date': '2026-10-03'},
    {'title': '认知数字海洋：量子混合计算、数字孪生与图神经网络融合展望',
     'badge': '[论文]',
     'abstract': '研究提出「认知数字海洋」（Cognitive Digital Ocean）框架，探讨将量子混合计算、数字孪生与图神经网络整合用于海洋系统建模与分析的思路，面向海洋观测、预报与决策支持等场景，勾勒把物理模型与认知/学习能力相结合的技术路线。',
     'source': 'Fisheries（俄）',
     'url': 'https://doi.org/10.36038/0131-6184-2026-4-130-139', 'date': '2026-09-24'},
    {'title': '用神经方案破解海洋生物地球化学动力学的校准与再分析难题（一维垂直模型）',
     'badge': '[论文]',
     'abstract': '海洋生物地球化学模型的参数校准与再分析重建长期依赖高成本反演。研究在一维垂直模型框架下引入神经网络方案来求解校准与再分析挑战，探索以学习方法替代或加速传统参数估计的可行性，为生物地球化学模式的参数化与再分析产品生成提供新途径。（Copernicus）',
     'source': 'Biogeosciences',
     'url': 'https://doi.org/10.5194/bg-23-6879-2026', 'date': '2026-10-06'},
    {'title': '面向近海航运CO₂减排的风险感知数字孪生航速优化（伊斯坦布尔—比雷埃夫斯航线）',
     'badge': '[论文]',
     'abstract': '研究以近海短途航运为对象，构建风险感知的数字孪生框架用于航速优化，在兼顾航期与运营约束的同时以降低CO₂排放为目标，并以伊斯坦布尔—比雷埃夫斯航线为案例开展验证，展示数字孪生在绿色航运决策中的应用路径。',
     'source': 'Journal of ETA Maritime Science',
     'url': 'https://doi.org/10.4274/jems.2026.95826', 'date': '2026-10-02'}]},

{'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [
    {'title': 'Bluegraph：把NOAA浮标原始波谱重建为三维海况的可视化工具',
     'badge': '[工具]',
     'abstract': 'Bluegraph是一个新的三维可视化平台，将美国国家数据浮标中心（NDBC）的海洋观测数据从「测得的波谱」重建为三维海况并加以呈现。平台聚合了浮标、沿岸站、验潮站与河口站等共715个站点（含286座浮标、175个沿岸站、226个验潮站、28个河口站），横跨两大洋、加勒比海与五大湖，自2025年4月起已累计跟踪超过1.13亿个数据点，截至最近观测有699/715个站点在近3小时内回传数据，可直观查看波高、风速等要素的空间分布。',
     'source': 'Bluegraph (via Hacker News)',
     'url': 'https://bluegraph.io/', 'date': '2026-09-29'},
    {'title': '世界航运理事会携手HUB Ocean发布数字化「全球鲸类图谱」',
     'badge': '[动态]',
     'abstract': '世界航运理事会（WSC）与HUB Ocean合作，把2023年首发的WSC鲸类图谱升级为数字化版本，将全球范围内为减少船舶对鲸类伤害而设的强制性/自愿性措施（限速、定线、避让区、水下噪声管控等）集中呈现在可地图化、可检索的地理平台上，并接入HUB Ocean海洋数据平台，可与海洋保护区等权威数据集叠加使用，便于航行规划与作业系统直接调用。',
     'source': 'World Shipping Council',
     'url': 'https://www.worldshipping.org/news/world-shipping-council-launch-digital-global-whale-chart-with-hub-oceannbsp', 'date': '2026-10-07'},
    {'title': 'Apaluma推出Currents：基于开放联邦数据的交互式海洋—气候可视化模型',
     'badge': '[动态]',
     'abstract': 'Apaluma发布Currents系列交互式在线模型，首个发布「厄尔尼诺与格兰德河」把来自十余个联邦数据源的实时海表温度、预报、河流水位与积雪数据整合进单一仪表盘，并以Esri ArcGIS地图技术呈现；模型还设实时校验面板追踪海气耦合状态，并明确说明区域气候信号无法归因单日天气，强调可视化在线的可信度透明。',
     'source': 'PR Newswire',
     'url': 'https://www.prnewswire.com/news-releases/el-nino-is-back-see-what-it-means-for-snowpack-and-water-from-the-rockies-to-the-rio-grande-302901199.html', 'date': '2026-10-07'},
    {'title': 'Ocean Visions发布海洋CO₂去除知识平台：交互式地图与图表',
     'badge': '[动态]',
     'abstract': 'Ocean Visions上线海洋二氧化碳去除（mCDR）知识平台，提供交互式地图展示历史与在建的mCDR野外试验及参与方分布，附可交互与可下载的图表，并收录近300个mCDR参与方及其连接关系目录；该平台整合并替代其2023与2024年发布的试验数据库与生态数据库，面向研究者、资助方、决策者与媒体开放。',
     'source': 'Carbon Herald',
     'url': 'https://carbonherald.com/ocean-visions-launches-new-marine-carbon-dioxide-removal-knowledge-platform/', 'date': '2026-10-01'}]},

{'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA-QC', 'items': [
    {'title': '圣劳伦斯河口SWOT验证水位与海浪基准数据集',
     'badge': '[数据]',
     'abstract': '研究发布用于SWOT卫星验证的水位与海浪基准数据集，覆盖圣劳伦斯河口与萨格奈峡湾（加拿大魁北克）。数据集整合现场水位与波浪观测，为SWOT在河口/峡湾复杂动力环境下的水位与波高验证、标定及误差诊断提供参照，支撑下游卫星测高产品的质量评估。（Copernicus/ESSD）',
     'source': 'Earth System Science Data',
     'url': 'https://doi.org/10.5194/essd-18-7269-2026', 'date': '2026-10-05'},
    {'title': '基于云原生处理与海豹标签验证的高分辨率南极海表温度',
     'badge': '[论文]',
     'abstract': '南极近岸海表温度（SST）观测稀疏。研究借助云原生（cloud-native）处理流程生成高分辨率南极SST产品，并利用在海豹身上布放的标签数据开展独立验证，为极区SST产品的精度评估与改进提供新证据。（Elsevier）',
     'source': 'Remote Sensing of Environment',
     'url': 'https://doi.org/10.1016/j.rse.2026.115706', 'date': '2026-10-05'},
    {'title': '面向高效海洋环境监测的船载异常检测',
     'badge': '[论文]',
     'abstract': '针对海洋环境监测数据量大、回传带宽有限的问题，研究提出船载（on-board）异常检测方法，在数据采集端即完成异常识别，以降低传输与后处理负担，提高监测系统的效率与实时性。',
     'source': 'arXiv',
     'url': 'https://arxiv.org/abs/2610.03649', 'date': '2026-10-02'},
    {'title': 'GNSS/水准导出的大地水准面高质量控制及其对LiDAR海岸低地分类的启示',
     'badge': '[论文]',
     'abstract': '研究针对由GNSS与水准测量导出的大地水准面高开展质量控制，分析其对基于LiDAR的海岸低海拔分类的影响，为海岸带高程基准一致性与低地识别提供质量把关方法与证据。（MDPI）',
     'source': 'Remote Sensing (MDPI)',
     'url': 'https://doi.org/10.3390/rs18193406', 'date': '2026-10-04'}]},

{'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [
    {'title': 'REACT：海洋活性示踪物的物理与化学一致重建',
     'badge': '[论文]',
     'abstract': '海洋活性示踪物（如营养盐、溶解氧等）的观测稀疏且分布不均。研究提出REACT方法，在重建海洋活性示踪物场时同时约束物理与化学一致性，力求在填补观测空白的同时保持与物理场及化学计量关系的自洽，服务于海洋生物地球化学场的再分析/重建。',
     'source': 'arXiv',
     'url': 'https://arxiv.org/abs/2610.03888', 'date': '2026-10-02'},
    {'title': 'BridgeCast：以外生变量的流匹配连接海浪预报与再分析',
     'badge': '[论文]',
     'abstract': '研究提出BridgeCast，利用带外生变量的流匹配（flow matching）方法在海浪预报与再分析之间建立映射，实现预报场与再分析场之间的偏差校正与桥接，从而改善长时序海浪记录的连续性与一致性。',
     'source': 'arXiv',
     'url': 'https://arxiv.org/abs/2610.03759', 'date': '2026-09-27'},
    {'title': '融合卫星与现场观测的多尺度三维海洋温度反演',
     'badge': '[论文]',
     'abstract': '研究提出多尺度方法，融合卫星观测与现场（in situ）观测来反演三维海洋温度场，兼顾不同空间尺度上的信息，改善次表层温度结构的重建精度，为三维温盐场产品生成提供技术路径。（Elsevier）',
     'source': 'International Journal of Applied Earth Observation and Geoinformation',
     'url': 'https://doi.org/10.1016/j.jag.2026.105615', 'date': '2026-09-28'},
    {'title': '用动态图神经网络增强SWOT像素云中的水体检测',
     'badge': '[论文]',
     'abstract': 'SWOT卫星的像素云（pixel cloud）数据在近岸与复杂水文条件下水体检测困难。研究提出基于动态图神经网络的检测方法，利用像素之间的空间关系建模，提升SWOT像素云中水体的识别能力，为下游水位/流量产品处理打下基础。',
     'source': 'arXiv',
     'url': 'https://arxiv.org/abs/2609.34954', 'date': '2026-09-28'}]},

{'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [
    {'title': 'OAE Data Commons：海洋碱度增强研究数据共享开放基础设施',
     'badge': '[动态]',
     'abstract': 'Submarine Scientific与Carbon to Sea联合发布OAE Data Commons，面向海洋碱度增强（OAE）研究提供共享开放基础设施：包含与NOAA共同制定、逾百位协作方参与的OAE数据管理协议，可检索的OAE Data Search注册库（含项目与数据集、支持申请专有数据），以及引导数据管理员规范提交的Metadata Builder工具，首批纳入加拿大、美国与欧洲的6个项目。',
     'source': 'Carbon to Sea Initiative',
     'url': 'https://www.carbontosea.org/2026/10/06/oae-data-commons/', 'date': '2026-10-06'},
    {'title': '面向海洋观测系统互操作的水深数据：整合水文学标准与FAIR数据实践',
     'badge': '[论文]',
     'abstract': '研究聚焦海洋观测系统中水深（bathymetric）数据的互操作性问题，探讨如何整合水文学相关标准与FAIR数据原则，弥合不同平台与格式间的语义鸿沟，为水深数据的发现、共享与跨系统复用提供规范路径。（Frontiers）',
     'source': 'Frontiers in Marine Science',
     'url': 'https://doi.org/10.3389/fmars.2026.1949937', 'date': '2026-10-05'},
    {'title': '英国地质调查局海洋调查数据（含地质样品）更新并接入MEDIN地质与地球物理归档中心',
     'badge': '[数据]',
     'abstract': '英国地质调查局（BGS）更新其自1966年以来的海洋调查数据集合，内容涵盖数字与模拟记录及实体样品材料，数据存放于国家地球科学数据中心（NGDC）及海洋环境数据与信息网络（MEDIN）地质与地球物理数据归档中心（DAC），包括地震反射、侧扫声呐、多波束测深与后向散射、重磁以及钻孔/岩芯/海底取样等地质地球物理与样品数据，最新更新日期为2026年10月2日。',
     'source': 'data.gov.uk / British Geological Survey',
     'url': 'https://data.gov.uk/dataset/9fb2372b-42b6-4c1a-8573-8fec60612089/marine-survey-data-from-around-the-uk-1966-onwards1', 'date': '2026-10-02'},
    {'title': '开放科学背景下科研数据共享的演化博弈分析',
     'badge': '[论文]',
     'abstract': '研究运用演化博弈方法分析开放科学情境下科研数据共享中各方（如数据提供方与使用方）的策略选择与均衡，探讨激励机制、成本收益与制度设计对共享意愿及稳定共享格局的影响，为海洋等领域的科学数据开放共享机制设计提供理论参考。（Frontiers）',
     'source': 'Frontiers in Physics',
     'url': 'https://doi.org/10.3389/fphy.2026.1941515', 'date': '2026-10-05'}]},

{'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
    {'title': 'CSIRO「Investigator」号执行170°W赤道至冰缘P-TROPOE航次，太平洋青年科学家同船',
     'badge': '[航次]',
     'abstract': '澳大利亚联邦科学与工业研究组织（CSIRO）「Investigator」号于2026年9月27日至12月16日执行P-TROPOE航次，沿西太平洋170°W断面从赤道一直观测到南极冰缘，开展全水深物理、生物地球化学与生物测量，以监测海洋变化与变率。航次分两段（斐济—惠灵顿、惠灵顿—霍巴特），共有逾15家机构约70名科研人员参与，并通过太平洋共同体（SPC）与POGO伙伴关系吸纳包括两名斐济学者在内的四位太平洋青年研究者同船，数据将服务于气候模式、IPCC评估与区域气候预估。',
     'source': 'CSIRO',
     'url': 'https://www.csiro.au/en/about/facilities-collections/MNF/Voyages-schedules/Voyages/2026/September/IN2026_V06', 'date': '2026-09-27'},
    {'title': '中国大洋97航次（B航段）启航：十余家单位联合开展多金属结核调查',
     'badge': '[航次]',
     'abstract': '由中国大洋事务管理局/自然资源部第二海洋研究所组织实施的中国大洋97航次（B航段）任务时间为2026年9月27日至2027年1月1日（为期96天），全国十余家单位共同参与，作业内容涵盖箱式取样、锚系观测、环境监测阵列布放试验及国家重点研发计划装备海试等，体现多单位联合、船时共享的大洋科考组织模式。',
     'source': '东华理工大学',
     'url': 'http://www.ecit.cn/34/33/c7857a144435/page.htm', 'date': '2026-09-27'},
    {'title': '「海洋地质七号」「海洋地质九号」双船坚守海上作业一线',
     'badge': '[航次]',
     'abstract': '中国地质调查局青岛海洋地质研究所「海洋地质七号」「海洋地质九号」船在国庆期间坚守海上作业一线，持续开展海域区域地质调查与海上多道地震勘探。「海洋地质七号」开展浅地层剖面探测、单波束测深及重力、磁力等地球物理观测，采集海底地形与地层结构数据，进一步完善海域地质数据库，为海洋地质科研与资源开发提供数据支撑。',
     'source': '中国自然资源报',
     'url': 'https://www.iziran.net/news.html?aid=5497320', 'date': '2026-10-02'}]},

{'title': '八、海洋数据中心', 'en': 'Ocean Data Centers / Archives / Repositories', 'items': [
    {'title': 'UVP5水下成像构建浮游生物与碎屑全球一致数据库（约800万图像）',
     'badge': '[数据]',
     'abstract': '研究发布由Underwater Vision Profiler 5（UVP5）SD与HD两种成像系统获取的浮游生物与碎屑全球数据集，覆盖2008—2018年、3114个剖面、约800万个目标，按33个统一类别分类；碎屑在浓度（90%）与生物量（95%）上占比最高，桡足类为最丰富浮游类群。数据集公开托管于SEANOE（doi:10.17882/107583），可作为机器学习分类的训练集，用以提升生物多样性量化与碳通量模型精度。（Copernicus/ESSD）',
     'source': 'Earth System Science Data / SEANOE',
     'url': 'https://essd.copernicus.org/articles/18/7345/2026/', 'date': '2026-10-06'},
    {'title': 'BCSS发布非洲首个永久海洋观测站8年环境与生物多样性开放数据',
     'badge': '[数据]',
     'abstract': '位于莫桑比克巴扎鲁托群岛的巴扎鲁托科学研究中（BCSS）发布其海洋观测站连续8年的监测数据——累计超过2200万条测量、覆盖30余项化学/环境/生物多样性变量、6类生态系统与14个长期监测站（约6850平方公里），并形成含21个数据集、带元数据与DOI链接的标准化开放获取数据仓储；相关方法学与「度假村转科研」（Resort-to-Research）资助模式发表于Frontiers in Marine Science两篇论文。',
     'source': 'BCSS (Bazaruto Center for Scientific Studies)',
     'url': 'https://bcssmz.org/?p=5166', 'date': '2026-10-01'},
    {'title': '1938年波罗的海藻类植物标本入藏Ocean Archive：高分辨率数字化长期存档',
     'badge': '[动态]',
     'abstract': '海洋生态学家Nils Kautsky将藻类研究者Mats Waern于1938年采集的波罗的海植物标本移交Ocean Archive。Ocean Archive将标本拍照并高分辨率数字化、在保存原件的同时形成可长期检索的数字记录，使未来研究者能像当年Kautsky回访Waern记录一样，用历史标本（含采集时间与地点）对比过去与现在的海洋环境。',
     'source': 'Voice of the Ocean',
     'url': 'https://voiceoftheocean.org/ocean-archive-baltic-sea-herbarium-1938/', 'date': '2026-10-01'}]},

{'title': '九、工具与代码资源调研', 'en': 'Tools & Code Resources', 'items': [
    {'title': '水下气泡声散射Python建模包',
     'badge': '[工具]',
     'abstract': '研究发布一个基于Python的建模包，用于计算单个气泡引起的水下声学后向散射，面向水体气泡声学探测与反演研究，提供可复用的建模与计算工具。（Wiley/ASLO）',
     'source': 'Limnology and Oceanography: Methods',
     'url': 'https://doi.org/10.1002/lom3.70099', 'date': '2026-10-06'},
    {'title': 'OSEkit v1.2.1：水声被动声学数据管理与分析Python工具包',
     'badge': '[开源]',
     'abstract': 'OSEkit是一个面向水下被动声学数据管理与分析的开源Python包，支持跨多文件的基于时间戳无缝访问（可按时间区间请求音频）、重采样与归一化等预处理，以及功率谱、频谱图、LTAS等频谱分析，并与其Web端频谱图标注工具APLOSE配合使用；v1.2.1于2026年9月底发布，仓库持续活跃更新。',
     'source': 'GitHub / Project-OSmOSE',
     'url': 'https://github.com/Project-OSmOSE/OSEkit', 'date': '2026-09-29'},
    {'title': 'Copernicus Marine Toolbox v2.5.0发布：新增多边形子集与文档元数据访问',
     'badge': '[工具]',
     'abstract': 'Copernicus Marine Toolbox于2026年9月28日发布v2.5.0。新版本引入多边形（polygon）子集切取能力，可通过describe命令更方便地访问产品文档元数据，并在元数据处理与文件大小估算方面带来多项修复与改进；同时支持以copernicusmarine[extra]方式安装rioxarray、geopandas等可选依赖，netcdf4 3.0.0亦已兼容。',
     'source': 'Copernicus Marine Service / PyPI',
     'url': 'https://pypi.org/project/copernicusmarine/2.5.0/', 'date': '2026-09-28'},
    {'title': 'OpenWater Hub：面向海洋机器人与水质数据采集的开源硬件平台',
     'badge': '[开源]',
     'abstract': '研究提出OpenWater Hub，一个面向海洋机器人支持与水质数据采集的开源硬件平台，旨在以模块化、低成本的开放设计降低海洋现场观测与水质监测设备的使用门槛。（Elsevier/HardwareX）',
     'source': 'HardwareX',
     'url': 'https://doi.org/10.1016/j.ohx.2026.e00845', 'date': '2026-10-01'}]},
]


def main():
    src_path = 'feishu_write_doc.py'
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_repr = repr(SECTIONS).replace('\\x27', "'")
    pattern = re.compile(r'SECTIONS = \[.*?(?=\ndef tr\(|\n# ---|\Z)', re.DOTALL)
    if not pattern.search(content):
        raise SystemExit('ERROR: SECTIONS block not found in feishu_write_doc.py')
    content = pattern.sub('SECTIONS = ' + new_repr + '\n\n\n', content, count=1)
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(content)
    total = sum(len(s['items']) for s in SECTIONS)
    effective = sum(1 for s in SECTIONS for i in s['items'] if i.get('badge') != '[备注]')
    print(f'OK: SECTIONS written. Total items: {total} (effective: {effective})')
    for s in SECTIONS:
        print('  ', s['title'], len(s['items']))


if __name__ == '__main__':
    main()
