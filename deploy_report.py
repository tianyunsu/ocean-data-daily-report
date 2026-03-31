#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报 - 自动化发布脚本
一键完成日报生成、更新、提交和推送流程

功能:
1. 拉取最新代码
2. 检查是否有其他机器正在部署
3. 生成今日日报HTML
4. 复制到posts目录
5. 更新index.html
6. 提交并推送到GitHub
7. 清理临时文件
"""

import os
import sys
import json
import subprocess
import shutil
from datetime import datetime
from pathlib import Path
import socket

# 配置常量
PROJECT_DIR = Path(__file__).parent.absolute()
DAILY_REPORTS_DIR = PROJECT_DIR / "daily_reports"
POSTS_DIR = PROJECT_DIR / "posts"
SECTIONS_FILE = PROJECT_DIR / "SECTIONS.json"
INDEX_HTML = PROJECT_DIR / "index.html"
LOCK_FILE = PROJECT_DIR / "deploy.lock"
LOG_DIR = PROJECT_DIR / "logs"
LOG_FILE = LOG_DIR / f"deploy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# 颜色输出(仅支持彩色终端)
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log(message, level="INFO"):
    """记录日志到文件和终端"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    # 写入日志文件
    LOG_DIR.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    # 终端输出(带颜色)
    if level == "ERROR":
        print(f"{Colors.FAIL}{log_entry.strip()}{Colors.ENDC}")
    elif level == "WARNING":
        print(f"{Colors.WARNING}{log_entry.strip()}{Colors.ENDC}")
    elif level == "SUCCESS":
        print(f"{Colors.OKGREEN}{log_entry.strip()}{Colors.ENDC}")
    else:
        print(log_entry.strip())

def run_command(command, check=True, capture_output=True):
    """运行shell命令并返回结果"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=capture_output,
            text=True,
            check=check,
            encoding='utf-8'
        )
        if capture_output and result.stdout:
            log(result.stdout.strip())
        return result
    except subprocess.CalledProcessError as e:
        log(f"命令执行失败: {command}", "ERROR")
        log(f"错误信息: {e.stderr if e.stderr else str(e)}", "ERROR")
        return None

def check_lock():
    """检查是否有其他机器正在部署"""
    if LOCK_FILE.exists():
        lock_content = LOCK_FILE.read_text(encoding='utf-8')
        hostname = socket.gethostname()
        if hostname not in lock_content:
            log(f"警告: 其他机器正在部署 - {lock_content}", "WARNING")
            response = input("是否继续部署? (y/n): ").strip().lower()
            if response != 'y':
                return False
    return True

def create_lock():
    """创建部署锁文件"""
    hostname = socket.gethostname()
    lock_content = f"deploying by {hostname} at {datetime.now().isoformat()}"
    LOCK_FILE.write_text(lock_content, encoding='utf-8')
    log(f"创建锁文件: {lock_content}")

def remove_lock():
    """删除部署锁文件"""
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()
        log("删除锁文件")

def check_environment():
    """检查环境是否就绪"""
    log("="*60)
    log("检查部署环境", "INFO")
    log("="*60)
    
    issues = []
    
    # 检查Python版本
    python_version = sys.version.split()[0]
    log(f"Python版本: {python_version}", "INFO")
    
    # 检查Git
    git_result = run_command("git --version", check=False)
    if git_result and git_result.returncode == 0:
        log(f"Git版本: {git_result.stdout.strip()}", "INFO")
    else:
        issues.append("Git未安装或不可用")
    
    # 检查关键文件
    required_files = [
        ("generate_html_report.py", "HTML生成脚本"),
        (SECTIONS_FILE, "搜索结果数据"),
    ]
    
    for file_path, description in required_files:
        if file_path.exists():
            log(f"✅ {description}: 存在", "SUCCESS")
        else:
            issues.append(f"❌ {description}: 不存在 - {file_path}")
    
    # 检查Git远程仓库
    remote_result = run_command("git remote -v", check=False)
    if remote_result:
        log(f"Git远程仓库:\n{remote_result.stdout}", "INFO")
    else:
        issues.append("Git远程仓库未配置")
    
    if issues:
        log("\n环境检查发现问题:", "ERROR")
        for issue in issues:
            log(f"  - {issue}", "ERROR")
        log("\n请修复问题后重试", "ERROR")
        return False
    
    log("\n✅ 环境检查通过", "SUCCESS")
    return True

def pull_latest_code():
    """拉取最新代码"""
    log("="*60)
    log("拉取最新代码", "INFO")
    log("="*60)
    
    # 切换到main分支
    result = run_command("git checkout main")
    if not result or result.returncode != 0:
        log("切换到main分支失败", "ERROR")
        return False
    
    # 拉取最新代码
    result = run_command("git pull origin main")
    if not result or result.returncode != 0:
        log("拉取代码失败", "ERROR")
        return False
    
    log("✅ 代码已更新到最新版本", "SUCCESS")
    return True

def generate_report():
    """生成今日日报"""
    log("="*60)
    log("生成今日日报", "INFO")
    log("="*60)
    
    # 检查SECTIONS.json是否存在且有数据
    if not SECTIONS_FILE.exists():
        log(f"错误: {SECTIONS_FILE} 不存在", "ERROR")
        return False
    
    try:
        with open(SECTIONS_FILE, 'r', encoding='utf-8') as f:
            sections = json.load(f)
        
        if not sections:
            log("警告: SECTIONS.json为空,可能需要先运行搜索脚本", "WARNING")
    except Exception as e:
        log(f"读取SECTIONS.json失败: {e}", "ERROR")
        return False
    
    # 运行生成脚本
    result = run_command("python generate_html_report.py")
    if not result or result.returncode != 0:
        log("生成日报失败", "ERROR")
        return False
    
    # 查找生成的日报文件
    date_str = datetime.now().strftime('%Y-%m-%d')
    report_file = DAILY_REPORTS_DIR / f"海洋AI简报_{date_str}.html"
    
    if not report_file.exists():
        log(f"错误: 未找到生成的日报文件 - {report_file}", "ERROR")
        return False
    
    log(f"✅ 日报已生成: {report_file}", "SUCCESS")
    return report_file

def copy_to_posts(report_file):
    """复制日报到posts目录"""
    log("="*60)
    log("复制日报到posts目录", "INFO")
    log("="*60)
    
    POSTS_DIR.mkdir(exist_ok=True)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    target_file = POSTS_DIR / f"{date_str}.html"
    
    # 读取源文件内容
    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        log(f"读取日报文件失败: {e}", "ERROR")
        return False
    
    # 写入目标文件
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        log(f"复制日报文件失败: {e}", "ERROR")
        return False
    
    log(f"✅ 日报已复制: {target_file}", "SUCCESS")
    return target_file

def update_index_html():
    """更新index.html,添加新日报链接"""
    log("="*60)
    log("更新index.html", "INFO")
    log("="*60)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    date_cn = datetime.now().strftime('%Y年%m月%d日')
    
    # 检查index.html是否存在
    if not INDEX_HTML.exists():
        log(f"错误: {INDEX_HTML} 不存在", "ERROR")
        return False
    
    # 读取现有index.html
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经包含今日日报链接
    if f'posts/{date_str}.html' in content:
        log("今日日报链接已存在,跳过更新", "INFO")
        return True
    
    # 创建新的日报链接HTML
    new_link = f'''
    <div class="report-item">
        <div class="report-date">{date_cn}</div>
        <div class="report-title">海洋AI研究日报</div>
        <a href="posts/{date_str}.html" class="report-link">查看详情</a>
    </div>
'''
    
    # 在reports-container中插入新链接
    if '<div class="reports-container">' in content:
        # 找到reports-container位置,在其后插入
        insert_pos = content.find('<div class="reports-container">') + len('<div class="reports-container">')
        updated_content = content[:insert_pos] + new_link + content[insert_pos:]
        
        # 写回文件
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        log(f"✅ 已添加今日日报链接: {date_cn}", "SUCCESS")
        return True
    else:
        log("警告: 未找到reports-container,可能需要手动更新index.html", "WARNING")
        return False

def commit_and_push(files):
    """提交并推送更改"""
    log("="*60)
    log("提交并推送到GitHub", "INFO")
    log("="*60)
    
    # 添加文件
    for file_path in files:
        result = run_command(f"git add \"{file_path}\"")
        if not result:
            log(f"添加文件失败: {file_path}", "ERROR")
            return False
    
    # 检查是否有更改
    status_result = run_command("git status --short", check=False)
    if not status_result or not status_result.stdout.strip():
        log("没有需要提交的更改", "WARNING")
        return True
    
    # 提交
    date_str = datetime.now().strftime('%Y-%m-%d')
    commit_msg = f"Add {date_str} daily report"
    result = run_command(f'git commit -m "{commit_msg}"')
    if not result or result.returncode != 0:
        log("提交失败", "ERROR")
        return False
    
    # 推送
    result = run_command("git push origin main")
    if not result or result.returncode != 0:
        log("推送失败", "ERROR")
        log("\n可能的原因:", "WARNING")
        log("  1. 认证失败: 请检查SSH密钥或GitHub Token", "WARNING")
        log("  2. 网络问题: 请检查网络连接", "WARNING")
        log("  3. 权限问题: 请确认你有推送权限", "WARNING")
        return False
    
    log(f"✅ 已成功推送到GitHub", "SUCCESS")
    return True

def main():
    """主函数"""
    print(f"{Colors.OKBLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}海洋AI日报 - 自动化发布脚本{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'='*60}{Colors.ENDC}")
    print()
    
    hostname = socket.gethostname()
    log(f"部署主机: {hostname}", "INFO")
    log(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "INFO")
    print()
    
    try:
        # 1. 检查锁
        if not check_lock():
            log("部署已取消", "WARNING")
            return False
        
        # 2. 创建锁
        create_lock()
        
        # 3. 检查环境
        if not check_environment():
            remove_lock()
            return False
        
        # 4. 拉取最新代码
        if not pull_latest_code():
            remove_lock()
            return False
        
        # 5. 生成日报
        report_file = generate_report()
        if not report_file:
            remove_lock()
            return False
        
        # 6. 复制到posts
        target_file = copy_to_posts(report_file)
        if not target_file:
            remove_lock()
            return False
        
        # 7. 更新index.html
        if not update_index_html():
            remove_lock()
            return False
        
        # 8. 提交并推送
        if not commit_and_push([target_file, INDEX_HTML]):
            remove_lock()
            return False
        
        # 9. 删除锁
        remove_lock()
        
        # 10. 成功
        log("="*60, "SUCCESS")
        log("🎉 日报发布成功!", "SUCCESS")
        log("="*60, "SUCCESS")
        log(f"✅ HTML文件: {report_file}", "SUCCESS")
        log(f"✅ 网站地址: https://tianyunsu.github.io/ocean-data-daily-report/", "SUCCESS")
        log(f"✅ 日报链接: https://tianyunsu.github.io/ocean-data-daily-report/posts/{datetime.now().strftime('%Y-%m-%d')}.html", "SUCCESS")
        log("="*60, "SUCCESS")
        log(f"日志文件: {LOG_FILE}", "INFO")
        
        return True
        
    except KeyboardInterrupt:
        log("\n\n用户中断部署", "WARNING")
        remove_lock()
        return False
    except Exception as e:
        log(f"\n\n部署过程中发生错误: {e}", "ERROR")
        import traceback
        traceback.print_exc()
        remove_lock()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
