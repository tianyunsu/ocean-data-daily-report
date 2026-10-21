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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'NeurIPS 2026：小波域优先级扫描破解无人机海上小目标检测', 'badge': '[会议]', 'abstract': '低空无人机海上影像中的目标尺度小、边界响应弱，又易被海浪、尾迹与反光等结构化杂波干扰；空间域增强难以区分「弱目标证据」与「高频杂波响应」。天津理工大学团队提出 PRISM 框架：先用小波分解金字塔把图像拆成方向性高频信息与低频场景上下文，由专用编码器独立建模以保持频率分离；再用优先级引导融合模块学习图像自适应的连续优先级图，据此决定局部因果特征精炼的扫描顺序；最后用小波合成解码器级联逆变换重建多尺度检测特征。PRISM 在 SeaDronesSee 与 AFO 两个海上数据集上达到 SOTA，显著提升了结构化杂波下的小目标检测与密集目标召回。（NeurIPS 2026 / 天津理工大学）', 'source': 'NeurIPS 2026', 'url': 'https://cs.tjut.edu.cn/info/1001/2984.htm', 'date': '2026-10-16'}, {'title': '海洋科学 AI 全景综述：八大学科的应用版图与瓶颈清单', 'badge': '[综述]', 'abstract': '海洋数据的特点是「量大而分布不均」——卫星、自主平台、传感器、船舶与基因组工具各自产出异构数据。该综述系统梳理了 AI/ML 在物理海洋学、海岸灾害、海洋生物地球化学、生态学、遥感、声学、海洋地质与应用海洋工程八大领域的应用现状，检视各领域的方法选择、验证策略与主要失效模式。研究采用文献合成工作流（Schlitsummarizer 辅助 + 全文抽取）识别趋势与缺口，为跨领域方法迁移提供了可对照的基线。（Frontiers in Marine Science）', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1890995', 'date': '2026-10-15'}, {'title': '南海所 DLSCR：用 7 个海表变量重建印-太交汇区 643 米深三维次表层流', 'badge': '[论文]', 'abstract': '次表层洋流在能量传递与物质输运中作用关键，但观测稀疏、数值同化代价高。中科院南海海洋研究所杜岩、张玉红团队以 Swin-UNet 为骨架构建 DLSCR 模型，输入海表流速、海表高度、温度、盐度及风应力等 7 个海表变量，实现印-太交汇区 1/12° 分辨率、最深约 643 米的三维次表层洋流重建（训练评估基于 1993—2022 年 GLORYS12 与 ERA5 逐日再分析）。2020—2022 年独立测试中，纬向与经向流速平均 RMSE 分别为 0.060 与 0.056 m/s，优于 U-Net、TransUNet 等基线，在 100—200 米温跃层表现尤佳，并经 ADCP 实测与 HYCOM 跨数据集检验。扰动实验显示海表流速是最关键输入（替换后 RMSE 上升 9.2%—11.0%），海表高度次之（2.9%—3.9%）。（IEEE JSTARS / 中科院南海海洋研究所）', 'source': 'IEEE JSTARS', 'url': 'https://www.ebiotrade.com/newsf/2026-10/20261017090325761.htm', 'date': '2026-10-17'}, {'title': 'XCAT-UIR：可解释交叉注意力让水下图像复原不再是「黑箱」', 'badge': '[论文]', 'abstract': '水下图像因光的吸收与散射普遍存在波长相关的颜色衰减、散射模糊与目标细节丢失，多种畸变叠加使其复原比常规图像增强更困难。研究提出 XCAT-UIR——以 ConvNeXt-Transformer 混合架构为骨干，引入交叉注意力模块在同一框架内整合局部细节与全局上下文，并附加可解释性设计，使模型对「哪部分特征驱动了复原结果」给出可回溯的依据。该工作面向水下探测与海洋工程巡检中的视觉前端，为深度学习水下复原方法的可信部署提供了新思路。（Scientific Reports）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-76042-6', 'date': '2026-10-17'}, {'title': 'EAU-Net：给 SAR 近岸分割补上「边缘感知」这一环', 'badge': '[论文]', 'abstract': 'SAR 具备全天候成像能力，是观测海面的重要手段，但把陆岸从海面中分离出来一直困难：相干斑噪声、侧视几何造成的几何畸变、以及沿岸建筑多次散射导致的特征混叠三者叠加，使近岸带成为分割的薄弱区。研究提出边缘感知增强注意力 U-Net（EAU-Net），在编码—解码结构中引入 SAR 散射特性与边缘增强机制，针对上述三类干扰分别设防。该框架面向近岸带自动制图与海岸线提取，对海洋测绘与近岸灾害监测具有直接应用价值。（SAE Technical Paper）', 'source': 'SAE Technical Paper', 'url': 'https://doi.org/10.4271/2026-99-2910', 'date': '2026-10-19'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '物理信息 LSTM 网络：动态海况下浮标的短期漂移轨迹预测', 'badge': '[论文]', 'abstract': '海上浮标在动态环境强迫下位置持续变化，能否准确预测其短期位移，直接影响航行安全、维护计划与搜寻回收成本。纯物理模型依赖精确的水动力与气象参数，而既有数据驱动方法多用浅层单向循环结构，难以充分挖掘历史观测中的时序上下文。研究提出物理信息 LSTM 网络（Physics-informed LSTMNet），把物理约束嵌入深层时序建模，在动态海洋环境条件下提升短期轨迹预测精度，为助航设施运维与海上搜救提供了更可靠的预测工具。（Frontiers in Marine Science）', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1953622', 'date': '2026-10-19'}, {'title': '船舶动力装置数字孪生：0D–1D 过程模型 + 逆向辨识做故障归因', 'badge': '[论文]', 'abstract': '船用内燃机的状态监测与参数偏离归因，直接关系船舶动力装置的安全经济运行。研究构建了一套面向船用发动机诊断的数字孪生框架，并演示了与 DEPAS 5.0W 诊断系统的集成：以标定后的 0D–1D 发动机过程模型为物理内核，结合传感器数据识别当前运行工况、生成参考状态、再通过逆向辨识定位参数偏离的成因。该框架把「物理模型—实测信号—诊断结论」串成闭环，为船舶动力系统的预测性维护提供了可落地的数字孪生范式，也为海洋装备数字孪生提供了方法样板。（Applied System Innovation，MDPI 集团刊，预警/受限，供参考）', 'source': 'Applied System Innovation（MDPI 集团刊，D 级，供参考）', 'url': 'https://doi.org/10.3390/asi9100212', 'date': '2026-10-10'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': 'web-ocean：单文件 WebGPU 实时海洋渲染器，六级 FFT 从千米波到毫米涟漪', 'badge': '[开源]', 'abstract': '这是一个从零编写、不依赖任何引擎或渲染库的实时海洋渲染器，整个管线装进一个自包含 HTML 文件（压缩后约 61 KB），可直接从本地文件打开。海面采用 Tessendorf FFT 模拟，六层级联各 256×256 采样，覆盖约 1.1 千米到 0.26 米的尺度——单一层无法同时承载长涌浪与细毛细波，六层堆叠正是为了兼顾二者；浪尖泡沫由表面雅可比行列式生成，配以物理化日落天空、AgX 色调映射与自由相机。谱采用受风区限制的 JONSWAP 风浪叠加 Donelan-Banner 方向扩散，并含毛细项色散关系；逆 FFT 以 radix-2 计算着色器在 workgroup 内存中实现。MIT 许可，适合作为海洋可视化教学与演示的可读参考实现。（GitHub / Noniv）', 'source': 'GitHub', 'url': 'https://github.com/Noniv/web-ocean', 'date': '2026-10-17'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'ARMS-gb v2.0：把地基微波辐射计的快速辐射传输推到全天候条件', 'badge': '[论文]', 'abstract': '地基微波辐射计能连续、全天候观测边界层温湿廓线，弥补了近地面观测的关键空白；而要把辐射亮温转成物理量，需要快速辐射传输模式作正演。ARMS-gb v2.0 新增了水凝物吸收与散射模块，并引入基于离散纵坐标叠加法（ADOM）的多重散射求解器，使模式从晴空扩展到全天空（含云、降水）条件。这一升级直接提升了云雨条件下边界层温湿反演的数据可用性与质量控制水平，对沿海与海上观测站的资料同化有实际意义。（Geoscientific Model Development）', 'source': 'Geoscientific Model Development', 'url': 'https://doi.org/10.5194/gmd-19-9957-2026', 'date': '2026-10-19'}, {'title': '南极半岛关键原材料浓度实测：生态风险指数需要为「新污染物」重新标定', 'badge': '[论文]', 'abstract': '关键原材料（CRM）因技术用途广泛而进入偏远海洋环境，正在成为一类新兴无机污染物，但其在南极水体中的赋存、分布与生态意义长期不清楚，且现成的生态风险指数并未针对 CRM 作适配。研究依托 2023—2025 年三次土耳其南极考察，在半岛与马蹄岛 21 个站位采集表层水，用电感耦合等离子体质谱测定痕量与超痕量浓度，据此重新标定潜在生态风险指数。该工作为极地水体新型污染物的数据质量与风险评价口径提供了基线依据。（Marine Pollution Bulletin）', 'source': 'Marine Pollution Bulletin', 'url': 'https://doi.org/10.1016/j.marpolbul.2026.120446', 'date': '2026-10-13'}, {'title': '知识驱动还是数据驱动：海岸带机器学习框架的方法学对比', 'badge': '[论文]', 'abstract': '海岸带研究中的机器学习应用正快速增加，但「把领域知识前置为约束」与「纯数据驱动」两条路线的适用边界并不清晰。该文在同一海岸带问题上并列构建知识驱动与数据驱动两类机器学习框架，从预测精度、样本需求、可解释性与外推稳健性四个维度作对照评估，讨论各自的适用条件与失败模式。对需要在数据稀疏海岸带做可靠推断的研究者而言，这类方法学对照比单一模型的精度报告更有决策价值。（Ocean & Coastal Management）', 'source': 'Ocean & Coastal Management', 'url': 'https://doi.org/10.1016/j.ocecoaman.2026.108411', 'date': '2026-10-19'}, {'title': '台风暴雨的雷达定量降水估计：先优化双偏振资料质量，再谈精度', 'badge': '[论文]', 'abstract': '雷达定量降水估计（QPE）是防灾减灾的关键环节，但山区地形遮挡低仰角波束会造成近地面降水观测缺失，比差分相移 KDP 的反演误差又进一步限制精度。研究以防城港与北海两部 S 波段双偏振雷达为基础，联合地面雨量计、本地雨滴谱（DSD）资料与 DEM 高程数据，采用混合扫描仰角策略并对双偏振参量作质量控制优化，在台风暴雨过程中提升 QPE 精度。该思路的价值在于把「资料质量」前置为精度提升的前提，而非直接堆叠反演算法。（Remote Sensing，MDPI 集团刊，预警/受限，供参考）', 'source': 'Remote Sensing（MDPI 集团刊，D 级，供参考）', 'url': 'https://doi.org/10.3390/rs18203504', 'date': '2026-10-13'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'MCMC 采样器直接估计海洋低频变率：地中海的观测约束重建', 'badge': '[论文]', 'abstract': '气候预估的技巧取决于模式能否重现系统的长期低频变率，因此需要用观测检验模式的低频统计量。研究提出一种方法：借助一个先验长期模拟的统计量，从原始观测中直接估计海洋变率的低频分量，并显式处理模式偏差、给出拟合观测所需的订正量。估计由 MCMC 采样器完成，并以地中海为对象重建其低频变率。该方法的通用性在于——它把「模式统计先验 + 观测约束」组合成可计算的估计问题，可迁移到其他海区的低频信号提取。（Ocean Science）', 'source': 'Ocean Science', 'url': 'https://doi.org/10.5194/os-22-3207-2026', 'date': '2026-10-19'}, {'title': '水动力 + 机器学习混合框架：海岸侵蚀与淤积的联合预测', 'badge': '[论文]', 'abstract': '海岸侵蚀与淤积是岸线管理的核心问题，纯水动力模型受限于参数率定与计算成本，纯数据模型又难以保证物理一致性。研究构建水动力与机器学习耦合的混合框架：以水动力过程提供物理骨架与特征，由机器学习模型承担非线性映射与预测，面向海岸冲淤变化给出联合预测。这类「物理 + 学习」的混合路线近年在海岸带预报中快速普及，其关键在于两边如何分工——该文给出了可复用的耦合设计。（Earth Science Informatics）', 'source': 'Earth Science Informatics', 'url': 'https://doi.org/10.1007/s12145-026-02274-9', 'date': '2026-10-19'}, {'title': '用聚类 + 分类器客观定义「气象季节」，并投影到未来气候', 'badge': '[论文]', 'abstract': '气象季节通常用固定日历区间或地区阈值定义，无法反映年循环的真实变率。研究提出机器学习框架：先用径向约束聚类（RCC）从再分析资料中客观识别季节，再训练多项式逻辑回归分类器（MLRC），把同一套季节定义应用到气候模式预估上，从而保证「历史识别」与「未来投影」使用一致口径。以印度次大陆为用例，该方法使季节边界的移动可以被定量追踪，为季风区气候影响评估提供了更严谨的时间分段依据。（JGR: Atmospheres）', 'source': 'JGR: Atmospheres', 'url': 'https://doi.org/10.1029/2025jd045869', 'date': '2026-10-15'}, {'title': '数据驱动风暴潮模型：把潮汐与波浪效应真正纳入输入', 'badge': '[论文]', 'abstract': '数据驱动的风暴潮预报常只以水位与气象场为输入，忽略潮汐与波浪的耦合贡献，导致极端条件下的峰值与相位偏差。研究通过在数据驱动模型中显式整合潮汐与波浪效应，改善风暴潮模拟精度。对沿海预警而言，这类改进的意义在于让纯数据模型在强天气过程中不至于「失准」，从而可与业务化数值模式形成互补。（Journal of Marine Systems）', 'source': 'Journal of Marine Systems', 'url': 'https://doi.org/10.1016/j.jmarsys.2026.104319', 'date': '2026-10-13'}, {'title': '多源深度学习重建北极海冰厚度：把稀疏观测拼成月尺度场', 'badge': '[论文]', 'abstract': '北极海冰厚度是气候系统中最难连续观测的关键变量之一：仰视声呐、卫星测高与现场钻测各有覆盖盲区，单一来源难以给出连续场。研究采用多源数据融合的深度学习方案重建月尺度北极海冰厚度，把不同平台观测的互补性转化为可用的格点产品。这类重建对航道安全、冰情预报与气候模式评估都有直接价值，也提示海冰数据产品的误差结构需要随源组合变化而重新刻画。（Journal of Marine Science and Engineering，预警/受限刊，供参考）', 'source': 'JMSE（MDPI 集团刊，D 级，供参考）', 'url': 'https://doi.org/10.3390/jmse14201909', 'date': '2026-10-14'}]}, {'title': '六、数据管理与共享', 'en': 'Data Management & Sharing', 'items': [{'title': 'Metacontextify：用地球观测数据自动补全海洋宏基因组样本的环境元数据', 'badge': '[工具]', 'abstract': '环境元数据是让宏基因组数据产生生物学洞见的前提——没有环境背景，就难以分析微生物群落与环境、基因组内容与蛋白层面适应之间的关系。然而为样本补全标准化环境背景一直很困难：用地球观测数据反查缺失元数据虽可行，却需要时空坐标匹配、并处理专业格式的大型环境数据集，形成实际门槛。Metacontextify 把这一流程自动化，为海洋宏基因组样本生成标准化环境注释，直接服务于数据的可复用性与跨库整合。（BMC Bioinformatics）', 'source': 'BMC Bioinformatics', 'url': 'https://doi.org/10.1186/s12859-026-06660-4', 'date': '2026-10-17'}, {'title': '珊瑚脱氧实验需要统一口径：方法学分歧正在阻碍知识积累', 'badge': '[论文]', 'abstract': '脱氧（海洋中生物可用氧的全球性流失）是造礁珊瑚面临的普遍且加剧的威胁，需要协同研究才能理解与管理。但随着珊瑚脱氧实验快速增多，方法学缺口也开始显现：研究显示，该领域的分歧主要来自关注的表型不同、脱氧暴露方式不同与实验执行细节不同，三者叠加使生物学变异与技术性变异难以区分，限制了集体知识的生产。文章因此提出标准化建议，为跨实验室结果可比与数据共享奠定基础。（Communications Biology）', 'source': 'Communications Biology', 'url': 'https://doi.org/10.1038/s42003-026-11025-x', 'date': '2026-10-19'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '深蓝瞭望第 2 期：美属萨摩亚深海测绘收官与国产声学装备密集出海', 'badge': '[动态]', 'abstract': '本期行业观察覆盖 10 月 11—13 日动态。航次侧，NOAA「Okeanos Explorer」号正在美属萨摩亚周边执行本年度第二阶段深海测绘航次（EX2607，9 月 24 日—10 月 19 日），以潜水器与多波束等传感器对深海底质作绘图与表征，作业画面每日对外直播，所获数据全部公开，服务于海底关键矿产评估与海洋管理。装备侧，美国 Klein Marine Systems 发布面向无人潜航器的 MANTIS UUV 多通道侧扫声呐——电子单元直接嵌入换能器阵列以压缩体积功耗，动态聚焦、多次观测与自适应波束形成保证不同航速量程下成像稳定，支持机载实时处理与以太网接口，反映「传感器为无人平台原生设计」的新趋势。学界侧，中科院声学研究所提出节律感知时-频增强方法（RASTE），以注意力机制筛选优质频带，从船舶辐射噪声中提取轴频、叶频特征，公开数据集上识别精度 80.78%，加入脉冲干扰后仍保持 78.15%，优于传统 DEMON 处理与深度基线模型。（水德科技「深蓝瞭望」）', 'source': '水德科技 · 深蓝瞭望', 'url': 'https://www.watertools.cn/index.php/news/info/490.html', 'date': '2026-10-13'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '日本四家联手提出「港内浮式数据中心」：把算力泊在码头边', 'badge': '[动态]', 'abstract': 'AI 训练集群推高电力与土地需求，合适站址愈发稀缺、建设周期拉长。NYK 航线、NTT Facilities、Eurus Energy 与三菱日联银行于 10 月 14 日联合发布「港内浮式数据中心」概念：把浮式数据中心系泊在港区码头旁，直接复用既有光纤登陆、本地电网与运维人力，从而回避独立海底电缆与远程运维物流的早期难题。四方分工明确——NYK 主导整体开发与商业策略，NTT Facilities 负责设计建造与稳定性技术验证，Eurus 研究海上风电等可再生能源接入，MUFG 设计融资与合伙结构。该概念建立在横滨 Osanbashi 码头已运行的试验之上（25 米×80 米浮式系泊、集装箱式数据中心、光伏加储能供电）。相较更远海方案，港内模式是从「近岸」走向「离岸」的务实过渡。（Blackridge Research / NYK 等四家联合发布）', 'source': 'NYK · NTT Facilities · Eurus · MUFG', 'url': 'https://www.blackridgeresearch.com/news-releases/nyk-ntt-facilities-eurus-energy-and-mufg-bank-unveil-port-based-offshore-floating-data-center-concept', 'date': '2026-10-14'}, {'title': '海上天然气就地供电建数据中心：Riverway 与 Offshore Data Center 合作', 'badge': '[动态]', 'abstract': '美国 Riverway Group 与 Offshore Data Center 达成合作，在美湾沿岸设计建造海上数据中心平台，思路是把「搁置或低价值天然气」就地转化为电力，供同址算力设施使用——省去登岸管道与输电线路，并大幅削减冷却开支。方案覆盖从面向大规模 AI 训练的 1 GW 级设施，到面向边缘推理的小型低成本配置；平台采用闭式深海冷却系统（冷却可占数据中心能耗约 40%），并结合 Riverway 自动化焊接与半潜式船体设计，宣称船体较常规设计轻至 50%。这类「算力随能源下海」的模式，正在把海洋工程与 AI 基础设施两条产业链捆到一起。（World Oil）', 'source': 'World Oil', 'url': 'https://worldoil.com/news/2026/10/14/offshore-data-center-taps-riverway-to-build-stranded-gas-data-center-platforms/', 'date': '2026-10-14'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'oceandatr：一条命令拉齐全球海洋空间数据，R 语言版', 'badge': '[开源]', 'abstract': '对海洋研究者来说，找数据常常和用数据一样费劲：海底深度、海山位置、海表温度散在不同来源，格式与尺度各异，需要大量代码把它们拼到一起。UCSB 环境市场实验室（emLab）团队把日常重复使用的取数与整理脚本固化成 R 包 oceandatr——用一条命令即可访问并整理多类全球海洋数据集，直接进入分析与制图。它的一项关键能力是跨源标准化：例如水深数据为 15 角秒（约 0.25°）分辨率，而捕捞努力量可达 0.01° 或 0.1°，包会在后台把不同尺度拉到一致，用户也可自带数据并指定目标空间尺度。论文发表于 Ecology and Evolution，代码托管于 GitHub（emlab-ucsb/oceandatr），团队称其为会持续演进的「living package」。（UC Santa Barbara / Ecology and Evolution）', 'source': 'UC Santa Barbara', 'url': 'https://news.ucsb.edu/2026/022878/new-tool-makes-mapping-ocean-easier', 'date': '2026-10-19'}, {'title': 'pyaro 0.3.3：气溶胶/大气成分观测的 Python 统一读取层', 'badge': '[工具]', 'abstract': 'pyaro 是面向大气成分观测数据的 Python 读取与统一接口层，把来自不同观测网络与文件格式的数据（如气溶胶光学厚度、颗粒物浓度等）映射到一致的数据模型，便于跨网络比对与再分析。0.3.3 版于 2026 年 10 月 9 日发布。对海洋大气与海气交换研究而言，这类「多源观测统一读取」工具能显著降低把船载、站点与遥感资料拼到一起的成本。（PyPI）', 'source': 'PyPI', 'url': 'https://pypi.org/project/pyaro/', 'date': '2026-10-09'}]}]



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
