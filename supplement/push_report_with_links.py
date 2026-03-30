#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报推送脚本 - 增强版（含可点击链接）
"""
import requests
import json
import os
from datetime import datetime, timedelta

webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/84da8bbf-9ccf-4179-b8da-1f0e9739f9ae'

yesterday_cn = (datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')
date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

print("="*70)
print("海洋AI日报推送 - 增强版（含可点击链接）")
print("="*70)

# 读取飞书文档链接
doc_url = ""
try:
    if os.path.exists('feishu_doc_url.txt'):
        with open('feishu_doc_url.txt', 'r', encoding='utf-8') as f:
            doc_url = f.read().strip()
            print(f"\n[1] 读取飞书文档URL成功")
            print(f"    URL: {doc_url[:60]}...")
except Exception as e:
    print(f"警告: 无法读取文档URL: {e}")

# 构建卡片消息
card = {
    "msg_type": "interactive",
    "card": {
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"海洋AI技术日报 · {yesterday_cn}"
            },
            "template": "blue"
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**📅 日报日期**\n{date_str}\n\n**📊 今日主题**\n🤖 海洋人工智能 | 🌐 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理 | 🗄️ 数据管理 | 🚢 开放航次"
                }
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**📈 本期资讯统计**\n• 总计资讯: 31 条\n• 覆盖方向: 7 个\n• 涵盖领域: 海洋AI与数据科学"
                }
            },
            {"tag": "hr"}
        ]
    }
}

# 添加文档链接（如果有的话）
if doc_url:
    card["card"]["elements"].append({
        "tag": "div",
        "text": {
            "tag": "lark_md",
            "content": f"**📄 完整日报（飞书云文档）**\n[点击查看31条完整资讯]({doc_url})\n\n*支持搜索、评论、分享*"
        }
    })
else:
    card["card"]["elements"].append({
        "tag": "div",
        "text": {
            "tag": "lark_md",
            "content": "**📄 完整日报**\n查看 `feishu_doc_url.txt` 获取云文档链接"
        }
    })

card["card"]["elements"].append({"tag": "hr"})

# 添加底部信息
card["card"]["elements"].append({
    "tag": "div",
    "text": {
        "tag": "lark_md",
        "content": "**📁 相关文件**\n• HTML报告: `daily_reports/海洋AI简报_" + date_str + ".html`\n• 执行记录: `.codebuddy/automations/ai/memory.md`"
    }
})

card["card"]["elements"].append({"tag": "hr"})

card["card"]["elements"].append({
    "tag": "note",
    "elements": [
        {
            "tag": "plain_text",
            "content": "由 WorkBuddy 海洋AI日报自动化系统生成 | 每日09:00推送"
        }
    ]
})

print("\n[2] 构建消息卡片完成")
print(f"    包含文档链接: {bool(doc_url)}")

# 发送到飞书
print("\n[3] 发送消息到飞书群组...")

try:
    resp = requests.post(webhook_url, json=card, timeout=10)
    result = resp.json()
    
    code = result.get('code')
    msg = result.get('msg')
    
    print(f"\n[4] 服务器响应:")
    print(f"    HTTP状态码: {resp.status_code}")
    print(f"    返回代码: {code}")
    print(f"    返回消息: {msg}")
    
    if code == 0:
        print(f"\n[✓] 推送成功！")
        print(f"    消息已发送到飞书群组")
        print(f"    群组中可见可点击的飞书文档链接")
    else:
        print(f"\n[×] 推送失败")
        
except Exception as e:
    print(f"[×] 错误: {e}")

print("\n" + "="*70)
