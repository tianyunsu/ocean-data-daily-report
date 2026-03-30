#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
from datetime import datetime

print("测试GitHub发布...")

# 测试Git命令
result = subprocess.run(
    "git status",
    shell=True,
    cwd=r"C:\Users\Administrator\WorkBuddy\Claw",
    capture_output=True,
    text=True,
    encoding='utf-8',
    timeout=30
)

print(f"返回码: {result.returncode}")
print(f"标准输出: {result.stdout}")
print(f"标准错误: {result.stderr}")

today = datetime.now().strftime('%Y-%m-%d')
html_file = f"海洋AI简报_{today}.html"
html_path = os.path.join(r"C:\Users\Administrator\WorkBuddy\Claw\daily_reports", html_file)

print(f"\nHTML文件路径: {html_path}")
print(f"文件存在: {os.path.exists(html_path)}")
