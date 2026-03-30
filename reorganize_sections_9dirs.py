#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新组织SECTIONS,从7个方向扩展为9个方向
增加:海洋数据中心 和 工具与代码资源
"""

from datetime import datetime, timedelta

# 原始7个方向的数据
ORIGINAL_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. 中科院海洋所发布AI赋能海洋卫星遥感综述:聚焦参数反演、数据重建与现象识别',
                'badge': '[新发]',
                'abstract': '2026年3月27日，中国科学院海洋研究所人工智能海洋学研究组联合中国海洋大学、福州大学、深圳大学等单位，在《IEEE会刊》发表最新综述，系统总结了人工智能在海洋卫星遥感中的关键进展及未来发展方向。该综述聚焦海洋参数反演、数据重建和现象识别三大方向，指出AI在提升遥感信息提取能力、增强复杂场景鲁棒性方面的潜力，同时分析了当前在可重复性、迁移性及业务应用中的短板，提出了未来重点发展方向，如精细尺度融合重构、物理约束与AI融合、基础模型构建等。相关论文DOI: https://doi.org/10.1109/JPROC.2026.3664121',
                'source': '科学网 / IEEE Proceedings',
                'date': '2026-03-27',
                'url': 'https://news.sciencenet.cn/htmlnews/2026/3/562156.shtm'
            },
            {
                'title': '2. MDPI JMSE推出AI海洋应用专刊:征集海洋科学与AI交叉研究',
                'badge': '[专刊]',
                'abstract': 'MDPI Journal of Marine Science and Engineering（JMSE）近日宣布推出最新专刊"Artificial Intelligence and Its Application in Ocean Science"，征集人工智能在海洋科学领域应用的研究论文。该专刊涵盖机器学习、深度学习在海洋预报、海洋观测、海洋生态系统管理等方向的创新应用，旨在推动AI技术与海洋科学的深度融合，为海洋研究提供新的方法论支撑。',
                'source': 'MDPI JMSE',
                'date': '2026-03(征稿中)',
                'url': 'https://www.mdpi.com/journal/jmse/special_issues/71OWD8421S'
            },
            {
                'title': '3. 2026中关村论坛:AI驱动海洋治理成果丰硕',
                'badge': '[动态]',
                'abstract': '2026中关村论坛年会上，中国海洋治理领域成果丰硕，展现了AI技术在海洋科学研究中的应用进展。2026年是我国"十五五"开局之年，亦处于联合国"海洋十年"全面推进的关键时期。中国将立足全球海洋治理的科技需求，坚持以科技创新引领海洋经济高质量发展。AI在海洋领域的应用正从单点突破走向体系化，为海洋预报、海洋生态监测、海洋资源开发等提供全方位支撑。',
                'source': '网易新闻 / 中关村论坛',
                'date': '2026-03-27',
                'url': 'https://www.163.com/dy/article/KP1H9C3705568W0A.html'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '1. EDITO2(2025-2028):欧洲数字孪生海洋平台正式进入第二阶段',
                'badge': '[项目]',
                'abstract': '欧洲数字孪生海洋（EDITO）平台在完成初始孵化阶段后，以1400万欧元投入正式启动 EDITO2 第二期项目（2025-2028），由 Mercator Ocean International 和比利时海洋研究所（VLIZ）联合领衔。EDITO 作为欧洲数字孪生海洋的核心基础设施平台，整合国家数字孪生和欧洲研究项目，承载着 EU 使命"恢复我们的海洋和水域"。EDITO2 将深化技术能力，扩大社区规模，推动开放协作。',
                'source': 'VLIZ / EDITO.eu / Mercator Ocean',
                'date': '2025-2026进行中',
                'url': 'https://www.edito.eu/'
            },
            {
                'title': '2. Mercator Ocean:EDITO 平台持续对外开放，汇聚欧洲海洋数据资产与数字孪生工具',
                'badge': '[平台]',
                'abstract': 'Mercator Ocean International 维护的欧洲数字孪生海洋平台持续向研究人员、政策制定者、企业和公民开放，整合欧洲海洋数字资产，包括各国国家数字孪生和欧洲研究项目成果，形成统一的业务化社区驱动系统。作为 EU 使命海洋恢复战略的技术支柱，用户可通过该平台访问尖端数字孪生开发工具，做出科学决策并最大化研究影响。',
                'source': 'Mercator Ocean International',
                'date': '2026持续运营',
                'url': 'https://www.mercator-ocean.eu/en/digital-twin-ocean/'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '1. Copernicus Marine可视化工具更新:1天前更新，支持多维度海洋数据探索',
                'badge': '[新功能]',
                'abstract': 'Copernicus Marine Service 可视化工具于1天前（2026年3月29日）完成最新更新，提供交互式海洋数据探索功能。用户可通过地图、时序图、剖面图等多种形式探索海洋状况，支持跨时间、空间、深度和变量维度的数据可视化。MyOcean Viewer 提供 ENSO 厄尔尼诺事件等专题仪表板，是海洋数据可视化的重要免费工具。',
                'source': 'Copernicus Marine Service',
                'date': '2026-03-29(更新)',
                'url': 'https://marine.copernicus.eu/access-data/ocean-visualisation-tools'
            },
            {
                'title': '2. NASA海平面预测工具:IPCC AR6海平面预测可视化平台',
                'badge': '[工具]',
                'abstract': 'NASA 海平面预测工具（Sea Level Projection Tool）允许用户可视化和下载IPCC第六次评估报告（AR6）的海平面预测数据。该工具提供全球沿海地区过去、现在和未来海平面上升的交互式地图，用户可点击海洋中任意一点获取该位置的海平面预测，了解不同物理过程对未来海平面上升的贡献。',
                'source': 'NASA / Climate.gov',
                'date': '2026持续更新',
                'url': 'https://sealevel.nasa.gov/ipcc-ar6-sea-level-projection-tool'
            },
            {
                'title': '3. World Ocean Observatory可视化剧场:4天前更新，现代化海洋数据可视化展示',
                'badge': '[工具]',
                'abstract': 'World Ocean Observatory 的可视化剧场（Visualization Theater）于4天前（2026年3月26日）完成更新，展示关于世界海洋、水道、供水、气候和天气的现代数据可视化。该平台通过创新的可视化方式，将复杂的海洋数据转化为直观易懂的展示，服务于公众海洋教育和科学传播。',
                'source': 'World Ocean Observatory',
                'date': '2026-03-26(更新)',
                'url': 'https://www.worldoceanobservatory.org/visualization-theater'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / Marine Data Quality Control',
        'items': [
            {
                'title': '1. QARTOD实时海洋数据质控手册更新:2026年3月最新引用',
                'badge': '[标准]',
                'abstract': '美国综合海洋观测系统（IOOS）QARTOD 项目的实时海洋学数据质量保障/质量控制手册，于2026年3月19日在 OceanBestPractices 知识库中获得最新引用记录。QARTOD 是2003年启动的实时数据质控规范体系，现已成为众多海洋观测站网的认证要求，涵盖温度盐度、海流、波浪、海平面等多要素实时数据的自动质控算法规范。',
                'source': 'OceanBestPractices / NOAA IOOS',
                'date': '2026-03-19(最新引用)',
                'url': 'https://ioos.noaa.gov/project/qartod/'
            },
            {
                'title': '2. IODE QA/QC培训课程:2026年2月开放，海洋数据质量保障系统培训',
                'badge': '[培训]',
                'abstract': 'UNESCO IOC IOCARIBE 于2026年2月26日发布通知，开放"海洋十年数据质量保障与质量控制（QA/QC）"培训课程。该课程为期10天（2026年2月26日-3月7日），提供海洋数据质量保证和质量控制的入门级知识，涵盖数据质量评估、异常检测、数据验证等核心内容，面向全球海洋数据管理从业者开放。',
                'source': 'IOC-UNESCO / IOCARIBE',
                'date': '2026-02-26',
                'url': 'https://iocaribe.ioc-unesco.org/en/event/3037'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Marine Data Processing',
        'items': [
            {
                'title': '1. xoa 2026.2.1发布:基于xarray的海洋分析库，3天前更新',
                'badge': '[新发]',
                'abstract': 'xoa（xarray-based ocean analysis library）于2026年3月3日发布 2026.2.1 版本，这是一个专门为海洋数据分析设计的 Python 库，基于 xarray 构建。xoa 支持读取和处理观测和模拟海洋数据，提供海洋学特定的数据处理功能，包括剖面分析、深度插值、温盐图绘制等实用工具。',
                'source': 'xoa.readthedocs.io / PyPI',
                'date': '2026-03-03',
                'url': 'https://xoa.readthedocs.io/'
            },
            {
                'title': '2. xarray 2026.2.0正式发布:多维海洋数据处理核心库',
                'badge': '[发布]',
                'abstract': 'xarray 于2026年2月16日发布 2026.2.0 版本，这是科学计算中最重要的多维标注数组处理 Python 库之一，广泛用于 NetCDF 格式海洋气候数据的读取、处理和分析。最新版本在 NaN 跳过聚合、滚动窗口计算、云存储直接读取等方面持续优化，配合 Dask 可实现海量海洋数据集的并行云端处理。',
                'source': 'xarray.dev / GitHub / PyPI',
                'date': '2026-02-16',
                'url': 'https://docs.xarray.dev/en/stable/index.html'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. IODE国际海洋数据信息交换:2天前更新，全球100+国家海洋数据中心网络',
                'badge': '[平台]',
                'abstract': 'UNESCO IOC 国际海洋数据信息交换（IODE）项目官网于2天前（2026年3月28日）完成最新更新，协调着全球100多个国家海洋数据中心（NODC）及关联数据单元（ADU）的数据交换网络，覆盖物理海洋、海洋化学、海洋生物、海洋地质等多学科数据。IODE 持续推进全球海洋数据互操作和开放共享，是全球海洋数据基础设施的核心治理节点。',
                'source': 'IODE / IOC-UNESCO',
                'date': '2026-03-28(更新)',
                'url': 'https://iode.org/'
            },
            {
                'title': '2. Copernicus Marine Service:2天前持续更新，全球海洋数据产品服务',
                'badge': '[服务]',
                'abstract': 'Copernicus Marine Service 官网于2天前（2026年3月28日）完成最新更新，持续提供覆盖物理、生物地球化学、海冰等要素的全球和区域海洋数据产品，包括实时观测、预报模型输出和再分析数据集。数据完全免费开放，支持科学研究、政策制定和商业应用。',
                'source': 'Copernicus Marine / Copernicus.eu',
                'date': '2026-03-28(更新)',
                'url': 'https://marine.copernicus.eu/'
            },
            {
                'title': '3. SeaDataNet欧洲海洋研究数据共享:持续推进泛欧数据互联',
                'badge': '[平台]',
                'abstract': 'SeaDataNet 作为欧洲海洋研究基础设施，通过 SeaDataCloud、SeaDataNet2 等欧盟项目持续推进泛欧海洋数据互操作与共享。平台整合欧洲各国海洋研究机构的历史和实时观测数据，提供统一元数据目录、标准化数据格式和共享 API，在海洋地质样品库、水文观测档案、生物多样性数据共享方面发挥关键作用。',
                'source': 'SeaDataNet',
                'date': '2026持续运营',
                'url': 'https://www.seadatanet.org/'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. One Ocean Expedition 2025-2026:挪威深海考察船环球航行',
                'badge': '[航次]',
                'abstract': 'One Ocean Expedition 2025-2026是挪威深海考察船Statsraad Lehmkuhl执行的12个月环球航行，致力于分享海洋在可持续未来中作用的知识。该航次作为开放航次的国际实践案例，为海洋教育和科学传播提供了独特平台，展示了开放航次模式在全球海洋意识提升中的应用价值。',
                'source': 'One Ocean Expedition',
                'date': '2025-2026进行中',
                'url': 'https://www.oneoceanexpedition.com/'
            },
            {
                'title': '2. 国家自然科学基金委2027年度共享航次计划征集启动',
                'badge': '[政策]',
                'abstract': '国家自然科学基金委员会发布通知，启动2027年度共享航次计划考察需求征集。共享航次计划用于资助海洋科学考察船和潜水器，为需要进行海洋和极地科学考察的国家自然科学基金资助项目提供稳定、可靠的调查设施保障，促进海洋科学数据共享。',
                'source': '国家自然科学基金委 NSFC',
                'date': '2026-03(征集启动)',
                'url': 'https://www.nsfc.gov.cn/p1/3381/2824/94025.html'
            },
        ]
    }
]

# 新增的海洋数据中心方向
NEW_OCEAN_DATACENTER = {
    'title': '八、海洋数据中心',
    'en': 'Ocean Data Centers / Marine Data Centers',
    'items': [
        {
            'title': '1. 中科院海洋研究所数据中心:持续更新海洋科学数据资源',
            'badge': '[数据中心]',
            'abstract': '中国科学院海洋研究所数据中心作为中国重要的海洋科学数据汇聚节点，持续收集、整理和共享海洋观测数据、标本数据和研究成果数据。中心提供数据下载、数据可视化、数据管理等服务，支持海洋科学研究、海洋资源开发和海洋环境监测等多领域应用。',
            'source': '中科院海洋研究所',
            'date': '2026持续运营',
            'url': 'http://www.qdio.ac.cn/datacenter/'
        },
        {
            'title': '2. 国家海洋科学数据中心:整合全国海洋数据资源',
            'badge': '[数据中心]',
            'abstract': '国家海洋科学数据中心整合全国海洋数据资源，提供海洋环境、海洋资源、海洋生态等领域的综合数据服务。中心通过数据共享平台，为科研机构、政府部门和企业提供数据查询、数据下载和数据定制服务，推动海洋数据开放共享和应用创新。',
            'source': '国家海洋科学数据中心',
            'date': '2026持续运营',
            'url': 'http://www.nmdis.org.cn/'
        },
        {
            'title': '3. NOAA National Centers for Environmental Information:海洋数据存储与访问',
            'badge': '[数据中心]',
            'abstract': 'NOAA国家环境信息中心（NCEI）提供全球海洋数据存储和访问服务，包括海洋观测、海洋气候、海洋地质等多类型数据。NCEI 是美国海洋数据的重要数据中心，为全球用户提供数据下载、数据服务和数据咨询，支持海洋科学研究和海洋管理决策。',
            'source': 'NOAA NCEI',
            'date': '2026持续运营',
            'url': 'https://www.ncei.noaa.gov/products/ocean-data'
        },
    ]
}

# 新增的工具与代码资源方向
NEW_TOOLS_AND_CODE = {
    'title': '九、工具与代码资源',
    'en': 'Tools & Code Resources / Ocean Tools & Software',
    'items': [
        {
            'title': '1. xarray海洋数据处理工具:多维数组处理核心库',
            'badge': '[Python库]',
            'abstract': 'xarray是科学计算中最重要的多维标注数组处理Python库之一，广泛用于NetCDF格式海洋气候数据的读取、处理和分析。xarray提供维度标注、坐标系统、分组运算等高级功能，配合Dask可实现海量海洋数据集的并行云端处理，是海洋数据处理的必备工具。',
            'source': 'xarray.dev / GitHub / PyPI',
            'date': '2026持续更新',
            'url': 'https://docs.xarray.dev/en/stable/'
        },
        {
            'title': '2. Cartopy海洋地图绘制:基于matplotlib的地理数据处理',
            'badge': '[Python库]',
            'abstract': 'Cartopy是基于matplotlib的地理数据处理和可视化库，提供地图投影、海岸线、边界等地理数据。Cartopy广泛用于海洋科学地图绘制，支持多种地图投影和地理坐标系，可以轻松绘制海洋温度、盐度、海流等海洋要素的空间分布图。',
            'source': 'Scipy / Cartopy',
            'date': '2026持续更新',
            'url': 'https://scitools.org.uk/cartopy/docs/latest/'
        },
        {
            'title': '3. Ocean Toolbox:Python海洋科学工具集',
            'badge': '[工具集]',
            'abstract': 'Ocean Toolbox是一个Python海洋科学工具集合，包含海洋数据处理、海洋统计分析、海洋可视化等多个模块。该工具集提供开箱即用的海洋数据分析功能，支持海洋观测数据、模型输出数据等多种数据类型的处理和分析。',
            'source': 'Ocean Toolbox / GitHub',
            'date': '2026持续开发',
            'url': 'https://github.com/ocean-foo/ocean-toolbox'
        },
    ]
}

# 合并所有方向
FINAL_SECTIONS = ORIGINAL_SECTIONS + [NEW_OCEAN_DATACENTER, NEW_TOOLS_AND_CODE]

# 输出代码
sections_code = "SECTIONS = [\n"
for section in FINAL_SECTIONS:
    sections_code += f"    {{\n"
    sections_code += f"        'title': '{section['title']}',\n"
    sections_code += f"        'en': '{section['en']}',\n"
    sections_code += f"        'items': [\n"
    
    for item in section['items']:
        sections_code += f"            {{\n"
        sections_code += f"                'title': '{item['title']}',\n"
        sections_code += f"                'badge': '{item['badge']}',\n"
        sections_code += f"                'abstract': (\n"
        sections_code += f"                    '{item['abstract']}'\n"
        sections_code += f"                ),\n"
        sections_code += f"                'source': '{item['source']}',\n"
        sections_code += f"                'date': '{item['date']}',\n"
        sections_code += f"                'url': '{item['url']}'\n"
        sections_code += f"            }},\n"
    
    sections_code += f"        ]\n"
    sections_code += f"    }},\n"
sections_code += "]\n"

# 统计信息
total_sections = len(FINAL_SECTIONS)
total_items = sum(len(s['items']) for s in FINAL_SECTIONS)

print(f"[INFO] 重构完成: {total_sections} 个方向，{total_items} 条动态")
print("\n[INFO] 新增方向:")
print("  - 八、海洋数据中心")
print("  - 九、工具与代码资源")

# 写入文件
with open('final_sections_9dirs.py', 'w', encoding='utf-8') as f:
    f.write(sections_code)

print("\n[OK] SECTIONS代码已保存到: final_sections_9dirs.py")
print("[INFO] 请手动复制到 feishu_write_doc.py 替换原SECTIONS部分")
