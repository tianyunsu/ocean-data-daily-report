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

yesterday_cn = (datetime.now()).strftime('%Y年%m月%d日')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '全国首个「海洋Token工厂」落地青岛：130余类涉海数据、800P算力、20余个海洋大模型', 'badge': '[要闻]', 'abstract': '2026海洋合作发展论坛「探索深海——海洋未来产业的价值变革」平行论坛现场，全国首个面向海洋产业的专属智能要素供给平台——海洋Token（词元）工厂正式发布并落地青岛。平台由中国移动山东公司建设，整体架构含数据、算力、算法三部分：数据侧提供海上作业规范、海洋环境要素等130多类涉海数据；算力侧已形成总规模超800P的海洋算力资源池并持续扩容；算法侧汇聚「观海」「海星」等20多个海洋领域专有大模型及「九天」等30多款通用模型。平台以Token为智能服务的统一计量载体，将数据治理、算力调度、模型服务与工具组件标准化封装，按需供给、按量计量。', 'source': '钱江晚报·潮新闻 / 今日头条', 'url': 'https://www.toutiao.com/article/7691582336281887259', 'date': '2026-10-01'}, {'title': '物理约束AI让海洋预测更可信：300余位专家的共识', 'badge': '[论文]', 'abstract': '《Ocean-Land-Atmosphere Research》在线刊出综述，指出AI海洋学的下一阶段取决于「物理约束」——把动力学方程与过程关系嵌入学习与评估，而非仅从历史数据中提取统计模式。文章源于在济南举行的第五届人工智能海洋学论坛（300余位专家、80余家机构）。作者归纳三类最有前景的问题：① 由海表信息重建次表层温盐场；② ENSO 等长周期气候预测；③ 业务化海浪预报；并强调不确定性量化与「AI+数值模式」混合路线，主张以物理知识作为可信度来源而非对AI能力的限制。', 'source': 'Ocean-Land-Atmosphere Research / Scienmag', 'url': 'https://scienmag.com/physics-constrained-ai-promises-a-more-predictable-ocean-researchers-say', 'date': '2026-10-02'}, {'title': '双分支物理信息神经网络：环境参数不足下的海洋声场预测与声速剖面重建', 'badge': '[论文]', 'abstract': '准确计算海洋声压场对水声应用至关重要，而传统数值模型依赖全深度声速剖面（SSP）与海底地声参数等完整环境先验。研究提出双分支物理信息神经网络（DB-PINN），在海底地声参数不确定、SSP 深度截断的条件下预测声压场，并同步重建全深度 SSP。模型由两条并行分支分别承担声压场预测与剖面重建，缓解了环境参数不足带来的精度退化。', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128177', 'date': '2026-09-29'}, {'title': 'LLM辅助分层规划框架：异构多AUV协同区域搜索', 'badge': '[论文]', 'abstract': '针对异构多AUV协同区域搜索中「平台能力差异带来的覆盖代价、时间—能量耦合、时序协同约束」考虑不足导致分区次优与能力—任务失配的问题，研究提出基于 Voronoi 的区域参数化方法，将区域分解与任务分配建模为连续优化问题，并引入大语言模型辅助的分层规划框架，使高层规划与底层执行解耦，提升异构集群协同搜索的任务适配性与效率。', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128408', 'date': '2026-10-01'}, {'title': '拉格朗日时序机器学习框架：海洋边界层云凝结核预测与驱动过程解析', 'badge': '[论文]', 'abstract': '大气气溶胶对气候与空气质量具有关键作用，准确评估其环境影响需理解丰度、分布及其控制过程；既有机器学习研究多侧重预测而较少用于过程解析，且往往忽略前若干日发生、却显著塑造气溶胶群体的过程。研究提出拉格朗日时序机器学习框架，更好地刻画随气团输运演变的前置过程，并以海洋边界层云凝结核（CCN）为对象开展应用，兼顾预测精度与驱动因子可解释性。（AGU）', 'source': 'Journal of Advances in Modeling Earth Systems (JAMES)', 'url': 'https://doi.org/10.1029/2026ms005751', 'date': '2026-09-28'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': 'ABS × HD现代重工 × 西门子：以数字孪生+CFD评估氨燃料船泄漏风险', 'badge': '[动态]', 'abstract': '在 Gastech 2026 上，ABS、HD韩国造船海洋（HD KSOE）与西门子宣布合作，将计算流体力学（CFD）分析与数字孪生技术结合，预测氨燃料船舶发生泄漏后氨的扩散行为，使设计早期即可评估更广泛的泄漏与事故场景。分工上，HD KSOE 负责氨安全系统开发与实验研究，西门子提供仿真分析与数字孪生技术，ABS 提供以数字孪生为核心的安全评估方法。三方称此举可为氨燃料船提供更快、更严格的安全验证。', 'source': 'The Motorship', 'url': 'https://www.motorship.com/news/alternative-fuels-lubricants/digital-twins-to-assess-ammonia-risks/', 'date': '2026-10-01'}, {'title': '富士通将在 CEATEC 2026 展出海洋数字孪生技术', 'badge': '[动态]', 'abstract': '富士通宣布参加 10 月 13—16 日在日本幕张展览馆举行的 CEATEC 2026。在 JEITA 主办的「海洋数字社会馆」，富士通将介绍其海洋数字孪生技术——利用海洋与河流观测数据把原本不可见的水下状况数字化，支撑水域利用与管理的决策；在「太空共创馆」则展示星上卫星AI与海事地面站协同、快速向现场下发观测数据的能力。', 'source': 'Fujitsu / JCN Newswire', 'url': 'https://hkcrunch.com/jcn-newswire/fujitsu-to-showcase-technologies-for-a-resilient-society-at-ceatec-2026', 'date': '2026-10-01'}, {'title': 'OceanStream Globe：运行于欧洲数字孪生海洋（EDITO）的三维海洋数据浏览器', 'badge': '[工具]', 'abstract': 'OceanStream 推出全新海洋数据服务 OceanStream Globe：持续下载并处理全球海洋每日物理与生物地球化学数据，计算历史时间序列与逐像素统计（均值、常态范围等），并以可旋转三维地球展示。整条流水线运行在欧洲基础设施之上：数据来自 Copernicus Marine OSTIA，平台为欧洲数字孪生海洋（EDITO）DataLab，存储由 CloudFerro 承担，批处理在巴塞罗那超算 MareNostrum 5 上通过 EuroHPC 完成（35 年气候态计算耗时约 2 小时 35 分钟）。页面以 2026 年厄尔尼诺为例演示 35 年 SST 气候态对比，现已公开预览。', 'source': 'OceanStream / EDITO（European Digital Twin Ocean）', 'url': 'https://oceanstream.io/visualise-the-2026-el-nino-with-35-years-of-copernicus-marine-data', 'date': '2026-09-28'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': 'IEEE VIS 2026 最佳论文荣誉提名：任务驱动的多尺度海洋流场动力学可视化框架', 'badge': '[顶会]', 'abstract': 'KAUST CLIMATics 研究组的论文《A Task-Driven Framework for Multiscale Ocean Flow Dynamics through Integrated Simulation and Visualization》获 IEEE VIS 2026 最佳论文荣誉提名。高分辨率海洋模式产生的大体量三维数据（内波生成与传播、能量输运、近岸相互作用）在复杂计算网格与多变量时变条件下难以理解；该框架把数值模拟与交互式可视化连接起来：将混合海洋模式网格重建为连续三维表示，并在统一环境中整合流场分解、体绘制、交互切片与多变量分析，支持从横向波传播、能量输运路径到浅化混合的多视角探索。论文将于 11 月在 IEEE VIS 2026 报告。', 'source': 'IEEE VIS 2026 / KAUST Visualization Core Lab', 'url': 'https://climatics.kaust.edu.sa/news/detail/2026/10/01/climatics-research-featured-with-best-paper-honorable-mention-at-ieee-vis-2026', 'date': '2026-10-01'}, {'title': 'OceanXL：分块划分与自适应剪枝的大规模水下三维高斯泼溅', 'badge': '[论文]', 'abstract': '水下三维重建对海洋勘探、生态监测与海底基础设施检测至关重要，但受光衰减、散射与采集覆盖限制，大尺度重建困难；三维高斯泼溅（3DGS）虽可实时高质量渲染，却受内存占用高、大范围优化低效制约。研究提出 OceanXL：采用分治策略把场景划分为空间连贯区块，在保持全局几何一致性的同时提升优化效率，并引入面向水下条件的自适应剪枝方案删除冗余基元以压缩表示；作者同时发布覆盖多样海洋环境的大规模水下数据集，在五个大场景上显示出良好的可扩展性与「效率—质量」折中。（布里斯托大学等）', 'source': 'arXiv (cs.CV) 2609.29985', 'url': 'https://arxiv.org/abs/2609.29985', 'date': '2026-09-24'}, {'title': '基于GIS的岛屿景观视觉特征评估：舟山群岛海陆互视刻画', 'badge': '[论文]', 'abstract': '海岸旅游、港口扩张与围填海持续加大对岛屿景观的压力，亟需系统的视觉评估支撑可持续规划管理。研究面向中国舟山群岛提出一套 GIS 方法：以景观特征制图为空间组织基础，分别刻画「由海向陆」与「由陆向海」的前景—背景互视条件，方法包含陆域、海岸与海域景观特征制图三个阶段，为海岛国土空间规划与景观管理提供可操作的视觉评估依据。', 'source': 'Ocean & Coastal Management', 'url': 'https://doi.org/10.1016/j.ocecoaman.2026.108379', 'date': '2026-10-01'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'GNSS-R海面散射计再校准：梯度提升决策树方案', 'badge': '[论文]', 'abstract': '星载全球导航卫星系统反射测量（GNSS-R）在海洋散射测量领域发展迅速，但部分关键参数不准与复杂空间环境导致的残余信号标定误差会显著降低性能。研究提出基于梯度提升决策树（GBDT）的一步式信号再校准框架，以定性分析引导的尺度订正方式进行；结果显示学习得到的订正因子与理论订正因子吻合良好，分箱比（BR）等指标表现优异，为 GNSS-R 海洋散射计产品的偏差治理提供了数据驱动路径。', 'source': 'Remote Sensing of Environment', 'url': 'https://doi.org/10.1016/j.rse.2026.115699', 'date': '2026-09-29'}, {'title': 'SHELDA：次小时级欧洲质量控制海平面数据集', 'badge': '[数据]', 'abstract': '公开可获取的海平面数据库常存在两个缺口：时间序列为小时级甚至更长采样步长，或虽为高频数据却未经过质量控制。SHELDA（Sub-Hourly European Quality Controlled Sea Level DAtaset）填补该空白：包含 257 条验潮站记录（NetCDF 格式），每条为质量控制后的海平面序列、采样间隔 1—15 分钟，并附带去除潮汐后得到的残差序列，便于风暴潮与极值水位分析。（ESSD 数据论文）', 'source': 'Earth System Science Data (ESSD)', 'url': 'https://doi.org/10.5194/essd-18-7143-2026', 'date': '2026-09-30'}, {'title': 'MHW-MAD：多定义全球海洋热浪数据库', 'badge': '[数据]', 'abstract': '海洋热浪（MHW）是海表温度（SST）的持续性暖异常，会扰动海洋生态系统、物理气候过程与沿海人类活动；但不同用户（生态学家与气候学家等）对阈值与指标的定义需求各异，导致结果难以横向比较。研究发布新的全球逐日 MHW 指标数据库 MHW-MAD，基于欧洲空间局 SST 气候变化倡议（ESA SST CCI）数据，提供气候态基线、阈值超越、SST 异常以及按严重程度的事件分类，支持多种定义的并行分析与交叉验证。（ESSD 数据论文）', 'source': 'Earth System Science Data (ESSD)', 'url': 'https://doi.org/10.5194/essd-18-7181-2026', 'date': '2026-09-30'}, {'title': 'FY-4B/AGRI中国海域海表温度产品全面验证：精度、时空偏差与多维误差特征', 'badge': '[论文]', 'abstract': '针对中国海域 FY-4B/AGRI 海表温度（SST）产品此前缺乏系统评估的问题，研究利用 2024 年 6 月至 2025 年 5 月的 iQuam 现场数据与 Himawari-9/AHI 数据开展全面验证。结果显示产品表现优异：逐月 RMSE 为 0.650—0.863 ℃，秋—春季 R²>0.966，与 Himawari-9 一致性高（RMSE 0.795—0.971 ℃）。误差呈明显纬度依赖，近岸偏差更大，冷水中呈正偏、暖水（>28 ℃）中呈负偏，且该模式在 FY-4A/4B 间持续存在，提示存在算法层面的系统来源。', 'source': 'Geocarto International', 'url': 'https://doi.org/10.1080/10106049.2026.2736392', 'date': '2026-09-28'}, {'title': 'NOAA GOMO资助8个AI与数据管理试点：含机器学习辅助Argo质控', 'badge': '[要闻]', 'abstract': '美国 NOAA 全球海洋监测与观测计划（GOMO）公布 FY26 创新计划资助名单，共资助 8 个面向海洋观测的 AI 与数据管理试点，含合作方投入的预计总投资约 150 万美元。试点覆盖：无人载具 AI 航线规划；元数据生成自动化；观测系统数据质量控制（含机器学习辅助 Argo 质控，以减少人工时间并提升一致性）；数据可视化；以及观测对预报模式影响的评估（飓风预报影响量化、传感器缺失的 AI 虚拟试验台替代昂贵物理仿真）。项目自今年秋季启动，2028 年秋季结束。', 'source': 'NOAA GOMO / Ocean Economist', 'url': 'https://oceaneconomist.com/articles/noaa-gomo-ai-data-pilots', 'date': '2026-10-01'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'IceNest：嵌套生成式降尺度，面向导航尺度的北极海冰预报', 'badge': '[论文]', 'abstract': '北极海冰快速消退提升了高纬航道的可达性，但航线尺度规划受制于海冰密集度（SIC）预报的空间分辨率与冰缘精度——粗分辨率预报产品会抹平边缘冰区、狭窄海峡与精细冰缘特征，而这些正是识别季节性融冰/结冰期可航走廊的关键。研究提出面向导航的北极 SIC 预报框架 IceNest，可生成提前 30 天的逐日 6.25 km SIC 预报，通过耦合深度学习与嵌套生成式降尺度改善边缘带刻画与预报时效。', 'source': 'ISPRS Journal of Photogrammetry and Remote Sensing', 'url': 'https://doi.org/10.1016/j.isprsjprs.2026.09.021', 'date': '2026-09-22'}, {'title': '运动学感知AIS预处理+双向循环网络：多输出船舶轨迹预测', 'badge': '[论文]', 'abstract': '船舶轨迹精确预测对海上交通监控与管理至关重要，而 AIS 数据存在采样不均、缺失值、噪声与传输错误。研究提出两阶段框架：第一阶段以清洗、轨迹提取、运动学感知异常订正与时间重采样构建一致可分析的轨迹；第二阶段用双向门控循环单元（BiGRU）联合预测未来船位、对地航速（SOG）与对地航向（COG），并针对圆周变量 COG 设计专门的余弦距离。模型在布列斯特港与丹麦海事局（DMA）两个真实 AIS 数据集上验证，与单向 LSTM/GRU、BiLSTM 及注意力增强变体在同一预处理与训练协议下对比；消融实验证实每个预处理阶段均有可测贡献。', 'source': 'Journal of Big Data', 'url': 'https://doi.org/10.1186/s40537-026-01562-x', 'date': '2026-10-03'}, {'title': 'eDNA宏条形码高分辨率重建北极峡湾营养网', 'badge': '[论文]', 'abstract': '在快速变化的北极，研究以 Kongsfjorden 海洋生态系统为对象，用环境 DNA（eDNA）宏条形码解析群落组成与结构动态。样本通过置于鱼笼中的被动 eDNA 采样器（metaprobes）在近岸区采集，并沿峡湾中部断面拖曳采集；分别扩增线粒体 COI 与核糖体 18S SSU（V8–V9）基因，刻画后生动物与原生生物群落。群落分析显示近岸与峡湾中部站位之间差异显著（ANOSIM），表明被动采样结合宏条形码可为北极峡湾营养网提供高分辨率重建。', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-73554-z', 'date': '2026-10-01'}, {'title': '浅水海底分类进展综述：声学、光学与多源数据融合', 'badge': '[论文]', 'abstract': '浅水海底分类对海洋资源开发、生态保护与海岸工程具有关键意义。该综述系统梳理近年进展，聚焦声学技术、光学技术与多源数据融合三大核心域；为突破单一模态综述的局限，作者以统一的「数据—方法」框架组织文献，并以演化视角梳理从点式采样、常规特征分析走向面状测绘与智能方法的技术路径，为该领域提供整体性参考。', 'source': 'Journal of Sea Research', 'url': 'https://doi.org/10.1016/j.seares.2026.102753', 'date': '2026-10-01'}]}, {'title': '六、数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'CalCOFI.io发布v2026.10.01：可引用的开源版本化海洋数据库', 'badge': '[数据]', 'abstract': '加州合作海洋渔业调查（CalCOFI）的开放、版本化集成数据库发布 v2026.10.01：把 16 个来源数据集（瓶测数据库、CTD 档案、网采表格等）整合为统一模式，共 17 个数据集、23 张表、375,505,833 行、2.73 GB parquet，托管于公共存储桶并具有 DOI。配套提供浏览器端 Explorer（DuckDB 六种视图）、R 与 Python 包，以及每个数据集的可引用记录；由单一记录自动生成数据集页、元数据文档并分发至 ERDDAP、OBIS、EDI、NCEI 等门户，实现「一处撰写、处处可达」。（SIO-CalCOFI）', 'source': 'CalCOFI.io / Scripps Institution of Oceanography', 'url': 'https://calcofi.io/docs/index.html', 'date': '2026-10-01'}, {'title': 'Copernicus Marine In Situ TAC二期全体会议在罗得岛举行', 'badge': '[要闻]', 'abstract': 'Copernicus Marine In Situ TAC 2 第二阶段全体会议于 2026 年 9 月 22—24 日在希腊罗得岛举行，由希腊海洋研究中心（HCMR）承办。会议回顾服务进展并筹备后续发布，议题涵盖海浪与生物地球化学/碳产品、高频雷达观测、海冰与 UV 漂流浮标数据，以及 EMSO 与 GLOSS 数据整合；并讨论新产品、Marine In Situ 仪表盘、产品验证、质量控制与数据交付演进。会议特别强调 Copernicus Marine、EMODnet、EDITO 与 EMSO 之间日益增强的协作，尤其关注强化 EMSO 与 In Situ TAC 之间的数据流与未来数据集整合。', 'source': 'Copernicus Marine In Situ TAC', 'url': 'https://marineinsitu.eu/copernicus-marine-in-situ-tac-2-phase-ii-general-assembly-in-rhodes/', 'date': '2026-10-02'}, {'title': '科学外交「菌丝网络」：波斯湾生物多样性数据共享模式', 'badge': '[论文]', 'abstract': '在波斯湾/阿拉伯湾，跨界生态系统、迁徙物种与人为压力使保育工作分外复杂；加之基础设施不足、数据标准不一致、互操作性有限，地缘政治敏感、机构碎片化与能力不均共同构成制约跨境科学合作的复杂信任环境。研究借鉴去中心化、互惠且具适应性的「菌丝」模式，提出一套面向生物多样性数据外交的协作模型，为高敏感海域的跨境数据共享提供治理思路。', 'source': 'Marine Policy', 'url': 'https://doi.org/10.1016/j.marpol.2026.107294', 'date': '2026-10-03'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '中国第16次北冰洋考察凯旋：「雪龙」「雪龙2」双船探极成果丰硕', 'badge': '[航次]', 'abstract': '9 月 30 日，自然资源部组织的中国第16次北冰洋考察「雪龙」号、「雪龙2」号返回上海，考察规模与任务总量均创新高（集聚国内外 79 家单位 336 名队员）。本次在楚科奇海台、加拿大海盆与北冰洋中央区完成 88 个海洋综合调查站位、26 个冰站作业：在加拿大海盆 50—100 m 深处首次发现太平洋次表层暖水注入增强现象，高纬冰区发现较多极鳕幼鱼；在加克洋中脊东段海底深渊发现新的大型热液羽流区；获取跨 2500 万年时间尺度的岩石圈电性结构完整记录，发现岩石圈底部界面对约 60 km 深处近水平延伸，突破传统板块冷却模型预测。国产极地生态无人冰站、冰基海洋剖面浮标等实现规模化测试；「双龙探极」协同完成 19 个冰站作业与 95 套冰基浮标布放，构建局域无人值守观测阵列；并实现国产卫星最大纬度跨度通信（北纬 86 度至南纬 75 度）。「极地」号与「探索三号」预计 10 月中旬返航。', 'source': '自然资源部 / 新华社', 'url': 'https://m.mnr.gov.cn/dt/ywbb/202609/t20260930_2939480.html', 'date': '2026-09-30'}, {'title': '中科院海洋所「科学」轮2605航次：国庆海上科考作业持续推进', 'badge': '[航次]', 'abstract': '正在执行 2605 航次科考任务的「科学」轮于 10 月 1 日举行国庆海上升国旗等系列活动后迅即投入作业。该航次自 9 月 14 日启航以来，作业海域先后遭遇第 26、27 号台风影响，海区水文条件复杂、科考设备多系统联动、突发状况较多；在船长与首席科学家统筹指挥下，团队实时研判海况、快速调整作业方案，克服船体摇晃、长期高强度连续作业与设备突发故障等困难，保障海上科考稳步推进。', 'source': '中国科学院海洋研究所', 'url': 'https://qdio.cas.cn/2019Ver/News/PicNews/202610/t20261001_8289238.html', 'date': '2026-10-01'}, {'title': '地球物理与水下机器人测量结合：乌克兰Solotvyno盐矿灾害评估', 'badge': '[论文]', 'abstract': '西乌克兰 Solotvyno 盐矿在矿井淹水后盐岩失控溶解，带来地面沉降、天坑与蒂萨河跨界污染风险。研究采用创新性多学科方法刻画地下条件与污染通道：自主水下机器人平台 UX-1Neo 在两个淹水矿井中完成 14 次下潜，发现主井筒结构完整，但水平巷道存在令人担忧的堵塞，并识别出明显的盐跃层；研究进一步结合地球物理探测与输运/地球化学建模，评估灾害与污染路径。', 'source': 'Hydrogeology Journal', 'url': 'https://doi.org/10.1007/s10040-026-03181-5', 'date': '2026-10-02'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers & Infrastructure', 'items': [{'title': 'Copernicus第10期《海洋状况报告》(OSR10)正式发布：十年海洋监测的权威快照', 'badge': '[报告]', 'abstract': 'Copernicus Marine Service 于 9 月 30 日正式发布第 10 期《海洋状况报告》(OSR10)，纪念十年海洋监测与评估，报告发表于期刊 State of the Planet，含 18 个新同行评审章节。关键发现：2012 年以来全球平均海平面每年上升约 4.2 mm；北极 1979—2025 年月均海冰范围每十年减少约 49 万 km²（相当于每十年失去一个西班牙的面积），约 60% 北极沿海基础设施已面临侵蚀与海平面上升风险；2024 年地中海与黑海出现破纪录海洋热浪，温度较常年偏高逾 4.6 ℃，地中海 2024 年海洋热浪天数创近二十年之最；小岛屿发展中国家 65% 的专属经济区自 1999 年以来海平面上升加速。（注：09-20 期仅收录其发布预告，本期为正式发布与结论）', 'source': 'Copernicus Marine Service / Mercator Ocean International', 'url': 'https://marine.copernicus.eu/news/publication-of-10th-ocean-state-report', 'date': '2026-09-30'}, {'title': '国家海洋科学数据中心广西分中心落户南宁', 'badge': '[要闻]', 'abstract': '广西壮族自治区政协委员围绕「以科技创新推动海洋产业创新」持续建言，相关提案由自治区海洋局、科技厅、数据局等部门对接落实。数据共享层面，广西一体化智能公共数据平台已汇聚超 500 亿条政务数据，国家海洋科学数据中心广西分中心落户南宁，「海洋信息孤岛」正加速联通；算力底座方面形成「一核多点」多元算力设施布局，全区 14 个设区市均建成边缘数据中心，可支撑海洋产业多场景算力需求。', 'source': '广西政协报 / 搜狐', 'url': 'https://www.sohu.com/a/1083114606_121106875', 'date': '2026-10-01'}, {'title': '2026中国海洋经济博览会10月22日开幕：「数智深蓝」集中展示海洋数据装备', 'badge': '[要闻]', 'abstract': '2026 中国海洋经济博览会（海博会）将于 10 月 22 日在深圳开幕，主题聚焦「数智深蓝」。AI 海洋大模型、海洋卫星、水下机器人、海工装备与海上低空装备将集中亮相：中国电信、中国联通带来海洋大模型与远海组网通信等技术突破；海洋气象卫星星座、海洋数字孪生系统与各类海洋传感器为辽阔海洋构建「感知神经」。本届首次设置主宾国（法国，设 675 m² 中法联合展馆）与主宾省（海南）机制，并联动「深蓝百万里」环球科考计划等。', 'source': '香港商报', 'url': 'https://hkcd.com/hkcdweb/content/2026/10/01/content_8778070.html', 'date': '2026-10-01'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'ctdam v2.11.0：CTD数据转换、处理与绘图Python包', 'badge': '[工具]', 'abstract': '德国海洋研究联盟（DAM）CTD 软件项目发布 ctdam v2.11.0（2026-10-02）。本次更新以质量控制为核心：新增流量计（flow meter）范围限制与 QC 标志测试，并对流量异常时段内的温度、电导率与溶解氧自动打标；同时包含解析器与代码重构改进，HEX 与 CNV 解析后将自动运行流量质量检查，便于温盐深数据的批处理与审核。', 'source': 'Zenodo / DAM-CTD-Software', 'url': 'https://zenodo.org/records/22095048/latest', 'date': '2026-10-02'}, {'title': 'IOOS Code Lab v3.2.3：海洋观测数据处理开放教程与代码集', 'badge': '[工具]', 'abstract': '美国综合海洋观测系统（IOOS）发布 Code Lab v3.2.3（2026-10-02，Zenodo 归档）。该版本将预提交钩子（pre-commit）迁移至 prek，并移除大体量地图文件以精简仓库，属于面向海洋观测数据处理的开放教程与代码集合的维护版本，供社区复现与引用。', 'source': 'Zenodo / IOOS', 'url': 'https://zenodo.org/records/22117941/latest', 'date': '2026-10-02'}, {'title': 'HECO：轻量级CMEMS溢油风险评估工具', 'badge': '[开源]', 'abstract': '溢油威胁海洋生态与海岸经济，快速有效的应急响应至关重要；业务化预报模式虽精度高，却需领域专家判断环境脆弱性，这道技术门槛造成可及性缺口，可能在应急最初数小时延误情势感知，尤其影响缺乏专职技术力量的属地管理部门。HECO（Here Comes the Oil）是一个开源、基于 Python 的拉格朗日粒子扩散模型，基于 Copernicus Marine（CMEMS）数据提供轻量级溢油风险评估，以降低使用门槛、加快首响应。', 'source': 'Ocean & Coastal Management', 'url': 'https://doi.org/10.1016/j.ocecoaman.2026.108378', 'date': '2026-09-28'}]}]



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


def write_blocks_to_doc(token, doc_id, blocks, max_retries=3, batch_size=30):
    """分批写入内容块到飞书文档"""
    base_url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 分批处理
    total_batches = (len(blocks) + batch_size - 1) // batch_size
    for batch_idx in range(total_batches):
        batch_start = batch_idx * batch_size
        batch_end = min((batch_idx + 1) * batch_size, len(blocks))
        batch_blocks = blocks[batch_start:batch_end]
        
        for attempt in range(max_retries):
            try:
                payload = {
                    "blocks": batch_blocks
                }
                resp = requests.post(base_url, headers=headers, json=payload)
                resp.raise_for_status()
                print(f"Batch {batch_idx + 1}/{total_batches}: blocks {batch_start}-{batch_end-1} written successfully")
                break
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Batch {batch_idx + 1} attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"Batch {batch_idx + 1} failed after {max_retries} attempts: {e}")
                    raise
    print(f"All {len(blocks)} blocks written to document {doc_id}")


def main():
    resp = requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal", json={
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    })
    resp.raise_for_status()
    token = resp.json()["tenant_access_token"]

    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)

    print(f"Document URL: https://{TENANT_DOMAIN}/docx/{doc_id}")


if __name__ == "__main__":
    main()
