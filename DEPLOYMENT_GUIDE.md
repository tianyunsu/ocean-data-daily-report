# 海洋AI日报系统 - 多机部署迁移指南

## 目录
1. [系统要求](#系统要求)
2. [快速开始](#快速开始)
3. [详细配置步骤](#详细配置步骤)
4. [自动化脚本使用](#自动化脚本使用)
5. [常见问题排查](#常见问题排查)
6. [多机协作注意事项](#多机协作注意事项)

---

## 系统要求

### 硬件要求
- 操作系统: Windows 10/11, macOS, 或 Linux
- 至少 2GB 可用磁盘空间
- 稳定的网络连接(用于Git推送和数据检索)

### 软件要求
- **Python 3.7+**
- **Git 2.20+**
- **WorkBuddy** (可选,用于自动化任务)

### Python依赖
```bash
# 如果有requirements.txt,运行:
pip install -r requirements.txt

# 或安装必要的包:
pip install requests beautifulsoup4 lxml
```

---

## 快速开始

### 1. 克隆代码仓库

```bash
# 使用HTTPS(需要GitHub凭据)
git clone https://github.com/tianyunsu/ocean-data-daily-report.git
cd ocean-data-daily-report

# 或使用SSH(推荐)
git clone git@github.com:tianyunsu/ocean-data-daily-report.git
cd ocean-data-daily-report
```

### 2. 配置Git认证

#### 方式A: SSH密钥(推荐)
```bash
# 生成SSH密钥(如果没有)
ssh-keygen -t ed25519 -C "your_email@example.com"

# 将公钥添加到GitHub
# 复制 ~/.ssh/id_ed25519.pub 的内容
# 访问: GitHub Settings -> SSH and GPG keys -> New SSH key

# 测试连接
ssh -T git@github.com
```

#### 方式B: Personal Access Token
```bash
# 访问: GitHub Settings -> Developer settings -> Personal access tokens
# 创建token,权限至少需要: repo

# 推送时使用token作为密码
```

### 3. 首次运行

```bash
# 切换到main分支
git checkout main

# 拉取最新代码
git pull origin main

# 运行发布脚本
python deploy_report.py
```

---

## 详细配置步骤

### 步骤1: 准备工作目录

```bash
# 创建工作目录(如果使用自定义路径)
mkdir ocean-data-daily-report
cd ocean-data-daily-report
```

### 步骤2: 配置Python环境

#### Windows
```powershell
# 检查Python版本
python --version

# 安装依赖
pip install requests beautifulsoup4 lxml

# 创建虚拟环境(推荐)
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

#### macOS/Linux
```bash
# 检查Python版本
python3 --version

# 安装依赖
pip3 install requests beautifulsoup4 lxml

# 创建虚拟环境(推荐)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 步骤3: 配置Git用户信息

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 步骤4: 验证关键文件

确保以下文件存在于项目根目录:
```
ocean-data-daily-report/
├── generate_html_report.py    # HTML生成脚本
├── deploy_report.py            # 自动化发布脚本
├── check_env.py                # 环境检查脚本
├── SECTIONS.json               # 搜索结果数据
├── search_strategy.md          # 检索策略
├── daily_reports/              # 生成的日报存放目录
├── posts/                     # 网站发布目录
└── index.html                 # 网站首页
```

### 步骤5: 测试环境

```bash
# 运行环境检查
python check_env.py

# 如果所有检查通过,会显示:
# ✅ Python环境: 正常
# ✅ Git配置: 正常
# ✅ 仓库连接: 正常
# ✅ 关键文件: 存在
```

---

## 自动化脚本使用

### 主要脚本说明

#### 1. `deploy_report.py` - 主发布脚本
一键完成日报生成和发布流程

```bash
# 使用方法
python deploy_report.py

# 脚本会自动:
# 1. 拉取最新代码
# 2. 生成今日日报HTML
# 3. 复制到posts目录
# 4. 更新index.html
# 5. 提交并推送到GitHub
```

#### 2. `check_env.py` - 环境检查脚本
验证部署环境是否就绪

```bash
# 使用方法
python check_env.py
```

#### 3. 手动发布流程(可选)

如果需要分步执行:

```bash
# 步骤1: 生成日报
python generate_html_report.py

# 步骤2: 复制到posts目录
DATE=$(date +%Y-%m-%d)
cp daily_reports/海洋AI简报_${DATE}.html posts/${DATE}.html

# 步骤3: 更新index.html
# 手动编辑或使用脚本

# 步骤4: 提交推送
git add posts/${DATE}.html index.html
git commit -m "Add ${DATE} daily report"
git push origin main
```

### 定时任务配置

#### Windows任务计划程序
1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器: 每天上午9点
4. 操作: 启动程序 `python.exe`, 参数 `C:\path\to\ocean-data-daily-report\deploy_report.py`

#### macOS/Linux Cron
```bash
# 编辑crontab
crontab -e

# 添加以下行(每天9:00运行)
0 9 * * * cd /path/to/ocean-data-daily-report && python deploy_report.py >> logs/deploy.log 2>&1
```

#### WorkBuddy自动化任务
如果使用WorkBuddy,可以创建自动化任务:

```json
{
  "name": "海洋AI日报自动发布",
  "scheduleType": "recurring",
  "rrule": "FREQ=DAILY;BYHOUR=9;BYMINUTE=0",
  "cwds": ["C:/Users/Administrator/WorkBuddy/Claw"],
  "prompt": "运行 deploy_report.py 脚本生成并发布今日海洋AI日报",
  "status": "ACTIVE"
}
```

---

## 常见问题排查

### 问题1: Git推送失败
**错误信息**: `Authentication failed`

**解决方案**:
```bash
# 检查远程URL
git remote -v

# 如果使用HTTPS,更新为SSH
git remote set-url origin git@github.com:tianyunsu/ocean-data-daily-report.git

# 重新配置SSH密钥
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### 问题2: Python依赖缺失
**错误信息**: `ModuleNotFoundError: No module named 'xxx'`

**解决方案**:
```bash
# 安装缺失的包
pip install <module_name>

# 或安装所有依赖
pip install -r requirements.txt
```

### 问题3: 文件权限错误
**错误信息**: `Permission denied`

**解决方案**:
```bash
# Windows: 以管理员身份运行PowerShell
# macOS/Linux: 使用sudo
sudo python deploy_report.py
```

### 问题4: 日报日期错误
**现象**: 生成的日报日期不是当天

**解决方案**:
检查 `generate_html_report.py` 中的日期计算:
```python
from datetime import datetime, timedelta

# 确保使用当天日期,而不是昨天
date_str = datetime.now().strftime('%Y-%m-%d')  # 正确
# date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')  # 错误
```

### 问题5: 合并冲突
**错误信息**: `CONFLICT (content): Merge conflict in index.html`

**解决方案**:
```bash
# 查看冲突文件
git status

# 方式1: 使用远程版本
git checkout --theirs index.html
git add index.html

# 方式2: 使用本地版本
git checkout --ours index.html
git add index.html

# 方式3: 手动编辑解决冲突
# 打开index.html,搜索 <<<<<<<, =======, >>>>>>>
# 修改后执行:
git add index.html
```

---

## 多机协作注意事项

### 1. 同步策略
- **主备模式**: 一台机器作为主要发布者,其他机器作为备份
- **轮换模式**: 不同日期由不同机器发布
- **时间分片**: 主机上午发布,备用机下午检查

### 2. 避免冲突的方法

#### 方法A: 使用Git锁机制
```bash
# 创建.lock文件表示正在发布
echo "deploying by $(hostname)" > deploy.lock

# 发布完成后删除
rm deploy.lock

# 其他机器发布前检查
if [ -f deploy.lock ]; then
    echo "其他机器正在发布,稍后再试"
    exit 1
fi
```

#### 方法B: 时间分片
```bash
# 在deploy_report.py中添加主机检查
import socket
hostname = socket.gethostname()

if hostname == "primary-pc":
    # 主机在9:00发布
    if 8 <= datetime.now().hour < 10:
        deploy()
else:
    # 备用机在10:00后检查并发布
    if datetime.now().hour >= 10:
        check_and_deploy()
```

#### 方法C: Pull Request模式
```bash
# 备用机器创建分支发布
git checkout -b feature/daily-report-$(date +%Y-%m-%d)
python generate_html_report.py
git commit -m "Add daily report"
git push origin feature/daily-report-$(date +%Y-%m-%d)

# 手动或自动创建PR合并到main
```

### 3. 日志和监控

#### 添加日志记录
```python
import logging

logging.basicConfig(
    filename='logs/deploy.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.info(f"开始发布日报 - 主机: {hostname}")
```

#### 监控脚本
```bash
#!/bin/bash
# monitor.sh - 检查每日是否正常发布

TODAY=$(date +%Y-%m-%d)
EXPECTED_FILE="posts/${TODAY}.html"

if [ ! -f "$EXPECTED_FILE" ]; then
    echo "警告: 今日日报未发布"
    # 发送通知(邮件/Slack/飞书等)
else
    echo "今日日报已正常发布"
fi
```

### 4. 备份策略
```bash
# 定期备份关键数据
tar -czf backup/SECTIONS_$(date +%Y%m%d).tar.gz SECTIONS.json search_strategy.md

# 保留最近30天备份
find backup/ -name "SECTIONS_*.tar.gz" -mtime +30 -delete
```

---

## 文件结构说明

```
ocean-data-daily-report/
│
├── deploy_report.py           # 🚀 自动化发布脚本
├── check_env.py              # 🔧 环境检查脚本
├── generate_html_report.py   # 📝 HTML生成脚本
├── requirements.txt          # 📦 Python依赖
├── DEPLOYMENT_GUIDE.md      # 📖 本文档
│
├── SECTIONS.json             # 🔍 搜索结果数据
├── search_strategy.md       # 🎯 检索策略说明
│
├── daily_reports/            # 📁 生成的日报(本地)
│   └── 海洋AI简报_YYYY-MM-DD.html
│
├── posts/                   # 🌐 发布到网站的日报
│   └── YYYY-MM-DD.html
│
├── index.html              # 🏠 网站首页
│
├── logs/                   # 📋 日志目录
│   └── deploy.log
│
└── backup/                # 💾 备份目录
    └── SECTIONS_YYYYMMDD.tar.gz
```

---

## 更新日志

### 2026-03-30
- 创建完整的多机部署迁移指南
- 添加自动化发布脚本
- 添加环境检查脚本
- 添加多机协作最佳实践

---

## 技术支持

如有问题,请联系:
- GitHub Issues: https://github.com/tianyunsu/ocean-data-daily-report/issues
- 仓库地址: https://github.com/tianyunsu/ocean-data-daily-report
- 网站地址: https://tianyunsu.github.io/ocean-data-daily-report/

---

**最后更新**: 2026-03-30
**版本**: v1.0
