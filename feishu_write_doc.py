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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'FASST：把大气与海冰换成 U-Net 代理、只保留 POP2 海洋，跑通 140 年自由耦合积分（NeurIPS 2026 CCAI Workshop）', 'badge': '[会议]', 'abstract': '耦合气候模拟的计算瓶颈主要在大气模块。FASST 保留具有预报能力的 POP2 海洋模式，用轻量 U-Net 代理替换大气与海冰：大气代理为诊断型，每 6 个模拟小时由不断演化的海洋—海冰状态预测地表通量；海冰代理按月推进。140 年无外强迫积分中，FASST 在不做海表温度恢复的情况下维持稳定全球平均气候态，平衡后全球平均 SST 为 291.30±0.22 K（CESM2 piControl 为 291.25±0.10 K）；亦能再现 Niño-3.4 区年际变率，但振幅偏弱（0.62 K 对 1.02 K）。结果表明无显式状态变量的学习型大气足以支撑百年尺度自由耦合积分。（NeurIPS 2026「Tackling Climate Change with Machine Learning」Workshop；arXiv v1 2026-10-26）', 'source': 'NeurIPS 2026 Workshop / arXiv', 'url': 'https://arxiv.org/abs/2610.36297', 'date': '2026-10-26'}, {'title': 'GAP：用共享概率表征把数据同化、天气预报与气候模拟接成一套生成式框架（npj Climate and Atmospheric Science）', 'badge': '[论文]', 'abstract': '机器学习天气预报在两周尺度上已超过过程模式，但多数方法没有把数据同化真正纳入预测流程，且自回归误差累积限制了其在延伸期与气候投影上的适用性。该文提出生成式同化与预测（GAP）：从再分析数据学习大气状态的气候学分布，再按观测、预测与外强迫三类约束适配到不同任务，用同一个共享概率表征连接同化、预报与气候模拟。作者在跨天气—气候的多类任务上评估了该框架，意图绕开自回归长程积分的误差累积。（npj Climate and Atmospheric Science，Nature 系；2026-11-02）', 'source': 'npj Climate and Atmospheric Science', 'url': 'https://doi.org/10.1038/s41612-026-01585-4', 'date': '2026-11-02'}, {'title': '九结构地标替代旋转框：光学遥感定向船舶检测绕开角度周期性与长宽比敏感（IEEE TIP）', 'badge': '[论文]', 'abstract': '遥感船舶检测是海洋监测与海上交通管理的基础，但水平框（HBB）引入过多背景噪声、有向框（OBB）受角度周期性不连续与长宽比高敏感困扰。该文先按船舶功能形态提出九关键点结构表征，把船艏、船艉与上层建筑的关键区域作为显式几何先验；再在此表征上构建两阶段框架，用 HBB 检测器粗定位后完成高精度 OBB 检测与语义分割。为复杂海面场景下的舰船定向检测提供了不依赖角度回归的新路径。（IEEE Transactions on Image Processing，2026-11-06）', 'source': 'IEEE TIP', 'url': 'https://doi.org/10.1109/TIP.2026.3748963', 'date': '2026-11-06'}, {'title': 'RPCA 多时相 Sentinel-2 融合 + Geo-MSENet：光学复杂近岸测深 RMSE 0.60–1.23 m（IEEE JSTARS）', 'badge': '[论文]', 'abstract': '浅水近岸测深对航行与工程规划关键，却受传统测量成本与光学复杂水体限制。该框架先用鲁棒主成分分析（RPCA）融合多时相 Sentinel-2 影像，抑制太阳耀斑、船迹等瞬态扰动；再用轻量卷积网络 Geo-MSENet，结合融合影像与地理坐标，通过多尺度提取与注意力机制反演水深。在中国三处近岸海域以声呐数据（0–20 m）验证，RMSE 分别为 0.60 m、0.81 m、1.23 m，较五个基准模型降低 25–55%。（IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing，2026-11-06）', 'source': 'IEEE JSTARS', 'url': 'https://doi.org/10.1109/JSTARS.2026.3751362', 'date': '2026-11-06'}, {'title': '发改委「人工智能+」与海洋经济发布会：2030 年海洋生产总值剑指 13 万亿元，盘古海洋预报大模型工程化落地', 'badge': '[政策]', 'abstract': '11 月 3 日国家发展改革委新闻发布会上，区域协调发展司提出「十五五」在新科技、新产业、新空间三方面发力，到 2030 年我国海洋生产总值预计突破 13 万亿元、海上风电累计并网装机 1 亿千瓦以上，并一体谋划近岸、远洋、极地、深海的保护开发利用。创新和高技术发展司同场明确深化拓展「人工智能+」行动，优先在矿山开采、高空作业、应急救灾等场景组织应用攻关，并推进人工智能基础性综合性立法与「监管沙盒」。据发布会配套报道，全国首个深度融合 AI、全栈国产算力支撑的盘古海洋智能预报大模型已工程化落地，目标把海洋预报从天级压缩到分钟级。（新华社 / 求是网，发布会 2026-11-03）', 'source': '新华社 / 求是网', 'url': 'http://qstheory.com/20261104/e414f4d8f3e84e0ebe320994bc2a0170/c.html', 'date': '2026-11-03'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': 'OCEAN-X 启动：六个大西洋岛国与沿岸国共建马卡罗尼西亚首个一体化海洋数字孪生（240 万欧元 / 3 年）', 'badge': '[动态]', 'abstract': '在加那利群岛海洋平台（PLOCAN）牵头下，加那利、亚速尔、马德拉、佛得角、塞内加尔、圣多美和普林西比六方联合启动欧盟 INTERREG VI-D MAC 计划下的 OCEAN-X 项目，预算 240 万欧元、周期三年，将交付马卡罗尼西亚首个一体化「海洋数字孪生」。技术路线把原位与同步观测、高分辨率数值模式和 AI 结合，由区域内可移动的与固定的自主海洋平台集群实时产出符合 FAIR 原则的数据，与历史序列一同驱动高分辨率模式，基于统一数据库构建模块化数字孪生操作界面，并以亚速尔、马德拉、加那利三个用例落地，可向东中大西洋扩展。（PLOCAN / Environment Coastal & Offshore，2026-11-05）', 'source': 'PLOCAN / eco magazine', 'url': 'https://ecomagazine.com/news/research/ocean-x-project-launches-digital-twin-of-the-ocean-for-macaronesia/', 'date': '2026-11-05'}, {'title': 'FIO-AOW 第三代台风模式落地南海局超算：常态化 120 小时台风与海气极端环境预报', 'badge': '[要闻]', 'abstract': '自然资源部第一海洋研究所乔方利团队研发的自主可控新型台风业务预报模式 FIO-AOW，在南海局超算平台正式落地运行，可常态化开展未来 120 小时台风及海气极端环境预测预报。该模式从湍流角度构建海浪影响台风的理论体系，实现从「海—气耦合」到「海浪—海洋—大气相互作用」的跨越，针对长期存在的「弱台风偏强、强台风偏弱」难题。在 2612 号台风「红霞」检验中，近海快速强化过程的 24 小时强度增幅预报与实况仅差 0.2 m/s、峰值风速误差 0.8 m/s；双方联合检验成果发表于《Ocean Modelling》。（自然资源部南海局，2026-11-02）', 'source': '自然资源部南海局', 'url': 'https://scs.mnr.gov.cn/scsb/fjdt/202611/10d58a418365499380b0820a9b7cf47d.shtml', 'date': '2026-11-02'}, {'title': '认知数字海洋（CDO）第二部分：量子混合计算 + 数字孪生层级 + 图神经网络管渔业与船队', 'badge': '[论文]', 'abstract': '该文提出认知数字海洋（CDO）概念——面向渔业综合体的多层信息物理系统，整合量子混合计算、物理信息神经网络（PINN）、图神经网络（GNN）、从基因组到全球海洋的数字孪生层级，以及生物资源空间分布的分形分析。论文着墨于造船维度，给出船舶动力装置、可调螺距螺旋桨、推进综合体与船体水动力学的数学模型，并讨论在量子计算机上求解 Navier–Stokes 方程对最长 30 天水动力预报 horizon 的可能影响；系统面向俄罗斯联邦渔业署 2030 年前增产 25%、数字化转型与技术主权目标，同时列出量子方法的适用边界与工程绕行方案。（Fisheries，2026-11-02）', 'source': 'Fisheries', 'url': 'https://doi.org/10.36038/0131-6184-2026-5-60-69', 'date': '2026-11-02'}, {'title': 'CMIP6 大集合检验「秋季北大西洋 SST → 冬季 NAO」：模式普遍把海气耦合因果方向模拟反了', 'badge': '[论文]', 'abstract': '观测研究提示秋季北大西洋海表温度异常与冬季北大西洋涛动（NAO）位相存在因果联系，但季节预测模式普遍低估该联系。该文用 ERA5 再分析与 CMIP6 历史大集合检验秋冬大气—海洋变率表征：模式能再现秋冬同季内主要由大气驱动的海气协变，但秋季 SST—冬季平均海平面气压的协变主模态与 ERA5 不同——ERA5 中秋季北大西洋中部暖异常领先冬季正 NAO，而 CMIP6 集合平均表现为弱的秋季冷异常领先正 NAO 且模式间离散很大；作者进一步用大气相似法分离大气驱动与海洋驱动分量。对孪生/集合模拟的偏差归因给出了明确诊断口径。（Weather and Climate Dynamics，Copernicus，2026-11-05）', 'source': 'Weather and Climate Dynamics', 'url': 'https://doi.org/10.5194/wcd-7-2155-2026', 'date': '2026-11-05'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Data Visualization', 'items': [{'title': 'Abyssal Claims v1.8：50 个海域 + 13 个陆域图层的三维集成平台，首次把 2433 万条浮游生物记录与格点场背后的原始观测同屏', 'badge': '[工具]', 'abstract': '这个独立开发的非商业 Web 平台把五十余套公共资助环境数据集放到同一张交互式三维地图上，从深海采矿起步扩展到海洋与陆域数据。v1.8（2026 年 11 月，生产快照 11-04）新增/纳入：2433 万条 OBIS 浮游生物记录（1566 个数据集，可按类群、年代、深度与 eDNA 过滤）、GLODAPv3 的 75102 条采水瓶次、SOCAT v2026 的 4401.8 万条表层 CO₂ 观测（8310 个航次）、WOD 2023 的 743.5 万条剖面、39.2 万条 BGC-Argo 氧气剖面，以及 CoastDOM 7.08 万份沿岸溶解有机物样品。四个格点场（GLODAP、SOCAT、世界海洋图集、海洋溶氧）新增「按各数据源自身质量规则绘制原始观测」的第三种视图；地址栏携带相机、图层、筛选、显示设置与打开记录，复制 URL 即可复现同一视图；另建 9201 个 GLODAP/SOCAT 航次页与默认开启的三维海山、热液喷口模型。v1.8 同时更正了 v1.7 数据清单中的许可错误（如 OceanOPS 为保留部分权利、允许非商业使用，非 CC-BY）。（Zenodo 概念记录，v1.8，2026-11-04）', 'source': 'Zenodo / Abyssal Claims', 'url': 'https://doi.org/10.5281/zenodo.19745884', 'date': '2026-11-04'}, {'title': '陆—水界面拼接：GNSS + 测深 + ADCP 生成连续「顶测深」剖面，把多瑙河三角洲河床与岸坡统一到同一坐标系', 'badge': '[论文]', 'abstract': '陆水交界面的地形采集是打通陆地地形与水文测深两套数据集的前提；多瑙河三角洲河道地貌动态变化、水位波动显著，很难给出统一表达。该研究提出一套拼接方法：陆地侧用 Trimble R980/R12/R4 接收机以 RTK 模式接入罗马尼亚 ROMPOS 永久站网，每点三次观测、卫星几何不佳处延长采样；水上侧沿预设断面测深，并用 ADCP 基于多普勒效应测量高精度三维流速与流量。关键一步是以 GPS 观测到的陆水界面高程为基准把水深换算成地形高程，把水下河床与出露岸坡统一进 STEREO 70 平面坐标与黑海 1975 垂直基准，生成连续的高分辨率水陆一体剖面，用于分析河床形态演化及流场、输沙与地形配置的相互作用，支撑三角洲生态系统保育与可持续管理。（Inżynieria Mineralna，2026-11-01；该刊尚未登记分级，待校准）', 'source': 'Inżynieria Mineralna', 'url': 'https://doi.org/10.29227/im-2026-02-02-003', 'date': '2026-11-01'}, {'title': '海滩垃圾「足迹」：七个来源相关子指标同时刻画尺寸与来源，可输出足迹图、细分辨率地图与垃圾曲线', 'badge': '[论文]', 'abstract': '公众、科研与政府机构积累了大量海滩大型垃圾清单数据，但多数海岸环境状态评估只用垃圾件数总量，浪费了尺寸与类型信息。该文提出海滩垃圾足迹（Beach Litter Footprint）多维指标，由七个与来源相关的子指标构成，同时考虑垃圾尺寸与潜在来源，可依用途表现为足迹可视化、细分辨率地图或垃圾曲线，从而给出更具诊断力的海岸状态判读与更有针对性的管理指引；研究在伊比利亚、巴利阿里与马卡罗尼西亚区域做了设计与业务化测试。（Ecological Indicators，Elsevier，2026-10-28）', 'source': 'Ecological Indicators', 'url': 'https://doi.org/10.1016/j.ecolind.2026.115751', 'date': '2026-10-28'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': '独立测深数据揭穿卫星测深「深水精度高估」：主被动融合 FCNN 内部验证 RMSE 1.50 m，独立验证 3.70 m 且负偏差显著', 'badge': '[论文]', 'abstract': '以 ICESat-2 激光种子点与多光谱影像做主被动融合的卫星测深（SDB）已有广泛应用，但不少研究的精度指标仅来自内部验证——训练与验证都基于同一批 ICESat-2 种子点。该文在两处热带近岸水域对 FCNN 型 SDB 模型做内部与独立验证对比：在超出被动光学测深极限、但仍处 ICESat-2 覆盖深度的范围（万宁 18.78–25.05 m、瓦胡岛 21.10–27.23 m），内部验证 RMSE 为 1.50 m 与 2.25 m，独立验证则为 3.70 m 与 3.40 m，且负偏差明显更强。结论是仅由卫星输入导出并验证的主被动融合产品及其精度，会显著高估深水性能；既有光学测深深度适用界限需要重新审视。（IEEE Geoscience and Remote Sensing Letters，2026-11-06）', 'source': 'IEEE GRSL', 'url': 'https://doi.org/10.1109/LGRS.2026.3750909', 'date': '2026-11-06'}, {'title': '卫星重力去混叠：海洋底压对大气强迫与海洋模式垂向分辨率的敏感性量化（LICOM3.0 三组试验）', 'badge': '[论文]', 'abstract': '卫星重力月解需去混叠产品抑制高频质量变化混叠，其中海洋分量不确定性通常大于大气分量，而大气强迫与海洋模式垂向分辨率这两个限制因素长期缺乏量化。该文用 LICOM3.0 环流模式，以 ERA5 与 CRA-40 两套大气再分析、30 层与 80 层两套垂向配置，构成 ERA5-L30、ERA5-L80、CRA-40-L80 三组全球海洋底压（OBP）模拟，并与实测 OBP 记录比对。结果显示在短周期海洋质量变化上，垂向分辨率的影响总体大于大气强迫，为去混叠产品的误差预算与模式配置选择提供了直接依据。（IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing，2026-11-03）', 'source': 'IEEE JSTARS', 'url': 'https://doi.org/10.1109/JSTARS.2026.3750208', 'date': '2026-11-03'}, {'title': '多 GNSS-R 海面风速「异质信号 → 一致风场」：CYGNSS / 风云三号 / 天目一号分组随机森林融合', 'badge': '[论文]', 'abstract': 'GNSS 反射测量（GNSS-R）以低成本获得密集时空采样的海面风场，多系统观测进一步改善采样，但任务、发射信号与接收平台之间的差异限制了一致的多源反演与融合。该文用 CYGNSS、FY-3 与天目一号观测构建海面风速反演与融合框架：为降低系统内异质性，采用分组随机森林策略，按发射 GNSS 星座与接收 GNSS-R 卫星分别建模，再在系统层合并子组结果；分组模型的均方根误差优于不分组方案。为跨星座海面风产品的一致性处理给出可复用路径。（Geo-spatial Information Science，Taylor & Francis，2026-10-29）', 'source': 'Geo-spatial Information Science', 'url': 'https://doi.org/10.1080/10095020.2026.2753898', 'date': '2026-10-29'}, {'title': '高光谱 + LiDAR 分类滨海湿地：把「跨模态差异」当作引导信号而非噪声（DGMF-Net）', 'badge': '[论文]', 'abstract': '滨海湿地分类对生态保护与环境管理重要，高光谱影像（HSI）与 LiDAR 融合潜力已获公认，但湿地地类复杂、光谱混淆严重、空间结构破碎，导致跨模态差异特征利用不足、表征受限。该文提出差异引导多模态融合网络（DGMF-Net）：以判别性跨模态差异作为引导信号促进互补表征与协同融合，先引入差异引导的跨模态交互机制在早期完成交互与互补信息注入，再逐层强化特征表达。为多源海岸带数据融合中的模态差异处理提供新范式。（IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing，2026-10-26）', 'source': 'IEEE JSTARS', 'url': 'https://doi.org/10.1109/JSTARS.2026.3747308', 'date': '2026-10-26'}, {'title': '44 年 ERA5 再分析 + 现场观测校验：孟加拉湾波候的季节—年际行为与长期趋势', 'badge': '[论文]', 'abstract': '该文用 1980 年 6 月至 2024 年 5 月共 44 年 ERA5 再分析资料并以现场观测校验，研究 ENSO 与印度洋偶极子（IOD）对孟加拉湾季节与年度波浪特征的影响。结果显示季节性反转的风场主导波高与周期变化：风速在季风期（6–9 月）最大、季风前期（3–5 月）最小，波浪活动季风期最强、冬季最弱；北部孟加拉湾年平均风速与海面高度呈统计显著的年代际负趋势，而涌浪高、有效波高与最大波高呈现不同变化。为区域再分析产品的长期一致性评估与大尺度气候模态归因提供基准。（International Journal of Climatology，Wiley，2026-11-03）', 'source': 'International Journal of Climatology', 'url': 'https://doi.org/10.1002/joc.70653', 'date': '2026-11-03'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'GSDEM：陆→海迁移学习把全球 DEM 超分到 1 角秒，RMSE/MAE/坡度 RMSE 各降 18%/19%/20%', 'badge': '[论文]', 'abstract': '高分辨率全球数字高程模型对海岸与海洋研究关键，但公开全球海底 DEM 仍停留在 15 角秒，且高分辨率海洋 DEM 稀缺、高低分辨率配对常来自不同高程产品。该文把全球陆海重建表述为真实跨产品超分，提出 GSDEM：以 Swin Transformer 为骨干、SimpleGate 前馈、级联 ×3 后 ×5 重建，先在大规模陆地 DEM 上预训练、再在海岸与海洋 DEM 上微调，把地形知识从陆迁移到海。相比仅用海洋数据训练，陆海迁移学习使平均 RMSE、MAE 与坡度 RMSE 分别下降 18%、19%、20%。（IEEE Transactions on Geoscience and Remote Sensing，2026-11-06）', 'source': 'IEEE TGRS', 'url': 'https://doi.org/10.1109/TGRS.2026.3751156', 'date': '2026-11-06'}, {'title': 'SWOT 宽刈幅 + DTU21 长波：迭代频域组合精化海洋重力场，兼顾短波长与长波稳定性', 'badge': '[论文]', 'abstract': '高精度海洋重力场是解析精细海底构造与海洋地球物理研究的基础，但传统卫星测高受轨迹间距、测量噪声与滤波限制，难以恢复短波长重力信号；SWOT 任务提供密集宽刈幅观测，改善更短波长海面坡度恢复，而长期多任务测高模型在长波段更稳定。该文提出迭代频域组合方法，用高斯低通及其互补高通把 DTU21 的中长波分量与 SWOT_04 的中短波分量结合，并对候选截止波长做迭代优选。（Geophysical Journal International，Oxford University Press，2026-11-05）', 'source': 'Geophysical Journal International', 'url': 'https://doi.org/10.1093/gji/ggag480', 'date': '2026-11-05'}, {'title': '海洋涡街多源大数据综述：从数值模拟、观测到 AI—物理融合的快速预测、稀疏重构与参数反演', 'badge': '[论文]', 'abstract': '海洋涡街是海流与岛屿、礁体、海上风电设施等钝体相互作用形成的代表性尾流现象，是研究沿岸物质输运、能量串级与生态响应的重要载体。该综述从模拟数据、观测数据与应用三个视角综合近期进展：先梳理传统数值模拟在产出高保真流场、阐明动力机制上的基础作用，以及 AI—物理融合方法在快速预测、稀疏重构与参数反演上的延伸价值；再归纳多源观测的接入方式与典型应用，为涡街数据的多源组织与智能处理给出框架。（Big Earth Data，Taylor & Francis，2026-11-05）', 'source': 'Big Earth Data', 'url': 'https://doi.org/10.1080/20964471.2026.2753277', 'date': '2026-11-05'}, {'title': '连续台风的累积海洋响应：南海北部四次相继台风造出表层—次表层双核冷却结构', 'badge': '[论文]', 'abstract': '热带气旋强烈改变上层海洋并反过来调制海气热交换与后续气旋发展，但多个接连台风的累积影响研究不足。该文用卫星观测与再分析数据研究南海北部四次连续台风：相继台风在表层与次表层形成独特的双核冷却结构，伴随混合层加深与障碍层增厚；海洋响应由大气环境条件、风驱垂直混合、Ekman 抽吸与表面热通量交换共同调制，中尺度涡进一步调整其幅度，演化中的上层海洋状态又影响后续台风。（Monthly Weather Review，AMS，2026-11-06）', 'source': 'Monthly Weather Review', 'url': 'https://doi.org/10.1175/MWR-D-26-0024.1', 'date': '2026-11-06'}, {'title': 'HY-3A 海洋卫星 2048 像元短波红外 InGaAs 焦平面：四通道片上滤光、量子效率 >80%', 'badge': '[论文]', 'abstract': '该文报道用于 HY-3A 海洋卫星多光谱成像仪的短波红外焦平面阵列：分别采用 In0.53Ga0.47As/InP 与 In0.75Ga0.25As/In0.52Al0.48As 材料，格式 2048×52 与 2048×12，其中延伸波长 FPA 的阵列长度为已知航天应用中最长。组件密集集成 1.020、1.245、1.640、2.135 μm 四个中心波长滤光片，形成两组空间级 FPA 探测器组件，并配套三次采样保持架构的低噪声读出电路。在 293 K 与 223 K 芯片温度下，两组件各通道暗电流密度 48 与 320 nA/cm²、量子效率 >80%、暗信号 20 mV、读出噪声 1.8 与 1.1 mV、响应非均匀性 3.0%。（IEEE Transactions on Geoscience and Remote Sensing，2026-11-02）', 'source': 'IEEE TGRS', 'url': 'https://doi.org/10.1109/TGRS.2026.3749724', 'date': '2026-11-02'}]}, {'title': '六、数据管理与共享', 'en': 'Marine Data Management & Sharing', 'items': [{'title': '国家海洋信息中心获 PICES 开放数据卓越贡献奖（PODA）：我国首次，CGOF1.0 入选国家首批行业高质量数据集', 'badge': '[要闻]', 'abstract': '2026 年 10 月 24—30 日北太平洋海洋科学组织（PICES）年会在加拿大纳奈莫举行，国家海洋信息中心获颁 PICES 开放数据卓越贡献奖（PODA），为我国首次。该奖表彰在海洋数据综合管理、共享服务、关键数据集质量控制与改进、互操作性提升上具示范效应的机构。中心对外共享覆盖水文、气象、生物、化学等 7 大学科 83 类要素，数据最早可追溯至 1662 年；2024 年上线的国家海洋大数据服务平台（海洋云）已提供下载超 70 万次；牵头研制的中国全球海洋融合数据集 CGOF1.0 含 10 项核心参数、时序逾 60 年、10 km 分辨率，2025 年 6 月在第三届联合国海洋大会发布，累计在线服务近 8 万次，并入选国家首批行业高质量数据集典型案例。中心同时承担 IODE 国家协调员、WDS 天津海洋学中心、CMOC/China、中国 Argo 资料中心与 ODIS 中国节点等职能。（国家海洋信息中心，2026-11-06 发布）', 'source': '国家海洋信息中心 / 搜狐', 'url': 'https://www.sohu.com/a/1098116473_121107000', 'date': '2026-11-06'}, {'title': 'OPMM2 海洋实践成熟度模型：135 位实践作者逐属性访谈共设计，已被欧盟 OBPS 采纳为成熟度框架', 'badge': '[论文]', 'abstract': '全球性挑战需要被广泛采纳的观测、数据管理与应用实践，以产出一致、可互操作的信息。该文复盘原版海洋实践成熟度模型（OPMM），通过与海洋研究与应用社群共设计提出 OPMM2：保留五级但重命名并细化（Formation / Repeatable / Documented / Adopted / Sustained），给出各级属性的标准化定义与词表，明确从「已记录」到「已采纳」再到「可持续」的推进路径。修订基于对 135 项公认海洋实践作者的逐属性访谈（complies / 不符合 / 作者不清楚三档），据反馈放宽了持久标识符不限于 DOI、把「多机构认可」简化为「三家及以上机构实际使用」、删除了机器可读性属性等；结果分布为 Level 3 为 13 项、Level 4 为 83 项、Level 5 为 39 项。该模型已被欧盟委员会 Ocean Best Practices and Standards System 采纳为成熟度框架。（Frontiers in Marine Science，2026-10-29）', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1941879', 'date': '2026-10-29'}, {'title': 'ISO/TC 211「Standards in Action 2026」：S-100 海事域落地与面向 AI 的标准 API 同场演示', 'badge': '[政策]', 'abstract': 'ISO/TC 211 地理信息技术委员会于 11 月 6 日举办免费线上活动 Standards in Action 2026，展示 ISO 19100 系列地理空间标准在政府、国防、海上导航、人工智能、地址与自动驾驶中的实际应用。议程重点包括：ISO 19100 系列在海事领域经 S-100 实施的具体做法、面向现代地理空间元数据方法的国防互操作性、基于标准的 API 如何支撑 AI，以及 ISO 与 OGC 标准用于高清地图语言（HDML）的进展；另设数据治理中元数据智能使用、跨政府地址标准一致性等议题，并邀请日本国土地理院介绍国家标准化活动。对海洋空间数据的编目、互操作与 AI 就绪具有直接参考价值。（ISO/TC 211，活动通知 2026-11-02 / 活动 11-06）', 'source': 'ISO/TC 211', 'url': 'https://committee.iso.org/sites/tc211/home/standards-in-action/presentation-archive/2026-11-02-standards-in-action-2026-discover-how-geospatial-standards-are-shaping-the-future.html', 'date': '2026-11-02'}, {'title': '从商业智能到「保护智能」：企业级 BI 仪表盘驱动大堡礁长棘海星适应性防控的近实时决策', 'badge': '[论文]', 'abstract': '韧性为本的管理（RBM）强调在气候变化下主动维持并增强生态系统抵抗与恢复能力，需要持续建模、评估、评价与调整。该文把企业商业智能软件用于保护决策（Conservation Intelligence），为 RBM 提供所需近实时分析与决策支持系统，并以澳大利亚大堡礁长棘海星防控计划为示范：集成可视化仪表盘用于评估暴发严重程度、排定防控行动优先级、评价成效，并纳入新研究以闭合研究—实施回路，形成可复用的数据驱动适应性管理口径。（Conservation Science and Practice，Wiley，2026-11-05）', 'source': 'Conservation Science and Practice', 'url': 'https://doi.org/10.1111/csp2.70437', 'date': '2026-11-05'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '中国第 43 次南极考察队 11 月 7 日三亚起航：雪龙、雪龙 2、大洋号三船保障，100 余家单位 600 余名队员', 'badge': '[航次]', 'abstract': '11 月 7 日中国第 43 次南极考察队起航仪式在三亚南山港举行，队员登上「雪龙 2」号极地科考破冰船出发。此次考察将完善极地考察站点与运输保障体系，持续开展南极多领域综合调查监测，瞄准国际极地科技前沿实施重点任务，推进国产技术装备测试应用，深化双多边国际科研与保障合作。任务由「雪龙」号、「雪龙 2」号和「大洋号」共同保障，来自国内 100 多家单位的 600 余名队员参加，预计 2027 年 4 月完成任务返回。（新华社 / 凤凰网，2026-11-07）', 'source': '新华社 / 凤凰网', 'url': 'https://news.ifeng.com/c/8xr98khtthe', 'date': '2026-11-07'}, {'title': 'MARLEY：776 m 深、不在海底留死重的无废自主冷水珊瑚观测站（比斯开湾 Lampaul 峡谷）', 'badge': '[论文]', 'abstract': '冷水珊瑚礁被列为脆弱海洋生态系统，除当代人为扰动外还长期受海洋增温与酸化威胁，需要长期、高频的海洋监测系统。该文介绍 MARLEY（Monitoring deep-seA coRaL EcosYstems）观测站的设计、实现与运行表现：一套自主多参数平台，部署于比斯开湾 Lampaul 峡谷 776 m 水深处，用于低环境足迹地监测冷水珊瑚健康与行为；首要设计目标是消除在海底投放压载死重（累积性废弃物的重要来源）.（Deep Sea Research Part I: Oceanographic Research Papers，Elsevier，2026-10-28）', 'source': 'Deep Sea Research Part I', 'url': 'https://doi.org/10.1016/j.dsr.2026.104771', 'date': '2026-10-28'}, {'title': '刚柔耦合水下机械臂：油液压刚性臂做粗定位 + 水液压连续体腕做柔顺微调（RA-L）', 'badge': '[论文]', 'abstract': '水下作业既需要大范围运动又需要局部柔顺适应。该文提出异质液压刚柔耦合机械臂：油液压刚性臂负责宏定位，水液压连续体腕负责末端主动调节；一致性协调接口把刚性液压缸与软腔体的运动映射到共同末端任务空间，同时保留各自传动关系，生成的运动参考由针对刚、软子系统分别设计的液压控制器执行。样机经软腕独立轨迹跟踪、外部扰动下的定点调节、受限水下任务中的协同操作三类实验：刚性臂提供稳定大范围定位，软腕实现局部柔顺调整与扰动恢复。（IEEE Robotics and Automation Letters，2026-10-26）', 'source': 'IEEE RA-L', 'url': 'https://doi.org/10.1109/LRA.2026.3747601', 'date': '2026-10-26'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'Copernicus 海洋状态报告第 10 版发布：十年 636 位作者、214 份成果、37 国 258 家机构，附沉浸式十周年增刊', 'badge': '[报告]', 'abstract': '欧盟 Copernicus 海洋状态报告（OSR）迎来第 10 版。过去十年 OSR 持续记录海洋自然变率及其对海洋环境、生物多样性与社会的深刻改变，形成支撑研究、政策与社会的权威科学记录。十周年里程碑数据为：636 位作者、214 份出版物、来自 37 个国家的 258 家机构。为纪念这一节点，特别推出十周年增刊，以沉浸式滚动叙事（scrollytelling）形式通过十项关键洞见，梳理海洋变化、科学认识进展，以及持续海洋观测与国际协作的重要性。（Copernicus Marine Service / Marine Ireland，2026-11-02）', 'source': 'Copernicus Marine / Marine Ireland', 'url': 'https://marine-ireland.ie/node/2150', 'date': '2026-11-02'}, {'title': 'NOAA NCEI 新增 GTSPP 实时温盐剖面归档（Accession 0319413）：加拿大 DFO 2026-10-18 提交批次', 'badge': '[数据]', 'abstract': 'NOAA 国家环境信息中心（NCEI）新入库一批全球温盐剖面计划（GTSPP）实时剖面数据，由加拿大渔业与海洋部（DFO）海洋环境数据处汇编、2026-10-18 提交，归档号 0319413，出版与创建日期均为 2026-11-02，状态为「Complete / Historical archive」，更新频率为按需。要素含水温、盐度、海表温度、流速流向、气温、气压、湿度、风向风速与深度等，平台标识涵盖多个 WMO 浮标与船舶呼号；数据并入 GTSPP 数据库并向公众开放，用于科学研究与分析。该归档隶属自 1999-10-04 起持续汇交的 MEDS-GTSPP 长期集合，体现全球温盐数据中心例行汇交与开放共享链路。（NOAA NCEI，2026-11-02）', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/archive/accession/0319413', 'date': '2026-11-02'}, {'title': '自然资源部发布全国首批 14 个海洋减灾典型案例：广州 135 个岸基站 + 全栈国产 AI 大模型支撑 7 参数 3 天预测', 'badge': '[要闻]', 'abstract': '自然资源部发布全国首批 14 个海洋减灾典型案例，广东「广州市夯实珠江口黄金内湾海洋防灾减灾硬实力」与「深圳市海洋灾害风险提示基层社区精准落地」两案例入选。广州围绕观测监测能力升级、传输网优化、预报警报提质、风险管控增效，建成 60 个海水入侵监测站、13 个海洋生态监测站等 7 类 135 个岸基观测站点，实现水文、生态、气象 100 余种要素全天候观测；并在全省首次依托全栈国产化 AI 算力平台与国产 AI 芯片构建软硬件一体的海洋灾害防治大模型，支持 7 种海洋气象参数 3 天预测、单模型分析预报效率达分钟级，参数量超 6 亿，可识别船舶、码头、构筑物等 5 类目标并划分 6 类地物。（新快报，2026-11-06）', 'source': '新快报', 'url': 'https://epaper.xkb.com.cn/view/1270198', 'date': '2026-11-06'}, {'title': 'NOAA 马里亚纳海底图完成约 28.97 万 km² 测深：CNMI—关岛专属经济区 95% 以上已有公开高分辨率数据', 'badge': '[数据]', 'abstract': 'NOAA 海洋勘探局 11 月 2 日宣布，与合作伙伴已完成北马里亚纳群岛联邦（CNMI）与关岛美国专属经济区约 289700 km² 的高分辨率海底测深，公开数据覆盖率超过 95%（CNMI 周边约 267500 km²、关岛周边约 22200 km²）。成果由 Saildrone Surveyor、美国海军研究项目数据以及 2026 年「Nautilus」号两次航次（船载测深声呐、ROV 与 WHOI 的自主潜器 Sentry）混合拼合；NCEI 已列出 5 个 2026 年关岛/CNMI 调查条目（2 次 Nautilus 航次、3 次 Saildrone 调查），可按航次检索测深、水文、水柱声呐与浅地层剖面数据。报道同时提示：覆盖率不等于生态系统认知，测深只描述形状与深度，物种分布、季节变化与未来活动影响仍需独立证据；全球仅约 28.7% 洋底按现代标准完成测绘（UNESCO-IOC 4 月更新）。这一背景与「海山图志」等深海空间数据产品的补齐方向直接呼应。（NOAA Ocean Exploration 11-02 公告 / OceanVines 11-04 报道）', 'source': 'NOAA Ocean Exploration / OceanVines', 'url': 'https://oceanvines.org/news/2026-11-04-mariana-seafloor-mapping', 'date': '2026-11-04'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'pystac 1.16.0：新增 octet-stream/zip 媒体类型、JSON Schema 抓取允许清单与 SpecDeprecationWarning', 'badge': '[工具]', 'abstract': 'STAC（时空资产目录）Python 库 pystac 发布 1.16.0（PyPI 上传 2026-11-04，GitHub release 2026-11-04，变更条目标注 11-02）。新增特性包括：支持 octet-stream 与 zip 媒体类型、为抓取 JSON Schema 增加可选允许清单、引入 SpecDeprecationWarning 以提示规范弃用。对以 STAC 目录组织卫星海洋数据、栅格产品与航次资产的工作流，媒体类型支持与 Schema 抓取管控直接影响资产登记与校验环节。（PyPI / GitHub Releases）', 'source': 'PyPI / GitHub', 'url': 'https://pypi.org/project/pystac/1.16.0/', 'date': '2026-11-04'}, {'title': 'rio-tiler 9.4.13：修复加权分位数权重累加精度（回退到 float64）', 'badge': '[工具]', 'abstract': '栅格切片读取库 rio-tiler 发布 9.4.13（PyPI 与 GitHub release 均为 2026-11-02），为 9.4.12 的补丁版本，修复加权分位数计算中权重累加应在 float64 下进行的问题（回移植 PR #1051）。加权分位数常用于影像统计与动态拉伸，该修复直接影响基于 Cloud-Optimized GeoTIFF 的海洋栅格（SST、叶绿素、海色等）瓦片服务在大幅值或长序列下的统计稳定性。（PyPI / GitHub Releases）', 'source': 'PyPI / GitHub', 'url': 'https://pypi.org/project/rio-tiler/9.4.13/', 'date': '2026-11-02'}, {'title': 'pyvista 0.49.2：三维可视化与网格分析库新版本（PyPI 2026-10-28）', 'badge': '[工具]', 'abstract': '面向科学与工程三维可视化、网格分析的 pyvista 在 PyPI 发布 0.49.2（2026-10-28）。该库基于 VTK 提供网格数据结构与绘图接口，常用于海底地形、水体体积与流场三维表达。相邻的 0.49.1（GitHub release 2026-10-11）修复了 IPython < 8.8 环境下的导入、无标量时 add_mesh 的 rgb 参数异常、命名不透明度越界、缩放截图后的陈旧瓦片，以及 vtk<9.4 下 32 位面索引网格细分等问题；0.49.2 为该分支的后续补丁版本。（PyPI / GitHub Releases）', 'source': 'PyPI / GitHub', 'url': 'https://pypi.org/project/pyvista/0.49.2/', 'date': '2026-10-28'}]}]



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
