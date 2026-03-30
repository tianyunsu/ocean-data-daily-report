@echo off
REM 解决PowerShell执行策略限制的批处理脚本
REM 需要管理员权限运行

echo =====================================================
echo     飞书日报助手 - 执行策略修复工具
echo =====================================================
echo.

REM 检查是否有管理员权限
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [错误] 需要管理员权限！
    echo.
    echo 请右键点击此文件，选择"以管理员身份运行"
    echo.
    pause
    exit /b 1
)

echo [步骤 1/3] 查看当前执行策略...
powershell.exe -Command "Write-Host '当前执行策略:' (Get-ExecutionPolicy) -ForegroundColor Yellow"
echo.

echo [步骤 2/3] 设置执行策略为 RemoteSigned...
powershell.exe -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"
echo.

echo [步骤 3/3] 验证新的执行策略...
powershell.exe -Command "Write-Host '新的执行策略:' (Get-ExecutionPolicy) -ForegroundColor Green"
echo.

echo =====================================================
echo           执行策略修复完成！
echo =====================================================
echo.
echo 现在您可以正常运行 PowerShell 脚本了。
echo.
echo 下一步：
echo   1. 运行环境变量配置：set_feishu_env.bat
echo   2. 测试飞书文档创建：test_feishu_doc.bat
echo.
pause
