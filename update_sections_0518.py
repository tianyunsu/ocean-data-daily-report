#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-05-18 SECTIONS 数据更新脚本
"""
import re

NEW_SECTIONS = [
  {'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [
    {'title': 'Njord：首个概率性图神经网络海洋集成预报模型（arXiv, 2026-05-14）', 'badge': '近7天', 'abstract': '芬兰赫尔辛基大学团队提出Njord——首个用于海洋预报的概率数据驱动模型，突破现有ML海洋模型只能输出确定性预报的局限。Njord将深度潜变量框架与图神经网络架构结合，支持单次前向传播完成集成采样并量化不确定性。模型以0.25度分辨率应用于全球尺度，并以2km分辨率应用于波罗的海区域；引入K-means聚类网格适应不规则海面几何。在OceanBench全球基准上，上层海洋变量平均误差最低，SST预测改进最为显著。', 'source': 'arXiv', 'url': 'https://arxiv.org/abs/2605.15470', 'date': '2026-05-14'},
    {'title': 'CMEMS：人工智能如何驱动下一代业务化海洋产品（2026-05-04）', 'badge': '近7天', 'abstract': 'Copernicus海洋服务全面披露AI技术业务化进展：深度学习将北极海冰浓度预报误差降低41%；神经网络实现近实时全球海面风场偏差校正；ANN显著提升北大西洋极端风暴期间波浪预报精度；4DVarNet算法实现多传感器海表温度重建。成果依托COSI、KAILANI、CERAINE等项目，正逐步从研究走向业务化运行。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/how-artificial-intelligence-powering-next-generation-operational-marine-products', 'date': '2026-05-04'},
    {'title': '基于多气象因素与机器学习的南海SST短期与长期预测（Frontiers, 2026-05-13）', 'badge': '近7天', 'abstract': 'Frontiers in Marine Science发表研究，利用随机森林、XGBoost、LightGBM融合多气象变量对南海SST进行短期和长期预测，发现多元模型显著优于单一变量模型，随机森林表现最佳，总云量对长期SST预测贡献甚至超过盐度，有效预测期可达20个月以上。', 'source': 'Frontiers in Marine Science', 'url': 'https://www.frontiersin.org/articles/10.3389/fmars.2026.1820102/full', 'date': '2026-05-13'},
  ]},
  {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
    {'title': '厦门大学柴扉教授团队：海洋数字孪生赋能蓝色经济创新综述（2026-02-26）', 'badge': '1周~1个月', 'abstract': '厦门大学柴扉教授联合多国专家系统梳理海洋数字孪生核心架构（数据、模型，分析、可视化与交互四大模块），综述其在水产养殖、海上风电、可持续航运、海洋防灾减灾、蓝碳及海洋旅游等蓝色经济核心领域的全生命周期应用，指出海洋数字孪生正推动从被动式数据分析向主动式预测型决策支持的范式跃迁。', 'source': '厦门大学海洋与地球学院', 'url': 'https://mel.xmu.edu.cn/info/1012/61071.htm', 'date': '2026-02-26'},
    {'title': '《海洋通报》海岸带时空智能与数字孪生专栏征稿启事（2026-05-08）', 'badge': '近7天', 'abstract': '自然资源部主管，国家海洋信息中心与中国海洋学会主办的《海洋通报》发布专栏征稿启事，围绕海岸带多模态数据治理、物理与AI融合的海洋时空建模、海岸带灾害预测预报、数字孪生赋能海岸带治理等9大方向征稿，编辑部开辟绿色通道加快审稿流程。', 'source': '国家海洋信息中心 / 中国海洋学会', 'url': 'https://www.nmdis.org.cn/c/2026-05-08/85285.shtml', 'date': '2026-05-08'},
  ]},
  {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [
    {'title': '南加州海带森林连续海洋热浪群落变化研究（Comm E&E, 2026-05-16）', 'badge': '近7天', 'abstract': 'Communications Earth & Environment发表研究，结合温度数据与生态样带分析，揭示连续海洋热浪导致南加州海带森林群落组成发生显著变化——底层海带减少，亚热带和外来物种入侵。研究利用长期野外监测数据与卫星遥感可视化方法追踪海带森林动态，为气候变化下近岸海洋生态系统可视化监测提供方法范例。', 'source': 'Communications Earth & Environment / Nature', 'url': 'https://www.nature.com/articles/s43247-026-03599-5', 'date': '2026-05-16'},
    {'title': '美国东北陆架浮游植物温度敏感性主导净初级生产力季节变化（Comm E&E, 2026-05-16）', 'badge': '近7天', 'abstract': 'Communications Earth & Environment发表研究，综合现场观测数据与数值模型，发现美国东北陆架生态系统中热性状介导效应（温度对浮游植物生长速率的直接促进）强于营养盐效应。温升导致浮游植物生长速率提高，同时生物量下降，二者补偿作用使净初级生产力季节波动被显著抑制。该发现挑战传统认知，对气候变化下海洋碳汇评估具有重要意义。', 'source': 'Communications Earth & Environment / Nature', 'url': 'https://www.nature.com/articles/s43247-026-03611-y', 'date': '2026-05-16'},
  ]},
  {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [
    {'title': 'BGC-Argo+：含二次质量控制的全球生物地球化学Argo浮标数据集（ESSD预印本, 2026-05-12）', 'badge': '近7天', 'abstract': '夏威夷大学团队在ESSD发表预印本，对截至2025年1月的2429个BGC-Argo浮标数据进行了自动与人工结合的异常值检测（重点针对O2、硝酸盐和pH值），并提供剔除异常值后的统一剖面和网格化数据存储库，是当前最大规模的经二次QC的BGC-Argo数据集合。', 'source': 'Earth System Science Data / Copernicus', 'url': 'https://essd.copernicus.org/preprints/essd-2026-311/', 'date': '2026-05-12'},
    {'title': 'JAMSTEC团队：基于路径签名的Argo剖面自动QC方法改进（2026-04-29）', 'badge': '1周~1个月', 'abstract': 'JAMSTEC团队在Journal of Oceanography发表研究，改进基于路径签名的Argo自动质量控制方法并融入机器学习技术，使用2016年数据训练的模型在2017-2021年间表现稳健，能准确识别错误剖面并接近Argo数据中心水平，可快速生成中等质量数据集以填补实时数据发布与人工QC之间的时间空白。', 'source': 'Journal of Oceanography / Springer', 'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1', 'date': '2026-04-29'},
  ]},
  {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [
    {'title': 'GEOXYGEN：基于生物地球化学感知ML框架的全球长期溶解氧数据集（ESSD, 2026-05-12）', 'badge': '近7天', 'abstract': '复旦大学团队在ESSD发表GEOXYGEN数据集，利用分层建模框架融合物理和生物地球化学预测因子，生成1960-2024年、月均、0.5度x0.5度分辨率、覆盖0-5500m深度的全球溶解氧场，独立测试R2大于0.9，重建空间格局与World Ocean Atlas 2023气候态高度一致。', 'source': 'Earth System Science Data / 复旦大学', 'url': 'https://essd.copernicus.org/articles/18/3125/2026/', 'date': '2026-05-12'},
    {'title': 'Euro-Argo ERIC：Argo叶绿素数据将于2026年6月起全面重新处理和重新分发（2026-05-05）', 'badge': '近7天', 'abstract': 'Euro-Argo ERIC发布重要数据更新预告：自2026年6月起，BGC-Argo叶绿素数据将由数据汇集中心（DACs）采用新校正方法重新处理和重新分发，数据质量和精度将显著提升，但部分区域数据值可能出现明显变化。提醒依赖该数据进行学术发表或建模分析的用户注意数值变化。', 'source': 'Euro-Argo ERIC', 'url': 'https://www.linkedin.com/posts/euroargo_argofloats-oceanscience-activity-7455168522688761856-Bu9b', 'date': '2026-05-05'},
  ]},
  {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [
    {'title': 'Eos观点：失去美国海平面科学的全球影响（Eos/AGU, 2026-05-15）', 'badge': '近7天', 'abstract': '多位美国、荷兰、香港科学家在Eos（AGU）联名发表观点文章，分析美国气候科学经费大规模削减（NASA削减24%、NOAA削减27%、NSF削减57%）对全球海平面科研的影响。自1982年以来103项全球平均海平面预测研究中约1/3由美国机构主导，超2000个数据集已从联邦平台下架。文章呼吁多方采取行动保护全球海平面数据和科学基础设施。', 'source': 'Eos / AGU', 'url': 'https://eos.org/opinions/the-global-impact-of-losing-u-s-sea-level-science', 'date': '2026-05-15'},
    {'title': 'NOAA NCEI：史上最大规模云迁移FAQ发布——AWS迁移进展与用户问答（2026-05-12）', 'badge': '近7天', 'abstract': 'NOAA NCEI在宣布AWS云迁移后进一步发布详细FAQ，解答用户关于数据访问路径变化、迁移时间线、服务连续性和数据可用性的核心问题。NCEI每月归档超229TB数据，覆盖130以上观测平台。迁移完成后将实现数据按需访问，显著提升AI/ML场景下的数据利用效率。', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/cloud-migration-FAQ', 'date': '2026-05-12'},
  ]},
  {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
    {'title': 'NOAA：EX2603航次正式启动——Okeanos Explorer夏威夷海域ROV系统综合测试（2026-05-16）', 'badge': '近7天', 'abstract': 'NOAA Ocean Exploration宣布Okeanos Explorer号于2026年5月16日正式启动EX2603航次，在夏威夷海域执行ROV系统综合测试，对机械、电气和软件组件进行全面压力测试，为2026年勘探季做准备，持续至6月5日。此前EX2602（4月29日至5月6日）已完成测绘系统测试，E/V Nautilus 2026航季（6-10月）将探索中太平洋和西太平洋深海栖息地。', 'source': 'NOAA Ocean Exploration', 'url': 'https://oceanexplorer.noaa.gov/expeditions/', 'date': '2026-05-16'},
    {'title': '中科院深海所：全球深渊探索计划太平洋穿越航次圆满完成（2026-05-12）', 'badge': '近7天', 'abstract': '探索一号搭载奋斗者号完成156天、总航程超4万公里的太平洋穿越航次，6国83名队员参与，奋斗者号完成63个潜次（50次超6000米），首次发现南半球最深化能生态系统，采集大量生物地质标本，多个生物可能为新物种，入选联合国海洋十年行动计划。', 'source': '中国科学院深海科学与工程研究所', 'url': 'https://www.idsse.ac.cn/xwdt/ywdt/202605/t20260512_8200019.html', 'date': '2026-05-12'},
  ]},
  {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [
    {'title': 'Nature Communications：AMOC减弱驱动热带辐合带（ITCZ）向南迁移（2026-05-16）', 'badge': '近7天', 'abstract': 'NCAR团队在Nature Communications发表研究，揭示大西洋经向翻转环流（AMOC）的实质性减弱是近期热带辐合带（ITCZ）向南偏移的关键驱动力。研究发现仅约1/3的CMIP6模型能模拟出与观测一致的ITCZ南移。AMOC完全崩溃情景下，若无气候变暖基态ITCZ将被推入南半球；若有变暖基态则向赤道移动，深刻影响全球热带降水格局。', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-73200-2', 'date': '2026-05-16'},
    {'title': 'Nature Communications：地面沉降使人口密集海岸海平面上升速率翻倍（2026-05-16）', 'badge': '近7天', 'abstract': '利用整合GNSS、InSAR、潮位仪和卫星测高的高分辨率垂直陆地运动数据，研究表明71%的全球沿海人口居住在正在下沉的地区，1995-2020年沿海人口经历的平均海平面上升速率约为6mm/年，约为气候驱动绝对海平面上升速率的两倍。雅加达沉降速率最高达13.7mm/年（局部达42mm/年），天津达13.5mm/年。InSAR数据纳入后受沉降影响人口估算增加约10倍。', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72293-z', 'date': '2026-05-16'},
    {'title': 'Nature Communications（2026-05-11）：低云反馈在不可逆海平面上升中的关键作用', 'badge': '近7天', 'abstract': '首尔国立大学团队在Nature Communications发表研究，利用全耦合气候模型揭示：即使没有冰川融化，由于海洋内部巨大热惯性，海平面将在数个世纪内持续升高。关键机制是特定的海表温度升温模式通过低云反馈增强短波辐射吸收，从而维持海洋热量吸收和热膨胀。', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72898-4', 'date': '2026-05-11'},
    {'title': 'NOAA NCEI：ADT-HURSAT飓风分析数据集更新扩展至2024年（2026-05-13）', 'badge': '近7天', 'abstract': 'NCEI联合威斯康星大学麦迪逊分校/CIMSS发布更新版ADT-HURSAT数据集，将HURSAT数据扩展至2024年，提供自1978年以来跨时间和地理的标准化风暴强度信息，支持长期历史分析和行业风险评估。NCEI同步发布配套Python Jupyter Notebook教程，用户可在Google Colab直接运行进行数据探索。', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/noaa-releases-updated-dataset-hurricane-analysis', 'date': '2026-05-13'},
  ]},
  {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [
    {'title': 'Copernicus Marine Toolbox v2.4.1发布——修复气候数据集子集访问Bug（2026-05-11）', 'badge': '近7天', 'abstract': 'Copernicus Marine Toolbox发布v2.4.1版本，修复了访问气候数据集（climatology datasets）时subset命令失败的问题（原因为Toolbox错误地将新维度nv识别为时间轴）。此前v2.4.0引入了重要更新：Python最低版本提升至3.10、支持在数据集ID中直接指定版本、新增NetCDF稀疏数据集子集支持、新增CSV密集数据集子集支持、支持pandas>=3.0.0。工具箱支持CLI、Python API及Web界面访问CMEMS数据，无配额限制。', 'source': 'Copernicus Marine Service / PyPI', 'url': 'https://pypi.org/project/copernicusmarine/', 'date': '2026-05-11'},
    {'title': 'OSGeo（2026-05-08）：GDAL 3.13.0 Iowa City发布——新增Zarr V3、COG写入、SAR CPHD驱动等', 'badge': '近7天', 'abstract': '开源地理空间数据抽象库GDAL发布3.13.0版本（代号Iowa City），新增10余个gdal CLI子命令；Zarr V3支持显著增强（sharding、multiscales、空间扩展）；新增COG随机写入、E57 2D影像读取、SAR CPHD多维数据读取等驱动；S102/S104/S111新增写入能力；INTERLIS 2.4格式支持。', 'source': 'OSGeo / GitHub', 'url': 'https://github.com/OSGeo/gdal/releases', 'date': '2026-05-08'},
    {'title': 'IOOS（2026-05-07）：5月简报——J-SCOPE数据上线AWS、HF雷达历史数据归档至NCEI', 'badge': '近7天', 'abstract': '美国IOOS发布5月简报：JISAO季节性海岸生态预报数据（J-SCOPE，6-9个月预见期）正式上线AWS开放数据注册表；NCEI与Scripps CORDC合作完成IOOS HF雷达项目全历史数据归档；华盛顿州Kalaloch新HF雷达站投入运行；CeNCOOS新增两处WebCOOS海岸摄像头。', 'source': 'US IOOS / NOAA', 'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-may-2026/', 'date': '2026-05-07'},
  ]},
]

def replace_sections(filepath, new_sections):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.index('SECTIONS = [')
    depth = 0
    end_idx = start_idx
    for i, ch in enumerate(content[start_idx:]):
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                end_idx = start_idx + i + 1
                break

    # 构建新SECTIONS字符串
    import pprint
    new_sections_str = 'SECTIONS = ' + pprint.pformat(new_sections, width=200, sort_dicts=False)

    new_content = content[:start_idx] + new_sections_str + content[end_idx:]

    # 验证
    try:
        compile(new_content, filepath, 'exec')
        print('语法验证通过')
    except SyntaxError as e:
        print(f'语法错误: {e}')
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'文件已更新: {filepath}')
    return True

if __name__ == '__main__':
    replace_sections('feishu_write_doc.py', NEW_SECTIONS)
