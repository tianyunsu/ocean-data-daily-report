# GitHub Pages发布指南

## 目的
将海洋AI研究日报的HTML简报发布到GitHub Pages网站，实现自动化的在线访问。

---

## 前置准备

### 1. 创建GitHub仓库

1. 登录 [GitHub](https://github.com/)
2. 点击右上角 **+** → **New repository**
3. 填写仓库信息：
   - **Repository name**: `ocean-ai-daily-report`（或其他名称）
   - **Description**: 海洋AI研究日报每日更新
   - **Public** 或 **Private**（公开仓库的GitHub Pages免费）
4. 点击 **Create repository**

### 2. 配置Git（首次使用）

```bash
# 配置用户信息
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@163.com"

# 初始化本地仓库
cd C:\Users\Administrator\WorkBuddy\Claw
git init

# 添加远程仓库
git remote add origin https://github.com/<你的用户名>/ocean-ai-daily-report.git
```

---

## 快速开始（3步完成）

### 步骤1：生成今日日报

```bash
cd C:\Users\Administrator\WorkBuddy\Claw
python generate_html_report.py
```

输出：
```
[OK] HTML报告已生成: C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_2026-03-30.html

     共 9 个方向，23 条动态
```

### 步骤2：发布到GitHub Pages

```bash
python publish_to_github_pages.py
```

脚本会自动完成以下操作：
1. 创建或切换到`gh-pages`分支
2. 复制今日HTML文件到网站目录
3. 创建首页index.html
4. 提交更改
5. 推送到GitHub

### 步骤3：启用GitHub Pages

1. 打开刚创建的GitHub仓库
2. 点击 **Settings** 标签
3. 左侧菜单找到 **Pages**
4. 配置Source：
   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages` / `(root)`
5. 点击 **Save**

等待1-2分钟，GitHub会自动部署网站。

---

## 访问你的网站

部署成功后，访问：

```
https://<你的用户名>.github.io/ocean-ai-daily-report/
```

示例（假设用户名为`yourname`）：
```
https://yourname.github.io/ocean-ai-daily-report/
```

---

## 每日更新流程

### 方法1：手动发布（推荐测试）

每天执行以下命令：

```bash
cd C:\Users\Administrator\WorkBuddy\Claw

# 1. 生成今日日报
python generate_html_report.py

# 2. 发布到GitHub Pages
python publish_to_github_pages.py
```

### 方法2：设置自动化任务（推荐）

在WorkBuddy中创建定时任务，每天自动执行。

#### 创建自动化任务

在WorkBuddy中运行以下命令：

```
创建一个自动化任务：
- 名称：海洋AI日报GitHub发布
- 执行时间：每天上午9点
- 工作目录：C:/Users/Administrator/WorkBuddy/Claw
- 执行命令：python generate_html_report.py && python publish_to_github_pages.py
```

或者使用automation_update工具配置。

---

## 脚本说明

### publish_to_github_pages.py

**功能：**
- 自动创建和管理`gh-pages`分支
- 复制HTML文件到网站目录
- 生成首页index.html
- 提交并推送更改到GitHub

**参数：**
- 无需参数，自动使用今日日期

**输出：**
- 成功：显示GitHub Pages URL
- 失败：显示具体错误信息

---

## 常见问题

### Q1: 提示"not a git repository"

**解决方案：**
```bash
cd C:\Users\Administrator\WorkBuddy\Claw
git init
git remote add origin https://github.com/<用户名>/<仓库名>.git
```

### Q2: git push失败，提示认证错误

**解决方案：**

使用Personal Access Token（推荐）：
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → 选择`repo`权限
3. 复制生成的token
4. 修改remote URL：
   ```bash
   git remote set-url origin https://<token>@github.com/<用户名>/<仓库名>.git
   ```

### Q3: GitHub Pages无法访问

**检查清单：**

1. 确认仓库是**Public**的（Private仓库需要GitHub Pro）
2. 确认Pages设置中Branch是`gh-pages`和`(root)`
3. 检查Settings → Pages中的部署状态
4. 等待2-3分钟，GitHub部署需要时间

### Q4: 如何自定义网站样式？

编辑以下文件：

1. **首页样式**：修改`publish_to_github_pages.py`中的`index_content`变量
2. **日报样式**：修改`generate_html_report.py`中的CSS样式

---

## 高级功能

### 1. 添加历史报告列表

在`publish_to_github_pages.py`中添加逻辑，自动生成历史报告列表。

### 2. 添加搜索功能

使用JavaScript在前端实现搜索，或者使用GitHub自带的搜索。

### 3. 添加RSS订阅

创建`rss.xml`文件，让用户可以订阅日报更新。

### 4. 多语言支持

修改`generate_html_report.py`，同时生成中文和英文版本。

---

## 文件结构

```
Claw/
├── daily_reports/
│   ├── 海洋AI简报_2026-03-30.html
│   ├── 海洋AI简报_2026-03-29.html
│   └── ...
├── index.html (首页，由脚本自动生成)
├── generate_html_report.py (生成HTML)
├── publish_to_github_pages.py (发布到GitHub)
├── feishu_write_doc.py (飞书文档，可选)
└── run_daily_report.py (完整流程，可选)
```

---

## 总结

通过GitHub Pages发布海洋AI研究日报的优势：

✅ **免费托管**：GitHub Pages完全免费  
✅ **自定义域名**：可以绑定自己的域名  
✅ **HTTPS支持**：自动提供HTTPS加密  
✅ **版本控制**：Git管理所有历史版本  
✅ **易于访问**：只需一个URL即可访问  
✅ **自动化友好**：可集成到CI/CD流程  

---

## 需要帮助？

如果遇到问题，请提供：

1. 错误信息
2. 执行的命令
3. Git仓库配置（`git remote -v`）
4. GitHub Pages设置截图
