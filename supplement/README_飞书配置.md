# 🔧 解决 PowerShell 执行策略问题

## 问题说明

您遇到的错误是因为 PowerShell 的执行策略设置为 `Restricted`（受限），这会阻止运行任何脚本。

## 🎯 解决方案（3种方法）

---

### 方法一：使用批处理脚本（推荐，最简单）✅

我已经为您创建了批处理版本的配置工具，不需要修改 PowerShell 执行策略。

#### 使用步骤：

1. **右键点击** `QUICK_START.bat`
2. 选择 **"以管理员身份运行"**
3. 按照向导提示操作：

   - 选项 1：修复 PowerShell 执行策略
   - 选项 2：配置环境变量
   - 选项 3：测试飞书文档创建

---

### 方法二：手动修改执行策略（需要管理员权限）

如果您想修改 PowerShell 执行策略，请按以下步骤操作：

#### 1. 以管理员身份打开 PowerShell

- 按 `Win + X`
- 选择「Windows PowerShell (管理员)」或「终端 (管理员)」

#### 2. 查看当前执行策略
```powershell
Get-ExecutionPolicy -List
```

#### 3. 修改执行策略

**方案 A：仅修改当前用户策略（推荐）**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**方案 B：修改本地机器策略（需要管理员权限）**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

#### 4. 验证修改
```powershell
Get-ExecutionPolicy
```

应该显示 `RemoteSigned`

#### 5. 运行原来的 PowerShell 脚本
```powershell
cd C:\Users\Administrator\WorkBuddy\Claw
.\set_feishu_env.ps1
```

---

### 方法三：绕过执行策略（临时）

如果您不想修改执行策略，可以临时绕过限制：

```powershell
# 绕过执行策略运行单个脚本
powershell.exe -ExecutionPolicy Bypass -File .\set_feishu_env.ps1

# 或者
powershell.exe -ExecutionPolicy Unrestricted -File .\set_feishu_env.ps1
```

---

## 📝 执行策略说明

| 策略 | 说明 | 推荐程度 |
|------|------|---------|
| `Restricted` | 不允许运行任何脚本 | ❌ 最严格 |
| `RemoteSigned` | 本地脚本可运行，远程脚本需签名 | ✅ 推荐 |
| `Unrestricted` | 允许运行所有脚本 | ⚠️ 不安全 |
| `Bypass` | 完全绕过检查 | ⚠️ 临时使用 |

---

## 🚀 推荐操作流程

### 最简单的方式（推荐）：

```
1. 双击运行 QUICK_START.bat
2. 选择选项 [1] 修复执行策略
3. 选择选项 [2] 配置环境变量
4. 选择选项 [3] 测试文档创建
5. 完成！
```

---

## ⚠️ 安全提示

- `RemoteSigned` 是最安全且实用的策略
- 它允许运行本地脚本，但要求远程脚本有数字签名
- 不会降低系统安全性

---

## 🆘 仍然遇到问题？

如果修改执行策略后仍然无法运行脚本：

1. **检查文件路径**
   ```powershell
   Test-Path .\set_feishu_env.ps1
   ```

2. **检查文件编码**
   - 用记事本打开脚本
   - 文件 → 另存为
   - 编码选择 "UTF-8 with BOM"

3. **使用批处理版本**
   - 直接运行 `set_feishu_env.bat`
   - 不需要 PowerShell

---

## 📞 需要帮助？

如果问题仍未解决，请提供：
1. 具体的错误信息
2. 您尝试过的方法
3. 当前执行策略：`Get-ExecutionPolicy -List`
