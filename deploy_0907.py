# -*- coding: utf-8 -*-
"""deploy_0907.py — 发布 2026-09-07 日报：复制到 posts/ 并更新 index.html / archive.html"""
import re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

TODAY = '2026-09-07'
TOTAL = 15
shutil.copy(f'daily_reports/海洋AI简报_{TODAY}.html', f'posts/{TODAY}.html')
print('copied ->', f'posts/{TODAY}.html')


def dedup_on_semicolon(seg: str) -> str:
    """按中文分号切分后做去标点归一化去重（09-02 archive 重复事故对策）"""
    parts = seg.split('；')
    seen, out = [], []
    for x in parts:
        k = re.sub(r'[^一-龥A-Za-z0-9]', '', x)
        if k and k in seen:
            continue
        seen.append(k)
        out.append(x)
    return '；'.join(out)


ABSTRACT = (
    'MHWCorrNet 可解释深度学习订正 ECMWF 次季节海洋热浪预报、全球 CSI 提升约 9%（JGR: MLC 09-01）；'
    '本体 + 多 LLM 的 AUV 共享自主认知架构（arXiv 08-29）；'
    'SurgeGen 两阶段扩散合成风暴潮情景（arXiv 09-03）；'
    'EchoST-SSL 面向渔业回声探测的自监督时空表征（IEEE Sensors Journal 09-03）；'
    'RFA+RCSA 轻量化水下海洋垃圾检测器（Sustainability 09-02）；'
    '面向海洋数字孪生本方向今日暂无新增符合时效要求的动态；'
    '面向海洋可视化本方向今日暂无新增符合时效要求的动态；'
    'PhyEnv-GAN 融合运动学约束与海况的船舶行为异常检测（Ocean Engineering 09-01）；'
    'S-DEIM 仅需 0.2% 格点观测重建高分辨率 SST 场（JGR: MLC 08-27）；'
    '以海滩为标尺把近岸潮汐分辨率从 10 km 提升到 100 m（Communications Earth & Environment 09-01）；'
    'MITECO 与 IEO-CSIC 签署 2576 万欧元海洋战略科学基础新协议（09-01）；'
    'NSF 就未来海洋观测优先级公开征询、截止 9 月 30 日（OOIFB）；'
    'MBARI 海山热点航次 ROV 在 3277 m 拍到罕见大鳍鱿鱼（09-02）；'
    'OSIL 发布 3.0 米海洋观测浮标（09-04）；'
    '美国 BGC-Argo 浮标网络面临联邦资金 10 月中断（09-03）；'
    'EMODnet 首次纳入欧洲游艇码头数据、统一 50 泊位口径（09-01）；'
    'coops-mcp 0.1.1 发布把 NOAA CO-OPS 潮汐水位数据接入 MCP（PyPI 09-04）'
)
# 剔除两条"暂无新增"占位，摘要只保留真实条目
ABSTRACT = '；'.join(
    x for x in ABSTRACT.split('；') if '暂无新增' not in x
)
ABSTRACT = dedup_on_semicolon(ABSTRACT)

DIGEST = (
    '可解释深度学习把 S2S 海洋热浪预报技巧提升约 9%；'
    '本体增强多 LLM 架构推动 AUV 共享自主；'
    'S-DEIM 用 0.2% 观测重建高分辨率 SST；'
    'coops-mcp 让 AI 助手直连 NOAA 潮汐数据'
)

# ---------- index.html ----------
p = 'index.html'
s = open(p, encoding='utf-8').read()

s = re.sub(r'9 个研究方向 · \d+ 条精选资讯', f'9 个研究方向 · {TOTAL} 条精选资讯', s)

anchor = s.find('<div class="post-card"')
if anchor == -1:
    raise RuntimeError('未找到 post-card 锚点')

card = f'''<div class="post-card">
                <div class="post-header">
                    <a href="posts/{TODAY}.html" class="post-title">海洋AI技术日报 · {TODAY}（周一）</a>
                    <span class="post-date">{TODAY}</span>
                </div>
                <p class="post-excerpt">9 个研究方向 · {TOTAL} 条精选资讯。{DIGEST}。</p>
                <div class="post-tags">
                    <span class="tag">海洋AI</span>
                    <span class="tag">数字孪生</span>
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
s = s[:anchor] + card + s[anchor:]
open(p, 'w', encoding='utf-8').write(s)
print('index.html updated')

# ---------- archive.html ----------
p2 = 'archive.html'
a = open(p2, encoding='utf-8').read()

newli = (f'<li><a href="posts/{TODAY}.html"><strong>{TODAY}</strong></a>'
         f'（周一） · 9个方向 · {TOTAL}条动态 · 重点：{ABSTRACT}等。</li>\n')

m = re.search(r'(<h2>[^<]*2026年09月[^<]*</h2>\s*<ul>)', a)
if m:
    a = a[:m.end()] + newli + a[m.end():]
else:
    m2 = re.search(r'<div class="archive-group">\s*<h2>[^<]*2026年08月[^<]*</h2>', a)
    if not m2:
        raise RuntimeError('未找到 2026年08月 分组')
    grp = (f'<div class="archive-group">\n<h2>📅 2026年09月</h2>\n<ul>\n{newli}</ul>\n</div>\n')
    a = a[:m2.start()] + grp + a[m2.start():]

open(p2, 'w', encoding='utf-8').write(a)
print('archive.html updated')

for f in (p, p2):
    t = open(f, encoding='utf-8').read()
    print(f'{f}: {TODAY} 出现 {t.count(TODAY)} 次')
