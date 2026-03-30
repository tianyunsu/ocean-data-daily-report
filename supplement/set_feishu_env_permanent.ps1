# 永久设置飞书环境变量
# 警告：这会在用户级别设置环境变量，需要管理员权限

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  永久设置飞书环境变量" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "⚠️ 这将在用户级别设置环境变量，请确认是否继续？" -ForegroundColor Yellow
$confirm = Read-Host "输入 'yes' 继续，其他任何键取消"

if ($confirm -ne "yes") {
    Write-Host "操作已取消" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "正在设置环境变量..." -ForegroundColor Cyan
Write-Host ""

try {
    [System.Environment]::SetEnvironmentVariable("FEISHU_APP_ID", "cli_a93d483f6ff81bca", "User")
    Write-Host "✅ FEISHU_APP_ID 设置成功" -ForegroundColor Green
    
    [System.Environment]::SetEnvironmentVariable("FEISHU_APP_SECRET", "CU3EPesfCzNayK4bqsnh6droaJsf4HV8", "User")
    Write-Host "✅ FEISHU_APP_SECRET 设置成功" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "✅ 所有环境变量设置成功！" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠️ 注意：新的环境变量将在新打开的终端窗口中生效" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "请关闭当前终端，打开新的终端后再运行上传脚本" -ForegroundColor Cyan
    Write-Host ""
    
} catch {
    Write-Host "❌ 设置环境变量失败：" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "请确保以管理员身份运行此脚本" -ForegroundColor Yellow
}
