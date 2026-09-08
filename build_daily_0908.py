# -*- coding: utf-8 -*-
"""
build_daily_0908.py — 将 2026-09-08 日报 SECTIONS 写入 feishu_write_doc.py
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': 'NWM 神经波浪模型：国际上首个融合人工智能与数值模式的海浪智能模型（Ocean Engineering 366, 127556, 2026-09-06）',
                'badge': '[论文]',
                'abstract': '中山大学海洋科学学院卢文芳团队联合南京信息工程大学董昌明团队、南方海洋实验室陈大可院士等，在国际上首次提出融合人工智能与数值模式的海浪智能模型（Neural Wave Model, NWM）。该模型保留波作用量平衡方程的动力传播核心，利用神经网络学习风输入、底摩擦等复杂源汇过程的净效应，实现全可微分混合框架。团队用 WAVEWATCH III 生成 100 组近岸斜坡样本开展敏感性实验：训练数据仅保留 10% 时方向波谱相关系数仍高于 0.99，均方根误差较前沿 AI 模型降低约 80%；观测点稀疏至 10% 时相关系数仍约 0.97；简单浅层神经网络表现优于深层注意力网络，且学到的源汇项可再现水深减小后底摩擦耗散增强的趋势，兼具精度、数据效率与物理一致性。',
                'source': 'Ocean Engineering（中山大学×南京信息工程大学）',
                'url': 'https://www.sohu.com/a/1072582500_726570',
                'date': '2026-09-06',
            },
            {
                'title': 'AquaBEV：以 3D 成像声呐为几何监督，从单目水下 RGB 图像预测 BEV 占用（arXiv, 2026-09-03）',
                'badge': '[论文]',
                'abstract': '自主水下机器人安全航行依赖于对周围自由/占用空间的理解，但仅凭单张水下 RGB 图像可用的几何线索有限，难以预测鸟瞰（BEV）占用。AquaBEV 提出在训练时以配对的三维成像声呐作为几何监督，将视觉特征映射到免标定的极坐标表征，沿距离维做因果解码后在笛卡尔 BEV 坐标重建预测。团队建立了受控水下占用基准，将多种代表性占用方法统一适配到"RGB→声呐"任务下对比：AquaBEV 取得 31.4 Visible IoU 与 38.6 Observed IoU，较最强迁移基线分别相对提升 4.0% 与 4.3%。',
                'source': 'arXiv (cs.CV)',
                'url': 'https://arxiv.org/abs/2609.04411',
                'date': '2026-09-03',
            },
            {
                'title': 'SEMI-DETR 半监督检测：仅 34 张标注影像即可让白鲸无人机调查的幼鲸检出超越监督基线（Frontiers in Marine Science, 2026-09-04）',
                'badge': '[论文]',
                'abstract': '北极白鲸航空调查中，专家标注是最大瓶颈——幼鲸是最难检测且对种群健康最关键的类别。美国佛罗里达大西洋大学（FAU）与加拿大渔业海洋部团队将 CVPR 2023 提出的半监督检测框架 SEMI-DETR（师生 EMA + 分阶段混合匹配 + 跨视图查询一致性 + 代价式伪标签挖掘）应用于白鲸航拍影像，在 7655 张无人机影像、27118 个标注个体数据集上测试。结果显示仅用 34 张（标注池 1%）标注图训练即可检出监督基线（YOLO11 各规模、Soft Teacher）漏掉的幼鲸，把专家标注负担降低 5–10 倍，且小样本下伪标签质量过滤对稀有类别尤为关键。',
                'source': 'Frontiers in Marine Science（FAU + Fisheries and Oceans Canada）',
                'url': 'https://www.techtimes.com/articles/326692/20260904/drone-ai-trained-34-beluga-images-finds-calves-supervised-models-miss.htm',
                'date': '2026-09-04',
            },
            {
                'title': 'Too Rare to Learn：把气旋轨迹硬塞给孟加拉湾海洋模拟器反而损伤预报技巧（arXiv, 2026-09-04）',
                'badge': '[论文]',
                'abstract': '神经海洋模拟器（neural ocean emulator）正被用于气旋暴露海岸的区域预报，一个看似自然的设计是"把气旋作为规定输入交给网络"。本文在孟加拉湾用 GLORYS12 再分析验证了这一设计并发现其有害：作者扣留 15 个完整气旋（65–150 kt），对比仅差 4 条规定气旋轨迹通道的两个 U-Net。跨 3 个随机种子，纯海洋模型每次运行都胜过持续性预报，而气旋条件化模型每次都不如持续性预报，两类技巧区间完全不重叠（p=3.1e-5）。根因是暴露频率而非信号内容：轨迹通道在训练日中仅 7.9% 非零，一旦激活便处于分布外。推断时将真实气旋图替换为无风暴图，留出气旋预报在每种子下提升 7.5%–16.4%。这一案例警示：对稀有信号学习出的响应可能"自信地错误"。',
                'source': 'arXiv (cs.LG / physics.ao-ph)',
                'url': 'https://arxiv.org/abs/2609.04635',
                'date': '2026-09-04',
            },
        ]
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': 'Fugro 加入欧盟 OCEANITY 项目：共建欧洲数字孪生海洋（EDITO）决策就绪应用（Fugro, 2026-09-07）',
                'badge': '[要闻]',
                'abstract': 'Fugro 宣布加入欧盟地平线欧洲计划资助的 OCEANITY 项目，与 CMCC 牵头的联盟共同为 EDITO——欧洲数字孪生海洋——设计面向海岸与海洋利益相关方的决策就绪应用，让政府、产业与公众在行动前先"预演"决策后果。Fugro 负责共同设计 EDITO 应用并管理利益相关方参与，其旗下 EOMAP 提供地球观测洞察、平台组件及支撑"海岸与城市韧性"应用的虚拟现实环境。项目运行期 2026 年 9 月至 2029 年 8 月，将围绕海岸与城市韧性、海洋空间规划、可持续海上作业开发三个用户驱动应用，并在欧洲四大海盆示范。注：Fugro 新加坡 AI 海洋数字孪生枢纽（09-03）已在此前日报收录，本条为其欧洲 EDITO 新进展。',
                'source': 'Fugro（OCEANITY / EDITO）',
                'url': 'https://www.fugro.com/news/business-news/2026/fugro-joins-eu-mission-to-create-europe-s-digital-twin-ocean',
                'date': '2026-09-07',
            },
        ]
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': '本方向今日暂无新增符合时效要求的动态',
                'badge': '[备注]',
                'abstract': '近一周未检索到符合收录标准（发布 ≤14 天）的海洋可视化新工具/新作品，本期从缺。',
                'source': '',
                'url': '',
                'date': '2026-09-08',
            },
        ]
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality",
        "items": [
            {
                'title': '本方向今日暂无新增符合时效要求的动态',
                'badge': '[备注]',
                'abstract': '近一周未检索到符合收录标准（发布 ≤14 天）的海洋数据质量方向新方法/新规范（候选的 JMSE 大气校正 QA 选择论文编号偏早、超出时效窗口，已剔除）。',
                'source': '',
                'url': '',
                'date': '2026-09-08',
            },
        ]
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': 'A-Predator：各向异性核点卷积的多波束测深点云配准网络（Remote Sensing 18(17), 3035, 2026-09-05）',
                'badge': '[论文]',
                'abstract': '多波束测深（MBES）点云配准是海底测绘与海洋勘探的基础，但其噪声高、重叠率低、条带式扫描造成的强各向异性分布令常规配准算法失效。西北工业大学团队提出 A-KPConv 算子：用 PCA 估计局部几何主方向，构造仿射变换让卷积核形状与朝向贴合局部几何，将特征提取从各向同性聚合转向沿主结构方向的结构感知学习；并将其嵌入 Predator 低重叠配准框架形成 A-Predator。在公开 Dotson-east 数据集上，10% 极低重叠条件下配准召回从 31.63% 提升至 59.55%，跨数据集迁移至自采 LQL-MBES 数据同样有效。',
                'source': 'Remote Sensing（西北工业大学）',
                'url': 'https://www.mdpi.com/2072-4292/18/17/3035',
                'date': '2026-09-05',
            },
            {
                'title': '跨河口颜色锋识别泛化研究：多尺度光谱-空间特征 + DenseNet-121（JMSE 14(17), 1657, 2026-09-06）',
                'badge': '[论文]',
                'abstract': '水色锋（color front）是光学性质陡变的水体过渡带，传统梯度阈值法难以跨河口迁移、易大面积过检。中科院地理资源所团队构建 165 维多尺度光谱-空间特征（7 种窗口 × 均值/标准差 × 11 波段），重排为 3D 张量后做 DenseNet-121 迁移学习并叠加红光波段后处理约束。域内测试准确率与 F1 均达 0.953，优于随机森林；跨河口泛化平均 F1 为 0.744——径流主导的密西西比河口最佳（0.874），径流-潮汐共同控制的多通道珠江口因光学异质性降至 0.607。红光约束可减少面积误检并改善锋面空间连续性，但其有效性取决于光学可分性。',
                'source': 'Journal of Marine Science and Engineering（中科院地理科学与资源研究所）',
                'url': 'https://doi.org/10.3390/jmse14171657',
                'date': '2026-09-06',
            },
        ]
    },
    {
        "title": "六、海洋数据管理与共享",
        "en": "Data Management & Sharing",
        "items": [
            {
                'title': 'EMODnet 生物与海床栖息地开启新招标：CINEA 出资 392 万欧元，截止 10 月 23 日（EuroGOOS, 2026-09-03）',
                'badge': '[动态]',
                'abstract': '欧盟气候、基础设施和环境执行署（CINEA）为欧洲海洋观测与数据网络（EMODnet）发布新招标，总预算 392 万欧元，意向截止 2026 年 10 月 23 日。招标覆盖两个方向：EMODnet Biology（欧洲海域海洋物种分布、性状的开放互操作数据）与 EMODnet Seabed Habitats（海床栖息地数据、图件与观测的开放获取）。该招标旨在强化高质量海洋数据的获取能力，支撑科研、环境管理与欧洲海域可持续利用。',
                'source': 'EuroGOOS（CINEA / EMODnet）',
                'url': 'https://eurogoos.eu/news/emodnet-biology-and-seabed-habitats-new-call-for-tenders',
                'date': '2026-09-03',
            },
        ]
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Research Vessels",
        "items": [
            {
                'title': '"雪龙2"号北冰洋冰站作业新进展：无人机远距投放海冰浮标、抗低温磁探无人机原型测试（新华社, 2026-09-05）',
                'badge': '[航次]',
                'abstract': '我国第 16 次北冰洋科考正推进至北冰洋中央冰区（该航次 08-07 起已入此前日报），本期聚焦"雪龙2"号冰站作业阶段的新技术应用：一是首次使用无人机远距离投放海冰漂移观测浮标，最远投放距离达数公里，可实时获取单块海冰漂移速度与方向并协同刻画冰内剪切等精细化运动；二是搭载磁力仪的抗低温磁探无人机系统原型完成现场测试，成功探测到冰下 1 米以上附强电磁场发射线圈的模拟潜标、误差精度 3 米以内，为密集冰区冰下潜标回收定位提供新手段。科考队还在手动温盐深剖面中意外捕捉到海冰覆盖下海洋内部中尺度涡旋（此前仅在第 2、6 次考察中发现过），并完成我国北冰洋考察史上第二次长时间连续冰下上层海洋定点湍流观测。',
                'source': '新华社（第16次北冰洋科考）',
                'url': 'https://news.qq.com/rain/a/20260905A09MFM00',
                'date': '2026-09-05',
            },
        ]
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': '国家极地科学数据中心发布 2026 开放课题指南：设"极地 AI-Ready 数据集与模型构建"方向（中国极地研究中心, 2026-09-04）',
                'badge': '[动态]',
                'abstract': '国家极地科学数据中心（我国 20 个国家级科学数据中心之一，已汇聚约 1.1 PB、6100 余个数据集）发布 2026 年度开放课题基金申请指南，拟立 4 项、单项资助 5 万元，执行期 2026-11 至 2028-10，申请截止 2026-09-30。四个方向均面向数据科学前沿：①极地科学数据治理方法研究（数据质量评价、质量控制、元数据、互操作与标准化）；②数据治理与分析挖掘工具研制（含可视化工具）；③面向极地重点服务的专题数据产品开发；④面向极地重点应用需求的 AI-Ready 数据集与模型构建（训练数据集、基准数据集及模型成果）。后两个方向直接呼应极地科研对高质量、AI 就绪数据的迫切需求。',
                'source': '中国极地研究中心（国家极地科学数据中心）',
                'url': 'https://www.pric.org.cn/index.php?c=show&id=3489',
                'date': '2026-09-04',
            },
            {
                'title': '南海海洋大数据智能管理平台：130 TB 数据入库，AI 识别 + 数字孪生支撑南海智慧治理（《中国测绘》, 2026-09-04）',
                'badge': '[动态]',
                'abstract': '自然资源部南海海域海岛中心打造的南海海洋大数据智能管理与应用平台获专题报道：平台完成 60 余项历史项目资料数字化，建成 260 多类空间图层，入库数据超 500 万条、总存储突破 130 TB（从 1965 年纸质观测档案到卫星/浮标实时数据）。五大核心功能包括：自研空间数据处理引擎的多源数据汇集、北斗三代备用的多链路传输、卫星/无人机影像当日处理入库的自动化流程、面向红树林/海上风电/海水养殖的 AI 智能识别（整体准确率超 85%、红树林识别精度 90% 以上）、以及覆盖百余座海岛实景建模的海洋数字孪生展示。平台支撑海域立体分层设权、"风电+养殖"立体开发等应用，下一步将打造全域"南海孪境"陆海一体实景建模与对话式智能检索。',
                'source': '自然资源部宣传教育中心（南海海域海岛中心）',
                'url': 'https://www.pecmnr.cn/news.html?aid=5318100',
                'date': '2026-09-04',
            },
        ]
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code",
        "items": [
            {
                'title': 'Mini-Girona I-AUV：让水下干预机器人"可及"的开源干预型 AUV 平台（arXiv, 2026-09-02）',
                'badge': '[开源]',
                'abstract': '西班牙 Girona 大学团队发布 Mini-Girona 干预型自主水下航行器（I-AUV）平台，旨在弥合昂贵专用研究 AUV 与基础 ROV 之间的鸿沟，降低水下干预技术的准入门槛。该平台在 RAMI 2025（2025 年海上机器人技术应用与影响会议）上完成部署演示，论文详细介绍了系统架构、导航与干预能力及在真实场景中的表现，为低成本、可复现的水下干预机器人研究提供了开放参考平台。',
                'source': 'arXiv (cs.RO) · RAMI 2025',
                'url': 'https://arxiv.org/abs/2609.02605',
                'date': '2026-09-02',
            },
            {
                'title': 'Underwater Acoustic Channel Library：填补水声信道标准缺失的开源信道库（arXiv, 2026-09-02）',
                'badge': '[开源]',
                'abstract': '水声通信系统研发高度依赖真实信道模型，但该领域长期缺乏被广泛接受的信道标准。新发布的 Underwater Acoustic Channel Library 汇集多种实测与仿真水声信道，为调制解调器设计、协议验证与系统仿真提供统一可复用的信道基准，有望推动水声通信研究的可复现性与跨团队对比。',
                'source': 'arXiv (eess.SP)',
                'url': 'https://arxiv.org/abs/2609.03207',
                'date': '2026-09-02',
            },
        ]
    },
]

if __name__ == '__main__':
    content = open('feishu_write_doc.py', 'r', encoding='utf-8').read()
    new_block = 'SECTIONS = ' + repr(SECTIONS)
    pattern = re.compile(r'SECTIONS = \[.*?\]\n', re.S)
    if pattern.search(content):
        content = pattern.sub(new_block + '\n', content, count=1)
        open('feishu_write_doc.py', 'w', encoding='utf-8').write(content)
        total = sum(len(s['items']) for s in SECTIONS)
        real = sum(1 for s in SECTIONS for it in s['items'] if it.get('badge') != '[备注]')
        print(f'OK: SECTIONS 已写入, {len(SECTIONS)} 方向, {total} 项（实质 {real} 条 + 备注 {total-real}）')
    else:
        print('ERROR: SECTIONS pattern not found')
