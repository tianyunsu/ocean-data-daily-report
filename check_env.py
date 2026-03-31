#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
海洋AI日报 - 环境检查脚本
验证部署环境是否就绪

检查项:
- Python版本
- Git配置
- Git远程仓库连接
- 关键文件是否存在
- Python依赖包
- 目录结构
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import socket

# 配置常量
PROJECT_DIR = Path(__file__).parent.absolute()
REQUIRED_FILES = [
    ("generate_html_report.py", "HTML生成脚本"),
    ("deploy_report.py", "自动化发布脚本"),
    ("SECTIONS.json", "搜索结果数据"),
    ("search_strategy.md", "检索策略说明"),
    ("index.html", "网站首页"),
]

REQUIRED_DIRS = [
    ("daily_reports", "日报存放目录"),
    ("posts", "网站发布目录"),
]

PYTHON_PACKAGES = [
    "requests",
    "beautifulsoup4",
    "lxml",
]

# 颜色输出
class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_header(title):
    """打印标题"""
    print(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{title}{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_result(status, message):
    """打印检查结果"""
    if status == "OK":
        icon = "✅"
        color = Colors.OKGREEN
    elif status == "WARNING":
        icon = "⚠️ "
        color = Colors.WARNING
    else:
        icon = "❌"
        color = Colors.FAIL
    
    print(f"{color}{icon} {message}{Colors.ENDC}")

def run_command(command, capture_output=True):
    """运行shell命令"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=capture_output,
            text=True,
            encoding='utf-8'
        )
        return result
    except Exception as e:
        return None

def check_python():
    """检查Python环境"""
    print_header("1. Python环境检查")
    
    issues = []
    
    # Python版本
    version = sys.version.split()[0]
    version_info = sys.version_info
    
    print(f"Python版本: {version}")
    print(f"Python路径: {sys.executable}\n")
    
    # 检查版本
    if version_info < (3, 7):
        print_result("FAIL", f"Python版本过低,需要3.7+,当前: {version}")
        issues.append(f"Python版本需要 >= 3.7")
    else:
        print_result("OK", f"Python版本符合要求: {version}")
    
    # 检查依赖包
    print("\n检查Python依赖包:")
    missing_packages = []
    for package in PYTHON_PACKAGES:
        result = run_command(f"python -c \"import {package.replace('-', '_')}\" 2>&1", capture_output=True)
        if result and result.returncode == 0:
            print_result("OK", f"{package} - 已安装")
        else:
            print_result("FAIL", f"{package} - 未安装")
            missing_packages.append(package)
    
    if missing_packages:
        issues.append(f"缺少Python依赖包: {', '.join(missing_packages)}")
        print(f"\n安装命令:")
        print(f"  pip install {' '.join(missing_packages)}")
    
    return issues

def check_git():
    """检查Git配置"""
    print_header("2. Git配置检查")
    
    issues = []
    
    # Git版本
    result = run_command("git --version")
    if result and result.returncode == 0:
        version = result.stdout.strip()
        print(f"Git版本: {version}\n")
        print_result("OK", f"Git已安装: {version}")
    else:
        print_result("FAIL", "Git未安装或不可用")
        issues.append("Git未安装")
        return issues
    
    # Git用户配置
    print("\nGit用户配置:")
    user_name = run_command("git config --global user.name")
    user_email = run_command("git config --global user.email")
    
    if user_name and user_name.stdout.strip():
        print(f"  用户名: {user_name.stdout.strip()}")
        print_result("OK", "Git用户名已配置")
    else:
        print_result("WARNING", "Git用户名未配置")
        issues.append("Git用户名未配置")
        print("  配置命令: git config --global user.name \"Your Name\"")
    
    if user_email and user_email.stdout.strip():
        print(f"  邮箱: {user_email.stdout.strip()}")
        print_result("OK", "Git邮箱已配置")
    else:
        print_result("WARNING", "Git邮箱未配置")
        issues.append("Git邮箱未配置")
        print("  配置命令: git config --global user.email \"your.email@example.com\"")
    
    # Git远程仓库
    print("\nGit远程仓库:")
    remote_result = run_command("git remote -v")
    if remote_result and remote_result.stdout.strip():
        print(remote_result.stdout.strip())
        print_result("OK", "Git远程仓库已配置")
    else:
        print_result("WARNING", "Git远程仓库未配置")
        issues.append("Git远程仓库未配置")
        print("  克隆命令: git clone https://github.com/tianyunsu/ocean-data-daily-report.git")
    
    return issues

def check_files():
    """检查关键文件"""
    print_header("3. 关键文件检查")
    
    issues = []
    
    for file_path, description in REQUIRED_FILES:
        full_path = PROJECT_DIR / file_path
        if full_path.exists():
            size = full_path.stat().st_size
            print_result("OK", f"{description} ({file_path}) - {size} bytes")
        else:
            print_result("FAIL", f"{description} ({file_path}) - 不存在")
            issues.append(f"缺少文件: {file_path}")
    
    # 检查SECTIONS.json内容
    sections_file = PROJECT_DIR / "SECTIONS.json"
    if sections_file.exists():
        try:
            with open(sections_file, 'r', encoding='utf-8') as f:
                sections = json.load(f)
            
            section_count = len(sections)
            print(f"\nSECTIONS.json 包含 {section_count} 个研究方向的搜索结果")
            
            if section_count == 0:
                print_result("WARNING", "SECTIONS.json 为空,可能需要先运行搜索脚本")
                issues.append("SECTIONS.json 为空")
        except Exception as e:
            print_result("FAIL", f"读取SECTIONS.json失败: {e}")
            issues.append(f"SECTIONS.json格式错误")
    
    return issues

def check_directories():
    """检查目录结构"""
    print_header("4. 目录结构检查")
    
    issues = []
    
    for dir_path, description in REQUIRED_DIRS:
        full_path = PROJECT_DIR / dir_path
        if full_path.exists() and full_path.is_dir():
            file_count = len(list(full_path.iterdir()))
            print_result("OK", f"{description} ({dir_path}) - {file_count} 个文件")
        else:
            print_result("WARNING", f"{description} ({dir_path}) - 不存在")
            # 尝试创建目录
            try:
                full_path.mkdir(parents=True, exist_ok=True)
                print(f"  已自动创建目录: {dir_path}")
            except Exception as e:
                issues.append(f"无法创建目录: {dir_path}")
    
    return issues

def check_git_connection():
    """检查Git连接"""
    print_header("5. Git连接测试")
    
    issues = []
    
    # 检查当前分支
    branch_result = run_command("git branch --show-current")
    if branch_result and branch_result.stdout.strip():
        branch = branch_result.stdout.strip()
        print(f"当前分支: {branch}")
        print_result("OK", f"Git工作目录正常")
    else:
        print_result("WARNING", "无法获取当前分支")
        issues.append("Git工作目录可能有问题")
    
    # 测试远程连接
    print("\n测试远程连接:")
    remote_result = run_command("git ls-remote origin 2>&1", capture_output=True)
    if remote_result and remote_result.returncode == 0:
        print_result("OK", "可以连接到远程仓库")
    else:
        print_result("FAIL", "无法连接到远程仓库")
        issues.append("无法连接到远程仓库")
        print("\n可能的原因:")
        print("  1. 网络连接问题")
        print("  2. SSH密钥未配置或失效")
        print("  3. 仓库地址错误")
        print("\n解决方案:")
        print("  1. 检查网络连接")
        print("  2. 测试SSH连接: ssh -T git@github.com")
        print("  3. 重新配置远程仓库: git remote set-url origin <url>")
    
    return issues

def check_system_info():
    """显示系统信息"""
    print_header("系统信息")
    
    # 主机名
    print(f"主机名: {socket.gethostname()}")
    
    # 操作系统
    import platform
    print(f"操作系统: {platform.system()} {platform.release()}")
    print(f"架构: {platform.machine()}")
    
    # 工作目录
    print(f"工作目录: {PROJECT_DIR}")
    
    # 当前时间
    from datetime import datetime
    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """主函数"""
    print(f"{Colors.BOLD}海洋AI日报 - 环境检查工具{Colors.ENDC}")
    
    all_issues = []
    
    # 系统信息
    check_system_info()
    
    # 执行各项检查
    all_issues.extend(check_python())
    all_issues.extend(check_git())
    all_issues.extend(check_files())
    all_issues.extend(check_directories())
    all_issues.extend(check_git_connection())
    
    # 总结
    print_header("检查总结")
    
    if not all_issues:
        print(f"{Colors.OKGREEN}✅ 所有检查项通过!{Colors.ENDC}")
        print(f"\n{Colors.OKGREEN}环境配置完美,可以开始部署!{Colors.ENDC}")
        print(f"\n下一步:")
        print(f"  1. 运行日报生成: python generate_html_report.py")
        print(f"  2. 或一键发布: python deploy_report.py")
        return 0
    else:
        print(f"{Colors.FAIL}❌ 发现 {len(all_issues)} 个问题需要解决:{Colors.ENDC}\n")
        
        for i, issue in enumerate(all_issues, 1):
            print(f"{Colors.FAIL}{i}. {issue}{Colors.ENDC}")
        
        print(f"\n{Colors.WARNING}请解决以上问题后重试{Colors.ENDC}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
