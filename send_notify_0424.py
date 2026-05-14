#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发送飞书机器人通知 - 修正版 2026-04-24"""
import requests, os, sys
from datetime import datetime

date_str = '2026-04-24'
yesterday_cn = '2026年04月24日'

webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')

card_content = {
    "msg_type": "interactive",
    "card": {
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"海洋AI技术日报（修正版）· {yesterday_cn}"
            },
            "template": "blue"
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**📌 本期修正说明：**\n\n本次推送为修正版，已替换以下过期内容：\n- ~~EDITO Phase 2 (2025-08-01)~~ → INESC TEC 数字孪生互操作性 (2026-04-10)\n- ~~hellosea DTO (2024-07-18)~~ → DITTO Programme 全球DTO治理框架 (2026-04-24)\n- ~~HAD-QC (2025-11-24)~~ → NOAA AOML Argo 实时运行更新 (2026-04-17)\n- ~~ODFAL (2025-04-08)~~ → Argo DMQC GitHub v2.4.2 (2026-04-24)\n- ~~Ocean Modelling review (2026-02-01)~~ → CMEMS 4月份产品更新 (2026-04-03)\n- ~~ADAF-Ocean (2025-11-08)~~ → EGUsphere BGC预测综述 (2026-04-21)\n- ~~Crafting the Future (2025-06-02)~~ → OceanPredict AI-TT Workshop (2026-04-13)\n- ~~PANGAEA OFOBS (2026-01-26)~~ → CMEMS Portal Update (2026-04-17)\n- ~~SEA-PY (2026-03-23)~~ → CROCO-Ocean v2.1.3 (2026-04-07)"
                }
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**本期资讯数量：** 30条研究进展（9个方向）\n\n**质量保证：** 所有内容均在近30天内发布\n\n**生成日期：** {date_str}\n\n**GitHub Pages：** https://tianyunsu.github.io/ocean-data-daily-report/"
                }
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "**报告类型：**\n\n1. HTML简报：daily_reports/海洋AI简报_2026-04-24.html\n2. GitHub Pages：https://tianyunsu.github.io/ocean-data-daily-report/"
                }
            },
            {"tag": "hr"},
            {
                "tag": "note",
                "elements": [
                    {
                        "tag": "plain_text",
                        "content": "由 WorkBuddy 海洋AI日报自动化系统生成"
                    }
                ]
            }
        ]
    }
}

if not webhook_url:
    # Try to read from feishu_webhook_url.txt
    try:
        with open('feishu_webhook_url.txt', 'r') as f:
            webhook_url = f.read().strip()
    except:
        pass

if not webhook_url:
    print("ERROR: FEISHU_WEBHOOK_URL not found")
    sys.exit(1)

print(f"Sending to webhook (len={len(webhook_url)})...")
try:
    response = requests.post(webhook_url, json=card_content, timeout=15)
    result = response.json()
    print(f"Response: {result}")
    if result.get('code') == 0:
        print("SUCCESS!")
    else:
        print(f"FAILED: {result.get('msg')}")
except Exception as e:
    print(f"ERROR: {e}")
