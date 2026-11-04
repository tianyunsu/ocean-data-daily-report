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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '深圳联合华为发布「司渊」海洋大模型：动力与生态要素融合预报，计算从小时级压到分钟级', 'badge': '[要闻]', 'abstract': '深圳市海洋发展局联合华为在 2026 海博会海洋灾害防御论坛发布「司渊」海洋大模型，称其为全国首个把海洋动力环境要素与海洋生态要素融合起来做预报的大模型。模型依托盘古大模型与昇腾算力底座，实现全球 1/12°、区域 1/36° 的温盐流浪预报，并覆盖叶绿素浓度、溶解氧浓度等 9 种生态要素；架构上采用海洋领域 3D Earth-Specific Transformer 与 3D 窗口注意力捕捉三维要素规律，训练时另引入重力位势、比湿、径向/纬向风速、海表温度、海平面气压等 13 层大气要素做海气耦合。官方给出的效果口径是预报计算时长由小时级降到分钟级，面向分钟级响应的城市海洋防灾场景。（华为企业业务）', 'source': '华为 / 深圳市海洋发展局', 'url': 'https://e.huawei.com/cn/news/2026/industries/government/shenzhen-municipal-ocean-development-bureau', 'date': '2026-10-23'}, {'title': '多生成源 + 双分支训练：苏禄海内孤立波生成传播一体化智能预报（TGRS）', 'badge': '[论文]', 'abstract': '苏禄海被岛链、海峡和浅滩环绕，内孤立波存在多源生成、路径复杂的问题：只靠卫星观测的数据驱动方法难以保证连续性与物理一致性，而传统方案又预设单一生成源。中科院海洋所人工智能海洋学研究组分析 2002—2022 年卫星影像，发现该海域波群空间上分西南部（Pearl Bank 及邻近海槛、浅滩）与东北部两组，整体向西北传播、平均速度约 2.05 m/s；据此用卫星观测联合 Eikonal 方程做多生成源寻优，确定「五点一线」生成源，再构建双分支模型——第一分支以多源 Eikonal 传播时间场为引导学连续区域结构，第二分支用卫星观测与源区潮汐信息学局地偏差，两支输出叠加。模型无需输入初始波峰线即可预报，相较单一生成源方案误差降低 70.40%。（IEEE TGRS / 中科院海洋所）', 'source': 'IEEE TGRS / 中科院海洋所', 'url': 'https://qdio.cas.cn/2019Ver/News/kyjz/202610/t20261028_8299912.html', 'date': '2026-10-28'}, {'title': 'YingLan：面向异构观测的多模态海洋基础模型，在昇腾 910B 上完成训练', 'badge': '[论文]', 'abstract': '卫星影像、网格化海洋场与浮标观测在数据结构、物理语义和时空特性上差异极大，导致现有方法多停留在任务定制，难以学到可迁移表征。YingLan 提出物理属性条件化的动态编码（按物理语义与观测特性生成自适应输入投影）、时空增量耦合（STIC，通过潜时间增量的跨尺度交互建模多尺度依赖）与海洋状态演化感知预训练（掩码观测重建 + 时间演化目标联合）。模型用 MindSpore 实现、在华为昇腾 910B 上训练，深圳近海 7 天表层盐度预报平均 RMSE 0.687508 PSU，相对 LangYa、XiHe、GloNet2 分别降低 0.58%、5.31%、12.42%；作者同时说明跨任务、跨区域的泛化性仍待更大范围评估。（arXiv）', 'source': 'arXiv', 'url': 'https://doi.org/10.48550/arXiv.2610.29313', 'date': '2026-10-21'}, {'title': 'GreenToken：用视觉 token 剪枝给水下生物多样性识别降算力（ACM MM 2026）', 'badge': '[会议]', 'abstract': '水下生物识别同时受图像退化、背景杂乱、长尾类别与算力有限四重约束，而 CLIP 对大范围弱信息区域仍逐 patch 计算。GreenToken 提出轻量剪枝协议：保留 class token，按视觉范数、文本引导或两者混合的打分挑选 CLIP patch token。在 FathomNet 风格基准（1,053 张图像、17 个海洋类别）上以 CLIP、DINOv2-small 与 DINO+CLIP 融合三种配置评测，三个随机种子下 DINO+GreenToken-75 取得最佳 macro-F1 0.569±0.017（保留 37/49 个 CLIP token）；GreenToken-50 用 24/49 token 取得 0.564±0.009，CLIP 注意力开销代理指标降 75%、纯视觉编码器加速 1.84×。作者结论是剪枝后的 CLIP 特征仍可作为 DINOv2 的紧凑语义补充。（ACM Multimedia 2026）', 'source': 'ACM Multimedia 2026', 'url': 'https://doi.org/10.1145/3840750.3841451', 'date': '2026-11-02'}, {'title': 'ISOPoT：用点多帧跟踪重做成像声呐里程计（RA-L）', 'badge': '[论文]', 'abstract': '水下远距离感知多依赖前视声呐，但声呐图像噪声大、伪影多、缺少丰富语义结构，直接把陆上视觉的关键点检测与匹配方法搬过来效果很差。ISOPoT 改用现代点跟踪技术，把多帧点轨迹作为主要对应关系表示，再叠加轻量优化提升鲁棒性，构建完整声呐里程计流程。在 Aracati 2017 公开数据集与自采真实水下声呐数据集上，纯声呐与多传感器两种设置下均稳定优于此前 SOTA。对浑浊、低能见度环境下的 AUV 导航，这条「以轨迹代替特征点」的路线值得关注。（IEEE Robotics and Automation Letters）', 'source': 'IEEE Robotics and Automation Letters', 'url': 'https://doi.org/10.1109/LRA.2026.3746126', 'date': '2026-10-23'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '深圳发布海洋防灾减灾数字孪生场景应用：15 类产品、6 种灾害、206 km² 陆海一体底座', 'badge': '[要闻]', 'abstract': '该场景由国家海洋信息中心与深圳市海洋发展局联合建设，2026 海博会期间正式发布，被称为目前全国精细化程度最高、现势性最强的地市级陆海一体化数字孪生底座，凝聚深圳大学、华为等本地力量。系统接入实况感知、观测监测、分析预报、承灾体等 15 类产品，针对台风、风暴潮、赤潮等 6 种频发海洋灾害构建模拟推演模型，打通「实时感知—分析预报—仿真推演—动态评估—响应决策」全链条，建成 206 km² 海陆一体化三维底座。今年 7 月台风「红霞」过程中已实战检验：灾前模拟淹没漫堤过程并识别岸段风险支撑人员转移，灾中打通多部门数据支撑会商调度，灾后评估损失并优化海堤加固与防汛预案。（深圳新闻网 / 21 世纪经济报道）', 'source': '深圳新闻网', 'url': 'https://www.sznews.com/news/content/2026-10/23/content_32199065.htm', 'date': '2026-10-23'}, {'title': '广西北部湾海洋三维数字孪生平台获全国智慧海洋大数据与 AI 应用创新大赛一等奖', 'badge': '[动态]', 'abstract': '10 月 27 日，第五届全国智慧海洋大数据与人工智能应用创新大赛暨第一届广西海洋智能装备创新大赛在钦州举办，由国家海洋信息中心主办。数字广西集团与中国电建华东勘测设计研究院共建的广西北部湾海洋三维数字孪生平台获一等奖。该平台依托公开海洋科学数据，融合 AI 大模型、数字孪生底座与数字人交互组件，构建近海虚实映射的三维数字镜像，覆盖生态监管、灾害推演、养殖服务与科普交流四类场景，目标指向海洋数据分散、场景仿真精度不足、跨领域协同难三个痛点，同时作为面向东盟海洋数字合作的具体实践。（数字广西集团）', 'source': '数字广西集团', 'url': 'https://weibo.com/ttarticle/p/show?id=2309405359283964608565', 'date': '2026-10-27'}, {'title': 'Eco Wave Power 完成 AI 数字孪生一期：从波浪载荷仿真走到能量预测', 'badge': '[动态]', 'abstract': '岸式波浪能公司 Eco Wave Power（Nasdaq: WAVE）与德国 AI engineering GmbH 完成 AI 数字孪生项目第一阶段：建立描述海浪与其浮体相互作用的物理基座模型，覆盖不同海况下的波浪载荷、浮体运动、结构受力与潜在发电量仿真，并具备能量与载荷预测的初步机器学习能力；同时评估了模型向不同波浪条件场址迁移的可行性。技术栈上双方使用并评估 NVIDIA Omniverse 做孪生可视化与仿真流程、NVIDIA Warp 进入建模工具链。规划中的后续阶段将把模型扩展到液压与机械能量转换系统、接入真实运行传感器与发电数据，并叠加机器学习运行层。值得注意的是，公司把该孪生能力与「为沿海数据中心供电」的设想直接关联。（SEC 披露 / Eco Wave Power）', 'source': 'SEC 披露', 'url': 'https://www.sec.gov/Archives/edgar/data/1846715/000121390026114691/ea031043701ex99-1.htm', 'date': '2026-11-02'}, {'title': 'EDITO 的 EOSC 节点投产：欧洲数字孪生海洋接上开放科学联邦', 'badge': '[动态]', 'abstract': '欧洲开放科学云（EOSC）联邦通过共享能力与共同参与规则连接各研究基础设施。CNR-ISTI 在 D4Science 上运营的「EOSC Node European Digital Twin Ocean」（由 EOSC-Marine 支持）自 2026 年 10 月 8 日起进入生产，为 EDITO 提供开放科学组件，把海洋研究资源与服务接入更广的 EOSC 社区。该报告梳理了节点从注册到投产的过程，区分强制性要求与推荐能力，说明联邦认证、目录集成与服务发现，以及用户支持、监控与对齐 FitSM 的服务管理；并进一步提出把 EDITO 服务通过该节点暴露的实用框架，涉及服务描述与访问策略、认证、支持联系人、可用性检查、成熟度与可持续性承诺。（Zenodo / EOSC-Marine）', 'source': 'Zenodo', 'url': 'https://doi.org/10.5281/zenodo.23674230', 'date': '2026-10-26'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': 'MapGIS 在海博会发布海洋版：GIS Agent 全时空智能体 + 海陆一体三维建模', 'badge': '[工具]', 'abstract': '2026 海博会（10 月 22—24 日，深圳）上，中地软件展示 MapGIS 全空间智能 GIS 平台、GIS Agent 全时空智能体与海洋信息化产品体系，并在新品发布专场推出面向海洋领域的最新成果。GIS Agent 融合大模型能力，打通时空数据理解、空间分析、业务推理、自动制图等环节，把 GIS 业务从人工操作推向智能问答、自动研判与任务式执行；海洋信息化侧依托全国产化平台的时空数据引擎与 AI 大模型引擎，构成「1 数据基座 + 2 专业平台 + N 场景应用」体系，提供数据处理、三维建模、智能分析等成套能力，落点是海陆一体化三维建模与数字孪生应用。（MapGIS 中地软件）', 'source': 'MapGIS 中地软件', 'url': 'https://www.mapgis.com/index.php?a=shows&catid=33&id=1913', 'date': '2026-10-24'}, {'title': '「耕海1号」装上「一张图」：多源数据融合把海洋牧场做成可视可测可控可预警体系', 'badge': '[动态]', 'abstract': '2026 年「数据要素×」大赛全国总决赛在青岛颁奖，山东海洋渔业联合浪潮智慧科技申报的《「经略深蓝·数智共生」——智慧海洋牧场多源数据融合赋能应用方案》获现代农业赛道三等奖。项目以国内首制大型现代化海洋牧场综合体「耕海1号」为载体，针对传统牧场生产粗放、环境风险高、数智化体系零散、产业融合度低的问题，汇聚治理养殖、环境、装备、文旅多维数据，构建「空天地海」一体化感知体系与海洋牧场「一张图」，试图用统一的可视化视图破除多源数据融合壁垒，形成「可视、可测、可控、可预警」的数智体系。其价值不在单点算法，而在把分散的养殖与环境数据接到同一张可操作视图上——这正是多数海洋可视化项目落地时最难的一步。（大众新闻 / 腾讯新闻）', 'source': '大众新闻', 'url': 'https://new.qq.com/rain/a/20261028A04ZEQ00', 'date': '2026-10-28'}, {'title': '漂视 CIMPro 孪大师 + DPE 数字样机编辑器：把船厂与港口搬进三维场景', 'badge': '[工具]', 'abstract': '2026 海博会上，上海漂视网络展示自研数字孪生开发平台 CIMPro 孪大师与 DPE 数字样机编辑器。孪大师对接 ERP、MES、堆场数字化等系统，做船舶制造全流程 3D 可视化（龙门吊实时定位、产线节拍、AGV 轨迹），并可构建港口 1:1 三维场景集成生产调度与船舶进出港数据；海洋侧支持海浪、洋流、天气模拟可视化与海底地形编辑，覆盖海上风电、钻井打捞、海缆铺设等特种作业的 3D 仿真。底层强调国产信创适配（自研三维渲染内核、兼容国产 CPU 与浏览器生态、支持私有化部署）与多源数据融合（MySQL、达梦、人大金仓、MQTT、OPC UA 等）。DPE 支持高斯泼溅模型直接导入、数亿高斯点秒级加载，并提供 AI 图生 3D、自动生成拆装课件等能力。（漂视网络）', 'source': '漂视网络', 'url': 'http://mp.weixin.qq.com/s?__biz=MzkzMDI2NzYwMg==&mid=2247501821&idx=1&sn=cd2f2c6748d430f0f3a3e6a85e5f8345', 'date': '2026-10-24'}, {'title': 'GEODESC：给大洋钻探岩芯的「可视化描述」做协同 Web 工具，40 年五代演进收口（Scientific Drilling）', 'badge': '[论文]', 'abstract': 'IODP/ODP 的「决心号」上，科学家要对数百公里岩芯做目视描述，为后续取样与分析定标；这套高度依赖人工协同的流程在 1985—2024 年间随技术与使用习惯演化了五代数据库与用户应用，最终收敛为 2019—2023 年构建、在决心号服役最后两年投产的 GEODESC（GEOlogical DESCription）工具集。它的设计选择很值得借鉴：以电子表格为数据采集载体（沿用用户自发采用且明确要求的做法），产物本身就是结构良好的表格、可直接分析与可视化；关系型数据库承担协同、数据安全与质量控制；Web 应用跑在所有主流浏览器上、无需安装软件，便于全球分布式团队协作。GEODESC 覆盖微观、宏观与汇总三个尺度的岩芯描述，并支持微体古生物数据采集；用可观测量的定义语法统一数百个观测项以保一致；模板目录与定制应用降低项目启动成本。服务原由 JRSO 托管，现由墨西哥湾岩芯库（GCR）维护。对海洋地质数据库与可视化系统建设，这是一份 40 年迭代出来的一手经验。（Scientific Drilling）', 'source': 'Scientific Drilling', 'url': 'https://doi.org/10.5194/sd-35-229-2026', 'date': '2026-10-23'}, {'title': '同一片海岸、三套 GIS 多准则框架：海平面上升下的分散式污水处理系统脆弱性排序（JAWRA）', 'badge': '[论文]', 'abstract': '沿海低洼地带的分户式污水处理系统（OSTDS）同时面临海平面上升（SLR）与地下水淹没的威胁，但「哪一套排在前、可不可信」取决于空间模型怎么选。研究构建了三套空间显式的 GIS 多准则评价框架——Bathtub-现状、Bathtub-2 英尺（0.6 m）SLR、MODFLOW-2 英尺 SLR——把 SLR 响应、潜水位埋深、海水入侵、反复淹水、风暴潮与 OSTDS 密度用 Delphi 打分、成对比较赋权与加权线性组合集成起来。结果显示：2 英尺 SLR 下静水（bathtub）法复现了 MODFLOW 淹没范围的 86%；三张脆弱性面高度一致（Pearson 0.966—0.994，RMSE 0.036—0.077），但具体到单个 OSTDS 的分级出现分歧——56,080 个受评对象中，至少一套框架判定 1,961 个高度脆弱，三套一致判定的只有 577 个。作者结论是静水模型可作为区域筛查工具，但不能替代地下水模型或现场核查；方法上则给出「分层筛查—优先监测」的资源分配逻辑。（JAWRA）', 'source': 'JAWRA（美国水资源协会志）', 'url': 'https://doi.org/10.1111/1752-1688.70158', 'date': '2026-10-29'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': '千里眼卫星 2 号融合应用会议：GOCI-II 海洋载荷精密验证与 AI 资料处理成主线', 'badge': '[动态]', 'abstract': '第八届千里眼卫星 2 号（GEO-KOMPSAT-2A/2B）融合应用会议于 2026 年 10 月 21 日在韩国釜山召开，由 KIOST、韩国国家气象卫星中心、国立环境科学院与国立海洋调查院共同举办——四家机构 2020 年组建协商机制，下设卫星运营、校验修正、融合应用三个分科，每年发布成果。会议三个环节分别讨论观测资料校正与算法改进（含 AI/深度学习处理案例）、后续海洋气象环境卫星开发方向，以及观测连续性、多传感器融合与气候危机应对。KIOST 分享了对其 2B 星海洋载荷 GOCI-II 观测资料的精密验证成果，并强调开发后续 GOCI-III 的必要性。（中韩海洋科学共同研究中心）', 'source': '中韩海洋科学共同研究中心', 'url': 'http://www.ckjorc.org/cn/news-center/ocean-dynamics/detail/3435', 'date': '2026-10-21'}, {'title': 'argoFloats 1.0.10：把 Argo 质控旗标与调整数据的三步流程写进文档', 'badge': '[工具]', 'abstract': 'Argo 核心、BGC 与 Deep Argo 数据都要经过实时（24—48 小时内赋旗标）与延时两种质控。CRAN 于 2026-10-23 发布 argoFloats 1.0.10，其质控文档把处理流程收敛为三步：plot(which="QC") 看质量、showQCTests() 查做过/未通过哪些检验、applyQC() 应用旗标；调整数据用 useAdjusted() 处理。文档同时提醒旗标 1/2/5/8 视为「好」、9 为缺失、3/4/6/7 为「坏」，并给出 dataStateIndicator 用于按处理程度取子集——对下游做延迟模式分析的人，这是一份可直接照做的口径说明，而不是又一层封装。（CRAN）', 'source': 'CRAN', 'url': 'https://cran.r-project.org/web/packages/argoFloats', 'date': '2026-10-23'}, {'title': '模型标定不再「一个参数打全场」：按上下文局部化的摊销后验推断（海洋湍流案例）', 'badge': '[论文]', 'abstract': '模型偏差会让单一标定参数无法在整個上下文域内复现物理响应；同时观测与上下文本身的不确定性也必须被量化。研究构造一族「局部化后验」：按与目标上下文的邻近程度对观测似然加权（高斯局部化权重），把上下文与观测的不确定性一并纳入，并用摊销推断避免每个上下文都重跑一遍 MCMC。方法以海洋湍流实验为应用案例。对海洋模式与观测算子标定而言，这条路线的意义是把「参数是否随环境漂移」从定性怀疑变成可估计的后验结构。（arXiv）', 'source': 'arXiv', 'url': 'https://doi.org/10.48550/arXiv.2610.37731', 'date': '2026-10-27'}, {'title': '把四点斜率阵列搬到岸基 X 波段雷达：米级分辨率近岸波向反演 + 信噪比质控（JTECH）', 'badge': '[论文]', 'abstract': '岸基观测平台普遍缺少监测表面重力波演变所需的空间分辨率，而近岸波场因地形引起的浅化与折射高度非均匀，使公海常用的三维 FFT 方法在近岸难以解释。该研究把原本用于压力传感器的经典四点斜率阵列法改造后应用于雷达后向散射影像，以米级分辨率估计波向；在加州 Point Sal 附近平直海滩采集数据，将斜率阵列导出的波统计量与现场 Spotter 浮标、谱折射模型、3D FFT 反演法三方对比，并提出一套基于信噪比的质控方法，用于识别劣化观测的采样条件、刻画本站点雷达波反演的最佳波浪与气象条件。经质控后，斜率阵列与 3D FFT 反演相对 Spotter 浮标时间序列的 RMSE 分别为 13° 与 11°；空间分析显示斜率阵列波向与谱折射模型预测更吻合，且方向估计的空间分辨率为 12 m，而 3D FFT 为 543 m。作者据此认为 X 波段雷达有能力捕捉小尺度近岸波浪折射。（Journal of Atmospheric and Oceanic Technology）', 'source': 'Journal of Atmospheric and Oceanic Technology', 'url': 'https://doi.org/10.1175/jtech-d-26-0004.1', 'date': '2026-11-02'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'Morlenn：北大西洋三小时、0.25° 混合层深度与层结数据集（神经网络 + Argo 监督）', 'badge': '[数据]', 'abstract': '混合层深度控制海洋与大气之间的热量交换，也塑造海洋生物生存条件，但次日尺度上的直接观测极其稀疏。Morlenn 以卫星海表观测、大气通量与波浪强迫历史为输入，用受 Argo 单剖面混合层深度与层结观测训练的神经网络，生成覆盖北大西洋及邻近赤道海域、空间分辨率 0.25°、时间分辨率 3 小时、跨 2011—2023 年的数据集，输出混合层深度与混合层下最大浮力频率平方两个变量，并提供「仅用海表输入」与「额外引入邻近 Argo 数据」两版。以 Argo 站位评分时，引入邻近 Argo 的版本混合层深度 RMSE 为 38 米，现有 ARMOR3D 为 45 米、GLORYS 为 56 米；作者提示次表层层结验证不如混合层深度充分，浅混合层、极深层与低盐区存在已知限制。数据以 CC BY 4.0 发布于 SEANOE（doi:10.17882/120058），论文为 ESSD 在审预印本。（ESSD Discussions）', 'source': 'Earth System Science Data (preprint)', 'url': 'https://doi.org/10.5194/essd-2026-807', 'date': '2026-10-28'}, {'title': 'MLAWind：用可解释随机森林重建 1950—2023 年全球月海表风场', 'badge': '[数据]', 'abstract': '长时段、网格化的海表风场数据是理解大气环流变化与不同时间尺度海气相互作用的前提。该研究用基于随机森林的可解释机器学习模型，生成 1950—2023 年、1°×1° 的月平均海表风场数据集 MLAWind，覆盖 60°S—60°N 的近全球海洋。相比纯再分析产品，这条路径的价值在于把重建过程做成可解释的映射关系，便于检验输入变量贡献与时空外推的可靠性；数据在 ESSD 正式发表，可直接用于长时序风场与海浪、混合层等衍生量研究。（Earth System Science Data）', 'source': 'Earth System Science Data', 'url': 'https://doi.org/10.5194/essd-18-7963-2026', 'date': '2026-11-02'}, {'title': '融合动态云遮蔽训练的葵花 8 号叶绿素 a 超分重建：0.05° 升到 0.01° 且补云洞', 'badge': '[论文]', 'abstract': '静止轨道水色卫星同时受「空间分辨率不足」与「云遮挡缺测」两重限制。该研究以葵花 8 号叶绿素 a 浓度产品为对象，把动态复合遮蔽策略嵌入 ESPCN 训练过程，使模型在做 5 倍超分的同时学会从部分遮蔽观测恢复完整空间结构，目标是用覆盖西太平洋的 0.05° 低分辨率数据同步产出 0.01° 且无云缺测的数据集。测试集精度为峰值信噪比 >50 dB、r>0.86；据此生成 2015—2022 年西太平洋高分辨率时空连续叶绿素 a 数据集，经独立 Argo 浮标验证，匹配样本量由 3,783 提升至 5,141，RMSE 由 0.693 降至 0.289、MAE 由 0.203 降至 0.171，并能在珠江口等近岸区刻画出羽状锋与叶绿素「低-高-低」演变。（中国海洋大学学报（自然科学版））', 'source': '中国海洋大学学报', 'url': 'https://qdhy.cbpt.cnki.net/portal/journal/portal/client/paper/a51033eda8eede3695317df1ee90d24b', 'date': '2026-10-27'}, {'title': '岩性标签帮不上忙：LILY 钻探数据库上的自监督嵌入与沉积物属性预测', 'badge': '[论文]', 'abstract': '科学钻探积累了海量物理、化学与磁学测量，但档案本身并不完整：仪器采样间隔不一、取芯率有限，破坏性分析又让同一材料无法二次测量。研究在 LILY 海洋钻探数据库上用六类常规测井/物性记录训练自监督嵌入模型，再预测海洋沉积物属性，并专门检验「专家岩性标签」是否带来增益。结论是否定的——在标签稀缺且不一致的现实条件下，自监督表征比引入专家岩性标签更有效。对把钻探档案做成可复用数据资产的工作，这是一个提醒：先解决表征，再谈标注。（arXiv）', 'source': 'arXiv', 'url': 'https://doi.org/10.48550/arXiv.2610.36410', 'date': '2026-10-26'}, {'title': '机载测深激光雷达仿真：分层水体下的偏振半解析蒙特卡洛', 'badge': '[论文]', 'abstract': '测深激光雷达仿真长期把海水当作光学均匀介质，因而无法复现温跃层、浊度层或次表层叶绿素最大层如何重塑偏振回波。研究提出面向垂向分层水体的偏振敏感半解析蒙特卡洛（SMC）方法：把光子引擎重建为分层感知的自由程推进与分层局部估计，重新推导强制赋分权重以在衰减系数与 Mueller 矩阵不连续处保持无偏，并在每次散射事件中完整携带 Stokes 态；再以重要性采样、边界附近自适应步长控制与 GPU 映射的多重散射合成把成本压到可做参数扫描的量级。方法与小角近似解析解吻合良好。对机载/星载测深反演的误差溯源，这提供了可解释的仿真底座。（Scientific Reports）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-76456-2', 'date': '2026-10-24'}]}, {'title': '六、数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'Seabed 2030 与波罗的海海道测量委员会签约：把区域测深数据接入 GEBCO 全球网格', 'badge': '[动态]', 'abstract': '2026 年 10 月 26 日，日本财团—GEBCO Seabed 2030 项目宣布与波罗的海海道测量委员会（BSHC）建立新伙伴关系，MoU 在立陶宛克莱佩达举行的 BSHC 第 31 届会议期间签署。BSHC 成立于 1983 年（赫尔辛基），是国际海道测量组织（IHO）的区域海道测量委员会，长期协调波罗的海区域的海道测量、海图制作与海事信息交换。此次合作意在强化参与海道测量机构之间的协调、推动测深数据共享，并把区域专业能力导向 Seabed 2030 的全球海底测绘目标；所有汇交数据进入免费公开的 GEBCO 全球网格。对区域数据「上行到全球产品」的治理链条，这是一次典型补位。（Seabed 2030）', 'source': 'Seabed 2030', 'url': 'https://seabed2030.org/2026/10/26/seabed-2030-and-baltic-sea-hydrographic-commission-join-forces-to-advance-global-ocean-mapping/', 'date': '2026-10-26'}, {'title': 'CIOOS 成为 IODE 协联数据单元：加拿大区域海洋观测网接入 UNESCO 全球数据体系', 'badge': '[动态]', 'abstract': '加拿大综合海洋观测系统（CIOOS）于 2026 年 10 月 22 日宣布成为 UNESCO 政府间海洋学委员会 IODE 的协联数据单元（ADU）。IODE 自 1961 年起协调全球海洋数据中心网络，各国设一个官方国家海洋数据中心（加拿大为渔业与海洋部的 MEDS），ADU 则是提供持续海洋数据服务的机构；CIOOS 由此与 Ocean Tracking Network 并列成为加拿大的 ADU，并承诺按 FAIR 原则做好数据托管、与 MEDS 协同。下一步是走 IODE 基于 ISO 9000 的质量管理框架（QMF）四步认证：先建并文档化质量体系，再提交 QMF 指导组评审，通过后持续维护以保持认证——这意味着区域观测网要把「数据怎么流、怎么质控」写成可审计文件。（CIOOS）', 'source': 'CIOOS', 'url': 'https://cioos.ca/new/cioos-joins-the-iode-global-network-as-an-associate-data-unit', 'date': '2026-10-22'}, {'title': 'NOAA 首次把 Okeanos 深海生物观测数据批量发布到 OBIS 与 GBIF', 'badge': '[动态]', 'abstract': 'NOAA 海洋探索办公室宣布，首次将「Okeanos Explorer」号科考船航次的深海生物出现数据发布至海洋生物地理信息系统（OBIS）与全球生物多样性信息设施（GBIF）。首批数据来自 2023 年美国西海岸与阿拉斯加外海三个航次、34 次 ROV 潜水，包含超过 6 万条生物观测记录、近 400 份生物样品与 245 份环境 DNA（eDNA）水样；视频标注依托加拿大海洋网络公司的 SeaTube 平台完成，并由夏威夷大学马诺阿分校团队审核。加上近期 eDNA 数据，NOAA 累计已向两大数据库贡献超过 74 万条带地理参照的生物记录，后续将把此类发布纳入常规数据流程并回溯整理历史航次数据。对深海影像这类「非结构化、靠人工标注」的资产，这条从视频到全球数据库的流水线值得国内科考借鉴。（水德科技「深蓝瞭望」第 18 期，据 NOAA Ocean Exploration）', 'source': '水德科技「深蓝瞭望」/ NOAA', 'url': 'https://www.watertools.cn/news/info/538.html', 'date': '2026-10-29'}, {'title': 'NNJA：1979 年至今的「策展式」地球系统观测档案，配套 Parquet 版直接喂 AI 训练（BAMS）', 'badge': '[论文]', 'abstract': 'NOAA-NASA 联合档案（NNJA，读音同 ninja）是一个公开可访问的策展型地球系统观测集合，覆盖 1979 年至今，目标有三：加速再分析生产、支撑 AI 应用开发、让用户能直接取到现代再分析背后的观测原始记录。档案囊括 60 多台 NOAA/NASA 及合作方传感器的资料——大气卫星辐射率与常规观测、海洋现场廓线、海冰密集度与干舷反演、陆面观测；大气记录量从 1979 年约 10⁶ 条/日增至现代约 10⁸ 条/日，并通过持续归档 NOAA 业务数据延伸到近实时。数据由 AWS 分发，格式与主流同化系统兼容，并附带通道级黑白名单以记录卫星资料的质量历史；完整性由三层流程校验：文件级元数据检查、与 NOAA/NASA 既有再分析黑白名单交叉验证、同化统计量与参考再分析与业务产品比对。为降低机器学习社区的门槛，配套数据集 NNJA-AI 把遗留格式转成列式 Apache Parquet，支持大规模查询并可直接接入 AI 训练流水线。（Bulletin of the American Meteorological Society）', 'source': 'Bulletin of the American Meteorological Society', 'url': 'https://doi.org/10.1175/bams-d-25-0157.1', 'date': '2026-10-22'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': 'CliMetS 与 MOCSI 两项国际大科学计划在广州南沙启动：以国际共享航次建统一观测方法与数据体系', 'badge': '[要闻]', 'abstract': '2026 大湾区科学论坛（10 月 31 日—11 月 2 日，广州南沙）期间，由南方海洋科学与工程广东省实验室（广州）牵头的两项计划正式启动：联合国「海洋十年」大科学计划「甲烷渗漏对全球气候的影响」（CliMetS）与「科学十年」大科学计划「海洋冷泉界面之谜」（MOCSI），首席科学家分别为钱培元与冯景春。两项计划秉持「共同设计、共同实施、共同拥有」，目前已汇聚全球 50 多个国家、140 多家涉海机构的 220 余位科学家；推进方式包括国际共享航次、跨学科联合研究、定期国际研讨会与培训班，并明确要建立统一的深海冷泉观测方法和数据体系。对国内海洋数据界而言，这意味着又多了一条以「共享航次换共享数据」的多边通道。（科学网 / 中新网）', 'source': '科学网', 'url': 'https://news.sciencenet.cn/htmlnews/2026/11/574029.shtm', 'date': '2026-11-01'}, {'title': '第九次北极考察航次数据产出：双碳同位素揭示北冰洋中心海域碳质气溶胶的本地排放', 'badge': '[论文]', 'abstract': '北极碳质气溶胶通常被归因于中低纬长距离输送，但北冰洋中心海域（尤其夏季）的直接观测长期匮乏。该研究基于中国第九次北极科学考察（「雪龙」号）航次采样，用双碳同位素（δ¹³C—Δ¹⁴C）、分子有机组分与相关示踪指标联合解析北冰洋中心海域碳质气溶胶的来源结构，结果显示本地排放的贡献不可忽略。方法学上，放射性碳（Δ¹⁴C）能直接区分化石源、生物质燃烧与现代碳，与稳定碳同位素和分子标志物联用可把「长距离输送为主」的默认假设检验得更清楚。对北极气溶胶与黑碳气候效应的模式评估，这组航次观测提供了关键约束。（Geophysical Research Letters）', 'source': 'Geophysical Research Letters', 'url': 'https://doi.org/10.1029/2026GL124056', 'date': '2026-11-02'}, {'title': '多年重复 UAV 航测给南极半岛海鸟建可复现基线', 'badge': '[论文]', 'abstract': '南极半岛大片区域的海鸟繁殖调查仍不完整，历史记录又常缺少评估变化所需的空间与方法细节。研究把大范围无人机（UAV）侦察与重点区域高分辨率测绘、重复航测结合起来，为 Destruction Bay—North 一带的地表营巢海鸟建立具有空间明确性的当代基线，并给出可复现的调查流程。相比船基或人工样方计数，UAV 航测的优势在于同一套航线与解译规则可跨年复用，从而把「某年有多少只」变成「同一方法下的年际变化」。这类基准对南极保护区管理与旅游影响评估是基础数据。（Scientific Reports）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-78685-x', 'date': '2026-10-31'}, {'title': '「蓝海101」号赴中西印度洋执行公海渔业资源综合调查：51 人、120 天', 'badge': '[航次]', 'abstract': '10 月 23 日，中国水产科学研究院黄海水产研究所「蓝海101」号调查船从青岛起航，执行「2026 年度中西印度洋公海渔业资源综合科学调查」航次，由黄海所与上海海洋大学合作实施。航次配置 51 名调查人员、计划航期 120 天，调查区域为中西印度洋公海，围绕浮游生物、鱼卵及仔稚鱼、渔业种类组成与数量分布开展多要素综合观测，目标是掌握印度洋重要渔业资源现状、为资源养护与管理积累数据基础。过去三年黄海所已完成 3 个同类航次并产出系列数据报告，本航次延续「航次即数据生产单元」的做法，同时承担青年队伍锤炼与平台共享职能。（黄海水产研究所）', 'source': '黄海水产研究所', 'url': 'http://ysfri.ac.cn/info/1108/59428.htm', 'date': '2026-10-23'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '全国首个海洋大数据应用中心在青岛揭牌：「海数通」上线，700 余项目录、4 个场景落地', 'badge': '[要闻]', 'abstract': '10 月 22 日，在第四届公共数据运营大会上，自然资源部与青岛市人民政府共建的青岛海洋大数据应用中心正式揭牌，「海数通」平台及海洋灾害智能监测预警、船舶船型智能规划等首批应用场景同步发布，海洋大数据应用产业生态社区成立。该中心是自然资源部「1+N」海洋数据布局体系的首个核心节点，由青岛市海洋发展局、自然资源部北海局作为建设主体、青岛市数据集团实施，统筹汇聚部市海洋数据资源、与部「一张图」国家级海洋分库联通，承担数据汇集、共享、流通与应用职能。试点以来部市两级海洋数据目录初步建立，汇集数据目录 700 余项、对接应用需求近百个，建成首批 4 个场景，「海数通」上线运行并联合 50 余家涉海企业、高校院所与金融机构组建生态社区。青岛已建成国内规模最大的海洋领域专用算力集群，形成「超算+智算+边缘计算」协同体系。（中国金融信息网 / 大众新闻）', 'source': '中国金融信息网', 'url': 'https://m.cnfin.com/cmjj-lb//zixun/20261030/4488855_1.html', 'date': '2026-10-22'}, {'title': 'Sentinel-6B 转入业务运行：全球海平面记录续到 2030 年代', 'badge': '[动态]', 'abstract': 'EUMETSAT 宣布哥白尼 Sentinel-6B 于 2026 年 10 月 30 日进入业务服务，其高精度测高数据开始向用户开放，使 1992 年 TOPEX/Poseidon 以来的全球海平面记录得以延续至 2030 年代，并将在数月内成为国际公认的高精度海洋测高参考基准。自 2025 年 12 月起，它与 2020 年发射的孪星 Sentinel-6 Michael Freilich 在 1,336 公里轨道上以 30 秒间隔编队飞行以完成交叉定标；两星合计可覆盖约 95% 的无冰洋面，提供海面高度、海流、波高、风速以及河流湖泊水位。数据采集后约三小时内进入各国天气与海洋预报模式，支撑大西洋冬季风暴、地中海气旋与飓风强度预报及厄尔尼诺/拉尼娜季节预测；公开口径的累计变化是 1992 年 12 月以来全球平均海平面上升超过 11.5 厘米，且速率在加快——最近十年升幅达 4.0 厘米。（EUMETSAT / myScience）', 'source': 'EUMETSAT / 水德科技「深蓝瞭望」', 'url': 'https://www.watertools.cn/news/info/544.html', 'date': '2026-10-30'}, {'title': 'Copernicus Marine 11 月产品更新：西北欧陆架首推日均海面高度，北极上线 3 km 潮汐预报', 'badge': '[数据]', 'abstract': 'Copernicus Marine 服务发布 2026 年 11 月产品路线更新。西北欧陆架（NWSHELF_ANALYSISFORECAST_PHY_004_013、WAV_004_015 等）此次更新要点：首次引入海面高度（SSH）日均产品；新增 7 个去潮（Doodson de-tided）数据集（1 个逐时、6 个逐日）与 5 个月平均数据集，涵盖温、盐、SSH、混合层深度、流、底层温度等变量。北极侧新增「3 km 分辨率、15 层」的北极海面潮汐分析与预报产品（ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015），其潮汐与风暴潮模式此次也同非潮汐 6 km 物理产品一样受海洋与海冰数据同化约束，由 6 km 的 TOPAZ5 EnKF 系统约束 3 km 的 TOPAZ6 确定性潮汐系统。配套安排为 2026 年 11 月 3 日至 2027 年 1 月 12 日双发布期，新旧数据集并行。对做区域再分析衔接与潮汐信号分离的用户，去潮数据集与日均 SSH 是直接影响下游口径的两项变化。（Copernicus Marine）', 'source': 'Copernicus Marine', 'url': 'https://marine.copernicus.eu/fr/user-corner/product-roadmap/transition-information', 'date': '2026-11-01'}, {'title': 'IBRA：伊势湾 12 年逐时全水柱生态水动力再分析，同化底层溶解氧（ESSD）', 'badge': '[数据]', 'abstract': '基于环流—生态耦合模式的再分析数据是理解近岸环境变异、支撑水质管理的核心工具，但封闭性强的海湾、尤其把溶解氧（DO）等次表层生地化观测纳入同化的数据集仍很少。IBRA（Ise Bay Reanalysis）提供了日本伊势湾 2011—2022 年、12 年、逐时、解析全水柱的水动力与生地化再分析数据：由港湾空港技术研究所 EcoPARI 模拟器耦合集合卡尔曼滤波同化系统生成，每 6 小时同化一次水温、盐度与底层 DO 现场观测。三个特点值得关注：一是不同于多数主要依赖卫星观测的再分析，IBRA 同化的是贯穿全水柱的连续现场测量（含高频 DO），改善次表层动力表征；二是 6 小时同化循环使其能解析潮汐驱动的短期变异——潮汐正是近岸输运与混合的主控；三是用 EnKF 在整个海湾施加空间连贯的校正，兼顾物理与生地化场的空间一致性，避免简单同化常带来的人为不连续。统计评估与多站多深度对比显示，同化整体改善与观测的吻合度、底层 DO 尤明显，并成功再现季节变化、垂向层化与内湾缺氧的形成与持续。数据可用于近岸缺氧、水质评估与环境管理研究。（Earth System Science Data）', 'source': 'Earth System Science Data', 'url': 'https://doi.org/10.5194/essd-18-7839-2026', 'date': '2026-10-29'}, {'title': '用 Ricker 小波把「模型对不对」拆到时频平面：标准指标看不见的台站差异（L&O Methods）', 'badge': '[论文]', 'abstract': '评估水动力模式的海面高度时，惯例是与验潮站比较标准差、Pearson 相关系数与中心化均方根误差（cRMSE）。这三个指标紧凑好用，但隐含假设「模式技巧与时序偏差的出现时刻和持续时间无关」——对潮汐弱、以气象强迫为主的海域，这个假设会漏掉关键信息。该研究提出互补做法：用 Ricker 小波变换把观测与模拟的海面高度同时表达到时频空间，取波罗的海（无明显强潮的内海）为案例，运行成熟配置的 NEMO 模式，与芬兰沿岸验潮站逐时数据对比，用小波功率谱及相关量评估模式对中尺度与天气尺度海面扰动的刻画能力，并揭示这些尺度上模式误差的季节性。结果显示谱分析能暴露验潮站之间模式表现的定性差异，而标准非谱指标完全看不出这些差异。对以 RMSE 为唯一验收口径的业务化评估流程，这是一条成本很低的补充路径。（Limnology and Oceanography: Methods）', 'source': 'Limnology and Oceanography: Methods', 'url': 'https://doi.org/10.1002/lom3.70102', 'date': '2026-10-29'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'oceanarray 0.5.1：从原始仪器文件到质控级 CF-NetCDF 的锚系阵列处理流水线', 'badge': '[工具]', 'abstract': '海上锚系阵列的数据处理长期是「每人一套脚本」：各厂商原始文件格式不同、标定与压力网格化步骤繁琐、质控结果难以复核。oceanarray 0.5.1（PyPI 发布于 2026-10-24，MIT 许可，要求 Python 3.11—3.13）把单套锚系的仪器处理做成可编排的流水线：stages 1—3、stacking 与 pressure gridding 各阶段均可单独运行，并为每一阶段生成 HTML 报告；命令行支持 init / validate / process / report，配置走 YAML。它自动依赖 seasenselib 读取 stage 1 的原始仪器文件，标定落差偏移交给 caldip、船基 CTD 处理交给 ctdcast。方法上参考了 RAPID 锚系阵列项目的处理经验，面向 DFG Ocean Array 基础设施项目开发。（PyPI / ocean-uhh）', 'source': 'PyPI', 'url': 'https://pypi.org/project/oceanarray/', 'date': '2026-10-24'}, {'title': 'thermochain v2026.10.3：锚系温度链的时钟与现场温度标定、网格化与漂移校正', 'badge': '[工具]', 'abstract': '锚系温度链（thermistor chain）数据的三个老问题是时钟漂移、传感器间系统偏差与共享涨落型漂移：不处理就无法把「温度变化」与「仪器漂移」分开。Scripps 海洋研究所 Gunnar Voet 发布 thermochain v2026.10.3（Zenodo，2026-10-29），把这三件事做成一套处理工具箱：时钟与现场温度标定、网格化，以及基于共享涨落的漂移校正。代码以 MIT 类开源方式在 GitHub 维护并随版本打 Zenodo DOI，便于在论文中精确引用某一版本。对做上层海洋热含量、内波与混合层长期序列的团队，这类小而专的工具比通用大包更贴合实际流程。（Zenodo / GitHub）', 'source': 'Zenodo', 'url': 'https://doi.org/10.5281/zenodo.23749880', 'date': '2026-10-29'}, {'title': 'CN-Waves：把 HOS-NWT 与 HOS-Ocean 非线性求解器搬进 Python', 'badge': '[工具]', 'abstract': '基于高阶谱（HOS）方法的非线性海况建模长期依赖 HOS-NWT 与 HOS-Ocean 两个求解器，但安装配置与数据后处理门槛较高。CN-Waves 让这两个求解器可在 Python 环境中直接使用：借 wheel 文件把安装过程简化，提供默认数值参数以便快速建立 HOS 配置，并配套多种处理 HOS 模拟数据的工具；同时实现了需要多次 HOS 模拟的波浪生成方法——TR 方法可在给定位置复现目标自由面高程信号，RCW 可估计特定事件的发生概率，所得波浪事件可作为实验或高保真数值模拟的输入，校准程序则用于保证给定位置的波谱与目标谱一致、使极端事件发生频率更接近真实。对极端海浪与海上结构物设计工况研究，这是一条从「造波」到「定概率」的完整链路。（生物通 / 期刊论文）', 'source': '生物通', 'url': 'https://www.ebiotrade.com/newsf/2026-10/20261023104103527.htm', 'date': '2026-10-23'}, {'title': 'WindAnalysis：容器化多服务框架下的海岸风资源评估工作流（MDPI 集团刊，D 级，供参考）', 'badge': '[工具]', 'abstract': '海岸风资源评估越来越依赖异构再分析数据、机组参数、地理空间运算与常驻计算服务的组合。WindAnalysis 是一个容器化 Web 框架，面向哥伦比亚加勒比海岸的风资源研究：其新颖性不在风模型本身，而在架构与运维——把 ERA5 与 MERRA-2 的定时抓取、地理空间处理与结果服务组织成可复现的多服务流水线，而非一次性脚本。对需要长期跑同一套评估口径的团队，这类「工程化封装」比再训练一个模型更能减少结果漂移。（Computers，MDPI 集团刊，D 级，供参考）', 'source': 'Computers（MDPI 集团刊，D 级）', 'url': 'https://doi.org/10.3390/computers15110763', 'date': '2026-10-29'}]}, {'title': '十、补录 · 往期漏检勘误', 'en': 'Errata & Backfilled Items', 'count_as_direction': False, 'items': [{'title': '本次核查说明：4 篇抽查文章中 2 篇补录、1 篇此前已收录、1 篇因双源无摘要不收', 'badge': '[备注]', 'abstract': '应核查的 4 篇文章处置如下。① ESSD《注意力增强 3D-U-Net++ 西北太平洋温盐重构》（10.5194/essd-18-4617-2026）已于 2026-09-04 期方向五收录，当时使用 Copernicus 直链（essd.copernicus.org/articles/18/4617/2026/）而非 DOI 链接，因此按 DOI 做跨期去重比对会出现假阴性——属链接口径记载不全，非漏收。② TGRS《GBM: An Ocean Front Detection Framework》与 ④ TGRS《KunPeng: A Global Ocean Environmental Model》为本次补录条目，原因分列于各自条目。③ The Innovation Informatics《Physics-informed neural networks help to strongly reduce uncertainty in ocean state forecasting》（10.59717/j.xinn-inform.2026.100051）首发 2026-07-20，落在 07-21 期窗口内，但 OpenAlex 的 abstract_inverted_index 与 Crossref 的 abstract 均为空，按「无摘要不收、不得据标题推断摘要」的既定纪律未收录；该刊另一篇（…2026.100031，数字海洋智能综述）已于 04-15 期收录，说明期刊本身在检索范围内，问题在索引侧摘要缺失。补录条目的首发日期早于常规 14 天时效窗口，故本期单列「补录与勘误」板块并逐条标注首发日与漏检原因，不计入常规时效统计与方向条数。核查台账与根因分析见仓库 .workbuddy/memory/2026-11-04.md。', 'source': '', 'date': ''}, {'title': 'KunPeng 全球海洋环境预报模型：把气象大模型技术迁到海洋，15 天全球预报 ACC 0.80（TGRS 补录）', 'badge': '[补录]', 'abstract': 'KunPeng 的出发点是海气物理耦合机制存在相似性，因此把气象领域的大模型技术迁移到海洋域，构建全球海洋环境预报模型。针对海洋空间的不连续特征（陆海边界处场量突变），提出地形自适应掩码约束机制，抑制边界梯度突变引发的训练发散；为同时整合远、中、近距离海洋特征，采用经度循环可变形卷积网络（LC-DCN）增强动态感受野，实现多尺度海洋特征的精细建模；再用可变形卷积增强的多步预测模块（DC-MTP）强化时序依赖特征提取。实验结果：0.25° 分辨率、15 天全球预报平均 ACC 0.80，较对比模型高 0.01—0.08；平均 MSE 0.41（降低 5%—31%）、平均 MAE 0.44（降低 0.6%—21%）；海表参数预报、深海区域表征与流速场预报三类任务提升最明显。作者还横向比较了不同尺度算子在海洋域的适用性，发现在慢变海洋过程下局地算子显著优于全局算子，印证动态特征金字塔表征在海洋物理参数预测中的有效性。补录原因：该文 Crossref 注册日为 2026-06-30，而 OpenAlex 把 IEEE 期刊的 publication_date 统一归一化为 2026-01-01，导致按日期窗口检索永久抓不到——现已改用 Crossref created-date 通道修复该结构性漏检。', 'source': 'IEEE TGRS（补录）', 'url': 'https://doi.org/10.1109/TGRS.2026.3708338', 'date': '2026-06-30'}, {'title': 'GBM 海洋锋检测框架：梯度先验 + 贝叶斯分类 + 形态学精修，替掉黑箱阈值调参（TGRS 补录）', 'badge': '[补录]', 'abstract': '海洋锋是调控热交换、物质输运与生态系统功能的基础动力界面。现有检测方法——直方图法、熵法、Lyapunov 指数法、梯度边缘检测与机器学习——普遍存在锋面碎片化、误检过多、对固定阈值敏感、可解释性与可复现性不足等问题。GBM（Gradient-Bayesian-Morphology）把三个互补环节串成一个物理知情且完全可解释的框架：一是梯度阈值策略，引入强调场量剧变位置的物理先验；二是贝叶斯推断，把梯度先验与局地场描述子结合，实现自适应的锋区数据驱动分类，无需人为调阈值；三是形态学与图方法精修，通过细化锋区、合并碎片段、系统性剔除伪环状结构来强制拓扑一致性。评测用 2022—2024 年南海与黑潮海域的逐日海表温度、盐度场，分别代表弱锋与强锋情形：GBM 有效抑制过度检测，产出锋面的空间连续性更好；统计分析显示锋面特征稳定、参数敏感性低，鲁棒性与可复现性得到验证。作者将其定位为黑箱方法的透明替代，并提供多变量海洋锋的统一分析框架。补录原因：Crossref 注册日 2026-02-03，早于日报系统首期（2026-03-23）运行，属系统上线前的窗口缺口。', 'source': 'IEEE TGRS（补录）', 'url': 'https://doi.org/10.1109/TGRS.2026.3660295', 'date': '2026-02-03'}]}]



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
