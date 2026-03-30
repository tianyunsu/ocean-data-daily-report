#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书Webhook连接测试脚本
用于验证 FEISHU_WEBHOOK_URL 环境变量是否配置正确
"""

import requests
import os
import sys
from datetime import datetime

print("=" * 60)
print("飞书Webhook连接测试")
print("=" * 60)

# 检查环境变量
webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')

if not webhook_url:
    print("\n[错误] FEISHU_WEBHOOK_URL 环境变量未设置")
    print("\n配置步骤：")
    print("1. 按照 FEISHU_WEBHOOK_SETUP.md 指南创建机器人并获取Webhook URL")
    print("2. 设置环境变量（Windows PowerShell）：")
    print("   [System.Environment]::SetEnvironmentVariable('FEISHU_WEBHOOK_URL', 'your_webhook_url', 'User')")
    print("3. 重启终端使环境变量生效")
    print("4. 重新运行本测试脚本")
    sys.exit(1)

print(f"\n[✓] 环境变量已设置")
print(f"    Webhook URL: {webhook_url[:60]}...")

# 构造测试消息
test_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
test_payload = {
    "msg_type": "interactive",
    "card": {
        "header": {
            "title": {
                "tag": "plain_text",
                "content": "🌊 飞书机器人配置测试"
            },
            "template": "blue"
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**测试时间**: {test_time}\n\n✅ **飞书Webhook连接正常！**\n\n您现在可以接收海洋AI研究日报通知。"
                }
            },
            {
                "tag": "note",
                "elements": [
                    {
                        "tag": "plain_text",
                        "content": "由 WorkBuddy 自动化工具发送"
                    }
                ]
            }
        ]
    }
}

print("\n[*] 正在发送测试消息...")

try:
    response = requests.post(webhook_url, json=test_payload, timeout=15)
    result = response.json()
    
    print(f"\n[*] HTTP状态码: {response.status_code}")
    print(f"[*] 响应内容: {result}")
    
    if response.status_code == 200 and result.get('StatusCode') == 0:
        print("\n" + "=" * 60)
        print("[✓] 测试成功！")
        print("=" * 60)
        print("\n飞书机器人已正确配置。")
        print("现在可以运行日报脚本：")
        print("  python C:/Users/Administrator/WorkBuddy/Claw/run_daily_report.py")
        print("\n或在自动化任务中使用该脚本进行定时推送。")
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("[❌] 测试失败")
        print("=" * 60)
        print(f"\n错误详情: {result.get('StatusMessage', '未知错误')}")
        print("\n可能原因：")
        print("1. Webhook URL 格式错误")
        print("2. Webhook URL 已过期，需要重新生成")
        print("3. 飞书机器人已被禁用")
        print("4. 飞书服务暂时不可用")
        print("\n解决方案:")
        print("- 检查 Webhook URL 是否完整无误")
        print("- 在飞书群组中重新生成机器人Webhook URL")
        print("- 查看 FEISHU_WEBHOOK_SETUP.md 获取更多帮助")
        sys.exit(1)
        
except requests.exceptions.Timeout:
    print("\n" + "=" * 60)
    print("[❌] 连接超时")
    print("=" * 60)
    print("\n网络连接失败，请检查：")
    print("1. 网络连接是否正常")
    print("2. 防火墙是否阻止连接")
    print("3. Webhook URL 是否正确")
    sys.exit(1)
    
except requests.exceptions.ConnectionError:
    print("\n" + "=" * 60)
    print("[❌] 连接错误")
    print("=" * 60)
    print("\n无法连接到飞书服务器，请检查：")
    print("1. 网络连接状态")
    print("2. Webhook URL 是否有效")
    print("3. 飞书官网是否可访问")
    sys.exit(1)
    
except Exception as e:
    print("\n" + "=" * 60)
    print("[❌] 异常错误")
    print("=" * 60)
    print(f"\n错误信息: {str(e)}")
    print("\n请检查：")
    print("1. Python requests 库是否已安装 (pip install requests)")
    print("2. Webhook URL 格式是否正确")
    sys.exit(1)
