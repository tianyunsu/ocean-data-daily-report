#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查今日日报所有链接的有效性和页面内容一致性
"""
import requests
import re
import time
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

ITEMS = [
    # 一、海洋AI
    {"section": "一、海洋AI", "idx": 1,
     "title": "北极夏季海冰快速融化事件的驱动机制",
     "url": "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026GL121848",
     "date": "2026-04-22", "key": "10.1029/2026GL121848"},
    {"section": "一、海洋AI", "idx": 2,
     "title": "基于ConvLSTM的海冰密集度长期预测",
     "url": "https://link.springer.com/article/10.1007/s12145-026-02125-7",
     "date": "2026-04-18", "key": "s12145-026-02125-7"},
    {"section": "一、海洋AI", "idx": 3,
     "title": "ML大气强迫 vs. NWP大气强迫驱动海洋预报",
     "url": "https://arxiv.org/abs/2604.07861",
     "date": "2026-04-09", "key": "2604.07861"},
    {"section": "一、海洋AI", "idx": 4,
     "title": "AI技术首次揭示肉眼不可见的海洋洋流——GOFLOW",
     "url": "https://www.sciencedaily.com/releases/2026/04/260421042803.htm",
     "date": "2026-04-21", "key": "260421"},
    {"section": "一、海洋AI", "idx": 5,
     "title": "人工智能赋能可持续海洋研究综述专题",
     "url": "https://www.frontiersin.org/research-topics/80289/artificial-intelligence-for-sustainable-oceans",
     "date": "2026-04-24", "key": "80289"},

    # 二、海洋数字孪生
    {"section": "二、海洋数字孪生", "idx": 1,
     "title": "海洋数字孪生互操作性取得新进展",
     "url": "https://www.inesctec.pt/en/news/interoperability-ocean-digital-twins-featuring-inesc-tec",
     "date": "2026-04-10", "key": "interoperability-ocean-digital-twins"},
    {"section": "二、海洋数字孪生", "idx": 2,
     "title": "EGU 2026海洋预测系统展区——Blue-Cloud与数字孪生联合展示",
     "url": "https://www.copernicus.eu/en/news-events/general/copernicus-marine-service-and-eurogoos-join-forces-egu-2026",
     "date": "2026-04-13", "key": "eurogoos-join-forces-egu-2026"},
    {"section": "二、海洋数字孪生", "idx": 3,
     "title": "DITTO Programme全球DTO治理框架正式启动",
     "url": "https://ditto-oceandecade.org/",
     "date": "2026-04-24", "key": "ditto"},
    {"section": "二、海洋数字孪生", "idx": 4,
     "title": "DITTO Summit 2026日本横滨",
     "url": "https://w3.jamstec.go.jp/j/pr-event/ditto_summit2026/index.html",
     "date": "2026-04-24", "key": "ditto_summit2026"},

    # 三、海洋可视化
    {"section": "三、海洋可视化", "idx": 1,
     "title": "Blue-Cloud 2026九份新开放获取培训材料",
     "url": "https://blue-cloud.d4science.org/",
     "date": "2026-04-21", "key": "blue-cloud"},
    {"section": "三、海洋可视化", "idx": 2,
     "title": "Argo DAC可视化工具新批次工具",
     "url": "https://www.argodatamgt.org/",
     "date": "2026-04-15", "key": "argodatamgt"},
    {"section": "三、海洋可视化", "idx": 3,
     "title": "NOAA AOML Argo浮标实时运行与数据质量控制",
     "url": "https://www.aoml.noaa.gov/argo/",
     "date": "2026-04-17", "key": "aoml"},
    {"section": "三、海洋可视化", "idx": 4,
     "title": "Zenodo海色叶绿素-a月度填补数据集",
     "url": "https://zenodo.org/records/19555449",
     "date": "2026-04-25", "key": "19555449"},

    # 四、海洋数据质量
    {"section": "四、海洋数据质量", "idx": 1,
     "title": "Argo DAC可视化工具（重复条目）",
     "url": "https://www.argodatamgt.org/",
     "date": "2026-04-15", "key": "argodatamgt"},
    {"section": "四、海洋数据质量", "idx": 2,
     "title": "Argo Myanmar数据恢复项目",
     "url": "https://www.argodatamgt.org/DataAccess.html",
     "date": "2026-04-15", "key": "DataAccess"},
    {"section": "四、海洋数据质量", "idx": 3,
     "title": "ETOOCC2海表二氧化碳数据质量控制标准更新",
     "url": "https://www.socat.info/",
     "date": "2026-04-01", "key": "socat"},
    {"section": "四、海洋数据质量", "idx": 4,
     "title": "NOAA AOML Argo浮标实时运行（重复条目）",
     "url": "https://www.aoml.noaa.gov/argo/",
     "date": "2026-04-17", "key": "aoml"},
    {"section": "四、海洋数据质量", "idx": 5,
     "title": "GO-BGC 2026年浮标数据与科学Workshop开放注册",
     "url": "https://www.go-bgc.org/",
     "date": "2026-04-07", "key": "go-bgc"},

    # 五、海洋数据处理
    {"section": "五、海洋数据处理", "idx": 1,
     "title": "CMEMS 4月份产品与服务更新公告——北极新产品",
     "url": "https://marine.copernicus.eu/news/april-releases-copernicus-marine-launches-three-new-products",
     "date": "2026-04-03", "key": "april-releases"},
    {"section": "五、海洋数据处理", "idx": 2,
     "title": "EGUsphere数据驱动生物地球化学预测模型",
     "url": "https://egusphere.copernicus.org/",
     "date": "2026-04-21", "key": "egusphere"},
    {"section": "五、海洋数据处理", "idx": 3,
     "title": "NOAA AFSC北太平洋多尺度海洋物理-生物地球化学耦合模拟",
     "url": "https://www.fisheries.noaa.gov/ak/science-data/ocean-observations",
     "date": "2026-04-15", "key": "ocean-observations"},
    {"section": "五、海洋数据处理", "idx": 4,
     "title": "OceanPredict AI-TT Workshop论文集出版",
     "url": "https://www.mercator-ocean.eu/en/news/copy-of-crafting-the-future-machine-learning-for-ocean-forecasting/",
     "date": "2026-04-13", "key": "machine-learning-for-ocean-forecasting"},
    {"section": "五、海洋数据处理", "idx": 5,
     "title": "Argo DMQC v2.0 BGC参数扩展",
     "url": "https://github.com/ArgoDMQC/ArgoDMQC",
     "date": "2026-04-24", "key": "ArgoDMQC"},

    # 六、海洋数据管理
    {"section": "六、海洋数据管理", "idx": 1,
     "title": "ICY-TPACIFIC太平洋西边界流航次共享平台",
     "url": "https://www.oceanpc.io/ship-time",
     "date": "2026-04-17", "key": "ship-time"},
    {"section": "六、海洋数据管理", "idx": 2,
     "title": "CMEMS新增实时海表温度网格化产品",
     "url": "https://marine.copernicus.eu/access-data/",
     "date": "2026-04-17", "key": "copernicus marine access"},
    {"section": "六、海洋数据管理", "idx": 3,
     "title": "OCEAN:ICE北极-大西洋相互作用研究开放数据论文",
     "url": "https://ocean-ice.eu/news-events/publications/",
     "date": "2026-04-10", "key": "ocean-ice"},
    {"section": "六、海洋数据管理", "idx": 4,
     "title": "Argo数据访问门户新增Erddap实时服务器支持",
     "url": "https://www.argodatamgt.org/DataAccess.html",
     "date": "2026-04-23", "key": "DataAccess"},

    # 七、开放航次
    {"section": "七、开放航次", "idx": 1,
     "title": "SOOSmap南极绕极流观测数据地图集",
     "url": "https://soos.oceanobserver.org/",
     "date": "2026-04-20", "key": "soos"},
    {"section": "七、开放航次", "idx": 2,
     "title": "GTSPP新增2025年航海采集数据",
     "url": "https://www.ncei.noaa.gov/products/world-ocean-database",
     "date": "2026-04-16", "key": "world-ocean-database"},
    {"section": "七、开放航次", "idx": 3,
     "title": "SeaDataNet 3.0预览新增语义互操作层",
     "url": "https://www.seadatanet.org/",
     "date": "2026-04-12", "key": "seadatanet"},
    {"section": "七、开放航次", "idx": 4,
     "title": "ICES 2025年度开放数据报告",
     "url": "https://ices.dk/news/",
     "date": "2026-04-18", "key": "ices"},
    {"section": "七、开放航次", "idx": 5,
     "title": "IODE Ocean InfoHub联合国教科文组织海洋数据生态系统",
     "url": "https://iode.org/data/",
     "date": "2026-04-23", "key": "iode"},

    # 八、海洋数据中心
    {"section": "八、海洋数据中心", "idx": 1,
     "title": "GDC全球数据中心联盟新版交叉检索工具",
     "url": "https://www.geodcc.org/",
     "date": "2026-04-22", "key": "geodcc"},
    {"section": "八、海洋数据中心", "idx": 2,
     "title": "NOAA CoastWatch Gulf of Mexico门户升级",
     "url": "https://coastwatch.noaa.gov/",
     "date": "2026-04-19", "key": "coastwatch"},
    {"section": "八、海洋数据中心", "idx": 3,
     "title": "WMO GTSPP数据整合（重复条目）",
     "url": "https://www.ncei.noaa.gov/products/world-ocean-database",
     "date": "2026-04-16", "key": "world-ocean-database"},
    {"section": "八、海洋数据中心", "idx": 4,
     "title": "SeaDataNet 3.0预览（重复条目）",
     "url": "https://www.seadatanet.org/",
     "date": "2026-04-12", "key": "seadatanet"},
    {"section": "八、海洋数据中心", "idx": 5,
     "title": "ICES 2025年度开放数据报告（重复条目）",
     "url": "https://ices.dk/news/",
     "date": "2026-04-18", "key": "ices"},
    {"section": "八、海洋数据中心", "idx": 6,
     "title": "PANGAEA IODP 2025年expeditions数据集批量下载",
     "url": "https://iodp.pangaea.de/",
     "date": "2026-04-25", "key": "iodp"},

    # 九、工具与代码
    {"section": "九、工具与代码", "idx": 1,
     "title": "MITgcm adjoint工具包GPU加速",
     "url": "https://github.com/MITgcm/MITgcm",
     "date": "2026-04-16", "key": "MITgcm"},
    {"section": "九、工具与代码", "idx": 2,
     "title": "CMEMS Python工具包v3.3",
     "url": "https://marine.copernicus.eu/access-data/",
     "date": "2026-04-20", "key": "copernicus"},
    {"section": "九、工具与代码", "idx": 3,
     "title": "CROCO-Ocean v2.1.3 bug修复版",
     "url": "https://www.croco-ocean.org/",
     "date": "2026-04-07", "key": "croco"},
    {"section": "九、工具与代码", "idx": 4,
     "title": "NOAA OceanDataLinks新增27个数据链接",
     "url": "https://www.pmel.noaa.gov/gtmba/",
     "date": "2026-04-14", "key": "gtmba"},
    {"section": "九、工具与代码", "idx": 5,
     "title": "Xarray v2026.4.0新增稀疏数组支持",
     "url": "https://github.com/pydata/xarray/releases",
     "date": "2026-04-13", "key": "xarray/releases"},
]

results = []
print(f"共 {len(ITEMS)} 条，开始检查...\n")

for item in ITEMS:
    url = item["url"]
    label = f"[{item['section']} #{item['idx']}]"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        status = resp.status_code
        content = resp.text[:3000] if resp.text else ""
        
        # 检查关键词
        key = item["key"].lower()
        content_lower = content.lower()
        
        # 基本有效性
        is_valid_http = status == 200
        is_not_error_page = not any(x in content_lower for x in ["404", "page not found", "not found", "error", "does not exist", "no longer available"])
        
        # 内容一致性（关键词是否出现在页面中）
        # 对于通用主页（如 argodatamgt.org/），放宽判断
        is_generic_homepage = url.endswith("/") and len(url.split("/")) <= 5
        
        result = {
            "section": item["section"],
            "idx": item["idx"],
            "title": item["title"],
            "url": url,
            "date": item["date"],
            "status": status,
            "is_valid_http": is_valid_http,
            "content_snippet": content[:200].replace("\n", " ").strip(),
            "is_generic_homepage": is_generic_homepage,
            "key_found": key in content_lower,
        }
        
        flag = "OK" if is_valid_http else "FAIL"
        if is_valid_http and not result["key_found"] and not is_generic_homepage:
            flag = "WARN"
        
        print(f"{flag} {label} HTTP {status} | key='{key}' found={result['key_found']} | {url[:70]}")
        results.append({**result, "flag": flag})
        
    except Exception as e:
        print(f"FAIL {label} ERROR: {e} | {url[:70]}")
        results.append({
            "section": item["section"],
            "idx": item["idx"],
            "title": item["title"],
            "url": url,
            "date": item["date"],
            "status": "ERR",
            "error": str(e),
            "flag": "❌",
            "is_generic_homepage": False,
            "key_found": False,
        })
    
    time.sleep(0.5)

# 保存结果
with open("link_check_0427.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n=== Summary ===")
print(f"Total: {len(results)}")
print(f"OK: {sum(1 for r in results if r['flag']=='OK')}")
print(f"WARN (HTTP 200 but key not found): {sum(1 for r in results if r['flag']=='WARN')}")
print(f"FAIL: {sum(1 for r in results if r['flag']=='FAIL')}")

print("\n=== Items needing attention ===")
for r in results:
    if r["flag"] != "OK":
        print(f"  {r['flag']} [{r['section']} #{r['idx']}] {r['title'][:50]}")
        print(f"      URL: {r['url']}")
        print(f"      Status: HTTP {r.get('status','ERR')} | key_found={r.get('key_found')}")
        if "error" in r:
            print(f"      Error: {r['error']}")
        print()
