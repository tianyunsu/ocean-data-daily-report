# 飞书机器人Webhook配置指南

## 目的
配置飞书机器人Webhook，用于自动推送海洋AI研究日报通知到飞书群组。

---

## 第一步：创建飞书自定义机器人

### 方法1：通过飞书群组添加机器人（推荐）

1. **打开飞书群组**
   - 进入要接收日报的飞书群组
   - 点击群组名称进入群组详情

2. **添加机器人**
   - 点击右上角的 **⋯** 菜单
   - 选择 **群组设置** 或 **管理群组**
   - 找到 **群机器人** 或 **应用** 选项
   - 点击 **添加应用** 或 **添加机器人**

3. **创建自定义机器人**
   - 选择 **自定义机器人** 或 **Incoming Webhook**
   - 输入机器人名称，例如：`海洋AI日报机器人`
   - 可选：上传机器人头像
   - 点击 **完成** 或 **创建**

4. **获取Webhook URL**
   - 机器人创建成功后，会显示一个 **Webhook URL**
   - 复制这个URL，格式类似：
     ```
     https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxxxxxxxx
     ```

### 方法2：通过飞书开放平台（高级）

如果上述方法不可用，可通过开放平台创建：

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 创建应用 → 选择 **机器人**
3. 配置机器人权限（消息发送）
4. 获取对应的Webhook地址

---

## 第二步：配置环境变量

### Windows 用户

#### 方法A：设置用户级环境变量（推荐）

1. **打开环境变量设置**
   - 右键点击 **此电脑** 或 **我的电脑**
   - 选择 **属性**
   - 点击 **高级系统设置**
   - 点击 **环境变量** 按钮

2. **添加新的用户变量**
   - 在 **用户变量** 部分，点击 **新建**
   - 变量名：`FEISHU_WEBHOOK_URL`
   - 变量值：粘贴刚才复制的Webhook URL
   - 点击 **确定**

3. **重启终端**
   - 关闭所有打开的PowerShell/CMD窗口
   - 重新打开一个新窗口，新设置才会生效

#### 方法B：通过PowerShell设置（快速）

打开 PowerShell（**以管理员身份运行**），执行：

```powershell
[System.Environment]::SetEnvironmentVariable('FEISHU_WEBHOOK_URL', 'https://open.feishu.cn/open-apis/bot/v2/hook/你的WebhookURL', 'User')
```

替换 `你的WebhookURL` 为实际的Webhook地址。

然后重启PowerShell使其生效。

#### 方法C：在Python脚本中临时设置（测试用）

编辑 `run_daily_report.py`，在顶部添加：

```python
import os
os.environ['FEISHU_WEBHOOK_URL'] = 'https://open.feishu.cn/open-apis/bot/v2/hook/你的WebhookURL'
```

---

## 第三步：测试Webhook连接

### 运行测试脚本

创建文件 `test_feishu_webhook.py`：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')

if not webhook_url:
    print("错误：FEISHU_WEBHOOK_URL 环境变量未设置")
    print("请先按照指南配置环境变量")
    exit(1)

print(f"Webhook URL: {webhook_url[:50]}...")

# 发送测试消息
test_payload = {
    "msg_type": "interactive",
    "card": {
        "header": {
            "title": {"tag": "plain_text", "content": "🌊 飞书机器人配置测试"},
            "template": "blue"
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "✅ **测试成功！**\n\n飞书Webhook连接正常，您现在可以接收海洋AI日报通知了。"
                }
            }
        ]
    }
}

try:
    response = requests.post(webhook_url, json=test_payload, timeout=15)
    result = response.json()
    
    if response.status_code == 200 and result.get('StatusCode') == 0:
        print("✅ 测试消息发送成功！")
        print(f"响应: {result}")
    else:
        print(f"❌ 发送失败: {result}")
except Exception as e:
    print(f"❌ 连接异常: {e}")
```

运行测试：

```bash
cd C:/Users/Administrator/WorkBuddy/Claw
python test_feishu_webhook.py
```

---

## 第四步：启用日报推送

配置完成后，运行日报脚本时会自动推送消息：

```bash
cd C:/Users/Administrator/WorkBuddy/Claw
python run_daily_report.py
```

脚本会检测环境变量 `FEISHU_WEBHOOK_URL`，如果已配置，会自动推送包含以下内容的飞书卡片：

- 📅 日报日期
- 🎯 七大研究方向摘要
- 📄 飞书云文档链接
- 🔗 所有资源链接

---

## 常见问题

### Q1：如何获取自己的Webhook URL？

**A：** 按照第一步操作，机器人创建后会显示Webhook URL。如果忘记了：

1. 打开飞书群组
2. 找到机器人管理界面
3. 编辑或查看机器人详情
4. 复制Webhook URL

### Q2：Webhook URL可以泄露吗？

**A：** 
- **有风险**：Webhook URL本身没有密钥验证，任何人知道它都可以发送消息
- **建议**：不要在公开场所分享Webhook URL（如GitHub公开仓库）
- **如果泄露**：在飞书机器人管理界面重新生成新的Webhook URL

### Q3：怎么验证环境变量是否生效？

**A：** 在PowerShell中运行：

```powershell
[System.Environment]::GetEnvironmentVariable('FEISHU_WEBHOOK_URL', 'User')
```

如果返回Webhook URL，说明配置成功。

### Q4：推送消息包含哪些内容？

**A：** 消息卡片包含：
- 日报标题和日期
- 七大研究方向说明
- 飞书云文档链接
- 自动化工具标签

### Q5：如何修改推送消息内容？

**A：** 编辑 `run_daily_report.py` 的第82-114行，修改 `card_content` 字典中的相关内容。

---

## 应用到自动化任务

配置完 Webhook 后，编辑自动化任务触发脚本，确保 `run_daily_report.py` 被执行：

```bash
cd C:/Users/Administrator/WorkBuddy/Claw && py run_daily_report.py
```

每次自动化任务运行时，会自动检测环境变量并推送消息到飞书群组。

---

## 支持信息

- 📖 飞书官方文档：https://open.feishu.cn/document
- 💬 飞书开发者社区：https://open.feishu.cn/
- 📧 联系 WorkBuddy 支持：参考 FEISHU_SETUP_GUIDE.md

