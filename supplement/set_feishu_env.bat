@echo off
REM 飞书日报助手环境变量配置脚本（批处理版本）
REM 无需管理员权限

echo =====================================================
echo     飞书日报助手 - 环境变量配置工具
echo =====================================================
echo.
echo 请输入您的飞书应用凭证信息：
echo.

set /p APP_ID="请输入 App ID (格式: cli_xxxxxxxxxxxxx): "
set /p APP_SECRET="请输入 App Secret: "
set /p FOLDER_TOKEN="请输入文件夹 Token (可选，直接回车跳过): "

echo.
echo [信息] 设置环境变量...
set FEISHU_APP_ID=%APP_ID%
set FEISHU_APP_SECRET=%APP_SECRET%
if not "%FOLDER_TOKEN%"=="" (
    set FEISHU_FOLDER_TOKEN=%FOLDER_TOKEN%
    echo [成功] Folder Token 已设置
) else (
    echo [提示] Folder Token 未设置，文档将保存到应用根目录
)

echo.
echo =====================================================
echo           环境变量配置完成！
echo =====================================================
echo.
echo 已配置的信息：
echo   App ID: %FEISHU_APP_ID%
echo   App Secret: %FEISHU_APP_SECRET:~0,10%...
if not "%FOLDER_TOKEN%"=="" (
    echo   Folder Token: %FEISHU_FOLDER_TOKEN%
)
echo.
echo 注意：这些环境变量仅在当前命令行窗口中有效。
echo       关闭窗口后需要重新设置。
echo.
echo 如果需要永久设置，请使用 set_feishu_env_permanent.bat
echo.
echo 下一步：测试飞书文档创建
echo   运行命令: test_feishu_doc.bat
echo.
pause
