# -*- coding: utf-8 -*-
"""
build_daily_0824.py — 将 2026-08-24 日报 SECTIONS 写入 feishu_write_doc.py
"""
import re

SECTIONS = [
    {
        "title": "一、海洋人工智能",
        "en": "Ocean AI / Marine Artificial Intelligence",
        "items": [
            {
                'title': 'DLESyM-Ocean：深度学习概率全球上层海洋-海冰模拟模型（arXiv, 2026-08-12）',
                'badge': '[论文]',
                'abstract': '华盛顿大学与NVIDIA团队提出 DLESyM-Ocean——深度学习地球系统模型，模拟全球现代海冰与上层海洋状态。与基于扩散目标或连续排序概率分数的传统概率模型不同，该模型采用 patch energy score loss 训练，在大气强迫驱动下能生成校准良好、空间连贯、技巧可靠的海冰与上层海洋集合预报，且自回归多年运行稳定、相对再分析偏差极小。海冰极端事件、强海洋热浪、2023年厄尔尼诺转换与全球均温飙升等案例验证显示其能产生真实的上层海洋轨迹与充分集合多样性，为次季节-季节预报提供高计算效率工具。',
                'source': 'arXiv / physics.ao-ph（华盛顿大学+NVIDIA）',
                'url': 'https://arxiv.org/abs/2608.11545',
                'date': '2026-08-12',
            },
            {
                'title': 'Underwater Color Restoration with Vanishing Uncertainty：水下颜色恢复不确定性理论（arXiv, 2026-08-16）',
                'badge': '[论文]',
                'abstract': 'Sea-thru 作者 Derya Akkaynak 团队从理论侧审视水下颜色恢复：指出在完全数学一般性下该问题病态（fatally ill-posed），需额外约束将解限定到有限不确定区间；当前方法几乎完全依赖经验验证，理论与真实数据约束之间的差距理解不足，难以判断现有方法是否在求解一个实际可解的问题。研究识别出保证有界不确定性（随相机空间分辨率提高收敛至零）的理想化条件，为水下颜色恢复的科学可信度建立理论根基，对海洋科学影像定量分析具有重要意义。',
                'source': 'arXiv / eess.IV（Solomatov & Akkaynak）',
                'url': 'https://arxiv.org/abs/2608.15598',
                'date': '2026-08-16',
            },
            {
                'title': '第九届中国模式识别与计算机视觉大会（PRCV 2026）在哈尔滨举办，聚焦水下智能视觉（2026-08-22）',
                'badge': '[要闻]',
                'abstract': '8月22日至25日，第九届中国模式识别与计算机视觉大会（PRCV 2026）在哈尔滨举办，10余位院士、1000余名学者与会。大会由四家国家级学会联合主办、哈尔滨工程大学承办——该校依托海洋复杂场景优势深耕水下智能视觉技术攻关，是唯一承办高校。会议设置大模型时代视觉智能、具身智能感知交互、多模态遥感解译等前沿专题，共19场专题论坛、10场特邀报告及30余场学术交流活动，推动智能感知成果向船舶智能系统、水下无人平台转化，服务海洋强国建设。',
                'source': '人民网',
                'url': 'https://so.html5.qq.com/page/real/search_news?docid=70000021_3176a8b080375052',
                'date': '2026-08-22',
            },
        ],
    },
    {
        "title": "二、海洋数字孪生",
        "en": "Ocean Digital Twin",
        "items": [
            {
                'title': '本周暂无明显进展（日照港数字孪生 08-14、WavyOcean 3.0 07-13 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数字孪生方向近一周无重大新平台或新框架发布。山东港口日照港集装箱数字孪生系统（08-14收录）、WavyOcean 3.0（07-13/07-28收录）、DITTO Summit 2026（07-30收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://ocean-ecosystem.wiki/',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "三、海洋可视化",
        "en": "Ocean Visualization",
        "items": [
            {
                'title': '本周暂无明显进展（MyOcean Health 07-01、MyOcean Pro 3D 08-03 已收录）',
                'badge': '[关注]',
                'abstract': '海洋可视化方向近一周无重大新工具或平台发布。Copernicus MyOcean Health（07-01收录）、MyOcean Pro 3D可视化路线图（08-03收录）、WavyOcean 3.0（07-13收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://myocean.marine.copernicus.eu/',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "四、海洋数据质量",
        "en": "Ocean Data Quality",
        "items": [
            {
                'title': '本周暂无明显进展（DTF-Net 08-07、ML辅助事件感知QC 08-08 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据质量方向近一周无重大新方法或新进展发布。DTF-Net 深度学习风数据质控（08-07收录）、ML辅助事件感知QC框架（08-08收录）、BGC-Argo CHLA 大规模再处理（07-11收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://www.argo.org.cn/',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "五、海洋数据处理",
        "en": "Ocean Data Processing",
        "items": [
            {
                'title': 'DBSD-Net：海表温度超分辨率的双分支状态位移网络（arXiv, 2026-08-15, IEEE JSTARS）',
                'badge': '[论文]',
                'abstract': '中国海洋大学与密西西比州立大学团队提出 DBSD-Net，面向卫星海表温度（SST）图像超分辨率：双分支架构中，小波频段分支通过离散小波变换显式分离低频与高频分量（引入带门控结构细化的结构状态空间模块SSSM捕获长程依赖、位移门模块DGM学习位移场进行几何感知高频细节调制），VGGUNet分支从冻结的预训练VGG骨干提取多尺度语义特征，缓解卫星数据空间变化退化对海洋锋面等精细热结构的模糊。多个公开SST数据集实验显示其全面超越现有最优方法，已获 IEEE JSTARS 录用。',
                'source': 'IEEE JSTARS / arXiv（中国海洋大学）',
                'url': 'https://arxiv.org/abs/2608.15423',
                'date': '2026-08-15',
            },
        ],
    },
    {
        "title": "六、海洋数据管理与共享",
        "en": "Ocean Data Management & Sharing",
        "items": [
            {
                'title': '本周暂无明显进展（EMODnet 24届SC 08-03、ODIS筹备IODE-29 07-22 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据管理与共享方向近一周无重大新政策或新发布。EMODnet 第24届指导委员会会议纪要（08-03收录）、ODIS指导小组筹备IODE-29（07-22收录）、海洋十年第11轮征集（08-10收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://odis.org/',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "七、开放航次与科考",
        "en": "Open Cruises & Research Expeditions",
        "items": [
            {
                'title': 'HiAOOS 2026 北极航次启航：挪威海岸警卫队 Svalbard 号回收深潜标组网（2026-08-17）',
                'badge': '[航次]',
                'abstract': '8月17日，来自挪威、波兰、美国的24名科学家与工程师登上挪威海岸警卫队 Svalbard 号，开启 HiAOOS 2026 北极航次（逾5周，南森/阿蒙森海盆）。团队将回收 HiAOOS 深海潜标网络（6套潜标+1套为阿尔弗雷德·魏格纳研究所回收）、布放多枚支撑 Euro-Argo 基础设施的剖面浮标、为国际北极浮标计划与 Polhavet 2050 布放冰基观测站。回收的两年级别深潜标时间序列对理解北极深层海洋层结、环流与海冰变率具有里程碑意义，标志着北极深部持续观测体系建设迈出重要一步。',
                'source': 'Norwegian Armed Forces / NERSC',
                'url': 'https://www.forsvaret.no/en/news/articles/hiaoos-2026-expedition',
                'date': '2026-08-17',
            },
        ],
    },
    {
        "title": "八、海洋数据中心",
        "en": "Ocean Data Centers",
        "items": [
            {
                'title': '本周暂无明显进展（GEBCO_2026 WMS 08-04、Argo快照 08-08 已收录）',
                'badge': '[关注]',
                'abstract': '海洋数据中心方向近一周无重大新发布。GEBCO_2026 网格 WMS 图层上线（08-04收录）、Argo GDAC 全球快照（08-08收录）、CMEMS 8月北极潮汐3km产品（路线图标注 Aug 2026，尚无精确发布日期）已纳入跟踪，本期不重复收录。',
                'source': '-',
                'url': 'https://seabed2030.org/',
                'date': '2026-08-24',
            },
        ],
    },
    {
        "title": "九、工具与代码资源",
        "en": "Tools & Code Resources",
        "items": [
            {
                'title': '本周暂无明显进展（gridstats v2.6.0 08-12、wavespectra 4.8.0 07-22 已收录）',
                'badge': '[关注]',
                'abstract': '海洋工具与代码资源方向近一周无重要新版本或新开源项目发布。gridstats v2.6.0（08-12收录）、wavespectra v4.8.0（07-22收录，5.0仍未发布）、cstar-ocean v0.8.0（08-05收录）均已在此前日报覆盖，本期不重复收录。',
                'source': '-',
                'url': 'https://github.com/topics/oceanography',
                'date': '2026-08-24',
            },
        ],
    },
]

# 读入 feishu_write_doc.py 并替换 SECTIONS
DATA_SOURCE = r'C:\Users\Administrator\WorkBuddy\20260327163052\ocean-data-daily-report\feishu_write_doc.py'
with open(DATA_SOURCE, encoding='utf-8') as f:
    content = f.read()

new_block = 'SECTIONS = ' + repr(SECTIONS)
pattern = re.compile(r'SECTIONS = \[.*?\]\n', re.S)
if pattern.search(content):
    content = pattern.sub(new_block + '\n', content, count=1)
else:
    raise RuntimeError('未找到 SECTIONS 占位')

with open(DATA_SOURCE, 'w', encoding='utf-8') as f:
    f.write(content)

n_items = sum(len(s['items']) for s in SECTIONS)
print(f'OK: SECTIONS 已写入, {len(SECTIONS)} 方向, {n_items} 条')
