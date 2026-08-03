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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'HybridOM：物理-数据混合的全球海洋建模与高效空间降尺度（ICML 2026）', 'badge': '[论文]', 'abstract': 'HybridOM 由清华、复旦、上海AI for Science研究院等团队提出，被 ICML 2026 接收（预印本 arXiv:2602.00598，2026-01）。该方法将轻量可微分数值求解器作为“骨架”以强制物理守恒，再嵌入神经网络作为“血肉”修正子网格尺度动力，并引入基于通量门控的物理信息区域降尺度机制。在 GLORYS12V1 与 OceanBench 上验证了次季节-季节模拟与耦合 FuXi-2.0 的短期业务化预报两种场景，在保持物理一致性的同时达到 SOTA 精度，被称为“下一代海洋数字孪生的可扩展基石”。代码已开源。', 'source': 'ICML 2026 / arXiv', 'url': 'https://arxiv.org/abs/2602.00598', 'date': '2026-07'}, {'title': 'BALLAST：面向海洋漂流器布放的贝叶斯主动学习（ICML 2026）', 'badge': '[论文]', 'abstract': 'BALLAST 由 Lancaster University 等团队提出，被 ICML 2026 接收（预印本 arXiv:2509.26005，2025-09）。针对拉格朗日观测器（漂流器）被流场持续平流、难以用标准主动学习评估全生命周期信息增益的难题，提出“前瞻修正”（look-ahead amendment）：从 GP 后验采样向量场并模拟漂流器未来轨迹，将轨迹上所有后续观测的信息增益纳入效用函数。同时提出 VaSE（Vanilla SPDE Exchange）推理方法，将 GP 后验采样效率提升数千倍。在合成与高保真海洋流场上较空间填充与启发式策略节省约 16%–22% 布放成本。', 'source': 'ICML 2026', 'url': 'https://icml.cc/virtual/2026/poster/66731', 'date': '2026-07'}, {'title': 'SWIN-DeepONet：用 Swin Transformer 增强 DeepONet 学习非线性波动力学（IJCAI-ECAI 2026）', 'badge': '[论文]', 'abstract': 'SWIN-DeepONet 由曼彻斯特大学等团队提出，将在 IJCAI-ECAI 2026（德国不莱梅，8月）以海报展示。该方法用 Swin Transformer 编码器替换 DeepONet 的 MLP 分支，将一维输入剖面提升为二维 token 网格并施加分层滑动窗口自注意力，以线性计算代价捕捉色散波包的多尺度空间结构。在 MNLS 方程波高包络数据上的单步与自回归 rollout 测试中，平均 rollout MSE 较傅里叶特征基线降低 24.3%、最终相对 L2 误差降低 16.0%，且未见训练-测试发散，为非线性波动力学的物理可信代理模型开辟新路径。', 'source': 'IJCAI-ECAI 2026', 'url': 'https://research.manchester.ac.uk/en/publications/swin-deeponet-a-swin-transformer-enhanced-deeponet-for-learning-w', 'date': '2026-07'}, {'title': '多尺度CNN+DropKey-Transformer 的海况估计与不确定性量化模型（JMSE, 2026-07-29）', 'badge': '[论文]', 'abstract': '发表于 Journal of Marine Science and Engineering，提出一种融合多尺度一维 CNN、Transformer 编码器与 MC-DropKey 机制的海况估计架构，从船舶运动响应反演波高与波向。前端多尺度 CNN 提取高质量局部特征，后端 Transformer 捕获全局长程时间依赖，MC-DropKey 在保持高精度的同时实现动态不确定性量化。对比与消融实验显示波高估计 MAE 低至 0.117 m、波向 CAE 5.212°，预测区间覆盖概率达 96.67%，为复杂海况下的智能船舶科学调度与决策提供技术支撑。', 'source': 'Journal of Marine Science and Engineering (MDPI)', 'url': 'https://www.mdpi.com/2077-1312/14/15/1397', 'date': '2026-07-29'}, {'title': 'V-JEPA+深度时空学习从单目视频估算海岸波浪参数（arXiv, 2026-07-15）', 'badge': '[论文]', 'abstract': 'arXiv:2607.11998 提出一种基于视频的深度学习框架，从单目海岸监控视频估算有效波高、波向等五个关键海岸波浪参数。系统利用 V-JEPA 骨干在挑战性视觉条件下提取特征，结合双流 SlowFast 时间编码器与基于 Farneback 光流的方法。在数据受限（仅 6 个带标注训练场景）环境下，对有效波高、波向等参数显示出统计学显著的时间相关性，验证了在更大规模数据集下改进与业务化应用的潜力。', 'source': 'arXiv (cs.AI)', 'url': 'https://arxiv.org/abs/2607.11998', 'date': '2026-07-15'}, {'title': '第2届 ECCV 2026 海洋视觉研讨会（Marine Vision）征稿，聚焦水下成像与感知', 'badge': '[动态]', 'abstract': '由基尔大学、奥尔堡大学、南丹麦大学、MIT、Ocean Networks Canada 等联合组织的第 2 届 Marine Vision 研讨会将在 ECCV 2026（瑞典马尔默，9月8-9日）举办，并申请 UNESCO 海洋十年活动认证。研讨会涵盖水下图像增强与色彩复原、导航建图、三维重建、长尾视觉识别、多目标跟踪、生物细粒度分类、基础模型、遥感环境监测等方向，旨在构建先进的海洋计算机视觉研究社区，推动海岸与深海自动监测能力发展。全文投稿截止 2026-07-13，短摘要截止 2026-07-31。', 'source': 'ECCV 2026 / 基尔大学', 'url': 'https://vap.aau.dk/marinevision/call-for-papers/', 'date': '2026-07'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin / Marine Digital Twin', 'items': [{'title': '欧盟“目的地地球”（DestinE）正式迈入第三阶段，AI 成为核心（2026-07）', 'badge': '[动态]', 'abstract': '欧盟委员会确认 Destination Earth（DestinE）于 2026 年 7 月进入第三阶段（至 2028 年 6 月），由 ECMWF、ESA、EUMETSAT 三方共同实施。新阶段将把气候适应数字孪生（Climate DT）与极端天气数字孪生（Extremes DT）从能力建设转向规模化业务应用，AI 扮演核心角色：ECMWF 将进一步耦合地球系统各圈层（陆地、海洋、海冰、波浪、水文学）的机器学习模块，构建欧洲 AI 地球系统模型，并将海量数字孪生产出转化为供 AI 工厂使用的高质量数据集；ESA 推进平台自然语言交互；EUMETSAT 成熟 Data Lake 运营。海洋相关 ML 组件是 AI 地球系统模型的重要组成部分。', 'source': 'Destination Earth / ECMWF', 'url': 'https://destination-earth.eu/news/destination-earth-moves-into-phase-three/', 'date': '2026-07'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': 'Copernicus Marine 更新产品路线图：预告 MyOcean Pro 3D 可视化与 MyOcean Light 降尺度（2026-07-27）', 'badge': '[动态]', 'abstract': 'Copernicus Marine Service 于 2026-07-27 更新产品路线图，披露多项可视化能力演进：2027 年 1 月将推出 MyOcean Pro 3D Viewer，在数字地球上渲染高分辨率地形与测深；同期 MyOcean Light 扩展降尺度可视化，支持观测数据的降尺度展示；2026 年 12 月将把 EDITO 数据集完整集成进 MyOcean Pro；2026 年 6 月已推出 MyOcean Stories 交互式叙事工具与 MyOcean Health 实时海洋状态图表。路线图体现了哥白尼海洋服务从数据门户向沉浸式、可解释可视化平台的持续演进。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/user-corner/product-roadmap/transition-information?roadmap_category=service', 'date': '2026-07-27'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA-QC', 'items': [{'title': '基于边缘计算与云优化的海洋观测数据实时质量控制方法获中国专利公开（2026-07-07）', 'badge': '[专利]', 'abstract': '国家海洋局北海预报中心（青岛海洋预报台）申请的发明专利（CN122346797A）于 2026-07-07 公开，提出一种边缘计算与云优化结合的海洋观测数据实时质量控制方法。边缘观测节点调用轻量 QC 初筛模型进行粗粒度异常检测并上传疑似异常数据段，云端调用海洋 QC 协同优化模型进行细粒度校验、计算综合异常评分并判定数据质量等级，执行传感器漂移监测与数据剔除，并通过异步联邦学习框架更新边缘节点模型。该方法在保障实时性的同时显著提升异常识别与传输优化能力，有效识别系统性与低概率异常。', 'source': '中国国家知识产权局（CN122346797A）', 'url': 'https://eureka.patsnap.com/patent-CN122346797A', 'date': '2026-07-07'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'BGC-Argo 叶绿素-a（CHLA）首次大规模再处理启动，精度与可用性显著提升（2026-06 起，7月持续推进）', 'badge': '[数据]', 'abstract': '国际 BGC-Argo 计划于 2026 年 6 月 8 日启动其首次高影响叶绿素-a（CHLA）再处理，应用 Sauzède 等（2025）提出的实时生理比新方法，在实时调整中修正 CHLA，部分区域（如南大洋）变化可达约 4 倍。该再处理可能对终端用户产生显著影响，2026-07-08 起未处理的浮标在 MYNRT 产品中将被标记为 QC3（可疑）待其 DAC 处理。截至 2026-07-11 再处理进度持续更新，过渡期内数据集暂缺均一性。这是 BGC-Argo 生物地球化学数据质量提升的关键一步。', 'source': 'Biogeochemical Argo / Copernicus Marine', 'url': 'https://biogeochemical-argo.org/chla-reprocessing.php', 'date': '2026-07-11'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'ODIS 指导小组召开会议审议任务组进展并筹备 IODE-29（2026-07-22/23）', 'badge': '[动态]', 'abstract': '海洋数据与信息系统（ODIS）指导小组于 2026 年 7 月 22–23 日召开两次线上会议，审议年初成立的两个任务组（传播与运营、技术支撑）的进展，并为即将召开的 IODE 委员会第 29 届会议（IODE-29，2026 年 10 月）做准备。会议议程涵盖与各国海洋数据中心（NODC）及关联数据单元（ADU）的沟通、2026–2028 年工作计划的推进，以及 ODIS 与 IOC 数据架构（IOC DA）的对齐，持续推动全球海洋数据的开放共享与互操作。', 'source': 'ODIS / IOC-IODE', 'url': 'https://odis.org/news', 'date': '2026-07-23'}, {'title': 'IOC 执行理事会第 59 届会议通过强化海洋数据交换与互操作的关键决议（2026-07-03）', 'badge': '[动态]', 'abstract': '联合国教科文组织政府间海洋学委员会（IOC）执行理事会第 59 届会议于 2026 年 7 月 3 日在巴黎闭幕，通过一系列推进全球海洋科学、强化早期预警系统、改善海洋观测与数据共享的决议。会议重申 IOC 作为联合国海洋科学、海洋观测、海啸预警、海洋数据交换与能力建设的专门机构角色，并审议了全球海洋观测系统（GOOS）改革、全球海平面观测系统（GLOSS）2026–2030 实施计划，以及构建更具整合性的 IOC 数据架构（IOC DA）以提升海洋数据的可获取性与互操作性。会议还支持 IOC 作为技术伙伴参与《国家管辖范围以外区域海洋生物多样性协定》（BBNJ）信息交换机制建设。', 'source': 'IOC-UNESCO', 'url': 'https://www.ioc.unesco.org/en/articles/iocc-executive-counil-adopts-key-decisions', 'date': '2026-07-03'}]}, {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [{'title': 'Schmidt 海洋研究所“加勒比盐指”科考航次即将启航，探究细尺度混合与碳输出（2026-08-06 起）', 'badge': '[航次]', 'abstract': 'Schmidt 海洋研究所 2026 年航次计划中的“Surveying Salt Fingers in the Caribbean”（加勒比盐指调查）将于 2026-08-06 至 09-02 在 R/V Falkor (too) 上开展，由罗格斯大学 Joseph Gradone 与 Corday Selden 领衔。团队将利用 4 台自主滑翔机、CTD 采水器与垂直微结构剖面仪，研究赤道北大西洋热盐阶梯中的盐指（salt fingering）细尺度混合过程及其向表层输送氮营养盐、促进初级生产与碳输出的作用。研究假设在全球变暖导致盐度格局变化的背景下，盐指正在增强，或影响生态系统结构与全球气候。', 'source': 'Schmidt Ocean Institute / Rutgers', 'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/', 'date': '2026-08-03'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '哥白尼海洋服务（CMEMS）2026 年 7 月服务发布：新监测与预报中心入网，扩展全球数据共享（2026-07-07）', 'badge': '[动态]', 'abstract': '哥白尼海洋服务（Copernicus Marine Service，由 Mercator Ocean International 实施，是欧洲核心海洋数据中心之一）于 2026 年 7 月 7 日发布新一轮服务更新，迎来新的监测与预报中心 COLAB MFC 加入其网络，通过国际数据共享伙伴关系是该服务全球覆盖扩展的重要一步。本轮发布还包含多项数据集与产品更新：地中海与黑海 SST 采用 1991–2020 新气候态并回溯重处理异常场；波浪产品整合 Sentinel-1C 观测；新增 FY-3E WindRAD 风场 L3 近实时数据集；为 Sentinel-6B 接入 DUACS 系统预置新海平面数据集；并将生物地球化学多年代再分析延长至 2025 年上半年。这些更新持续夯实 CMEMS 作为业务化海洋数据中心的全球服务能力。', 'source': 'Copernicus Marine Service / Mercator Ocean', 'url': 'https://marine.copernicus.eu/news/july-release-expanding-copernicus-marine-service-through-global-collaboration', 'date': '2026-07-07'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'xarray v2026.07.0 发布：支持 Dask 查询优化表达式数组与新日期访问器（2026-07）', 'badge': '[工具]', 'abstract': 'Python 多维标注数组库 xarray 发布 v2026.07.0，新增对 Dask 查询优化表达式数组（query-optimizing expression arrays）的支持，可显著提升数据查询与计算效率；引入 day_of_week 与 day_of_year 等 datetime 访问器属性；修复 Coordinates.to_index 性能回归、Zarr v3 fill_value 往返、drop_encoding 过度内存占用等若干缺陷。本次发布由 25 位贡献者共同完成，是海洋与地球科学数据处理流水线的重要基础工具更新。', 'source': 'PyData / xarray', 'url': 'https://github.com/pydata/xarray/releases/tag/v2026.07.0', 'date': '2026-07'}, {'title': 'uxarray v2026.07.0 发布：非结构化网格海洋与气候数据分析可视化扩展（2026-07-21）', 'badge': '[工具]', 'abstract': '作为 xarray 的非结构化网格扩展，uxarray v2026.07.0（2026-07-21 更新）为气候与全球天气非结构化数据（UGRID、SCRIP、Exodus、shapefile 等格式）提供类 xarray 的读取与分析函数，由 Project Raijin（NCAR 与宾州州立）与 SEATS 项目（阿贡国家实验室等）合作开发。新版本延续对非结构化网格数据集的标准分析支持，便于海洋与地球科学社区直接对非结构化网格数据开展标准化处理与可视化。', 'source': 'UXARRAY / Project Raijin', 'url': 'https://anaconda.org/conda-forge/uxarray', 'date': '2026-07-21'}]}]

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
