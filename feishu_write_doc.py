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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'OCEANS 2026国际海洋技术大会三亚开幕：海洋AI成为核心专题方向（中国日报 / IEEE OES, 2026-05-26）', 'badge': '近7天', 'abstract': '5月26日，全球海洋工程与科技领域旗舰会议OCEANS 2026在海南三亚启幕。大会以"走向深蓝"为主题，汇聚全球26个国家和地区近750名专家学者、行业精英。海洋人工智能（AI）被列为核心专题之一，来自美国、丹麦、中国等国的专家围绕物理驱动机器学习、AI驱动的海洋感知与预报等议题发表主旨报告。大会设深海探测、海洋AI、水下传感器网络、海上风电、极地观测等6大专题方向，51家海内外参展商集中展示。海南大学作为继上海交通大学之后第二所获得该会议主办权的中国大陆学术机构。', 'source': '中国日报 / IEEE OES', 'url': 'https://news.qq.com/rain/a/20260527A03QJY00', 'date': '2026-05-26'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': []}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': 'Copernicus Marine海洋空间规划数据可视化平台v1.0-beta发布：交互式3D卫星数据可视化（GitHub, 2026-05-24）', 'badge': '近7天', 'abstract': '面向海洋空间规划的开源数据可视化平台v1.0-beta在GitHub发布（Copernicus Marine DataViz Challenge参赛项目）。该平台旨在降低海洋数据使用门槛，将复杂的卫星观测数据转化为直观的三维可视化，并集成对话式AI辅助分析功能。面向研究人员、学生和海洋管理者，支持Copernicus Marine等海洋数据源的可视化分析，推动海洋数据民主化与开放科学实践。', 'source': 'GitHub / Copernicus Marine DataViz Challenge', 'url': 'https://github.com/ROYCEFTC/Marine-Spatial-Planning-Application---DataViz-Challenge2026/releases', 'date': '2026-05-24'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': []}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': 'OceanSR-Prob：基于扩散模型的全球海洋风速空间降尺度方法（Neurocomputing, 2026-05-22）', 'badge': '近7天', 'abstract': '发表于Neurocomputing期刊，提出OceanSR-Prob生成式扩散框架，用于全球海洋风速剖面的空间降尺度。该方法通过概率建模捕捉海洋风速的多尺度空间变异性，克服传统降尺度方法过度平滑和高分辨率细节丢失的局限。在多个分辨率下（从0.25度降至更精细区域尺度）验证，优于现有插值和统计降尺度基线方法，为高分辨率海气耦合模型和海上风电评估等应用提供可靠的数据预处理工具。', 'source': 'Neurocomputing (Elsevier)', 'url': 'https://www.sciencedirect.com/science/article/pii/S0925231226014669', 'date': '2026-05-22'}]}, {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'PACE Data Hackweek开放科学实践报告：两次Hackweek的经验与启示（Oceanography, 2026-05-19）', 'badge': '1周~1个月', 'abstract': '发表于Oceanography期刊的开放科学论文，系统总结了两届NASA PACE（浮游植物、气溶胶、云和海洋生态系统）Data Hackweek的目标、成果和参与者经验。两届Hackweek共为数百名研究人员提供了PACE卫星高光谱海洋颜色数据的实操培训，推动了开放科学协作模式在海洋遥感数据处理中的应用，并探讨了数据访问、培训基础设施和社区建设等持续挑战，为类似海洋数据培训项目提供了参考框架。', 'source': 'Oceanography (The Oceanography Society)', 'url': 'https://tos.org/oceanography/article/the-pace-data-hackweek-launches-a-new-wave-of-open-science-how-we-did-it-twice-and-why', 'date': '2026-05-19'}]}, {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': []}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'CMEMS推出"理解我们的海洋II：收集海洋数据"科普系列（Copernicus Marine, 2026-05-26）', 'badge': '近7天', 'abstract': 'Copernicus Marine Service（CMEMS）发布"Understanding Our Ocean"科普系列第二篇《收集海洋数据》，系统介绍海洋数据的多种采集方式，包括卫星遥感（海面温度、海面高度、海洋颜色）、原位观测（Argo浮标、漂流浮标、锚系阵列、科考船CTD）、滑翔机和水下滑翔器等平台。文章帮助数据用户理解CMEMS数据来源和质量控制流程，是CMEMS提升全球海洋数据素养与用户服务能力的系列举措之一。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/news/understanding-our-ocean-ii-collecting-ocean-data', 'date': '2026-05-26'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': []}]

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
