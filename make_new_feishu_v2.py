#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
替换 feishu_write_doc.py 中的 SECTIONS 数据（修正后版本）
使用 bracket-counting 方法精准定位
"""

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': 'Njord：首个概率性图神经网络海洋集成预报模型（arXiv, 2026-05-14）',
                'badge': '近7天',
                'abstract': '芬兰赫尔辛基大学团队提出Njord——首个用于海洋预报的概率数据驱动模型，突破现有ML海洋模型只能输出确定性预报的局限。Njord将深度潜变量框架与图神经网络架构结合，支持单次前向传播完成集成采样并量化不确定性。模型以0.25度分辨率应用于全球尺度，并以2km分辨率应用于波罗的海区域；引入K-means聚类网格适应不规则海面几何。在OceanBench全球基准上，上层海洋变量平均误差最低，SST预测改进最为显著。',
                'source': 'arXiv',
                'url': 'https://arxiv.org/abs/2605.15470',
                'date': '2026-05-14',
            },
            {
                'title': 'ECMWF：IFS 50r1与AIFS v2正式上线——首次AI驱动波浪预报（2026-05-12）',
                'badge': '近7天',
                'abstract': 'ECMWF于2026年5月12日同步上线IFS Cycle 50r1与AIFS v2两大重要升级。IFS 50r1引入全耦合大气-海洋-海冰数据同化和新NEMO4-SI³海洋-海冰模型，新增40余个海洋与海冰变量，改进波浪与海流相互作用表征。AIFS v2则实现ECMWF史上首次AI驱动波浪预报，新增11个波浪变量，中期预报技巧相比IFS物理模型有显著提升，同时增加首套AI驱动积雪覆盖预报产品。',
                'source': 'ECMWF',
                'url': 'https://www.ecmwf.int/en/about/media-centre/news/2026/ifs-cycle-50r1-aifsv2-live',
                'date': '2026-05-12',
            },
            {
                'title': 'STC：基于Swin-Transformer的全球深度学习海洋预报区域后处理校正模型（Frontiers, 2026-05-13）',
                'badge': '近7天',
                'abstract': 'Frontiers in Marine Science发表论文，提出Swin-Transformer Corrector（STC）——一种专用于深度学习全球海洋预报系统（GOFS）的轻量级区域后处理校正模型。STC以层次化Swin Transformer为骨干，通过残差校正捕获多尺度空间误差结构，应用于南海区域多变量联合校正，RMSE平均降低20.35%，在热带气旋"海葵"等极端场景下亦表现出强鲁棒性，为"全球预报+区域轻量校正"范式提供了验证范例。',
                'source': 'Frontiers in Marine Science',
                'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1826293/full',
                'date': '2026-05-13',
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': 'DITTO国际数字孪生海洋峰会2026将于横滨召开（2026年11月）',
                'badge': '1周~1个月',
                'abstract': '联合国海洋十年认可项目DITTO（Digital Twins of the Ocean）宣布，第三届国际数字孪生海洋峰会将于2026年11月11-13日在日本横滨举行，主办方为JAMSTEC、GEOMAR等机构。峰会聚焦共享框架、互操作性、假设情景推演能力及海洋保护、治理与蓝色经济实际应用，继伦敦（2022）和厦门（2023）峰会之后，推动全球海洋数字孪生生态系统走向融合。',
                'source': 'JAMSTEC / DITTO',
                'url': 'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/',
                'date': '2026-05-12',
            },
            {
                'title': 'National Science Review：海洋数字孪生赋能蓝色经济创新综述（NSR, 2026-01-20）',
                'badge': '1周~1个月',
                'abstract': '厦门大学柴扉教授联合多国专家在National Science Review发表综述，系统梳理海洋数字孪生核心架构（数据、模型、分析、可视化与交互四大模块），综述其在水产养殖、海上风电、可持续航运、海洋防灾减灾、蓝碳及海洋旅游等蓝色经济核心领域的全生命周期应用，指出海洋数字孪生正推动从被动式数据分析向主动式预测型决策支持的范式跃迁。',
                'source': 'National Science Review / Oxford Academic',
                'url': 'https://academic.oup.com/nsr/article/13/3/nwag012/8431396',
                'date': '2026-01-20',
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization',
        'items': [
            {
                'title': 'CopernicusLAC Chile：面向拉丁美洲和加勒比的海岸监测可视化平台（2026）',
                'badge': '近7天',
                'abstract': 'CopernicusLAC Chile是位于圣地亚哥的哥白尼计划拉美区域中心，基于Sentinel-3、MetOp-B/-C、NOAA-20/SNPP、MODIS Aqua等多源卫星数据，提供SST和叶绿素a等海洋关键变量的连续监测与可视化服务。平台涵盖海岸监测、土地利用、城市地图和Sentinel影像存档四大模块，是欧盟哥白尼计划在拉美地区的数据处理、分发与应用推广核心枢纽。',
                'source': 'CopernicusLAC Chile / EU / Universidad de Chile',
                'url': 'https://www.copernicuslac-chile.eu/',
                'date': '2026',
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / QA/QC',
        'items': [
            {
                'title': '玄武深海Argo浮标数字孪生模型更新与异常检测应用（IET, 2026-03-17）',
                'badge': '1周~1个月',
                'abstract': '研究以中国自主研发并获国际Argo计划认证的"玄武"深海Argo浮标为案例，构建数字孪生模型更新框架，演示其在浮标异常检测中的典型应用，涵盖传感器故障识别、剖面质量评估等场景，为基于数字孪生的Argo数据实时质控提供了新路径。',
                'source': 'IET / The Institution of Engineering and Technology',
                'url': 'https://digital-library.theiet.org/doi/pdf/10.1049/icp.2026.0496',
                'date': '2026-03-17',
            },
            {
                'title': '改进基于路径签名的Argo剖面自动质控方法：融合机器学习实现快速中质量数据集生成（J. Oceanogr., 2026-04-29）',
                'badge': '近7天',
                'abstract': 'JAMSTEC团队在Journal of Oceanography发表论文，在前期路径签名（path-signature）Argo自动质控方法基础上引入新型机器学习模型，用于快速生成中质量Argo数据集。以2016年和2022年数据训练的模型在2017-2021年验证期间表现一致且稳健，表明该方法成功学习了QC的一般性特征，判别精度与Argo数据中心人工QC相当，为近实时Argo数据质控提供了高效替代方案。',
                'source': 'Journal of Oceanography / Springer',
                'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1',
                'date': '2026-04-29',
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '北太平洋历史营养盐数据集（1895-2024）：基于机器学习与水文观测重建（ESSD, 2026-04-28）',
                'badge': '近7天',
                'abstract': 'Earth System Science Data发表论文，从WOD和CCHDO获取北太平洋水文和营养盐（NO₃⁻、NO₂⁻、DIP、Si(OH)₄）观测数据，建立严格的四层QC流程清洗数据后，以高质量CCHDO数据集训练随机森林、LightGBM和高斯过程回归三种机器学习模型，利用经纬度、深度、时间和水团属性（位温、盐度）重建营养盐浓度。最终产出约4.73亿个重建数据点，覆盖192万站次、35744航次，相比原始营养盐观测增加2127-2393倍，数据在Zenodo开放获取。',
                'source': 'Earth System Science Data / Copernicus',
                'url': 'https://essd.copernicus.org/articles/18/2951/2026/essd-18-2951-2026.html',
                'date': '2026-04-28',
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'title': 'Eos观点：失去美国海平面科学的全球影响（Eos/AGU, 2026-05-15）',
                'badge': '近7天',
                'abstract': '多位美国、荷兰、香港科学家在Eos（AGU）联名发表观点文章，分析美国气候科学经费大规模削减（NASA削减24%、NOAA削减27%、NSF削减57%）对全球海平面科研的影响。自1982年以来103项全球平均海平面预测研究中约1/3由美国机构主导，超2000个数据集已从联邦平台下架。文章呼吁多方采取行动保护全球海平面数据和科学基础设施。',
                'source': 'Eos / AGU',
                'url': 'https://eos.org/opinions/the-global-impact-of-losing-u-s-sea-level-science',
                'date': '2026-05-15',
            },
            {
                'title': 'NOAA NCEI：史上最大规模云迁移FAQ发布——AWS迁移进展与用户问答（2026-05-12）',
                'badge': '近7天',
                'abstract': 'NOAA NCEI发布云迁移FAQ，详解将海量气候和海洋数据迁移至AWS的进展、用户访问路径变化及数据连续性保障措施，被称为NOAA史上最大规模的数据基础设施转型。FAQ涵盖数据集覆盖范围、访问工具适配、迁移时间表及用户反馈渠道，是国际海洋数据基础设施云化的重要参考案例。',
                'source': 'NOAA NCEI',
                'url': 'https://www.ncei.noaa.gov/news/cloud-migration-FAQ',
                'date': '2026-05-12',
            },
            {
                'title': 'PANGAEA社区工作坊2026年5月：数据发现与检索实践培训（2026-05-07/08）',
                'badge': '近7天',
                'abstract': 'PANGAEA（地球与环境数据发布平台）举办为期两天的社区工作坊（每天2小时在线），主题为"从PANGAEA发现与检索数据"，聚焦FAIR²和可持续研究数据管理原则，涵盖系统性数据搜索、利用和集成，以及针对海洋科学领域数据集的实操练习。该系列工作坊为用户导向培训，旨在提升全球海洋与环境科学家的数据素养。',
                'source': 'PANGAEA / de.NBI / TESS Hub',
                'url': 'https://tesshub.org/events/pangaea-community-workshop-may-2026-finding-and-retrieving-data-from-pangaea',
                'date': '2026-05-07',
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '"深蓝百万里"2026西太平洋航次圆满收官——首次在深圳设立"深海共享"数据节点（2026-05-11）',
                'badge': '近7天',
                'abstract': '"深蓝百万里"十年计划2026西太平洋航次由"向阳红10"号科考船承担，历时45天圆满完成，科考队于5月11日返回深圳。本航次为联合国"海洋十年"贡献项目，由南方科技大学海洋高等研究院等联合实施，调查了西太平洋关键海洋-大气过程，首次在深圳设立"深海共享"数据节点，推动科考数据向全球开放共享。',
                'source': '南方科技大学海洋高等研究院',
                'url': 'https://newshub.sustech.edu.cn/html/202605/47565.html',
                'date': '2026-05-11',
            },
            {
                'title': 'Schmidt Ocean Institute 2026年科考计划——从巴西深水到中大西洋海山（2026-02-22）',
                'badge': '1周~1个月',
                'abstract': 'Schmidt Ocean Institute发布2026年科考计划，国际团队将在巴西深水、中大西洋洋中脊海山开展生物多样性调查、物理化学与地质现象研究及海底测绘，继续推动开放数据政策，所有数据和样品通过在线数据库向全球科学界开放共享，体现国际开放航次共享理念标杆。',
                'source': 'Schmidt Ocean Institute',
                'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/',
                'date': '2026-02-22',
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': 'Seabed 2030：全球海底测绘达28.7%里程碑——年增近500万平方公里（IHO, 2026-04-28）',
                'badge': '1周~1个月',
                'abstract': 'Nippon Foundation-GEBCO Seabed 2030项目于2026年4月28日宣布，全球海底已完成测绘面积达28.7%，约1.04亿平方公里，过去一年新增约500万平方公里——相当于超过地球陆地面积三分之二的海底数据已实现覆盖。这一里程碑标志着实现2030年百分之百测绘目标的持续进展。',
                'source': 'IHO / Seabed 2030 / Nippon Foundation-GEBCO',
                'url': 'https://iho.int/en/global-seabed-mapping-reaches-new-milestone-as-five-million-square-kilometres-added-in-a-year',
                'date': '2026-04-28',
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': 'pyTMD v3.0.7发布——Python潮汐预测工具文档与功能更新（2026-05-07）',
                'badge': '近7天',
                'abstract': 'pyTMD（Python-based tidal prediction software）发布v3.0.7版本，新增计算潮高潮低峰值函数、pint友好单位转换、URL类S3存储桶访问支持及lineage属性记录模型文件名，改进xarray点积计算成分相位，规范化文档和PEP-0639许可证格式。支持OTIS、ATLAS、GOT、FES等主流潮汐模型，广泛用于卫星测高数据处理与潮汐校正。',
                'source': 'GitHub',
                'url': 'https://github.com/pyTMD/pyTMD/releases/tag/3.0.7',
                'date': '2026-05-07',
            },
            {
                'title': 'Copernicus Marine Toolbox v2.4.1发布——修复气候态数据集子集提取缺陷（2026-05-11）',
                'badge': '近7天',
                'abstract': '哥白尼海洋数据服务发布Copernicus Marine Toolbox v2.4.1补丁版本，修复了使用subset命令访问气候态（climatology）数据集时失败的关键缺陷：Toolbox此前会错误地将nv维度识别为时间轴，导致子集操作失败。该修复确保Toolbox正确识别和使用原始时间轴进行数据提取，适用于通过Python API和命令行接口的所有数据访问场景。',
                'source': 'Copernicus Marine Service',
                'url': 'https://help.marine.copernicus.eu/en/articles/8218641-next-milestones-and-roadmap',
                'date': '2026-05-11',
            },
            {
                'title': 'Gribstream：ECMWF IFS 50r1/AIFS v2用户迁移指南——GRIB2流参数变更说明（2026-04-02）',
                'badge': '1周~1个月',
                'abstract': 'Gribstream发布ECMWF IFS Cycle 50r1与AIFS v2切换技术说明，详细列出2026年5月12日起生效的模型、数据流、波浪和层次参数变更，包括新增NEMO4海洋变量、40余海冰变量和11个AI波浪变量的GRIB键值和访问方式，帮助API用户无缝适配系统升级。',
                'source': 'Gribstream / ECMWF',
                'url': 'https://gribstream.com/blog/ecmwf-ifs-cycle-50r1-aifs-v2-may-12-2026',
                'date': '2026-04-02',
            },
        ]
    },
]

import ast

with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# find SECTIONS
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

# Validate
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

# Verify section counts
import ast as ast2
sections = ast2.literal_eval(new_sections_str)
total = 0
for s in sections:
    n = len(s['items'])
    total += n
    print(f"  {s['title']}: {n} 条")
print(f"Total: {total} 条")
