#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""替换 feishu_write_doc.py 中的 SECTIONS 数据（2026-08-07 日报）"""

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '“盘古”海洋智能预报大模型工程化落地：全国首个AI+全栈国产算力，海洋预报从“天级”迈向“分钟级”（2026-08-03）',
                'badge': '[要闻]',
                'abstract': '自然资源部 8 月 3 日发布的上半年海洋经济运行情况披露：全国首个深度融合 AI 技术、全栈国产算力支撑的“盘古”海洋智能预报大模型实现工程化落地，将实现海洋预报从“天级”到“分钟级”的颠覆性跨越。同期国家海洋信息中心主任石绥祥介绍，OceanAI 海洋时空智能大模型聚焦海洋预警预报、防灾减灾等业务场景，攻克通用大模型落地海洋场景“水土不服”问题；海境AI大模型、琅琊2.0、南溟海洋大模型及海洋数字孪生引擎 DTO Engine 2.0 相继发布。国产大模型集群正加速支撑海洋生态保护、海洋牧场、海上风电等场景应用。',
                'source': '自然资源部 / 央广网',
                'url': 'https://www.sohu.com/a/1058055789_362042',
                'date': '2026-08-03',
            },
            {
                'title': '生成式AI海啸概率预报：条件扩散模型实现实时近岸淹没概率预报（arXiv, 2026-08-05）',
                'badge': '[论文]',
                'abstract': 'arXiv:2608.04327 提出基于条件扩散模型（生成式AI）的概率集成海啸预报框架，将海啸预报从确定性向概率性转变。模型以 2011 年东日本大地震海啸数据验证，能忠实追踪震后随时间衰减的不确定性，同时准确预测淹没深度与范围。传统机器学习近岸淹没预报缺乏不确定性量化，可能产生虚假安全感；该框架调和了精度与校准，为下一代海啸早期预警提供了基础，是生成式AI在海洋灾害预报领域的标志性应用。',
                'source': 'arXiv:2608.04327',
                'url': 'https://arxiv.org/abs/2608.04327',
                'date': '2026-08-05',
            },
            {
                'title': 'BG4Sea：首个全球数据驱动海洋生物地球化学季节预报系统（arXiv, 2026-07-18，豁免）',
                'badge': '[论文]',
                'abstract': 'Mercator Ocean International 与 Sorbonne 大学团队提出 BG4Sea，据称是首个全球数据驱动的多变量海洋生物地球化学季节预报系统。架构由列自编码器（压缩垂直剖面）、潜空间预报器、FiLM 表面强迫条件器与跨注意力水平耦合模块组成，在 BIORYS4（NEMO/PISCES）全球再分析上训练，输出 1/4°、月分辨率 6 个月预报，涵盖溶解化学、生物学与碳库变量，多数变量与提前期超越持久性与气候态基线。该工作获 NeurIPS@Cam AI for Science 海报奖，是 AI 季节尺度海洋生态系统预报的代表性基线。',
                'source': 'Mercator Ocean International / arXiv:2607.16731',
                'url': 'https://arxiv.org/abs/2607.16731',
                'date': '2026-07-18',
            },
            {
                'title': 'Swimm3R：介质感知SfM+水下Beta Splatting实现鲁棒水下3D重建（arXiv, 2026-08-02）',
                'badge': '[论文]',
                'abstract': 'arXiv:2608.00950 提出 Swimm3R 统一框架，将介质感知结构从运动（SfM）与水下 Beta Splatting 结合，解决散射与衰减导致的水下 3D 重建失败。方法将空气几何先验蒸馏进前馈骨干，用物理头回归水下成像参数、相机位姿与恢复点云；水下 Beta Splatting 以 Beta 基元与散射感知几何梯度扩展高斯泼溅。团队另建巴巴多斯水下视频数据集验证，平均 PSNR 较 WaterSplatting 提升 1.47 dB，下游定位 RRA@15/RTA@15 分别提升 2.0/2.4 个百分点，为 AUV 海底测绘与生态监测提供可迁移的水下视觉基础。',
                'source': 'arXiv:2608.00950',
                'url': 'https://arxiv.org/abs/2608.00950',
                'date': '2026-08-02',
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': 'DITTO Summit 2026 早鸟注册开启，8 月 25 日公布完整议程（2026-07-30，更新）',
                'badge': '[动态]',
                'abstract': '联合国海洋十年数字孪生计划（DITTO）旗舰峰会 DITTO Summit 2026 于 7 月 30 日开启早鸟注册（至 8 月 31 日），完整议程定于 8 月 25 日公布。峰会将于 11 月 11–13 日在日本横滨举行，聚焦可运营、可互操作、用户驱动的数字孪生，覆盖实时观测、先进建模与 AI、云/边缘/高性能计算、开放架构与互操作标准，并设会前培训（11/9–10）、Hackathon 创新冲刺（海洋热浪与极端事件专题）与会后实验室（11/14–17）。摘要投稿已于 7 月 20 日截止。（更新：早鸟注册与议程节点为新增进展）',
                'source': 'DITTO / EuroGOOS',
                'url': 'https://eurogoos.eu/events/ditto-summit-2026---building-ocean-intelligence-together/',
                'date': '2026-07-30',
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期海洋可视化方向暂无重大新进展。港科大 WavyOcean 3.0（07-10 发布）、Copernicus Marine 路线图预告的 MyOcean Pro 3D Viewer（2027-01 计划）均已在前期日报详细收录（2026-07-13/07-31、08-03）。',
                'source': '',
                'url': '',
                'date': '2026-08-07',
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA-QC',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期海洋数据质量方向暂无重大新进展。BGC-Argo VAE 生物附着检测（07-11 发布）与 CMEMS Argo 叶绿素 QC3 标记（07-08）均已在 07-24/07-28 日报收录；边缘计算实时 QC 中国专利（07-07）已收录于 08-03。',
                'source': '',
                'url': '',
                'date': '2026-08-07',
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '2DCNN-LSTM 从 Sentinel-2 纹理反演海底沙波水深——低成本大范围测深新框架（Remote Sensing, 2026-08-01）',
                'badge': '[论文]',
                'abstract': '自然资源部第二海洋研究所、浙江大学与 Helmholtz-Zentrum Hereon 团队在 Remote Sensing 18(15):2511 提出空间-时序 2DCNN-LSTM 模型，从 Sentinel-2 表面反射率纹理反演海底沙波水深：CNN 提取局部图像纹理，LSTM 学习沙波形态的剖面尺度韵律连续性。模型以多波束测深训练，在台湾浅滩约 4000 km² 外推区验证 RMSE 3.78 m、MAE 2.99 m、MRE 9.1%，优于随机森林/CNN/LSTM 基线，为船测稀疏区提供低成本沙波场测深监测手段，但性能受水体光学纹理可见性制约。',
                'source': 'Remote Sensing (MDPI) 18(15):2511',
                'url': 'https://www.mdpi.com/2072-4292/18/15/2511',
                'date': '2026-08-01',
            },
            {
                'title': '贝叶斯多模态神经网络融合AUV光学/测深/侧扫声呐，开源multimodal-auv库（EAAI, 2026-07-01，豁免）',
                'badge': '[论文]',
                'abstract': '发表于 Engineering Applications of Artificial Intelligence（181:115340）的研究提出贝叶斯多模态神经网络，融合光学影像、测深与侧扫声呐三类 AUV 遥感数据，量化认知性与偶然性不确定性以提升海底生境分类可靠性：在大型 AUV 调查数据上准确率 85.5%，较单模态基线提升约 7%，并分析 30 m 斑块尺寸与 Monte Carlo 采样次数对精度/算力的平衡，支持机载实时不确定性感知生境分类。完整代码库与预训练模型经 PyPI 包 multimodal-auv 开源发布。（豁免：超14天，顶级期刊+不重复）',
                'source': 'Engineering Applications of AI / SAMS',
                'url': 'https://pure.uhi.ac.uk/en/publications/bayesian-multimodal-fusion-for-seafloor-habitat-mapping-with-auto/',
                'date': '2026-07-01',
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'title': '海洋二所牵头“普惠性海洋遥感科技”（RAISE-Ocean）入选联合国“科学十年”第三批全球计划（2026-08-01）',
                'badge': '[动态]',
                'abstract': '自然资源部海洋二所卫星海洋环境监测预警全国重点实验室何贤强研究员牵头申报的“智能助力地方行动：普惠性海洋遥感科技”（RAISE-Ocean）正式获 UNESCO 批准，入选“2024—2033 科学促进可持续发展国际十年”第三批全球计划，成为“科学十年”框架下首个聚焦海洋遥感科技领域的全球计划。计划联合澳、法、瑞典、英、美等十余国学者，构建“数据—知识—能力—行动”链条式赋能体系，探索“开放全球遥感数据+主权本地数据+协同AI进化”范式，聚焦蓝碳监测、水产养殖智能监管、渔业资源感知等五大方向。',
                'source': '自然资源部第二海洋研究所',
                'url': 'https://dy.163.com/article/L373U77H0511KMS0.html',
                'date': '2026-08-01',
            },
            {
                'title': '中国台湾海洋委员会发布 MDImageNet 海废影像资料集（CC BY 4.0），同步启动 2026 海废影像辨识国际AI竞赛（2026-07-30）',
                'badge': '[数据]',
                'abstract': '中国台湾地区海洋委员会所属国家海洋研究院于 7 月 30 日发布首套 AI-Ready“MDImageNet 海废影像资料集”：累积超 2 万张真实海岸影像、完成逾 4.2 万个海废物件标注，以国际净滩行动（ICC）分类为基础建立 NAMR 三层级分类架构，依循《人工智能基本法》推动资料治理与开放共享，以 CC BY 4.0 授权释出，供研究机构、教育单位与产业界投入海洋 AI 训练。同期由 AWS 提供技术支持、工研院 AIdea 平台执行，启动“2026 海废影像辨识国际AI竞赛”，以开放数据+国际竞赛双轨推动海洋垃圾智慧辨识。',
                'source': '中国台湾海洋委员会国家海洋研究院（NAMR）',
                'url': 'https://www.namr.gov.tw/ch/home.jsp?dataserno=202607300001&id=36&mcustomize=news_view.jsp&parentpath=0%2C6',
                'date': '2026-07-30',
            },
            {
                'title': 'DORI 虎鲸声学数据集：正无标签+主动学习构建 5298 小时南方定居型虎鲸声音档案（arXiv/KDD 2026 审稿, 2026-08-07）',
                'badge': '[数据]',
                'abstract': '研究团队提出结合正无标签学习（PU Learning）与主动学习的方法，从超过 30 年公开水听器记录中筛选海洋哺乳动物声音，构建目前规模最大的南方定居型虎鲸声学数据集之一 DORI（Dataset for Orca Resident Interpretation），含 5298 小时海洋哺乳动物声音、其中 919 小时为南方定居型虎鲸。数据整合 Ocean Networks Canada（6 万+水听器日）、SanctSound、海洋观测计划（OOI）与 OrcaSound 等长期被动声学监测项目，论文在 arXiv 发布并正接受 KDD 2026 审稿，为濒危鲸类声学监测与 AI 识别提供高质量开放数据基础。',
                'source': 'arXiv / KDD 2026（审稿中）',
                'url': 'https://new.qq.com/rain/a/20260807A03QSD00',
                'date': '2026-08-07',
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '“奋斗者”号发现全球最深最大鲸类化石群：Nature 论文揭示 1200 公里深渊“鲸类大墓地”（2026-06-10 发表，豁免）',
                'badge': '[论文]',
                'abstract': '中科院深海所主导的“全球深渊探索计划”依托“探索一号”科考船与“奋斗者”号全海深载人潜水器，在东南印度洋迪亚曼蒂纳深渊（水深 4616–7001 m、绵延约 1200 km）开展 32 次下潜，发现全球已知最深、规模最大的鲸落生态系统与鲸类化石群：5 处化能自养阶段鲸落、476 处化石堆积点、密度高达 759.5 具/km²，锶同位素测年显示化石距今约 526 万年至 12 万年；6789 m 处鲸落为已知最深鲸落生态系统，将深度极限推进逾 2500 m。成果 6 月 10 日发表于《自然》。（豁免：顶级来源 Nature+重大发现+不重复，原始发表日 2026-06-10）',
                'source': 'Nature / 中科院深海所',
                'url': 'https://gzb.cas.cn/kyj/202606/t20260611_8227458.html',
                'date': '2026-06-10',
            },
            {
                'title': 'E/V Nautilus NA181“威克岛深海探索”航次即将启航：30 天测绘+ROV+Argo 浮标（2026-08-20 起）',
                'badge': '[航次]',
                'abstract': 'Ocean Exploration Trust 2026 航季第四个航次 NA181“Exploration of Wake Island\u0027s Deep Sea”将于 8 月 20 日—9 月 18 日开展（关岛启航、檀香山结束）。威克岛位于夏威夷与马里亚纳之间，周边 407,241 km² 海床大多未测绘，属美国管辖下调查最薄弱的区域之一。航次将利用 ROV（Hercules/Atalanta）、多波束测绘与陆上遥现系统，聚焦太平洋群岛遗产海洋国家纪念碑与威克环礁国家野生动物保护区的深海优先区，包括深渊平原、未探索海山与威克岛战役相关海洋遗产遗址，并部署全球海洋生物地球化学阵列 Argo 浮标。',
                'source': 'Ocean Exploration Trust / NOAA',
                'url': 'https://nautiluslive.org/cruise/NA181',
                'date': '2026-08-20',
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期海洋数据中心方向暂无重大新发布。GEBCO_2026 网格（28.7% 覆盖率，04-08 发布）已收录于早前日报；CMEMS 2026 年 7 月服务发布（新 MFC 入网，07-07）已收录于 08-03；Copernicus Marine 产品路线图更新（MyOcean Pro 3D 等）亦已收录于 08-03。',
                'source': '',
                'url': '',
                'date': '2026-08-07',
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': 'cstar-ocean v0.7.0 发布——海洋碳循环计算系统 Python 库迭代更新（PyPI, 2026-07-24，更新）',
                'badge': '[工具]',
                'abstract': '海洋碳追踪计算系统 Python 库 cstar-ocean 发布 v0.7.0（2026-07-24）。cstar-ocean 面向海洋碳循环建模与追踪，提供数值实验构建、运行与追踪工具链，支持 ROMS 等海洋模型的碳循环计算工作流；依赖 f90nml、roms-tools、prefect 等生态。作为海洋碳科学开源工具链的重要组件，v0.6.0 已于 07-02 收录于 07-24 日报，本版为持续迭代更新，与当前 CMEMS/BGC-Argo 碳循环再处理进展形成工具侧配套。（更新：较 07-24 日报 v0.6.0 新版本）',
                'source': 'PyPI / piwheels',
                'url': 'https://www.piwheels.org/project/cstar-ocean/',
                'date': '2026-07-24',
            },
            {
                'title': 'oceanspy v0.3.6 发布——海洋模型数据分析与可视化 Python 库（PyPI, 2026-06-15，豁免）',
                'badge': '[工具]',
                'abstract': '开源海洋模型数据分析可视化库 oceanspy 发布 v0.3.6（2026-06-15，最新版）。oceanspy 基于 Pangeo 生态（xarray、dask、xgcm），面向 MITgcm 等结构化网格海洋环流模型输出，提供类似物理海洋学家分析观测数据的方式分析模式数据的能力，支持大规模仿真（PB 级）数据集的流式计算，已在 SciServer 等平台提供公开仿真数据服务。v0.3.6 为本年度重要迭代版本。（豁免：超14天（约53天）且≤60天，顶级开源工具+不重复，原始发布日 2026-06-15）',
                'source': 'PyPI / Pangeo',
                'url': 'https://pypi.org/project/oceanspy/',
                'date': '2026-06-15',
            },
        ]
    },
]

import re
import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('SECTIONS = [')
start = idx + len('SECTIONS = ')
depth = 0
end = start
for i, ch in enumerate(content[start:], start):
    if ch == '[':
        depth += 1
    elif ch == ']':
        depth -= 1
        if depth == 0:
            end = i + 1
            break

old_sections_str = content[start:end]
new_sections_str = repr(NEW_SECTIONS)

new_content = content[:start] + new_sections_str + content[end:]

try:
    compile(new_content, 'feishu_write_doc.py', 'exec')
    print('Syntax validation: OK')
except SyntaxError as e:
    print(f'Syntax error: {e}')
    exit(1)

with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('feishu_write_doc.py updated successfully!')
print(f'Old SECTIONS size: {len(old_sections_str)} chars')
print(f'New SECTIONS size: {len(new_sections_str)} chars')

sections = ast.literal_eval(new_sections_str)
total = 0
for s in sections:
    n = len(s['items'])
    total += n
    print(f"  {s['title']}: {n} 条")
print(f"Total: {total} 条")
