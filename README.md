# 海洋AI研究日报系统

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![GitHub](https://img.shields.io/badge/GitHub-main-brightgreen)

自动化海洋AI研究信息收集、整理与发布系统。每日生成海洋AI相关领域研究进展的HTML简报,并自动发布到GitHub Pages网站。

## 🌐 网站地址

- **主站**: https://tianyunsu.github.io/ocean-data-daily-report/
- **GitHub仓库**: https://github.com/tianyunsu/ocean-data-daily-report

## ✨ 主要功能

- **自动生成日报**: 每日自动生成海洋AI研究进展的HTML格式日报
- **多方向覆盖**: 涵盖海洋AI、数字孪生、可视化、数据质量、数据处理、数据管理、开放航次、海洋数据中心、工具与代码资源等9个研究方向
- **自动发布**: 一键发布到GitHub Pages网站
- **多机部署**: 支持在多台计算机上运行相同的任务
- **历史归档**: 自动保存历史日报,方便查阅

## 🚀 快速开始

### 方式1: 一键部署(推荐)

```bash
# 1. 克隆仓库
git clone https://github.com/tianyunsu/ocean-data-daily-report.git
cd ocean-data-daily-report

# 2. 检查环境
python check_env.py

# 3. 一键发布
python deploy_report.py
```

### 方式2: 手动发布

```bash
# 1. 生成日报
python generate_html_report.py

# 2. 复制到posts目录
cp daily_reports/海洋AI简报_YYYY-MM-DD.html posts/YYYY-MM-DD.html

# 3. 提交推送
git add posts/YYYY-MM-DD.html index.html
git commit -m "Add YYYY-MM-DD daily report"
git push origin main
```

## 📋 系统要求

### 必需软件
- Python 3.7+
- Git 2.20+

### Python依赖
```bash
pip install requests beautifulsoup4 lxml
```

## 📁 项目结构

```
ocean-data-daily-report/
├── deploy_report.py              # 🚀 一键发布脚本
├── check_env.py                  # 🔧 环境检查脚本
├── generate_html_report.py     # 📝 HTML生成脚本
├── DEPLOYMENT_GUIDE.md          # 📖 部署迁移指南
├── README.md                    # 📄 本文档
│
├── SECTIONS.json                # 🔍 搜索结果数据
├── search_strategy.md          # 🎯 检索策略说明
│
├── daily_reports/               # 📁 生成的日报(本地)
│   └── 海洋AI简报_YYYY-MM-DD.html
│
├── posts/                      # 🌐 发布到网站的日报
│   └── YYYY-MM-DD.html
│
├── index.html                  # 🏠 网站首页
│
└── logs/                       # 📋 日志目录
    └── deploy_YYYYMMDD_HHMMSS.log
```

## 🛠️ 核心脚本说明

### 1. `deploy_report.py` - 一键发布脚本

自动化完成以下流程:
1. 检查部署锁(避免多机冲突)
2. 拉取最新代码
3. 生成今日日报HTML
4. 复制到posts目录
5. 更新index.html
6. 提交并推送到GitHub

**使用方法**:
```bash
python deploy_report.py
```

### 2. `check_env.py` - 环境检查脚本

检查以下项目:
- Python版本和依赖包
- Git配置和远程仓库连接
- 关键文件是否存在
- 目录结构是否完整

**使用方法**:
```bash
python check_env.py
```

### 3. `generate_html_report.py` - HTML生成脚本

根据`SECTIONS.json`中的搜索结果生成HTML格式的日报。

**使用方法**:
```bash
python generate_html_report.py
```

## 🌍 多机部署

支持在多台计算机上运行相同的发布任务。详细配置请参考 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)。

### 快速配置步骤

1. **克隆仓库到新机器**
```bash
git clone https://github.com/tianyunsu/ocean-data-daily-report.git
cd ocean-data-daily-report
```

2. **配置Git认证**
```bash
# 使用SSH(推荐)
ssh-keygen -t ed25519 -C "your_email@example.com"
# 将公钥添加到GitHub: ~/.ssh/id_ed25519.pub

# 测试连接
ssh -T git@github.com
```

3. **检查环境**
```bash
python check_env.py
```

4. **首次运行**
```bash
python deploy_report.py
```

### 多机协作策略

#### 策略1: 主备模式
- 主机: 每日9:00自动发布
- 备机: 10:00后检查,如未发布则补充

#### 策略2: 轮换模式
- 不同日期由不同机器发布
- 通过锁定机制避免冲突

#### 策略3: Pull Request模式
- 每台机器在独立分支上发布
- 通过PR合并到main分支

详细说明请参考 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)。

## ⏰ 定时任务配置

### Windows任务计划程序

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器: 每天上午9点
4. 操作: 启动程序
   - 程序: `python.exe`
   - 参数: `C:\path\to\ocean-data-daily-report\deploy_report.py`

### macOS/Linux Cron

```bash
# 编辑crontab
crontab -e

# 添加以下行(每天9:00运行)
0 9 * * * cd /path/to/ocean-data-daily-report && python deploy_report.py >> logs/deploy.log 2>&1
```

### WorkBuddy自动化

如果使用WorkBuddy,可以创建自动化任务:
- 名称: 海洋AI日报自动发布
- 计划: 每天上午9点
- 命令: 运行 deploy_report.py 脚本

## 📊 研究方向覆盖

系统覆盖以下9个海洋AI相关研究方向:

1. **海洋AI (Ocean AI)** - 海洋人工智能研究
2. **数字孪生 (Digital Twin)** - 海洋数字孪生技术
3. **可视化 (Visualization)** - 海洋数据可视化
4. **数据质量 (Data Quality)** - 海洋数据质量控制
5. **数据处理 (Data Processing)** - 海洋数据处理技术
6. **数据管理 (Data Management)** - 海洋数据管理
7. **开放航次 (Open Cruises)** - 海洋开放航次数据
8. **海洋数据中心 (Ocean Data Centers)** - 海洋数据中心动态
9. **工具与代码资源 (Tools & Code)** - 海洋数据处理工具和代码资源

## 🔧 常见问题

### Q: Git推送失败,提示认证错误?
**A**: 
- 检查SSH密钥是否正确配置
- 或使用Personal Access Token: GitHub Settings -> Developer settings -> Personal access tokens

### Q: Python依赖包缺失?
**A**: 
```bash
pip install -r requirements.txt
# 或
pip install requests beautifulsoup4 lxml
```

### Q: 日报日期不是当天?
**A**: 检查 `generate_html_report.py` 中的日期计算,确保使用当天日期。

### Q: 多台机器同时发布产生冲突?
**A**: 
- 使用部署锁机制(deploy.lock)
- 或采用时间分片策略
- 详细说明见 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 📝 更新日志

### 2026-03-30
- ✅ 添加一键发布脚本 `deploy_report.py`
- ✅ 添加环境检查脚本 `check_env.py`
- ✅ 添加多机部署迁移指南 `DEPLOYMENT_GUIDE.md`
- ✅ 支持多机部署和协作
- ✅ 添加日志记录功能
- ✅ 优化日报生成流程

### 2026-03-27
- ✅ 初始化GitHub Pages网站
- ✅ 创建基本的日报生成流程

## 🤝 贡献指南

欢迎提交Issue和Pull Request!

## 📄 许可证

MIT License

## 📧 联系方式

- GitHub Issues: https://github.com/tianyunsu/ocean-data-daily-report/issues
- 网站: https://tianyunsu.github.io/ocean-data-daily-report/

---

**最后更新**: 2026-03-30
**版本**: v1.0
