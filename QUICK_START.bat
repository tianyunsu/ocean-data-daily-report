@echo off
REM 飞书日报助手 - 一键启动配置工具

echo =====================================================
echo         飞书日报助手 - 快速配置向导
echo =====================================================
echo.
echo 此工具将帮助您完成飞书云文档的配置。
echo.
echo 配置步骤：
echo   1. 修复 PowerShell 执行策略（需要管理员权限）
echo   2. 配置环境变量
echo   3. 测试飞书文档创建
echo.
echo =====================================================
echo.

:MENU
echo 请选择操作：
echo.
echo   [1] 修复 PowerShell 执行策略（需要管理员）
echo   [2] 配置环境变量
echo   [3] 测试飞书文档创建
echo   [4] 查看配置指南
echo   [5] 查看故障排查
echo   [0] 退出
echo.
set /p CHOICE="请输入选项 (0-5): "

if "%CHOICE%"=="1" goto FIX_POLICY
if "%CHOICE%"=="2" goto SET_ENV
if "%CHOICE%"=="3" goto TEST_DOC
if "%CHOICE%"=="4" goto SHOW_GUIDE
if "%CHOICE%"=="5" goto SHOW_TROUBLESHOOT
if "%CHOICE%"=="0" goto END

echo [错误] 无效的选项，请重新选择。
echo.
goto MENU

:FIX_POLICY
echo.
echo =====================================================
echo           修复 PowerShell 执行策略
echo =====================================================
echo.
echo 此操作需要管理员权限。
echo 将会把执行策略设置为 RemoteSigned。
echo.
echo RemoteSigned 策略说明：
echo   - 允许运行本地创建的脚本
echo   - 需要远程脚本的数字签名
echo   - 这是推荐的安全策略
echo.
pause
call fix_execution_policy.bat
goto MENU

:SET_ENV
echo.
echo =====================================================
echo             配置环境变量
echo =====================================================
echo.
echo 您需要准备：
echo   1. 飞书应用的 App ID
echo   2. 飞书应用的 App Secret
echo   3. (可选) 目标文件夹的 Token
echo.
echo 如果还没有创建飞书应用，请先访问：
echo   https://open.feishu.cn/
echo.
pause
call set_feishu_env.bat
goto MENU

:TEST_DOC
echo.
echo =====================================================
echo           测试飞书文档创建
echo =====================================================
echo.
echo 此步骤将：
echo   1. 检查环境变量是否正确
echo   2. 使用您的凭证连接飞书API
echo   3. 创建一个测试文档
echo   4. 在文档中添加测试内容
echo.
echo 如果测试成功，您的配置就完成了！
echo.
pause
call test_feishu_doc.bat
goto MENU

:SHOW_GUIDE
echo.
echo =====================================================
echo               查看配置指南
echo =====================================================
echo.
echo 配置指南已保存在文件：FEISHU_SETUP_GUIDE.md
echo.
echo 主要内容包括：
echo   1. 创建飞书自建应用
echo   2. 获取应用凭证
echo   3. 开通必要权限
echo   4. 设置环境变量
echo   5. 测试文档创建
echo   6. 故障排查
echo.
start notepad FEISHU_SETUP_GUIDE.md
goto MENU

:SHOW_TROUBLESHOOT
echo.
echo =====================================================
echo               故障排查指南
echo =====================================================
echo.
echo 常见问题：
echo.
echo 1. PowerShell 执行策略限制
echo    解决方案：运行 fix_execution_policy.bat
echo.
echo 2. 环境变量未设置
echo    解决方案：运行 set_feishu_env.bat
echo.
echo 3. App ID 或 Secret 错误
echo    解决方案：检查飞书开放平台应用凭证
echo.
echo 4. 权限不足
echo    解决方案：在飞书应用管理中开通权限
echo.
echo 5. Node.js 未安装
echo    解决方案：访问 https://nodejs.org/ 安装
echo.
echo 6. 网络连接问题
echo    解决方案：检查网络，确保能访问 open.feishu.cn
echo.
echo 详细故障排查请查看 FEISHU_SETUP_GUIDE.md
echo.
pause
goto MENU

:END
echo.
echo =====================================================
echo              感谢使用飞书日报助手！
echo =====================================================
echo.
echo 配置完成后，日报自动化任务将自动创建飞书文档。
echo.
echo 如需帮助，请查看 FEISHU_SETUP_GUIDE.md
echo.
pause
