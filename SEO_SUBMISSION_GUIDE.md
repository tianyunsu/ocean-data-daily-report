# 搜索引擎收录提交指南

本文档指导如何将海洋AI技术日报网站提交到各大搜索引擎，以便被搜索到。

## 已完成的 SEO 配置

| 文件 | 说明 | 状态 |
|------|------|------|
| `sitemap.xml` | 站点地图，列出所有页面 | ✅ 已创建 |
| `robots.txt` | 爬虫规则文件 | ✅ 已创建 |
| `index.html` | 添加了 meta/OG 标签 | ✅ 已修改 |
| `archive.html` | 添加了 meta/OG 标签 | ✅ 已修改 |
| `deploy_report.py` | 自动更新 sitemap.xml | ✅ 已集成 |

## 下一步：向搜索引擎提交

### 1. Google Search Console（最重要）

1. 访问 [Google Search Console](https://search.google.com/search-console)
2. 点击「添加资源」→ 选择「网址前缀」
3. 输入：`https://tianyunsu.github.io/ocean-data-daily-report/`
4. 选择验证方式（推荐 HTML 文件验证）：
   - 下载验证文件 `google123456789.html`
   - 将其放入仓库根目录
   - 提交验证
5. 验证通过后：
   - 进入「站点地图」
   - 在「添改站点地图」输入：`sitemap.xml`
   - 点击提交

### 2. Bing Webmaster Tools

1. 访问 [Bing Webmaster Tools](https://webmaster.bing.com)
2. 点击「添加网站」
3. 输入网站 URL
4. 验证网站（方法同上）
5. 提交站点地图

### 3. 百度站长平台

1. 访问 [百度搜索资源平台](https://ziyuan.baidu.com)
2. 登录百度账号
3. 点击「用户中心」→「站点管理」→「添加网站」
4. 输入网站 URL
5. 验证网站
6. 提交站点地图

**注意**：百度对 GitHub Pages 收录较慢，建议配置自定义域名后提交。

## 验证收录状态

在搜索引擎中输入以下命令验证：

```
site:tianyunsu.github.io/ocean-data-daily-report
```

### 预期结果
- **Google**：通常 1-7 天内收录
- **Bing**：通常 3-14 天内收录
- **百度**：可能需要 2-4 周，GitHub Pages 收录不稳定

## 后续维护

### 自动更新
- `deploy_report.py` 已在发布流程中自动更新 `sitemap.xml`
- 每次生成新日报并推送时，sitemap 会同步更新

### 手动更新 sitemap
如需手动更新 sitemap，运行：
```bash
cd /c/Users/Administrator/WorkBuddy/Claw
python update_sitemap.py
```

## 常见问题

### Q: 网站已经在运行了，还需要做什么？
A: 只需完成上面的「向搜索引擎提交」步骤即可。

### Q: 百度收录慢怎么办？
A: 可以考虑为网站配置自定义域名，GitHub Pages 配合自定义域名更易被百度收录。

### Q: 如何查看爬虫抓取情况？
A: 在 Google Search Console 中查看「抓取统计信息」和「索引覆盖范围」报告。
