#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报 - 飞书推送脚本（增强版）
支持从命令行参数或环境变量获取Webhook URL
"""

import requests
import os
import sys
from datetime import datetime, timedelta

def main():
    # 获取昨天的日期
    yesterday_cn = (datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')
    date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    print("=" * 70)
    print("海洋AI日报 - 飞书推送")
    print("=" * 70)
    print(f"目标日期: {yesterday_cn} ({date_str})")

    # ============================================================
    # 步骤 1：获取Webhook URL
    # ============================================================
    print("\n[步骤1] 获取飞书Webhook URL...")
    
    # 优先级：命令行参数 > 环境变量 > 提示输入
    webhook_url = None
    
    # 尝试从命令行参数获取
    if len(sys.argv) > 1:
        webhook_url = sys.argv[1]
        print(f"OK: 从命令行参数获取 Webhook URL")
    
    # 尝试从环境变量获取
    if not webhook_url:
        webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')
        if webhook_url:
            print(f"OK: 从环境变量获取 Webhook URL")
    
    # 提示用户输入
    if not webhook_url:
        print("\nERROR: FEISHU_WEBHOOK_URL 未配置")
        print("\n请选择以下方式提供 Webhook URL:")
        print("1. 设置环境变量: $env:FEISHU_WEBHOOK_URL='your_url'")
        print("2. 作为命令行参数: python send_feishu_report_v2.py 'your_url'")
        print("3. 在此提示中输入")
        
        user_input = input("\n请输入 Webhook URL (或按 Ctrl+C 退出): ").strip()
        if not user_input:
            print("ERROR: 未提供有效的 Webhook URL")
            sys.exit(1)
        webhook_url = user_input

    if not webhook_url.startswith('https://'):
        print("ERROR: Webhook URL 格式不正确（应以 https:// 开头）")
        sys.exit(1)

    print(f"OK: Webhook URL 已获取 (长度: {len(webhook_url)} 字符)")

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
                        "content": "**今日涵盖主题：**\n\n海洋人工智能 | 海洋数字孪生 | 海洋可视化 | 数据质量 | 数据处理 | 数据管理 | 开放航次"
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**本期资讯数量：** 31条研究进展\n\n**报告类型：** HTML简报 + 飞书云文档\n\n**生成日期：** {date_str}"
                    }
                },
                {"tag": "hr"},
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**详细内容：**\n\n1. HTML简报文件\n   daily_reports/海洋AI简报_{date_str}.html\n\n2. 飞书云文档\n   查看 feishu_doc_url.txt\n\n3. 执行记录\n   .codebuddy/automations/ai/memory.md"
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

    print("OK: 消息卡片构建完成")

    # ============================================================
    # 步骤 3：发送到飞书机器人
    # ============================================================
    print("\n[步骤3] 发送消息到飞书群组...")

    try:
        response = requests.post(webhook_url, json=card_content, timeout=15)
        result = response.json()
        
        if result.get('code') == 0:
            print(f"\n✓ 消息推送成功！")
            print(f"  返回代码: {result.get('code')}")
            print(f"  返回消息: {result.get('msg')}")
            print(f"\n消息已发送到飞书群组，您可以在群组中查看。")
        else:
            print(f"\nERROR: 推送失败")
            print(f"  返回代码: {result.get('code')}")
            print(f"  返回消息: {result.get('msg')}")
            if 'invalid_webhook' in str(result):
                print("\n提示：Webhook URL 可能无效或已过期，请重新创建机器人。")
            sys.exit(1)
            
    except requests.exceptions.Timeout:
        print(f"ERROR: 网络请求超时")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print(f"ERROR: 无法连接到飞书服务器")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: 网络请求异常: {e}")
        sys.exit(1)

    print("\n" + "=" * 70)
    print("推送完毕")
    print("=" * 70)

if __name__ == '__main__':
    main()
