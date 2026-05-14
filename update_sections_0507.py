#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 feishu_write_doc.py 中的 SECTIONS 数据为 2026-05-07 版本
"""
import re

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. Nature Geoscience（2026-04-13）：GOFLOW——利用静止卫星热红外影像实现前所未见的海洋表面流场观测',
                'badge': '近7天',
                'abstract': 'GOFLOW（Geostationary Ocean Flow）是一种深度学习框架，利用已在轨的静止气象卫星连续热红外影像序列，首次实现了大范围海洋表面流场的高分辨率观测。该方法无需新增硬件，利用GOES和Himawari等卫星的SST梯度数据训练神经网络推断海洋表面速度场，填补了传统漂流浮标和卫星高度计的空间覆盖空白，研究成果发表于Nature Geoscience。',
                'source': 'Nature Geoscience',
                'url': 'https://www.nature.com/articles/s41561-026-01943-0',
                'date': '2026-04-13'
            },
            {
                'title': '2. Science Daily（2026-04-22）：AI揭示前所未见的海洋洋流细节',
                'badge': '近7天',
                'abstract': '基于GOFLOW技术，科学家利用深空气象卫星热红外影像，以前所未有的分辨率和覆盖范围追踪海洋表面流场。该技术能够揭示传统方法无法捕捉的中尺度到亚中尺度海洋动力学特征，对于理解海洋热量传输、营养盐输运和碳循环具有重大意义。相关代码和数据已开源。',
                'source': 'Science Daily',
                'url': 'https://www.sciencedaily.com/releases/2026/04/260421042803.htm',
                'date': '2026-04-22'
            },
            {
                'title': '3. IOCCG（2026-05）：IOCCG报告22——水生高光谱遥感科学路线图发布',
                'badge': '近7天',
                'abstract': '国际海洋色彩协调组（IOCCG）发布第22号报告《A Scientific Roadmap of Aquatic Hyperspectral Remote Sensing》，系统定义了高光谱遥感相对于传统多光谱传感器的优势，识别了新兴科学问题，并强调了待解决的技术差距和挑战。报告指出高光谱数据对内陆水体、近岸复杂水域和浮游植物功能类型识别具有变革性潜力。报告可通过DOI:10.25607/OBP-2062免费获取。',
                'source': 'IOCCG',
                'url': 'https://ioccg.org/2026/05/may-2026/',
                'date': '2026-05-05'
            }
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. Ocean Science杂志（2026-02）：DeepDA——基于深度学习的潜在空间数据同化方法',
                'badge': '',
                'abstract': '发表于Ocean Modelling的DeepDA方法提出了一种基于深度学习的潜在空间数据同化框架，使用生成式深度学习模型捕捉复杂非线性海洋动力学，将观测数据有效同化到模型中。该方法能够生成"未见过的"非线性演化过程，显著提升海洋预报对极端事件和快速变化过程的捕捉能力。',
                'source': 'Ocean Modelling / ScienceDirect',
                'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000016',
                'date': '2026-02-01'
            },
            {
                'title': '2. JAMSTEC（2026）：2026年国际海洋数字孪生峰会（DITTO Summit）将于日本召开',
                'badge': '近7天',
                'abstract': '联合国海洋十年认可的数字孪生海洋计划（DITTO）将召开旗舰全球活动——2026年DITTO峰会。此次峰会将汇聚全球数字孪生海洋领域的科学家、工程师和政策制定者，探讨数字孪生技术在海洋观测、预测和可持续管理中的最新进展和应用前景，推动海洋数字孪生从研究走向业务化。',
                'source': 'JAMSTEC / UN Ocean Decade DITTO',
                'url': 'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/',
                'date': '2026-05-01'
            }
        ]
    },
    {
        'title': '三、可视化',
        'en': 'Visualization',
        'items': [
            {
                'title': '1. NASA SVS（2026-03-03）：海平面变化可视化——"透过舷窗看海平面"',
                'badge': '',
                'abstract': 'NASA科学可视化工作室发布创意可视化作品"Sea Level Through a Porthole"，通过圆形舷窗视角展示全球平均海平面的长期变化趋势。蓝色标记精确显示当前海平面高度，直观呈现海平面上升的累积效应。该可视化采用NASA海冰、云和陆地高程卫星（ICESat-2）等数据源。',
                'source': 'NASA Scientific Visualization Studio',
                'url': 'https://svs.gsfc.nasa.gov/5620',
                'date': '2026-03-03'
            },
            {
                'title': '2. EMODnet（2026-04-30）：EMODnet首次新增滨海旅游数据主题，拓展社会经济数据维度',
                'badge': '近7天',
                'abstract': '欧洲海洋观测与数据网络（EMODnet）自成立以来首次推出滨海旅游（Coastal Tourism）数据主题，标志着其从传统物理/生物海洋数据向社会经济数据领域拓展。滨海旅游是欧洲蓝色经济的重要支柱，新主题提供协调统一、高分辨率的沿海旅游活动数据，支持循证沿海管理决策。',
                'source': 'EMODnet',
                'url': 'https://emodnet.ec.europa.eu/en',
                'date': '2026-04-30'
            }
        ]
    },
    {
        'title': '四、数据质量',
        'en': 'Data Quality',
        'items': [
            {
                'title': '1. Journal of Oceanography（2026-04-29）：基于路径签名的Argo剖面自动质量控制方法改进',
                'badge': '近7天',
                'abstract': '日本JAMSTEC团队在Journal of Oceanography发表论文，改进了基于路径签名（path-signature）的Argo自动质量控制方法。新方法结合机器学习技术，使用2016年数据集训练的模型在2017至2021年间表现稳健，能够快速生成中等质量数据集，成功学习QC通用特征，准确率接近Argo数据中心水平。',
                'source': 'Journal of Oceanography / JAMSTEC',
                'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1',
                'date': '2026-04-29'
            },
            {
                'title': '2. GeoAquaWatch（2026-05）：Argo叶绿素-a数据将于6月起全面再处理',
                'badge': '近7天',
                'abstract': 'Bio-Geochemical Argo社区发布重要通知：自2026年6月起，Argo叶绿素-a数据将由数据汇编中心（DACs）使用新校正方法进行全面再处理和重新分发。新方法基于4D-BGC产品的实时调整，将显著改善荧光到叶绿素-a的转换精度。社区将于5月12日举办专题网络研讨会，主讲人为CNRS的Raphaelle Sauzedee。',
                'source': 'GeoAquaWatch / BGC-Argo',
                'url': 'https://www.geoaquawatch.org/important-update-for-argo-users-argo-chlorophyll-data-reprocessing-instructional-webinar-may-12th/',
                'date': '2026-05-01'
            },
            {
                'title': '3. LinkedIn（2026-04-29）：Bio-Geochemical Argo社区确认叶绿素计算方法更新',
                'badge': '近7天',
                'abstract': 'BGC-Argo官方LinkedIn账号发布重要更新公告，确认将从2026年6月开始重新处理和分发所有Argo叶绿素数据。此次更新解决了长期存在的荧光到叶绿素-a转换偏差问题，对使用BGC-Argo数据进行海洋生物地球化学研究的用户将产生广泛影响，建议所有相关用户关注。',
                'source': 'Bio-Geochemical Argo / LinkedIn',
                'url': 'https://www.linkedin.com/posts/biogeochemical-argo_important-chlorophyll-calculation-update-activity-7454806893761323008-PaDA',
                'date': '2026-04-29'
            }
        ]
    },
    {
        'title': '五、数据处理',
        'en': 'Data Processing',
        'items': [
            {
                'title': '1. IOCCG（2026-05）：NASA PACE任务多仪器数据重新处理启动',
                'badge': '近7天',
                'abstract': 'NASA PACE（浮游生物、气溶胶、云和海洋生态系统）卫星任务正在进行大规模数据重新处理。包括OCI Version 3.0.2 Level-1B和Level-1C数据、OCI Version 3.2 Level-2/3水生地球物理产品，以及HARP2和SPEXone Version 4.0全级别产品。此外，第6届PACE应用研讨会录像已存档，5月14日将举行实践社区季度电话会议。',
                'source': 'IOCCG / NASA',
                'url': 'https://ioccg.org/2026/05/may-2026/',
                'date': '2026-05-05'
            },
            {
                'title': '2. IOCCG（2026-05）：HyperInSPACE社区处理器HyperCP v1.2.15发布，引入全面不确定性预算',
                'badge': '近7天',
                'abstract': 'HyperCP（HyperInSPACE Community Processor）发布v1.2.15重大更新，核心亮点是引入了按仪器类别和传感器分类的不确定性预算系统。新版本还新增了绝对辐射校准表征、单次测量不确定性贡献分解报告、耀斑校正和BRDF校正功能，以及SolarTracker、pySAS、DALEC等自主观测平台的支持。对海洋光学遥感数据处理的标准化和精度提升具有重大意义。',
                'source': 'IOCCG / HyperInSPACE',
                'url': 'https://ioccg.org/2026/05/may-2026/',
                'date': '2026-05-05'
            },
            {
                'title': '3. CopernicusLAC（2026-05）：智利启动哥白尼沿海监测新平台，覆盖拉丁美洲和加勒比地区',
                'badge': '近7天',
                'abstract': 'CopernicusLAC智利节点推出全新沿海监测服务，为拉丁美洲和加勒比地区提供海岸和海洋系统连续分析。平台当前提供海表温度（SST）和叶绿素-a（Chl-a）两种关键变量，整合Sentinel-3、MODIS Aqua等多源卫星数据。数据可免费下载，支持NetCDF和ZARR格式，计划年内增加更多变量和高时间分辨率产品。',
                'source': 'CopernicusLAC Chile',
                'url': 'https://ioccg.org/2026/05/may-2026/',
                'date': '2026-05-05'
            }
        ]
    },
    {
        'title': '六、数据管理与共享',
        'en': 'Data Management & Sharing',
        'items': [
            {
                'title': '1. NOAA Ocean Explorer（2026-05-05）：NOAA发布首套深海环境DNA（eDNA）数据集',
                'badge': '近7天',
                'abstract': 'NOAA海洋探索办公室公开发布其首套深海环境DNA数据集，数据来自Okeanos Explorer号考察船2021至2023年在大西洋和太平洋的探险。eDNA样本通过ROV Deep Discoverer采集，经国家系统学实验室进行DNA扩增测序和AOML进行生物信息学分析。原始序列可通过NCBI BioProject获取，物种鉴定信息通过OBIS发布。NOAA将于5月28日举办专题研讨会。',
                'source': 'NOAA Ocean Explorer',
                'url': 'https://oceanexplorer.noaa.gov/news/from-seawater-to-sequences-exploring-noaas-new-deep-sea-environmental-dna-dataset/',
                'date': '2026-05-05'
            },
            {
                'title': '2. Seabed 2030（2026-04-20）：全球海底测绘达到新里程碑——28.7%海底已完成测绘',
                'badge': '近7天',
                'abstract': '日本财团-GEBCO Seabed 2030项目宣布全球海底测绘覆盖率已达28.7%，过去一年新增近500万平方公里数据。220个组织参与贡献，新增15个贡献者。区域亮点包括ROPME海域覆盖率从6.4%增长至20.5%。主要数据贡献来自NOAA-NCEI、PANGAEA、JAMSTEC、巴西海军水道测量局以及卫星测深数据。累计约1.04亿平方公里海底数据已整合至免费GEBCO网格。',
                'source': 'Seabed 2030 / The Nippon Foundation-GEBCO',
                'url': 'https://seabed2030.org/2026/04/20/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year/',
                'date': '2026-04-20'
            },
            {
                'title': '3. EMODnet Biology（2026-05-06）：EMODnet Biology数据下载新增物种缺失记录',
                'badge': '近7天',
                'abstract': 'EMODnet Biology改进了海洋生物多样性数据访问方式，允许用户在数据下载中包含分类单元的缺失记录（absence data）。这是生物多样性评估方法精细化的关键进展，缺失数据的引入能够显著降低物种分布模型的假阳性率，提升海洋生物多样性空间格局分析的准确性和可靠性。',
                'source': 'EMODnet Biology / VLIZ',
                'url': 'https://emodnet.ec.europa.eu/en',
                'date': '2026-05-06'
            }
        ]
    },
    {
        'title': '七、开放航次/船时共享',
        'en': 'Open Research Cruises / Ship-time Sharing',
        'items': [
            {
                'title': '1. 中科院海洋所（2026-05-06）：长心卡帕藻超大型藻株培育通过专家验收',
                'badge': '近7天',
                'abstract': '中国科学院海洋研究所藻类与藻类生物技术团队成功破解长心卡帕藻苗种供应瓶颈，培育出超大型藻株并通过专家验收。超大型藻株单株平均重达55.2斤，单茬鲜重净增270余倍，最重单株达71.6斤，为已知世界最大个体。长心卡帕藻是天然卡拉胶生产的基础原料，该突破为我国实现卡拉胶原料国产化供应、摆脱长期依赖进口局面带来希望。',
                'source': '科技日报 / 中科院海洋研究所',
                'url': 'https://finance.sina.com.cn/tech/discovery/2026-05-06/doc-inhwyqhc5689241.shtml',
                'date': '2026-05-06'
            },
            {
                'title': '2. EGU（2026-05）：Tillys Petit荣获EGU海洋科学2026年杰出早期职业科学家奖',
                'badge': '近7天',
                'abstract': '欧洲地球科学联合会（EGU）宣布Tillys Petit荣获2026年海洋科学分部杰出早期职业科学家奖。该奖项旨在表彰海洋科学领域做出卓越贡献的青年研究者。EGU 2026年度大会于5月3至8日在维也纳举行，Copernicus Marine Service在会上展示了AI增强海洋产品和欧洲海洋数字孪生（DTO）等最新成果。',
                'source': 'EGU / Copernicus Marine Service',
                'url': 'https://events.marine.copernicus.eu/egu-26',
                'date': '2026-05-05'
            }
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '1. Copernicus Marine Service（2026-05）：第9版哥白尼海洋状况报告（OSR 9）正式发布',
                'badge': '近7天',
                'abstract': '第9版哥白尼海洋状况报告揭示了破纪录的海洋极端事件、加速的变化趋势以及对海洋生态系统和社会日益增长的影响。报告重点关注2023和2024年极端事件，提供过去几十年海洋变化和变异的全面信息，并附有交互式摘要。OSR 9是全球海洋环境状况最权威的定期评估报告之一。',
                'source': 'Copernicus Marine Service',
                'url': 'https://marine.copernicus.eu/access-data/ocean-state-report/ocean-state-report-9',
                'date': '2026-05-03'
            },
            {
                'title': '2. NOAA NCEI（2026-04-30）：CORA沿海海洋再分析数据集在AWS开放数据注册中心上线',
                'badge': '近7天',
                'abstract': 'NOAA沿海海洋再分析（CORA）数据集在AWS开放数据注册中心上线，提供1979至2022年美国东海岸、墨西哥湾和加勒比海的建模历史水位和波浪数据。该数据集使用国家海洋服务局经验证的小时水位数据生成，由马里兰大学利用SCHISM模型计算。太平洋和夏威夷区域的再分析计划后续发布。',
                'source': 'NOAA NCEI / AWS Open Data',
                'url': 'https://registry.opendata.aws/noaa-nos-cora/',
                'date': '2026-04-30'
            },
            {
                'title': '3. PANGAEA（2026-05）：PANGAEA社区研讨会5月7-8日举行',
                'badge': '近7天',
                'abstract': 'PANGAEA地球与环境科学数据发布平台将于5月7至8日举行为期两天的社区研讨会，主题为"从PANGAEA发现和获取数据"。研讨会提供理论讲解与实践操作结合的课程，帮助参与者系统学习数据检索、利用和整合方法。PANGAEA作为全球最大的地球科学数据仓库之一，拥有数十万条已发布的研究数据集。',
                'source': 'PANGAEA / MARUM',
                'url': 'https://www.pangaea.de/',
                'date': '2026-05-07'
            }
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '1. GitHub（2026-01）：GOFLOW——基于深度学习的海洋表面流场预测框架开源',
                'badge': '',
                'abstract': 'GOFLOW（Geostationary Ocean Flow）代码库在GitHub正式开源，提供基于深度学习的海洋表面速度场预测完整实现。框架训练神经网络从卫星海表温度梯度观测推断海洋动力学特征，支持GOES和Himawari等静止卫星数据输入，对应Nature Geoscience论文方法。',
                'source': 'GitHub / KSR-Ocean',
                'url': 'https://github.com/ksr-ocean/goflow',
                'date': '2026-01-07'
            },
            {
                'title': '2. AGU Geophysical Research Letters（2026-04-13）：SWOT宽幅高度计数据推动全球海洋预测突破',
                'badge': '近7天',
                'abstract': '发表于AGU Geophysical Research Letters的研究系统评估了SWOT卫星KaRIn干涉仪对全球海洋预测的贡献。自2022年12月发射以来，SWOT提供的宽幅海面高度数据首次将亚中尺度海洋动力学纳入全球预报系统，显著提升了对中尺度涡旋、边界流和沿海动力过程的预测能力，标志海洋观测进入宽幅高度计时代。',
                'source': 'AGU Geophysical Research Letters',
                'url': 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025GL115016',
                'date': '2026-04-13'
            },
            {
                'title': '3. IOCCG（2026-05）：POGO-SCOR奖学金计划2026申请截止延长至5月13日',
                'badge': '近7天',
                'abstract': '国际海洋观测平台POGO与SCOR联合奖学金计划申请截止日期延长至2026年5月13日。优先资助领域包括：新兴低成本海洋观测技术、浮标和滑翔机传感器、漂浮物观测、开放和沿海海洋观测、数据管理与时间序列分析、声学观测等。面向发展中国家的早期职业科学家，提供1至3个月出国访问资助。',
                'source': 'IOCCG / POGO / SCOR',
                'url': 'https://ioccg.org/2026/05/may-2026/',
                'date': '2026-05-05'
            }
        ]
    }
]


def replace_sections_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find SECTIONS = [ position
    start_marker = 'SECTIONS = ['
    start_idx = content.index(start_marker)

    # Find the matching closing ] using bracket counting
    bracket_start = start_idx + len('SECTIONS = ') - 1  # position of '['
    depth = 0
    end_idx = bracket_start
    for i in range(bracket_start, len(content)):
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
            if depth == 0:
                end_idx = i
                break

    # Build new SECTIONS string
    new_sections_str = 'SECTIONS = ' + repr(NEW_SECTIONS)

    # Replace
    new_content = content[:start_idx] + new_sections_str + content[end_idx + 1:]

    # Verify
    try:
        compile(new_content, 'feishu_write_doc.py', 'exec')
        print("Syntax check PASSED")
    except SyntaxError as e:
        print(f"Syntax check FAILED: {e}")
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"SECTIONS replaced successfully. Total items: {sum(len(s['items']) for s in NEW_SECTIONS)}")
    return True


if __name__ == '__main__':
    replace_sections_in_file('feishu_write_doc.py')
