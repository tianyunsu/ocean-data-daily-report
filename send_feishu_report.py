#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接推送海洋AI日报到飞书群组
"""

import requests
import os
import sys
from datetime import datetime, timedelta

# 获取昨天的日期
yesterday_cn = (datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')
date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

print("=" * 60)
print("海洋AI日报 - 飞书推送")
print("=" * 60)
print(f"目标日期: {yesterday_cn} ({date_str})")

# ============================================================
# 步骤 1：检查飞书Webhook配置
# ============================================================
print("\n[步骤1] 检查飞书Webhook配置...")
webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')

if not webhook_url:
    print("ERROR: FEISHU_WEBHOOK_URL 环境变量未配置")
    sys.exit(1)

print(f"OK: Webhook URL 已配置")

# ============================================================
# 步骤 2：构建消息卡片
# ============================================================
print("\n[步骤2] 构建消息卡片...")

card_content = {
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
                    "content": "**今日涵盖主题：**\n\n海洋人工智能 | 海洋数字孪生 | 海洋可视化 | 海洋数据质量 | 海洋数据处理 | 海洋数据管理与共享 | 开放航次/船时共享"
                }
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**本期资讯数量：** 31条研究进展\n\n**报告类型：** HTML简报 + 飞书云文档\n\n**生成时间：** 自动化每日09:00执行"
                }
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**详细内容：**\n\n1. HTML简报：daily_reports/海洋AI简报_" + date_str + ".html\n\n2. 飞书云文档：查看 feishu_doc_url.txt\n\n3. 本次执行记录：.codebuddy/automations/ai/memory.md"
                }
            },
            {"tag": "hr"},
            {
                "tag": "note",
                "elements": [
                    {
                        "tag": "plain_text",
                        "content": "由 WorkBuddy 海洋AI日报自动化系统生成 | 每日09:00推送"
                    }
                ]
            }
        ]
    }
}

print("OK: 消息卡片构建完成")

# ============================================================
# 步骤 3：发送到飞书机器人
# ============================================================
print("\n[步骤3] 发送消息到飞书群组...")

try:
    response = requests.post(webhook_url, json=card_content, timeout=15)
    result = response.json()
    
    if result.get('code') == 0:
        print(f"✓ 消息推送成功！")
        print(f"  返回代码: {result.get('code')}")
        print(f"  返回消息: {result.get('msg')}")
    else:
        print(f"ERROR: 推送失败")
        print(f"  返回代码: {result.get('code')}")
        print(f"  返回消息: {result.get('msg')}")
        sys.exit(1)
        
except Exception as e:
    print(f"ERROR: 网络请求异常: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("推送完毕")
print("=" * 60)
