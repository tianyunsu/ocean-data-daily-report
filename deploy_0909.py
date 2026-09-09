# -*- coding: utf-8 -*-
"""deploy_0909.py — 发布 2026-09-09 日报：复制到 posts/ 并更新 index.html / archive.html"""
import re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

TODAY = '2026-09-09'
TOTAL = 13
WEEKDAY = '周三'
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
    'Neptune：CNN+球面傅里叶神经算子构建的全球海洋—海冰次季节 AI 模拟器，稳定预报 60 天（arXiv 09-08）；'
    '"丝路海运"北极航线气象导航服务启用：风云卫星+AI 提供 15 天逐日海冰预报（09-08）；'
    'SKANN 原始波形选择性核声学网络实现开放集跨航次船舶再识别（arXiv 09-07）；'
    '把视觉基础模型适配到声呐，首次实现无位姿三维声呐重建（arXiv 09-05）；'
    'DARB 方向非对称 realism 桥实现单一模型双向声呐—光学翻译（arXiv 09-05）；'
    '"丝路海运"港口气象风险智能体：58 座中外港口气象风险集中展示，据称国际首创（09-08）；'
    '水域时间序列异常检测机器学习综述：覆盖 106 篇文献（Water 09-05）；'
    '图神经网络用于海图变化关键性分类评测（arXiv 09-02）；'
    '小批量风险规避深度 Q 学习：以水下机器人导航为案例（arXiv 09-07）；'
    'CORD 获"海洋十年"认可：开放数字公共基础设施整合南亚东南亚沿海数据（IOC 09-04）；'
    '"深海一号"搭载"蛟龙"号从青岛起航执行新一轮深海科考（人民日报 09-06）；'
    'EastAsiaClimateExtremes：东亚大气—海洋极端事件 AI-Ready 数据集（arXiv 09-08）；'
    'cstar-ocean 发布 0.13.5：海洋碳循环可复现建模工作流工具（PyPI 09-05）'
)
# 剔除"暂无新增"占位，摘要只保留真实条目
ABSTRACT = '；'.join(
    x for x in ABSTRACT.split('；') if '暂无新增' not in x
)
ABSTRACT = dedup_on_semicolon(ABSTRACT)

DIGEST = (
    '全球海洋—海冰次季节 AI 模拟器 Neptune 可稳定预报 60 天；'
    '"丝路海运"北极航线气象导航服务启用，风云卫星+AI 做 15 天海冰预报；'
    '"深海一号"搭载"蛟龙"号起航；'
    '东亚大气—海洋极端事件 AI-Ready 数据集发布'
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
                    <a href="posts/{TODAY}.html" class="post-title">海洋AI技术日报 · {TODAY}（{WEEKDAY}）</a>
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
         f'（{WEEKDAY}） · 9个方向 · {TOTAL}条动态 · 重点：{ABSTRACT}等。</li>\n')

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
