@echo off
REM 飞书云文档创建测试脚本（批处理版本）
REM 需要先运行 set_feishu_env.bat 设置环境变量

echo =====================================================
echo     飞书日报助手 - 文档创建测试工具
echo =====================================================
echo.

REM 检查环境变量是否已设置
if "%FEISHU_APP_ID%"=="" (
    echo [错误] 环境变量未设置！
    echo.
    echo 请先运行: set_feishu_env.bat
    echo.
    pause
    exit /b 1
)

if "%FEISHU_APP_SECRET%"=="" (
    echo [错误] 环境变量未设置！
    echo.
    echo 请先运行: set_feishu_env.bat
    echo.
    pause
    exit /b 1
)

echo [信息] 环境变量检查通过
echo   App ID: %FEISHU_APP_ID%
echo   App Secret: %FEISHU_APP_SECRET:~0,10%...
if not "%FEISHU_FOLDER_TOKEN%"=="" (
    echo   Folder Token: %FEISHU_FOLDER_TOKEN%
)
echo.

REM 检查 Node.js 是否已安装
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到 Node.js！
    echo.
    echo 请先安装 Node.js:
    echo   访问: https://nodejs.org/
    echo   下载并安装 LTS 版本
    echo.
    pause
    exit /b 1
)

echo [信息] Node.js 已安装
node --version
echo.

echo [信息] 开始测试飞书文档创建...
echo.

REM 运行 Node.js 测试脚本
node test_feishu_doc.js

echo.
echo =====================================================
echo           测试完成
echo =====================================================
echo.

REM 检查 Node.js 脚本是否执行成功
if %errorlevel% equ 0 (
    echo [成功] 测试脚本执行完成！
    echo.
    echo 如果测试成功，现在可以运行日报自动化任务了。
) else (
    echo [警告] 测试脚本执行出现问题
    echo.
    echo 请检查错误信息，确保：
    echo   1. 飞书应用凭证正确
    echo   2. 权限已开通
    echo   3. 网络连接正常
)

echo.
pause
