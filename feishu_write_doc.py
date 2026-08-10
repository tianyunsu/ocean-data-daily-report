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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': '中国科协年会“面向可持续发展的海洋系统AI大模型与知识融合”专题论坛在京举办（2026-07-28）', 'badge': '[动态]', 'abstract': '第二十八届中国科协年会专题论坛于 7 月 28 日在京举办，由中国科协主办、中科院海洋所等承办，60 余位学者参会。该所所长王凡做主旨报告《面向未来的海洋大数据与人工智能海洋学》，系统回顾团队从搭建人工智能海洋学理论框架到成立海洋人工智能交叉研究中心的历程，提出下一步将研发“多智能体协同大模型、构建全场景海洋智慧预测决策体系”的战略目标。论坛集中展示了琅琊 1.0-2.0、飞鱼 1.0 海气耦合大模型、卫星遥感智能预测、海洋环流智能预报、海洋知识图谱等创新成果，探索知识-数据-物理融合驱动海洋复杂系统计算的创新方法论。（距今天 13 天，在时效内）', 'source': '中国科学院海洋研究所 / 中国科协', 'url': 'https://csol.qdio.ac.cn/portal/article/index.html?id=3596&cid=12', 'date': '2026-07-28'}, {'title': '端到端视觉控制框架实现UUV实时自主定位、导航与三维建图（arXiv, 2026-08-05）', 'badge': '[论文]', 'abstract': 'arXiv:2608.04723 由 SINTEF 等团队提出一个完整的视觉驱动自主水下航行器（UUV）框架，集成实时鲁棒定位、自主导航与环境三维建图能力，支持网箱相对定位与全局定位两种模式。框架在合成数据集（含地面真值）上验证并通过搭载实测，在动态视觉挑战环境中展现实时性能与强鲁棒性，为水下关键设施巡检与测绘任务的现场部署提供了可迁移的视觉自主方案。论文源自挪威水产养殖网箱巡检场景的实际需求。', 'source': 'arXiv:2608.04723 (cs.RO)', 'url': 'https://arxiv.org/abs/2608.04723', 'date': '2026-08-05'}, {'title': '占位-规划-学习统一框架实现部分可观测下UUV鲁棒水下导航（arXiv, 2026-08-05）', 'badge': '[论文]', 'abstract': 'arXiv:2608.05365 提出一种仅依赖机载观测（声纳+深度图像）的 UUV 自主框架，融合持续性占位图构建、全局航路隙感知规划器与风险感知局部强化学习控制器，并通过行为树蒸馏与不确定性校准蒸馏机制提升训练安全性与稳定性。在 NVIDIA Isaac Sim 高保真 GPU 加速仿真中进行多种子可复现评估，较纯行为树基线与标准 RL 基线在动态条件下表现出更强的鲁棒性与安全性，为部分可观测水下环境的通用 UUV 自主架构提供基准。', 'source': 'arXiv:2608.05365 (cs.RO)', 'url': 'https://arxiv.org/abs/2608.05365', 'date': '2026-08-05'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin / Marine Digital Twin', 'items': [{'title': '本周暂无明显进展', 'badge': '[备注]', 'abstract': '近期海洋数字孪生方向暂无重大新发布。港科大 WavyOcean 3.0（07-10 发布）、欧盟 DestinE 第三阶段（07月）、DITTO Summit 2026 早鸟注册与议程公布（07-30）均已在近期日报收录（2026-07-13/07-31/08-03/08-07）。', 'source': '', 'url': '', 'date': '2026-08-10'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization / Marine Data Visualization', 'items': [{'title': '本周暂无明显进展', 'badge': '[备注]', 'abstract': '近期海洋可视化方向暂无重大新工具发布。Copernicus Marine 产品路线图预告的 MyOcean Pro 3D Viewer（计划 2027-01）已在 08-03 日报收录，MyOcean Health 实时海洋状态图表已收录于 07-01/08-03。', 'source': '', 'url': '', 'date': '2026-08-10'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA-QC', 'items': [{'title': '机器学习辅助+物理引导的事件感知QC框架：保留真实涌升/台风信号，只剔除传感器异常（JMSE, 2026-08-08）', 'badge': '[论文]', 'abstract': '发表于 Journal of Marine Science and Engineering（14(16):1462）的研究，针对韩国东海岸 6 个浮标 2008-2024 年的 30 分钟温度记录，构建了一套“事件保留型”质量控制框架：用台站级岭回归模型残差粗筛异常候选，再用空间一致性（相邻浮标）、垂向一致性（不同水层）与大气强迫（ERA5+台风最佳路径）三个物理可解释轴做精细分类。结果显示，纯残差无法有效分离传感器异常与真实事件（AUC 仅 0.52-0.56），而物理轴的多变量交叉验证 AUC 达 0.987，保留了涌升致冷 8 °C 的事件信号，仅影响月均值约 0.0005 °C。该框架为业务化浮标 QC 提供了可解释、可追溯的事件感知新范式。', 'source': 'JMSE (MDPI) 14(16):1462', 'url': 'https://www.mdpi.com/2077-1312/14/16/1462', 'date': '2026-08-08'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'AUV海底图像AI远程感知：近40万倍数据压缩实现低带宽卫星通信下的实时态势认知（arXiv, 2026-07-30，豁免）', 'badge': '[论文]', 'abstract': 'arXiv:2607.18013 由南安普顿大学、MBARI 等团队提出一种 AUV 海底图像实时处理与低带宽传输方法：利用 AI 技术从大批量图像中自动筛选最具代表性的子集，或按查询返回最相似图像，结合图像元数据压缩后通过卫星通信（如 Iridium SBD，44 字节/秒）或水声调制解调器回传，让岸上操作员在 AUV 仍在部署中即可了解采集图像的类型与质量。英国近海与加那利群岛三次海上实测验证：2 小时 47 分钟的测绘任务数据经近 40 万倍压缩，仅 34 分钟即完成低带宽传输，为远洋 AUV 任务中实时决策与自适应采样提供关键能力。（豁免：超 14 天（约 26 天），顶级机构+不重复；此工作与 07-24 日报收录的 arXiv 低带宽传输论文为不同技术路线）', 'source': 'arXiv:2607.18013 / SAMS / MBARI', 'url': 'https://arxiv.org/abs/2607.18013', 'date': '2026-07-30'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '青岛发布全国首个海洋公共数据团体标准：《分类分级指南》+《目录编制规则》落地（2026-08-06）', 'badge': '[政策]', 'abstract': '2026 年 8 月 6 日，第二期青岛市数据要素成果发布会上重磅发布《海洋公共数据分类分级指南》与《海洋公共数据资源目录编制规则》两项团体标准，由青岛市海洋发展局、青岛数据集团等联合起草，是全国首个针对海洋公共数据领域的专项标准化成果。《分类分级指南》构建“行业领域-业务职能-内容主题”三级分类体系，按数据损毁影响程度将海洋公共数据分为核心、重要、一般共六级，配套差异化安全保护与开发利用规则；《目录编制规则》搭建覆盖共享、开放、授权运营三类目录的完整元数据体系。两项标准形成“分类分级定规则、目录编制明底数”的海洋公共数据治理闭环，为跨部门共享、社会化开放与市场化运营提供统一数据语言。', 'source': '青岛市大数据发展促进会 / 海洋知圈', 'url': 'https://www.163.com/dy/article/L3P5FOVJ0511KMS0.html', 'date': '2026-08-06'}, {'title': '联合国“海洋十年”第 11 轮行动征集启动，项目申请截止 2026-08-31', 'badge': '[动态]', 'abstract': 'UNESCO/IOC 正式发布“海洋十年行动征集（Call for Decade Actions No. 11/2026）”，面向全球科研机构、政府部门及相关利益攸关方开放。本轮围绕《巴塞罗那宣言》优先领域，征集三类申请：大科学计划（Programme）意向书（截止 5/31）、项目（Project，截止 8/31）与捐助（Contribution，全年开放、建议 8/31 前提交）。截至目前海洋十年已实施 62 个大科学计划与 657 个项目、累计超 133 项资源投入。该征集为海洋数据共享与国际合作提供了重要的制度化通道。', 'source': 'UNESCO-IOC / 海洋十年 OSF', 'url': 'https://www.osf-un-ocean-decade.cn/cn/news/news-detail-14949.htm', 'date': '2026-08-10'}]}, {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [{'title': 'NOAA Okeanos Explorer EX2605 库克群岛ROV探险进入最后阶段，已完成超12次深海下潜（2026-07-19 至 08-13，更新）', 'badge': '[航次]', 'abstract': 'NOAA 与库克群岛海底矿物管理局合作的 26 天深海探险（7/19-8/13）进入收官周。截至 8 月 9 日已完成 Dive 13（Northern Boundary Seamount，水深 2800 m 海山岩脉），此前 12 次下潜覆盖了 5400 m 深渊平原、海底峡谷、海山等生境类型，对深海珊瑚、多金属结核、海参、玻璃海绵等做了系统性影像记录与有限取样。ROV 双机（Discoverer + Seirios）配合多波束测绘与 Argo 浮标部署，全程遥现直播，为库克群岛海洋资源管理决策提供科学基础。（更新：前次收录于 07-16/07-31）', 'source': 'NOAA Ocean Exploration', 'url': 'https://origin.oceanexplorer.noaa.gov/expedition/ex2605/', 'date': '2026-08-09'}, {'title': 'E/V Nautilus NA180 马里亚纳深Ⅱ航次即将结束，NA181“威克岛深海探索”8月20日接力启航（2026-08-16 / 08-20）', 'badge': '[航次]', 'abstract': "OET 2026 航季第三航次 NA180“Deep-Sea Habitats in the Mariana Islands II”（7/25-8/16）即将返航，该航次聚焦马里亚纳东北部专属经济区深渊平原生境，ROV Hercules + AUV Sentry 联合作业，并部署 NOAA PIFSC 高频声学记录包用于鲸类监测。第四航次 NA181“Exploration of Wake Island's Deep Sea”将于 8/20 从关岛启航前往威克岛（9/18 檀香山结束），30 天测绘+ROV+Argo 浮标部署，NA181 详细计划已于 08-07 日报报道。（NA180 首次收录于 07-28）", 'source': 'Ocean Exploration Trust / NOAA', 'url': 'https://nautiluslive.org/expedition', 'date': '2026-08-16'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': '本周暂无明显进展', 'badge': '[备注]', 'abstract': '近期海洋数据中心方向暂无重大新发布。GEBCO_2026 网格（28.7% 覆盖率，04-08 发布）、CMEMS 2026 年 7 月服务发布（新 MFC 入网，07-07）、Copernicus Marine 产品路线图更新（MyOcean Pro 3D 等）均已在前期日报收录。', 'source': '', 'url': '', 'date': '2026-08-10'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': 'raschii v2.0.1 发布——非线性规则波理论 Python 库持续维护（PyPI, ~2026-08，豁免）', 'badge': '[工具]', 'abstract': '非线性规则波理论 Python 库 raschii 在 v2.0.0（07-07）基础上发布 v2.0.1 维护更新，修复若干稳定性问题。raschii 实现 Stokes 2-5 阶与 Fenton 流函数等非线性波浪理论，新增向量化计算与流体粒子加速度支持，广泛应用于海洋工程波浪载荷与水动力分析。作为海洋波浪建模开源工具链的基础组件，v2.0.0 与 wavespectra v4.8.0 共同覆盖谱分析至非线性规则的完整波浪数据处理链路。（豁免：超 14 天，v2.0.0 原始发布日为 2026-07-07，本次为维护更新）', 'source': 'PyPI / GitHub', 'url': 'https://pypi.python.org/project/raschii/', 'date': '2026-08-07'}, {'title': 'wavespectra v5.0 即将发布：重大架构升级（谱变换返回 Dataset 保留非谱变量）', 'badge': '[工具]', 'abstract': '海洋波谱分析 Python 库 wavespectra v5.0.0 版本已在 CHANGELOG 中发布变更日志（v5.0.0 未正式 release，为 unreleased 状态）。该版本带来重大 API 升级：从 Dataset 访问器调用谱变换方法（插值、拆分、旋转、分区等）时默认返回携带非谱变量（wspd, wdir, dpt）的完整 Dataset，此前该行为仅在 v4.7.0 作为可选功能，解决了谱变换后环境变量静默丢失的痛点；同时移除 Python 3.9 支持，最低要求 Python 3.10。v4.8.0（07-23）已收录于 07-28 日报。', 'source': 'wavespectra / GitHub', 'url': 'https://wavespectra.readthedocs.io/en/latest/history.html', 'date': '2026-08-10'}]}]

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
