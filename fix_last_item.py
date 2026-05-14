# -*- coding: utf-8 -*-
with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_sub = 'Biogeosciences'
idx = content.find(old_sub)
# Find where this item starts (after }, {)
item_start = content.rfind(", {'", 0, idx)
print(f"Item starts at: {item_start}")
print(f"Found context: {repr(content[item_start:idx+50])}")

# Find the closing of the Biogeosciences item
# It ends with }} after the date field
date_literal = "'date': '2026-01-12'"
date_pos = content.index(date_literal)
# After the date, we have '}} (item close) and then ]}] (items+section+SECTIONS close)
after_date = content[date_pos + len(date_literal):]
close_bracket = after_date.index('}')
item_end = date_pos + len(date_literal) + close_bracket + 1
print(f"Item ends at: {item_end}")
print(f"After item: {repr(content[item_end:item_end+20])}")

old_item = content[item_start:item_end]
print(f"\nOld item length: {len(old_item)}")
print(f"Old item: {repr(old_item[:100])}...")

new_item = ", {'title': '4. OceanPredict AI-TT（2026-04-13）：ML海洋预报方法、应用与挑战国际研讨会——汇聚全球海洋预测AI前沿进展', 'badge': '近7天', 'abstract': 'OceanPredict AI任务组（AI Task Team）于2026年4月13-14日在加拿大蒙特利尔召开ML海洋预报国际研讨会，主题为\"Machine Learning for Ocean Prediction: Methods, Applications & Challenges\"。为期2天的会议汇聚全球海洋预测领域ML研究进展，涵盖端到端学习型预报、数据驱动状态估计、物理约束神经网络、海洋次网格过程参数化和集合预报等核心议题，并特别讨论ML模型在业务化海洋预报系统中的部署挑战与可信度评估方法，是2026年海洋AI预报领域最重要的学术交流活动之一。', 'source': 'OceanPredict / Mercator Ocean International', 'url': 'https://www.mercator-ocean.eu/event/oceanpredict-ai-task-team-workshop/', 'date': '2026-04-13'}"
# The old item ends with }} but we need }} for items+section close
# Old: ...'date': '2026-01-12'}}  -> ends with }}
# New: should end with }} too
new_item = new_item.strip()

if old_item in content:
    content = content.replace(old_item, new_item)
    with open('feishu_write_doc.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("\nReplacement successful!")
else:
    print("\nNOT FOUND")
