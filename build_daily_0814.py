#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""替换 feishu_write_doc.py 中的 SECTIONS 数据（2026-08-14 日报）"""

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '中科院海洋所“琅琊”海洋大模型技术框架发表于《Science Bulletin》：单一模型 1/12° 全球 1-7 天预报 128 变量（2026-08-12，更新）',
                'badge': '[论文]',
                'abstract': '中科院海洋所人工智能海洋学研究组与海洋热力学过程气候变化研究组在 Science Bulletin 在线发表“琅琊”（LangYa）全球海洋智能预报大模型技术框架论文。模型面向全球海洋温盐与三维流场，构建融合跨时空演变、大气强迫与温跃层物理特征的统一预报框架，由单一模型在 1/12° 分辨率下直接生成未来 1-7 天 32 个深度层、128 个变量的全球预报（不经逐日递推）。四项关键设计：大语言模型时间嵌入显式表征预报时效、异步交叉迭代随机采样刻画大气驱动、余弦注意力海洋自注意力模块、温跃层自适应损失函数。7 天预报纬向/经向流速、温度、盐度 RMSE 分别达 0.0736/0.0701 m/s、0.4376 ℃、0.1302 psu。（更新：琅琊 2.0 模型本体已于 07-31 收录，本次为 Science Bulletin 论文正式发表）',
                'source': 'Science Bulletin / 中科院海洋所',
                'url': 'https://www.163.com/dy/article/L43FFHQN0511KMS0.html',
                'date': '2026-08-12',
            },
            {
                'title': 'Multi-AUV 自组网目标追踪：值梯度引导多智能体扩散强化学习（arXiv, 2026-08-12）',
                'badge': '[论文]',
                'abstract': 'arXiv:2608.12436 提出 VGG-MADiffRL 值梯度引导多智能体扩散强化学习算法与 MDCA 扩散分层控制架构，解决多 AUV 自组网在受限声通信、动态拓扑与海洋扰动下协同追踪机动目标难题。MDCA 构建“全局智能控制-局部在线训练-物理动作执行”三层闭环，VGG-MADiffRL 基于扩散策略，在反向去噪中引入值梯度引导动作生成，并采用双子网络联合优化与软目标更新缓解过估计与训练振荡。实验表明较现有 MARL 方法收敛更快、追踪精度更高、训练更平滑，为动态水下协同追踪提供了工程可行方案。',
                'source': 'arXiv:2608.12436',
                'url': 'https://arxiv.org/abs/2608.12436',
                'date': '2026-08-12',
            },
            {
                'title': '李群上随机物理信息神经网络：学习水下航行器随机动力学（arXiv, 2026-08-08）',
                'badge': '[论文]',
                'abstract': 'arXiv:2608.08356 提出一种数据驱动的随机水下航行器动力学学习框架：基于 Euler-Poincaré 动力学与李群几何构建随机物理信息神经网络，利用保结构随机积分、矩匹配与有限维匹配保证几何一致的训练。方法在仿真与港口码头桩导航实船数据上验证，学习到准确鲁棒的动力学模型，支持挑战性海洋环境下的安全基于模型控制，为 AUV 基础设施巡检与科学采样的自主执行提供动力学基础。',
                'source': 'arXiv:2608.08356 (Oregon State University)',
                'url': 'https://arxiv.org/abs/2608.08356',
                'date': '2026-08-08',
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '本周暂无明显进展',
                'badge': '[备注]',
                'abstract': '近期海洋数字孪生方向暂无重大新发布。港科大 WavyOcean 3.0（07-10 发布）、欧盟 DestinE 第三阶段（07月）、DITTO Summit 2026 早鸟注册与议程节点（07-30）均已在近期日报收录（2026-07-13/07-31/08-03/08-07）。',
                'source': '',
                'url': '',
                'date': '2026-08-14',
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
                'abstract': '近期海洋可视化方向暂无重大新工具发布。Copernicus Marine 路线图预告的 MyOcean Pro 3D Viewer（计划 2027-01）与 MyOcean Health 实时图表（06月上线）均已在 07-01/08-03 日报收录。',
                'source': '',
                'url': '',
                'date': '2026-08-14',
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
                'abstract': '近期海洋数据质量方向暂无重大新方法。ML辅助事件感知 QC 框架（JMSE 08-08 发表）已收录于 08-10 日报；BGC-Argo VAE 生物附着检测（07-11）与 CMEMS Argo 叶绿素 QC3 标记（07-08）已收录于 07-24/07-28。',
                'source': '',
                'url': '',
                'date': '2026-08-14',
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': 'BenthiCat 光-声多模态数据集：约百万侧扫声呐瓦片+AUV光学影像，底栖分类测绘基准（ESSD, 2026-08-10）',
                'badge': '[数据]',
                'abstract': 'ESSD 预印本发布 BenthiCat：沿西班牙加泰罗尼亚海岸采集的约 100 万侧扫声呐（SSS）瓦片，辅以测深图与 AUV 定向调查共配准光学影像，其中约 3.6 万瓦片带分割掩膜标注，用于监督微调分类模型。所有原始传感器数据与镶嵌图一并发布，并配套开源预处理与标注工具，支持自监督跨模态表征学习。该资源旨在为水下生境测绘建立标准化基准，推动海底自主分类与多传感器集成研究。',
                'source': 'ESSD (Copernicus) 预印本',
                'url': 'https://essd.copernicus.org/preprints/essd-2026-565',
                'date': '2026-08-10',
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'title': 'Copernicus Marine In Situ TAC 集成 One Ocean Expedition 帆船观测：机会式观测扩充稀疏海域覆盖（2026-08-12）',
                'badge': '[动态]',
                'abstract': 'Copernicus Marine Service 公布 In Situ TAC 最新进展：2025-2026 年 One Ocean Expedition 航次（三桅帆船 Statsraad Lehmkuhl）的观测数据已纳入哥白尼海洋目录。帆船通过连接海水入口的 ferrybox 系统连续测量温盐，经 In Situ TAC 近实时产品传输，形成沿航线近连续记录，在布雷斯特停靠期间完成全流程集成。尽管北冰洋冰况与通信中断造成数据缺口，该航次展示了机会式观测平台（仪表化船舶）对传统观测网络的补充价值，尤其填补弱采样海域覆盖。',
                'source': 'Copernicus Marine Service / In Situ TAC',
                'url': 'https://marineinsitu.eu/data-from-the-one-ocean-expedition-2025-2026-integrated-into-copernicus-marine/',
                'date': '2026-08-12',
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '“科学”号完成 2026 年度西太平洋共享航次返回母港：35 天 5845 海里，捕捉 3 次台风过境（2026-08-07，更新）',
                'badge': '[航次]',
                'abstract': '8 月 7 日，“科学”号综合考察船返回青岛母港，2026 年度西太平洋科学考察共享航次（第 15 次）圆满收官：历时 35 天、航行 5845 海里，搭载 10 余家单位 32 名科研人员，围绕西太平洋主流系-暖池变异气候环境效应等两大科学问题开展多学科综合观测。航次完成“琅琊”系列潜浮标组网运行（实时立体观测体系里程碑），精准锁定“巴威”“红霞”“白海豚”三次台风过境的海-气协同演变过程（最低气压 996 hPa、最大风速约 15 m/s），并针对可能的最强厄尔尼诺事件开展专项观测，累计采集水下海水 900 余升、表层海水 8000 余升。（更新：启航已于 07-31 收录）',
                'source': '中国科学院海洋研究所 / 央视新闻',
                'url': 'https://www.thepaper.cn/newsDetail_forward_33739031',
                'date': '2026-08-07',
            },
            {
                'title': 'NOAA Okeanos Explorer EX2605 库克群岛 ROV 探险收官：26 天完成 13 次深海下潜（2026-08-13，更新）',
                'badge': '[航次]',
                'abstract': 'NOAA 与库克群岛海底矿物管理局合作的 EX2605 库克群岛 ROV 探险于 8 月 13 日收官。26 天航次中，Okeanos Explorer 在 2500-6000 m 水深开展 13 次 ROV 下潜（Discoverer+Seirios 双机），覆盖深渊平原、海底峡谷、海山与 Manihiki 高原等生境，对深海珊瑚、多金属结核、玻璃海绵等做了系统影像记录与有限取样；同步进行多波束测绘、Argo 浮标部署与 CTD 采样，全程遥现直播。数据按 NOAA 公开数据政策入库，支持库克群岛海洋资源管理决策。（更新：07-16/07-31/08-10 收录，本次为收官）',
                'source': 'NOAA Ocean Exploration',
                'url': 'https://origin.oceanexplorer.noaa.gov/expedition/ex2605/',
                'date': '2026-08-13',
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
                'abstract': '近期海洋数据中心方向暂无重大新发布。GEBCO_2026 网格（28.7% 覆盖率，04-08 发布）、CMEMS 2026 年 7 月服务发布（新 MFC 入网，07-07）、Copernicus Marine 产品路线图更新（MyOcean Pro 3D 等）均已在前期日报收录。',
                'source': '',
                'url': '',
                'date': '2026-08-14',
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': 'gridstats v2.6.0 发布——Oceanum 海洋与气候网格统计计算库快速迭代（PyPI, 2026-08-12）',
                'badge': '[工具]',
                'abstract': 'Oceanum 开发的网格统计库 gridstats 发布 v2.6.0（2026-08-12），距 v2.5.0（07-17）不足一月。该库通过 YAML 声明式流水线对大尺度海洋与气候网格数据做惰性、核外统计计算（基于 xarray+dask），支持均值/分位数/超越概率/重现期值/方向统计/分布拟合等丰富统计函数，输出 CF 标准 NetCDF 或 Zarr，支持按月份/季节分组统计与空间分块控制内存。作为海洋数据处理工具链的新成员，为波浪后报、风能等大规模网格统计提供便捷 CLI 方案。',
                'source': 'PyPI / Oceanum',
                'url': 'https://www.piwheels.org/project/gridstats',
                'date': '2026-08-12',
            },
            {
                'title': 'π-SUB：物理信息合成水下图像增强基准数据集（arXiv, 2026-08-11）',
                'badge': '[数据]',
                'abstract': 'arXiv:2608.10589 提出 π-SUB，基于物理信息的水下图像增强（UIE）合成基准数据集生成框架：扩展经典水下成像模型，纳入深度相关下行辐照度、生物分辨吸收与散射（覆盖 10 种 Jerlov 水型）及独立可控残差现象，生成浅深、近岸-远洋配对的合成-参考图像对。全局 FID 较 Syrea 低 46%；在四种 SOTA UIE 架构（FUnIE-GAN、Pix2Pix、PUIE-Net、Phaseformer）与六个真实基准上的跨数据集评估中，UIQM 较 PHISWID 提升 4.18%、NIQE 降低 48.78%，为下一代水下图像增强方法提供高真实感、可泛化的基准。代码与数据集开源。',
                'source': 'arXiv:2608.10589',
                'url': 'https://arxiv.org/abs/2608.10589',
                'date': '2026-08-11',
            },
        ]
    },
]

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

sections = ast.literal_eval(new_sections_str)
total = 0
for s in sections:
    n = len(s['items'])
    total += n
    print(f"  {s['title']}: {n} 条")
print(f"Total: {total} 条")
