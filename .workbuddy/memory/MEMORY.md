# 海洋AI研究日报系统记忆（精简版）

## 系统配置

- **用户**：苏老师
- **自动化任务ID**：`ai`
- **CWD**：`C:/Users/Administrator/WorkBuddy/Claw`（正确）
- **Schedule**：`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`
- **GitHub**：https://github.com/tianyunsu/ocean-data-daily-report
- **网站**：https://tianyunsu.github.io/ocean-data-daily-report/

## 日报结构

9个方向：海洋AI、数字孪生、可视化、数据质量、数据处理、数据管理与共享、开放航次/船时共享、海洋数据中心、工具与代码资源

## 执行流程

```
步骤1 - 更新 feishu_write_doc.py SECTIONS 数据
步骤2 - 生成 HTML 简报 (daily_reports/海洋AI简报_YYYY-MM-DD.html)
步骤3 - 执行 feishu_write_doc.py（推送飞书文档）
步骤4 - 执行 run_daily_report.py（飞书机器人通知，需 $env:PYTHONUTF8=1）
步骤5 - 执行 deploy_report.py（发布到 GitHub Pages）
```

## 内容质量规则（必须遵守）

1. **近7天优先**，超1个月一律删除，1周~1个月仅保留高价值内容
2. **每条URL必须先fetch返回200**，404/403/超时一律不收录
3. **工具版本特性必须从官方release notes核实**，不得推断
4. **摘要必须从原文提取**，不得根据标题推断内容
5. **方向归类按文章内容判断**，不按来源机构功能判断
6. **跨方向去重**：同URL只能出现在一个方向中
7. **主页新闻必须找到具体链接**，不得使用机构主页URL
8. **各方向严格定义**（2026-05-13教训）：
   - "工具与代码资源"仅限：软件工具、代码库、开发框架、数据处理程序
   - 硬件装备（无人船、潜水器、传感器）→ 归"开放航次"或对应方向
   - 评估报告/状况报告 → 归"数据中心"或"可视化"，不归工具
   - **宁可某方向为空，也不凑数填入不相关内容**

## GitHub Pages 架构

- **main 分支**：源代码 + 每日日报（posts/、index.html、archive.html）
- **supplement 分支**：另一台机器检索结果（不需要本地拉取）
- **gh-pages 分支**：由Actions自动部署（不要手动编辑）
- 每次生成日报后必须同时更新 index.html 和 archive.html

## SECTIONS 数据替换方法（可靠）

使用 `make_new_feishu_v2.py` 方法：
1. 找到原始文件中 `SECTIONS = [` 的精确位置
2. 用 bracket-counting（depth 计数）找到对应的结束 `]`
3. 用新的 SECTIONS 数据整体替换这一段
4. 验证：`compile(new_content, 'feishu_write_doc.py', 'exec')`

## 常见故障处理

| 问题 | 解决方案 |
|------|---------|
| git push TLS错误 | `git config --unset http.sslbackend` |
| git push代理拦截 | `git config --global --unset http.proxy && git push origin main` |
| git push HTTPS超时 | `git remote set-url origin git@github.com:tianyunsu/ocean-data-daily-report.git && git push origin main` |
| push后验证 | `Invoke-RestMethod https://api.github.com/repos/tianyunsu/ocean-data-daily-report/git/refs/heads/main` |
| run_daily_report.py编码错误 | `$env:PYTHONUTF8=1; python run_daily_report.py` |
| deploy_report.py卡住 | 手动：复制HTML到posts/ → 更新index/archive → git push |
| automation CWD错误 | SQL: `UPDATE automations SET cwds='["C:/Users/Administrator/WorkBuddy/Claw"]' WHERE id='ai'` |

## 去重基准（滚动更新）

- 2026-04-30：19条已发布（含GOFLOW、NOAAGlobalTemp v6.1、xarray v2026.04.0、GEBCO_2026、PANGAEA Event-Campaign Merge、IndOBIS等）
- 2026-05-06：24条（含Copernicus AI下一代业务化海洋产品、DestinE GMD论文、DSON-DT深海数字孪生、东北浮游生物数据集等）
- 2026-05-07：24条（含GOFLOW、NOAA首套深海eDNA数据集、OSR 9哥白尼海洋状况报告、Argo叶绿素再处理、Seabed 2030 28.7%等）
- 2026-05-08：18条（含EGU 2026 DestinE数字孪生展示、NOAA $21.6M无人系统合同、Thomas Jefferson五大湖测绘、WMO厄尔尼诺预测、三篇Nature Communications论文、IOCCG PACE再处理与HyperCP v1.2.15等）
- 2026-05-09：26条（与05-08部分重叠+新增，含OceanPile、GOFLOW、DestinE GMD、EGU OS4.8、NOAA无人系统、WMO厄尔尼诺、Nature Communications热带气旋预测、NOAA eDNA、Seabed 2030等）
- 2026-05-13：25条（初版22条分类修正后25条。含OCEANPILE浙大海洋语料库、陈大可院士AI海洋理论、GDAL 3.13.0、HyperCP v1.2.15、NCEI Data Tour Notebooks、"探索一号"全球深渊探索156天、"深蓝百万里"西太平洋航次、NCEI云迁移AWS、BGC-Argo+二次QC、NOAA无人水文测量/LR30采购、自主船舶数字孪生综述JMSA、OSR 9等）
