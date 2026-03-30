# 飞书简报上传工具使用说明

## 📋 功能介绍

自动将本地生成的 HTML 简报上传到飞书云文档，实现简报的云端存储和协作共享。

## 📁 文件说明

- `upload_to_feishu.py` - 主程序脚本
- `setup_feishu_env.ps1` - 临时环境变量设置脚本
- `set_feishu_env_permanent.ps1` - 永久环境变量设置脚本
- `run_upload_to_feishu.bat` - 一键执行批处理文件

## 🔧 使用方法

### 方法一：使用批处理文件（推荐，最简单）

双击运行 `run_upload_to_feishu.bat` 文件，脚本会自动：
1. 设置所需的环境变量
2. 执行上传脚本
3. 显示结果

### 方法二：使用 PowerShell 临时设置

```powershell
# 1. 设置环境变量（仅当前会话有效）
.\setup_feishu_env.ps1

# 2. 执行上传脚本
python upload_to_feishu.py
```

### 方法三：永久设置环境变量

```powershell
# 1. 以管理员身份运行 PowerShell
# 2. 执行永久设置脚本
.\set_feishu_env_permanent.ps1

# 3. 关闭当前终端，打开新的终端
# 4. 执行上传脚本
python upload_to_feishu.py
```

### 方法四：手动设置环境变量

在执行上传脚本前，在命令行中设置：

**PowerShell:**
```powershell
$env:FEISHU_APP_ID = "cli_a93d483f6ff81bca"
$env:FEISHU_APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
```

**CMD:**
```cmd
set FEISHU_APP_ID=cli_a93d483f6ff81bca
set FEISHU_APP_SECRET=CU3EPesfCzNayK4bqsnh6droaJsf4HV8
```

然后运行：
```bash
python upload_to_feishu.py
```

## ⚙️ 环境变量说明

| 变量名 | 必需 | 说明 |
|--------|------|------|
| `FEISHU_APP_ID` | ✅ 必需 | 飞书应用 ID |
| `FEISHU_APP_SECRET` | ✅ 必需 | 飞书应用 Secret |
| `FEISHU_FOLDER_TOKEN` | ⭕ 可选 | 指定保存文档的文件夹 token，不填则保存到应用根目录 |

## 📝 工作流程

1. **获取访问令牌** - 使用应用凭据获取飞书 API 访问令牌
2. **读取本地简报** - 从 `daily_reports` 目录读取最新日期的 HTML 简报文件
3. **创建飞书文档** - 在飞书中创建一个新的 docx 文档
4. **写入内容** - 将 HTML 内容转换为文本块并写入文档
5. **返回链接** - 输出创建的飞书文档链接

## 📄 文件命名规则

脚本会自动查找以下格式的文件（按顺序）：
- `海洋AI简报_YYYY-MM-DD.html`
- `海洋AI简报_YYYY-MM-DD-2.html`
- `海洋AI简报_YYYY-MM-DD-3.html`

例如：`海洋AI简报_2026-03-15.html`

## ⚠️ 注意事项

1. **环境变量安全性**
   - 凭据已硬编码在脚本中，请妥善保管
   - 在生产环境中，建议使用更安全的方式管理凭据

2. **内容格式**
   - 当前版本将 HTML 转换为纯文本，格式会简化
   - 如需保留富文本格式，需要更复杂的 HTML 解析和飞书块类型转换

3. **权限要求**
   - 飞书应用需要具有创建文档的权限
   - 如果指定了文件夹，需要有该文件夹的写入权限

4. **网络要求**
   - 需要能够访问飞书 API（open.feishu.cn）

5. **日期计算**
   - 脚本默认上传昨天的简报
   - 如需上传其他日期的简报，请修改脚本中的日期计算逻辑

## 🐛 常见问题

### Q1: 提示"未找到简报文件"
**A:** 检查 `daily_reports` 目录下是否存在对应日期的 HTML 文件，文件命名格式是否正确。

### Q2: 提示"获取访问令牌失败"
**A:** 检查 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 是否正确设置。

### Q3: 创建文档成功但内容写入失败
**A:** 这是非致命错误，文档已创建，可以手动复制内容到飞书文档。这通常是因为 HTML 内容格式复杂导致的。

### Q4: 如何上传今天的简报？
**A:** 修改 `upload_to_feishu.py` 中的日期计算，将 `timedelta(days=1)` 改为 `timedelta(days=0)`。

## 🚀 自动化建议

可以将此工具设置为定时任务，自动上传每天的简报：

**Windows 任务计划程序：**
1. 创建基本任务
2. 设置触发器（例如每天上午 9:00）
3. 操作：启动程序 `python.exe`，参数为 `upload_to_feishu.py` 脚本完整路径
4. 在环境变量中设置凭据，或使用批处理文件

## 📞 技术支持

如有问题，请检查：
1. Python 版本是否为 3.6+
2. `requests` 库是否已安装（`pip install requests`）
3. 网络连接是否正常
4. 飞书应用权限配置是否正确
