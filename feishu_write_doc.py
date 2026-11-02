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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '可学习 Gabor 卷积 + ResNeXt：给水下声学分类注入频域先验', 'badge': '[论文]', 'abstract': '船舶辐射噪声与环境噪声的复杂性，让水下声学目标分类长期难以稳定：数据集规模有限、实验设置缺乏标准化，模型间精度对比往往不可信。研究提出 GSE ResNeXt，把可学习的 Gabor 卷积层嵌入 ResNeXt 骨干——Gabor 核本身对应带通滤波，等于让网络从第一层起就带着「频域先验」而非从零学习边缘，再叠加压缩-激励式通道注意力强化判别性频带。对水声信号这类强噪声、小样本场景，把信号处理的先验做成可学习算子，比单纯加深网络更对症。（Ocean Engineering）', 'source': 'Ocean Engineering', 'url': 'https://doi.org/10.1016/j.oceaneng.2026.129035', 'date': '2026-10-29'}, {'title': '天星-S2S：多圈层耦合 + 扩散模型做次季节到季节概率集合预报', 'badge': '[论文]', 'abstract': '次季节到季节（S2S）预报处在「天气已不可报、气候尚不可报」的缝隙里，难点在于多圈层相互作用与大气内在不确定性同时存在。研究提出 TianXing-S2S：先把海洋、陆面、冰雪等多圈层预测量编码进紧凑潜空间，再用扩散模型生成逐日集合预报，并在去噪器中引入基于最优传输（OT）的耦合模块来协调各圈层信息的交互。相比确定性模型只给一条轨迹，扩散式集合能直接给出概率分布——这对海洋防灾减灾的决策口径更实用。（npj Climate and Atmospheric Science）', 'source': 'npj Climate and Atmospheric Science', 'url': 'https://doi.org/10.1038/s41612-026-01572-9', 'date': '2026-10-30'}, {'title': '分类学约束的层级深度学习：西沙珊瑚礁鱼类耳石图像鉴定', 'badge': '[论文]', 'abstract': '耳石自动鉴定此前多把「物种」当作唯一输出层，鱼类分类学里蕴含的层级信息被浪费。研究以西沙群岛七连屿 2020—2025 年采集的珊瑚礁鱼类耳石图像为对象，覆盖 25 个物种，构建引入分类学约束的层级深度学习模型，并与非层级基线在同一批数据上训练、验证、测试。层级建模的价值在于：即便细粒度物种判错，模型仍能给出科/属层面的可靠结论，对以耳石为基础的食物网与渔业资源研究更实用。（Journal of Fish Biology）', 'source': 'Journal of Fish Biology', 'url': 'https://doi.org/10.1111/jfb.70717', 'date': '2026-10-29'}, {'title': '可解释机器学习 + 结构路径分析：山东半岛入海河流富营养化风险的水文状态重组', 'badge': '[论文]', 'abstract': '小型入海集蓄水体中，富营养化风险会随水文状态从「低流量源区累积」切换到「降雨驱动输运」，但这一转折很少被定量刻画。研究以山东半岛 30 条入海河流 2020—2024 年的月度富营养化指数（由总氮、总磷、溶解氧、高锰酸盐指数构成）为对象，用可解释机器学习结合实测变量的结构路径分析，评估地形等下垫面因子与水文状态的交互影响。方法学意义在于：不满足于「哪个因子重要」，而是把因子间的作用路径拆开，为陆海统筹的养分管理提供可解释依据。（Ecological Indicators）', 'source': 'Ecological Indicators', 'url': 'https://doi.org/10.1016/j.ecolind.2026.115773', 'date': '2026-10-28'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '把 GIS 搬进 Unity：情景式 3D 数字孪生量化城市海平面上升暴露', 'badge': '[论文]', 'abstract': '沿海城市的海平面上升（SLR）暴露评估，长期受两件事限制：高程数据分辨率普遍粗于 30 米；传统制图与 GIS 的「浴缸法」只能给出淹没范围，难以支撑资产级统计与情景解读。研究把 GIS 数据导入 Unity 引擎构建 3D 数字孪生，对三类城市要素在多种 SLR 情景下生成定量暴露统计，并以阿联酋为案例。相比静态淹没图，可交互孪生的增量在于「同一套三维场景里换情景、出统计」，让决策者看到的不是一张图而是一组可比较的数。（Frontiers in Built Environment）', 'source': 'Frontiers in Built Environment', 'url': 'https://doi.org/10.3389/fbuil.2026.1969739', 'date': '2026-10-30'}, {'title': '船舶电力系统运维的数字孪生：从被动维修转向预测性维护', 'badge': '[论文]', 'abstract': '船舶电力系统承担推进、发电与主设备支撑，其运维质量直接决定船舶可用性。传统运维在设备状态监测、异常检测与维修决策三环节均有短板，本质仍是「坏了再修」。文章以文献综述方式梳理数字孪生在船舶电力系统智能运维中的应用路径：用孪生体同步物理系统的运行状态，提前识别故障征兆并给出维修决策建议。对海洋工程装备而言，这类综述的价值在于把「孪生该建到哪一层、数据从哪来、决策如何闭环」讲清楚，而不是停留在概念倡导。（Applied and Computational Engineering）', 'source': 'Applied and Computational Engineering', 'url': 'https://doi.org/10.54254/2755-2721/2026.38220', 'date': '2026-10-27'}, {'title': '侨乡近代建筑的 Revit/HBIM 多模块信息集成：数字孪生辅助预防性保护', 'badge': '[论文]', 'abstract': '湿热沿海地区的侨乡近代建筑，同时面临表皮劣化、环境性能不足与长期使用需求三重压力；既有数字化保护研究常把勘察、诊断、干预、复检分段处理，导致信息碎片化、空间关联弱、流程不连续。研究构建基于 Revit/HBIM 的数字孪生辅助多模块信息集成与更新框架，把上述环节挂接到同一建筑信息模型上并支持迭代更新。这类「遗产孪生」的技术门槛不在建模，而在让巡检数据能持续回写模型——框架把更新机制作为一等公民，值得海岸带遗产监测借鉴。（Buildings，MDPI 集团刊，D 级，供参考）', 'source': 'Buildings（MDPI 集团刊，D 级，供参考）', 'url': 'https://doi.org/10.3390/buildings16204154', 'date': '2026-10-20'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': '不只看作者单位：世界海洋评估报告的地理—主题交互可视化', 'badge': '[论文]', 'abstract': '联合国《世界海洋评估 II》用 49 章、引用 3500 余篇文献综合海洋研究成果，这种体量的语料，读者很难把文档结构与主题、时间、引用、地理信息连起来。常规文献计量只能显示作者单位所在地，却显示不了研究实际讨论的海域。研究构建交互式学术数据可视化系统，核心贡献是把「内容导出的地理信息」与主题信息一并整合进可视化，让用户按海域、主题、时间多维穿梭。对海洋政策与研究综述类读者，这是把「读不完的报告」变成「可探索的地图」的一种解法。（Information Visualization）', 'source': 'Information Visualization', 'url': 'https://doi.org/10.1177/14738716261492254', 'date': '2026-10-26'}, {'title': 'QGIS 复现工作流：把 CMEMS 地中海温度产品做成可复现专题图', 'badge': '[技术报告]', 'abstract': '海洋再分析产品动辄 NetCDF 多维数组，非 GIS 背景的使用者常在「读进来」这一步就卡住。这份技术文档给出完整可复现流程：以 Copernicus Marine（CMEMS）地中海物理分析与预报产品（MEDSEA_ANALYSISFORECAST_PHY_006_013，同化卫星与现场观测）为例，在 QGIS LTR 3.44 中完成 NetCDF 加载、表层子集提取、色标范围校准与时间维配置。它的价值不是新算法，而是把「开源桌面环境里怎么把业务化海洋产品画对」的每一步固定下来，可直接用于教学与业务出图。（Marine and Fishery Sciences）', 'source': 'Marine and Fishery Sciences (MAFIS)', 'url': 'https://doi.org/10.47193/mafis.4012027010106', 'date': '2026-10-26'}, {'title': '交互式地层正演模拟：面向海洋地学教学的开源工具包', 'badge': '[工具/论文]', 'abstract': '正演地层模拟计算沉积盆地对海平面变化、构造沉降与沉积物供给的响应，是层序地层学的核心方法；但「动态强迫如何生成进积、退积、加积的静态结构」一直是教学难点。现有软件两极分化：商业包昂贵，研究代码难用。作者发布开源交互式工具包，把参数调整与结果渲染放在同一界面，让学习者即时看到强迫变化如何改写地层架构。对海洋地学教学与快速情景试验，这类「可上手」的工具比功能更全的商业软件更有推广价值。（Applied Sciences，MDPI 集团刊，D 级，供参考）', 'source': 'Applied Sciences（MDPI 集团刊，D 级，供参考）', 'url': 'https://doi.org/10.3390/app162110608', 'date': '2026-10-27'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': '缺测填补会改变设计：11 种方法对滨海近零能耗建筑技术经济方案的影响', 'badge': '[论文]', 'abstract': '高分辨率太阳辐照与风速序列的缺测通常在系统选型前被「填掉」，但填补方法本身会怎样改变设计结论，很少被检验。研究对大连一座氢集成的滨海近零能耗建筑的分钟级辐照与风速序列，施加 11 种统计、时序与学习型填补方法，在 5%—80% 四档缺失率与两种缺口形态下对比，并用「逐点误差 + 分布/技术经济后果」双重验证。结论指向一个容易被忽视的质量命题：填补误差不只是 RMSE 数字，它会传导到容量配置与经济性判断。（Scientific Reports）', 'source': 'Scientific Reports', 'url': 'https://doi.org/10.1038/s41598-026-76333-y', 'date': '2026-10-24'}, {'title': '孤立森林 + Fellegi-Sunter + DeepER：气象观测的异常检测与记录去重', 'badge': '[论文]', 'abstract': '台站观测的传感器异常与记录重复会显著偏置气候分析，而现行质量控制多依赖人工核查与静态阈值，对极端天气缺乏适应性。研究提出自动化质控框架：用孤立森林在无分布假设下识别多变量离群，用 Fellegi-Sunter 概率记录 linkage 结合 DeepER 做实体去重，在印尼 Sudjarwo Tjondro Negoro 气象站的观测数据上验证。方法组合的思路值得海洋观测网借鉴——异常检测负责「值不对」，去重负责「记录重复」，两者本是两类不同错误。（Journal of Applied Informatics and Computing）', 'source': 'Journal of Applied Informatics and Computing', 'url': 'https://doi.org/10.30871/jaic.v10i5.13951', 'date': '2026-10-19'}, {'title': '无泄漏验证下的卫星水深反演：换一个港区，精度还剩多少', 'badge': '[预印本]', 'abstract': '卫星测深（SDB）常被视为多波束港区测量的低成本补充，但其精度很少在模型「没见过」的区域上被真正检验。研究在阿布扎比浑浊、浅水且潮差显著的近岸，用 6 个港区 12 次测量、285,619 个多波束测深点（归算至最低天文潮位）作真值，比较 Stumpf 比值法、Lyzenga 变换、LightGBM 与 U-Net 集成，基于 72 景 Sentinel-2 影像训练，并设置「跨站点迁移」与「站内局部控制（20% 测深点、225 米缓冲区块）」两种验证。结论显示验证设计本身会改写排序——这正是 SDB 论文之间精度不可比的根源。（arXiv 预印本）', 'source': 'arXiv', 'url': 'https://arxiv.org/abs/2610.33609', 'date': '2026-10-24'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': '格陵兰西岸两处不稳定斜坡：正在成形的北极海啸风险', 'badge': '[论文]', 'abstract': '滑体入峡湾可激发海啸，威胁远超滑源区。研究在格陵兰中西部 Uummannaq 峡湾系统识别出两处正在变形的不稳定斜坡：Karrat 峡湾一处约 4 亿立方米，Kangerluarsuk 峡湾一处约 3000 万立方米但更临近失稳。两处均在 2017 年 Karrat 灾难性滑坡海啸之后被系统排查发现。文章的核心贡献是把「斜坡形变监测—失稳体积估计—海啸情景」串成一条链，提示北极变暖下这类灾害的风险评估需要从事件响应转向常态化形变监测。（Communications Earth & Environment）', 'source': 'Communications Earth & Environment', 'url': 'https://doi.org/10.1038/s43247-026-04175-7', 'date': '2026-10-28'}, {'title': '8 公里区域海洋模式：中国近海极端海平面的过程归因预估', 'badge': '[论文]', 'abstract': '全球与区域平均海平面的未来变化已被大量量化，但极端海平面（ESL）的预估仍稀缺——对人口稠密的中国近海而言，这恰是风险所在。研究用约 8 公里分辨率的区域海洋模式预估中国边缘海的海平面变化与分布，模式能解析陆架浅海动力过程，从而对动力型 ESL 变化做基于过程的归因，而非仅靠统计外推。对海岸防护设计而言，把「平均海平面上升」与「极端水位重现期变化」分开估计，是两种不同的工程输入。（JGR: Oceans）', 'source': 'JGR: Oceans', 'url': 'https://doi.org/10.1029/2026jc024403', 'date': '2026-10-27'}, {'title': '锋区声速剖面重建：先分冷暖水侧，再逐侧重构密度场', 'badge': '[论文]', 'abstract': '海洋锋区结构复杂、误差大，声速剖面（SSP）重建在此尤其困难。研究提出 RF-SFDL 模型，融合多源卫星数据、Argo 剖面与锋面数据集：先依据锋面特征把锋区划分为冷、暖水团两侧，分别重建各侧海水密度场；再以海表温度、海面高度异常、海表盐度、海表密度与地理坐标为输入，结合 Argo 密度建立「海表—水下」声速映射；最后把海表参数与重构密度场组合生成锋区 SSP。结果把平均绝对误差压到 1.77 m/s、均方根误差 2.69 m/s，较单经验正交函数回归（sEOF-r）分别降低 78.04% 与 74.55%。（Acta Oceanologica Sinica）', 'source': 'Acta Oceanologica Sinica', 'url': 'https://doi.org/10.1007/s13131-026-2694-2', 'date': '2026-10-27'}, {'title': '35 万条水位记录 + 高斯过程：潮汐非线性的季节变化怎么量化', 'badge': '[论文]', 'abstract': '浅水河口在潮波向陆传播过程中持续扭曲潮汐，扭曲强度决定涨水速率、净输沙方向与盐水入侵上限。研究以泰国湾内侧受季风影响的 Bang Pakong 河口为对象，使用 2019 年 5 月至 2026 年 6 月约每十分钟一条、共 353,644 条水位记录，先做含 33 个分潮的最小二乘调和分析，再用高斯过程重建并刻画潮汐非线性的季节变化。长序列加概率式重建的组合，让「非线性强度随季节怎么变」从定性描述变成可量化、可外推的结论。（Ocean Dynamics）', 'source': 'Ocean Dynamics', 'url': 'https://doi.org/10.1007/s10236-026-01869-6', 'date': '2026-10-19'}, {'title': '生成模型补全冰区水深网格：北极 DTM 从碎片到连续', 'badge': '[论文]', 'abstract': '冰封极区的水深制图长期受两重限制：常年海冰阻碍系统测量；破冰作业又会通过噪声、船体振动与冰干扰劣化多波束数据，使数字地形模型碎片化、分辨率粗、空洞多，进而影响对海底地貌（含指示古冰川范围的冰川地貌）的解释。常规插值在放大与补洞时往往过度平滑，抹掉地形细节。研究以北极为例，用生成模型增强粗糙水深网格，力图在补全空洞的同时保留形态特征。对极地航行保障与古冰盖重建，这类「生成式补全」是目前最现实的技术路径。（Artificial Intelligence in Geosciences）', 'source': 'Artificial Intelligence in Geosciences', 'url': 'https://doi.org/10.1016/j.aiig.2026.100284', 'date': '2026-10-26'}, {'title': 'CNN + 等渗回归：让全球平均海平面预报不长出「短期抖动」', 'badge': '[论文]', 'abstract': '深度学习预报全球平均海平面（GMSL）时，常会给出短期上下起伏的轨迹，与物理上应有的长期单调趋势相冲突。研究提出 CNN-ISO 框架，用卷积网络对 1880—2024 年的年际 GMSL 变化建模，输入 11 个表征大气、海洋与冰冻圈状况的预测量，再用等渗回归把输出投影到单调约束上，兼顾拟合能力与物理合理性。这类「物理约束后处理」的做法，对其它长序列海洋要素预测同样适用：先让模型学，再把不合物理的部分投回去。（Estuarine, Coastal and Shelf Science）', 'source': 'Estuarine, Coastal and Shelf Science', 'url': 'https://doi.org/10.1016/j.ecss.2026.110293', 'date': '2026-10-23'}]}, {'title': '六、数据管理与共享', 'en': 'Data Management & Sharing', 'items': [{'title': '分类单元对齐：立陶宛淡水大型无脊椎动物标准名录', 'badge': '[论文]', 'abstract': '分类学口径不一致，是国家尺度数据合成与生物监测报告失真的隐形杀手：同一物种在不同年份、不同机构笔下可能对应不同学名或不同分类层级。研究综合文献与监测数据，编制立陶宛淡水大型无脊椎动物标准化操作分类单元名录，并按现行命名规范统一，目标是提升监测数据的可比性与生态质量评估的可靠性。对任何做跨源整合的海洋生物监测体系，这份名录的方法学（如何对齐、如何留痕）比名录本身更可迁移。（Environmental Monitoring and Assessment）', 'source': 'Environmental Monitoring and Assessment', 'url': 'https://doi.org/10.1007/s10661-026-16088-1', 'date': '2026-10-22'}, {'title': '军事开放科学用于海岸遗产：从可持续监测实践走向开放提案', 'badge': '[会议]', 'abstract': '海岸带是气候变率与地质过程共同塑造的动态边界，也是沉船、要塞、港口设施、灯塔与脆弱生态共存的遗产富集区。这类海岸与水下遗产的保护，需要工程地质、监测技术与数据治理的交叉方案。文章以历史上重要的港口、神庙、聚落构成的连续体为线索，提出把「军事开放科学」的实践规范引入海岸遗产监测，从可持续监测走向可共享、可复用的开放数据提案。对涉密或敏感区位的海岸数据，如何在开放与安全之间取平衡，是这篇的着力点。（TU Delft Open，会议论文）', 'source': 'TU Delft Open（会议论文）', 'url': 'https://doi.org/10.59490/6ad293ec1111c11e2bf480b5', 'date': '2026-10-29'}, {'title': '46 个物种、56 个变量：海牛类与海兽类的标准化性状数据仓库', 'badge': '[论文]', 'abstract': '海牛类与海生食肉类是少数从陆地重返水生的哺乳动物谱系，是海洋生态系统健康的重要指示类群，但近半数物种受威胁。此前缺少同时覆盖生物学性状与环境变量的综合数据库。研究为全部 46 个物种构建标准化数据仓库，整合形态、生理、生活史、生态与环境共 56 个变量，并给出统一的字段定义与缺失标注。对宏观生态分析而言，这类「小而全」的性状库往往比再抓一批原始数据更有用——它把可比性提前做完了。（Integrative Zoology）', 'source': 'Integrative Zoology', 'url': 'https://doi.org/10.1111/1749-4877.70217', 'date': '2026-10-24'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Expeditions', 'items': [{'title': '“蛟龙”号完成 7000 米级海试：3 个潜次、最大 7056.9 米', 'badge': '[新闻]', 'abstract': '依托中国大洋 100 航次第二航段，“蛟龙”号载人潜水器在菲律宾海盆完成 3 个潜次试验，其中 2 个潜次超过 7000 米，最大下潜深度 7056.9 米（10 月 2 日第 465 潜次），各项指标达到 7000 米级海试要求。这是它完成第二次迭代升级与关键部件国产化替代后的首个 7000 米级海试：换装 7000 米级高能量密度油浸锂电池组、安装国产直驱型低噪直流推进器、扩展应急液压系统接口，并应用大深度海水液压浮力调节与广视角高变倍超高清摄像系统。国家深海基地管理中心研究员孙永福表示，这验证了升级后装备的可靠性与安全性。（新华社）', 'source': '新华社（深海一号船）', 'url': 'https://www.ce.cn/xwzx/gnsz/gdxw/202610/t20261027_3272858.shtml', 'date': '2026-10-27'}, {'title': '合成浮标阵列诊断：南大洋风暴如何改写海气碳通量', 'badge': '[论文]', 'abstract': '南大洋是地球上风暴最频繁的海区，但观测稀疏，风暴对海气通量的影响长期难以量化。研究在 E3SM 的物理-生物地球化学模拟中布放「合成浮标」——按真实平台的采样节奏与分辨率对 2014—2023 年的模式场二次采样，再据此诊断现有观测阵列捕捉风暴驱动碳通量的能力。方法学价值在于：它把「观测网够不够用」从经验判断变成可用模式做定量压力测试的问题，也为下一轮南大洋观测系统设计提供了评估框架。（Geophysical Research Letters）', 'source': 'Geophysical Research Letters', 'url': 'https://doi.org/10.1029/2026gl125540', 'date': '2026-10-28'}, {'title': '751 个表层沉积物样品：渤黄东海粒度数据集', 'badge': '[数据]', 'abstract': '研究发布覆盖渤海、黄海、东海三大陆架海的表层沉积物粒度数据集，共 751 个样品，采样时间跨 2001—2019 年，按国家海洋调查规范（GB/T 12763.8—2007）用箱式采样器采集，全部样品由 Malvern Mastersizer 2000 激光衍射粒度仪分析。对沉积物输运、陆源物质扩散与陆架沉积动力研究，这套跨十余年、覆盖三个陆架海的统一口径数据，是难得的基准资料——它的价值不在单点精度，而在「同一方法、同一区域、长时间跨度」带来的可比性。（Earth System Science Data）', 'source': 'Earth System Science Data', 'url': 'https://doi.org/10.5194/essd-18-7743-2026', 'date': '2026-10-26'}, {'title': '飞机当震源：航空声-震耦合探测南极粒雪—冰转变', 'badge': '[论文]', 'abstract': '要预测南极冰盖对气候变化的响应，必须知道冰体浅层结构，但直接测量困难：传统地震勘探后勤代价高，星载遥感对次表层信息有限。研究提出「非接触式航空地震学」——利用飞机飞行产生的声波在冰面转化为地震波，以此探测冰体内部。团队用 36 节点地震阵列在多次飞越中记录到多类型地震波并加以分析，反演粒雪—冰转变界面与近表层弹性结构。这类把「噪声源当信号」的思路，为极地浅层结构调查提供了一种低成本、可重复的观测方式。（Geophysical Research Letters）', 'source': 'Geophysical Research Letters', 'url': 'https://doi.org/10.1029/2026gl123670', 'date': '2026-10-22'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '“妈祖”海洋预报数值模式升级 2.0：全球 5 公里、重点海域 1 公里', 'badge': '[新闻]', 'abstract': '11 月 1 日，自然资源部国家海洋环境预报中心在第十一届世界妈祖文化论坛上发布“妈祖”海洋预报数值模式 2.0 版本。升级后全球预报系统分辨率较上一代提升一倍至 5 公里，我国近海与西太平洋等重点海域提升至 1 公里；在全球可变分辨率数值模拟、物理动力框架更新、海冰与海洋生态应用场景拓展、大规模并行计算等方面均有升级，并保留 GPU 加速与轻量化低能耗特性，已在“雪龙 2”号科考船完成船载运行测试。经检验评估与院士专家评审，温盐流预报效果达国际先进水平，有效波高精度与国际权威模式相当。模式代码已开源并在沿海省级预报机构部署，并向印尼、孟加拉国开展移植与培训。（新华社）', 'source': '新华社', 'url': 'https://www.news.cn/tech/20261101/168023aec7ec46b3a1559d59804988d6/c.html', 'date': '2026-11-01'}, {'title': '上海临港风电直连海底数据中心实现全面商业运行', 'badge': '[新闻]', 'abstract': '据央视《新闻联播》11 月 1 日报道，位于东海海域的上海临港风电直连海底数据中心近日实现全面商业运行，国内运营商及头部 AI 大模型企业已接入海底算力资源，开展国产大模型推理与科学计算等商业应用。该项目把海上风电直供与海水自然冷却合在一处，是“东数西算”全国一体化算力网在东部海域的落点之一。对海洋数据基础设施而言，这标志海底数据中心从示范工程跨到商业运营：算力供给、能源结构、冷却方式三件事在同一物理空间内被重新组织。（央视新闻联播）', 'source': '央视新闻联播', 'url': 'https://v.china.com.cn/2026-11/01/content_118756997.html', 'date': '2026-11-01'}, {'title': '2026 中国海洋经济博览会：以“数字智能海洋”为主线', 'badge': '[业界]', 'abstract': '2026 中国海洋经济博览会在深圳国际会展中心举行，主题为“数字智能海洋：共创可持续未来”，展出面积 5 万平方米、350 余家企业参展，设深海远海能源、绿色航运与低碳物流、海洋电子信息、海洋生态、低空经济海上应用、全域海洋监测与灾害预警等八个展区。首次设立主宾国机制（法国）与主宾省（海南）。与数据主题直接相关的看点集中在三处：海底具身智能机器人与海洋大模型（海南展团）、海洋环境数字孪生与开放海域网络通信（中国电信、华为等）、以及三亚海洋实验室面向南海的“魔针”大模型。（SeaNews）', 'source': 'SeaNews', 'url': 'https://www.seanews.com.tr/article/2026-china-marine-economy-expo-launches-navigating-towards-a-digital-ocean-future-mvybfbuc', 'date': '2026-11-02'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'COAST：把 OpenFOAM 波浪越浪模拟做成一条命令的开源框架', 'badge': '[工具/论文]', 'abstract': '相分辨的 VOF 模拟能给出经验公式与数据驱动模型给不出的越浪细节，但配置、运行、后处理一个数值波浪水槽需要相当的 CFD 功底。作者发布开源框架 COAST，把 OpenFOAM 与 waves2Foam 的工作流自动化：从标准 EurOtop 断面出发自动建模、生成网格、设置造波与消波、运行并提取越浪量。对海岸工程实务，这是把「能做但很贵」的相分辨模拟降到「按断面参数批量跑」的门槛之下。（Results in Engineering）', 'source': 'Results in Engineering', 'url': 'https://doi.org/10.1016/j.rineng.2026.113720', 'date': '2026-10-23'}, {'title': 'OWL：把波场求解、残差与反演算法装进一个库的开源框架', 'badge': '[工具/论文]', 'abstract': '地震波建模与全波形反演（FWI）是探测地下结构与属性的重要手段，开源工具让研究者能复现他人结果、试验新方法；但搭建灵活的 FWI 流程，仍需自行集成波场求解器、残差函数与反演算法，工作量大且易错。作者发布 Open Wave Library（OWL），在声学与弹性介质中统一组织波场模拟与 FWI 的各个环节，目标是让「换求解器、换残差、换优化器」变成配置而非重写。对海底结构成像与海洋地球物理研究，这类框架能显著降低方法对比的成本。（Geophysical Journal International）', 'source': 'Geophysical Journal International', 'url': 'https://doi.org/10.1093/gji/ggag450', 'date': '2026-10-19'}, {'title': 'echopype v0.12.0：新增 BI500 解析与 Echoview 匹配几何重网格', 'badge': '[工具]', 'abstract': '渔业声学数据处理库 echopype 发布 v0.12.0（2026-10-19）。新增功能包括：BI500 文件解析支持、基于 Echoview Match Geometry 的重网格、按选定通道解析与存储、AZFP ULS6 初步支持与 ULS5 改进；性能上优化了降噪与海底检测；工程侧按 Scientific Python SPEC 0 现代化打包与依赖策略，新增 Python 3.14 支持并强化 CI 与测试基础设施。对把原始声学文件转成可分析数据集的流程，这次更新直接减少了格式适配与重采样环节的手工步骤。（GitHub Release）', 'source': 'GitHub', 'url': 'https://github.com/OSOceanAcoustics/echopype/releases/tag/v0.12.0', 'date': '2026-10-19'}]}]



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
