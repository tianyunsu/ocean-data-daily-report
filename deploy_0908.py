# -*- coding: utf-8 -*-
"""deploy_0908.py — 发布 2026-09-08 日报：复制到 posts/ 并更新 index.html / archive.html"""
import re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

TODAY = '2026-09-08'
TOTAL = 13
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
    'NWM 神经波浪模型：国际上首个 AI+数值模式混合海浪模型（Ocean Engineering 09-06）；'
    'AquaBEV 以 3D 声呐监督从单目水下图像预测 BEV 占用（arXiv 09-03）；'
    'SEMI-DETR 半监督检测：34 张标注图让白鲸幼鲸检出超越监督基线（Front. Mar. Sci. 09-04）；'
    '气旋轨迹硬编码反损孟加拉湾海洋模拟器技巧（arXiv 09-04）；'
    'Fugro 加入欧盟 OCEANITY 共建欧洲数字孪生海洋 EDITO 应用（09-07）；'
    'A-Predator 各向异性核点卷积的多波束测深点云配准（Remote Sensing 09-05）；'
    'DenseNet-121 跨河口颜色锋识别泛化研究（JMSE 09-06）；'
    'EMODnet 生物与海床栖息地 392 万欧元新招标、截止 10-23（EuroGOOS 09-03）；'
    '雪龙2号冰站无人机远距投放海冰浮标+抗低温磁探无人机原型测试（新华社 09-05）；'
    '国家极地科学数据中心 2026 开放课题：设极地 AI-Ready 数据集与模型构建方向（09-04）；'
    '南海海洋大数据智能管理平台：130TB 入库+AI 识别+海洋数字孪生（《中国测绘》09-04）；'
    'Mini-Girona I-AUV 开源干预型水下机器人平台（arXiv 09-02）；'
    'Underwater Acoustic Channel Library 水声信道开源库（arXiv 09-02）'
)
# 剔除两条"暂无新增"占位，摘要只保留真实条目
ABSTRACT = '；'.join(
    x for x in ABSTRACT.split('；') if '暂无新增' not in x
)
ABSTRACT = dedup_on_semicolon(ABSTRACT)

DIGEST = (
    '国际上首个 AI+数值模式混合海浪模型（NWM）发布；'
    '以声呐为监督让水下机器人看懂三维占用空间；'
    '雪龙2号冰站无人机投放浮标+磁探无人机测试；'
    '国家极地科学数据中心设 AI-Ready 数据集开放课题'
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
                    <a href="posts/{TODAY}.html" class="post-title">海洋AI技术日报 · {TODAY}（周二）</a>
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
         f'（周二） · 9个方向 · {TOTAL}条动态 · 重点：{ABSTRACT}等。</li>\n')

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
