# -*- coding: utf-8 -*-
"""deploy_0903.py — 发布 2026-09-03 日报：复制到 posts/ 并更新 index.html"""
import re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

TODAY = '2026-09-03'
shutil.copy(f'daily_reports/海洋AI简报_{TODAY}.html', f'posts/{TODAY}.html')
print('copied ->', f'posts/{TODAY}.html')

ABSTRACT = (
    '季节感知混合卷积-Transformer 南极海冰浓度预报（arXiv 09-01）；'
    'KSG-Net 海上三维船舶 LiDAR 检测（arXiv 09-02）；'
    'Enhanced Crossformer 双塔多浮标有效波高预报（JMSE 09-02）；'
    '单变量深度学习波高预报收益边界测评（Ocean Engineering 08-31）；'
    '海上风机剩余寿命无标签预测双路径网络（JMSE 09-01）；'
    'Eco Wave Power 联手 AI engineering 共建波浪能 AI 数字孪生平台（09-02）；'
    '红海全球目的地 10 平方公里陆海一体化数字孪生（09-02）；'
    '连云港空天地一体化智慧渔港数字孪生（09-01）；'
    'CMEMS《Mediterranean in Motion》地中海增温可视化叙事（08-28）；'
    '海洋碳数据表征质量量化框架（arXiv 08-31）；'
    'HarmoCore 函数潜在扩散振荡波场稀疏重建（arXiv 09-02）；'
    'AUWave 稀疏浮标区域波高场重建（Ocean Engineering 08-31）；'
    '我国首本海洋科学数据期刊 DEOS 正式上线（09-01）；'
    '海洋四所参加 SOOS 与 SCAR 开放科学大会（09-02）；'
    '2026"蓝梦同航"联合海洋调查实习航次青岛启航（08-29）；'
    'Nautilus NA181 威克岛二战沉船考古搜索窗口开启（09-01）；'
    'OSI SAF 基于 AMSR3 的海冰产品转为业务化（09-01）；'
    'NOAA CO-OPS 潮汐基准分析计算器 TADC 升级（09-01）'
)

DIGEST = (
    '南极海冰预报与海上三维感知双线并进；波浪能 AI 数字孪生落地；'
    '我国首本海洋科学数据期刊 DEOS 上线；OSI SAF 海冰产品切换 AMSR3'
)

# ---------- index.html ----------
p = 'index.html'
s = open(p, encoding='utf-8').read()

# 1) 更新头部描述中的条数
s = re.sub(r'9 个研究方向 · \d+ 条精选资讯', '9 个研究方向 · 18 条精选资讯', s)

# 2) 定位第一个 post-card，插入新卡片
anchor = s.find('<div class="post-card"')
if anchor == -1:
    raise RuntimeError('未找到 post-card 锚点')

card = f'''<div class="post-card">
                <div class="post-header">
                    <a href="posts/{TODAY}.html" class="post-title">海洋AI技术日报 · {TODAY}（周四）</a>
                    <span class="post-date">{TODAY}</span>
                </div>
                <p class="post-excerpt">9 个研究方向 · 18 条精选资讯。{DIGEST}。</p>
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

# 尝试定位 2026年09月 分组
m = re.search(r'(<h2>[^<]*2026年09月[^<]*</h2>\s*<ul>)', a)
if m:
    ins_at = m.end()
    newli = (f'<li><a href="posts/{TODAY}.html"><strong>{TODAY}</strong></a>'
             f'（周四） · 9个方向 · 18条动态 · 重点：{ABSTRACT}等。</li>\n')
    a = a[:ins_at] + newli + a[ins_at:]
else:
    # 新建 09 月分组，插到 08 月分组之前
    m2 = re.search(r'<div class="archive-group">\s*<h2>[^<]*2026年08月[^<]*</h2>', a)
    if not m2:
        raise RuntimeError('未找到 2026年08月 分组')
    grp = (f'<div class="archive-group">\n<h2>📅 2026年09月</h2>\n<ul>\n'
           f'<li><a href="posts/{TODAY}.html"><strong>{TODAY}</strong></a>'
           f'（周四） · 9个方向 · 18条动态 · 重点：{ABSTRACT}等。</li>\n</ul>\n</div>\n')
    a = a[:m2.start()] + grp + a[m2.start():]

open(p2, 'w', encoding='utf-8').write(a)
print('archive.html updated')

# 校验
for f in (p, p2):
    t = open(f, encoding='utf-8').read()
    print(f'{f}: 09-03 出现 {t.count(TODAY)} 次')
