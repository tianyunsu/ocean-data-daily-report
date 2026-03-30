#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime, timedelta

webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/84da8bbf-9ccf-4179-b8da-1f0e9739f9ae'

yesterday_cn = (datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')
date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

print("="*70)
print("推送海洋AI日报到飞书")
print("="*70)

card = {
    "msg_type": "interactive",
    "card": {
        "header": {
            "title": {"tag": "plain_text", "content": f"海洋AI技术日报 · {yesterday_cn}"},
            "template": "blue"
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**本期主题** 海洋人工智能 | 海洋数字孪生 | 数据质量 | 数据处理 | 数据管理 | 开放航次"
                }
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {"tag": "lark_md", "content": f"**资讯数量** 31条\n**生成日期** {date_str}"}
            },
            {"tag": "hr"},
            {
                "tag": "note",
                "elements": [{"tag": "plain_text", "content": "WorkBuddy 海洋AI日报系统"}]
            }
        ]
    }
}

print("\n[1] 发送消息卡片...")
print(f"Webhook: {webhook_url[:60]}...")

try:
    resp = requests.post(webhook_url, json=card, timeout=10)
    result = resp.json()
    
    print(f"\n[2] 服务器响应:")
    print(f"    状态码: {resp.status_code}")
    print(f"    返回代码: {result.get('code')}")
    print(f"    返回消息: {result.get('msg')}")
    
    if result.get('code') == 0:
        print("\n[✓] 推送成功！消息已发送到飞书群组。")
    else:
        print(f"\n[×] 推送失败: {result}")
        
except Exception as e:
    print(f"\n[×] 错误: {e}")

print("\n" + "="*70)
