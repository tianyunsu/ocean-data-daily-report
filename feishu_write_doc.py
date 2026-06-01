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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'FuXi-Ocean：首个达到6小时分辨率与涡旋分辨率的深度学习全球海洋预报模型（npj Climate and Atmospheric Science, 2026-05-30）', 'badge': '近7天', 'abstract': '由复旦大学、上海科学人工智能研究院、天津大学、海南热带海洋学院联合团队在Nature Portfolio旗下期刊npj Climate and Atmospheric Science发表。FuXi-Ocean是首个数据驱动的全球海洋预报模型，实现每6小时一次、1/12°（约8 km）的涡旋分辨率预报，深度覆盖至1500米。模型采用多时间窗融合策略，在温度、盐度、海流、海面高度等关键海洋变量上全面超越传统动力模式，而推理速度提升数个数量级。论文于2026年5月30日在线发表，标志着数据驱动的全球海洋预报正式进入"业务化可用"阶段。', 'source': 'npj Climate and Atmospheric Science (Nature Portfolio)', 'url': 'https://www.nature.com/articles/s41612-026-01444-2', 'date': '2026-05-30'}, {'title': 'CMEMS"理解我们的海洋"系列III发布：AI与机器学习如何赋能海洋预报（Copernicus Marine, 2026-05-29）', 'badge': '近7天', 'abstract': '哥白尼海洋服务（CMEMS）发布科普系列第三篇，聚焦海洋预报技术与实践。文章系统介绍了数据同化、数值模型与AI/ML技术在海洋预报中的协同应用：人工神经网络技术显著提升了海洋热浪检测与预报能力；TARDIS项目结合数据同化与AI重建北极海冰厚度历史数据（追溯至1991年），生成TOPAZ4-ML数据集；机器学习还应用于洋流模型构建与卫星观测解读（如识别微塑料斑块）。文章预告下一系列将探讨海洋数字孪生技术。', 'source': 'Copernicus Marine Service (CMEMS)', 'url': 'https://marine.copernicus.eu/news/understanding-our-ocean-iii-predicting-ocean', 'date': '2026-05-29'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': []}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': []}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': []}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': []}, {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': '2026年度IOOS数据管理与网络基础设施（DMAC）会议将于6月2-4日在Silver Spring召开（IOOS, 2026年5月）', 'badge': '近7天', 'abstract': '美国综合海洋观测系统（IOOS）年度DMAC会议将于6月2-4日在马里兰州Silver Spring举行，线上线下同步开放。会议汇集IOOS 11个区域协会、联邦机构、学术界和私营部门代表，核心议题包括海洋数据搜索与发现、元数据互操作性、云端数据分发架构及数据管理框架演进。议程草案已于5月初发布，是了解美国海洋数据管理最新实践的重要窗口。', 'source': 'IOOS / NOAA', 'url': 'https://ioos.noaa.gov/project/dmac/', 'date': '2026-05'}, {'title': 'PacIOOS重获RCOS认证 + CeNCOOS发布2026-2030战略计划 + IOOS HF雷达历史数据完成NCEI归档（IOOS, 2026年5月）', 'badge': '1周~1个月', 'abstract': '三项海洋数据管理重要进展：(1) 太平洋岛屿海洋观测系统（PacIOOS）成功重新获得IOOS区域沿海观测系统（RCOS）认证，有效期5年，确认其数据管理实践符合联邦标准；(2) 加州中部与北部海洋观测系统（CeNCOOS）发布2026-2030年战略与实施计划，为未来五年区域海洋数据管理与服务能力建设提供路线图；(3) 美国国家环境信息中心（NCEI）已完成从CORDC服务器检索并归档IOOS高频地波雷达（HF Radar）项目全部历史数据，确保十余年近海表层海流观测数据的长期保存与FAIR化可发现性。', 'source': 'IOOS / PacIOOS / CeNCOOS / NCEI', 'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-may-2026/', 'date': '2026-05'}]}, {'title': '七、开放航次/船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': []}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers / Data Archives / Data Repository', 'items': []}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': []}]

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
