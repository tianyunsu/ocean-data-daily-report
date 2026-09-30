#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
独立发送飞书机器人通知（当日日期 + 动态条数自动计算）

修复记录（2026-09-30）：
  - 原实现硬编码 (now - 1 day) 与「39 条动态」，会误发昨日日期与旧条数；
  - 现改为：日期取当日、条数与方向数从 feishu_write_doc.py 的 SECTIONS 实时解析，
    并补充 GitHub Pages 链接。若 SECTIONS 解析失败则回退为“今日”。
"""
import ast
import os
from datetime import datetime

import requests

TODAY_CN = datetime.now().strftime('%Y年%m月%d日')
SITE = "https://tianyunsu.github.io/ocean-data-daily-report/"

# --- 从 feishu_write_doc.py 解析 SECTIONS，动态统计条数与方向数 ---
n_items, n_dirs = None, None
try:
    with open('feishu_write_doc.py', 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == 'SECTIONS':
                    secs = ast.literal_eval(node.value)
                    n_dirs = sum(1 for s in secs if s.get('items'))
                    n_items = sum(len(s['items']) for s in secs)
                    break
        if n_items is not None:
            break
except Exception as e:  # noqa: BLE001
    print(f"[WARN] SECTIONS 解析失败，回退默认值：{e}")

summary = f"{n_dirs} 个方向 · {n_items} 条动态" if n_items else "今日"

# 读取最新文档 URL
doc_url = ""
url_file = "C:/Users/Administrator/WorkBuddy/Claw/feishu_doc_url.txt"
if os.path.exists(url_file):
    with open(url_file, 'r', encoding='utf-8') as f:
        doc_url = f.read().strip()

print(f"[INFO] date={TODAY_CN} summary={summary} doc_url={doc_url}")

webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')
if not webhook_url:
    print("[WARN] FEISHU_WEBHOOK_URL not set")
else:
    doc_line = doc_url if doc_url else SITE
    card_content = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": f"\U0001f30a 海洋AI技术日报 · {TODAY_CN}"},
                "template": "blue"
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": (
                            "**今日涵盖主题：**\n"
                            "\U0001f916 海洋人工智能 | \U0001f310 数字孪生 | \U0001f4ca 可视化 | "
                            "\u2705 数据质量 | \u2699\ufe0f 数据处理 | \U0001f5c4\ufe0f 数据管理与共享 | "
                            "\U0001f6a2 开放航次/科考 | \U0001f3db\ufe0f 数据中心 | \U0001f6e0\ufe0f 工具与代码资源"
                        )
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"\U0001f4c4 **完整简报：**\n{doc_line}\n\U0001f310 **网站：**\n{SITE}"
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "note",
                    "elements": [
                        {"tag": "plain_text", "content": f"由 WorkBuddy 自动生成 · {summary}"}
                    ]
                }
            ]
        }
    }
    resp = requests.post(webhook_url, json=card_content, timeout=15)
    print(f"[OK] webhook result: {resp.json()}")
