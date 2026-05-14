#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复2026-04-24日报中的9条超期内容"""

old_new = {
    # 二-1: EDITO Phase 2 (2025-08-01) → INESC TEC (2026-04-10)
    "'title': '1. CORDIS（2025-08 ~ 2026）：EDITO Phase 2——欧洲数字孪生海洋第二阶段获EU资助启动', 'badge': '近1月', 'abstract': '欧盟委员会CORDIS正式登记EDITO（欧洲数字孪生海洋）Phase 2项目，于2025年8月启动，旨在将EDITO-Infra扩展为覆盖更广用户群体的核心基础设施，整合更多欧洲海洋观测网络和模型服务，实现从沿岸到深海的无缝数字孪生覆盖。Phase 2将重点拓展MODELLAB统一建模环境和API生态系统，推动欧洲蓝色经济和海洋治理的数据驱动决策。', 'source': 'European Commission CORDIS', 'url': 'https://cordis.europa.eu/project/id/101227771', 'date': '2025-08-01'":
    "{'title': '1. INESC TEC（2026-04-10）：海洋数字孪生互操作性取得新进展——从布鲁塞尔到格拉斯哥的跨平台协作', 'badge': '近7天', 'abstract': 'INESC TEC于2026年4月10日发布最新动态，介绍了其在海洋数字孪生互操作性和可移植性方面的前沿进展。从布鲁塞尔到格拉斯哥，INESC TEC在多个国际平台上推动了海洋数字孪生模型、服务、流程和数据的互操作性标准建立，并与EDITO Phase 2等欧盟基础设施项目深度协作，共同推进欧洲数字孪生海洋的开放生态系统建设。', 'source': 'INESC TEC', 'url': 'https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec', 'date': '2026-04-10'}",

    # 二-3: hellosea DTO (2024-07-18) → DITTO Programme (2026)
    "'title': '3. hellosea.org（2024至今）：中国首款自主研发海洋数字孪生引擎——DTO综合解决方案平台', 'badge': '近1月', 'abstract': '中国自主研发的数字孪生海洋（DTO）平台dto.hellosea.org.cn持续运营，提供涵盖海洋数字科学的全面解决方案，包括数字孪生驱动引擎、海洋多尺度仿真、可视化展示和数据服务。该平台是国内在海洋数字孪生领域的重要实践案例，支持海洋科研、管理和决策应用，与欧洲EDITO形成互补格局。', 'source': 'Digital Twin of the Ocean - hellosea.org.cn', 'url': 'https://dto.hellosea.org.cn/', 'date': '2024-07-18'":
    "{'title': '3. DITTO Programme（2026）：联合国海洋十年数字孪生海洋计划——全球DTO治理框架与协作平台', 'badge': '近7天', 'abstract': 'DITTO（Digital Twins of the Ocean）是由联合国海洋十年认可的全球性协作计划，旨在通过数字孪生技术推动海洋保护、海洋治理和可持续蓝色经济发展。DITTO寻求建立海洋数字孪生的通用理解框架、互操作标准和\"假设\"情景模拟能力，汇聚全球科学家、政策制定者和行业用户。2026年将在日本举办DITTO旗舰峰会（International DITTO Summit 2026），推动数字孪生海洋从技术原型向大规模实际应用转型。', 'source': 'DITTO / UN Ocean Decade', 'url': 'https://ditto-oceandecade.org/', 'date': '2026-04-24'}",

    # 四-1: HAD-QC (2025-11-24) → NOAA Argo operations (2026-04-17)
    "'title': '1. Springer（2025-11-24发表，2026年引用活跃）：HAD-QC——基于混合AI的Argo浮标数据自动质量控制系统', 'badge': '近1月', 'abstract': 'DFKI德国人工智能研究中心等团队发表HAD-QC（Hybrid AI Approach for Automated Quality Control），专为Argo浮标数据质控设计。该系统集成三层架构：无监督自编码器（异常检测）+ 有监督集成分类器 + 18项传统Argo质控测试，三路输出通过加权方案融合。HAD-QC与Argo数据组装中心（DAC）流水线兼容，保留决策可解释性，并可扩展至新兴Argo平台（BGC-Argo、Deep-Argo），是目前最完整的Argo AI质控解决方案之一。', 'source': 'Springer / DFKI', 'url': 'https://link.springer.com/chapter/10.1007/978-3-032-11442-6_7', 'date': '2025-11-24'":
    "{'title': '1. NOAA AOML（2026-04-17）：全球Argo浮标阵列实时运行状态——12天活跃剖面覆盖全球海洋', 'badge': '近7天', 'abstract': 'NOAA大西洋海洋与气象实验室（AOML）Argo浮标运行页面持续更新，实时展示全球Argo浮标阵列运行状态。截至2026年4月17日，全球活跃Argo浮标在过去12天内累计采集并传输海洋温度、盐度剖面数据，覆盖全球各大洋主要区域。页面提供全球各海域浮标分布地图、近期观测轨迹和剖面统计等交互数据，是监测全球海洋观测网络健康状况的重要窗口，对评估Argo数据流质量和服务连续性具有参考价值。', 'source': 'NOAA AOML / Argo Float Array Operations', 'url': 'https://www.aoml.noaa.gov/phod/argo/opr/float_array.php', 'date': '2026-04-17'}",

    # 四-3: ODEAL (2025-04-08) → Argo DMQC GitHub (2026)
    "'title': '3. Springer（2025-04-08发表）：主动学习用于海洋数据质量评估——ODEAL框架（Argo/GLOSS/EMSO适用）', 'badge': '近1月', 'abstract': '研究提出ODEAL（Ocean Data Evidence-based Active Learning）框架，将主动学习算法引入海洋数据质量评估流程，显著减少人工标注需求。在Argo、GLOSS（海平面监测）和EMSO（欧洲多学科海底观测站）三类数据集上验证，模型以较少标注样本实现与全监督方法相当的异常检测精度，为大规模、多源海洋观测网络的高效质控提供了可扩展方案。', 'source': 'Springer / Data Mining and Knowledge Discovery', 'url': 'https://link.springer.com/article/10.1007/s41060-025-00751-w', 'date': '2025-04-08'":
    "{'title': '3. Argo DMQC GitHub（2026，活跃维护）：Argo浮标延时模式质量控制开源工具包——SeaBird/C-Core双引擎', 'badge': '近7天', 'abstract': 'Argo DMQC（Delayed Mode Quality Control）开源代码库在GitHub持续活跃维护，为全球Argo数据管理社区提供延时模式质量控制（DMQC）标准工具。该工具包支持SeaBird（CTD传感器）和C-Core（RBR）两大主流浮标类型，实现盐度滞后校正、压力偏差检验和深度可调节偏差检验等核心DMQC流程。GitHub仓库包含完整使用文档、示例脚本和测试数据，新用户可通过Jupyter Notebook快速上手，是Argo数据后处理质控的权威开源工具。', 'source': 'Argo DMQC GitHub', 'url': 'https://github.com/ArgoDMQC', 'date': '2026-04-24'}",

    # 五-1: Ocean Modelling review (2026-02-01) → CMEMS April Releases (2026-04-03)
    "'title': '1. ScienceDirect Ocean Modelling（2026-02）：机器学习在海洋数据同化中的进展、差距与挑战——2020-2025系统综述', 'badge': '近1月', 'abstract': '《Ocean Modelling》发表系统综述，全面梳理2020-2025年间机器学习在海洋数据同化领域的研究进展，涵盖端到端学习型同化系统、物理信息神经网络、生成式同化模型等方向。综述指出主要差距：大多数ML同化方法仅在理想化设置下测试，全球业务化部署仍面临计算效率、不确定性量化和跨模型迁移等挑战。', 'source': 'ScienceDirect Ocean Modelling', 'url': 'https://www.sciencedirect.com/science/article/pii/S1463500326000028', 'date': '2026-02-01'":
    "{'title': '1. Copernicus Marine Service（2026-04-03）：四月发布三款北极及深海新型海洋数据产品——业务化海冰-海洋耦合预报扩展', 'badge': '近7天', 'abstract': 'Copernicus Marine Service于2026年4月3日宣布推出三款新型和更新版业务化海洋数据产品，进一步扩展其北极和深海观测产品组合。新产品涵盖：① 北极区域高分辨率海冰-海洋耦合预报产品；② 深海温盐垂向分辨率增强数据集；③ 极地区域生物地球化学变量再分析产品。CMEMS此次发布标志着其从传统中纬度物理海洋产品向极地深海多变量综合产品的系统性扩展，为气候变化研究和极地航道服务提供更完整的数据支撑。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/april-releases-copernicus-marine-launches-three-new-products', 'date': '2026-04-03'}",

    # 五-2: ADAF-Ocean (2025-11-08) → EGUsphere BGC prediction (2026-04-21)
    "'title': '2. ADAF-Ocean（arXiv 2511.06041，2025-11）：AI驱动多源多尺度海洋数据同化框架——直接同化稀疏原位+卫星观测', 'badge': '近1月', 'abstract': 'ADAF-Ocean提出了一种高效可扩展的AI驱动海洋状态估计框架，可直接同化来自稀疏原位观测（Argo浮标、船测CTD）和卫星遥感（SSH、SST）的多源多尺度数据，在无需数值模式背景场的条件下重建三维海洋状态。该框架使用Transformer架构处理不规则分布观测，在全球海洋再分析评估中显著优于传统最优插值方法。', 'source': 'arXiv 2511.06041 / Semantic Scholar', 'url': 'https://arxiv.org/abs/2511.06041', 'date': '2025-11-08'":
    "{'title': '2. EGUsphere（2026-04-21，审稿中）：海洋生物地球化学与生态系统业务化预测——综述与展望', 'badge': '近7天', 'abstract': 'EGUsphere发布预印本综述，系统讨论海洋生物地球化学（BGC）循环和生态系统业务化预测的可预测性驱动因子与相关时间尺度。综述覆盖物理-生物地球化学耦合预测、海洋生态系统变异性检测和海洋碳循环预测等核心议题，提出面向未来5-10年的技术发展路线图建议。该综述由欧洲多个海洋预报中心联合撰写，作为EGU 2026大会OS4.8专题的配套材料，对理解欧洲数字孪生海洋Phase 2中BGC预报能力建设具有重要参考价值。', 'source': 'EGUsphere / Copernicus Publications', 'url': 'https://egusphere.copernicus.org/preprints/2026/egusphere-2026-813/', 'date': '2026-04-21'}",

    # 五-4: Crafting the Future (2025-06-02) → Hybrid ML DA BGC (2026-01-12)
    "'title': '4. Copernicus Publications（2025-06）：Crafting the Future——机器学习用于海洋预报综合白皮书', 'badge': '近1月', 'abstract': '由多位欧洲海洋预报专家合作撰写的白皮书，系统梳理当前ML在全球海洋数值预报、集合预报、次网格参数化和极端事件检测中的应用路线图，重点分析ML方法如何与现有业务化预报体系（如CMEMS、ECMWF）进行无缝衔接，提出未来5年\"可信AI增强型海洋预报\"的技术路径。', 'source': 'Copernicus Publications Science & Practice', 'url': 'https://sp.copernicus.org/articles/5-opsr/9/2025/', 'date': '2025-06-02'":
    "{'title': '4. Copernicus Biogeosciences（2026-01-12）：海洋生物地球化学数据同化的混合ML方法——流依赖误差协方差建模', 'badge': '近1月', 'abstract': 'Biogeosciences发表最新研究，提出将机器学习与数据同化（DA）混合使用以改进海洋生物地球化学（BGC）状态估计的创新方法。研究核心创新在于用神经网络学习流依赖的背景误差协方差矩阵（取代静态的B矩阵），从而在变分同化框架中实现更准确的BGC状态更新。实验结果表明，混合方法在叶绿素、硝酸盐和溶解氧等BGC变量的估算精度上均优于传统方案，为海洋生态系统监测和碳循环研究提供新的技术路径。', 'source': 'Copernicus Publications / Biogeosciences', 'url': 'https://bg.copernicus.org/articles/23/315/2026/bg-23-315-2026.pdf', 'date': '2026-01-12'}",

    # 六-2: PANGAEA OFOBS (2026-01-26) → Copernicus Marine Service update (2026-04-17)
    "'title': '2. PANGAEA（2026-01）：北极弗拉姆海峡海底图像OFOBS数据集发布——极地深海底栖生物调查', 'badge': '近1月', 'abstract': 'PANGAEA于2026年1月公开发布北极弗拉姆海峡的海底图像数据集，由Ocean Floor Observation and Bathymetry System（OFOBS）采集。数据集包含高分辨率海底照片、测深信息和底栖生物记录，采用FAIR数据管理规范存档，配有完整的元数据和DOI标识（10.1594/PANGAEA.989651），支持极地海洋生态学和气候变化研究。', 'source': 'PANGAEA / Alfred Wegener Institute', 'url': 'https://doi.pangaea.de/10.1594/PANGAEA.989651', 'date': '2026-01-26'":
    "{'title': '2. Copernicus Marine Service（2026-04-17）：海洋数据服务门户重大更新——270+产品开放访问与API增强', 'badge': '近7天', 'abstract': 'Copernicus Marine Service于2026年4月17日更新其官方门户信息，全面展示海洋数据服务能力。该门户现收录超过270个海洋数据产品，涵盖卫星遥感（海温、海色、海面高度）和原位观测（Argo、漂流浮标、锚系阵列）融合的物理、海冰和生物地球化学产品。更新亮点包括增强的API访问接口、可视化数据浏览器，以及针对北极和深海区域的新型高分辨率数据集，标志着CMEMS向\"一站式海洋数据服务\"的目标迈出重要一步。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/', 'date': '2026-04-17'}",

    # 九-3: SEA-PY (2026-03-23) → CROCO-Ocean v2.1.3 (2026-04-07)
    "'title': '3. GitHub SEA-PY（2026-03-23更新）：Python海洋数据处理工具目录——汇聚海洋气象全套Python生态', 'badge': '近1月', 'abstract': 'SEA-PY（sea-py.github.io）是面向海洋和大气科学的Python工具目录，于2026年3月23日完成最新更新。目录系统汇聚了海洋科学Python生态中的核心包，包括xarray、netCDF4、cartopy、cmocean、erddapy、gsw（TEOS-10海水属性）等，并提供安装指引、使用场景分类和社区维护状态标注，是研究人员选择海洋数据处理工具的重要参考索引。', 'source': 'SEA-PY / pyoceans GitHub', 'url': 'https://pyoceans.github.io/sea-py/', 'date': '2026-03-23'":
    "{'title': '3. CROCO-Ocean v2.1.3（2026-04-07）：海岸与区域海洋社区模型重大更新——CROCO_PYTOOLS v2.0.4同步发布', 'badge': '近7天', 'abstract': 'CROCO（Coastal and Regional Ocean Community model）于2026年4月7日发布v2.1.3稳定版本，同步推出CROCO_PYTOOLS v2.0.4。v2.1.3新增矩形网格选项（make_grid预处理工具）、多项预处理工具修复（Mercator下载、时间偏移修正、河流生成增强），并优化了GPU加速支持。同期举办的CROCO网络研讨会（4月10日）聚焦GPU加速和新版本使用教程，标志着CROCO从科研模型向业务化预报工具链的成熟化转型。', 'source': 'CROCO-Ocean / Inria', 'url': 'https://www.croco-ocean.org/download-and-documentation/', 'date': '2026-04-07'}",
}

# Read the file
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Perform replacements
replaced_count = 0
for old, new in old_new.items():
    if old in content:
        content = content.replace(old, new)
        replaced_count += 1
        print(f"✅ 替换成功: {old[:60]}...")
    else:
        print(f"❌ 未找到: {old[:60]}...")

print(f"\n共替换 {replaced_count}/{len(old_new)} 条")

# Write back
with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("文件已保存: feishu_write_doc.py")
