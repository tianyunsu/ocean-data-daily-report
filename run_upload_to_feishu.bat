@echo off
chcp 65001 >nul
echo ========================================
echo   飞书简报上传工具
echo ========================================
echo.

REM 设置环境变量
set FEISHU_APP_ID=cli_a93d483f6ff81bca
set FEISHU_APP_SECRET=CU3EPesfCzNayK4bqsnh6droaJsf4HV8

echo 环境变量已设置
echo.
echo 开始上传到飞书...
echo.

python upload_to_feishu.py

echo.
echo ========================================
echo   按任意键退出...
echo ========================================
pause >nul
