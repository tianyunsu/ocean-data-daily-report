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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'Digital Ocean Week开幕——AI Ocean Forum发布2030年海洋AI路线图（Mercator Ocean / Copernicus Marine, 2026-06-11）', 'badge': '[要闻]', 'abstract': '首届Digital Ocean Week（6月8-12日，布鲁塞尔）于6月11-12日举行为期两天的AI Ocean Forum，汇集政策制定者、科学家、行业和技术专家，聚焦AI在海洋观测、预测和决策支持中的新应用。核心成果包括发布2030年海洋AI路线图，规划欧洲数字海洋社区AI应用的共同方向，涵盖机器学习在海洋预报中的嵌入、AI驱动数据界面和跨平台互操作。论坛由Mercator Ocean International主办，系OceanEye倡议从愿景到实施的关键组成部分。', 'source': 'Mercator Ocean International / Copernicus Marine Service', 'url': 'https://events.marine.copernicus.eu/digital-ocean-week', 'date': '2026-06-11'}, {'title': 'arXiv: PCA增强自适应NVAR框架实现东海高分辨率海表温度预测（2026-06-11）', 'badge': '[论文]', 'abstract': 'Sherkhon Azimov等（墨西哥/韩国联合团队）提出基于奇异值分解降维与自适应非线性向量自回归（NVAR）相结合的东海SST预测框架。方法先将SST场通过SVD压缩为低维表示以提取海洋变异主导模态，再由自适应NVAR建模潜在状态时间演变并重构预测。在多个预测时间范围内，自适应NVAR均优于传统NG-RC/NVAR方法，SVD降维同时降低了计算复杂度，使该框架适用于实时海洋预报。arXiv: 2606.12141。', 'source': 'arXiv (cs.LG)', 'url': 'https://arxiv.org/abs/2606.12141', 'date': '2026-06-11'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin / Marine Digital Twin', 'items': [{'title': 'CMEMS"理解我们的海洋"系列IV发布：数字孪生海洋——卫星数据+AI+海洋模型融合（Copernicus Marine, 2026-06-08）', 'badge': '[科普]', 'abstract': '哥白尼海洋服务发布科普系列第四篇，系统介绍了欧洲数字孪生海洋（EU DTO）的架构与实现路径。EU DTO融合卫星数据、多源传感器实时和历史观测、高级分析与海洋建模来模拟未来情景，并引入AI/机器学习融入海洋预报系统和AI驱动界面以降低使用门槛。平台由Copernicus Marine Service与EMODnet数据支撑，EDITO基础设施提供云计算与建模工具，目标于2030年全面运行，服务海洋保护和科学决策。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/news/understanding-our-ocean-iv-digital-twin-ocean', 'date': '2026-06-08'}, {'title': 'DITTO 2026国际峰会开放摘要提交——聚焦可互操作与用户驱动的海洋数字孪生（6月5日起，11月横滨举行）', 'badge': '[会议]', 'abstract': '联合国海洋十年认可的数字孪生海洋（DITTO）计划第三届国际峰会将于2026年11月11-13日在日本横滨举行，摘要提交已于6月5日开放（截止7月20日）。峰会设六大核心主题：数据观测与建模、数字基础设施与互操作性、AI自动化与优化、跨行业应用、运营系统与工业部署、集成地球-社会系统框架。峰会将汇集研究人员、政策制定者、行业领袖和技术创新者，推动可互操作的运营化海洋数字孪生技术发展。', 'source': 'JAMSTEC / DITTO / UN Ocean Decade', 'url': 'https://www.jamstec.go.jp/j/pr-event/ditto_summit2026/', 'date': '2026-06-05(开放)'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization / Marine Data Visualization', 'items': []}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': []}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': []}, {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '自然资源部发布《海洋数据开放共享目录（第二批，2026年6月）》（自然资源部, 2026-06-08）', 'badge': '[政策]', 'abstract': '6月8日（世界海洋日），自然资源部发布第二批海洋数据开放共享目录。在首批37项产品基础上更新了2024-2025年中国海洋观测标准数据集及全球海洋水文气象、水深地形整合数据集；新增10项全球海洋三维温盐、海流、海浪、气压等融合数据集和7项全球海洋水文气象统计分析产品。数据通过国家海洋大数据服务平台（海洋云）开放，首批目录已服务百余用户、提供数据服务超60万次、数据量100TB。', 'source': '自然资源部 / 新浪财经', 'url': 'https://finance.sina.com.cn/jjxw/2026-06-08/doc-iniasfpu5655873.shtml', 'date': '2026-06-08'}, {'title': 'Copernicus Marine Service七月发布预告：COLAB MFC加入，通过全球合作扩展海洋预报覆盖（CMEMS, 2026-06-05）', 'badge': '[数据产品]', 'abstract': '哥白尼海洋服务宣布2026年7月版本将新增COLAB监测与预报中心（MFC），通过国际数据交换合作模式将非哥白尼体系开发的高质量区域海洋预报纳入哥白尼产品目录。首个合作方为加拿大环境与气候变化部（ECCC），首个产品覆盖西北大西洋——从哈特拉斯角至拉布拉多南部（含墨西哥湾流分离区、纽芬兰大浅滩、圣劳伦斯湾等）。生产单元由西班牙NOW Systems运营，使用加利西亚超算中心（CESGA）HPC基础设施。此举开创了国际合作新模式，扩大全球覆盖和科学多样性。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/news/july-release-expanding-copernicus-marine-service-through-global-collaboration', 'date': '2026-06-05'}]}, {'title': '七、开放航次/船时共享', 'en': 'Open Cruises / Research Vessels / Marine Equipment', 'items': [{'title': '施密特海洋研究所旗舰科考航次：亚马逊海底峡谷浊流活动研究（R/V Falkor (too), 2026年5月17日-6月20日）', 'badge': '[航次]', 'abstract': 'Schmidt Ocean Institute 2026年"西南大西洋"系列航次中的"Underwater Avalanches in the Amazon Canyon"航次于5月17日至6月20日期间执行。研究船R/V Falkor (too)在亚马逊海底峡谷开展浊流活动及其对海底地貌和生态系统影响的调查。同期SOI还公布了2026全年共9个航次计划，覆盖南美至中大西洋海岭海域，聚焦中层透明生物多样性、副热带环流碳输出等前沿课题。', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/', 'date': '2026-05-17至2026-06-20'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers / Repositories', 'items': [{'title': 'GMRT v4.5.0发布：新版全球多分辨率地形数据整合23次新调查，新增GMRT Downloader工具（LDEO/Columbia, 2026年6月）', 'badge': '[数据产品]', 'abstract': '全球多分辨率地形合成数据（GMRT）发布v4.5.0版本。核心更新包括：升级GEBCO 2026底图、整合23次新增多波束调查数据覆盖大西洋/太平洋/南大洋/印度洋、新增来自OceanXplorer船的红海高分辨率网格数据。同步发布UNH-CCOM开发的GMRT Downloader工具（GitHub开源），支持批量下载多个高分辨率网格并合并为单一复合网格，已集成至多波束咨询委员会（MAC）规划工具中。', 'source': 'GMRT / LDEO, Columbia University', 'url': 'https://www.gmrt.org/about/news.php', 'date': '2026年6月'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': []}]

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
