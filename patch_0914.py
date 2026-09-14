# -*- coding: utf-8 -*-
"""
patch_0914.py — 修正 2026-09-14 日报的 5 类缺陷
1) D4 两条与历史期重复（DTF-Net 见 08-18；事件保留 QC 见 08-10）→ 替换为全新条目
2) D8 一条与 09-04 期重复（EMODnet Data Ingestion）→ 替换为全新条目
3) 两条 mnr.gov.cn 链接 404（推测生成的 URL）→ 换为实测可访问来源
4) EMODnet Biology 条目链接指向首页 → 换为具体数据产品页，并补真实细节
5) Ocean-E2E 以会议日作 date 但摘要未标注预印本原始公开日 → 补注
说明：中文正文内一律使用全角引号“”，与仓库既有稿件风格一致。
"""
import io, sys

P = 'build_daily_0914.py'
s = io.open(P, encoding='utf-8').read()
orig = s


def span_replace(text, start_anchor, end_anchor, new, label):
    i = text.find(start_anchor)
    if i < 0:
        print('  [FAIL] 未找到起始锚点: ' + label); sys.exit(1)
    j = text.find(end_anchor, i)
    if j < 0:
        print('  [FAIL] 未找到结束锚点: ' + label); sys.exit(1)
    j += len(end_anchor)
    print('  [OK] ' + label + '  (%d 字符 -> %d 字符)' % (j - i, len(new)))
    return text[:i] + new + text[j:]


def one_replace(text, old, new, label):
    n = text.count(old)
    if n != 1:
        print('  [FAIL] ' + label + ' 命中 %d 次（应为 1）' % n); sys.exit(1)
    print('  [OK] ' + label)
    return text.replace(old, new, 1)


# ---------- 1) 替换 D4 两条重复条目 ----------
NEW_D4 = """                'title': 'Sentinel-6 双星同轨串联飞行完成星间交叉校验：海平面基准卫星交接就绪，延续近四十年测高记录（NASA/JPL, 2026-09-09）',
                'badge': '[动态]',
                'abstract': 'NASA 与欧洲伙伴于 2025 年 11 月发射的 Sentinel-6B，目前正以约 30 秒的间隔紧随前辈 Sentinel-6 Michael Freilich 在同一轨道上串联飞行，两颗卫星先后测量同一片海面，以此交叉校验新卫星的测高系统与既有海平面基准是否一致——这正是“同一方法、每次都量得一样”的连续性保障机制。Sentinel-6B 已于 2026 年 7 月 15 日开始向预报系统输出低延迟数据。两颗卫星各载一台 Poseidon-4 雷达高度计与微波辐射计，测量海面高度、浪高与海面风速，另配 GNSS 掩星仪反演大气湿度、气压与温度。NOAA 专家评价“就数据质量而言，Sentinel-6 任务无与伦比”，并计划在年底前将该高度计数据纳入其卫星海洋热含量算法。Sentinel-6B 将于今年晚些时候接任全球海平面测量的参考卫星，延续自 1992 年 TOPEX/Poseidon 以来近四十年的海平面记录。',
                'source': 'NASA / JPL（Sentinel-6/Jason-CS 任务；ESA、EUMETSAT、NOAA、CNES 联合）',
                'url': 'https://www.nasa.gov/missions/jason-cs-sentinel-6/how-2-us-european-satellites-are-studying-hurricanes-during-el-nino/',
                'date': '2026-09-09',
            },
            {
                'title': 'CFOSAT SWIM 海浪谱产品三代版本质量评估：6.0.3 / 7.0.0 / 7.1.0 与 ERA5 时空匹配，按海况分级验证（《海洋学报》, 网络出版 2026-09-04）',
                'badge': '[论文]',
                'abstract': '中法海洋卫星 CFOSAT 搭载全球首款专门测量二维海浪谱的海浪波谱仪 SWIM，已在轨运行超过七年；随着地面处理技术持续优化，SWIM 海浪谱产品经历多次版本迭代，不同版本在数据预处理算法与观测波束校正策略上的差异，已使其公开可用的 6.0.3、7.0.0、7.1.0 三个版本在谱结构与数据质量上表现出明显分化。南京信息工程大学与国家卫星海洋应用中心等团队将各版本 SWIM 海浪谱与 ERA5 海洋再分析数据做时空匹配，并基于风浪与涌浪有效波高开展精细化海况分类验证，系统刻画了三代产品的质量演变特征。该工作为全球用户按研究目的选择合适版本、为后续版本迭代改进提供了量化依据。',
                'source': '《海洋学报》Acta Oceanologica Sinica（南京信息工程大学 + 国家卫星海洋应用中心）',
                'url': 'http://hyxbocean.cn/article/id/1bddb856-f5ac-40d6-8996-ad69bba16ae0?viewType=HTML',
                'date': '2026-09-04',
            },
        ],"""
s = span_replace(s,
    "                'title': 'DTF-Net：双轨信息融合网络",
    "                'date': '2026-08-08',\n            },\n        ],",
    NEW_D4, 'D4 替换两条重复条目')

# ---------- 2) 替换 D8 重复条目 ----------
NEW_D8 = """                'title': 'NOAA NCEI 为深海科考上线 SOUP 样品数据管理系统：覆盖采样到归档的全生命周期云端管理（NOAA Ocean Exploration, 2026-09-10）',
                'badge': '[动态]',
                'abstract': '为提升深海实物样品所关联数据的完整性，美国国家环境信息中心（NCEI）开发了新一代采样数据管理系统 SOUP（Sampling Operations User Portal），并于 2026 年科考季开始时安装到 Okeanos Explorer 号科考船，现已纳入常态化作业。SOUP 是一个带后端数据库的云端应用，用于存储、管理与维护深海样品的全部信息：经纬度、水深、温度、盐度、溶解氧以及采样时的原位影像等环境元数据随采集即录入；用户可一键导入采样元数据、打印博物馆级标签、生成汇总导出与报告。系统与船载数据记录软件集成，通过自动化与网络化管道简化采样工作流，使数据备份与远程访问更快、人为差错更少。NCEI 负责样品数据自采集、处理直至长期归档与公共访问的全生命周期管理，后续或将 SOUP 推广至其他项目以替代过时流程。',
                'source': 'NOAA Ocean Exploration / NCEI',
                'url': 'https://oceanexplorer.noaa.gov/expedition-feature/soup-a-recipe-for-managing-data-from-the-abyss-to-archive',
                'date': '2026-09-10',
            },"""
s = span_replace(s,
    "                'title': 'EMODnet 数据吸纳服务新阶段启动",
    "                'date': '2026-08-31',\n            },",
    NEW_D8, 'D8 替换一条重复条目')

# ---------- 3) EMODnet Biology 条目：链接改为具体产品页 + 摘要补真实细节 ----------
OLD_12 = ("                'abstract': 'EMODnet Biology 发布了关于北海荷兰部分底拖网捕捞对底栖动物影响的新数据产品。底层渔业是全球食品供应的重要贡献者，但也显著影响海洋生态系统功能——渔具与海底的物理接触会导致沉积物变化和底栖生物直接死亡。该数据产品应用了渔业影响模型于底栖动物群，评估拖网捕捞的生态影响，为渔业影响评估和管理提供数据支撑。该产品通过 EMODnet 地图查看器可视化，体现了 EMODnet 在支持基于生态系统的渔业管理方面的持续贡献。',\n"
          "                'source': 'EMODnet Biology',\n"
          "                'url': 'https://emodnet.ec.europa.eu/en/',\n"
          "                'date': '2026-09-11',")
NEW_12 = ("                'abstract': 'EMODnet Biology 发布关于北海荷兰海域底拖网捕捞对底栖动物影响的新数据产品。产品基于 EMODnet Biology 前期开发的两个 R 包（Btrait 与 Bfiat，Soetaert & Beauchard）所构成的确定性建模框架：该框架描述拖网扰动期间底栖物种密度或生物量的衰减及其在两次捕捞事件之间的恢复过程，并以扰动状态下平均生物量或生态系统功能相对于扰动前状态的比例，定量表达捕捞影响。本产品将 Bfiat 方法应用于 EMODnet Biology 的底栖数据（荷兰所属北海部分，2009 年），量化底层捕捞如何与物种生活史性状相互作用，进而改变底栖生物量，以及底栖动物混合与生物灌溉沉积物的潜力（即沉积物的生物扰动与生物灌溉潜力，二者直接影响沉积物地球化学与全球生物地球化学循环）。理解底拖网渔具对底栖生命的影响，是正确评估渔业影响不可或缺的一步。',\n"
          "                'source': 'EMODnet Biology（NIOZ；Beauchard & Soetaert, 2026, Ecological Applications）',\n"
          "                'url': 'https://emodnet.ec.europa.eu/en/emodnet-biology-product-impacts-bottom-trawling-benthic-fauna-dutch-part-north-sea',\n"
          "                'date': '2026-09-11',")
s = one_replace(s, OLD_12, NEW_12, 'EMODnet Biology 条目：链接改产品页 + 摘要补细节')

# ---------- 4) 向阳红 10 号条目：修 404 链接 + 摘要补真实发现 ----------
OLD_14 = ("                'abstract': '向阳红 10 号科考船自 8 月 10 日起航赴西太平洋开展海底热液区联合科学考察。该航次由清华大学、青岛海洋地质研究所和上海交通大学联合组织，聚焦西太平洋海底热液系统的地质、化学与生物综合调查，包括热液喷口定位、流体采样、生物群落调查及海底地形测绘。航次于 9 月 11 日获媒体报道，是多方联合开展深海热液区科考的典型案例，对理解海底热液系统的成矿过程、极端环境生物多样性和深海生态系统功能具有重要意义。',\n"
          "                'source': '新华社 / 青岛海洋地质研究所',\n"
          "                'url': 'https://www.mnr.gov.cn/dt/hy/202609/t20260911_2830895.html',")
NEW_14 = ("                'abstract': '清华大学、中国地质调查局青岛海洋地质研究所、上海交通大学等单位联合开展的西太平洋海底热液活动与资源科考航次取得重要突破。科考队搭乘“向阳红 10”号科考船，于 8 月 10 日自深圳起航，历时 18 天，在位于我国专属经济区的西太平洋弧后盆地内实施 7 次探测器下潜作业。团队依托自主研制的深海可控式可视采样器（DCVS，国家自然科学基金重大科学仪器研制项目，清华大学自动化系牵头），在前期十多次探测、数十处高温热液喷口的基础上，精准锁定一处全新且规模巨大的海底热液活动矿区：伴生热液硫化物矿体由 3 个大型圆锥状矿体构成，主要矿物为黄铜矿、黄铁矿、闪锌矿；喷口位于水下约 700 至 1500 米，端元流体最高温度超过 315 ℃。对部分样品的初步分析显示，矿石中伴生金最高含量达 15.4 ppm、伴生银最高含量达 1271 ppm，金银平均含量显著优于陆地矿床。',\n"
          "                'source': '中国新闻网（转央视新闻客户端）',\n"
          "                'url': 'https://www.hn.chinanews.com.cn/news/gnxw/2026/0911/533649.html',")
s = one_replace(s, OLD_14, NEW_14, '向阳红 10 号条目：修 404 链接 + 摘要补真实发现')

# ---------- 5) 雪龙 2 号条目：修 404 链接 + 摘要补真实细节 ----------
OLD_15 = ("                'url': 'https://www.mnr.gov.cn/dt/hy/202609/t20260911_2830896.html',")
NEW_15 = ("                'url': 'https://cbgc.scol.com.cn/news/7945979',")
s = one_replace(s, OLD_15, NEW_15, '雪龙 2 号条目：修 404 链接')

OLD_15B = ("                'source': '新华社 / 自然资源部',\n"
           "                'url': 'https://cbgc.scol.com.cn/news/7945979',\n"
           "                'date': '2026-09-11',")
NEW_15B = ("                'source': '新华社（记者温竞华）· 经川观新闻转载',\n"
           "                'url': 'https://cbgc.scol.com.cn/news/7945979',\n"
           "                'date': '2026-09-11',")
s = one_replace(s, OLD_15B, NEW_15B, '雪龙 2 号条目：来源标注改为实测可访问来源')

# ---------- 5c) 雪龙 2 号条目：行级替换摘要（避开原文引号字符差异） ----------
NEW_15_ABS = ("                'abstract': '在北纬 80 度以北的北冰洋中央区，执行中国第 16 次北冰洋考察任务的“雪龙 2”号，为法国“塔拉极地站”科考平台破冰引航 110 海里，助其顺利抵达并固定于目标浮冰，开启首次北极越冬漂流考察。塔拉极地站是专门用于随北冰洋浮冰漂流观测的新型科考平台，自身航行与破冰能力较弱；2025 年中法双方达成意向，2026 年经自然资源部批准纳入本次考察任务。北京时间 9 月 8 日晚，正在马卡洛夫海盆开展海洋调查的“雪龙 2”号与塔拉极地站会合，两船保持约 300 米安全距离、以 4 至 7 节速度航行约 20 小时后于 9 日抵达目标浮冰；“雪龙 2”号从事先商定方向精准破入浮冰 100 多米开辟水道，确认浮冰无碎裂后退出，塔拉极地站沿水道驶入并锚定随冰漂流。两船告别后，“雪龙 2”号在附近多块浮冰布设冰基浮标，塔拉极地站亦协助布设一套，形成阵列协同开展海冰长期观测；因塔拉极地站途经俄罗斯以北海域遭遇气旋、油料消耗较多，“雪龙 2”号还应其请求提供船用燃油补给。',\n")
lines = s.split('\n')
hit = [i for i, l in enumerate(lines)
       if l.strip().startswith("'abstract': '中国第 16 次北冰洋科学考察中")]
if len(hit) != 1:
    print('  [FAIL] 雪龙 2 号摘要行命中 %d 行（应为 1）' % len(hit)); sys.exit(1)
print('  [OK] 雪龙 2 号条目：行级替换摘要（第 %d 行）' % (hit[0] + 1))
lines[hit[0]] = NEW_15_ABS.rstrip('\n')
s = '\n'.join(lines)

# ---------- 6) Ocean-E2E：补注预印本原始公开日 ----------
s = one_replace(s,
    "代码已在 GitHub 开源。',",
    "代码已在 GitHub 开源。（注：该工作的 arXiv 预印本 v1 首次公开于 2025 年 5 月，本条以 KDD 2026 会议报告日作为新闻时点。）',",
    'Ocean-E2E 补注预印本原始公开日')

io.open(P, 'w', encoding='utf-8').write(s)
print('')
print('差异统计: 原 %d 字符 -> 新 %d 字符' % (len(orig), len(s)))
print('patched: ' + P)
