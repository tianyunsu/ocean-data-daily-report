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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'MHWCorrNet：可解释深度学习订正 ECMWF 模式，全球海洋热浪次季节预报技巧提升约 9%（JGR: MLC, 2026-09-01）', 'badge': '[论文]', 'abstract': '海洋热浪（MHW）预警需要在次季节至季节（S2S）尺度上提前数周给出可靠判断，但动力模式在该尺度上存在明显系统性偏差。中科院南海海洋所 CSTO 与 LTO 团队提出可解释深度学习后处理框架 MHWCorrNet，用于订正 ECMWF IFS 的 S2S 海洋热浪预报。结果显示，提前 1–6 周全球平均临界成功指数（CSI）较原始模式提高约 6%–12%，6 周平均提升约 9%；北、南半球中高纬提升幅度更大，分别约 15% 与 22%。空间分析显示南印度洋改善最为突出，部分区域 CSI 提升超过 0.2。更关键的是改进机制呈现纬向差异：热带海域 MHW 与非 MHW 状态的温度对比度较弱、模式更易误报，因此订正主要来自误报率下降；中高纬受中尺度涡与西边界流等局地动力过程影响、模式漏报偏多，改进则主要来自命中率提升。', 'source': 'Journal of Geophysical Research: Machine Learning and Computation（中科院南海海洋研究所）', 'url': 'https://www.gzb.cas.cn/kyj/202609/t20260901_8274884.html', 'date': '2026-09-01'}, {'title': '本体 + 多 LLM 的认知架构用于 AUV 作业共享自主：GPT-OSS 规划最优、Qwen2.5 擅任务识别（arXiv, 2026-08-29）', 'badge': '[论文]', 'abstract': '遥控潜水器（ROV）作业高度依赖操作员，而操作员常面临情境意识不足与工作负荷过高的问题。爱丁堡大学与赫瑞瓦特大学团队提出一种由领域本体与多个大语言模型组成的认知架构：每个 LLM 都通过本体获取领域知识约束，并承担单一角色，从而在任务可行性评估、任务规划与仿真执行三个阶段辅助操作员。架构支持操作员介入规划与执行环节，确保方案有效且航行器行为安全。作者对比了 Llama3、GPT-OSS 与 Qwen2.5 三种模型，发现 GPT-OSS 在可行性评估、规划与执行任务上表现最佳，而 Qwen2.5 最适合从自然语言输入中识别任务类型。该工作表明"本体 grounding + LLM 推理"的组合可使决策既扎根于领域知识，又具备通用推理能力。', 'source': 'arXiv (cs.RO) · IEEE OES AUV Symposium 2026 Southampton', 'url': 'https://arxiv.org/abs/2608.29347', 'date': '2026-08-29'}, {'title': 'SurgeGen：两阶段扩散生成框架合成风暴潮情景，支持连续风暴参数空间探索（arXiv, 2026-09-03）', 'badge': '[论文]', 'abstract': '登陆热带气旋引发的风暴潮是沿海洪水与基础设施损毁的主要来源，而 ADCIRC、SLOSH 等高保真水动力模型计算成本高昂，构建最大水位包络图（MEOW）需反复运行大量假设风暴，且只能在离散参数组合上取值。德克萨斯大学奥斯汀分校团队提出 SurgeGen：先用基线模型给出增水高度的粗略估计，再以该估计为条件驱动扩散模型生成精细化的风暴潮情景，从而在连续的风暴参数空间上条件化采样。相比 CNN、时空循环模型等确定性代理模型只能输出单一确定的增水图，SurgeGen 可生成多样化的实现以支撑不确定性分析与风险评估。实验表明该方法在训练分布内外的条件下均能生成逼真的风暴潮情景。', 'source': 'arXiv (math.DS)', 'url': 'https://arxiv.org/abs/2609.03382', 'date': '2026-09-03'}, {'title': 'EchoST-SSL：面向渔业回声探测数据的自监督时空表征学习框架（IEEE Sensors Journal, 2026-09-03）', 'badge': '[论文]', 'abstract': '回声探测数据的标注成本高，且模型跨水域、跨仪器难以直接迁移。中国水产科学研究院淡水渔业研究中心段金荣团队提出自监督时空表征学习框架 EchoST-SSL：构建时空解耦掩码自编码器，从深度维度挖掘垂直分布特征、从脉冲维度提取短时动态特征，并利用同源 50 kHz 与 200 kHz 双频探测数据开展对比学习。该框架预训练阶段无需任何生物学标签，下游评估时编码器保持冻结。在三文鱼养殖网箱数据集上，冻结表征的线性探针判别养殖病害相关声学状态的马修斯相关系数达 0.576；迁移至安徽杭埠河单频回声数据后，相邻日特征相似度均值达 0.944，并能有效捕捉梅雨降雨带来的水域声学状态变化。', 'source': 'IEEE Sensors Journal（中国水产科学研究院淡水渔业研究中心）', 'url': 'https://www.ffrc.cn/info/1084/20274.htm', 'date': '2026-09-03'}, {'title': 'RFA + RCSA 改进 YOLO11n：4.19M 参数的轻量化水下海洋垃圾检测器（Sustainability, 2026-09-02）', 'badge': '[论文]', 'abstract': '海洋垃圾威胁水生栖息地，也使港口、海床与海上基础设施的检测巡检复杂化。既有轻量化检测器面对弱纹理、边界模糊与多尺度特征杂乱时仍然脆弱，而直接扩大网络又与 onboard 算力受限相冲突。上海工程技术大学与上海理工大学团队以 YOLO11n 为基础，集成感受野聚合（RFA）模块与基于动态残差组的残差通道-空间重校正（RCSA）。实验使用公开的 15 类数据集（10,884 张训练图像、1,001 张验证图像、1,892 个标注目标），全部训练 100 个 epoch；在 42、2026、3407 三个随机种子下，验证集精确率 0.861±0.016、召回率 0.801±0.012、mAP@0.5 达 0.848±0.001。在经审计的组间不相交留出集（498 张图像、963 个实例）上 mAP@0.5 为 0.779±0.018。模型含 4.19M 参数、8.91 GFLOPs。', 'source': 'Sustainability', 'url': 'https://doi.org/10.3390/su18178986', 'date': '2026-09-02'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '本方向今日暂无新增符合时效要求的动态', 'badge': '[备注]', 'abstract': '本期检索未见新的、符合时效要求（≤14 天且不重复）的海洋数字孪生类动态。近期该方向的主要进展（如 Fugro 新加坡 AI 海洋数字孪生平台、连云港空天地一体化智慧渔港数字孪生场景）已分别在此前两期日报中收录，本期不作重复报道。', 'source': '—', 'url': 'https://tianyunsu.github.io/ocean-data-daily-report/', 'date': '2026-09-07'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': '本方向今日暂无新增符合时效要求的动态', 'badge': '[备注]', 'abstract': '本期检索未见新的、符合时效要求（≤14 天且不重复）的海洋可视化方法/工具/平台类动态。CMEMS 的 Mediterranean in Motion 交互式叙事已于 09-03 日报收录，本期不作重复报道。检索中出现的若干可视化平台资讯（如部分海岸带遥感共享系统）来源日期无法核实，按质量标准不予收录。', 'source': '—', 'url': 'https://tianyunsu.github.io/ocean-data-daily-report/', 'date': '2026-09-07'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'PhyEnv-GAN：融合船舶运动学约束与海况条件的船舶行为异常检测（Ocean Engineering, 2026-09-01）', 'badge': '[论文]', 'abstract': '船舶异常检测对海上交通安全至关重要，但既有深度学习方法普遍忽略海况影响与船舶运动学约束，容易把受风浪影响产生的正常偏航误判为异常。研究提出生成对抗框架 PhyEnv-GAN 对不同海况下正常船舶轨迹的概率分布进行建模：环境感知生成器以条件变分模块的形式，基于历史位置与海况条件重建物理上合理的轨迹；TCN 判别器通过对抗学习增强结构真实性；同时引入物理信息约束对生成过程正则化，强制运动学一致性并减少物理上不合理的输出。大量对比实验表明，PhyEnv-GAN 使正常轨迹的重构误差较既有方法降低 20%–30%，案例分析进一步验证了其对锯齿形机动与航速失配等异常行为的识别能力。', 'source': 'Ocean Engineering', 'url': 'https://www.sciencedirect.com/science/article/pii/S0029801826030842', 'date': '2026-09-01'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'S-DEIM：稀疏离散经验插值 + RNN，仅需 0.2% 格点观测即可重建高分辨率海表温度场（JGR: MLC, 2026-08-27）', 'badge': '[论文]', 'abstract': '从稀疏的海表温度（SST）观测重建高分辨率 SST 场对分析地球系统过程至关重要，但在观测稀疏时推断精度往往很差。研究提出稀疏离散经验插值法（S-DEIM）作为一种无需模型的数据同化方法：估计量由两部分构成，一部分用经验插值从瞬时原位观测直接计算，另一部分用循环神经网络（RNN）从观测的历史时间序列中学习得到。作者使用 NOAA 1989–2021 年周平均高分辨率 SST 数据集训练 RNN，在 2022 年 1 月至 2023 年 1 月的测试数据上检验：S-DEIM 仅用 100 个原位观测（占高分辨率空间网格的 0.2%）即可完成重建，精度比 DEIM、Q-DEIM 等经验插值方法高约 40%，且 91% 的估计值与真实 SST 相差在 ±1°C 以内。该方法对传感器布放位置具有鲁棒性——即使随机布放，重建误差也仅劣化 1%–2%，且 RNN 离线训练约 1 分钟、在线重建不到 1 秒。', 'source': 'Journal of Geophysical Research: Machine Learning and Computation', 'url': 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026JH001279', 'date': '2026-08-27'}, {'title': '以海滩为"标尺"：卫星岸线时间序列把近岸潮汐分辨率从 10 km 提升到 100 m（Communications Earth & Environment, 2026-09-01）', 'badge': '[论文]', 'abstract': '验潮站只能提供点位上的精确数据，而近岸区域卫星测高分辨率往往不足，导致许多沿海地区的潮汐变化难以准确把握。慕尼黑工业大学（TUM）德意志大地测量研究所与牛津大学团队提出一种新思路：不再直接测量水深，而是把海滩本身当作"标尺"——将卫星影像上可见的水边线与已知的海滩坡度相结合，从而反演海面高度并计算潮汐变化。该方法基于 NASA Landsat 与美国地质调查局超过 40 年的卫星影像，空间精度可达 100 米，而此前卫星数据只能提供约 10 公里分辨率，相差两个数量级。应用于新西兰库克海峡一段 90 公里长的海岸线时，新方法揭示出单一海湾内潮差可达近 1 米，这类小尺度差异直接决定相邻区域在同一次风暴中是否被淹没。', 'source': 'Communications Earth & Environment（TUM / University of Oxford）', 'url': 'https://www.hydro-international.com/content/news/new-method-fills-the-gaps-in-coastal-tide-monitoring', 'date': '2026-09-01'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '西班牙 MITECO 与 IEO-CSIC 签署新协议：2576 万欧元支撑 2026–2027 海洋战略科学基础（IEO-CSIC, 2026-09-01）', 'badge': '[政策]', 'abstract': '西班牙部长会议批准生态转型与人口挑战部（MITECO）与西班牙国家研究委员会（CSIC）下属西班牙海洋研究所（IEO-CSIC）签署新协议，在 2026–2027 年投入 2575.88 万欧元（其中 MITECO 海岸与海洋总局出资上限 1564.98 万欧元），用于持续开发与完善西班牙海洋战略（Marine Strategies）的科学与技术基础。该协议延续了 IEO 自 2010 年以来的工作：评估西班牙海域环境状况、制定良好环境状态的定义与环境目标，并建立周期性的监测与评估体系。IEO-CSIC 将继续执行生物多样性、栖息地、污染、海洋垃圾、水下噪声、外来入侵物种与气候变化等人类压力要素的监测计划。IEO 主任 Rosa Figueroa 指出，海洋战略是把数十年观测、海洋学考察与科学知识转化为可用信息的公共服务典范。', 'source': 'IEO-CSIC（西班牙海洋研究所）', 'url': 'https://ieo.csic.es/noticias/miteco-y-el-ieo-csic-refuerzan-el-seguimiento-cientifico-de-los-mares-espanoles-con-un-nuevo-convenio-de-cerca-de-26-millones-de-euros/', 'date': '2026-09-01'}, {'title': 'NSF 就未来海洋观测优先级公开征集意见：截止 9 月 30 日，覆盖 OOI、GO-BGC Argo 等设施（OOIFB, 2026-09）', 'badge': '[动态]', 'abstract': '美国国家科学基金会（NSF）发布 Dear Colleague Letter，就未来海洋观测系统的能力建设公开征求学界意见，征集内容包括优先事项、战略与技术方案，涉及海洋观测计划（OOI）、全球海洋生物地球化学阵列（GO-BGC Argo）、卡斯卡迪亚俯冲带观测站（COSZO）、海底地震仪中心（OBISC）等提供时间序列与长期观测的项目。 NSF 围绕观测缺口、固定与移动资产、国内国际计划协调、业务化应用与利益相关方、影响力度量，以及现有观测组合中哪些应维持或更新等问题征询回应，每个问题回复上限 3250 字符。回应截止日期为 2026 年 9 月 30 日。OOI 设施委员会（OOIFB）将在 DCL 截止前组织多场按主题划分的线上"海洋观测交流会"，并计划在 AGU 2026 年会前（12 月 4–5 日，旧金山）举办社区论坛，产出 2–4 页的行动建议摘要。', 'source': 'OOI Facility Board（NSF）', 'url': 'https://ooifb.org/news/community-input-opportunity-future-ocean-observing-priorities', 'date': '2026-09-02'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Research Vessels', 'items': [{'title': 'MBARI"海山热点"航次：ROV Doc Ricketts 在 3277 米深处拍到罕见大鳍鱿鱼（MBARI, 2026-09-02）', 'badge': '[航次]', 'abstract': '在 MBARI 旗舰科考船 R/V David Packard 执行的为期 10 天的"海山热点"（Seamount Hotspots）航次中，MBARI 科学家与 NOAA 合作者在距蒙特雷西南约 130 公里的戴维森海山附近、约 3277 米水深作业期间，用遥控潜水器 ROV Doc Ricketts 观测到一只罕见的大鳍鱿鱼（Magnapinna sp.）。全球有记录的大鳍鱿鱼观测或采集仅约 70 例，这是东北太平洋首次确认的活体观测，也是蒙特雷湾国家海洋保护区内的首次确认记录。团队用 ROV 的激光测距系统估算该个体从体顶到腕足末端长约 1.25 米。航次同时部署了多种技术手段，研究海山隆起如何偏转海流、富集营养盐并支撑繁盛生物群落，并探寻海底泥质沉积上的神秘沟槽是否由喙鲸取食造成。', 'source': 'MBARI（蒙特雷湾海洋研究所）', 'url': 'https://www.mbari.org/news/mbari-researchers-film-chance-encounter-with-a-rare-deep-sea-bigfin-squid', 'date': '2026-09-02'}, {'title': 'OSIL 发布 3.0 米海洋观测浮标：兼顾关键基础设施安防与海洋学/水质监测（Marine Technology News, 2026-09-03）', 'badge': '[动态]', 'abstract': '英国 Ocean Scientific International Ltd（OSIL）发布 3.0 米海洋观测浮标，该平台面向海军港口、关键国家基础设施、军事设施与商业港口部署，用于水面与水下的入侵监测预警，同时可支撑广泛的海洋学、气象与水质应用。平台可搭载摄像机、水听器以及伽马辐射与化学探测传感器；基于 OSIL 可定制的数据浮标平台构建，仪器可从近表层布放至海床，并支持单点、双点与顺应式系泊。为保障偏远与恶劣环境下的可靠运行，浮标可配置最多 6 块 160W 太阳能板、备用电池、导航与警示灯，遥测方式涵盖 UHF/VHF、GSM、GPRS 与卫星通信，并配套桌面或基于 Web 的数据软件。', 'source': 'Marine Technology News（OSIL）', 'url': 'https://www.marinetechnologynews.com/news/announces-marine-observation-665768', 'date': '2026-09-03'}, {'title': '美国 BGC-Argo 浮标网络面临资金中断：18 国阵列中半数由美方部署（Surfer, 2026-09-03）', 'badge': '[动态]', 'abstract': '生物地球化学 Argo（BGC-Argo）浮标可测量海洋酸化、温度、氧气与叶绿素等深层数据，并通过卫星回传，是斯克里普斯海洋研究所等机构研究海洋生态系统、天气型态及有害藻华威胁的重要数据来源。目前全球约 500 台 BGC 浮标、由 18 个国家共同维持，其中约一半由美国部署。NOAA 已非正式支持该项目 16 年，但作为 2025 年 NOAA 预算削减的一部分，联邦资金将于 10 月终止。浮标依靠浮力驱动，靠外部气囊充放气实现升降，五年的工作寿命内可下潜超过一英里、每 10 天浮出水面传输一次数据。斯克里普斯估算，维持该网络的美方成本约为纳税人每人每年 10 美分。美国海军、气象预报机构与多家研究中心均在使用该数据流。', 'source': 'Surfer（经 Yahoo 转载）', 'url': 'https://www.yahoo.com/news/science/articles/ocean-tracking-robots-going-way-203001610.html', 'date': '2026-09-03'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'EMODnet 首次纳入欧洲游艇码头数据：统一"50 泊位以上"口径并与 OSM 要素对齐（EBI, 2026-09-01）', 'badge': '[数据]', 'abstract': '欧洲海岸空间日益拥挤，若游艇码头与休闲划船活动未被纳入海洋空间规划讨论，其空间需求可能在用海分配中被忽视。此前欧洲码头数据分散在各家商业导航 App、国家登记系统与区域机构，口径、格式与语言各异，难以跨境汇总。为此，主导 EMODnet"人类活动"主题的 Cogea BIP Group 联合覆盖 11 国的 TransEurope Marinas 与欧洲船舶工业协会（EBI）启动数据汇聚与协调：各方首先统一了码头定义——包含带浮栈的干舱设施、排除无配套港口，并以 50 个泊位为阈值识别重要设施。爱沙尼亚海洋工业协会、法国休闲港联合会、英国游艇港协会与 TransEurope Marinas 率先提交数据，现已可在 EMODnet 上结合 OpenStreetMap 的点位与面要素查看。', 'source': 'European Boating Industry / EMODnet', 'url': 'https://www.europeanboatingindustry.eu/newsroom/latest-news/item/1276-european-marina-mapping-on-emodnet-supporting-effective-decision-making', 'date': '2026-09-01'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'coops-mcp 0.1.1 发布：把 NOAA CO-OPS 潮汐/水位/海流数据接入 MCP 客户端（PyPI, 2026-09-04）', 'badge': '[工具]', 'abstract': 'OceanMCP 是一组独立安装的 MCP（Model Context Protocol）服务器集合，用于让 AI 助手直接访问海洋与海岸数据。本次 coops-mcp 发布 0.1.1 版本（PyPI 记录发布日 2026-09-04），封装 NOAA CO-OPS 的数据 API、元数据 API 与衍生产品 API 三套接口，无需 API key。功能涵盖站点检索（按类型/州/坐标查找最近站点）、实时与历史水位（支持多种基准面）、调和潮汐预报（6 分钟/小时/高低潮）、气象观测（风、气温水温、气压、湿度、能见度）、PORTS 站点海流观测与预报，以及极端水位、洪水统计、海平面趋势、风暴事件与潮汐基准面等衍生产品，共 12 个工具。同仓库另有 erddap-mcp、ndbc-mcp、ofs-mcp、rtofs-mcp、ww3-mcp、goes-mcp 等 13 个已发布到 PyPI 的服务器。', 'source': 'PyPI / GitHub (oceanmodeling/ocean-mcp)', 'url': 'https://pypi.org/project/coops-mcp/', 'date': '2026-09-04'}]}]

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
