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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'Neptune：CNN+球面傅里叶神经算子构建的全球海洋—海冰次季节 AI 模拟器，可稳定预报 60 天（arXiv, 2026-09-08）', 'badge': '[论文]', 'abstract': '次季节至季节（S2S）预报对水资源、农业、防灾、能源与保险等领域至关重要，但传统物理海洋环流模式（OGCM）计算昂贵、代码复杂难以迭代。来自欧洲地中海气候变化中心（CMCC）、哥伦比亚大学等机构的团队提出 Neptune——面向 S2S 尺度的端到端数据驱动全球海洋与海冰分量模拟器。它结合卷积神经网络捕捉局地特征与球面傅里叶神经算子（SFNO）刻画全球跨尺度相互作用，在给定逐日大气强迫下，逐日输出温度、盐度、经向/纬向流、海表高度、混合层深度以及海冰厚度与密集度（含整个水柱剖面）。团队以 ORAS5 海洋再分析预训练 1° 的 Neptune-1，再微调得到 0.25° 的 Neptune-025。在 RMSE、CRPS、ACC 等统计指标，海洋热含量、涡动能、海冰 Brier 评分等物理一致性指标，以及 ENSO/Z20、IOD 等气候指数上，Neptune 均能稳定再现海洋场 60 天的时空演变，证明端到端数据驱动海洋模拟器可成为下一代 S2S 预报系统的核心组件。', 'source': 'arXiv (physics.ao-ph / cs.AI)（CMCC + Columbia）', 'url': 'https://arxiv.org/abs/2609.08606', 'date': '2026-09-08'}, {'title': '"丝路海运"北极航线气象导航服务正式启用：风云卫星+AI 提供未来 15 天逐日海冰预报（中国经济网, 2026-09-08）', 'badge': '[要闻]', 'abstract': '第八届"丝路海运"国际合作论坛在厦门开幕，19 个国家和地区 1800 余名代表参会。论坛宣布"丝路海运"北极航线气象导航服务正式启用。该服务由中国气象局与"丝路海运"联盟联合打造，依托风云气象卫星建立北极海冰观测网络，融合数值预报与人工智能算法，提供未来 15 天逐日海冰预报及极地气旋动态监测，破解极地观测覆盖不足、数据滞后的难题，为船舶规避冰情、规划安全航线提供决策支撑。海杰航运已与"丝路海运"签署北极航线气象导航服务协议，其 2026 年度北极航线运营的全部 7 艘船舶将统一采用该服务，实现北极船队气象保障全覆盖，标志着我国气象导航服务在极地航区实现常态化保障的实质性突破。国家气象中心副主任肖潺介绍，"丝路海运"全球气象导航服务自 2021 年首次试用以来平均航线优化率达 30%。', 'source': '中国经济网 / 第八届"丝路海运"国际合作论坛', 'url': 'https://www.ce.cn/xwzx/gnsz/gdxw/202609/t20260909_3203412.shtml', 'date': '2026-09-08'}, {'title': 'SKANN：原始波形选择性核声学神经网络实现开放集跨航次船舶再识别（arXiv, 2026-09-07）', 'badge': '[论文]', 'abstract': '水下声学目标识别长期停留在"按船型分类"的闭集设定，无法回答监测系统"以前是否听过这条船"。研究形式化了开放集、跨航次船舶再识别任务，并给出一套堵住两条"刷分捷径"的评测协议：按 MMSI/IMO 划分船体互斥的训练/测试集、查询与候选库取自同一船体的不同航次、候选库保持信源纯净，并引入经人工裁决的航次去重闸门。所提出的 SKANN 是一个原始波形编码器，前端为四尺度可学习滤波器组、经选择性核注意力融合，以角度间隔损失训练，并在保持窄带线谱身份特征的前提下扰动记录链路、环境噪声与多途。在 40 条船的 IARA 候选库（96 次查询、98 个航次候选）上，跨航次 rank-1 为 0.25（嵌入）与 0.26（自动窄带线谱比较器），两者融合达 0.35；嵌入排序可靠性更高（AUC 0.82 对 0.76）。作者强调该结果支持"分析员按排序短名单分流"而非直接身份认定，并指出仅航次去重一项就消除 16–21 个百分点的虚假 rank-1 优势。检查点、验证嵌入与逐查询输出以 CC-BY-4.0 发布。', 'source': 'arXiv (cs.SD / eess.AS)', 'url': 'https://arxiv.org/abs/2609.07399', 'date': '2026-09-07'}, {'title': '把视觉基础模型适配到声呐：首次实现无位姿的三维声呐重建（arXiv, 2026-09-05）', 'badge': '[论文]', 'abstract': '在浑浊、低能见度水域，基于互联网 RGB 数据训练的视觉基础模型难以直接适用；而声呐领域缺乏公开大规模数据集，从零训练声呐基础模型不现实。研究提出两条适配路径：一是利用视觉与声呐两种传感模态之间的几何关系，二是采用精确的物理噪声模型生成合成数据。由此得到的声呐适配模型首次在实验中实现了基于声呐的无位姿三维重建——即无需预先知道传感器位姿即可从声呐序列恢复三维场景，为水下机器人在光学失效环境下的场景理解提供了新能力。', 'source': 'arXiv (cs.CV)（CMU / UMD / Johns Hopkins 等）', 'url': 'https://arxiv.org/abs/2609.06261', 'date': '2026-09-05'}, {'title': 'One Model, Two Worlds：方向非对称 realism 桥实现单一模型的双向声呐—光学翻译（arXiv, 2026-09-05）', 'badge': '[论文]', 'abstract': '成像声呐与光学相机之间的互译对水下感知很有价值，但两个方向各建一套模型会重复占用存储与算力。研究指出"共享生成模型"并不等于"共享成像物理"，提出方向非对称 realism 桥（DARB）：保留共享的扩散桥主干，同时按方向路由各自的物理先验——声呐转光学走距离感知调制，光学转声呐走极坐标射线相关处理。进一步发现训练上的对称同样代价高昂：统一的 realism 调度会使声呐转光学 PSNR 下降 2.60 dB，为此提出自适应 realism 监督（ARS），依据重建质量与梯度平衡决定感知监督的时机、位置与强度。最终单一双向模型在声呐转光学上与专用模型相差仅 0.11 dB PSNR，在光学转声呐上以 0.70 FID 优于专用模型，并在八项指标中的七项超过两个独立训练的 BBDM。', 'source': 'arXiv (cs.CV)', 'url': 'https://arxiv.org/abs/2609.06253', 'date': '2026-09-05'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '本期暂无符合时效要求的海洋数字孪生新增动态', 'badge': '[备注]', 'abstract': '欧盟 OCEANITY/EDITO、Fugro 新加坡枢纽等数字孪生海洋进展已于 09-04、09-07、09-08 各期收录；本期检索未发现 9 月 2 日之后发布的海洋数字孪生新平台、新架构或新应用案例，故本方向留空，不以旧素材凑数。', 'source': '—', 'url': '', 'date': '2026-09-09'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Data Visualization', 'items': [{'title': '"丝路海运"港口气象风险智能体：国内外 58 座港口气象风险集中展示，据称为国际首创（国务院国资委, 2026-09-09）', 'badge': '[动态]', 'abstract': '福建港口集团联合厦门市气象局打造"丝路海运"港口气象风险智能体，将国内外 58 座港口的气象风险集中呈现在同一视图中，集成风险等级、距台风中心距离、封航开港状态等关键信息，让港口、航运、贸易、保险等上下游环节快速掌握多港口态势，大幅降低协同决策成本。福建港口集团董事长陈志平表示，该智能体在国际上尚属首创，下一步将持续打磨并接入更多"一带一路"港口，同时推动智能体与全球气象导航服务深度融合——智能体管港口作业、导航管海上航行，实现从海上到陆端的全链条覆盖。', 'source': '厦门日报 / 第八届"丝路海运"国际合作论坛', 'url': 'http://www.sasac.gov.cn/n2588025/n2588129/c35891784/content.html', 'date': '2026-09-08'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality (QA/QC)', 'items': [{'title': '水域时间序列异常检测的机器学习综述：覆盖 106 篇文献，聚焦变量本身的异常（Water 18(17) 2209, 2026-09-05）', 'badge': '[论文]', 'abstract': '水域相关时间序列的异常检测往往能揭示重要环境问题，也是科学发现的起点，机器学习已成为该领域主流方法与研究热点。来自生态环境部南京环境科学研究所、天津市政工程设计研究总院与西北工业大学无人系统研究院的团队系统评述了 Web of Science 近十年 106 篇研究。与既有综述不同，本工作聚焦"由水域变量本身产生的异常"而非设备故障引起的异常，从发展阶段与异常检测范式两个维度对机器学习异常检测模型进行分类，剖析各类范式的机制、优势、局限与应用场景，并指出当前挑战与未来方向。对海洋观测数据质控而言，区分"真异常"与"仪器故障"正是二次 QC 的核心难题，该分类框架具有直接参考价值。', 'source': 'Water (MDPI)', 'url': 'https://www.mdpi.com/2073-4441/18/17/2209', 'date': '2026-09-05'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': '图神经网络用于海图变化关键性分类的适用性评测（arXiv, 2026-09-02）', 'badge': '[论文]', 'abstract': '电子海图（ENC）更新数据量大，但真正影响航行安全的变化只占少数。研究系统评测图神经网络在"海图变化关键性分类"任务上的表现，将海图要素及其空间关系建模为图结构，判断某项更新是否属于需优先处理的关键变更。这类方法可帮助海道测量机构在有限的更新产能下优先推送高危变更，是海洋空间数据自动化处理链条上的实用环节。', 'source': 'arXiv (cs.LG)', 'url': 'https://arxiv.org/abs/2609.02996', 'date': '2026-09-02'}, {'title': '小批量风险规避深度 Q 学习：以水下机器人导航为案例的风险敏感控制（arXiv, 2026-09-07）', 'badge': '[论文]', 'abstract': '研究针对马尔可夫决策过程提出一种风险敏感控制方法——策略优劣不再以期望折扣代价评价，而是以动态、时间一致的马尔可夫风险度量评价，从而让智能体在训练与执行阶段都显式规避尾部风险。论文以水下机器人导航为案例研究：洋流扰动与定位不确定性使水下导航的代价分布具有重尾特征，仅优化期望回报会导致策略在少数高风险情形下失效。该方法为自主水下平台的可靠决策与轨迹规划提供了风险感知的新工具。', 'source': 'arXiv (cs.LG / eess.SY)', 'url': 'https://arxiv.org/abs/2609.07998', 'date': '2026-09-07'}]}, {'title': '六、数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'Coastal & Ocean Resilience Data Collaborative 获"海洋十年"认可：开放数字公共基础设施整合南亚东南亚沿海数据（UNESCO IOC, 2026-09-04）', 'badge': '[政策]', 'abstract': '由联合国教科文组织支持、CivicDataLab 牵头的"沿海与海洋韧性数据协作体"（CORD）获得"海洋十年"Ocean Practices for the Decade 计划认可。CORD 面向南亚与东南亚，建设开放的数字公共基础设施，把来自政府机构、区域组织与社区的海洋学、气象、社会经济、基础设施、金融及公民上报数据标准化并打通互操作，提供近实时的灾害、脆弱性与暴露度洞察。项目与渔业社区、海员、公民社会、学界及政府机构共同创建，强调以负责任的 AI 与分析直接支撑基础设施规划、公共融资、健康保障与气候适应，而非止步于仪表盘。2026 年 7 月 CORD 团队与海洋十年数据共享协调办公室会晤，为其接入负责任 AI 与数据共享实践社群、参与 2027 蓝色蓝图对话，并对接 INCOIS/NODC、Argo 等数据仓储铺平道路。', 'source': 'UNESCO 政府间海洋学委员会（IOC）', 'url': 'https://www.ioc.unesco.org/en/articles/ocean-decade-endorsement-accelerates-partnerships-and-data-sharing-coastal-resilience', 'date': '2026-09-04'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Ocean Exploration', 'items': [{'title': '"深海一号"科考船搭载"蛟龙"号从青岛起航，奔赴深海执行新一轮科考任务（人民日报, 2026-09-06）', 'badge': '[航次]', 'abstract': '9 月 6 日，山东青岛，搭载"蛟龙"号载人潜水器的"深海一号"科考船顺利出港，奔赴深海执行新一轮海洋科考任务。"蛟龙"号是我国自主研发的 7000 米级载人潜水器，可覆盖全球 99.8% 海域，能够完成深海探测、样本采集、地质勘查等作业；"深海一号"作为专业科考母船，设备先进、续航强劲，为深潜作业提供全方位海上支撑。青岛海事局提前部署专项保障，对"深海一号"开展全方位船舶安全检查，重点核查导航、动力、应急救生及科考配套设备运行状态并跟踪闭环整改，同时维护航道通航秩序、发布安全预警，保障科考船舶顺利启航。', 'source': '人民日报 / 人民网', 'url': 'https://kpzg.people.com.cn/n1/2026/0908/c404214-40794387.html', 'date': '2026-09-06'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers & Repositories', 'items': [{'title': 'EastAsiaClimateExtremes：面向次季节预测的东亚大气—海洋极端事件 AI-Ready 数据集（arXiv, 2026-09-08）', 'badge': '[数据]', 'abstract': '尽管基于 AI 的气候极端事件预测备受关注，但以"事件/标签"形式组织的 AI-Ready 极端气候数据集仍然稀缺，制约了对这类现象的系统刻画与预报。该数据集基于 ERA5 再分析与 OISST 海表温度，提供东亚区域异常高温（AHT）、强降水（HR）与海洋热浪（MHW）三类极端事件的周尺度极端标签与事件型评价指标，并配套托管在 GitHub 的分析工作流以支持复现与适配。数据集与 ECMWF S2S 回报（hindcast）输出在同一空间网格与时间框架上配准，可直接比对再分析衍生标签与动力模式预报，既支持定量刻画区域极端的时空发生特征，也可系统诊断 S2S 模式的预报技巧，并拓展至极端事件归因与复合风险分析。', 'source': 'arXiv (physics.ao-ph)', 'url': 'https://arxiv.org/abs/2609.08241', 'date': '2026-09-08'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'cstar-ocean 发布 0.13.5：海洋碳循环可复现建模工作流工具（PyPI / conda-forge, 2026-09-05）', 'badge': '[工具]', 'abstract': 'C-Star（包名 cstar-ocean）发布 0.13.5 版本。该项目由 C]Worthy 开发，通过蓝图驱动、具备编排感知能力的 Python API 与命令行工具，自动化搭建并执行可复现的海洋碳建模工作流（ROMS-MARBL 及相关的区域海洋/生物地球化学模拟）。除常规安装外，项目在 conda-forge 上提供 cstar-ocean-standalone，捆绑编译器、MPI、netCDF-Fortran、PnetCDF 与 CMake 完整工具链，使 ROMS 无需系统依赖即可编译。项目采用 Apache-2.0 许可，文档托管于 Read the Docs。此前日报已收录 v0.6.0 与 v0.8.0，本次 0.13.5 为跨多个小版本的新版本更新。', 'source': 'PyPI / conda-forge（C]Worthy）', 'url': 'https://pypi.org/project/cstar-ocean/', 'date': '2026-09-05'}]}]

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
