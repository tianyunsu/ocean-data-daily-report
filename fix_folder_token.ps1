# 修复 Folder Token 问题
# 提供两种解决方案

Write-Host "=== 修复 Folder Token 问题 ===" -ForegroundColor Yellow
Write-Host ""

Write-Host "错误信息：folder not found" -ForegroundColor Red
Write-Host "原因：Folder Token 不正确或文件夹不存在" -ForegroundColor Red
Write-Host ""

Write-Host "请选择解决方案：" -ForegroundColor Cyan
Write-Host ""
Write-Host "  [1] 不设置 Folder Token（推荐）" -ForegroundColor Green
Write-Host "      文档将保存到应用根目录" -ForegroundColor Gray
Write-Host ""
Write-Host "  [2] 重新输入正确的 Folder Token" -ForegroundColor Yellow
Write-Host "      需要提供正确的文件夹 Token" -ForegroundColor Gray
Write-Host ""

$choice = Read-Host "请输入选项 (1 或 2)"

if ($choice -eq "1") {
    # 方案1：不设置 Folder Token
    $env:FEISHU_FOLDER_TOKEN = ""
    Write-Host ""
    Write-Host "✅ Folder Token 已清除" -ForegroundColor Green
    Write-Host "文档将保存到应用根目录" -ForegroundColor Green
    Write-Host ""
    Write-Host "现在请重新运行测试：node test_feishu_doc.js" -ForegroundColor Cyan
}
elseif ($choice -eq "2") {
    # 方案2：重新输入 Folder Token
    Write-Host ""
    Write-Host "如何获取正确的 Folder Token：" -ForegroundColor Cyan
    Write-Host "1. 在浏览器中打开飞书云文档" -ForegroundColor White
    Write-Host "2. 进入您想保存文档的文件夹" -ForegroundColor White
    Write-Host "3. 复制浏览器地址栏中的 Token" -ForegroundColor White
    Write-Host "   URL格式：https://xxx.feishu.cn/drive/folder/boxcxxxxxxxxxxxxxxxxx" -ForegroundColor Gray
    Write-Host "   Token 是 box 后面的部分" -ForegroundColor Gray
    Write-Host ""
    
    $newToken = Read-Host "请输入正确的 Folder Token"
    
    if ($newToken -ne "") {
        $env:FEISHU_FOLDER_TOKEN = $newToken
        Write-Host ""
        Write-Host "✅ Folder Token 已更新：$newToken" -ForegroundColor Green
        Write-Host ""
        Write-Host "现在请重新运行测试：node test_feishu_doc.js" -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "⚠️ 未输入 Token，Folder Token 保持不变" -ForegroundColor Yellow
    }
}
else {
    Write-Host ""
    Write-Host "❌ 无效的选项" -ForegroundColor Red
}

Write-Host ""
Write-Host "当前配置：" -ForegroundColor Cyan
Write-Host "  App ID: $env:FEISHU_APP_ID" -ForegroundColor White
Write-Host "  App Secret: $($env:FEISHU_APP_SECRET.Substring(0,10))..." -ForegroundColor White
if ($env:FEISHU_FOLDER_TOKEN -eq "") {
    Write-Host "  Folder Token: (未设置，文档将保存到应用根目录)" -ForegroundColor Gray
} else {
    Write-Host "  Folder Token: $env:FEISHU_FOLDER_TOKEN" -ForegroundColor White
}
Write-Host ""
