# 飞书日报助手环境变量配置脚本
# 请替换为您真实的凭证信息

$env:FEISHU_APP_ID = "cli_a93d483f6ff81bca"           # 替换为您的 App ID
$env:FEISHU_APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"     # 替换为您的 App Secret
$env:FEISHU_FOLDER_TOKEN = "box_xxxxxxxxxxxxx"   # 可选：替换为文件夹 Token

Write-Host "=== 飞书环境变量已设置 ===" -ForegroundColor Green
Write-Host "App ID: $env:FEISHU_APP_ID" -ForegroundColor Cyan
Write-Host "App Secret: $env:FEISHU_APP_SECRET.Substring(0,10)..." -ForegroundColor Cyan
Write-Host "Folder Token: $env:FEISHU_FOLDER_TOKEN" -ForegroundColor Cyan
Write-Host ""
Write-Host "提示：这些环境变量仅在当前PowerShell会话中有效" -ForegroundColor Yellow
Write-Host "如需永久设置，请参考文档说明" -ForegroundColor Yellow
