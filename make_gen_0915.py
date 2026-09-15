# -*- coding: utf-8 -*-
"""make_gen_0915.py — 由 gen_html_0914.py 派生 gen_html_0915.py（改日期/星期/页脚来源声明）"""
src = 'gen_html_0914.py'
dst = 'gen_html_0915.py'

with open(src, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("TODAY = '2026-09-14'", "TODAY = '2026-09-15'")
c = c.replace("TODAY_CN = '2026年09月14日'", "TODAY_CN = '2026年09月15日'")
c = c.replace('· 周日', '· 周二')
c = c.replace(
    'Powered by WorkBuddy AI · Data sources: arXiv, GitHub, CMEMS, NOAA, CNKI and more',
    'Powered by WorkBuddy AI · 本期来源：arXiv、中科院海洋所、科学网、npj Ocean Sustainability、Ocean Science、Climate Dynamics、JGR: Oceans、CMEMS、PyPI、Parcels 官方博客、IODP-China、新华社',
)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(c)

print('generated', dst)
print('checks: TODAY ok =', "TODAY = '2026-09-15'" in c)
print('checks: footer ok =', '本期来源' in c)
print('checks: no stale date =', '2026-09-14' not in c)
