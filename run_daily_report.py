#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报 - 飞书推送 & 邮件发送脚本
日期: 2026-03-16
"""

import requests
import os
import json
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

yesterday = datetime.now().strftime('%Y年%m月%d日')
date_str = datetime.now().strftime('%Y-%m-%d')

print(f"=== 海洋AI日报推送脚本 ===")
print(f"目标日期: {yesterday} ({date_str})")

html_file = f"C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_{date_str}.html"
doc_url = None

# ============================================================
# 第三步：飞书云文档
# ============================================================
app_id = os.environ.get('FEISHU_APP_ID', 'cli_a93d483f6ff81bca')
app_secret = os.environ.get('FEISHU_APP_SECRET', 'CU3EPesfCzNayK4bqsnh6droaJsf4HV8')
folder_token = os.environ.get('FEISHU_FOLDER_TOKEN', '')

print(f"\n--- 步骤3：飞书云文档 ---")
print(f"App ID: {app_id}")

try:
    # 获取 tenant_access_token
    token_resp = requests.post(
        'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
        json={'app_id': app_id, 'app_secret': app_secret},
        timeout=15
    )
    token_data = token_resp.json()
    print(f"Token响应: code={token_data.get('code')}, msg={token_data.get('msg')}")
    access_token = token_data.get('tenant_access_token')

    if not access_token:
        print(f"警告：未能获取 token，跳过飞书文档创建。响应: {token_data}")
    else:
        print(f"access_token 获取成功: {access_token[:12]}...")
        # 调用独立写入脚本
        import subprocess, sys
        result = subprocess.run(
            [sys.executable, 'feishu_write_doc.py'],
            capture_output=True, text=True, encoding='utf-8', timeout=120
        )
        print(result.stdout)
        if result.returncode == 0 and 'SUCCESS' in result.stdout:
            import os
            if os.path.exists('feishu_doc_url.txt'):
                with open('feishu_doc_url.txt', 'r', encoding='utf-8') as f:
                    doc_url = f.read().strip()
                print(f"OK Feishu doc created: {doc_url}")
            else:
                print("警告：feishu_doc_url.txt 不存在")
        else:
            print(f"警告：文档写入脚本异常: {result.stderr[:200]}")

except Exception as e:
    print(f"警告：飞书文档创建异常: {e}")

# ============================================================
# 第四步：飞书机器人消息
# ============================================================
print(f"\n--- 步骤4：飞书机器人消息 ---")
webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')

if not webhook_url:
    print("警告：FEISHU_WEBHOOK_URL 未配置，跳过消息推送")
else:
    try:
        github_url = f"https://tianyunsu.github.io/ocean-data-daily-report/posts/{date_str}.html"
        
        # 构建链接文字
        if doc_url:
            link_content = f"📄 **飞书文档：** {doc_url}\n\n🌐 **网页版：** {github_url}"
        else:
            link_content = f"🌐 **完整日报（网页版）：** {github_url}\n\n> 飞书文档写入失败，请点击上方链接查看完整日报"

        card_content = {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {"tag": "plain_text", "content": f"🌊 海洋AI技术日报 · {yesterday}"},
                    "template": "blue"
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": "**今日涵盖主题：**\n🤖 海洋人工智能 | 🌐 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理 | 🗄️ 数据管理与共享 | 🚢 开放航次/船时共享"
                        }
                    },
                    {"tag": "hr"},
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": link_content
                        }
                    },
                    {"tag": "hr"},
                    {
                        "tag": "note",
                        "elements": [
                            {"tag": "plain_text", "content": "由 WorkBuddy 自动生成 · 每日09:00推送"}
                        ]
                    }
                ]
            }
        }
        resp = requests.post(webhook_url, json=card_content, timeout=15)
        print(f"OK Feishu webhook result: {resp.json()}")
    except Exception as e:
        print(f"警告：飞书消息推送异常: {e}")

# ============================================================
# 第五步：邮件发送
# ============================================================
print(f"\n--- 步骤5：邮件发送 ---")
sender = os.environ.get('REPORT_EMAIL_SENDER', '')
password = os.environ.get('REPORT_EMAIL_PASSWORD', '')
smtp_server = os.environ.get('REPORT_EMAIL_SMTP', 'smtp.163.com')
smtp_port = int(os.environ.get('REPORT_EMAIL_SMTP_PORT', '465'))

if not sender or not password:
    print("警告：REPORT_EMAIL_SENDER/REPORT_EMAIL_PASSWORD 未配置，跳过邮件发送")
else:
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'海洋AI技术日报 · {yesterday}'
        msg['From'] = sender
        msg['To'] = 'sutiany@163.com'

        doc_link_html = ''
        if doc_url:
            doc_link_html = f'<p style="margin:12px 0;padding:10px;background:#e8f4fd;border-radius:8px;">📄 <a href="{doc_url}" style="color:#005b9a;font-weight:600;">点击查看飞书云文档版本</a></p>'

        with open(html_file, 'r', encoding='utf-8') as f:
            html_body = f.read()

        html_body = html_body.replace('<body>', f'<body>{doc_link_html}')
        msg.attach(MIMEText(html_body, 'html', 'utf-8'))

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, ['sutiany@163.com'], msg.as_string())
        print(f"OK Email sent -> sutiany@163.com")
    except Exception as e:
        print(f"警告：邮件发送异常: {e}")

print("\n=== 脚本执行完毕 ===")
