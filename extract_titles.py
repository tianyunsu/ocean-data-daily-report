import re, sys

with open(r'C:\Users\Administrator\WorkBuddy\Claw\daily_reports\海洋AI简报_2026-04-07.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 提取所有条目标题
titles = re.findall(r'<div class="item-title">(.*?)</div>', html, re.DOTALL)
clean_titles = []
for t in titles:
    clean = re.sub(r'<[^>]+>', '', t).strip()
    if clean:
        clean_titles.append(clean)

print(f"=== 今日日报（2026-04-07）共 {len(clean_titles)} 条 ===")
for i, t in enumerate(clean_titles, 1):
    print(f"{i}. {t}")

# 提取链接
links = re.findall(r'href="(https?://[^"]+)"', html)
print(f"\n=== 共 {len(links)} 个链接 ===")
for link in links:
    # 只打印正文中的链接，排除导航链接
    if 'github.com' in link or 'arxiv' in link or 'doi.org' in link or 'springer' in link or 'sciencedirect' in link or 'frontiersin' in link or 'noaa' in link or 'wmo' in link or 'eurekalert' in link or 'vliz' in link or 'lr.org' in link or 'copernicus' in link or 'nature' in link or 'iop' in link or 'oceanbestpractices' in link or 'pangaea' in link or 'eosc' in link:
        print(f"  {link}")
