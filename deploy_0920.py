# -*- coding: utf-8 -*-
"""Deploy 2026-09-20 report: update index.html + archive.html (insert at top)."""

CARD = '''    <div class="post-card">
                <div class="post-header">
                    <a href="posts/2026-09-20.html" class="post-title">海洋AI技术日报 · 2026-09-20（周日）</a>
                    <span class="post-date">2026-09-20</span>
                </div>
                <p class="post-excerpt">9 个研究方向 · 27 条精选资讯。OceanMoE 条件稀疏专家混合框架用于长时程多变量海洋预报（arXiv 09-17）；中国首个海洋 Token 工厂发布、汇聚 130 多类涉海数据与 20 余个海洋大模型（中新社 09-18）；Drift Field Net 学习海洋拉格朗日漂移场、定位误差较业务模式减小约 20 公里（arXiv 09-14）；海冰类型预测重构为弱监督多标签比例学习、MAE 最高降 21.5%（arXiv 09-14）；PAMGuard 3D 鲸类声定位器重大未报告误差（arXiv 09-17）；UniqueShip 水声船舶分类防数据泄漏基准 4218 船 2460 小时（arXiv 09-12）；GDCM-EOF 自监督叶绿素 a 时空重构、加勒比海 R² 升至 0.998（J. Remote Sensing 09-07）；SeaExplorer 滑翔机开源 QC 管线（Frontiers 09-07）；多波束水体数据全扫幅深度学习底检测（JMSE 09-09）；UN 海洋十年《海洋数据共享与国家安全》讨论稿征询至 9 月底；中国-海管局联合中心深海科研项目落地青岛（09-18）；Copernicus Sentinel-3C 发射成功（09-15）；CMEMS 第 10 期海洋状况报告 OSR10 将于 9 月 30 日发布；《中国海洋发展指数报告 2026》发布（09-17）；PX4 空-海两栖固件、SPAR LLM 故障恢复平台、HoloOcean 沿岸场景生成等工具更新。</p>
                <div class="post-tags">
                    <span class="tag">海洋AI</span>
                    <span class="tag">可视化</span>
                    <span class="tag">数据质量</span>
                    <span class="tag">数据处理</span>
                    <span class="tag">数据共享</span>
                    <span class="tag">开放航次</span>
                    <span class="tag">数据中心</span>
                    <span class="tag">工具资源</span>
                </div>
            </div>
'''

ARCHIVE_LI = '<li><a href="posts/2026-09-20.html"><strong>2026-09-20</strong></a>（周日） · 8个方向 · 27条动态（D2数字孪生暂无新增） · 重点：OceanMoE 条件稀疏专家混合框架用于长时程多变量海洋预报（arXiv 09-17）；2026海洋合作发展论坛发布中国首个海洋 Token 工厂、汇聚 130 多类涉海数据与 20 余个海洋大模型（中新社 09-18）；Drift Field Net 学习海洋拉格朗日漂移场、定位误差较业务模式减小约 20 公里（arXiv 09-14）；海冰类型预测重构为弱监督多标签比例学习（arXiv 09-14）；OceanSim 合成数据规模化海洋感知、真实海胆检测验证（arXiv 09-17）；稀疏视角水下 3D 高斯泼溅密集几何先验（arXiv 09-16）；分类学条件控制的浮游生物图像生成（arXiv 09-10）；LOTUSim-Energy 海事人-无人机交互仿真平台（arXiv 09-15）；PAMGuard 3D 鲸类声定位器重大未报告误差（arXiv 09-17）；UniqueShip 水声船舶分类防数据泄漏基准（arXiv 09-12）；多冰图不确定性感知海冰类型制图（arXiv 09-08）；SeaExplorer 滑翔机开源 QC 管线（Frontiers 09-07）；GDCM-EOF 自监督叶绿素 a 时空重构（J. Remote Sensing 09-07）；高光谱叶绿素反演光谱信息量化（arXiv 09-16）；AquaCubeAI Φsat-2 星上浊度监测（arXiv 09-11）；多会话声光多模态水下建图因子图优化（arXiv 09-15）；多波束水体数据全扫幅深度学习底检测（JMSE 09-09）；UN 海洋十年《海洋数据共享与国家安全》讨论稿征询至 9 月底（08-27 豁免）；"海洋十年"海洋公益行动全球倡议（09-19 转载稿）；中国-海管局联合中心深海科研项目落地青岛（09-18）；CougarTail 与 CUB 开源水下耐压舱电子套件（arXiv 09-09）；Copernicus Sentinel-3C 发射成功（09-15）；CMEMS OSR10 十周年报告 9 月 30 日发布（09-04 豁免）；《中国海洋发展指数报告 2026》发布（09-17）；PX4 空-海两栖固件（arXiv 09-17）；SPAR LLM 驱动 AUV 故障恢复闭环仿真平台（arXiv 09-17）；HoloOcean 沿岸环境自动生成管线（arXiv 09-09）等。</li>\n'

# index.html
idx = open('index.html', encoding='utf-8').read()
anchor = '    <div class="post-card">\n                <div class="post-header">\n                    <a href="posts/2026-09-15.html"'
if 'posts/2026-09-20.html' in idx:
    print('index: already inserted')
elif anchor not in idx:
    raise SystemExit('ERROR: index anchor not found')
else:
    idx = idx.replace(anchor, CARD + anchor, 1)
    open('index.html', 'w', encoding='utf-8').write(idx)
    print('index: inserted 09-20 card')

# archive.html
arch = open('archive.html', encoding='utf-8').read()
arch_anchor = '<ul><li><a href="posts/2026-09-15.html">'
if 'posts/2026-09-20.html' in arch:
    print('archive: already inserted')
elif arch_anchor not in arch:
    raise SystemExit('ERROR: archive anchor not found')
else:
    arch = arch.replace(arch_anchor, '<ul>' + ARCHIVE_LI + '<li><a href="posts/2026-09-15.html">', 1)
    open('archive.html', 'w', encoding='utf-8').write(arch)
    print('archive: inserted 09-20 li')
