#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, requests

doc_url = ''
try:
    with open('feishu_doc_url.txt', 'r', encoding='utf-8') as f:
        doc_url = f.read().strip()
    print('doc_url:', doc_url)
except Exception as e:
    print('no doc_url:', e)

webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')
if not webhook_url:
    print('FEISHU_WEBHOOK_URL not set, skip')
else:
    doc_link_text = doc_url if doc_url else '文档URL未获取'
    card_content = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": "海洋AI技术日报 2026-03-31"},
                "template": "blue"
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": "**今日涵盖9大主题：**\n海洋AI | 数字孪生 | 可视化 | 数据质量 | 数据处理 | 数据管理与共享 | 开放航次 | 数据中心 | 工具代码"
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": "飞书文档：" + doc_link_text
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "note",
                    "elements": [{"tag": "plain_text", "content": "由 WorkBuddy 自动生成 · 每日09:00推送"}]
                }
            ]
        }
    }
    resp = requests.post(webhook_url, json=card_content, timeout=15)
    print('webhook result:', resp.json())

print('done')
