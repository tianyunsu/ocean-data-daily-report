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

yesterday_cn = (datetime.now()).strftime('%Y年%m月%d日')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'DLESyM-Ocean：深度学习概率全球模型模拟当代上层海洋与海冰（arXiv, 2026-08-12）', 'badge': '[论文]', 'abstract': '华盛顿大学团队提出 DLESyM-Ocean，一种深度学习地球系统模型，利用 patch energy score 损失（非扩散或 CRPS）训练，在全球大气强迫下生成校准良好、空间一致的海冰与上层海洋集合预报。模型可自回归稳定运行多年，气候态与变率偏差极小。案例研究覆盖海冰极端事件、海洋热浪、2023年厄尔尼诺过渡及全球均温 spike，均能产生 realistic 的表层/次表层轨迹与充分的集合多样性，展现出学习到的自回归海洋动力学。计算效率高，可与大气分量耦合用于次季节-季节预报。', 'source': 'arXiv / physics.ao-ph（Univ. Washington + UCI + MIT）', 'url': 'https://arxiv.org/abs/2608.11545', 'date': '2026-08-12'}, {'title': 'OceanLight：几何自适应非结构化网格+GNN高效全球海洋预报（arXiv, 2026-08-17）', 'badge': '[论文]', 'abstract': '现有深度学习海洋预报多基于结构化网格，在陆地区域产生无效计算且无法适应不同区域的流动复杂性。OceanLight 创新性地结合几何自适应非结构化网格 tokenization 与图神经网络（GNN）骨干，实现全球海洋预报。其点预报精度与动能能谱保真度超越业务数值分析和现有AI模型，且在地转平衡一致性上优于所有AI海洋模型。可靠地再现中尺度涡旋等相干海洋结构。相比结构化网格基线，GPU显存减少62%、FLOPs减少70%，为可扩展数据驱动海洋学建立通用范式。', 'source': 'arXiv / cs.LG', 'url': 'https://arxiv.org/abs/2608.16070', 'date': '2026-08-17'}, {'title': 'IJCAI-ECAI 2026 AI4G：AI-海洋动力学协同的海洋热极端事件早期预警系统（2026-08-20, Bremen）', 'badge': '[论文]', 'abstract': '北京邮电大学团队在第35届IJCAI暨第29届ECAI大会"AI for Social Good"专题track发表海洋热极端事件早期预警系统研究。该工作融合多源观测与物理信息神经网络（PINN），确保预测受基本物理定律约束，可预报事件 onset、强度、持续时间和空间范围，同时归因底层机制（海洋平流、海气热交换）。建立专门海洋热极端基准评估预测技巧与归因可靠性，并引入增量学习机制持续适应长期气候演变。为政策制定与海洋决策提供可靠、可解释、自适应的预警工具。', 'source': 'IJCAI-ECAI 2026 AI4G Special Track（BUPT）', 'url': 'https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-social-good', 'date': '2026-08-20'}, {'title': '退化视觉条件下水下机器人跨模态基础模型感知：DINOv2+声呐门控融合（arXiv, 2026-08-20）', 'badge': '[论文]', 'abstract': '针对水下机器人在退化视觉条件（低光照、悬浮物、色彩失真）下的环境感知难题，研究团队提出跨模态基础模型框架。该方法以 DINOv2 视觉基础模型为核心，引入前视声呐作为互补感知模态，通过门控融合机制动态调节视觉与声呐信息的权重。在浑浊水域、夜间作业等极端场景下，显著提升了目标检测与场景理解的鲁棒性，为AUV在复杂近海环境中的自主作业提供新的感知范式。', 'source': 'arXiv / cs.CV', 'url': 'https://arxiv.org/abs/2608.19710', 'date': '2026-08-20'}, {'title': '世界模型接地LLM规划用于AUV/ASV近海风电场导航（arXiv, 2026-08-20）', 'badge': '[论文]', 'abstract': '研究团队将世界模型（World Model）与大语言模型（LLM）规划相结合，为自主水下航行器（AUV）和自主水面艇（ASV）在近海风电场的导航与运维任务提供高层决策能力。世界模型学习环境动态，LLM负责任务级规划与异常推理，二者协同使无人系统能够在复杂海洋工程环境中执行 inspection、维护路径规划等任务。该方法弥补了传统路径规划在动态障碍物响应与任务语义理解方面的不足。', 'source': 'arXiv / cs.RO', 'url': 'https://arxiv.org/abs/2608.19661', 'date': '2026-08-20'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': 'Digital Twins of the Ocean：架构、使能技术与挑战综述（Ocean-Land-Atmosphere Research, 2026-08-17）', 'badge': '[论文]', 'abstract': '发表在OLAR的综述论文系统阐述海洋数字孪生（DTO）的四层架构：数据层（多源观测与再分析）、模型层（AI/物理耦合模拟）、服务层（交互式可视化与决策支持）和应用层（渔业管理、气候适应、近海工程）。论文梳理了数字孪生海洋所需的关键使能技术，包括高分辨率海洋模式、边缘计算、物联网浮标网络、AI同化算法，并指出当前面临的数据孤岛、实时性瓶颈和跨尺度耦合等挑战。为海洋数字孪生从概念走向业务化提供路线图。', 'source': 'Ocean-Land-Atmosphere Research (OLAR)', 'url': 'https://www.sciencedirect.com/science/article/pii/S2772373726001234', 'date': '2026-08-17'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': "NERACOOS推出新版Mariner's Dashboard beta：区域海洋数据一站式可视化（IOOS, 2026-08）", 'badge': '[动态]', 'abstract': "美国东北区域沿海海洋观测系统（NERACOOS）发布升级后的 Mariner's Dashboard beta 版本，响应用户与利益相关方反馈进行交互优化。该仪表板整合浮标地图最受用户喜爱的组件与站点其他核心功能，将当前实况、观测、后报和预报集成于单一面板，用户无需访问多个页面即可获取完整信息。点击地图点位可查看该资产最新记录，右侧表格始终显示最新观测，下方图表展示12小时趋势，并支持7天历史与预报标签页切换。为美国东北部海域航运、渔业和防灾决策提供一体化数据可视化入口。", 'source': 'NERACOOS / IOOS Newsletter', 'url': 'https://mariners.neracoos.org/', 'date': '2026-08-25'}, {'title': 'GLOS发布Seagull Coast移动应用：五大湖沿岸休闲安全数据可视化（2026-08）', 'badge': '[工具]', 'abstract': '大湖观测系统（GLOS）推出全新移动端应用 Seagull Coast，将复杂的五大湖环境观测、预报和海岸灾害信息转化为清晰、可操作的休闲安全洞察。该应用专为移动场景设计，支持实时查看沿岸环境条件、获取游泳、划船、皮划艇等活动的安全建议、设定收藏地点快速访问，并基于NWS大湖海滩灾害预报提供危险感知。Seagull Coast 继承了 Seagull 平台的数据基础设施，以移动优先体验让公众在抵达水边前做出更安全的决策，体现海洋数据可视化从科研走向民生服务的趋势。', 'source': 'GLOS (Great Lakes Observing System)', 'url': 'https://glos.org/seagull-coast-has-launched/', 'date': '2026-08-20'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': '本周暂无明显新进展（Argo GDAC快照 08-08、DTF-Net 08-07 已收录）', 'badge': '[关注]', 'abstract': '海洋数据质量方向近一周无重大新方法或新工具发布。Argo GDAC全球快照（08-08收录于数据中心方向）、DTF-Net深度学习风数据质控（08-07收录）、ML辅助事件感知QC框架（08-08收录）均已在此前日报覆盖，本期不重复收录。', 'source': '-', 'url': 'https://www.argo.org.cn/', 'date': '2026-08-26'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'CMEMS发布北极潮汐分析预报新数据集：3km分辨率15层，TOPAZ6确定性潮汐系统（2026-08）', 'badge': '[动态]', 'abstract': 'Copernicus Marine Service新增北极海洋潮汐分析与预报产品（ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015），空间分辨率3km，垂直15层。该数据集基于TOPAZ6确定性潮汐系统，受TOPAZ5 EnKF 6km系统约束，覆盖北极全海域潮汐与风暴潮预报。作为CMEMS 2026年8月产品路线图的重要组成，该数据集填补了高纬度区域高分辨率潮汐预报的空白，为北极航道航运安全、近海工程设计和海平面变化研究提供关键数据支撑。采用双重发布期机制确保业务连续性。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information?roadmap_category=product', 'date': '2026-08-13'}, {'title': 'CMEMS北极多年度波浪后报时间扩展至1960年：ARCTIC_MULTIYEAR_WAV_002_013更新（2026-08）', 'badge': '[动态]', 'abstract': 'Copernicus Marine Service将北极多年度波浪后报产品时间覆盖范围扩展至1960年，为北极海冰减少背景下的波浪气候态研究提供超过60年的连续数据记录。该产品基于ERA5再分析大气强迫驱动波浪模式，覆盖整个北极海域，包括边缘 ice zone 和开放水域的波高、周期和方向参数。时间扩展使研究人员能够分析北极波浪场对气候变暖的长期响应，为极区基础设施设计和海岸侵蚀评估提供历史基准。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information?roadmap_category=product', 'date': '2026-08-13'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'NSF地球科学部海洋科学项目数据管理与共享计划指南：BioOce/ChemOce/PhysOce截止8月17日（2026-08）', 'badge': '[政策]', 'abstract': '美国国家科学基金会（NSF）地球科学部（GEO）更新海洋科学领域数据管理与共享计划（DMSP）指南。生物海洋学（BioOce）、化学海洋学（ChemOce）和物理海洋学（PhysOce）项目要求所有元数据、完整数据集、衍生产品和实物样本必须在发表时或采集后两年内公开可获取。指南强调使用长期、FAIR对齐的数据仓库，并鼓励利用BCO-DMO（生物与化学海洋学数据管理办公室）确保提案合规。下一次项目申请截止日为2026年8月17日，反映NSF持续推动海洋科学数据开放共享与可重复研究的战略导向。', 'source': 'NSF Directorate for Geosciences (GEO)', 'url': 'https://www.nsf.gov/geo/geo-data-policies/index.jsp', 'date': '2026-08-17'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Research Expeditions', 'items': [{'title': 'NOAA EX2606美属萨摩亚ROV+测绘航次启动：关键矿产与深海生态基线评估（2026-08-20至09-17）', 'badge': '[航次]', 'abstract': '8月20日，NOAA船Okeanos Explorer开启2026年美属萨摩亚ROV+测绘航次（EX2606），为期29天探索美属萨摩亚周边深海水域。航次进行2000-6000米深度ROV下潜，聚焦多金属结核等海洋关键矿产基线评估，以及海山生境、深水珊瑚和海绵群落、鱼类生境和水柱生态调查。通过telepresence技术每日直播（8AM-8PM SST），公众和岸基科学家可实时参与。所有数据将在120天内提交NOAA公开档案。美属萨摩亚被指定为美国EEZ内最高优先级测绘与勘探区域。', 'source': 'NOAA Ocean Exploration', 'url': 'https://oceanexplorer.noaa.gov/expedition/ex2606', 'date': '2026-08-20'}, {'title': '库克群岛政府为Okeanos Explorer举行欢迎仪式：EX2605深潜航次圆满完成（2026-08-17）', 'badge': '[航次]', 'abstract': '8月17日，库克群岛政府在拉罗通加阿瓦提乌港举行正式仪式，欢迎NOAA船Okeanos Explorer完成2026年库克群岛ROV探险（EX2605）。该航次7月19日至8月13日在库克群岛EEZ内进行26天考察，完成14次ROV下潜，采集400余份样本，探索海山、深海平原和Manihiki高原。库克群岛总理布朗表示，小国最大的优势不是海洋面积，而是理解海洋的自信；库克岛民不仅是观察者，更参与制定研究优先事项并与国际专家并肩工作。美国宣布将在库克群岛设立NOAA科学研究员职位。', 'source': 'Cook Islands Seabed Minerals Authority / NOAA', 'url': 'https://www.sbma.gov.ck/news-3/article-279', 'date': '2026-08-17'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'Argo GDAC发布2026-08-08全球快照：133,193个文件/87GB，BGC Sprof CHLA再处理同步更新（2026-08-08）', 'badge': '[数据]', 'abstract': '全球Argo数据assembly中心（GDAC）发布2026年8月8日全球快照，包含133,193个数据文件，总容量87GB。同步发布的BGC-Argo Sprof CHLA（叶绿素a）再处理快照容量6GB。该快照反映全球Argo浮标阵实时观测能力的最新状态，为海洋热含量、盐度趋势和生物地球化学循环研究提供基础数据支撑。GDAC定期快照机制确保全球海洋观测社区能够获取一致、可追溯的数据版本，是海洋数据中心维护数据时效性与完整性的核心运维实践。', 'source': 'Argo Global Data Assembly Centre (GDAC)', 'url': 'https://argo.ucsd.edu/data/argo-data-management/', 'date': '2026-08-08'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'uxarray v2026.08.0发布：球面几何EFT补偿算术+自定义错误类型+面面积向量化（2026-08-18）', 'badge': '[工具]', 'abstract': '非结构化网格气候与全球天气数据分析的Xarray扩展库uxarray发布v2026.08.0版本。核心更新包括：(1)引入基于误差自由变换（EFT）的补偿算术，显著改善球面几何中GCA相交、点-面测试和面部边界在近退化构型下的数值鲁棒性；(2)全面清理和向量化face_areas API，恢复calculate_total_face_area的缓存快速路径；(3)建立专用异常层次结构，替代代码库中误导性和不一致的错误类型。此外修复了calculate_face_area中的雅可比矩阵错误、拓扑聚合中坐标属性保留等问题，并提升文档对新手的友好度。', 'source': 'UXARRAY / GitHub / conda-forge', 'url': 'https://github.com/UXARRAY/uxarray/releases/tag/v2026.08.0', 'date': '2026-08-18'}]}]

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
        
        for attempt in range(max_retries):
            try:
                payload = {
                    "blocks": batch_blocks
                }
                resp = requests.post(base_url, headers=headers, json=payload)
                resp.raise_for_status()
                print(f"Batch {batch_idx + 1}/{total_batches}: blocks {batch_start}-{batch_end-1} written successfully")
                break
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Batch {batch_idx + 1} attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"Batch {batch_idx + 1} failed after {max_retries} attempts: {e}")
                    raise
    print(f"All {len(blocks)} blocks written to document {doc_id}")


def main():
    resp = requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal", json={
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    })
    resp.raise_for_status()
    token = resp.json()["tenant_access_token"]

    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)

    print(f"Document URL: https://{TENANT_DOMAIN}/docx/{doc_id}")


if __name__ == "__main__":
    main()
