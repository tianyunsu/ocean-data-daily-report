# -*- coding: utf-8 -*-
"""Write SECTIONS for 2026-09-20 into feishu_write_doc.py (regex replace)."""
import re

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': 'OceanMoE：条件稀疏专家混合框架用于长时程多变量海洋预报',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.19768 提出面向长时程多变量海洋预报的 OceanMoE 框架，通过内容条件化的稀疏路由在共享海洋上下文与自适应专家特化之间取得平衡，兼顾多变量耦合关系与区域差异，为长时效海洋预报提供了结构化条件稀疏计算的新范式。',
                'source': 'arXiv (cs.LG)',
                'url': 'https://arxiv.org/abs/2609.19768',
                'date': '2026-09-17',
            },
            {
                'title': '2026海洋合作发展论坛：中国首个海洋Token（词元）工厂发布，汇聚130多类涉海数据与20余个海洋大模型',
                'badge': '[要闻]',
                'abstract': '9月17-18日在青岛举行的2026海洋合作发展论坛上，面向海洋产业的专属智能要素供给平台"深蓝智擎·海洋Token工厂"正式发布并落地青岛。该平台由山东移动海洋实验室主导建设，汇聚130多类涉海数据、20余个海洋领域专有大模型，实现海洋智能服务"即开即用"；论坛同期报道了"琅琊"海洋大模型2.0将台风、风暴潮纳入智能预报体系，以及"蓝鲲智种"蓝色种业大模型等成果。',
                'source': '中新社（青岛）',
                'url': 'https://m.chinanews.com/wap/detail/cht/zw/10699119.shtml',
                'date': '2026-09-18',
            },
            {
                'title': 'Drift Field Net：从现场与卫星观测学习海洋拉格朗日漂移场，定位误差较业务模式减小约20公里',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.16288 提出深度神经网络 Drift Field Net，直接从卫星与现场观测学习海洋表层流场并预报拉格朗日漂移，用于漂浮物轨迹与搜救支撑；对比业务化数值模式，平均定位误差减小约20公里，展示了数据驱动漂移预报在应急场景的应用价值。',
                'source': 'arXiv (physics.ao-ph)',
                'url': 'https://arxiv.org/abs/2609.16288',
                'date': '2026-09-14',
            },
            {
                'title': '多标签比例学习重新定义海冰类型预测：冰图弱监督下MAE最高降低21.5%',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.16347 将海冰类型预测重构为弱监督的多标签比例学习问题，以冰区图（ice chart）多边形为弱标签训练，无需逐像素标注；在SAR与多模态输入上，相比基线MAE分别降低14.5%与21.5%，为业务化海冰制图提供了低标注成本的训练范式。',
                'source': 'arXiv (cs.CV)',
                'url': 'https://arxiv.org/abs/2609.16347',
                'date': '2026-09-14',
            },
            {
                'title': 'OceanSim 扩展：以合成数据规模化海洋感知，真实海胆检测任务验证',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.20680 在海底模拟器 OceanSim 基础上构建合成数据生成管线，用于规模化训练水下感知模型，并在真实世界的海胆检测任务上验证了合成到真实的迁移效果，为海洋生物监测中标注数据稀缺问题提供了可扩展的解决方案。',
                'source': 'arXiv (cs.CV)',
                'url': 'https://arxiv.org/abs/2609.20680',
                'date': '2026-09-17',
            },
        ],
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Digital Twin of the Ocean',
        'items': [
            {
                'title': '本方向暂无新增',
                'badge': '[备注]',
                'abstract': '本期未收录新条目：DISCUSS 深海微生物数字孪生系统、DTO-BioFlow 生物多样性数据接入研讨会、E-ODP 电子海洋钻探研讨会与 OCEANITY/EDITO 相关动态均已在 09-15 期及此前收录；DITTO Summit 2026 议程公布与 06-18 期（摘要征集）为同一官网页面，按去重铁律不重复收录。',
                'source': '',
                'url': '',
                'date': '',
            },
        ],
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization',
        'items': [
            {
                'title': '稀疏视角水下3D高斯泼溅：密集几何先验显著改善水下重建几何质量',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.18737 研究水下稀疏视角三维高斯泼溅（3DGS）重建，将基于物理的水下成像模型引入泼溅优化，并系统分析几何初始化质量对重建的影响，提出利用密集几何先验缓解水下散射与稀疏视角导致的几何畸变，可服务于水下遗迹数字化与生态调查可视化。',
                'source': 'arXiv (cs.CV)',
                'url': 'https://arxiv.org/abs/2609.18737',
                'date': '2026-09-16',
            },
            {
                'title': '分类学条件控制的浮游生物图像生成：CLIP编码器+扩散Transformer应对长尾数据',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.11673 提出以分类学标签为条件的浮游生物显微图像生成框架，采用CLIP文本编码器与扩散Transformer生成分类学一致的合成图像，用于增广长尾分布的浮游生物自动成像数据集，提升稀有类识别能力。',
                'source': 'arXiv (cs.CV)',
                'url': 'https://arxiv.org/abs/2609.11673',
                'date': '2026-09-10',
            },
            {
                'title': 'LOTUSim-Energy：面向海上风电运维的多域人-无人机实时海事仿真平台',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.17124 发布 LOTUSim-Energy，一个覆盖 UAV、USV、AUV、ROV 多域平台的实时海事仿真器，支持海上运维场景中的人-无人机交互研究与三维可视化演练，为海上风电运维培训与自主作业策略评估提供平台工具。',
                'source': 'arXiv (cs.RO)',
                'url': 'https://arxiv.org/abs/2609.17124',
                'date': '2026-09-15',
            },
        ],
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality (QA/QC)',
        'items': [
            {
                'title': 'PAMGuard 3D鲸类声定位器存在重大未报告误差，声学监测数据质量引发关注',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.20350 对广泛使用的被动声学监测软件 PAMGuard 的两个三维定位器进行系统评估，发现其对鲸类叫声的三维定位存在此前未报告的大幅误差，提示依赖该工具产出的鲸类声学定位数据集需重新审视误差结构，对海洋生物声学数据质量控制具有直接意义。',
                'source': 'arXiv (physics.ao-ph)',
                'url': 'https://arxiv.org/abs/2609.20350',
                'date': '2026-09-17',
            },
            {
                'title': 'UniqueShip：控制数据泄漏的水声船舶分类基准发布，含4218艘船2460小时数据',
                'badge': '[数据]',
                'abstract': 'arXiv 2609.13659 指出既有水声船舶识别基准普遍存在同一船舶跨训练/测试集的数据泄漏问题，并基于 Ocean Networks Canada 数据构建 UniqueShip 基准：2460小时音频、4218艘唯一船舶，按船只唯一性严格划分，为水声分类模型的真实泛化能力提供了可信评测基础。',
                'source': 'arXiv (cs.SD)',
                'url': 'https://arxiv.org/abs/2609.13659',
                'date': '2026-09-12',
            },
            {
                'title': '多冰图不确定性感知的海冰类型制图：软监督提升与多标注者分歧的一致性',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.09451 融合多国海冰服务机构的多种冰区图产品，量化标注不确定性与模型不确定性，以软监督策略训练海冰发展阶段分类模型；结果显示软监督显著提升模型输出与多标注者分歧的相关性，为海冰数据集标注质量控制提供了不确定性量化框架。',
                'source': 'arXiv (cs.LG)',
                'url': 'https://arxiv.org/abs/2609.09451',
                'date': '2026-09-08',
            },
            {
                'title': 'SeaExplorer滑翔机数据开源质量控制管线发布（加那利群岛La Palma案例）',
                'badge': '[开源]',
                'abstract': 'Frontiers in Marine Science（Ocean Observation栏目）发表面向 SeaExplorer 系列滑翔机数据的开源质量控制管线，并在加那利群岛 La Palma 以东海域给出案例验证，涵盖声速、溶解氧等传感器数据的延迟模式QC流程，代码与流程可供滑翔机数据管理中心复用（经出版商页面核实，2026-09-07发表）。',
                'source': 'Frontiers in Marine Science',
                'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1905807/full',
                'date': '2026-09-07',
            },
        ],
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': 'GDCM-EOF：自监督时空重构填补卫星叶绿素a观测缺口，加勒比海R²提升至0.998',
                'badge': '[论文]',
                'abstract': 'Journal of Remote Sensing（Science合作期刊）发表 GDCM-EOF 自监督时空缺口填充框架：以地理位置编码表征大尺度空间梯度，以EOF低秩模态注入背景一致性先验，并采用分阶段知识迁移与多尺度注意力增强极端缺失下的鲁棒性。在ESA OC-CCI v6.0日尺度叶绿素a数据上，加勒比海测试RMSE由0.107降至0.019、R²由0.803升至0.998，全球尺度R²由0.904升至0.979，并能恢复热带不稳定波等中尺度结构。',
                'source': 'Journal of Remote Sensing (Science Partner Journal)',
                'url': 'https://spj.science.org/doi/10.34133/remotesensing.1064',
                'date': '2026-09-07',
            },
            {
                'title': '高光谱叶绿素反演究竟需要多少光谱信息？符号回归给出量化答案',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.18531 以符号回归系统评估高光谱反射率中叶绿素浓度反演所需的光谱信息量，识别对反演贡献最大的波段组合与光谱特征，为下一代水色卫星（如高光谱任务）的波段配置与反演算法设计提供定量依据。',
                'source': 'arXiv (physics.ao-ph)',
                'url': 'https://arxiv.org/abs/2609.18531',
                'date': '2026-09-16',
            },
            {
                'title': 'AquaCubeAI：Φsat-2星上部署的轻量化近岸浊度监测模型',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.12744 提出可在 Φsat-2 卫星嵌入式VPU上运行的轻量机器学习模型 AquaCubeAI，直接在星上完成多光谱影像的近岸水体浊度估计，实现低延迟近岸水质监测，是"在轨AI处理海洋光学数据"的代表性实践。',
                'source': 'arXiv (cs.CV)',
                'url': 'https://arxiv.org/abs/2609.12744',
                'date': '2026-09-11',
            },
            {
                'title': '多会话多模态水下建图：声呐+光学数据的因子图联合优化框架',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.17929 提出跨会话、声学与光学联合的多模态水下建图框架，以因子图优化同时估计轨迹与声呐-光学数据配准，解决长时间尺度水下调查中漂移累积与多源数据一致性问题，可服务于海底考古与生境制图的数据融合处理。',
                'source': 'arXiv (cs.RO)',
                'url': 'https://arxiv.org/abs/2609.17929',
                'date': '2026-09-15',
            },
            {
                'title': '多波束水体数据全扫幅空间上下文深度学习底检测，知识蒸馏支持嵌入式实时推理',
                'badge': '[论文]',
                'abstract': 'JMSE 14(18):1676（东海实验室海洋感知中心）提出建模全扫幅空间上下文的深度卷积架构，用于多波束测深仪水体数据中的海底检测，在EM302/EM710深水数据上克服鱼群与气泡羽流干扰导致的误检，并经知识蒸馏压缩后可在嵌入式边缘设备上高速推理。',
                'source': 'J. Mar. Sci. Eng. (MDPI)',
                'url': 'https://www.mdpi.com/2077-1312/14/18/1676',
                'date': '2026-09-09',
            },
        ],
    },
    {
        'title': '六、数据管理与共享',
        'en': 'Data Management & Sharing',
        'items': [
            {
                'title': 'UN海洋十年发布《海洋数据共享与国家安全》讨论稿，线上调查征询至9月底',
                'badge': '[政策]',
                'abstract': '联合国"海洋十年"发布讨论稿《Ocean Data Sharing and National Security》（OceanExpert文档38785），探讨政府、科研机构、产业、国防与数据管理者如何在保障正当国家安全关切的同时最大化海洋数据共享收益，并开放线上调查征集意见（截至2026年9月底）。该稿原始发布于8月27日（>14天，因征询窗口仍在进行中按重要性豁免收录），EMODnet表态支持"尽可能开放、必要时限制"原则。',
                'source': 'UN Ocean Decade / EC EMODnet Newsroom',
                'url': 'https://ec.europa.eu/newsroom/emodnet/items/952324/en',
                'date': '2026-08-27',
            },
            {
                'title': '2026海洋合作发展论坛发起"海洋十年"海洋公益行动全球倡议：海洋预报等公共产品面向全球开放共享',
                'badge': '[政策]',
                'abstract': '9月17日举行的2026海洋合作发展论坛发起"海洋十年"海洋公益行动全球倡议，提出推动海洋预报、防灾减灾等公共产品与治理工具面向全球开放共享，支持公益组织与志愿者参与生态监测、修复巡护和社区教育。论坛同期发布《中国海洋发展指数报告2026》与《国家海洋综合试验场（威海）海上试验流程》（五阶段19节点，见八、九方向相关条目）。',
                'source': '新华社报道 · 网易号转载稿（转载关系已标注）',
                'url': 'https://www.163.com/dy/article/L779I5MM05346RC6.html',
                'date': '2026-09-19',
            },
        ],
    },
    {
        'title': '七、开放航次与科考',
        'en': 'Open Cruises & Ship-time',
        'items': [
            {
                'title': '中国-海管局联合培训研究中心深海科研项目在青岛落地启动，聚焦国际海底数据处理分析',
                'badge': '[要闻]',
                'abstract': '9月17日，2026海洋合作发展论坛平行论坛"探索深海——海洋未来产业的价值变革"在青岛西海岸新区举行，中国-国际海底管理局联合培训研究中心深海科研项目正式落地启动，聚焦国际海底数据处理分析与西北太平洋深海生物多样性研究，补齐全球深海科研数据短板；十余位院士专家联名发布《海洋矿产勘查开发与生态环境保护协同发展倡议书》。',
                'source': '腾讯新闻',
                'url': 'https://news.qq.com/rain/a/20260918A0AOBG00',
                'date': '2026-09-18',
            },
            {
                'title': 'CougarTail与CUB：开源圆柱形水下耐压舱通用电子桅杆与中央公用板',
                'badge': '[开源]',
                'abstract': 'arXiv 2609.10230 发布面向圆柱形水下耐压舱的开源电子组件：CUB中央公用板与CougarTail传感器桅杆，统一供电、通信与传感器接口，显著压缩舱内堆叠体积、提升载荷能力，为科研与教育级水下平台提供可复用的开源硬件方案（硬件装备归入本方向）。',
                'source': 'arXiv (cs.RO)',
                'url': 'https://arxiv.org/abs/2609.10230',
                'date': '2026-09-09',
            },
        ],
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': 'Copernicus Sentinel-3C发射成功：海洋水色、海表温度与海平面观测能力再增强',
                'badge': '[动态]',
                'abstract': '9月15日，哥白尼Sentinel-3C从法属圭亚那欧洲航天港发射入轨，与两颗姊妹星组网。星上搭载海洋水色、海表温度与海平面测量三类互补载荷，将接续保障CMEMS等业务化海洋监测与预报服务的卫星观测数据链（CMEMS于9月16日发布专题报道）。',
                'source': 'Copernicus Marine Service',
                'url': 'https://marine.copernicus.eu/news/copernicus-sentinel-3c-launched',
                'date': '2026-09-16',
            },
            {
                'title': 'CMEMS第10期《海洋状况报告》(OSR10)将于9月30日发布：十年海洋科学评估纪念版',
                'badge': '[报告]',
                'abstract': '哥白尼海洋服务预告：第10期海洋状况报告（OSR10）将于2026年9月30日发布，纪念该系列报告发布十周年。本期延续独立同行评审（发表于State of the Planet期刊），内容涵盖海洋盐度与海平面变化、海洋热浪、极端事件对沿海基础设施的影响及海洋生态系统变化，并以"海洋叙事"方法聚焦极地与小岛屿发展中国家（SIDS）两个热点区域（原发布日09-04，因十周年节点按重要性豁免收录）。',
                'source': 'Copernicus Marine Service',
                'url': 'https://marine.copernicus.eu/news/what-ocean-state-report',
                'date': '2026-09-04',
            },
            {
                'title': '《中国海洋发展指数报告2026》发布：2025年指数132.3，海洋生产总值达11万亿元',
                'badge': '[报告]',
                'abstract': '国家海洋信息中心与中国海洋发展研究会在2026海洋合作发展论坛上发布《中国海洋发展指数报告2026》：2025年中国海洋发展指数为132.3，比上年增长2.5%；其中科技创新指数138.5，"瞰海"等海洋领域AI大模型相继发布、深海探测与数智技术装备取得新进展；全国海洋生产总值达11万亿元，同比增长5.5%。',
                'source': '中国新闻网',
                'url': 'https://www.chinanews.com.cn/sh/2026/09-17/10698393.shtml',
                'date': '2026-09-17',
            },
        ],
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '面向空-海两栖混合任务的自定义PX4固件发布',
                'badge': '[开源]',
                'abstract': 'arXiv 2609.20691 发布面向空-海两栖混合任务的PX4自定义固件扩展，在保留标准飞行功能的同时，支持两栖无人机自主海洋导航任务的统一规划与执行，为开源飞控社区贡献海空跨介质任务能力。',
                'source': 'arXiv (cs.RO)',
                'url': 'https://arxiv.org/abs/2609.20691',
                'date': '2026-09-17',
            },
            {
                'title': 'SPAR：LLM驱动的AUV故障诊断与恢复闭环仿真平台',
                'badge': '[论文]',
                'abstract': 'arXiv 2609.20620 提出SPAR闭环仿真架构，将AUV仿真软件与大语言模型驱动的故障诊断、恢复规划耦合，实现无人干预下的故障缓解策略评估，为AUV自主运维工具链提供可复现的测试平台（软件平台归入本方向）。',
                'source': 'arXiv (cs.RO)',
                'url': 'https://arxiv.org/abs/2609.20620',
                'date': '2026-09-17',
            },
            {
                'title': 'HoloOcean沿岸环境自动生成管线：从航拍影像到UE5水下仿真场景',
                'badge': '[工具]',
                'abstract': 'arXiv 2609.10484 为开源水下机器人仿真器 HoloOcean 增加沿岸环境自动生成能力：基于Unreal Engine 5，从俯视影像自动构建沿岸仿真场景，降低海洋机器人算法在真实沿岸环境中的仿真验证门槛，工具能力以论文形式正式发布。',
                'source': 'arXiv (cs.RO)',
                'url': 'https://arxiv.org/abs/2609.10484',
                'date': '2026-09-09',
            },
        ],
    },
]


def main():
    src_path = 'feishu_write_doc.py'
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_repr = repr(SECTIONS).replace('\\x27', "'")
    pattern = re.compile(r'SECTIONS = \[.*?(?=\ndef tr\(|\n# ---|\Z)', re.DOTALL)
    if not pattern.search(content):
        raise SystemExit('ERROR: SECTIONS block not found in feishu_write_doc.py')
    content = pattern.sub('SECTIONS = ' + new_repr + '\n\n\n', content, count=1)

    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(content)

    total = sum(len(s['items']) for s in SECTIONS)
    effective = sum(1 for s in SECTIONS for i in s['items'] if i.get('badge') != '[备注]')
    print(f'OK: SECTIONS written. Total items: {total} (effective: {effective})')


if __name__ == '__main__':
    main()
