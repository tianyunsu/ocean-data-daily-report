#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接以数据对象形式定义，绕过字符串引号冲突
"""
import requests
import json
import sys
import time
import os
from datetime import datetime, timedelta

# 2026-10-18 苏老师决定整改：APP_ID / APP_SECRET 明文从公开仓库移除，
# 统一改由 _feishu_auth 供给（环境变量 > 本地 _feishu_credentials.env）。
import _feishu_auth

APP_ID, APP_SECRET = _feishu_auth.get_app_credentials()
TENANT_DOMAIN = "wcn5jx0ifkx3.feishu.cn"

if not APP_ID or not APP_SECRET:
    print("错误：未找到飞书应用凭证。请设置环境变量 FEISHU_APP_ID / FEISHU_APP_SECRET，"
          "或创建本地 _feishu_credentials.env（已在 .gitignore）。")
    sys.exit(1)

yesterday_cn = (datetime.now()).strftime('%Y年%m月%d日')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'VesselBench-800K：80 万张光学/SAR 配对影像，把海上船舶检测、计数与密度估计做成统一基准（TGRS）', 'badge': '[论文]', 'abstract': '海上船舶感知是交通监管与环境保护的基础任务，但现有数据集多做光学遥感通用目标检测，单模态在云雨、昼夜与复杂海况下明显不足。VesselBench-800K 给出目前全球规模最大的多模态船舶感知基准：80 万张 512×512 光学/SAR 配对图像，覆盖不同平台、传感器、场景、拍摄高度与合成源，空间分辨率从 4.5 m 到 0.1 m，同时支撑检测、计数与密度估计三类任务。对训练跨模态、跨分辨率的船舶识别模型，这是目前最完整的评测底座。（IEEE TGRS，Crossref 注册日 2026-11-02）', 'source': 'IEEE TGRS', 'url': 'https://doi.org/10.1109/TGRS.2026.3749162', 'date': '2026-11-02'}, {'title': 'SonarT165 + STFTrack：首个大规模水下声学目标跟踪基准，揭示现有 SOT 跟踪器的失效边界（TIP）', 'badge': '[论文]', 'abstract': '水下能见度不足时只有成像声呐能提供稳定数据，但水下声学目标跟踪（UAOT）长期缺少统一评测基准，导致传统方法与孪生网络路线之间无法比较。SonarT165 是首个大规模 UAOT 基准：165 段方形扫描序列、165 段扇形序列与 20.5 万条高质量标注，实验显示现有单目标跟踪 SOTA 在该基准上存在明显局限。配套的 STFTrack 提出多视角模板融合模块 MTFM（融合原图与动态模板二值图的多视角特征，以类跨注意力层融合）与最优轨迹修正模块 OTCM，构成完整的声学目标跟踪框架。（IEEE TIP）', 'source': 'IEEE TIP', 'url': 'https://doi.org/10.1109/TIP.2026.3747251', 'date': '2026-10-30'}, {'title': 'GLHR：分层特征聚合 + 全局到局部对齐重排序，压制复杂背景与视角尺度变化下的船舶重识别误差（TIP）', 'badge': '[论文]', 'abstract': '船舶重识别的难点在复杂背景干扰与视角、尺度变化叠加。GLHR 采用统一两阶段框架：先学层级特征表示，再做全局到局部的对齐重排序。分层特征聚合模块 HFA 协调不同网络阶段的特征并聚合成统一描述子，强制整体上下文表征与局部邻域模式之间的跨尺度几何一致性，从而在保留判别性局部细节的同时得到鲁棒全局表示；结构对齐重排序策略 GLSA 通过计算局部对齐关系进一步优化检索排序。对海上监视与船流分析这类需要跨镜头连续追踪的场景，是可复用的表示学习范式。（IEEE TIP）', 'source': 'IEEE TIP', 'url': 'https://doi.org/10.1109/TIP.2026.3744688', 'date': '2026-10-23'}, {'title': 'NeuralPOM：可微 POM 求解器 + 守恒约束神经校正器，给纯数据驱动预报补上物理守恒（arXiv）', 'badge': '[论文]', 'abstract': '粗网格环流模式依赖经验次网格参数化，难以刻画中尺度涡；纯数据驱动预报又会累积轨迹漂移、破坏示踪物守恒、阻尼小尺度变率。NeuralPOM 把 POM 的显式模态分裂与半隐式自由面实现做成可微求解器，再耦合带守恒约束的神经校正器：三维原始方程求解器推进海洋状态，网络按 1 小时（高频）或 1 天（低频）间隔在体积、热量、盐度守恒约束下更新物理场。训练用超过 10 万模式天的高分辨率双涡旋参考数据集，采用离线单步预训练、多步可微训练等三阶段流程。注意：该文目前仅有 arXiv 预印本（v1 提交 2026-11-02），尚未见刊。', 'source': 'arXiv', 'url': 'https://doi.org/10.48550/arXiv.2611.02460', 'date': '2026-11-02'}, {'title': 'EarthOracle：把「预报—观测—同化」闭环写进推理过程，治长时自回归的误差累积与气候漂移（CIKM 2026）', 'badge': '[会议]', 'abstract': '深度学习天气预报在长时自回归 rollout 中普遍出现误差累积、谱衰减与气候漂移。作者认为根因是把预报当成开环的一次性外推，而非业务数值系统固有的「预报—观测—同化」闭环。EarthOracle 是自校正地球世界模型：核心的可微数据同化模块 Diff-DA 用可学习的不确定度权重，把卫星辐射率、浮标、探空等稀疏异构观测直接注入潜状态；配合基于扰动一致性的自校正训练目标，使模型在推理过程中持续消化新观测，而不是一次性外推到底。（ACM CIKM 2026）', 'source': 'ACM CIKM 2026', 'url': 'https://doi.org/10.1145/3799682.3840988', 'date': '2026-11-03'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '海洋信息技术创新中心年度盘点：5 套数据集 + 3 个智能体，二三维一体化孪生支撑平台初步建成', 'badge': '[要闻]', 'abstract': '自然资源部海洋信息技术创新中心 2026 工作年会（10 月 27 日，广西钦州）披露年度成果：围绕智慧海洋工程技术支撑、海洋大数据分析预测增值服务、海洋信息智慧应用三条主线，研制中国全球海洋融合数据集（CGOF 1.0）、海岸带高质量样本集、防灾减灾中文指令微调数据集、海洋视频多模态数据集、遥感影像数据集共 5 套数据产品，以及海洋综合监管、船舶航行海洋环境保障、海洋专题制图 3 套智能体；初步建成二三维一体化、可定制可拓展的海洋数字孪生支撑平台，形成「平台底座—领域知识—智能体引擎—孪生应用」四层协同体系。支撑侧另建成「一张图」海洋数据分类分级体系、全国陆海垂直基准转换工具与陆海衔接的统一地理底图，并首次依托国产卫星实现跨南北极最大纬度实时通信。年度承担项目 13 项、发论文 37 篇、发布实施行标 10 项。（国家海洋信息中心）', 'source': '国家海洋信息中心', 'url': 'https://www.nmdis.org.cn/c/2026-11-02/86013.shtml', 'date': '2026-11-02'}, {'title': '田湾 200 万千瓦海上光伏的三维数字孪生管控平台：把看不见的海底地层「摊开」，并做工艺尺度推演', 'badge': '[动态]', 'abstract': '中核田湾 200 万千瓦滩涂光伏示范项目（中国规模最大的海上光伏）并网容量突破 100 万千瓦，水电水利规划设计总院受中核汇能委托牵头研发的智能建设管控平台以三维数字孪生为底座，把进度、质量、安全与船舶、人员、气象信息汇到同一张图：融合三维地理信息与 BIM 还原桩基、光伏阵列、施工船舶与监测点位的真实空间位置；用钻孔资料插值构建三维地质模型展示土层分布，并给出关注桩位的地质剖面柱状图辅助桩长与技术参数复核；质量验评按单位工程、分部、分项、检验批在线填报流转并支持电子签名；安全侧把视频监控点位关联三维场景、工作票开票到终结全程线上；接入气象站与海洋预报的风速、浪高、能见度、潮汐；再把三维模型与时间计划结合做进度仿真，对沉桩、桁架散拼、模块化吊装等关键工艺做工艺尺度三维模拟，用于方案对比推演与技术交底。（水电水利规划设计总院）', 'source': '水电水利规划设计总院', 'url': 'https://solar.in-en.com/html/solar-2465221.shtml', 'date': '2026-11-03'}, {'title': '用 ANN 替代高分辨率水动力模型跑实时：沿海淹没预警从「算不起」到分区秒级响应（Ocean Engineering）', 'badge': '[论文]', 'abstract': '沿海洪水预警系统长期依赖物理数值模型，但高分辨率降尺度计算量大，难以满足实时预报。该研究把数值模型与机器学习结合：用高分辨率水动力模型输出训练人工神经网络，把外海条件预报快速转换为分区尺度的沿海淹没指标预测，覆盖多种波浪与水位情景组合，从而在保持物理模型精度水准的同时获得接近实时的响应速度。对数字孪生/预警系统落地而言，这是把「离线高精度」与「在线快响应」解耦的典型做法：物理模型负责造样本与校验，轻量模型负责业务触发。（Ocean Engineering）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128821', 'date': '2026-11-03'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': '集合预报怎么给人看：沿海淹没的 2D 与 2D+1 可视化方案，帮预报员判趋势、找离群、估不确定性', 'badge': '[会议]', 'abstract': '集合预报能刻画模型不确定性，但预报员要在多情景、多空间尺度下凭可视化界面判断趋势、识别离群情景并评估不确定性，而地理空间集合可视化多用二维聚合指标。该会议报告给出 2D 与 2D+1 两类可视化方案，目标是帮助预报员在不同空间尺度与不同复杂度层级下目视分析沿海淹没集合模拟结果，为确定预警等级提供依据——把「算出一堆情景」转成「看得懂的一张图」，正是海洋预警可视化最缺的一环。（Visualising Climate 2026 会议报告，HAL 开放存档）', 'source': 'HAL / Visualising Climate 2026', 'url': 'https://hal.science/hal-05801805', 'date': '2026-11-04'}, {'title': 'GeoViews 1.16.0：移除 Python 3.10/3.11 支持、修 project_quadmesh 与 operation 导入缺陷，兼容 Cartopy 0.26', 'badge': '[工具]', 'abstract': 'GeoViews 是构建在 HoloViews 之上的地理数据可视化库，海洋与大气要素场绘图常用它叠 Cartopy 底图。1.16.0（10 月 24 日）为破坏性版本：移除 Python 3.10/3.11 支持与 entry point；修复 project_quadmesh 覆盖 source、.operation 导入触发 RecursiveError、线要素 Feature 默认 facecolor 等缺陷；兼容 Cartopy 0.26.0、Bokeh 3.10.0、Iris 3.15 与 PyProj 9.8，并新增 Python 3.15 支持。现场经验是：升级前先锁 Python 与 Cartopy 版本，否则容易在制图流水线上踩到版本地板。', 'source': 'GitHub / HoloViz', 'url': 'https://github.com/holoviz/geoviews/releases/tag/v1.16.0', 'date': '2026-10-24'}, {'title': 'oceanography-plotting-style：把物理海洋学出版级配图规范做成可复用的 Agent 技能包', 'badge': '[工具]', 'abstract': '一个面向物理海洋学出版级配图的复用技能包：以 Matplotlib、Cartopy 与 cmocean 为基础，把常用海洋要素图的配色、投影、色标与标注规范沉淀成可被 Agent 直接调用的技能形式（仓库 10 月 21 日创建、10 月 30 日最后更新，体量小、关注度尚低）。它的价值不在代码量，而在把反复调参的绘图细节固化——跨团队出图口径不一致，往往比算法差异更影响成果的可比性。适合作为自建配图规范的起点，而非开箱即用的成品库。', 'source': 'GitHub', 'url': 'https://github.com/Char0nChengg/oceanography-plotting-style', 'date': '2026-10-30'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'QuaSAR：海上 SAR 自监督学习先「评质」再「配比」，把数据质量变成可调参的训练变量（TGRS）', 'badge': '[论文]', 'abstract': '自监督预训练若缺少质量与多样性控制，会导致训练更久、泛化更弱；下游过度依赖高质量数据易过拟合与分布偏移，而无差别混入低质量数据又引入噪声。QuaSAR 提出质量感知的选取与配比框架：预训练阶段用多维数据评价体系与自动分类流水线筛选样本，加速并稳定表征学习；微调阶段从高、中、低质量池构造固定规模微调集，系统分析各质量层级对学习的贡献，进而导出可复现的配比方案。对海上 SAR 影像这类标注贵、质量参差的数据，「先评质、再配比」比继续堆自监督轮数更划算。（IEEE TGRS）', 'source': 'IEEE TGRS', 'url': 'https://doi.org/10.1109/TGRS.2026.3749622', 'date': '2026-11-02'}, {'title': 'ADMT-27 关键结论：Argo CTD 出厂 CPcor 自 11 月 1 日起统一改为 −11.7e-8，历史盐度数据须显式记元数据', 'badge': '[动态]', 'abstract': '第 27 次国际 Argo 资料管理组会议（ADMT-27，法国布雷斯特）披露深海 Argo 盐度质控进展：传统标准 CPcor 值（−9.57e-8）在高压环境下补偿不足，导致盐度系统性负偏差且随深度加剧；目前全球 595 个深海浮标、74,036 条剖面中约 90% 已在实时或延时模式完成 CPcor 修正，无优化值的浮标统一采用经验值 −11.7e-8。海鸟 SBE 61 实测表明新值可大幅降低盐度偏差，SBE 公司宣布自 2026 年 11 月 1 日起所有 Argo CTD 型号（SBE 41/41CP/Deep SBE 41/SBE 61、SBS 61）出厂 CPcor 校准系数统一替换为 −11.7e-8。会上另讨论 CTD 采样时序固件优化（冷区向暖区过渡的盐度尖峰改善明显、反向有限），RBR 则推出集成实时质控、盐度漂移监控与温盐一致性检验的监控面板，以缓解各 DAC 处理能力参差。凡使用历史 CTD 数据的流程，CPcor 新旧值切换必须写进元数据，否则跨航次比对会引入系统性偏差。（中国 Argo 实时资料中心）', 'source': '中国 Argo 实时资料中心', 'url': 'https://www.argo.org.cn/index.php?a=show&c=index&catid=10&id=1131&m=content', 'date': '2026-11-04'}, {'title': '巴伦支—喀拉海海冰评估：3 套再分析 + 4 套模式在同一分区上表现并不一致，全北极结论不能下推（Ocean Science）', 'badge': '[论文]', 'abstract': '巴伦支海—喀拉海是北极海冰下降与海温上升最显著的区域之一，观测稀疏使耦合模式与再分析产品成为主要工具，但模式评估多在泛北极尺度进行，分区结论可能不同。该研究以 OSI-SAF 卫星观测为基准，系统评估 1991—2020 年两个区域耦合海气模式（HIRHAM-NAOSIM 2.2、RASM）、两个 CMIP6 模式（CNRM-ESM2_1、NorESM2-MM）、两个区域海洋再分析（RARE 1.15.2、TOPAZ 4B）与一个全球再分析（ORAS5）的海冰密集度与相关变率，指出分区尺度上的能力差异，为产品选型与偏差订正提供依据。（Ocean Science，Copernicus）', 'source': 'Ocean Science', 'url': 'https://doi.org/10.5194/os-22-3537-2026', 'date': '2026-11-03'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'SWOT 重力场 + 多波束监督：ResNet 直接把西北太平洋水深预测做到 15 弧秒格网（TGRS）', 'badge': '[论文]', 'abstract': '为充分发挥多波束（MBES）对水深建模的约束能力，该研究提出基于深度残差网络的 15 弧秒格网直接水深预测框架：融合 SWOT 任务衍生的重力异常、垂直重力梯度与垂线偏差等多源重力特征，以 MBES 数据作监督，用三阶段六残差块的 ResNet 学习 160 km 以下波长重力场与地形的非线性关系，并引入 SYSU_Topo 模型提供长波背景分量。结果表明该框架能更好刻画细尺度地形、填补无船测航迹的数据空白，明显缓解缺测区的模糊效应，独立测试集上精度优于对照方案。（IEEE TGRS）', 'source': 'IEEE TGRS', 'url': 'https://doi.org/10.1109/TGRS.2026.3745627', 'date': '2026-10-23'}, {'title': '沿海声层析 + 神经网络：丽水湾用 5 站双向声传播时间反演完整三维流场（JOE）', 'badge': '[论文]', 'abstract': '沿海声层析（CAT）通过站点间双向声传播时间观测水温与流场变化。该研究在韩国丽水湾把反演分析与人工神经网络结合：以 30 分钟时间分辨率、约 100 m 空间分辨率的高分辨率沿岸海洋模式输出为主数据集，先用 Bellhop 射线追踪基于 5 个 CAT 站 15 天资料计算互易传播时间，再用斜率拟合方法扩展传播时间差样本以降低计算量；以传播时间差为输入，ANN 估计 5 个深度层的路径平均流速，最后逐层反演重建完整三维流场。这条「物理正演造样本 + 网络估路径平均 + 分层反演」的路线，对近岸低成本立体观测有参考价值。（IEEE JOE）', 'source': 'IEEE JOE', 'url': 'https://doi.org/10.1109/JOE.2026.3724238', 'date': '2026-10-30'}, {'title': '不从稀疏测量直接学声场：从亥姆霍兹方程与简正波提取结构表示，再做张量式神经重建（arXiv）', 'badge': '[论文]', 'abstract': '从稀疏测量重建三维海洋声场受高振荡波结构与受限观测路径双重制约：纯数据驱动方法不显式利用波动物理，可解释性与训练成本欠佳；物理知情方法又依赖难以获取的环境参数。该工作（arXiv 2611.01680，v1 提交 2026-11-01）改走第三条路——不求解完整波动方程，而是从亥姆霍兹方程与简正波传播中提取结构化表示，再用数据学习该表示的各个分量，实现既有物理基础、又对环境不确定性更稳健的三维声场重建。对声呐性能评估与水下通信规划，这类「物理结构先行」的建模范式值得关注。', 'source': 'arXiv', 'url': 'https://doi.org/10.48550/arXiv.2611.01680', 'date': '2026-11-01'}, {'title': 'SWOT 海面高度同化改用两步多尺度 4DVAR：先压大尺度失配，再用短去相关尺度吸收剩余信息（GRL）', 'badge': '[论文]', 'abstract': 'SWOT 提供传统测高难以采样的宽刈幅海面高度，但同化难点在于部分短波方差未必能被给定模式配置动力学表达。该研究提出两步多尺度 4DVAR 框架同化真实 SWOT 观测：第一步约束大尺度海面高度失配，第二步以第一步分析为背景、用更短的去相关尺度吸收剩余 SWOT 信息。在南海北部，该框架降低了 SWOT 残差、给出更有组织的尺度相关增量，并改善模式可分辨多尺度海面高度变率的再现与预报持续性；独立 SST、Argo 与漂流浮标观测进一步显示上层海洋改善。（Geophysical Research Letters）', 'source': 'Geophysical Research Letters', 'url': 'https://doi.org/10.1029/2026GL124606', 'date': '2026-11-03'}, {'title': 'SST 到底给叶绿素预报带来多少增量：双分支 Swin Transformer + 同口径对照，给出可归因的答案（JSTARS）', 'badge': '[论文]', 'abstract': '卫星叶绿素 a 场短期预报可支撑开阔大洋生物变率监测，但辅助海表温度带来的增量价值缺乏定量评估。该研究构建双分支 Swin Transformer，在赤道东太平洋热带不稳定波（TIW）区联合历史 Chl-a 与 SST 序列预报 Chl-a 场：独立分层编码器保留变量专属表示，瓶颈跨注意力与多尺度特征线性调制把 SST 信息注入 Chl-a 重建通路；并用共享同一 Chl-a 编解码器、峰值目标、训练日程与模型选择的对照实验，比较 CHL+SST 与仅 CHL 两种配置，同时给出持续性预报与训练期基准对照。（IEEE JSTARS）', 'source': 'IEEE JSTARS', 'url': 'https://doi.org/10.1109/JSTARS.2026.3748264', 'date': '2026-10-29'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '五项团体标准 10 月 30 日起实施：从数据元、标签、智能服务到质量评价与安全分级，给地球表层系统数据立规矩', 'badge': '[要闻]', 'abstract': '国家地球系统科学数据中心牵头制定的五项团体标准经中关村国基条件科技资源共享服务创新联盟批准发布，2026 年 10 月 30 日起正式实施。《地球表层系统科学数据元》（T/STRSA 035—2026）规定数据元描述规范与分类，划分 15 个组别并含海洋与冰冻圈专题，附标识符索引；《数据标签处理流程》（036）规范分词、停用词过滤、权重与相似度计算及标签可视化；《数据智能服务框架》（037）把服务链拆成语义查询、自动获取、就绪处理、高效计算、结果后处理与可视化响应六个模块；《数据质量评价指南》（038）建立发布前后两段式评价——发布前评数据本身，发布后结合下载量、引用率、用户反馈与应用证明，设正确性、完整性、一致性维度；《数据安全分级指南》（039）按就高从严等五项原则分四级。国家地球系统科学数据中心副主任王卷乐研究员主持研制。（国家地球系统科学数据中心）', 'source': '国家地球系统科学数据中心', 'url': 'https://www.geodata.cn/news/newsDetails.html?newsguid=277466173224030980', 'date': '2026-10-29'}, {'title': 'AquaNord-SE：88 万条瑞典湖河样本、38 项水质参数与 5 路卫星观测拼成一个纵向多模态基准（CIKM 2026）', 'badge': '[数据]', 'abstract': '可靠预测内陆水质需同时整合水质观测、卫星遥感、气象再分析与流域描述符，但面向光学复杂、季节性结冰水体的公开基准一直缺位。AquaNord-SE 给出瑞典内陆水的纵向多模态基准：2000—2025 年 18,743 个湖河监测站的 883,325 条样本，整合 SLU Miljödata MVM 的 38 项水质参数、5 路卫星传感器观测、ERA5-Land 与 MESAN 气象再分析、64 项 HydroATLAS 流域属性与 13 项派生水质指数；采用站址对齐的多模态特征集与时空档案结构，配五级模态消融设计与空间、时间、纬度三轴正交泛化切分，并给出表格模型与时空深度模型的横评基线。（ACM CIKM 2026）', 'source': 'ACM CIKM 2026', 'url': 'https://doi.org/10.1145/3799682.3840989', 'date': '2026-11-03'}, {'title': '三大文献库对 SDG 相关研究的表征仍不均衡：选哪个库，本身就在决定「什么算数」（Scientometrics）', 'badge': '[论文]', 'abstract': 'Web of Science、Scopus、OpenAlex 等大型文献数据库既是科研决策依据，也是「表演性」基础设施——其分类口径直接影响哪些成果可见、哪些主体被计量。该文考察三大库对联合国可持续发展目标（SDG）相关研究的表征，指出持续存在的不均衡与视角差异，并讨论大语言模型等 AI 工具进入科研实践后对数据库信息处理与分类环节的影响。对以文献计量做学科态势判断的团队，这是关于「数据源本身即变量」的提醒：口径不统一时，跨库比较得到的趋势差异未必来自科研本身。（Scientometrics）', 'source': 'Scientometrics', 'url': 'https://doi.org/10.1007/s11192-026-05857-x', 'date': '2026-11-02'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '「实验3」号起航出征西太平洋：台风「蔷琵」压缩作业窗口，海关一站式保障零延误', 'badge': '[航次]', 'abstract': '11 月 4 日 14 时，「实验3」号综合科考船从广州港泥洲头锚地起航，赴西太平洋执行新一轮综合科考任务。该船为我国自主建造的远洋综合科考船，长期承担南海、西太平洋、印度洋的海洋环境、生态资源与海气相互作用调查。船长李伟表示本次聚焦西太平洋关键海域开展多维度任务研究，海上观测窗口不可复制；受超强台风「蔷琵」影响航次被迫延后，剩余作业窗口十分紧张。黄埔老港海关提前掌握航行计划、安排专人全程跟踪，一站式办结兼营船舶转国际运输、船舶免予卫生控制措施证书更新与出境核验等业务，压缩待港时间。该关已完成「实验1」「海洋地质六号」等科考船进出境监管 11 艘次。（中国新闻网）', 'source': '中国新闻网', 'url': 'https://www.chinanews.com/gn/2026/11-04/10726189.shtml', 'date': '2026-11-04'}, {'title': '把报废的金枪鱼探鱼浮标改造成观测平台：西印度洋试点导出 393 条声学记录与 1,281 条分层生物量观测（Sci Rep）', 'badge': '[论文]', 'abstract': '工业金枪鱼渔业用的声学探鱼浮标在寿命末期通常报废，但其回声探测能力可直接转为海洋观测平台。该技术转移与试点可行性研究通过 Satlink 的 ReCon 项目，把翻新浮标以固定点与漂流两种方式布放在西印度洋莫桑比克 Bazaruto 群岛的一个陆架试验区、两处珊瑚礁与两处海山/尖峰系统：固定点声学记录跨度 51.5—96.2 小时/站点，固定与漂流合计导出 393 条带时间戳声学记录、1,281 条按深度分层的相对声学生物量与后向散射观测，并附浮标位置与声学数据。对观测稀疏的西部印度洋，这是低成本扩容观测网的一条现实路径，也提示渔业现有装备的二次利用价值。（Scientific Reports）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-72665-x', 'date': '2026-11-03'}, {'title': '矢量推进 AUV 的三维轨迹跟踪：主动洋流抑制视线律 + 超螺旋观测器 + 优先级推力分配（RA-L）', 'badge': '[论文]', 'abstract': '鱼雷型 AUV 高速巡航效率高但低速时舵效下降、机动性变差；矢量推进可在不加辅助推进器的情况下改善低速机动，却带来欠驱动、水动力不确定、未知海流与执行器饱和等叠加难题。该文提出分层制导—控制—分配框架：制导层以路径跟随 LOS 为启发，构造主动洋流抑制视线（AOCRLOS）律，用统一三维形式而非解耦平面子系统处理三维轨迹跟踪，并证明制导误差动态一致全局渐近稳定；动力学层用带超螺旋扰动观测器的反步控制器增强抗扰；分配层用优先级驱动的矢量推力分配（PDVTA）处理执行器约束。（IEEE RA-L）', 'source': 'IEEE Robotics and Automation Letters', 'url': 'https://doi.org/10.1109/LRA.2026.3747613', 'date': '2026-10-26'}, {'title': 'PPAP：把「扫完全场」和「盯住目标」统一进一个强化学习策略，效率比割草机式覆盖高 15%—20%（JOE）', 'badge': '[论文]', 'abstract': 'AUV 做近岸底栖监测时，系统化区域覆盖与对感兴趣生态特征的适应性调查常被视为竞争目标，导致稀疏底栖环境下资源利用低效。PPAP 是基于强化学习的自适应信息路径规划框架，通过把环境信息做直观的 HSV（色相—饱和度—明度）编码，并设计平衡两类目标的奖励机制，把覆盖完成与目标聚焦信息采集统一到同一策略中。与割草机式覆盖模式的对比数值实验显示，在多种环境尺度下 PPAP 效率比系统化基线高约 15%—20%，覆盖检测性能相当或更优；在预算收紧时，PPAP 是唯一能取得非零回合的方法。（IEEE JOE）', 'source': 'IEEE JOE', 'url': 'https://doi.org/10.1109/JOE.2026.3726174', 'date': '2026-10-22'}]}, {'title': '八、海洋数据中心与算力', 'en': 'Ocean Data Centers', 'items': [{'title': '全国首个海上算力联盟落地珠海：25 家单位发起，提「海底—岛端—岸基」三级算力协同', 'badge': '[要闻]', 'abstract': '11 月 2 日，Token 算力驱动国际数字经济发展峰会在横琴粤澳深度合作区举行，全国首个海上算力联盟——港珠澳琴海上算力联盟成立并落地珠海：由粤港澳及海上算力领域 25 家企业、科研院校、金融机构与行业组织联合发起，曙光信息产业股份有限公司与南方海洋科学与工程广东省实验室（珠海）任双组长单位。成员含中国移动、中国电信、中国联通三大运营商，国家电投、大唐集团珠海公司等能源基建力量，阿里千问办公、澳门电讯等数字化企业，以及中山大学广州超算中心、澳门科技大学等科研机构。联盟宣言提出海底算力、岛端算力、岸基智算三级协同，打通「陆数海算」「澳数珠算」「港数珠算」通道；三大任务为加快海上算力中心硬件建设、推动上游全链条协同、结合数据跨境试点形成算力出海能力。脉络上，珠海 6 月发布「海上新基建」行动方案、7 月「风算一体」海底算力中心签约、10 月桂山岛岛礁连廊海底算力中心项目签约。（珠海特区报）', 'source': '珠海特区报', 'url': 'https://pub-zhtb.hizh.cn/a/202611/04/AP6aea0b61e4b02381c6bfa154.html', 'date': '2026-11-02'}, {'title': '中国—岛屿国家海洋合作论坛：海岛资源共享平台与《海平面上升状况 2026》同台发布，配套三年行动清单', 'badge': '[动态]', 'abstract': '11 月 4 日，中国—岛屿国家海洋合作论坛在福建平潭举行，自然资源部海岛研究中心发布《中国和美海岛建设阶段性成效报告》：首批 33 个和美海岛三年建设中，超 70% 的受损生态区域得到修复，半数和美海岛清洁能源消费占比超 60%，30 个海岛饮用水安全覆盖率超 90%，建成国家级与省级海洋牧场示范区 30 余个。论坛发布《中国—岛屿国家海洋防灾减灾合作举措清单（2026—2028）》，围绕海洋环境观测预报、灾害预警监测、生态系统保护修复、蓝色经济发展、人才培养与能力建设五大主题开展合作。会上国家海洋信息中心主任石绥祥、国家卫星海洋应用中心副主任尚文艳、国家海洋环境预报中心副主任原野等分别以《气候变化下岛屿国家海平面上升状况 2026》《岛屿国家珊瑚礁白化卫星监测预警产品》《「妈祖」系列海洋数值预报模式》与《海岛资源共享平台》为题作报告；联合国「海洋十年」「海岛治理工具包」与「加勒比海域海洋空间规划与蓝色经济融合」项目完成签约。（平潭综合实验区管委会）', 'source': '平潭综合实验区管委会', 'url': 'https://www.pingtan.gov.cn/zwgk/yw/ptyw/202611/t20261105_109871.htm', 'date': '2026-11-04'}, {'title': '珊瑚礁白化预警产品面向全球岛屿国家开放：5 km、每日更新，海温精度误差小于 0.7 ℃', 'badge': '[要闻]', 'abstract': '11 月 4 日，国家卫星海洋应用中心正式发布《岛屿国家珊瑚礁白化卫星监测与预警产品》，面向全球岛屿国家开放共享：覆盖西太平洋、东太平洋、加勒比海、西印度洋、东印度洋与热带东大西洋六大重点区域，空间分辨率 5 km、每日动态更新；融合海洋一号、海洋二号系列卫星与国际卫星观测数据，海温监测精度误差小于 0.7 ℃，产出海温异常、海温趋势、热点指数、周热度与区域白化预警等级五类核心产品，打通风险识别—强度评估—预警发布链条。2025 年 4 月该产品捕捉到罗德里格斯岛热周峰值 11.14 degree-weeks 并连续 30 天维持二级预警，与国际同类产品高度一致。产品已通过国家卫星海洋应用中心数据服务系统向全球开放，支持实时下载与每日更新，并可用于海洋保护区规划、渔业管理与气候影响评估。背景数据：第四次全球白化事件（2023 年初—2025 年中）影响全球 84% 的礁区、82 个国家和地区。（国家卫星海洋应用中心 / 海洋卫星）', 'source': '国家卫星海洋应用中心', 'url': 'https://www.163.com/dy/article/LAUEB5O10511KMS0.html', 'date': '2026-11-04'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'ctdcast v0.4.1：船载 CTD/LADCP 一站式出「自包含 HTML 报告」，图件全部内嵌 base64', 'badge': '[工具]', 'abstract': 'ctdcast 是船载 CTD 与 LADCP 数据的处理与报告生成工具，v0.4.1（11 月 1 日，Zenodo 存档；作者 Eleanor Frajka-Williams（汉堡大学海洋研究所）与 Angel Ruiz-Angulo（冰岛大学地球科学研究所））把原始仪器文件转换为经质控、符合 CF/CCHDO 规范的 netCDF 与合并剖面网格，并生成完全自包含的 HTML 报告——所有图件以 base64 data URI 内嵌，产出按站位的单 cast 页面、断面剖面页与全航次时间序列页。对既要在船上快速出报告、又要保证数据规范化的航次，这种「处理口径与报告形态一体化」的设计很实用。', 'source': 'Zenodo', 'url': 'https://zenodo.org/records/23861916', 'date': '2026-11-01'}, {'title': 'Copernicus Marine Toolbox v2.5.1：维护性补丁，同日跟进 post1 修文档索引', 'badge': '[工具]', 'abstract': 'Copernicus Marine Toolbox（CLI + Python 客户端，用于检索、子集化与下载 CMEMS 产品）发布 v2.5.1（11 月 3 日），同日跟进 v2.5.1.post1，修复变更日志未进文档索引的问题；PyPI、conda 与官方二进制作同步更新。发布说明中未见功能性变更，属维护性补丁。对需要长期复现的海洋数据流程，建议固定到具体版本号而非跟随 latest，避免补丁版本引入的非预期差异。', 'source': 'GitHub / Mercator Ocean', 'url': 'https://github.com/mercator-ocean/copernicus-marine-toolbox/releases/tag/v2.5.1', 'date': '2026-11-03'}, {'title': 'erddapy v3.3.2：新增实验性构建信息，无 API 破坏性改动', 'badge': '[工具]', 'abstract': 'erddapy（IOOS 维护的 Python ERDDAP 客户端，用于数据集搜索、元数据获取、子集下载与图件生成）发布 v3.3.2（11 月 4 日），本次变更主要为新增实验性构建信息（experimental build info），未见 API 破坏性改动。对依赖 ERDDAP 批量取数的海洋数据流水线，属安全的例行升级；若下游脚本依赖构建信息字段做版本判别，需注意该字段仍标记为实验性、格式可能变化。', 'source': 'GitHub / IOOS', 'url': 'https://github.com/ioos/erddapy/releases/tag/v3.3.2', 'date': '2026-11-04'}]}]



def tr(text, bold=False, link=None):
    # 2026-10-18 修复：加粗与超链接必须放在 text_element_style 里。
    # 旧写法 text_run["style"] / text_run["link"] 均非合法字段，飞书静默忽略不报错，
    # 结果文档无加粗、无超链接（回读 text_element_style 全空）。
    style = {}
    if bold:
        style["bold"] = True
    if link:
        style["link"] = {"url": link}
    element = {"text_run": {"content": text}}
    if style:
        element["text_run"]["text_element_style"] = style
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


def find_existing_doc(token, title):
    """在云空间里查找同名文档（分页拉全量 docx 后精确匹配标题）。

    2026-10-18 新增：修复「每次运行都新建文档」导致的堆积问题
    （清理前云盘里已有 137 个日报文档，其中 89 个是同一天重复建的）。
    """
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    files, page_token = [], ""
    while True:
        params = {"page_size": 200}
        if page_token:
            params["page_token"] = page_token
        d = requests.get("https://open.feishu.cn/open-apis/drive/v1/files",
                         headers=headers, params=params, timeout=30).json()
        if d.get("code") != 0:
            print(f"列文件失败，按新建处理: code={d.get('code')} msg={d.get('msg')}")
            return None
        data = d.get("data", {})
        files.extend([f for f in data.get("files", []) if f.get("type") == "docx"])
        if not data.get("has_more"):
            break
        page_token = data.get("next_page_token")
    for f in files:
        if f.get("name") == title:
            return f["token"]
    return None


def clear_doc_children(token, doc_id):
    """清空文档正文（只留页面根块），供同日复用时重写。"""
    headers = {"Authorization": f"Bearer {token}",
               "Content-Type": "application/json; charset=utf-8"}
    # 先数一下现有子块数量
    items, page_token = [], ""
    while True:
        params = {"page_size": 500}
        if page_token:
            params["page_token"] = page_token
        d = requests.get(f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks",
                         headers=headers, params=params, timeout=30).json()
        if d.get("code") != 0:
            return False
        data = d.get("data", {})
        items.extend(data.get("items", []))
        if not data.get("has_more"):
            break
        page_token = data.get("next_page_token")
    root = next((b for b in items if b.get("block_type") == 1), None)
    n_children = len(root.get("children") or []) if root else 0
    if n_children == 0:
        return True
    r = requests.delete(
        f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children/batch_delete",
        headers=headers, json={"start_index": 0, "end_index": n_children}, timeout=30)
    body = r.json()
    if r.status_code != 200 or body.get("code") != 0:
        print(f"清空旧内容失败: HTTP {r.status_code} code={body.get('code')} {body.get('msg')}")
        return False
    print(f"已清空旧内容 {n_children} 块")
    return True


def create_document_and_write(tenant_access_token):
    """同日已有文档则复用（清空重写），否则新建。避免文档堆积。"""
    title = f"海洋AI技术日报 {datetime.now().strftime('%Y-%m-%d')}"
    existing = find_existing_doc(tenant_access_token, title)
    if existing:
        print(f"复用当天已有文档: {existing}")
        if clear_doc_children(tenant_access_token, existing):
            return existing
        print("复用失败，改走新建")
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    payload = {"title": title}
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
    # 2026-10-18 修复：写入端点漏了 /{block_id}/children。
    # 错误写法 POST .../documents/{doc_id}/blocks            -> 404
    # 正确写法 POST .../documents/{doc_id}/blocks/{doc_id}/children
    # （doc_id 即页面根块 block_id，用 children 追加到文档末尾）
    base_url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children"
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
                    "children": batch_blocks
                }
                resp = requests.post(base_url, headers=headers, json=payload)
                resp.raise_for_status()
                # 2026-10-18 补强：HTTP 200 不代表业务成功，必须校验 code
                body = resp.json()
                if body.get("code") != 0:
                    raise RuntimeError(f"Feishu API 业务错误 code={body.get('code')} msg={body.get('msg')}")
                print(f"Batch {batch_idx + 1}/{total_batches}: blocks {batch_start}-{batch_end-1} written successfully")
                break
            except (requests.exceptions.RequestException, RuntimeError) as e:
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

    doc_url = f"https://{TENANT_DOMAIN}/docx/{doc_id}"
    print(f"Document URL: {doc_url}")
    # 2026-10-18 修复：run_daily_report.py 依赖「stdout 含 SUCCESS」+「feishu_doc_url.txt」
    # 两个信号，旧版均未输出，导致上层永远判定文档链路失败。
    with open("feishu_doc_url.txt", "w", encoding="utf-8") as f:
        f.write(doc_url)
    print("SUCCESS Feishu document written.")


if __name__ == "__main__":
    main()
