# 📘 飞书云文档发布 - 完整配置指南

## 📋 快速开始

### 第一步：创建飞书自建应用（5分钟）

1. 登录 [飞书开放平台](https://open.feishu.cn/)
2. 点击「创建应用」→「自建应用」
3. 应用名称：海洋AI日报助手
4. 创建后进入应用详情页

### 第二步：获取应用凭证

在「凭证与基础信息」页面，记录：
- **App ID**：类似 `cli_xxxxxxxxxxxxx`
- **App Secret**：点击「查看」复制

### 第三步：开通权限

在「权限管理」页面，申请以下权限：
- ✅ `docx:document` - 创建和编辑文档
- ✅ `drive:drive:readonly` - 读取云文档信息

点击「申请权限」或「开通权限」

### 第四步：（可选）获取文件夹Token

如果想保存到特定文件夹：

1. 打开飞书云文档，进入目标文件夹
2. 复制浏览器地址栏中的 Token（格式：`box_xxxxxxxxxxxxx`）

### 第五步：设置环境变量

#### 方式A：临时设置（推荐用于测试）

在 PowerShell 中执行：

```powershell
cd C:\Users\Administrator\WorkBuddy\Claw

# 编辑 set_feishu_env.ps1，填入您的真实凭证
notepad set_feishu_env.ps1

# 运行配置脚本
.\set_feishu_env.ps1

# 测试飞书文档创建
node test_feishu_doc.js
```

#### 方式B：永久设置（推荐用于自动化）

```powershell
# 以管理员身份运行 PowerShell
cd C:\Users\Administrator\WorkBuddy\Claw

# 编辑 set_feishu_env_permanent.ps1，填入您的真实凭证
notepad set_feishu_env_permanent.ps1

# 运行永久配置脚本
.\set_feishu_env_permanent.ps1

# 重启 PowerShell 使环境变量生效
```

### 第六步：测试飞书文档创建

```powershell
# 确保已设置环境变量
$env:FEISHU_APP_ID  # 检查是否有值
$env:FEISHU_APP_SECRET  # 检查是否有值

# 运行测试脚本
node C:\Users\Administrator\WorkBuddy\Claw\test_feishu_doc.js
```

**预期输出：**
```
=== 飞书云文档创建测试 ===

✓ 环境变量检查通过

步骤1/3：获取访问令牌...
✓ 访问令牌获取成功

步骤2/3：创建飞书文档...
✓ 文档创建成功！
  文档ID：doxcnxxxxxxxxxxxxx
  文档URL：https://docs.feishu.cn/docx/doxcnxxxxxxxxxxxxx

步骤3/3：添加文档内容...
✓ 文档内容添加成功

=== 测试完成 ===
🎉 恭喜！飞书云文档配置成功！
```

---

## ✅ 测试成功后

测试成功后，自动化任务将自动创建飞书云文档。

运行日报任务：
```powershell
# 每日自动执行（已配置自动化）
# 或者手动执行：
node C:\Users\Administrator\WorkBuddy\Claw\publish_report.js
```

---

## 🔧 故障排查

### 问题1：环境变量未设置

**错误信息：**
```
❌ 错误：环境变量未设置
```

**解决方案：**
```powershell
# 重新设置环境变量
$env:FEISHU_APP_ID = "你的App ID"
$env:FEISHU_APP_SECRET = "你的App Secret"

# 验证设置
$env:FEISHU_APP_ID
$env:FEISHU_APP_SECRET
```

### 问题2：获取令牌失败

**错误信息：**
```
❌ 获取令牌失败
  错误码：99991663
  错误信息：app not exist
```

**解决方案：**
1. 检查 App ID 是否正确复制
2. 确认应用已创建且已激活
3. 检查 App Secret 是否正确

### 问题3：权限不足

**错误信息：**
```
❌ 创建文档失败
  错误码：99991401
  错误信息：no permission
```

**解决方案：**
1. 进入飞书开放平台应用管理
2. 在「权限管理」中开通所需权限
3. 等待权限开通生效（通常1-2分钟）

### 问题4：文件夹Token无效

**错误信息：**
```
❌ 创建文档失败
  错误码：99991400
  错误信息：folder not exist
```

**解决方案：**
1. 确认文件夹 Token 格式正确（box_xxxxx）
2. 确认文件夹存在且有访问权限
3. 或者不设置 `FEISHU_FOLDER_TOKEN`，文档会保存到应用根目录

---

## 📚 飞书API 参考

- **官方文档**：https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/document/create
- **认证文档**：https://open.feishu.cn/document/server-docs/authentication-management/access-token/tenant_access_token
- **权限说明**：https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/document/create#请求权限

---

## 💡 最佳实践

1. **安全性**
   - 不要将 App Secret 硬编码在代码中
   - 定期更换 App Secret
   - 限制应用权限范围

2. **组织管理**
   - 将日报保存到统一文件夹
   - 使用规范的命名格式
   - 定期清理过期文档

3. **自动化**
   - 设置固定执行时间（如每日09:00）
   - 配置错误通知机制
   - 定期检查自动化运行状态

---

## 🆘 需要帮助？

如遇到问题，请检查：
1. ✅ 飞书应用是否正确创建
2. ✅ App ID 和 Secret 是否正确
3. ✅ 权限是否已开通
4. ✅ 环境变量是否正确设置
5. ✅ 网络连接是否正常

如仍未解决，请查看飞书开放平台文档或联系飞书技术支持。
