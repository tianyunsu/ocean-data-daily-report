#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报 - 发布到GitHub Pages脚本
功能：将生成的HTML简报提交到GitHub仓库并推送到GitHub Pages
"""

import os
import shutil
import subprocess
from datetime import datetime
import sys

def run_command(cmd, cwd=None):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=60
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "命令执行超时"
    except Exception as e:
        return False, "", str(e)

def main():
    print("=== 海洋AI日报 - GitHub Pages发布 ===\n")
    
    # 配置参数（需要根据实际情况修改）
    workspace = r"C:\Users\Administrator\WorkBuddy\Claw"
    daily_reports_dir = os.path.join(workspace, "daily_reports")
    
    today = datetime.now().strftime('%Y-%m-%d')
    html_file = f"海洋AI简报_{today}.html"
    html_path = os.path.join(daily_reports_dir, html_file)
    
    # 检查HTML文件是否存在
    if not os.path.exists(html_path):
        print(f"错误：找不到HTML文件 {html_path}")
        print(f"请先生成今日的日报：python generate_html_report.py")
        return False
    
    print(f"[OK] 找到HTML文件: {html_file}")
    
    # 检查是否为Git仓库
    success, stdout, stderr = run_command("git status", workspace)
    if not success and "not a git repository" in stderr:
        print("\n错误：当前目录不是Git仓库")
        print("请先初始化Git仓库：")
        print("  cd C:\\Users\\Administrator\\WorkBuddy\\Claw")
        print("  git init")
        print("  git remote add origin <你的GitHub仓库地址>")
        return False
    
    print("[OK] Git仓库检查通过\n")
    
    # 检查git远程仓库
    success, stdout, stderr = run_command("git remote -v", workspace)
    if not success or not stdout.strip():
        print("警告：未配置Git远程仓库")
        print("请先添加远程仓库：")
        print("  git remote add origin https://github.com/<用户名>/<仓库名>.git")
        return False
    
    print(f"[OK] Git远程仓库:\n{stdout}\n")
    
    # 创建gh-pages分支（如果不存在）
    print("--- 步骤1：准备gh-pages分支 ---")
    success, stdout, stderr = run_command("git branch --list gh-pages", workspace)
    if not stdout.strip():
        print("创建gh-pages分支...")
        success, stdout, stderr = run_command("git checkout --orphan gh-pages", workspace)
        if not success:
            print(f"错误：创建分支失败: {stderr}")
            return False
        
        # 清空暂存区（保留当前文件）
        success, stdout, stderr = run_command("git rm -rf .", workspace)
        if not success:
            print(f"警告：清空暂存区失败: {stderr}")
        
        print("创建.index.html作为首页...")
        index_path = os.path.join(workspace, "index.html")
        
        # 创建索引页面
        index_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>海洋AI研究日报</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f5f5f5;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
            font-size: 1.1em;
        }}
        .report-list {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .report-item {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .report-item:hover {{
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        .report-item h3 {{
            margin: 0 0 10px 0;
            color: #333;
        }}
        .report-item a {{
            color: #667eea;
            text-decoration: none;
            display: inline-block;
            margin-top: 10px;
        }}
        .report-item a:hover {{
            text-decoration: underline;
        }}
        .latest {{
            border: 2px solid #667eea;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🌊 海洋AI研究日报</h1>
        <p>Ocean AI Research Daily Report</p>
        <p style="margin-top: 20px;">最后更新: {today}</p>
    </div>
    
    <h2>📊 最新日报</h2>
    <div class="report-item latest">
        <h3>🌟 {today} - 最新发布</h3>
        <p>本期共涵盖9个研究方向，23条动态</p>
        <a href="daily_reports/{html_file}" target="_blank">查看完整报告 →</a>
    </div>
    
    <h2>📚 历史日报</h2>
    <div class="report-list">
        <!-- 将在后续脚本中自动生成历史报告列表 -->
    </div>
    
    <footer style="text-align: center; margin-top: 60px; color: #666;">
        <p>由 WorkBuddy 自动生成 | 每日更新</p>
    </footer>
</body>
</html>
"""
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"[OK] 创建index.html\n")
    else:
        print("切换到gh-pages分支...")
        success, stdout, stderr = run_command("git checkout gh-pages", workspace)
        if not success:
            print(f"错误：切换分支失败: {stderr}")
            return False
        print("[OK] 已切换到gh-pages分支\n")
    
    # 确保daily_reports目录存在
    if not os.path.exists(os.path.join(workspace, "daily_reports")):
        os.makedirs(os.path.join(workspace, "daily_reports"))
    
    # 复制HTML文件
    print(f"--- 步骤2：复制今日日报 ---")
    dest_path = os.path.join(workspace, "daily_reports", html_file)
    
    # 先读取源文件内容，避免文件被锁定的问题
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 写入目标文件
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"[OK] 已复制: {html_file}\n")
    
    # 提交更改
    print("--- 步骤3：提交更改 ---")
    success, stdout, stderr = run_command("git add .", workspace)
    if not success:
        print(f"警告：git add失败: {stderr}")
    
    commit_msg = f"Update daily report: {today}"
    success, stdout, stderr = run_command(f'git commit -m "{commit_msg}"', workspace)
    if not success:
        print(f"警告：git commit失败: {stderr}")
    else:
        print(f"[OK] 已提交: {commit_msg}\n")
    
    # 推送到GitHub
    print("--- 步骤4：推送到GitHub ---")
    success, stdout, stderr = run_command("git push origin gh-pages", workspace)
    if success:
        print("[OK] 已推送到GitHub\n")
        print("=== 发布成功 ===")
        print("\n您的GitHub Pages网站地址为：")
        print("https://<用户名>.github.io/<仓库名>/")
        print("\n请在GitHub仓库设置中确认：")
        print("1. Settings → Pages")
        print("2. Source: Deploy from a branch")
        print("3. Branch: gh-pages / (root)")
        print("4. 点击Save")
    else:
        print(f"错误：git push失败: {stderr}")
        return False
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n操作已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
