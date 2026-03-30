#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
独立发送飞书机器人通知，带今日文档链接
"""
import requests
import os
from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y\u5e74%m\u6708%d\u65e5')

# 读取最新文档 URL
doc_url = ""
url_file = "C:/Users/Administrator/WorkBuddy/Claw/feishu_doc_url.txt"
if os.path.exists(url_file):
    with open(url_file, 'r', encoding='utf-8') as f:
        doc_url = f.read().strip()

print(f"[INFO] doc_url = {doc_url}")

webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')
if not webhook_url:
    print("[WARN] FEISHU_WEBHOOK_URL not set")
else:
    card_content = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": f"\U0001f30a \u6d77\u6d0bAI\u6280\u672f\u65e5\u62a5 \u00b7 {yesterday}"},
                "template": "blue"
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": (
                            "**\u4eca\u65e5\u6db5\u76d6\u4e3b\u9898\uff1a**\n"
                            "\U0001f916 \u6d77\u6d0b\u4eba\u5de5\u667a\u80fd | \U0001f310 \u6570\u5b57\u5b6a\u751f | \U0001f4ca \u53ef\u89c6\u5316 | "
                            "\u2705 \u6570\u636e\u8d28\u91cf | \u2699\ufe0f \u6570\u636e\u5904\u7406 | \U0001f5c4\ufe0f \u6570\u636e\u7ba1\u7406\u4e0e\u5171\u4eab | "
                            "\U0001f6a2 \u5f00\u653e\u822a\u6b21/\u8239\u65f6\u5171\u4eab | \U0001f3db\ufe0f \u6570\u636e\u4e2d\u5fc3 | \U0001f6e0\ufe0f \u5de5\u5177\u4e0e\u4ee3\u7801\u8d44\u6e90"
                        )
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"\U0001f4c4 **\u5b8c\u6574\u7b80\u62a5\uff08\u98de\u4e66\u6587\u6863\uff09\uff1a**\n{doc_url}"
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "note",
                    "elements": [
                        {"tag": "plain_text", "content": "\u7531 WorkBuddy \u81ea\u52a8\u751f\u6210 \u00b7 9\u4e2a\u65b9\u5411\u00b7 39\u6761\u52a8\u6001"}
                    ]
                }
            ]
        }
    }
    resp = requests.post(webhook_url, json=card_content, timeout=15)
    print(f"[OK] webhook result: {resp.json()}")
