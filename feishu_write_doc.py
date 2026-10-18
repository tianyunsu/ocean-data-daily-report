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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'Sub-Eddy-Net：用海表温度影像「看见」高度计分辨不了的亚中尺度涡', 'badge': '[论文]', 'abstract': '亚中尺度涡在海洋能量级串与物质输运中作用关键，但其尺度小于传统卫星高度计的有效分辨能力，直接探测长期受限。研究提出 Sub-Eddy-Net——在 YOLOv8 骨架上引入 SGAM 注意力增强的检测架构——以 MODIS 海表温度（SST）影像为输入，识别南海区域的亚中尺度涡特征，把涡旋在 SST 场中留下的锋面与冷暖异常形态作为判别依据。该思路绕开高度计的分辨率瓶颈，为亚中尺度过程的遥感监测提供了可业务化的技术路径。（Taylor & Francis / GIScience & Remote Sensing）', 'source': 'GIScience & Remote Sensing', 'url': 'https://doi.org/10.1080/15481603.2026.2748224', 'date': '2026-10-15'}, {'title': '公民科学影像 + 深度学习：大堡礁 742 个站点的珊瑚形态覆盖', 'badge': '[论文]', 'abstract': '公民科学能大幅扩展珊瑚礁调查的空间覆盖，但影像质量参差、人工判读慢，长期限制其科研价值。研究整合大堡礁 267 个礁体、742 个站点、46,879 张海底景观影像（2022 年 9 月至 2025 年 2 月由 Great Reef Census 志愿者采集），用深度学习完成珊瑚形态类别的自动判读，产出经校验的大范围珊瑚覆盖数据。该工作证明「志愿采集 + 模型判读」可在保持数据质量的同时把调查规模推到礁体尺度，为礁区长期监测提供了低成本范式。（Wiley / Limnology and Oceanography Letters）', 'source': 'Limnology and Oceanography Letters', 'url': 'https://doi.org/10.1002/lol2.70168', 'date': '2026-10-05'}, {'title': 'ECML PKDD 2026：为海洋碳吸收模式构建深度时间模拟器', 'badge': '[会议]', 'abstract': '海洋碳吸收模式是气候预估的核心组件，但其长时间积分计算代价高昂。该文提出面向海洋碳吸收模型的「深度时间模拟器」（deep temporal emulator），用深度网络学习模式的时间演化行为，以数据驱动方式近似昂贵的数值积分，从而在保持关键响应特征的前提下大幅降低计算成本。成果收录于 ECML PKDD 2026 应用数据科学轨道（Lecture Notes in Computer Science），是本期顶会检索的代表性收获之一。（Springer / ECML PKDD 2026）', 'source': 'ECML PKDD 2026（LNCS）', 'url': 'https://doi.org/10.1007/978-3-032-37682-4_39', 'date': '2026-10-05'}, {'title': 'ION GNSS+ 2026：UUV-NAV 项目攻关水下航行器定位', 'badge': '[会议]', 'abstract': "海上平台、海底管道、通信光缆与海上新能源装置等关键水下基础设施的巡检、测绘、监视与维护，都依赖高精度定位；而水下环境使 GNSS 完全失效，声学定位又受多径与时延制约。论文介绍 ASI 支持的新项目 UUV-NAV，围绕无人水下航行器的定位问题给出系统级方案设计，面向真实基础设施运维场景论证技术路线与精度需求。成果发表于 ION GNSS+ 2026 会议论文集。（ION / Proceedings of the Satellite Division's Meeting）", 'source': 'ION GNSS+ 2026', 'url': 'https://doi.org/10.33012/2026.20644', 'date': '2026-10-07'}, {'title': '物理约束扩散模型为主动声呐小样本「造数据」', 'badge': '[论文]', 'abstract': '真实海上试验的目标回波稀缺，直接制约数据驱动的主动声呐检测模型训练；纯仿真回波的分布又与真实海洋环境存在差异。研究提出物理约束的两阶段无条件扩散模型，用于主动声呐线性调频（LFM）回波时频谱的数据增强：第一阶段学习谱图的一般分布，第二阶段以声呐传播物理约束把生成样本拉回真实海域的统计特性。该方案在低信噪比条件下缓解了样本不足导致的检测性能退化，为水声小样本学习提供了可复用的增强框架。（Elsevier / Ocean Engineering）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128558', 'date': '2026-10-07'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '实时海浪预报：降阶模型 + 序贯同化的混合框架', 'badge': '[论文]', 'abstract': '高分辨率海浪预报业务化成本高，且面向不确定性决策时常常标定不足。研究提出混合预报框架：先用卷积自编码器在 WAM 海浪模式输出上学习海况变化的非线性低维流形（降阶模型），再耦合序贯数据同化，产出流依赖、空间连贯的有效波高集合预报，并以北海为试验区验证。该路线把「降阶」与「同化」两条加速路径合并，为近实时、可给出不确定度的区域海浪预报提供了工程化方案。（Elsevier / Applied Ocean Research）', 'source': 'Applied Ocean Research', 'url': 'https://doi.org/10.1016/j.apor.2026.105282', 'date': '2026-10-08'}, {'title': '图神经网络同化：稀疏观测下的海洋场空间重建', 'badge': '[论文]', 'abstract': '海洋观测在空间上高度稀疏且不规则，传统同化依赖背景误差协方差的建模假设。该研究把数据同化重构为图上的信息传播问题，用图神经网络在稀疏观测点与网格节点之间建立可学习的映射，实现海洋要素场的空间重建。相比格点卷积，图结构更贴合观测网的不规则拓扑与海陆边界，为中尺度涡、近岸锋面等结构的高分辨率重建提供了新工具。（Elsevier / Ocean Modelling）', 'source': 'Ocean Modelling', 'url': 'https://doi.org/10.1016/j.ocemod.2026.102849', 'date': '2026-10-13'}, {'title': '海岸水文数字孪生（HDT）范围综述：目标、数据与方法〔MDPI 刊·预警口径标注〕', 'badge': '[论文]', 'abstract': '海岸带及其连通的水陆系统是受气候灾害影响最直接的环境之一，欧洲政策已把数字孪生基础设施置于气候适应与海洋治理议程核心（DestinE 面向地球系统、EDITO 面向海洋与海岸）。该综述界定并评估「水文数字孪生」（Hydro Digital Twins, HDTs），系统梳理其目标设定、数据特征与方法体系，指出现有 HDT 在观测—模式耦合、不确定度传递与治理接口上的共性缺口。按期刊分级口径，该文发表于 MDPI 旗下期刊，列入 D 级（预警/受限）并标注，供取舍参考，不代表对论文质量的否定。（MDPI / Coasts）', 'source': 'Coasts（MDPI，D 级标注）', 'url': 'https://doi.org/10.3390/coasts6040045', 'date': '2026-10-16'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': '北极冰下三维重建基准：给机器人感知补上「纹理」这一课', 'badge': '[论文]', 'abstract': '北极正走向季节性无冰状态，刻画水下海冰的复杂形态对海-冰-气热交换建模与冰下生境监测至关重要。目前冰下测绘主要依靠多波束声呐，几何尺度可靠，却缺少光谱与高分辨率纹理信息，难以记录细微形态。该文构建面向北极冰下机器人感知的三维重建基准，系统评测光学与声学融合的重建路线在真实冰下环境中的精度与鲁棒性，为冰下自主作业的感知前端给出可复现的对比基线。（arXiv 预印本）', 'source': 'arXiv', 'url': 'https://arxiv.org/abs/2610.19097', 'date': '2026-10-13'}, {'title': '从测深栅格到生态制图：随机森林与 nnU-Net 分割海底巨砾', 'badge': '[论文]', 'abstract': '波罗的海南部以软底为主，地质成因的硬底是生物多样性热点，但缺少开源的像元级巨砾分割方法，制约了对巨砾场生态意义的认识。研究基于多波束测深（MBES）数据，训练并对比两类模型：经典机器学习 APOC-25（随机森林分类）与深度学习 nnU-Net，在人工标注样本上开展大规模巨砾分割，评估两者在精度、样本需求与迁移性上的差异，为底质制图提供了可直接复用的开源工作流。（EarthArXiv 预印本）', 'source': 'EarthArXiv', 'url': 'https://doi.org/10.31223/x5tj8d', 'date': '2026-10-07'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'DriftGuard：给 Argo 浮标漂移做「自主质检」的智能体框架', 'badge': '[论文]', 'abstract': '未被识别的传感器标定漂移会污染支撑气候再分析、季节预报与生态评估的温盐记录。现实是：任意时刻约有 15%–20% 的在役 Argo 浮标存在明显漂移，而人工校正流程需 3–6 个月。DriftGuard 提出五组件自主质检框架，在 135 个（浮标/传感器）构成的物理知情异构图网络上，耦合时序 Transformer 与图注意力网络，实现漂移的自动识别与订正决策，把质检周期从「季」压缩到「近实时」。（Frontiers / Frontiers in Marine Science）', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1977051', 'date': '2026-10-14'}, {'title': '绝对丰度能否互校？荧光显微与定量宏基因组在海洋原核生物上高度一致', 'badge': '[论文]', 'abstract': '带分类分辨率的微生物细胞绝对丰度量化，一直是海洋微生物生态的核心难题：荧光显微计数可靠但无分类信息，组学方法多只能给相对丰度。研究系统比较了荧光显微计数与基于单拷贝标记基因的定量宏基因组在海洋原核生物绝对丰度上的表现，发现两者高度一致。这一结果为「用组学数据反演绝对丰度」提供了实测校准依据，也意味着历史显微计数与新一代组学数据具备可比性。（Oxford / ISME Communications）', 'source': 'ISME Communications', 'url': 'https://doi.org/10.1093/ismeco/ycag297', 'date': '2026-10-14'}, {'title': '再分析资料里的次表层海洋热浪：三套产品的系统性比较', 'badge': '[论文]', 'abstract': '海洋热浪的次表层表现因原位观测稀疏而长期缺乏约束。研究利用 Copernicus 全球海洋再分析集合产品（GREP）中的 CGLORSv7、GLORYS2v4、ORAS5 三个成员，以统一的分位数阈值在 0.5–200 m 多个深度上识别热浪，比较其强度、持续时间与空间异质性，并与已有高置信度事件对照评估。结果揭示了不同再分析在次表层热浪刻画上的分歧，为把再分析用于海洋热浪监测与影响评估划定了不确定度边界。（EGUsphere 预印本）', 'source': 'EGUsphere（Copernicus）', 'url': 'https://doi.org/10.5194/egusphere-2026-5747', 'date': '2026-10-07'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': '水下滑翔机能耗多步预测：VMD 分解 + BiLSTM + 改进灰狼优化', 'badge': '[论文]', 'abstract': '能耗预测精度直接决定水下滑翔机能否完成长续航任务，但能耗序列非平稳、非线性强，常规物理模型与单步预测方法难以给出可靠的多步预报。研究提出混合框架：先用变分模态分解（VMD）把能耗序列自适应拆成若干本征模态分量，降低非平稳性；再用双向长短期记忆网络（BiLSTM）分别建模，并以改进灰狼优化器（IGWO）搜索超参数，最后重构多步预测结果。该「分解—建模—优化」组合为水下长航时平台的能源调度提供了可落地的技术路线。（Elsevier / Ocean Engineering）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128770', 'date': '2026-10-14'}, {'title': 'UPED：声-光-磁三模态水下环境感知高分辨率数据集', 'badge': '[数据]', 'abstract': '水下环境感知需要光学、声学与磁测三类互补模态，但公开数据多只覆盖单一传感器。UPED 在受控海水水池中采集 RGB 图像、多波束声呐图像、激光点云与三轴磁测，覆盖底栖生物、矿产富集、海底管道三类典型场景，包含 2,400 张 RGB 图像、2,400 帧声呐、22 段激光点云序列与 2,600 个磁测样本，其中 2,000 张低重叠 RGB 图像可用于跨模态配准研究。该数据集为多模态融合感知与水下目标识别提供了统一评测底座。（Springer Nature / Scientific Data）', 'source': 'Scientific Data', 'url': 'https://doi.org/10.1038/s41597-026-08422-6', 'date': '2026-10-10'}, {'title': 'PhyEddy-Net：亚 15 公里日尺度全球中尺度涡检测数据集', 'badge': '[数据]', 'abstract': '中尺度涡的自动识别长期在「分辨率」与「一致性」之间取舍。PhyEddy-Net 构建 2010–2021 年、60°S–60°N 无冰海域的日尺度全球涡旋检测数据集，采用物理-数据双驱动的多模态深度学习分割框架，融合海平面异常（SLA）、地转相对涡度与海表温度异常（SSTA）三源信息。每条记录给出涡心、极性（气旋/反气旋）、面积、等效圆半径、检测概率与所属海盆，全目录约 3,670 万条检测，为涡旋统计、输运估算与模式评估提供统一底账。（Copernicus / ESSD Discussion）', 'source': 'Earth System Science Data（讨论稿）', 'url': 'https://doi.org/10.5194/essd-2026-670', 'date': '2026-10-05'}]}, {'title': '六、数据管理与共享', 'en': 'Data Management & Sharing', 'items': [{'title': '《南海海洋大数据 共享交换接口规范》团体标准发布实施', 'badge': '[政策]', 'abstract': '中国海洋工程咨询协会批准发布团体标准《南海海洋大数据 共享交换接口规范》，编号 T/CAOE 124—2026，自发布之日起实施（中海协发〔2026〕28 号，10 月 8 日公告）。标准面向南海海洋大数据的跨机构共享交换，规范接口层的数据组织与调用方式，填补了区域海洋大数据在「可交换」环节的标准空白。对长期受制于格式不一、接口各异的南海数据汇聚而言，这是从「各自建库」走向「互联互通」的制度性一步。（中国海洋工程咨询协会）', 'source': '中国海洋工程咨询协会', 'url': 'https://www.caoe.org.cn/newsinfo/11346455.html', 'date': '2026-10-08'}, {'title': '地中海与黑海过渡水域浮游植物个体级性状数据集（已协调统一）', 'badge': '[数据]', 'abstract': '过渡水域位于淡水与海水交汇带，环境梯度剧烈，浮游植物群落响应复杂，但性状数据分散在不同项目与格式中。该数据集把地中海与黑海过渡水域的浮游植物性状整理到个体级、并完成跨来源的术语与单位协调，使不同航次、不同实验室的观测可在同一口径下比较。这类「协调而非简单汇总」的数据整编，是区域生态数据可复用、可合并分析的前提。（Pensoft / Biodiversity Data Journal）', 'source': 'Biodiversity Data Journal', 'url': 'https://doi.org/10.3897/bdj.14.e196603', 'date': '2026-10-12'}, {'title': 'EMODnet Chemistry 化学数据开通 OGC WFS 服务', 'badge': '[数据]', 'abstract': 'EMODnet Chemistry 通过 SeaDataNet 的通用数据索引（CDI）服务，为海洋化学数据发布符合 OGC WFS 1.1.0 规范的地理要素服务，覆盖酸化指标、防污剂、叶绿素、溶解气体、重金属、碳氢化合物、持久性有机污染物、放射性核素、硅酸盐等要素（元数据 10 月 7 日更新）。相较以往的下载式分发，WFS 让用户能把化学观测直接接入 GIS 与工作流，是「数据共享」从文件交换转向服务调用的一步。（EMODnet / SeaDataNet）', 'source': 'EMODnet Chemistry', 'url': 'https://emodnet.ec.europa.eu/geonetwork/srv/api/records/231b288d794fefd50853ea4b395504e3470ac489', 'date': '2026-10-07'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '南大洋冰系浮标阵列布放：把「相对冰缘」写进优化目标', 'badge': '[论文]', 'abstract': '南大洋边缘冰区对气候动力学与海冰模式验证至关重要，却因布放成本高、浮标寿命短而严重欠采样；更棘手的是冰缘年际摆动可达数百公里，按固定经纬度优化的阵列在未知冰情下会整体失效。研究提出以「相对冰缘特征」编码浮标位置的多目标优化框架，使同一套基因型可适应年际变化，用 NSGA-II 同时优化空间覆盖与船只作业成本，并基于 39 年极地海冰数据训练。该思路把「冰情不确定性」前置到观测设计阶段，对极区观测网规划具有直接参考价值。（EarthArXiv 预印本）', 'source': 'EarthArXiv', 'url': 'https://doi.org/10.31223/x5x81x', 'date': '2026-10-13'}, {'title': '水下滑翔机主动声学：把昼夜垂直迁移与锋面关系「听」出来', 'badge': '[论文]', 'abstract': '船基采样难以支撑对动态生物物理过程的高频重复观测。研究在美国西北太平洋华盛顿州近岸锋区，利用自主水下滑翔机搭载的多频主动声学系统，连续观测昼夜垂直迁移（DVM）以及浮游动物与鱼类聚集体的关系，检验滑翔机平台在锋面尺度上刻画生物量垂直结构的能力。相比船基断面，滑翔机以更低成本获得更高的时间连续性，为渔业声学与生态动力学研究提供了新的观测范式。（Frontiers / Frontiers in Marine Science）', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1944587', 'date': '2026-10-15'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'GEBCO 常设秘书处在摩纳哥成立：全球海底测绘有了「常驻中枢」', 'badge': '[动态]', 'abstract': '10 月 13 日，摩纳哥亲王阿尔贝二世与 IOC/UNESCO、IHO 负责人共同为 GEBCO（通用大洋水深图）常设秘书处揭幕，秘书处设于摩纳哥 IHO 办公区。GEBCO 是唯一拥有国际授权、以测绘全部海底为使命的计划，此前长期缺少专职协调机构。据 2026 年 4 月发布的 GEBCO_2026 全球网格，目前 28.7%（约 1.04 亿平方公里）的海底已按现代标准测绘，220 家机构贡献过数据；秘书处的核心任务之一是推动更便利的海洋数据共享政策环境。（IOC/UNESCO）', 'source': 'IOC/UNESCO', 'url': 'https://www.ioc.unesco.org/en/articles/permanent-home-ocean-mapping-gebco-secretariat-inaugurated-monaco', 'date': '2026-10-13'}, {'title': '122 种海洋外来动物全球分布数据集在国家地球系统科学数据中心发布', 'badge': '[数据]', 'abstract': '国家地球系统科学数据中心 10 月 8 日上线「122 种海洋外来动物全球分布数据集」，数据量 33.28 GB，含 122 个物种的全球地理分布记录（CSV）与基于物种分布模型（SDM）预测的当前及未来潜在适宜分布（TIF，3 弧分），覆盖 SSP2-4.5 与 SSP5-8.5 两种情景下的 2040–2050 与 2090–2100 时段，并配有 DOI/CSTR 标识。该数据集把入侵物种风险的空间预估做成可直接复用的标准化产品，为海洋生物多样性保护与航运压力量化提供基础底图。（国家地球系统科学数据中心 / 中科院南海海洋所）', 'source': '国家地球系统科学数据中心', 'url': 'https://www.geodata.cn/data/datadetails.html?dataguid=30378725417220', 'date': '2026-10-08'}, {'title': '第五届全国智慧海洋大数据与 AI 大赛 25 强出炉，10 月 27 日钦州路演', 'badge': '[动态]', 'abstract': '由国家海洋信息中心、广西海洋局、钦州市政府联合主办，国家海洋科学数据中心等单位承办的第五届全国智慧海洋大数据与人工智能应用创新大赛公布晋级赛 25 强：84 件有效作品中遴选 25 件，覆盖智慧渔业、海洋生态预警、海洋灾害研判、海洋三维数字孪生、海上风电管控、水声感知巡测、海洋垂域大模型与多智能体、水下机器人与无人船等场景。赛事以「智慧海洋赋能产业发展、通江达海聚力东盟合作」为主题，10 月 27 日将在钦州举行成果路演，是观察国内海洋数据要素化应用落地的一个窗口。（国家海洋信息中心）', 'source': '国家海洋信息中心（经网易转载）', 'url': 'https://dy.163.com/article/L983SJ9N0511KMS0.html', 'date': '2026-10-14'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code', 'items': [{'title': 'Metocean-stats v1.2：把海洋气象统计分析做成可复现的开源框架', 'badge': '[开源]', 'abstract': '海洋气象（metocean）分析是海上与海岸工程、海事作业与海上新能源开发的基础，需要可靠估计风、浪、流、水位等要素的极值与长期统计特征。现实是大数据集已不稀缺，但分析多靠临时脚本与碎片化流程，可复现性差。Metocean-stats v1.2 把这些分析固化为开源 Python 框架，提供从数据读取、质量控制到极值统计与报告输出的可复现流水线，并给出可直接用于工程决策的结果组织方式。（Elsevier / Applied Ocean Research）', 'source': 'Applied Ocean Research', 'url': 'https://doi.org/10.1016/j.apor.2026.105257', 'date': '2026-10-15'}, {'title': 'DATRASextra：把 ICES 底拖网调查数据的关系型表「一键」整理成可分析工作流', 'badge': '[开源]', 'abstract': '科学底拖网调查提供渔业独立的长期数据，是渔业与生态系统研究的基础；ICES DATRAS 汇集了东北大西洋多个长期调查的网次信息、种与体长别渔获以及个体生物学观测，但多张关系型表之间的整合与复现一直是门槛。DATRASextra 以 R 包形式提供标准化工作流，把下载、联接、筛选与派生指标封装为可复现步骤，降低跨调查、跨年份比较的技术摩擦。（Elsevier / SoftwareX）', 'source': 'SoftwareX', 'url': 'https://doi.org/10.1016/j.softx.2026.103108', 'date': '2026-10-07'}, {'title': 'oceantide 0.9.0：在 xarray 上做「惰性」潮汐调和预报', 'badge': '[开源]', 'abstract': 'oceantide 0.9.0 于 10 月 18 日发布，为持有潮汐调和常数的 xarray.Dataset 增加 `tide` 访问器，可直接由调和常数预报水位与潮流。其预报对分潮、时间与空间同时向量化，并在常数由 dask 承载时保持惰性计算，因此大网格上的长时间序列可以流式生成而不必整体载入内存。对需要把潮汐信号从观测或模式结果中分离的海洋数据处理流程而言，这类「随数据一起算」的设计显著降低了工程复杂度。（PyPI / Oceanum）', 'source': 'PyPI（Oceanum）', 'url': 'https://pypi.org/project/oceantide/0.9.0/', 'date': '2026-10-18'}]}]



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
