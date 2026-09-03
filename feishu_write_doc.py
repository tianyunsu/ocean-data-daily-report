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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '季节感知混合卷积-Transformer：引入月份感知位置编码的南极海冰浓度预报（arXiv, 2026-08-31）', 'badge': '[论文]', 'abstract': '南极海冰浓度（SIC）预报同时存在复杂空间结构、长程时间依赖与强季节变率三重挑战。该研究提出季节感知混合卷积-Transformer 框架：卷积层提取局部空间型态，自注意力机制建模长程时间依赖，并引入两项季节性先验机制——月份感知位置编码（month-aware positional encoding）与季节时间偏置（seasonal temporal bias），显式将季节循环注入模型。实验表明，该框架在短时效与长时效预报上均优于现有卷积类与循环类模型，为极地海冰业务化预报提供了新的建模范式。', 'source': 'arXiv (cs.LG)', 'url': 'https://arxiv.org/abs/2608.30654', 'date': '2026-08-31'}, {'title': 'KSG-Net：关键稀疏与全局上下文学习用于海上三维船舶检测（arXiv, 2026-09-02）', 'badge': '[论文]', 'abstract': '海上三维船舶检测对自主航行至关重要，但面临船舶尺度变化大、小型船舶点云稀疏、海杂波干扰严重等难题。现有方法多基于二维特征或稠密表示，难以兼顾精度与效率；面向道路场景设计的稀疏三维检测器迁移到海上效果不佳。KSG-Net 在全稀疏检测框架内联合增强局部判别特征与全局结构感知：关键稀疏多尺度聚合（KSMA）模块通过筛选信息量高的关键体素并聚合跨尺度邻域特征，强化稀疏小目标表征；全局上下文聚合（GCA）模块以门控残差交互建模场景级长程几何依赖。在泰晤士河船舶数据集与仿真数据集上，KSG-Net 在多尺度船舶检测上一致优于现有方法，并在复杂海上环境展现强鲁棒性。', 'source': 'arXiv (cs.CV)', 'url': 'https://arxiv.org/abs/2609.02077', 'date': '2026-09-02'}, {'title': '双塔全局-局部框架 Enhanced Crossformer：多浮标有效波高短期预报（JMSE, 2026-09-02）', 'badge': '[论文]', 'abstract': '稀疏浮标网络上的有效波高预报因时间变异复杂、空间依赖强而困难。东南大学与纽卡斯尔大学团队提出 Enhanced Crossformer 双塔时空框架：Crossformer 分支建模跨站点长程依赖，Cheb-LSTM 分支捕捉基于图的局部交互。针对缺测问题，先以图神经网络插补模型估计缺失观测，在人工掩膜测试集上 R² 达 0.85-0.95。基于美国西海岸 52 个 NDBC 站点 2020-2024 年 3 小时间隔数据评估 3-24 小时预报，该框架在全部预见期取得最低 MAE/MSE/MAPE 与最高 R²，较最强基线在短时效降低 MSE 约 8.7%，并在 24 小时预见期内保持改进。低至中等海况下技巧最高，高能浪况与南加州湾部分遮蔽站点下降。', 'source': 'J. Mar. Sci. Eng. 14(17), 1629', 'url': 'https://www.mdpi.com/2077-1312/14/17/1629', 'date': '2026-09-02'}, {'title': '单变量深度学习有效波高预报的收益边界：五类模型系统测评（Ocean Engineering, 2026-08-31）', 'badge': '[论文]', 'abstract': '鲁东大学海洋动力灾害预警预报研究团队选取 DLinear、LSTM、PatchTST、ResAttLstm 与 Mamba2 五类代表性模型，以大西洋、太平洋和阿拉斯加湾 47 座浮标观测为案例做统一测评。结果显示五类模型总体性能十分接近，均方根误差差异约 0.3 cm，已低于常规波高仪器观测精度；相较模型本身，浮标所在海域的环境差异对预测误差影响更显著。研究还发现极端浪高与秋冬风暴季节下单变量深度学习模型的优势明显减弱。结论指出短时效单变量波高预测已接近"换模型"所能获得的收益边界，未来应更多引入风场等大气强迫信息，并加强跨站迁移及风浪-涌浪分解研究。', 'source': 'Ocean Engineering 365: 127187 / 鲁东大学', 'url': 'https://sltm.ldu.edu.cn/info/1011/2915.htm', 'date': '2026-08-31'}, {'title': '双路径降解感知网络：海上风机剩余寿命无标签预测（JMSE, 2026-08-31）', 'badge': '[论文]', 'abstract': '江苏科技大学海洋学院与挪威科技大学团队合作提出双路径降解感知网络，用于海上风机剩余使用寿命（RUL）的无标签预测。方法先以自监督方式从 SCADA 数据构建部件级健康指标：基于健康期样本估计均值与协方差计算马氏距离，并以单侧 CUSUM 累积弱退化信号，形成"时间×6部件×5特征"的健康张量；再按停机事件时刻线性倒计时生成稠密伪 RUL 标签。网络由全局时间分支（两层 GRU）与全连接图注意力分支（4头、2层）双路径构成，分别建模整体退化演化与跨部件耦合交互，以 Huber 损失加单调性约束训练。在德国北海 Farm B 数据集 5 台故障风机上按留一交叉验证，取得 MAE 111.3 小时、RMSE 122.6 小时，较最强基线平均 MAE 降低约 19%；可解释性分析显示图分支对转子轴承部件赋予最高注意力权重（0.47-0.52），与数据集以轴承退化为主的故障特征一致。', 'source': 'J. Mar. Sci. Eng. 14(17), 1595 / 江苏科技大学 & NTNU', 'url': 'https://www.mdpi.com/2077-1312/14/17/1595', 'date': '2026-08-31'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': 'Eco Wave Power 联手德国 AI engineering 共建波浪能 AI 数字孪生平台（2026-09-02）', 'badge': '[动态]', 'abstract': '岸式波浪能公司 Eco Wave Power（Nasdaq: WAVE）宣布与美国子公司同德国 AI engineering GmbH 签署协议，共同开发物理与数据混合驱动的波浪能数字孪生平台。第一阶段聚焦数字化建模海浪与该专有浮子结构的相互作用，采用 AI engineering 的粒子多物理仿真框架 PAMICS 评估不同海况下的浮子行为、结构载荷与理论能量输入，并将仿真结果与真实传感器测量比对，进而开发面向发电量与系统载荷预报的机器学习能力。核心目标是让数字孪生可迁移到不同浪况场址。项目技术栈含 NVIDIA Omniverse（数字孪生可视化与仿真工作流）与 NVIDIA Warp（仿真建模工具链），两家公司均为 NVIDIA Inception 成员。', 'source': 'Eco Wave Power / SEC 6-K', 'url': 'https://www.sec.gov/Archives/edgar/data/1846715/000121390026096473/ea030437101ex99-1.htm', 'date': '2026-09-02'}, {'title': '红海全球目的地数字孪生：10 平方公里陆海一体化实时监测（2026-09-02）', 'badge': '[动态]', 'abstract': '沙特电信集团 stc 与 Red Sea Global 在 LEAP 2026（8月31日至9月3日，利雅得）展示面向三个红海目的地的智能运营管理系统。该系统由 stc 子公司 iot squared 开发，覆盖舒拉岛与海龟湾约 10 平方公里，融合高分辨率卫星影像、三维建模与传感器及运营系统数据，覆盖建筑、车辆与生态环境，并同时纳入水上与水下环境——包括珊瑚礁在内的海洋生境指标均被持续追踪。系统通过 Nucleus 智能运营平台按职责为宾客体验、交通调度、环境监测、海上运营等团队提供分角色视图，支持在天气、客流与车流变化前进行情景推演，并在风速、海况、气温等参数越界时自动告警。', 'source': 'stc group / Red Sea Global (LEAP 2026)', 'url': 'https://eng.pressbee.net/show4860287.html', 'date': '2026-09-02'}, {'title': '连云港建成空天地一体化智慧渔港：构建渔港数字孪生场景（2026-09-01）', 'badge': '[动态]', 'abstract': '中国移动江苏公司连云港分公司以 5G 岸基与海岛协同组网补齐近海通信短板，整合北斗定位、雷达光电、AIS 基站与 AI 视频分析技术，构建渔港数字孪生场景，搭载 AI 电子围栏、渔船管控、避碰预警、救援调度等核心功能。目前连云区 75 艘在册渔船与 297 艘养殖辅助船全部纳入 24 小时动态监管，替代传统人工巡查模式；开渔期间系统可自动识别与预警渔船越界、违规出海等行为，实现海域全域感知、智能预警与协同调度。5G 网络同时支撑渔船北斗定位、AI 视频回传与水下机器人远程操控等大带宽业务。', 'source': '连云港传媒网 / 新浪', 'url': 'https://k.sina.com.cn/article_5953190046_162d6789e06703qsp0.html?loc=17', 'date': '2026-09-01'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Data Visualization', 'items': [{'title': 'CMEMS "Mediterranean in Motion"：地中海三十年增温与外来物种扩张交互式叙事（2026-08-28）', 'badge': '[动态]', 'abstract': '哥白尼海洋服务（CMEMS）发布交互式可视化作品《Mediterranean in Motion》，作者 Olivia Ann Grech，为 CMEMS Dataviz Challenge 2026 成果。作品指出地中海增温速度快于全球海洋多数区域，通过融合 CMEMS 温度异常数据与生物多样性观测，交互式呈现过去三十年间地中海如何变暖、以及外来海洋物种如何在整个海盆扩张，揭示环境变化与物种迁移如何重塑这一全球气候最敏感的海域之一。作品以"可视化叙事"形式将长期气候信号与生态响应并置，为公众与管理者理解海洋气候变化提供直观入口。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/node/23475', 'date': '2026-08-28'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': '海洋碳数据"代表性"如何量化：内在维度与可微信息不平衡框架（arXiv, 2026-08-31）', 'badge': '[论文]', 'abstract': '来自哥伦比亚大学拉蒙特-多尔蒂地球观测站、OGS 与 SISSA 的团队提出一套通用框架，用于量化复杂地球物理数据集的信息含量与表征质量，核心工具为数据流形的内在维度（ID）与可微信息不平衡（DII）。该框架被用于推导并比较表层海洋碳在 SOCAT 观测数据库与全球海洋生物地球化学模型（GOBMs）中的最优表征，并评估可从现有数据中提取信息的稳健性。主要发现：在最广泛使用的一组特征下，GOBMs 未能完整刻画 SOCAT 观测的数据空间复杂度，但通过 GOBMs 学到的变量排序与相对重要性大体正确；海洋碳的学习表征在部分区域（含南大洋）精度较低，但过去二十年间未显著演化。文章进一步展示最优表征如何提升基于距离的机器学习模型技巧，并提出两个用于比较模型与观测的新指标，可用于构建更精确的加权集合估计。', 'source': 'arXiv (physics.ao-ph)', 'url': 'https://arxiv.org/abs/2609.00133', 'date': '2026-08-31'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'HarmoCore：函数潜在扩散用于振荡波场稀疏重建（arXiv, 2026-09-02）', 'badge': '[论文]', 'abstract': '浙江大学信息与电子工程学院团队针对振荡波场稀疏重建这一欠定逆问题，提出 HarmoCore 模型，通过在核心（core）空间采样的函数潜在扩散（functional latent diffusion）实现重建。该方法将扩散过程建立于函数空间而非离散网格，天然适配波场的连续振荡结构。研究在 1%-2% 传感率下的多类实验中取得显著性能提升，为极稀疏观测条件下的波场重建提供了生成式建模新路径，可望服务于声学测量、地震与海洋波动场的稀疏采样恢复场景。', 'source': 'arXiv (cs.LG) / 浙江大学', 'url': 'https://arxiv.org/abs/2609.00679', 'date': '2026-09-02'}, {'title': 'AUWave：利用稀疏浮标观测重建区域有效波高场（Ocean Engineering, 2026-08-31）', 'badge': '[论文]', 'abstract': '鲁东大学团队将研究重点由"单点未来预测"拓展为"利用少量观测重建波高的空间分布"，提出区域波浪场重建模型 AUWave。该模型通过站点编码器将稀疏浮标观测映射至潜在网格，并结合自注意力与多尺度 U-Net 重建区域有效波高场。实验显示 AUWave 全域平均均方根误差优于代表性基线方法，且浮标空间布局比单纯增加站点数量更加关键；将同一模型直接迁移至北大西洋和北太平洋后仍保持较好精度，体现出一定的普适能力。该模型可用于浮标缺测填补、海浪数值模式初值生成、观测中断情况下的应急重建以及海洋观测网优化。', 'source': 'Ocean Engineering 350: 124202 / 鲁东大学', 'url': 'https://sltm.ldu.edu.cn/info/1011/2915.htm', 'date': '2026-08-31'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '我国首本海洋科学数据期刊《海洋科学数据快报》(DEOS) 正式上线（2026-09-01）', 'badge': '[动态]', 'abstract': '由中国科学院海洋研究所与中国海洋湖沼学会共同主办的英文期刊《海洋科学数据快报》（Data Express in Ocean Sciences, DEOS）正式上线。DEOS 为开放获取电子期刊，是中国科学院 Data Express 数据期刊集群子刊之一，由科学出版社出版发行，依托 SciCloud 平台投审稿、SciEngine 平台传播、Science DB 进行数据存储，形成全链条出版服务体系。期刊由中科院海洋所所长兼中国海洋湖沼学会理事长王凡研究员与美国科罗拉多大学 William Emery 共同担任主编，李晓峰研究员任执行主编，首届编委会设 6 位副主编、25 位编委，国际化比例达 30%。DEOS 致力于打造全球首本专注海洋科学数据的开放获取数据型期刊，遵循 FAIR 原则，收稿范围覆盖海洋数据获取技术、质量控制与标准化、数据库与平台开发、数据同化、数据产品研发、数据驱动建模与数据可视化等方向，创新收录"数据论文""方法论文""基准数据集论文""系统介绍论文"等文体，实行双盲同行评议，创刊初期减免全部出版费用。', 'source': '中国科学院海洋研究所 / 海洋知圈', 'url': 'https://www.163.com/dy/article/L5PEVVF30511KMS0.html', 'date': '2026-09-01'}, {'title': '自然资源部海洋四所参加 SOOS 科学指导委员会与 SCAR 开放科学大会（2026-09-02）', 'badge': '[动态]', 'abstract': '应南大洋观测系统（SOOS）国际项目办公室与南极研究科学委员会（SCAR）秘书处邀请，自然资源部第四海洋研究所陈建芳所长赴挪威参加 SOOS 科学指导委员会（SSC）与数据管理分委会（DMSC）联席会议及 SCAR 开放科学大会。会上介绍了中国第 42 次南极考察普利兹湾秋冬季航次报告，并参与讨论 SOOS 科学执行计划（2026-2030 Science and Implementation Plan）等议题；在 SCAR 开放科学大会上主持中国第 42 次南极考察秋冬季航次专场会议，并作 30 分钟主旨报告，介绍航次科学背景、初步考察成果亮点，以及普利兹湾值得进一步探讨的三大科学问题与初步观测设想。此次参会扩大了我国在南极研究国际合作中的参与度。', 'source': '自然资源部第四海洋研究所', 'url': 'http://www.4io.org.cn/n4/n401/n420/260902090337135212.html', 'date': '2026-09-02'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Ocean Expeditions', 'items': [{'title': '2026"蓝梦同航"联合海洋调查实习航次在青岛启航（2026-08-29）', 'badge': '[航次]', 'abstract': '8月29日，由中国海洋大学牵头的 2026"蓝梦同航"联合海洋调查实习航次启航仪式在青岛举行。来自中国海洋大学、北京大学、清华大学、厦门大学、天津大学、国防科技大学、南方科技大学和浙江海洋大学等 8 所高校的 83 名学生登上"东方红 2"海洋综合科学考察实习船，开展多学科综合海洋调查实习。本航次立足教育部"海洋动力—生态系统与气候变化及科学应对"学科突破先导项目，是教育部海洋科学领域"101 计划"《海洋观测》教材的核心实践项目，聚焦中国近海典型海洋环境，覆盖物理海洋、海洋气象、海洋地质、海洋化学、海洋生物等多学科实习模块，并对标首席科学家综合能力开展沉浸式实训，使学生全程深度参与科考航次全链条运行管理。', 'source': '青岛日报 / 观海新闻', 'url': 'https://www.toutiao.com/article/7680382292283490842', 'date': '2026-08-29'}, {'title': 'Nautilus NA181 威克岛航次进入二战沉船考古搜索窗口（2026-09-01）', 'badge': '[航次]', 'abstract': '海洋探索信托（Ocean Exploration Trust）的"鹦鹉螺号"（E/V Nautilus）执行为期 31 天的 NA181 威克岛航次，由 NOAA 海洋探索计划通过海洋探索合作研究所（OECI）资助。航次自关岛启程、于夏威夷结束，目标区域为美国管辖下最偏远、测绘程度最低的海洋环境之一，涵盖超过 40.7 万平方公里基本未被测绘的海底。9月1日至10日进入考古搜索窗口，主要目标为寻找二战中首艘被击沉的日本军舰"疾风"号（Hayate）；考古解读由 NOAA 海洋探索计划首席考古学家 Phil Hartmeyer 与雷湾国家海洋保护区海事考古学家 Andrea Yoxsimer 共同领衔，日本考古学家远程参与，并通过密歇根州阿尔皮纳的临时探索指挥中心参与直播解说。航次同时开展深渊平原与海山栖息地测绘、深海珊瑚与海绵群落调查。', 'source': 'Ocean Exploration Trust / Thunder Bay NMS', 'url': 'https://thunderbayfriends.org/event/exploration-of-wake-islands-deep-sea/', 'date': '2026-09-01'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'OSI SAF 基于 AMSR3 的海冰产品于 9 月 1 日转为业务化运行（2026-09-01）', 'badge': '[数据]', 'abstract': 'EUMETSAT 海洋与海冰卫星应用设施（OSI SAF）海冰团队宣布，基于 AMSR3 的海冰产品自 2026 年 9 月 1 日起正式转为业务化状态，AMSR3 取代 AMSR2 成为 OSI SAF 海冰产品的主要卫星输入数据源。转为业务化的产品包括：L2 海冰密集度（OSI-410-g，新文件名）、L3 海冰密集度（OSI-408-g，新文件名）、L3 海冰边缘（OSI-402-d）、L3 海冰类型（OSI-403-d）、L3 海冰漂移（OSI-405-d）、L3 海冰发射率（OSI-404-d 替代 OSI-404-b）、海冰密集度临时气候数据记录（OSI-438-a）与海冰指数（OSI-420-a）。全部新产品通过 FTP 与 THREDDS 在原路径提供，近实时产品同时在 EUMETCast 分发；AMSR2 的 OSI-408-a、OSI-410-a 与 OSI-438 将在重叠期内继续生产。海冰指数 OSI-420-a 采用双源输入：最近 16 天基于 AMSR3 快-track ICDR，更早日期仍基于 AMSR2 名义 ICDR，以兼顾时效与气候一致性。', 'source': 'EUMETSAT OSI SAF', 'url': 'https://osi-saf.eumetsat.int/community/list-of-service-messages/operational-release-amsr3-based-sea-ice-products-1st-september', 'date': '2026-09-01'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'NOAA CO-OPS 潮汐基准分析计算器（TADC）升级发布（2026-09-01）', 'badge': '[工具]', 'abstract': 'NOAA 海洋与海岸中心（CO-OPS）升级其潮汐基准计算工具，新版潮汐基准分析计算器（TADC）提供更直观的界面与更高灵活性，支持更通用的基准计算以及用户驱动的洪水频率与历时分析。工具可接受多种常用日期/时间格式，并能自动将观测重采样为潮汐基准计算所需的等时间间隔，减少上传前的人工格式整理；可输出相对于指定水位阈值的洪水事件数量与频率（按峰值水位高度与洪水历时细分），以及相对于任一计算基准的日最高/最低水位观测。工具同时提供网页版与独立 Python 版本两种形式，并改进错误处理与提示信息。随着 NOAA 国家潮汐基准纪元（NTDE）计划于 2029 年发布，TADC 也可用于计算相对新纪元的初步基准。', 'source': 'NOAA CO-OPS / Tides & Currents', 'url': 'https://tidesandcurrents.noaa.gov/news_posts/article.html?post=2604', 'date': '2026-09-01'}]}]

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
