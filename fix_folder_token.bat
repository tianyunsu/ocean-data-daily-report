@echo off
REM 修复 Folder Token 问题（批处理版本）

echo =====================================================
echo           修复 Folder Token 问题
echo =====================================================
echo.
echo 错误信息：folder not found
echo 原因：Folder Token 不正确或文件夹不存在
echo.
echo 请选择解决方案：
echo.
echo   [1] 不设置 Folder Token（推荐）
echo       文档将保存到应用根目录
echo.
echo   [2] 重新输入正确的 Folder Token
echo       需要提供正确的文件夹 Token
echo.

set /p CHOICE="请输入选项 (1 或 2): "

if "%CHOICE%"=="1" goto NO_TOKEN
if "%CHOICE%"=="2" goto NEW_TOKEN

echo.
echo [错误] 无效的选项
pause
exit /b 1

:NO_TOKEN
echo.
set FEISHU_FOLDER_TOKEN=
echo [成功] Folder Token 已清除
echo       文档将保存到应用根目录
echo.
echo 现在请重新运行测试：test_feishu_doc.bat
echo.
goto END

:NEW_TOKEN
echo.
echo 如何获取正确的 Folder Token：
echo   1. 在浏览器中打开飞书云文档
echo   2. 进入您想保存文档的文件夹
echo   3. 复制浏览器地址栏中的 Token
echo      URL格式：https://xxx.feishu.cn/drive/folder/boxcxxxxxxxxxxxxxxxxx
echo      Token 是 box 后面的部分
echo.
set /p NEW_TOKEN="请输入正确的 Folder Token: "

if not "%NEW_TOKEN%"=="" (
    set FEISHU_FOLDER_TOKEN=%NEW_TOKEN%
    echo.
    echo [成功] Folder Token 已更新：%FEISHU_FOLDER_TOKEN%
    echo.
    echo 现在请重新运行测试：test_feishu_doc.bat
) else (
    echo.
    echo [警告] 未输入 Token，Folder Token 保持不变
)
echo.
goto END

:END
echo.
echo 当前配置：
echo   App ID: %FEISHU_APP_ID%
echo   App Secret: %FEISHU_APP_SECRET:~0,10%...
if "%FEISHU_FOLDER_TOKEN%"=="" (
    echo   Folder Token: (未设置，文档将保存到应用根目录)
) else (
    echo   Folder Token: %FEISHU_FOLDER_TOKEN%
)
echo.
pause
