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
SECTIONS = [
  {'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [
    {'title': 'AxiomOcean：预测上层海洋的三维垂直结构（arXiv, 2026-05-11）', 'badge': '近7天', 'abstract': '短期海洋预报能力很大程度上取决于上层海洋三维结构，但其垂直层次与跨层依赖关系在现有AI预报模型中往往被忽视，导致次表层特征过度平滑、强强迫条件下物理一致性弱。本研究提出AxiomOcean——一种显式保留水柱垂直层级结构与跨层依赖的全球AI海洋预报模型，在上层海洋三维结构预测上显著优于现有基线方法。', 'source': 'arXiv', 'url': 'https://arxiv.org/abs/2605.10455', 'date': '2026-05-11'},
    {'title': 'CMEMS：人工智能如何驱动下一代业务化海洋产品（2026-05-04）', 'badge': '近7天', 'abstract': 'Copernicus海洋服务全面披露AI技术业务化进展：深度学习将北极海冰浓度预报误差降低41%；神经网络实现近实时全球海面风场偏差校正；ANN显著提升北大西洋极端风暴期间波浪预报精度；4DVarNet算法实现多传感器海表温度重建。成果依托COSI、KAILANI、CERAINE等项目，正逐步从研究走向业务化运行。', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/news/how-artificial-intelligence-powering-next-generation-operational-marine-products', 'date': '2026-05-04'},
    {'title': '基于多气象因素与机器学习的南海SST短期与长期预测（Frontiers, 2026-05-13）', 'badge': '近7天', 'abstract': 'Frontiers in Marine Science发表研究，利用随机森林、XGBoost、LightGBM融合多气象变量对南海SST进行短期和长期预测，发现多元模型显著优于单一变量模型，随机森林表现最佳，总云量对长期SST预测贡献甚至超过盐度，有效预测期可达20个月以上。', 'source': 'Frontiers in Marine Science', 'url': 'https://www.frontiersin.org/articles/10.3389/fmars.2026.1820102/full', 'date': '2026-05-13'},
    {'title': '王军成院士：我国海洋观测正加快走向智能化（2026-05-13）', 'badge': '近7天', 'abstract': '中国工程院院士王军成在第五届人工智能海洋学论坛（济南）上指出，智能化观测以物联网、AI、大数据为支撑，应在传感器端实现数据融合，质量控制，误差修正和异常剔除，而非仅依赖后端分析，海洋观测智能化将大幅提升观测效率与数据质量。', 'source': '央视网 / 中国科学报', 'url': 'https://ocean.cctv.com/2026/05/13/ARTInpLweX9Y2iSnbK6U6Yhg260511.shtml', 'date': '2026-05-13'},
  ]},
  {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [
    {'title': '厦门大学柴扉教授团队：海洋数字孪生赋能蓝色经济创新综述（2026-02-26）', 'badge': '1周~1个月', 'abstract': '厦门大学柴扉教授联合多国专家系统梳理海洋数字孪生核心架构（数据、模型，分析、可视化与交互四大模块），综述其在水产养殖、海上风电、可持续航运、海洋防灾减灾、蓝碳及海洋旅游等蓝色经济核心领域的全生命周期应用，指出海洋数字孪生正推动从被动式数据分析向主动式预测型决策支持的范式跃迁。', 'source': '厦门大学海洋与地球学院', 'url': 'https://mel.xmu.edu.cn/info/1012/61071.htm', 'date': '2026-02-26'},
    {'title': '《海洋通报》海岸带时空智能与数字孪生专栏征稿启事（2026-05-08）', 'badge': '近7天', 'abstract': '自然资源部主管，国家海洋信息中心与中国海洋学会主办的《海洋通报》发布专栏征稿启事，围绕海岸带多模态数据治理、物理与AI融合的海洋时空建模、海岸带灾害预测预报、数字孪生赋能海岸带治理、流域-河口-近海连续体研究等9大方向征稿，编辑部开辟绿色通道加快审稿流程。', 'source': '国家海洋信息中心 / 中国海洋学会', 'url': 'https://www.nmdis.org.cn/c/2026-05-08/85285.shtml', 'date': '2026-05-08'},
  ]},
  {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': []},
  {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality / QA/QC', 'items': [
    {'title': 'JAMSTEC团队：基于路径签名的Argo剖面自动QC方法改进——ML融合提升检测稳健性（2026-04-29）', 'badge': '1周~1个月', 'abstract': 'JAMSTEC团队在Journal of Oceanography发表研究，改进基于路径签名的Argo自动质量控制方法并融入机器学习技术，使用2016年数据训练的模型在2017-2021年间表现稳健，能准确识别错误剖面并接近Argo数据中心水平，可快速生成中等质量数据集以填补实时数据发布与人工QC之间的时间空白。', 'source': 'Journal of Oceanography / Springer', 'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1', 'date': '2026-04-29'},
    {'title': 'BGC-Argo+：含二次质量控制的全球生物地球化学Argo浮标数据集（ESSD预印本, 2026-05-12）', 'badge': '近7天', 'abstract': '夏威夷大学团队在ESSD发表预印本，对截至2025年1月的2429个BGC-Argo浮标数据进行了自动与人工结合的异常值检测（重点针对O2、硝酸盐和pH值），并提供剔除异常值后的统一剖面和网格化数据存储库，是当前最大规模的经二次QC的BGC-Argo数据集合，讨论截止至2026年6月19日。', 'source': 'Earth System Science Data / Copernicus', 'url': 'https://essd.copernicus.org/preprints/essd-2026-311/', 'date': '2026-05-12'},
  ]},
  {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [
    {'title': 'GEOXYGEN：基于生物地球化学感知ML框架的全球长期溶解氧数据集（ESSD, 2026-05-12）', 'badge': '近7天', 'abstract': '复旦大学团队在ESSD发表GEOXYGEN数据集，利用分层建模框架融合物理和生物地球化学预测因子，生成1960-2024年、月均、0.5度x0.5度分辨率、覆盖0-5500m深度的全球溶解氧场，独立测试R2大于0.9，重建空间格局与World Ocean Atlas 2023气候态高度一致，为气候系统模型中溶解氧表征提供一致且物理约束的基准。', 'source': 'Earth System Science Data / 复旦大学', 'url': 'https://essd.copernicus.org/articles/18/3125/2026/', 'date': '2026-05-12'},
    {'title': '基于多气象因素与机器学习的南海SST多时间尺度预测研究（Frontiers, 2026-05-13）', 'badge': '近7天', 'abstract': 'Frontiers in Marine Science发表研究，系统评估RF、XGBoost、LightGBM三种ML算法在南海SST短期和长期预测中的表现，结合总云量、风速、气温、盐度等多元驱动因子，发现多元模型显著优于单一变量模型，RF整体最佳，总云量对长期SST预测贡献超过盐度，有效期达20个月以上。', 'source': 'Frontiers in Marine Science', 'url': 'https://www.frontiersin.org/articles/10.3389/fmars.2026.1820102/full', 'date': '2026-05-13'},
    {'title': 'Euro-Argo ERIC：Argo叶绿素数据将于2026年6月起全面重新处理和重新分发', 'badge': '近7天', 'abstract': 'Euro-Argo ERIC发布重要数据更新预告：自2026年6月起，BGC-Argo叶绿素数据将由数据汇集中心（DACs）采用新校正方法重新处理和重新分发，数据质量和精度将显著提升，但部分区域数据值可能出现明显变化。提醒依赖该数据进行学术发表或建模分析的用户注意，5月12日已举办专题网络研讨会说明变更原因及最佳实践。', 'source': 'Euro-Argo ERIC', 'url': 'https://www.linkedin.com/posts/euroargo_argofloats-oceanscience-activity-7455168522688761856-Bu9b', 'date': '2026-05-05'},
  ]},
  {'title': '六、海洋数据管理与共享服务', 'en': 'Ocean Data Management & Sharing', 'items': [
    {'title': 'IODE：PANGAEA社区研讨会与OBIS数据发布——IODE海洋数据管理最新动态（2026-05-13）', 'badge': '近7天', 'abstract': 'IOC-IODE更新近期动态：PANGAEA于2026年5月7-8日成功举办数据发现与获取社区实操研讨会，聚焦Jupyter Notebooks中的PANGAEA数据使用、Python和R编程查询及开放标准集成；OBIS持续更新Okeanos Explorer等航次数据；IODE OceanTeacher Global Academy 2026年在线培训课程（SP_ODM2026）继续接受报名，涵盖海洋数据管理全流程指导原则与典型职责。', 'source': 'IOC-UNESCO / IODE / PANGAEA', 'url': 'https://www.iode.org/', 'date': '2026-05-13'},
  ]},
  {'title': '七、开放航次 / 船时共享', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
    {'title': '中科院深海所（2026-05-12）：全球深渊探索计划太平洋穿越航次圆满完成——奋斗者号156天创纪录', 'badge': '近7天', 'abstract': '北京时间5月10日，探索一号搭载奋斗者号完成156天、总航程超4万公里的全球深渊探索计划太平洋穿越航次，6国83名队员参与，奋斗者号完成63个潜次（50次超6000米），首次发现南半球最深化能生态系统，采集大量生物地质标本，多个生物可能为新物种，入选联合国海洋十年行动计划。', 'source': '中国科学院深海科学与工程研究所', 'url': 'https://www.idsse.ac.cn/xwdt/ywdt/202605/t20260512_8200019.html', 'date': '2026-05-12'},
    {'title': '中国太平洋学会（2026-05-14）：第三届海洋计算挑战赛（MCC 2026）正式启动报名', 'badge': '近7天', 'abstract': '面向全国高校师生及科研单位的第三届海洋计算挑战赛（MCC 2026）正式启动，竞赛涵盖海洋大数据处理与分析、海洋环境模拟与预测、海洋灾害预警、海洋人工智能应用五大方向，依托海光国产DCU加速卡及国产超算平台。历届累计近70所高校、180余支队伍参赛，决赛最高奖金5万元，报名截止2026年5月25日。', 'source': '中国太平洋学会', 'url': 'https://finance.sina.cn/tech/2026-05-14/detail-inhxvpqq8804608.d.html', 'date': '2026-05-14'},
  ]},
  {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [
    {'title': 'NCEI / NOAA（2026-05-12）：NCEI启动史上最大规模云迁移——全部数据和服务将迁移至AWS', 'badge': '近7天', 'abstract': 'NOAA NCEI宣布将全部数据、产品和服务迁移至亚马逊云服务（AWS），为期10个月。NCEI拥有全球最大环境数据库之一，每月归档超229TB数据，数据来源覆盖130以上观测平台。迁移完成后用户将可通过按需访问数据，无需下载，显著提升AI/ML应用场景下的数据利用效率。NCEI同步发布云迁移FAQ并将在官网提前通知进度。', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/cloud-migration', 'date': '2026-05-12'},
    {'title': '复旦大学 / ESSD（2026-05-12）：GEOXYGEN——1960-2024年全球长期溶解氧数据集发布', 'badge': '近7天', 'abstract': '复旦大学大气与海洋科学系团队在ESSD正式发表GEOXYGEN数据集（doi.org/10.5194/essd-18-3125-2026），利用生物地球化学感知机器学习框架，基于多源观测生成1960-2024年全球月均0.5度x0.5度溶解氧场（0-5500m），测试R2大于0.9，重建格局与WOA 2023高度一致，为评估气候系统模型中溶解氧表征能力提供基准。', 'source': 'Earth System Science Data / 复旦大学', 'url': 'https://essd.copernicus.org/articles/18/3125/2026/', 'date': '2026-05-12'},
    {'title': 'Nature Communications（2026-05-11）：低云反馈在不可逆海平面上升中的关键作用', 'badge': '近7天', 'abstract': '首尔国立大学团队在Nature Communications发表研究，利用全耦合气候模型揭示：即使没有冰川融化，由于海洋内部巨大热惯性，海平面将在数个世纪内持续升高。关键机制是一种特定的海表温度升温模式通过低云反馈增强短波辐射吸收，从而维持海洋热量吸收和热膨胀。研究强调准确表征表面升温模式及相关云响应的重要性。', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72898-4', 'date': '2026-05-11'},
    {'title': 'Nature Communications（2026-05-07）：热带气旋年最大强度存在次表层信使——可提前数年预测', 'badge': '近7天', 'abstract': 'Nature Communications发表研究，揭示西北太平洋热带气旋峰值强度与形成于北太平洋高压控制下的次表层水团温度存在强相关性，该水团约4年被输送至西边界，可通过监测北太平洋高压强度提前数年预测热带气旋年最大强度。该机制为理解气候变化背景下热带气旋强度演变提供了新视角。', 'source': 'Nature Communications', 'url': 'https://www.nature.com/articles/s41467-026-72770-5', 'date': '2026-05-07'},
    {'title': 'NOAA Ocean Exploration（2026年航季）：Okeanos Explorer全年航次计划发布——太平洋深度探索', 'badge': '近7天', 'abstract': 'NOAA Ocean Exploration发布2026全年航次计划，Okeanos Explorer号将于太平洋及密歇根湖开展多航次作业：5月16日至6月5日夏威夷海域ROV系统测试（EX2603）；4月29日至5月6日完成测绘系统测试航次（EX2602）。E/V Nautilus 2026航季（6-10月）将探索中太平洋和西太平洋深海栖息地，各航次数据实时公开。', 'source': 'NOAA Ocean Exploration / OET', 'url': 'https://oceanexplorer.noaa.gov/expedition-2026-expeditions/', 'date': '2026-05-07'},
  ]},
  {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [
    {'title': 'OSGeo（2026-05-08）：GDAL 3.13.0 Iowa City发布——新增Zarr V3、COG写入、SAR CPHD驱动等', 'badge': '近7天', 'abstract': '开源地理空间数据抽象库GDAL发布3.13.0版本（代号Iowa City），新增10余个gdal CLI子命令；Zarr V3支持显著增强（sharding、multiscales、空间扩展）；新增COG随机写入、E57 2D影像读取、SAR CPHD多维数据读取等驱动；S102/S104/S111新增写入能力；INTERLIS 2.4格式支持。GDAL是海洋/气象NetCDF、GeoTIFF等数据处理的基础工具库。', 'source': 'OSGeo / GitHub', 'url': 'https://github.com/OSGeo/gdal/releases', 'date': '2026-05-08'},
    {'title': 'IOCCG / NASA（2026-05-05）：HyperCP v1.2.15发布——PACE高光谱数据处理器新增完整不确定性传播', 'badge': '近7天', 'abstract': 'NASA HyperInSPACE社区处理器（HyperCP）发布v1.2.15版本，为所有L2产品引入基于仪器类别和传感器型号的不确定性预算分解（含绝对辐射定标、杂散光、线性度、偏振、热响应等贡献项）；新增海面闪烁校正和BRDF校正方法；扩展SolarTracker、pySAS、DALEC自主平台支持；实验室标定由FRM4SOC联合完成。', 'source': 'IOCCG / NASA / GitHub', 'url': 'https://github.com/nasa/HyperCP', 'date': '2026-05-05'},
    {'title': 'IOOS（2026-05-07）：5月简报发布——J-SCOPE数据上线AWS、HF雷达历史数据归档至NCEI', 'badge': '近7天', 'abstract': '美国IOOS发布5月简报：JISAO季节性海岸生态预报数据（J-SCOPE，6-9个月预见期）正式上线AWS开放数据注册表；NCEI与Scripps CORDC合作完成IOOS HF雷达项目全历史数据归档；华盛顿州Kalaloch新HF雷达站投入运行；CeNCOOS新增两处WebCOOS海岸摄像头；NANOOS NVS新增水柱断面可视化工具。', 'source': 'US IOOS / NOAA', 'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-may-2026/', 'date': '2026-05-07'},
  ]},
]

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
