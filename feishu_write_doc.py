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
SECTIONS = [{'title': '一、海洋人工智能', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [{'title': 'AMR-Pose：主动LED标记+概率切换PnP的协同AUV相对位姿估计框架（arXiv, 2026-08-13）', 'badge': '[论文]', 'abstract': '针对水下光学退化（浑浊、光照变化、反射与间歇遮挡）下多AUV协同的相对位姿估计难题，研究者提出 AMR-Pose 框架：在领航AUV上集成一枚红心+三蓝周LED的主动标记模块，构建可辨识视觉特征；结合SE(3)李群位姿传播、概率标记关联与可见性自适应融合，开发概率切换PnP估计器（PSwPnP），实现六自由度相对位姿的鲁棒估计。水槽动捕真值实验与闭环领航-跟随实验验证了其在复杂水下条件下精度与平滑性，为协同海洋探索、采样与多机器人协调提供新工具。', 'source': 'arXiv / cs.RO', 'url': 'https://arxiv.org/abs/2608.12866', 'date': '2026-08-13'}, {'title': 'LinStereo：ECCV 2026 线性复杂度全局注意力水下立体匹配+SeaStereo数据集（arXiv, 2026-06-24，豁免55天）', 'badge': '[论文]', 'abstract': '悉尼大学团队提出 LinStereo，构建于 Depth Anything V3 之上，核心为位置感知线性注意力（PALA）模块，以线性成本实现全局聚合，将可靠匹配区域的估计传播至退化区域；配合层级语义代价体（HSCV）与深度先验初始化（DPI），解决水下严苛光度退化下立体匹配难题。在水下基准 SQUID 上 AbsRel 降低26%，TartanAir-UW 降低28%；同时发布 SeaStereo 数据集（40320对带稠密视差标注的水下立体图像，覆盖7种Jerlov水体类型），填补水下立体匹配公开数据空白。（顶会论文，以arXiv首次公开日2026-06-24为基准，55天豁免收录）', 'source': 'ECCV 2026 / arXiv', 'url': 'https://arxiv.org/abs/2606.25437', 'date': '2026-06-24'}, {'title': '福建"渔区海况预报"正式上线：全国首个省级渔区七天逐时专项预报产品（2026-08-10）', 'badge': '[要闻]', 'abstract': '福建省海洋预报台正式上线"渔区海况预报"产品，以农业农村部划定的159个渔区为基本单元，实现"一渔区一预报"的精细化服务，发布未来七天海浪、海温逐小时滚动预报。该产品依托全国首个省级精细化海洋智能网格预报平台（500米/5千米/10千米三级网格、1小时预报时效），是"海上福建"总平台的重要组成部分，标志着福建海洋预报服务向精细化、智能化、精准化迈出关键一步，为渔业安全生产提供数据支撑。', 'source': '福建省海洋预报台 / 网易', 'url': 'https://www.163.com/dy/article/L40NKLEI0514K885.html', 'date': '2026-08-10'}]}, {'title': '二、海洋数字孪生', 'en': 'Ocean Digital Twin', 'items': [{'title': '山东港口日照港集装箱数字孪生系统上线：全域感知实时同步的港口虚拟镜像（2026-08-14）', 'badge': '[要闻]', 'abstract': '山东港口日照港集装箱分公司正式上线集装箱数字孪生系统，将码头堆场、靠泊船舶、作业设备等核心生产要素数字化复刻，构建全域感知、实时同步的港口虚拟镜像。系统支持秒级箱号定位、历史回溯（依托智能数据重构复现任意时刻码头状态）、工班机械24小时热力图与闸口业务监控等能力，推动港口集装箱运营管理从经验驱动向数据驱动转型，是涉海基础设施数字孪生落地案例。', 'source': '山东省国资委 / 搜狐', 'url': 'https://www.sohu.com/a/1062984699_122066679', 'date': '2026-08-14'}]}, {'title': '三、海洋可视化', 'en': 'Ocean Visualization', 'items': [{'title': '本周暂无明显进展（MyOcean Health 07-01、WavyOcean 3.0 07-13 已收录）', 'badge': '[关注]', 'abstract': '海洋可视化方向近一周无重大新工具或平台发布。Copernicus MyOcean Health（07-01收录）、香港科技大学 WavyOcean 3.0（07-13收录）、CMEMS MyOcean Pro 3D路线图（08-03收录）均已在此前日报覆盖，本期不重复收录。', 'source': '-', 'url': 'https://marine.copernicus.eu/', 'date': '2026-08-18'}]}, {'title': '四、海洋数据质量', 'en': 'Ocean Data Quality', 'items': [{'title': 'DTF-Net：基于深度学习关联检验规则的风数据质量控制算法（JMSE 14(16):1453, 2026-08-07）', 'badge': '[论文]', 'abstract': '自然资源部北海预报减灾中心团队提出深度学习风数据质控算法：构建双轨信息融合网络（DTF-Net），时间轨捕获风速局部时变、全局轨挖掘温度-气压-风向等物理耦合关系，结合动态三倍标准差尖峰检测与基于深度学习预测的3δ-RMSE空间校验，实现无邻站条件下多维协同异常检测。实验表明1/12/24小时风速预报MAE较 AutoFormer 等通用模型降低3.8%~61.3%，质控异常检出率0.33%~9.20%，为稀疏海洋观测网提供新的智能质控范式。', 'source': 'Journal of Marine Science and Engineering', 'url': 'https://www.mdpi.com/2077-1312/14/16/1453', 'date': '2026-08-07'}]}, {'title': '五、海洋数据处理', 'en': 'Ocean Data Processing', 'items': [{'title': '条件多元函数PCA重建深潜海洋哺乳动物部分温盐剖面（arXiv 2608.05376, 2026-08-05）', 'badge': '[论文]', 'abstract': '法国艾克斯-马赛大学等团队提出统计方法，利用多元函数主成分分析（mfPCA）与条件估计，从南象海豹生物记录器获取的部分温盐剖面中推断未观测水层。基于2018-2020年24只雌性南象海豹在克尔格伦高原约300万平方公里海域的观测，使用15203条达500米深度的完整剖面构建统计模型，成功重建约9万条不完整剖面；引入地理协变量后250米截断剖面的重建精度提升30%（温度）与33%（盐度），展示了动物活动轨迹中蕴含的深层环境信息挖掘价值。', 'source': 'arXiv / physics.ao-ph', 'url': 'https://arxiv.org/abs/2608.05376', 'date': '2026-08-05'}, {'title': '哨兵-2 超时相数据立方体将光学测深极限拓展至70-80米（EUSPA, 2026-08-17）', 'badge': '[要闻]', 'abstract': '欧洲空间计划署（EUSPA）披露AI与遥感融合新进展：研究团队构建哨兵-2号超时相（HT）数据立方体，通过长时间序列辐射校正、云噪去除与时相合成，将光学测深有效深度极限从约20米拓展至70-80米。结合随机森林、XGBoost等机器学习算法，生成100米空间分辨率测深产品，全球多个清澈海域0-80米范围测深MAE最低1.88米（留尼汪站），浑浊海域（北大西洋韦桑岛）MAE控制在4.74米以内；首幅全球浅海测深试点产品已在哥白尼数据平台开放下载，为沿海生境测绘、近海航运安全、海底考古提供低成本新数据源。', 'source': 'EUSPA / SpaceMapper', 'url': 'https://spacemapper.cn/zh-cn/info/news/1494988529598466.html', 'date': '2026-08-17'}]}, {'title': '六、海洋数据管理与共享', 'en': 'Ocean Data Management & Sharing', 'items': [{'title': 'OBIS 发布南极 ROV 底栖图像丰度数据集（TANGO1-TANGO2, 2023-2024）（2026-08-14）', 'badge': '[数据]', 'abstract': '海洋生物多样性信息系统（OBIS）南极节点发布"Image-based abundance of Antarctic benthic morphotaxa from ROV surveys in the Western Antarctic Peninsula (TANGO1-TANGO2, 2023-2024)"数据集：基于BlueROV搭载GoPro HERO 10在西南极半岛浅海底拍摄的图像，记录底栖无脊椎动物形态种丰度，数据部分发表于 Polar Biology（2025）与 Ecology & Evolution（2026），以开放数据发布并由 SCAR 南极生物多样性门户提供技术支持，为南极底栖生态系统长期监测提供标准化图像观测数据源。', 'source': 'OBIS / Antarctic OBIS', 'url': 'https://portal.obis.org/', 'date': '2026-08-14'}]}, {'title': '七、开放航次与科考', 'en': 'Open Cruises & Research Expeditions', 'items': [{'title': 'NOAA Okeanos Explorer EX2606 美属萨摩亚 ROV 探险即将启航（2026-08-19起）', 'badge': '[航次]', 'abstract': 'NOAA 海洋探索计划公布 2026 年美属萨摩亚 ROV 探险（EX2606）：8月19日至9月16日，NOAA 船 Okeanos Explorer 将在美属萨摩亚周边深水开展 ROV 下潜与多波束测绘作业，探索海床与水柱生态，通过远程呈现技术实现岸基科学家与公众实时参与。数据将用于理解该区域地质历史与深海生境，并为包括关键矿产在内的海洋资源管理提供信息，是 NOAA 2026 年太平洋系列航次（EX2605库克群岛收官后）的接续任务。', 'source': 'NOAA Ocean Exploration', 'url': 'https://oceanexplorer.noaa.gov/expedition-2026-expeditions/', 'date': '2026-08-19'}]}, {'title': '八、海洋数据中心', 'en': 'Ocean Data Centers', 'items': [{'title': 'GEBCO_2026 全球地形网格 WMS 图层上线，海底地形数据开放服务升级（2026-08-04）', 'badge': '[数据]', 'abstract': 'GEBCO 发布基于 GEBCO_2026 网格的 Web Map Service（WMS）图层（8月4日）。GEBCO_2026 为15弧秒（约500米）全球海陆一体地形网格，融合 SRTM15+ V2.8 与新一代 SWOT 卫星重力场反演数据及海床2030项目四区域中心多波束编译成果；本轮发布后全球按现代标准测绘海床面积达28.7%（较2025年27.3%提升，新增约500万平方公里）。WMS 图层使地理信息系统用户可直接在线调用该权威海底地形数据，为海洋科研与制图提供标准化服务入口。', 'source': 'GEBCO / Seabed 2030', 'url': 'https://www.gebco.net/?page=9', 'date': '2026-08-04'}]}, {'title': '九、工具与代码资源', 'en': 'Tools & Code Resources', 'items': [{'title': '本周暂无明显进展（gridstats v2.6.0 08-12、wavespectra 5.0 预告 08-10 已收录）', 'badge': '[关注]', 'abstract': '海洋工具与代码资源方向近一周无重要新版本或新开源项目发布。gridstats v2.6.0（08-12收录）、wavespectra v5.0 架构升级预告（08-10收录）、cstar-ocean v0.8.0（08-05收录）均已在此前日报覆盖，本期不重复收录。', 'source': '-', 'url': 'https://pypi.org/', 'date': '2026-08-18'}]}]

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
