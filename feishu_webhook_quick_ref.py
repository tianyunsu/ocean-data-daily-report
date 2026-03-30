#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书机器人推送 - 配置快速参考卡
打印此文件即可获得便携式配置指南
"""

import platform

def print_reference_card():
    """打印配置快速参考卡"""
    
    card = """
========================================================
  Ocean AI - 飞书机器人推送 快速参考卡
========================================================

配置资源列表
========================================================

[1] FEISHU_WEBHOOK_QUICKSTART.md
    首先阅读！5分钟快速配置指南
    
[2] FEISHU_WEBHOOK_SETUP.md
    详细完整指南，遇到问题时查阅
    
[3] FEISHU_WEBHOOK_INDEX.md
    资源导航和文件组织结构


快速配置步骤（5分钟）
========================================================

步骤 1 - 创建飞书机器人
   * 打开飞书群组 -> 右上角菜单 -> 群组设置
   * 群机器人 -> 添加机器人 -> 自定义机器人
   * 输入名称 -> 完成 -> 复制 Webhook URL

步骤 2 - 设置环境变量
   打开 PowerShell (管理员身份):
   
   [System.Environment]::SetEnvironmentVariable(
     'FEISHU_WEBHOOK_URL',
     'your_webhook_url',
     'User'
   )
   
   [!] 然后关闭并重新打开 PowerShell

步骤 3 - 验证配置
   python test_feishu_webhook.py
   
   预期输出: [OK] 测试成功!

步骤 4 - 启用推送
   python run_daily_report.py
   
   每次运行会自动推送消息到飞书群组


文件位置速查
========================================================

C:/Users/Administrator/WorkBuddy/Claw/

配置指南:
  * FEISHU_WEBHOOK_QUICKSTART.md    [从这里开始]
  * FEISHU_WEBHOOK_SETUP.md         [详细参考]
  * FEISHU_WEBHOOK_INDEX.md         [导航索引]

执行脚本:
  * run_daily_report.py             [主脚本]
  * feishu_write_doc.py             [文档创建]
  * test_feishu_webhook.py          [验证工具]

输出文件:
  * daily_reports/海洋AI简报_*.html  [每日简报]
  * feishu_doc_url.txt              [文档链接]


常用命令
========================================================

检查环境变量:
  [System.Environment]::GetEnvironmentVariable(
    'FEISHU_WEBHOOK_URL', 'User'
  )

运行验证测试:
  python test_feishu_webhook.py

执行日报推送:
  python run_daily_report.py

查看执行记录:
  cat .codebuddy/automations/ai/memory.md


遇到问题?
========================================================

1. 运行 test_feishu_webhook.py 查看错误提示
2. 查看 FEISHU_WEBHOOK_SETUP.md FAQ 部分
3. 检查 Webhook URL 是否完整正确
4. 确认环境变量设置后已重启 PowerShell


成功指标
========================================================

[OK] 能运行 test_feishu_webhook.py
[OK] 看到测试成功消息
[OK] 飞书群组收到测试消息
[OK] 能运行 run_daily_report.py
[OK] 飞书群组每天收到日报推送


资源链接
========================================================

飞书官方文档:
  https://open.feishu.cn/document

飞书开发者社区:
  https://open.feishu.cn/

本地项目记录:
  .codebuddy/automations/ai/memory.md


========================================================
配置预计时间: 5-15分钟
立即开始: 阅读 FEISHU_WEBHOOK_QUICKSTART.md
========================================================

生成时间: 2026-03-18
"""
    
    print(card)
    
    if platform.system() == 'Windows':
        print("\nWindows 用户提示:")
        print("   1. 按 Win + R 打开运行对话框")
        print("   2. 输入 powershell 并按 Ctrl+Shift+Enter")
        print("   3. 在管理员 PowerShell 中粘贴环境变量设置命令")
        print("   4. 关闭所有 PowerShell 窗口并重新打开")


if __name__ == '__main__':
    print_reference_card()
