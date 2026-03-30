# 🌊 飞书机器人推送 - 完整资源导航

## 📚 配置文档（按阅读顺序）

### ⭐ 第一步：快速开始指南（必读）
**文件**：`FEISHU_WEBHOOK_QUICKSTART.md`
- **时间**：5分钟快速配置
- **内容**：
  - 创建飞书机器人步骤
  - PowerShell环境变量设置
  - 配置验证方法
  - 常见问题快速排查
- **推荐**：首先阅读这个文件

### 📖 第二步：详细配置指南（参考）
**文件**：`FEISHU_WEBHOOK_SETUP.md`
- **时间**：完整深入讲解
- **内容**：
  - 两种机器人创建方法
  - 三种环境变量设置方式
  - 测试脚本详细说明
  - FAQ完整解答
  - 自动化任务集成方案
- **推荐**：遇到问题时查阅

### 🔧 现有参考文档
**文件**：`FEISHU_SETUP_GUIDE.md`（原有）
**文件**：`README_飞书配置.md`（原有）
- 这些是项目历史文件，可作为补充参考

---

## 🧪 测试和验证工具

### 验证配置工具
**文件**：`test_feishu_webhook.py`
- **功能**：测试Webhook连接是否正常
- **使用方法**：
  ```bash
  cd C:/Users/Administrator/WorkBuddy/Claw
  python test_feishu_webhook.py
  ```
- **预期输出**：
  - ✅ 成功：`[✓] 测试成功！`
  - ❌ 失败：显示具体错误原因和解决方案
- **何时使用**：
  - 配置后验证
  - 出现问题时诊断

### 现有测试脚本
**文件**：`test_feishu_doc.bat` / `test_feishu_doc.js`
- 用于测试飞书文档创建（可选参考）

---

## 🔄 核心执行脚本

### 日报推送脚本（主要）
**文件**：`run_daily_report.py`
- **功能**：运行完整的日报推送流程
- **执行步骤**：
  1. 网络搜索→2. HTML生成→3. 飞书文档→4. 机器人推送
- **使用**：
  ```bash
  python C:/Users/Administrator/WorkBuddy/Claw/run_daily_report.py
  ```
- **依赖**：
  - `feishu_write_doc.py`（文档创建）
  - `FEISHU_WEBHOOK_URL` 环境变量（机器人推送）
- **输出**：
  - HTML文件：`daily_reports/海洋AI简报_YYYY-MM-DD.html`
  - 飞书文档URL：保存到 `feishu_doc_url.txt`

### 飞书文档写入脚本（辅助）
**文件**：`feishu_write_doc.py`
- **功能**：创建飞书云文档并写入资讯内容
- **调用**：由 `run_daily_report.py` 自动调用
- **可独立使用**：
  ```bash
  python feishu_write_doc.py
  ```

### 其他执行脚本（备选）
- `publish_report.py` / `publish_report.js`
- `upload_to_feishu.py`
- `run_upload_to_feishu.bat`
- （这些是历史版本或备选方案）

---

## ⚙️ 环境变量设置工具

### PowerShell 设置脚本
**文件**：
- `setup_feishu_env.ps1`（推荐）
- `set_feishu_env.ps1`（备选）
- `set_feishu_env_permanent.ps1`（高级）

**使用**：
```powershell
.\setup_feishu_env.ps1
```

### 批处理设置脚本
**文件**：
- `set_feishu_env.bat`
- `QUICK_START.bat`

**使用**：
```bash
set_feishu_env.bat
```

### 手动设置（推荐）
不推荐使用脚本，建议直接在PowerShell中运行：
```powershell
[System.Environment]::SetEnvironmentVariable('FEISHU_WEBHOOK_URL', 'your_url', 'User')
```

---

## 📁 文件组织结构

```
C:/Users/Administrator/WorkBuddy/Claw/
│
├── 【配置指南】
│   ├── FEISHU_WEBHOOK_QUICKSTART.md    ← ⭐ 快速开始
│   ├── FEISHU_WEBHOOK_SETUP.md         ← 详细指南
│   ├── FEISHU_SETUP_GUIDE.md           ← 原有参考
│   └── README_飞书配置.md              ← 原有参考
│
├── 【执行脚本】
│   ├── run_daily_report.py             ← 🔴 主脚本
│   ├── feishu_write_doc.py             ← 文档创建
│   ├── publish_report.py               ← 备选
│   └── upload_to_feishu.py             ← 备选
│
├── 【测试工具】
│   ├── test_feishu_webhook.py          ← ⭐ Webhook验证
│   ├── test_feishu_doc.bat             ← 文档测试
│   └── test_feishu_doc.js              ← 文档测试
│
├── 【环境设置】
│   ├── setup_feishu_env.ps1
│   ├── set_feishu_env.ps1
│   ├── set_feishu_env.bat
│   └── QUICK_START.bat
│
├── 【输出文件】
│   ├── daily_reports/
│   │   └── 海洋AI简报_YYYY-MM-DD.html
│   ├── feishu_doc_url.txt              ← 文档链接
│   └── feishu_doc_url_import.txt
│
└── 【其他】
    ├── package.json
    ├── .codebuddy/
    │   └── automations/ai/
    │       └── memory.md               ← 执行记录
    └── [其他历史文件]
```

---

## 🎯 快速查询表

| 我想... | 查看文件 | 操作 |
|--------|---------|------|
| **快速配置飞书机器人** | `FEISHU_WEBHOOK_QUICKSTART.md` | 按步骤操作（5分钟） |
| **详细了解配置方案** | `FEISHU_WEBHOOK_SETUP.md` | 深入阅读 |
| **验证Webhook配置** | `test_feishu_webhook.py` | `python test_feishu_webhook.py` |
| **运行日报推送** | `run_daily_report.py` | `python run_daily_report.py` |
| **查看执行历史** | `.codebuddy/automations/ai/memory.md` | 查看记录 |
| **查看今日简报** | `daily_reports/海洋AI简报_YYYY-MM-DD.html` | 用浏览器打开 |
| **获取文档链接** | `feishu_doc_url.txt` | 查看URL |
| **遇到问题排查** | `FEISHU_WEBHOOK_SETUP.md` FAQ部分 | 查看常见问题 |
| **自动化任务集成** | `FEISHU_WEBHOOK_SETUP.md` 第四步 | 参考设置方案 |

---

## 🚀 建议的使用流程

### 首次配置（15分钟）
1. ✅ 阅读 `FEISHU_WEBHOOK_QUICKSTART.md`（5分钟）
2. ✅ 创建飞书机器人（3分钟）
3. ✅ 设置环境变量（2分钟）
4. ✅ 运行 `test_feishu_webhook.py` 验证（2分钟）
5. ✅ 测试看看能否收到验证消息（3分钟）

### 日常使用（1分钟）
```bash
python C:/Users/Administrator/WorkBuddy/Claw/run_daily_report.py
```
或在自动化任务中配置每天 09:00 自动运行

### 出现问题（按需查阅）
1. 查看 `FEISHU_WEBHOOK_SETUP.md` 的FAQ
2. 运行 `test_feishu_webhook.py` 进行诊断
3. 根据错误消息调整配置

---

## 💡 重要提示

| 事项 | 说明 |
|------|------|
| **Webhook URL 安全** | 包含身份信息，不要分享或上传到公开仓库 |
| **环境变量持久化** | 设置为"用户"级别会永久保存，系统级别需管理员 |
| **重启终端** | 设置环境变量后需重启PowerShell/CMD |
| **测试先行** | 配置后运行 `test_feishu_webhook.py` 验证 |
| **错误诊断** | 测试脚本会给出具体的错误原因和解决方案 |

---

## 📞 技术支持资源

- 📖 飞书官方文档：https://open.feishu.cn/document
- 🔗 飞书开发者社区：https://open.feishu.cn/
- 💬 本地参考文件：`FEISHU_WEBHOOK_SETUP.md` 的常见问题部分

---

**目录最后更新**：2026-03-18  
**配置状态**：待激活（等待Webhook URL设置）  
**预计配置时间**：5-15分钟

立即开始：👉 阅读 `FEISHU_WEBHOOK_QUICKSTART.md`

