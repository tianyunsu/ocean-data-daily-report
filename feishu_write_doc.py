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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'NeurIPS 2026 收录同济大学三篇论文：PhysTC 台风数据集与架构、Blind-Window 实时基准', 'badge': '[顶会]', 'abstract': 'NeurIPS 2026 录用结果公布，同济大学智能机器人与计算感知实验室共 3 篇论文被录用（2 篇 Main Track、1 篇 ED Track，均为 Poster）：PhysTC 提出面向高精度热带气旋预报的物理增强数据集与架构（ED Track）；Blind-Window Forecasting 面向热带气旋构建实时基准与多模态重建（Main Track）。本届 Main Track 接收投稿 30709 篇、录用 7900 篇（25.7%）。', 'source': '同济大学智能机器人与计算感知实验室', 'url': 'https://robot.tongji.edu.cn/info/1253/2999.htm', 'date': '2026-09-25'}, {'title': 'OCEANS 2026 Monterey：跨多样沿海环境评测视觉语言模型', 'badge': '[顶会]', 'abstract': 'IEEE OES/MTS 主办的 OCEANS 2026 Monterey 录用论文面向沿海机器人感知，构建了含 1000 余张图像、18 个语义类、7400 余个标注实例的密集标注沿海数据集（夏威夷欧胡岛三区域七次任务），并通过 text-to-mask、mask-to-mask、mask-to-text 三类实验评测 7 个现代视觉语言模型。结果显示大范围景观类识别普遍优于常规对象与沿海概念类，但同类对象在沿海与陆地数据集间无系统性差异，低性能更多来自分割与语言表征而非环境本身，提示海洋 VLM 评测与提示词设计需重新校准。（本条为顶会录用类重要性豁免条目）', 'source': 'OCEANS 2026 Monterey / arXiv (cs.CV)', 'url': 'https://arxiv.org/abs/2609.10855', 'date': '2026-09-09'}, {'title': 'Wind-GeoDiff：改进 3D-Geoformer 的两阶段框架预测南海有效波高', 'badge': '[论文]', 'abstract': 'Ocean Engineering 刊文提出两阶段深度学习框架 Wind-GeoDiff，将改进的 3D-Geoformer 与扩散式细化模块结合，用于南海有效波高（SWH）时空预测。研究强调 SWH 预报对海洋混合层模拟、海表温度与大气边界层的重要意义，以及其对海洋工程与航行安全的直接价值，为区域海浪智能预报提供新架构。（齐鲁工业大学、山东省科学院）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.128340', 'date': '2026-09-26'}, {'title': 'DDSF-UNet：双域空间—频率学习的水下图像增强', 'badge': '[论文]', 'abstract': 'Scientific Reports 刊文针对水下成像中波长相关光吸收、散射与环境噪声导致的低能见度、偏色与细节丢失问题，提出 DDSF-UNet 双域空间—频率学习框架，跳出仅依赖空间域卷积的既有范式，显式变换与调制频域表征以恢复细节，在多个水下图像基准上取得领先表现，作者单位含中国海洋大学。', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-72013-z', 'date': '2026-09-28'}, {'title': '神经网络专家混合模型：面向流式细胞术浮游植物性状的环境响应建模', 'badge': '[论文]', 'abstract': 'Environmetrics 刊文面向海洋流式细胞术单细胞光学观测数据，提出神经网络专家混合（MoE）建模方法，刻画浮游植物光学性质随环境条件的变化，在保留异质群体分型结构的同时给出可解释的分量归属，为大规模、长期的原位浮游植物观测数据提供更契合的统计学习工具。（加州大学圣克鲁兹分校、华盛顿大学）', 'source': 'Environmetrics', 'url': 'https://doi.org/10.1002/env.70148', 'date': '2026-09-27'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '“北溟灵枢·海洋具身智能云脑工场”发布：虚实融合连接数字孪生体与真实水下装备', 'badge': '[要闻]', 'abstract': '9 月 20 日在 2026 年人工智能与海洋装备大会成果发布环节，大连理工大学“北溟灵枢——海洋具身智能云脑工场”正式对外发布。平台定位为连接海洋任务与真实装备的通用智能基础设施：底层由算力、数据、算法、模型与设备支撑，中间层贯通感知、训练、决策与控制全链路，通过虚实融合实现数字孪生体与真实机器人的联动交互，上层面向海洋牧场、海底资源开发与水下特种作业。其“云脑”采用“云端学本领、现场干实事”模式——模型集中训练与能力更新在云端完成，成熟模型部署至机器人本体或现场计算设备；平台提出“每潜一次，进化一步”，装备下潜回传新数据、经云端清洗优化与仿真验证后回送装备。平台将面向全国高校、科研院所与装备企业开放。同场大连海事大学“智慧海洋信息科技公共创新平台”亦正式发布。', 'source': '大连理工大学软件学院', 'url': 'https://ss.dlut.edu.cn/info/1571/34962.htm', 'date': '2026-09-21'}, {'title': '亚中尺度信息神经网络驱动的高保真动力降尺度框架', 'badge': '[论文]', 'abstract': 'Applied Ocean Research 刊文针对全球到区域海洋模式降尺度中亚中尺度过程难以充分解析的问题，提出“亚中尺度信息神经网络”驱动的高保真动力降尺度框架，将神经网络学习到的亚中尺度特征约束引入区域海洋环流模式（ORCM）配置，改善层结与近岸海域的模拟保真度，为构建高分辨率区域孪生海洋底座提供可复用的技术路线。', 'source': 'Applied Ocean Research', 'url': 'https://doi.org/10.1016/j.apor.2026.105280', 'date': '2026-09-24'}, {'title': '海事 AI 从“建议”走向“执行”：印度 JNPA 授出约 34 平方公里港口 AI/ML 数字孪生项目', 'badge': '[要闻]', 'abstract': '行业盘点显示，海事人工智能在 2026 年 9 月下旬正从独立演示转入运营级部署，主线是把有边界的运营决策逐步交给软件（航线与转速控制、机舱优化、堆场设备调度、数字孪生决策支持与船厂自适应机器人）。其中印度 JNPA 已授出金额 9.295 亿卢比（₹92.95 crore，约合人民币 7800 万元）的 AI/ML 数字孪生项目，覆盖约 34 平方公里港区运营，将连接海侧、陆侧、道路交通与 7×24 指挥控制中心。同篇盘点还列出 Fugro 新加坡海洋地理数据解译与数字孪生平台（亚太枢纽、开发中）等条目，可用于研判港口与海事数字孪生的落地节奏。', 'source': 'Ship Universe（Maritime AI Pulse, 2026-09）', 'url': 'https://www.shipuniverse.com/news/maritime-ai-roundup-as-fleet-rollouts-smart-ports-and-autonomous-systems-push-toward-2027', 'date': '2026-09-29'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization & Interaction', 'items': [{'title': 'AWI Basemap 2026：融合 GEBCO、IBCAO、IBCSO 的全球渲染阴影数字高程底图', 'badge': '[数据]', 'abstract': 'PANGAEA 发布 AWI Basemap（2026 版），面向 GIS 应用与 Web 地图查看器的全球底图数据集：以 GEBCO 网格为底，融合国际北冰洋水深图（IBCAO）与国际南大洋水深图（IBCSO）作为极地数据，并叠加南极数字数据库（ADD）、GLIMS 与 GIMP 的冰盖覆盖；提供 EPSG:4326 全球投影与 EPSG:3995、EPSG:3031 两套极地立体投影，以及三套面向不同用途的配色方案，可直接用于海洋地形图、极区专题图与在线地图服务的底图渲染。（数据 DOI：10.1594/PANGAEA.997175）', 'source': 'PANGAEA（AWI）', 'url': 'https://doi.pangaea.de/10.1594/PANGAEA.997175', 'date': '2026-09-25'}, {'title': '沿海韧性研究的三维分析框架：嵌入性、影响力与再生产', 'badge': '[论文]', 'abstract': 'Frontiers in Marine Science 刊文指出全球沿海社会—生态系统（SESs）正承受气候变化与人类扰动的双重压力，而既有研究对“变革性适应”（transformative adaptation）的解释多停留在二维叙事。文章提出一个三维分析框架——嵌入性（embeddedness）、影响力（influence）与再生产（reproduction），用以刻画沿海适应行动如何在制度与社会网络中生成、扩散并自我强化，为沿海韧性评估及其结构化表达与可视化提供维度支撑。', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1893781', 'date': '2026-09-21'}, {'title': '广东省近海海底基础数据调查成果接入省级海洋大数据平台', 'badge': '[要闻]', 'abstract': '历时 4 年多、累计 100 多航次，全国首个由省级部署开展的管辖海域大比例尺海底基础数据调查专项——广东省近海海底基础数据调查专项基本完成：完成全省 4.6 万余平方公里海域高精度地形地貌调查，覆盖 800 余座海岛，沉积物调查站位 800 余站，管线核查长度 8000 多公里，编制 1∶10000 水深地形图 1800 多幅、典型水下特征地貌图近 200 幅。成果已全面接入广东省海洋大数据平台，支撑三维立体海籍管理、用海活动监管、海底开发适宜性分析与海洋三维可视化。技术上首次实现“母船+无人船”组网规模化应用，无人船集群作业效率提升近 5 倍、成本降低超 30%。（本条为平台建设类重要性豁免条目）', 'source': '中国自然资源报', 'url': 'https://www.iziran.net/news.html?aid=5493085', 'date': '2026-09-02'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'SRAD：实验室再造海底环境中的多波束声学水下礁石检测数据集', 'badge': '[数据]', 'abstract': 'Scientific Data 刊文发布 SRAD 数据集，面向水下礁石与类礁目标检测中公开声学标注数据稀缺的问题：包含 3650 余张 8 位灰度声呐图像及对应真值检测框标注，并附原生 Oculus 声呐日志与配套数据处理工具。数据在大型海洋工程实验室的受控水池中采集，物理布置了砂、砾石、天然岩礁、藻礁、贝礁与模拟珊瑚等海底材料；由搭载于 ROV 的 Oculus M750d 多波束声呐在一致采集参数下获取，标注经专家复核与一致性核查。（大连海事大学 Magics Lab）', 'source': 'Scientific Data', 'url': 'https://www.nature.com/articles/s41597-026-08345-2', 'date': '2026-09-22'}, {'title': 'UCOD：面向近场底栖生物水下视觉伪装的多任务感知数据集', 'badge': '[数据]', 'abstract': 'Scientific Data 刊文发布 UCOD 数据集，针对底栖生物拟态特征与水体光学退化叠加导致的水下视觉伪装难题，构建可同时支持图像增强、目标检测、像素级分割与三维重建的多任务基准：含 7000 张高分辨率 RGB 图像（3500 张带检测标注、3500 张带分割掩码）与 16 个重建序列文件夹，覆盖扇贝、鱼类、海螺、鲍鱼、海星、海参六类典型伪装底栖生物；采集使用经标定的水下成像设备并控制平台运动学参数以保证空间一致性。（大连海事大学）', 'source': 'Scientific Data', 'url': 'https://www.nature.com/articles/s41597-026-08254-4', 'date': '2026-09-18'}, {'title': 'RSS SMAP L2C 海表盐度 V6.0 验证数据集发布', 'badge': '[数据]', 'abstract': 'NASA/JPL PO.DAAC 更新发布 RSS SMAP Level 2C 海表盐度（SSS）V6.0 验证数据集：相较 V5.0 主要改进包括剔除任务初期与 SMAP 雷达运行相关的偏差、缓解依赖观测天顶角的偏差、抑制北半球高纬偏咸偏差并修订太阳耀斑标志；产品含盐度及不确定度、亮温、天线温度、同址风速、HYCOM 参考盐度、降雨率与质量标志等，单文件覆盖一个 98 分钟轨道（每日 15 个），全球覆盖、约 4 天延迟，为海表盐度算法评估与气候应用提供经过验证的基准数据。（数据集目录最后核验：2026-09-22）', 'source': 'NASA/JPL PO.DAAC（data.gov 目录）', 'url': 'https://catalog.data.gov/dataset/rss-smap-level-2c-sea-surface-salinity-v6-0-validated-dataset', 'date': '2026-09-22'}, {'title': '沿海海洋浮标的数据质量评估、代表性与外部一致性检验', 'badge': '[论文]', 'abstract': 'Sensors 刊文以西班牙东南部 Cabo de Gata 近岸浮标为对象，对高频观测开展逐通道质量控制与代表性处理：数据经标准化与质控检验后按日均值聚合（不做插补），并与 Copernicus Marine 与 ERA5 产品做外部一致性比对（反距离权重插值、温度垂向插值至 5 m/10 m 传感器深度）。结果显示数据完整度 2025 年为 88.1%–88.3%、2026 年达 99.9%–100.0%，无越界失败；有效波高与气压一致性较强（RMSE 0.15/0.14 m、0.63/0.59 hPa），5 m 温度中等至强一致，而波谱反演风速差异随海况变化较大，提示近岸浮标数据的可用渠道需逐项甄别。', 'source': 'Sensors（MDPI，预警名单期刊，强制置底）', 'url': 'https://doi.org/10.3390/s26185873', 'date': '2026-09-16'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': '物理引导的统计数据融合：重建海洋中尺度涡三维流场', 'badge': '[论文]', 'abstract': 'Journal of the American Statistical Association 刊文提出物理引导的建模与学习框架，融合卫星、现场与模式等多源数据，估计海洋中尺度涡的三维流场结构。方法将海洋动力学约束嵌入统计融合过程，在观测稀疏条件下提升垂向流速与涡旋结构的重建稳定性，面向中尺度涡现场调查的实时航次决策需求。（北京大学、中国海洋大学、清华大学）', 'source': 'Journal of the American Statistical Association', 'url': 'https://doi.org/10.1080/01621459.2026.2739444', 'date': '2026-09-28'}, {'title': '地统计与确定性插值方法在季节性海洋要素制图中的对比评估', 'badge': '[论文]', 'abstract': 'Discover Geoscience 刊文系统比较地统计插值（克里金族）与确定性插值（反距离权重、径向基函数等）方法在季节性海洋要素空间制图中的表现，从交叉验证误差、空间结构保真度与对采样密度的敏感性等维度给出选用建议，为海洋环境要素空间化处理提供方法学参考。', 'source': 'Discover Geoscience', 'url': 'https://doi.org/10.1007/s44288-026-00736-7', 'date': '2026-09-24'}, {'title': '机器学习重建东海表层 pCO2 及其长期变率（2003–2023）', 'badge': '[论文]', 'abstract': 'Frontiers in Marine Science 刊文针对光学复杂近岸水体中表层二氧化碳分压（pCO2）估算难题，构建机器学习方法重建东海 2003—2023 年的表层 pCO2 场。研究利用卫星数据与多源辅助变量刻画该海域显著的生物地球化学异质性，给出长时序 pCO2 变率估计，为近岸碳汇监测与海洋酸化研究提供数据重建技术路径。', 'source': 'Frontiers in Marine Science', 'url': 'https://doi.org/10.3389/fmars.2026.1951665', 'date': '2026-09-28'}, {'title': 'HF 雷达表面流的时空重建混合框架', 'badge': '[论文]', 'abstract': 'Journal of Atmospheric and Oceanic Technology 刊文针对高频（HF）雷达表面流观测中缺测与噪声问题，提出融合数据驱动与物理约束的时空重建混合框架，对雷达反演表面流场进行时空补全与降噪，在保持流场物理一致性的同时提升缺测区域的重建精度，为海岸带流场业务化产品提供质量增强的处理路径。（本条为重要性豁免条目，在线首发日距本期 22 天）', 'source': 'Journal of Atmospheric and Oceanic Technology', 'url': 'https://doi.org/10.1175/jtech-d-25-0110.1', 'date': '2026-09-08'}]}, {'title': '六、数据管理与共享', 'en': 'Data Management & Sharing', 'items': [{'title': '全国多模态海洋环境与海冰数据集（2010–2026）完成国家数据产权登记', 'badge': '[要闻]', 'abstract': '2026 年 9 月 24 日，中科知道（北京）科技有限公司自研的 2010 年至 2026 年全国海洋环境与海冰数据集正式在国家数据产权登记服务系统完成登记。该数据集覆盖 2010 年 1 月至 2026 年 8 月全国海洋科学相关公开科研信息，整合 290 个合规数据源，符合《学科分类与代码》海洋科学（编号 170）分类；数据形态涵盖图像、数值、文本、点云等多模态类型（海洋观测图像、海洋参数数值、海洋文献文本、海底地形点云等），均附带来源、时间、空间及标注等完整元数据，并建立覆盖范围校验、缺测值质控与多源对齐的多级质量校验机制，可支撑海洋环境监测、海冰遥感分析以及海洋大模型预训练与微调。', 'source': '五号数据雷达', 'url': 'https://www.5radar.com/dataproperty/news/466698/', 'date': '2026-09-24'}, {'title': '国家数据产权登记服务系统上线试运行，数据“持证上岗”', 'badge': '[要闻]', 'abstract': '据国家数据局，国家数据产权登记服务系统于 9 月 11 日启动试运行，我国正式推行数据产权登记制度。登记机构将为各类形态数据出具“身份证明”，明确数据持有权、使用权、经营权归属，支撑数据流通交易、资产入表、融资担保与作价入股等生产经营活动。按 7 月印发的《数据产权登记工作指引（试行）》，全国统一登记对象、类型、流程、审查标准与效力；北京、上海、深圳数据交易所纳入首批登记机构目录，登记结果同步汇入国家系统实现“一次登记、全国通用”。上线首日已有 56 份凭证公示。对海洋科研数据而言，确权机制为高质量数据集的合规流通与复用提供了制度前提。（本条为国家级制度类重要性豁免条目）', 'source': '央视网《新闻联播》', 'url': 'https://news.cctv.com/2026/09/11/ARTIEOV1jVCtdd4kTQmOwnYI260911.shtml', 'date': '2026-09-11'}, {'title': '国家海洋信息中心出访埃及：共建阿拉伯区域海洋数据服务中心，赠送 CGOF1.0', 'badge': '[要闻]', 'abstract': '2026 年 9 月 20 日至 21 日，国家海洋信息中心主任石绥祥一行应邀访问阿盟科技海运学院（AASTMT），落实合作备忘录。作为联合国“海洋十年”官方实施伙伴，中心向对方赠送我国自主研发的长时序、高精度海洋公共服务产品——中国全球海洋融合数据集（CGOF1.0）。双方敲定四大务实合作路径：一是探索共建阿拉伯区域海洋数据服务中心，以 CGOF1.0 等数据集资源归集埃及等非洲和阿拉伯国家海洋观测资料，探索数据产品共建共享与可持续运营新模式；二是人才能力建设；三是联合编制发布区域气候变化与海平面研究报告；四是组建常态化联合科研团队，聚焦海洋大数据、人工智能、数字孪生等前沿方向协同攻关。', 'source': '搜狐（国家海洋信息中心）', 'url': 'https://www.sohu.com/a/1080778686_121107000', 'date': '2026-09-20'}, {'title': '《陆海地理信息融合——垂直基准建设中国实践》案例集在三亚发布', 'badge': '[要闻]', 'abstract': '2026 年 9 月 22 日，在海南三亚召开的联合国全球地理信息管理亚太区域委员会第 15 次全会上，国家海洋信息中心发布《陆海地理信息融合—垂直基准建设中国实践》案例集。针对长期存在的陆海基准不统一、陆图与海图难以无缝衔接问题，中心牵头联合高校与地方机构，以海洋水文方法为切入点，综合利用长时序海洋观测数据与自主研发的海洋再分析产品 CORA v2.0，建立中国近海海域海面地形模型、理论最低潮面模型、深度基准与高程基准统一转换模型及配套工具软件，相关成果已在全国 11 个沿海省市开展试点应用，架通陆海数据桥梁。', 'source': '国家海洋信息中心', 'url': 'https://www.nmdis.org.cn/c/2026-09-29/85915.shtml', 'date': '2026-09-22'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '巴西“The Gap”科考启航：Falkor (too) 探查罗曼什断裂带深部生态与地质', 'badge': '[航次]', 'abstract': '巴西科考队自塞阿拉州福塔莱萨启航，执行代号“The Gap”的科考航次，目标是揭示南大西洋罗曼什断裂带（Romanche Fracture Zone）的地质与生物奥秘。该断裂带位于巴西与非洲之间约 1000 公里处，是海底最深且最复杂的构造之一。航次使用 Schmidt Ocean Institute 提供的科考船 Falkor (too)，并由其 ROV SuBastian 支持（最大下潜 4500 米），用于精细探查岩壁并采集生物样品。团队由 Univali 的 José Angel Perez 教授领衔，共 25 名专家、来自 5 个国家（含 USP、UFRGS、UFES），重点关注赤道上升流如何影响深海群落；航次计划 10 月在加纳结束，并直播水下作业，全部数据公开。', 'source': 'Fato Paulista（巴西）', 'url': 'https://fatopaulista.com.br/expedicao-cientifica-explora-zona-fratura-romanche', 'date': '2026-09-18'}, {'title': 'Falkor (too) 加装走航 pCO2 系统，加入表面海洋 CO2 观测网络', 'badge': '[要闻]', 'abstract': 'NOAA 大西洋海洋与气象实验室（AOML）科学家与 Schmidt Ocean Institute 合作，在科考船 Falkor (too) 上安装走航式 pCO2 系统，在船舶横跨大西洋航行期间连续测量海—气二氧化碳交换。该系统纳入“机遇船”（Ships of Opportunity）计划，扩展了表面海洋 CO2 网络（SOCONET），重点填补南大西洋等采样稀疏的偏远海区数据空白；数据经专门团队质量控制后汇入国际公共数据仓储，支撑全球碳汇评估与海洋酸化研究。', 'source': 'Ocean Economist', 'url': 'https://oceaneconomist.com/articles/falkor-pco2-carbon-network', 'date': '2026-09-16'}, {'title': '中国-海管局联合中心深海科研项目落地启动，聚焦国际海底数据处理与西北太平洋生物多样性', 'badge': '[要闻]', 'abstract': '9 月 17 日，作为 2026 海洋合作发展论坛平行论坛之一，“探索深海——海洋未来产业的价值变革”论坛在青岛西海岸新区举行。现场中国-海管局联合中心深海科研项目正式落地启动，聚焦国际海底数据处理分析与西北太平洋深海生物多样性研究，旨在补齐全球深海科研数据短板。同场还发布了十余位院士专家联名签署的《海洋矿产勘查开发与生态环境保护协同发展倡议书》。', 'source': '今日头条（新黄河）', 'url': 'https://www.toutiao.com/article/7686861881620955698', 'date': '2026-09-17'}, {'title': '柔性仿生水下机器人：单驱动实现多方向机动控制', 'badge': '[论文]', 'abstract': 'Scientific Reports 刊文面向复杂海事环境（近海结构物与浅水区的贴近调查）中传统 AUV/ROV 机动能力受限的问题，探索一种柔性水下航行器的多方向控制方案，通过单一驱动实现多方向机动与高敏捷性，为紧凑空间下的水下巡检与感知作业提供新构型与控制思路。（佛罗里达大西洋大学）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-72152-3', 'date': '2026-09-23'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '海兰云推介汕头海底数据中心方案，提出“深汕算电协同”前店后厂模式', 'badge': '[要闻]', 'abstract': '9 月 22 日，第二届广东省人工智能应用对接大会在广州举行，汕头市发展和改革局组织海兰云（广东）科技有限公司参加主会场项目路演。海兰云总经理苏洋介绍，海底数据中心依托海水自然冷却与海上风电绿电供给，可节约土地、淡水与电力消耗；面向广东市场，企业规划在汕头布局海底数据舱集群，提出“深圳汕头前店后厂”的算力协同模式——汕头提供空间与海上能源底座、深圳承接市场需求与算力消纳，打造集能源供给、算力承载、智能调度、多能协同于一体的海上算力能源枢纽。相关方案已从海南、上海项目运营经验延伸至粤港澳大湾区布局。', 'source': '汕头市人民政府门户网站', 'url': 'https://www.shantou.gov.cn/stsfzhggj/zwgk/gzdt/content/post_2571736.html', 'date': '2026-09-22'}, {'title': '海底数据中心运营成效与百 MW 级集群规划公开', 'badge': '[要闻]', 'abstract': '在第二届广东省人工智能应用对接大会的公开介绍中，海兰云披露海底数据中心的实际运营指标：海水自然冷却使海南项目 PUE 低至 1.10，上海临港项目用电量较传统数据中心降低 30%、冷却淡水消耗减少 99%、绿电供给率超 95%。企业正规划“深圳汕头前店后厂”的百 MW 级海底数据舱集群，与汕头海上风电统一规划、统一建设，将海洋条件转化为项目建设、运营与服务的资源优势。该方向亦被列入汕头市人工智能产业“算力—算法—数据—应用”系统布局的一环。', 'source': '今日头条（广州日报综述）', 'url': 'https://www.toutiao.com/article/7688387875678831104', 'date': '2026-09-22'}, {'title': 'Fugro 在新加坡建设 AI 海洋数字孪生枢纽', 'badge': '[要闻]', 'abstract': '荷兰地理数据企业 Fugro 在新加坡扩展技术枢纽，建设由新加坡经济发展局（EDB）资助的 AI 驱动海洋数字孪生平台，用于加速海床条件对海上与近岸工程的影响判读。平台将地球物理勘探信息、岩土现场调查结果、实验室数据与成像资料整合到单一数字环境，利用人工智能与机器学习自动完成数据集成、解释与分析，减少海洋场地表征中人工拼接不同数据集的耗时。新加坡将作为该技术面向亚太的落地起点，企业计划随平台扩产增加 AI、数据科学与数字工程岗位；此前其 GeoAI 框架已实现部分地质灾害与栖息地评估较传统流程快约 10 倍。（本条为重要性豁免条目）', 'source': 'Splash247', 'url': 'https://splash247.com/fugro-builds-ai-marine-digital-twin-hub-in-singapore', 'date': '2026-09-03'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code', 'items': [{'title': 'C-Star (cstar-ocean) v0.14.1：面向 ROMS-MARBL 的海洋碳模拟工作流编排工具', 'badge': '[工具]', 'abstract': 'conda-forge 发布 C-Star（cstar-ocean）v0.14.1。该工具以“蓝图驱动、编排感知”的 Python API 与命令行工具，自动化可复现的海洋碳模拟工作流，覆盖 ROMS-MARBL 及相关区域海洋/生物地球化学模拟的配置与执行，降低区域碳循环模拟的环境搭建与流程管理门槛。（GitHub：CWorthy-ocean/C-Star；最新更新 2026-09-18）', 'source': 'conda-forge（Anaconda）', 'url': 'https://anaconda.org/channels/conda-forge/packages/cstar-ocean/overview', 'date': '2026-09-18'}, {'title': 'regional-mom6 v1.0.3：自动生成 MOM6 区域海洋模式配置', 'badge': '[工具]', 'abstract': 'conda-forge 发布 regional-mom6 v1.0.3。该包自动生成模块化海洋模式 MOM6（Modular Ocean Model 6）的区域配置，简化从全球网格与初始/边界条件到区域算例的构建流程，便于开展区域海洋模拟与降尺度研究，并与社区既有的 MOM6 工具链衔接。（GitHub：COSIMA/regional-mom6；最新更新 2026-09-17）', 'source': 'conda-forge（Anaconda）', 'url': 'https://anaconda.org/channels/conda-forge/packages/regional-mom6/overview', 'date': '2026-09-17'}, {'title': 'cstar-forge v0.9.0：ROMS-MARBL 域生成器并入 cstar-ocean', 'badge': '[工具]', 'abstract': 'conda-forge 更新 cstar-forge v0.9.0。该包原为 C-Star 体系中的 ROMS-MARBL 域生成器，现已整体迁入 cstar-ocean（cstar.applications.forge、cstar.catalog、cstar.wizard 及 cstar forge CLI），本版本转为兼容性垫片：依赖 cstar-ocean 并以弃用告警方式重新导出旧的 cstar_forge 导入路径，提示新环境应直接安装 cstar-ocean。对既有工作流用户而言，这是迁移路径的重要提示。（最新更新 2026-09-24）', 'source': 'conda-forge（Anaconda）', 'url': 'https://anaconda.org/conda-forge/cstar-forge', 'date': '2026-09-24'}, {'title': 'bacpipe：让生物声学深度学习模型“开箱可用”的 Python 工具包', 'badge': '[工具]', 'abstract': 'Methods in Ecology and Evolution 刊文发布 bacpipe——一个汇集生物声学深度学习模型与评估流水线的 Python 工具包，同时提供图形界面与编程接口，面向生态学家与计算机科学家。工具可将前沿模型用于自定义音频数据集，生成声学特征向量（嵌入）与分类预测；其模块化设计支持通过交互式可视化、聚类与探测（probing）开展模型评估与基准比较，降低被动声学监测（PAM）数据的分析门槛，对水声/海洋生物声学研究具有直接复用价值。', 'source': 'Methods in Ecology and Evolution', 'url': 'https://doi.org/10.1111/2041-210x.70406', 'date': '2026-09-18'}]}]



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
