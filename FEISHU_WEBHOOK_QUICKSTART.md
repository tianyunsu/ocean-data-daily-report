# 飞书机器人推送快速开始指南

## 概述
完成以下步骤后，海洋AI研究日报将自动推送到你的飞书群组。

---

## 快速5分钟配置

### 步骤1：创建飞书机器人（2分钟）

1. 打开飞书，进入接收日报的群组
2. 点击群组右上角 **⋯** → **群组设置** → **群机器人**
3. 点击 **+添加机器人** → **自定义机器人**
4. 输入名称：`海洋AI日报机器人`
5. 点击 **完成**，复制弹出的 **Webhook URL**

**Webhook URL 示例：**
```
https://open.feishu.cn/open-apis/bot/v2/hook/2ca51d3c-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### 步骤2：配置环境变量（2分钟）

**方法A：PowerShell 快速配置（推荐）**

1. 按 `Win + R`，输入 `powershell`，按 `Ctrl + Shift + Enter` 以管理员身份运行
2. 粘贴以下命令（替换 URL）：
   ```powershell
   [System.Environment]::SetEnvironmentVariable('FEISHU_WEBHOOK_URL', 'https://open.feishu.cn/open-apis/bot/v2/hook/你的URL', 'User')
   ```
3. 关闭所有PowerShell窗口，重新打开一个新窗口

**方法B：控制面板配置**

1. 右键 **此电脑** → **属性** → **高级系统设置** → **环境变量**
2. 点击 **新建** → 添加
   - 变量名：`FEISHU_WEBHOOK_URL`
   - 变量值：粘贴你的 Webhook URL
3. 点击 **确定**，重启PowerShell

### 步骤3：验证配置（1分钟）

打开PowerShell，进入项目目录：

```powershell
cd C:/Users/Administrator/WorkBuddy/Claw
python test_feishu_webhook.py
```

**预期输出：**
```
[✓] 环境变量已设置
[*] 正在发送测试消息...
[✓] 测试成功！
```

如果看到这个输出，说明配置成功！现在飞书群组应该收到一条测试消息。

---

## 启用自动推送

### 手动运行日报推送

```powershell
cd C:/Users/Administrator/WorkBuddy/Claw
python run_daily_report.py
```

脚本会：
1. ✅ 执行网络搜索
2. ✅ 生成HTML简报
3. ✅ 创建飞书云文档
4. ✅ 推送机器人消息到飞书群组

### 自动化定时推送

在 WorkBuddy 的自动化任务中创建每日定时任务：

```bash
python C:/Users/Administrator/WorkBuddy/Claw/run_daily_report.py
```

推荐设置：**每天 09:00 自动运行**

---

## 常见问题排查

### 问题1：环境变量设置后仍不生效

**解决：**
1. 关闭所有打开的 PowerShell/CMD 窗口
2. 重新打开一个新的 PowerShell 窗口
3. 验证设置：`[System.Environment]::GetEnvironmentVariable('FEISHU_WEBHOOK_URL', 'User')`

### 问题2：测试脚本显示"环境变量未设置"

**解决：**
- 确认已执行第2步中的环境变量设置命令
- 确认是否在PowerShell中以**管理员身份**运行
- 检查命令中的Webhook URL 是否正确无误

### 问题3：收到错误 "StatusCode != 0"

**原因可能：**
- Webhook URL 已过期（飞书有时间限制）
- 群组删除了机器人
- Webhook URL 格式错误

**解决：**
- 重新进入飞书群组，删除旧机器人，创建新机器人
- 复制新的 Webhook URL
- 更新环境变量

### 问题4：脚本运行成功但飞书群组没有收到消息

**检查：**
1. 确认发送到了正确的群组（机器人配置时选择的群组）
2. 确认机器人权限已启用
3. 检查 `test_feishu_webhook.py` 输出，是否显示 `[✓] 测试成功`

---

## 推送消息效果预览

配置完成后，你会在飞书群组收到这样的消息卡片：

```
🌊 海洋AI技术日报 · 2026年03月18日

今日涵盖主题：
🤖 海洋人工智能 | 🌐 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理 | 🗄️ 数据管理与共享 | 🚢 开放航次/船时共享

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 完整简报（飞书文档）：
[链接到飞书云文档]

由 WorkBuddy 自动生成 · 每日09:00推送
```

点击文档链接即可查看详细的31条研究资讯。

---

## 支持文档

- 📖 详细配置指南：`FEISHU_WEBHOOK_SETUP.md`
- 🧪 测试脚本：`test_feishu_webhook.py`
- 🔧 日报脚本：`run_daily_report.py`
- 📝 飞书官方文档：https://open.feishu.cn/document

---

## 下一步

配置完成后，你可以：

1. **查看已有日报**
   - HTML版本：`daily_reports/海洋AI简报_YYYY-MM-DD.html`
   - 飞书版本：查看飞书群组消息中的文档链接

2. **自定义推送内容**
   - 编辑 `run_daily_report.py` 中的卡片内容（第82-114行）
   - 修改日报推送标题、主题等

3. **设置自动化任务**
   - 在 WorkBuddy 中创建定时任务
   - 每天自动推送最新研究进展

---

**配置完成？** 运行以下命令验证：
```bash
python C:/Users/Administrator/WorkBuddy/Claw/test_feishu_webhook.py
```

祝配置顺利！🎉
