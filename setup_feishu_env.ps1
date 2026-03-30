# 飞书环境变量设置脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  飞书环境变量配置工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 设置环境变量（当前会话）
$env:FEISHU_APP_ID = "cli_a93d483f6ff81bca"
$env:FEISHU_APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"

# 可选：设置文件夹 token
# $env:FEISHU_FOLDER_TOKEN = "your_folder_token_here"

Write-Host "✅ 环境变量已设置（当前会话）" -ForegroundColor Green
Write-Host ""
Write-Host "已设置的变量：" -ForegroundColor Yellow
Write-Host "  FEISHU_APP_ID = $env:FEISHU_APP_ID" -ForegroundColor White
Write-Host "  FEISHU_APP_SECRET = *** (已隐藏)" -ForegroundColor White
Write-Host ""

Write-Host "⚠️ 注意：这些环境变量仅在当前 PowerShell 会话中有效" -ForegroundColor Yellow
Write-Host ""
Write-Host "如果要永久设置环境变量，请运行以下命令：" -ForegroundColor Yellow
Write-Host ""
Write-Host '[System.Environment]::SetEnvironmentVariable("FEISHU_APP_ID", "cli_a93d483f6ff81bca", "User")' -ForegroundColor Gray
Write-Host '[System.Environment]::SetEnvironmentVariable("FEISHU_APP_SECRET", "CU3EPesfCzNayK4bqsnh6droaJsf4HV8", "User")' -ForegroundColor Gray
Write-Host ""

Write-Host "现在可以运行上传脚本：" -ForegroundColor Cyan
Write-Host "  python upload_to_feishu.py" -ForegroundColor White
Write-Host ""
