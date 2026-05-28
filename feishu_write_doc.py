#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接以数据对象形式定义，绕过字符串引号冲突
"""
import requests
import json
import sys
import time
from datetime import datetime, timedelta

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
TENANT_DOMAIN = "wcn5jx0ifkx3.feishu.cn"

yesterday_cn = (datetime.now()).strftime('%Y\u5e74%m\u6708%d\u65e5')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [   {   'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [   {   'abstract': '山东科技大学测绘与空间信息学院艾波教授团队自主研发海洋时空智能大模型OceanAI，针对通用大模型在海洋场景"水土不服"问题，以垂直化、专业化、本地化为核心，突破多模态大模型协同推理与海洋时空智能体关键技术。已形成"智答"（基于法规知识库的自然语言问答，查询时间从数小时压缩至十几秒）、"智图"（数十秒自动生成海洋专题制图）、"智空"（自主完成空间分析任务）、"智策"（多源数据智能推演决策支持）四项标杆应用。成果通过青岛阅海信息服务有限公司商业化运营，服务自然资源部、交通运输部、中海油等近百家单位。',
                         'badge': '近7天',
                         'date': '2026-05-28',
                         'source': '科技日报 / 云南网',
                         'title': '山东科技大学推出海洋时空智能大模型OceanAI：海洋数据"开口说话"（科技日报, 2026-05-28）',
                         'url': 'https://finance.sina.com.cn/tjhz/2026-05-28/doc-inhzkwsv1236934.shtml'},
                     {   'abstract': '本论文研发Volador 1.0，一种基于MOE-Swin-Transformer框架的数据驱动海气全耦合区域预报模型，针对南海实现亚中尺度可分辨预报。核心创新包括：集成专家混合（MoE）系统的Swin-Transformer架构、跨网格双向交叉注意力隐空间交互架构、快慢双分支架构。3个月历史回放和15天实时预报验证表明，0-72小时内上层海洋温度、盐度和海表高度预报精度优于或等于REDOS V2.0、GLORYS12和ROMS数值模型。模型具备捕捉内波等亚中尺度过程的能力，消融实验证实海气动态通量交换显著提升预报性能。',
                         'badge': '近7天',
                         'date': '2026-05-21',
                         'source': 'arXiv (physics.ao-ph)',
                         'title': 'Volador 1.0：基于MOE-Swin-Transformer的南海海气全耦合亚中尺度可分辨预报模型（arXiv 2605.24032, 2026-05-21）',
                         'url': 'https://arxiv.org/abs/2605.24032'},
                     {   'abstract': 'Njord将深度潜变量框架与图神经网络（GNN）相结合，是首个适用于全球和区域域的概率数据驱动海洋预报模型。仅需单次前向传播即可对每个预报步骤进行采样，在0.25度全球分辨率和2公里波罗的海区域分辨率下应用验证。引入K-means聚类网格适配不规则海面几何形状。在全球OceanBench基准测试中，Njord在上层海洋变量（尤其是海表温度）的平均误差最低，同时通过集合采样提供不确定性估计，弥补了现有ML海洋模型仅能输出确定性预报的缺陷。',
                         'badge': '1周~1个月',
                         'date': '2026-05-15',
                         'source': 'arXiv (physics.ao-ph)',
                         'title': 'Njord：首个概率图神经网络集合海洋预报模型（arXiv 2605.15470, 2026-05-15）',
                         'url': 'https://arxiv.org/abs/2605.15470'},
                     {   'abstract': 'arXiv最新论文以地中海西部海表温度和动能日快照为研究对象，系统对比K-means、自组织映射（SOM）和InfoMap三种聚类算法识别海洋区域动力学模式的能力。结果表明：海表温度分析中K-means和SOM始终划分出4种与季节对应的稳定聚类；海表动能分析中InfoMap可揭示局地射流和涡旋等精细水动力结构，同时具备极端海洋事件异常检测能力。为海洋环流多尺度特征分析提供了互补的方法学参考。',
                         'badge': '近7天',
                         'date': '2026-05-27',
                         'source': 'arXiv (physics.ao-ph)',
                         'title': '聚类算法表征西地中海海表海洋变率对比分析（arXiv 2605.26666, 2026-05-27）',
                         'url': 'https://arxiv.org/abs/2605.26666'}],
        'title': '一、海洋人工智能'},
    {   'en': 'Ocean Digital Twin',
        'items': [   {   'abstract': '针对传统深海观测系统运维成本高、状态预测难、多平台协同不足等问题，提出深海观测网数字孪生原型（DSON-DT）。通过Unreal Engine 5高保真重建深海观测场景，融合静态设施建模、动态海洋环境仿真、多设备动态行为模拟；提出改进的AR-LSTM算法优化磷酸铁锂电源剩余电量预测精度（MSE低至0.00018，R^2达0.9981）；基于Vue.js开发Web原生交互系统，实现多平台远程操控、历史数据回溯、异常预警和运维规划的闭环管控。',
                         'badge': '1周~1个月',
                         'date': '2026-05-01',
                         'source': 'JGR-Oceans / Wiley',
                         'title': '深海观测网数字孪生原型DSON-DT：虚拟环境重建与数据驱动预测分析（JGR-Oceans, 2026-05-01）',
                         'url': 'https://cdn.ebiotrade.com/newsf/2026-5/20260501084512922.htm'},
                     {   'abstract': 'Maritime Technology Review报道海洋数字孪生（Digital Twin Ocean）正成为全球海洋治理的核心工具，功能类似"海洋版Google Earth"，可叠加洋流、生物、地缘热点等多维数据层，支持航运路线模拟、深海采矿影响预评估。目前已在港口和海上风电场开展测试，为海洋资源开发、合规监管和生态保护提供实时决策支撑。',
                         'badge': '近7天',
                         'date': '2026-05-21',
                         'source': 'Maritime Technology Review / Frontiers in Marine Science',
                         'title': '海洋数字孪生助力全球海洋治理：Maritime Technology Review深度解析（2026-05-21）',
                         'url': 'https://maritimetechnologyreview.com/2026/05/21/global-maritime-governance-gets-a-digital-twin-ocean-boost/'}],
        'title': '二、海洋数字孪生'},
    {   'en': 'Ocean Visualization',
        'items': [   {   'abstract': 'Taylor & Francis旗下Big Earth Data发表研究，评估六边形离散全球网格系统（DGGS）作为地球科学全球尺度建模框架的潜力。相比传统经纬度网格，六边形DGGS具有各向同性和均匀采样优势，能有效减少高纬度区域的几何畸变。研究聚焦其在海洋模型输出可视化、数据插值和多源数据融合展示中的性能提升，为下一代海洋环境数据可视化平台提供方法论依据。',
                         'badge': '近7天',
                         'date': '2026-05-20',
                         'source': 'Big Earth Data / Taylor & Francis',
                         'title': '六边形离散全球网格系统增强地球科学模型可视化性能（Big Earth Data, 2026-05-20）',
                         'url': 'https://www.tandfonline.com/doi/full/10.1080/20964471.2026.2666953'},
                     {   'abstract': 'DestinE推出DEA（Destination Earth Analysis）内容创作平台，用户无需编写代码即可将DestinE数据与自有素材组合，创建交互式数据故事并对外分享。平台专为科学家和决策者设计，支持海洋气候数字孪生模拟结果的可视化呈现，覆盖极端天气情节、长期气候变化趋势等场景，降低高质量海洋数据可视化的门槛。',
                         'badge': '1周~1个月',
                         'date': '2026-04-01',
                         'source': 'Destination Earth / ESA',
                         'title': 'Destination Earth Analysis平台（DEA）：无代码海洋数据故事创作工具（2026-04-01）',
                         'url': 'https://dea.destine.eu/'}],
        'title': '三、海洋可视化'},
    {   'en': 'Ocean Data Quality / QA/QC',
        'items': [   {   'abstract': 'NOAA IOOS QARTOD（Quality Assurance of Real-Time Oceanographic Data）项目持续发布实时海洋数据质控手册，涵盖CTD、流速计、波浪传感器等各类仪器的QC标志定义与使用规范。2026年5月最新更新包含对操作人员的指导说明，已成为全球海洋观测系统QA/QC标准化的重要参考文件，并整合至IOOS平台数据流质量管理流程中。',
                         'badge': '近7天',
                         'date': '2026-05-22',
                         'source': 'NOAA IOOS / QARTOD',
                         'title': 'IOOS QARTOD：实时海洋数据质控标志手册持续更新（2026-05）',
                         'url': 'https://ioos.noaa.gov/project/qartod/'}],
        'title': '四、海洋数据质量'},
    {   'en': 'Ocean Data Processing',
        'items': [   {   'abstract': '研究开发基于UNet的深度学习降尺度方法，将Pangu-Weather等AI气象预报模型的海洋表面矢量风分辨率从0.25度提升至更精细区域尺度，专注台湾海峡及周边海域。时空增强型TempE-UNet通过残差学习提升细尺度海洋风场结构重建能力，为高分辨率海洋-大气耦合数值建模提供数据预处理解决方案，已在Journal of Oceanology and Climatology发表。',
                         'badge': '近7天',
                         'date': '2026-05-01',
                         'source': 'Journal of Oceanology and Climatology / ScienceDirect',
                         'title': 'UNet深度学习降尺度：提升台湾海峡海洋表面矢量风分辨率（J. Oceanol. Climatol., 2026-05-01）',
                         'url': 'https://www.sciencedirect.com/science/article/pii/S0924796326000461'}],
        'title': '五、海洋数据处理'},
    {   'en': 'Ocean Data Management and Sharing Services',
        'items': [   {   'abstract': 'IOC/UNESCO IODE平台发布海洋数据信息管理战略计划（2023-2029），描述如何实施功能化、可互操作的数据与信息管理实践和框架。核心愿景是建立全面一体化的海洋数据与信息系统，通过基础设施能力提升、通用方法建立和可互操作数据共享，打造全球"数字海洋生态系统"，服务于联合国海洋十年目标。',
                         'badge': '近7天',
                         'date': '2026-05-20',
                         'source': 'IOC-UNESCO / IODE',
                         'title': 'IOC海洋数据信息管理战略计划（2023-2029）：构建全球数字海洋生态系统（IOC-UNESCO, 2026-05-20）',
                         'url': 'https://iode.org/ioc-strategic-plan-for-ocean-data-and-information-management/'},
                     {   'abstract': 'IOC/UNESCO通过IODE平台持续开放两门虚拟实验室在线课程：《How to use a Virtual Laboratory on Coastal Ocean Currents》和《How to use a Virtual Laboratory on Carbon Plankton Dynamics》，均延续至2026年7月，向全球海洋数据从业者和研究人员免费提供海洋数据处理与分析能力培训，是IODE数据能力建设"联合国海洋十年"行动计划的组成部分。',
                         'badge': '近7天',
                         'date': '2026-05-22',
                         'source': 'IOC-UNESCO / IODE',
                         'title': 'IOC-UNESCO：IODE虚拟实验室培训课程持续开放至2026年7月（2026-05）',
                         'url': 'https://iode.org/'}],
        'title': '六、海洋数据管理与共享服务'},
    {   'en': 'Open Cruises / Ship Time Sharing',
        'items': [   {   'abstract': '中国科学院海洋研究所"创新二"号科考船圆满完成北黄海水文环境调查航次，返回青岛母港。本航次搭载中科院海洋所、山东省海洋科学研究院等单位科考队员和船员23名，历时9天航程750余海里。首席科学家薛福峰介绍，团队精准获取了北黄海水深、春季温盐流及海底地形地貌数据，评估了深远海养殖设施布设安全与施工条件。',
                         'badge': '近7天',
                         'date': '2026-05-19',
                         'source': '青岛日报社 / 观海新闻',
                         'title': '中科院"创新二"号完成北黄海水文环境调查航次返回青岛（2026-05-19）',
                         'url': 'https://finance.sina.com.cn/roll/2026-05-19/doc-inhymivk0068297.shtml'},
                     {   'abstract': 'IOOS发布2026年5月通讯Eyes on the Ocean，涵盖观测系统、数据与建模最新进展：华盛顿州Kalaloch新HF雷达站投入运行，马萨诸塞州Martha\'s Vineyard新增13 MHz CODAR雷达站，佛罗里达州Venice WERA HF雷达站恢复运行（飓风损坏后）。NOAA-海军飓风滑翔机合作扩展，4架海军滑翔机将部署至夏威夷和关岛水域。DMAC数据管理年会将于6月2-4日在Silver Spring举行。',
                         'badge': '近7天',
                         'date': '2026-05-22',
                         'source': 'NOAA IOOS',
                         'title': 'IOOS 5月通讯：HF雷达网络扩展、滑翔机部署与数据管理年会（2026-05-22）',
                         'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-may-2026/'},
                     {   'abstract': 'NOAA海洋探索项目EX2603于2026年5月16日至6月5日在夏威夷附近海域对Okeanos Explorer号的ROV系统实施全面测试，涵盖机械、电气和软件组件，确保潜水器在2026年正式探索季开始前处于最佳工作状态。这是NOAA延续深海探索能力建设的常规年度举措，将为后续太平洋、加勒比海及密歇根湖科考项目提供技术保障。',
                         'badge': '近7天',
                         'date': '2026-05-16',
                         'source': 'NOAA Ocean Exploration',
                         'title': 'NOAA Okeanos Explorer ROV系统整备测试（EX2603）在夏威夷近海开展（2026-05-16）',
                         'url': 'https://oceanexplorer.noaa.gov/expedition-2026-expeditions/'},
                     {   'abstract': 'Schmidt Ocean Institute研究船R/V Falkor(too)于2026年5月17日至6月20日开展亚马逊峡谷深海浊流（水下雪崩）研究航次，由MBARI的Aaron Micallef和摩德纳大学Vittorio Maselli联合领队。将验证亚马逊河口322公里处是否存在现代活跃浊流，评估浊流对底栖生态系统的影响，研究有机碳和微塑料的深海埋藏通量。',
                         'badge': '近7天',
                         'date': '2026-05-17',
                         'source': 'Schmidt Ocean Institute',
                         'title': 'Schmidt海洋研究所R/V Falkor(too)：亚马逊峡谷水下雪崩科考启航（2026-05-17）',
                         'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/'}],
        'title': '七、开放航次 / 船时共享'},
    {   'en': 'Ocean Data Centers / Data Archives',
        'items': [   {   'abstract': 'Copernicus Marine In Situ TAC发布2026年第一季度数据组合扩展报告，主要新增：北极地区Fram Strait RV Lance CTD数据集和新FerryBox航线近实时观测；波罗的海爱沙尼亚15个新近实时海平面站；西北陆架德国46个验潮站历史数据整合；伊比利亚地区4个潮汐平台波浪数据和Galicia 5个浮标恢复；黑海新增罗马尼亚沿岸浮标提供温盐和生化观测；全球范围新增意大利波浪浮标和SHOM约8万个海洋学剖面数据（1902-2017年）。',
                         'badge': '近7天',
                         'date': '2026-05-26',
                         'source': 'Copernicus Marine In Situ TAC',
                         'title': 'CMEMS原位数据组合Q1 2026扩展：北极至黑海多区域新增数据流（2026-05-26）',
                         'url': 'https://marineinsitu.eu/expanding-the-copernicus-marine-in-situ-data-portfolio-in-q1-2026/'},
                     {   'abstract': 'Copernicus Marine Service（CMEMS）发布2026年5月产品质量月报，对全球、区域海洋物理分析和预报产品的科学性能指标进行系统性评估，涵盖SST偏差、盐度误差和海流速度精度等关键参数。报告支持用户判断数据可靠性，是CMEMS服务等级协议（SLA）履行的核心组成部分，相关数据可通过Access Data页面直接获取。',
                         'badge': '近7天',
                         'date': '2026-05-24',
                         'source': 'Copernicus Marine Service (CMEMS)',
                         'title': 'CMEMS 5月产品质量月报发布：全球海洋物理分析预报产品性能更新（2026-05-24）',
                         'url': 'https://marine.copernicus.eu/access-data/'}],
        'title': '八、海洋数据中心'},
    {   'en': 'Tools and Code Resources',
        'items': [   {   'abstract': 'Parcels（Probably A Really Computationally Efficient Lagrangian Simulator）是高度可定制的拉格朗日粒子追踪Python库，可利用格点化海洋模型输出（如NEMO、SCHISM、ROMS）创建粒子运动仿真模拟。2026年5月最新更新持续维护，支持海洋微塑料、鱼卵、石油扩散等多类海洋传输问题的定量分析，在GitHub上活跃维护。',
                         'badge': '近7天',
                         'date': '2026-05-21',
                         'source': 'Parcels / GitHub',
                         'title': 'Parcels粒子追踪库：最新更新（GitHub / parcels-code.org, 2026-05）',
                         'url': 'https://parcels-code.org/'}],
        'title': '九、工具与代码资源'}]

def tr(text, bold=False, link=None):
    element = {"text_run": {"content": text}}
    if bold:
        element["text_run"]["style"] = {"bold": True}
    if link:
        element["text_run"]["link"] = {"url": link}
    return element


def paragraph(elements):
    return {"block_type": 2, "text": {"elements": elements, "style": {}}}


def heading(text, level=1):
    prefix = {1: "\u3010", 2: "  >> "}.get(level, "    ")
    suffix = {1: "\u3011", 2: ""}.get(level, "")
    return paragraph([tr(prefix + text + suffix, bold=True)])


def divider():
    return paragraph([tr("\u2500" * 50)])


def item_block(num, title, badge, abstract, source, date, url):
    blocks = []
    badge_text = badge if badge else ""
    title_text = f"{badge_text} {title}" if badge_text else title
    blocks.append(paragraph([tr(f"  {num}. ", bold=True), tr(title_text, bold=True, link=url)]))
    blocks.append(paragraph([tr(abstract)]))
    meta_parts = []
    if source:
        meta_parts.append(f"来源：{source}")
    if date:
        meta_parts.append(f"日期：{date}")
    if url:
        meta_parts.append(f"链接：{url}")
    blocks.append(paragraph([tr(" | ".join(meta_parts), bold=False)]))
    blocks.append(divider())
    return blocks


def section_block(title, en_title, items):
    blocks = []
    blocks.append(heading(title, 1))
    blocks.append(paragraph([tr(en_title, bold=False)]))
    blocks.append(divider())
    for i, item in enumerate(items, 1):
        blocks.extend(item_block(
            i,
            item.get('title', ''),
            item.get('badge', ''),
            item.get('abstract', ''),
            item.get('source', ''),
            item.get('date', ''),
            item.get('url', '')
        ))
    return blocks


def build_blocks():
    blocks = []
    blocks.append(heading(f"海洋AI技术日报 · {datetime.now().strftime('%Y年%m月%d日')}", 1))
    blocks.append(divider())
    for section in SECTIONS:
        blocks.extend(section_block(
            section['title'],
            section.get('en', ''),
            section.get('items', [])
        ))
    return blocks


def create_document_and_write(tenant_access_token):
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    payload = {"title": f"海洋AI技术日报 {datetime.now().strftime('%Y-%m-%d')}"}
    headers = {
        "Authorization": f"Bearer {tenant_access_token}",
        "Content-Type": "application/json"
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    doc_id = resp.json()["data"]["document"]["document_id"]
    print(f"文档创建成功: {doc_id}")
    return doc_id


def write_blocks_to_doc(token, doc_id, blocks, max_retries=3, batch_size=30):
    """分批写入内容块到飞书文档"""
    base_url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 分批处理
    total_batches = (len(blocks) + batch_size - 1) // batch_size
    for batch_idx in range(total_batches):
        batch_start = batch_idx * batch_size
        batch_end = min((batch_idx + 1) * batch_size, len(blocks))
        batch_blocks = blocks[batch_start:batch_end]
        
        print(f"写入第 {batch_idx + 1}/{total_batches} 批 ({batch_start}-{batch_end} 共{len(blocks)}个块)...")
        
        for attempt in range(max_retries):
            try:
                resp = requests.post(
                    base_url, 
                    headers=headers, 
                    json={"children": batch_blocks, "index": batch_start},
                    timeout=120
                )
                if resp.status_code == 200:
                    print(f"  第 {batch_idx + 1} 批写入成功 ({len(batch_blocks)}个块)")
                    break
                elif resp.status_code == 429:
                    wait_time = 120
                    print(f"  遇到限流，等待 {wait_time} 秒...")
                    time.sleep(wait_time)
                else:
                    print(f"  写入失败 (状态码: {resp.status_code}): {resp.text[:200]}")
                    if attempt < max_retries - 1:
                        time.sleep(10)
            except Exception as e:
                print(f"  写入异常: {e}")
                if attempt < max_retries - 1:
                    time.sleep(10)
        else:
            print(f"  第 {batch_idx + 1} 批写入失败")
    
    print(f"文档写入完成，共 {len(blocks)} 个内容块")


def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["tenant_access_token"]


def main():
    print("开始推送飞书文档...")
    token = get_tenant_access_token()
    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)
    with open("feishu_doc_url.txt", "w") as f:
        f.write(f"https://wcn5jx0ifkx3.feishu.cn/docx/{doc_id}\n")
    print(f"文档地址已保存: feishu_doc_url.txt")


if __name__ == "__main__":
    main()
