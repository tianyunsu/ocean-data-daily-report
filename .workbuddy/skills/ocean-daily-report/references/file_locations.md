# 海洋AI研究日报 — 文件位置（角色定义）

不写死绝对路径。首次使用时，在 workspace MEMORY.md 中建立角色→路径映射。

## 角色定义

| 角色 | 说明 | 示例（Administrator 环境） |
|------|------|--------------------------|
| `$DATA_SOURCE` | 日报数据源文件，含 `SECTIONS = [...]` 定义（第18行附近） | `C:\...\WorkBuddy\Claw\feishu_write_doc.py` |
| `$WORKSPACE` | 当前 WorkBuddy 工作区根目录 | `C:\...\WorkBuddy\2026-06-18-09-27-39` |
| `$BUILD_SCRIPT` | 写入 sections 数据的 Python 脚本 | `$WORKSPACE/build_daily.py` |
| `$GEN_HTML` | 生成 HTML 简报的 Python 脚本 | `$WORKSPACE/gen_html.py` |
| `$HTML_OUT` | HTML 输出目录 | `$WORKSPACE/../daily_reports/` |
| `$GH_REPO` | GitHub Pages 仓库根目录 | `$WORKSPACE/../ocean-data-daily-report/` |
| `$RUN_DAILY_REPORT` | 飞书机器人通知脚本 | `C:\...\WorkBuddy\Claw\run_daily_report.py` |
| `$PYTHON` | Python 可执行文件路径 | `~\.workbuddy\binaries\python\versions\x.x.xx\python.exe` |

> `$DATA_SOURCE` 同时承担两个职责：① 存放 `SECTIONS` 数据；② 执行它即把简报**推送到飞书文档**（阶段四第 5 步）。
> 旧脚本 `deploy_report.py` 已废弃（发布改由 `git push` 直接完成）。

## 9大方向定义

1. 海洋人工智能（Ocean AI / Marine Artificial Intelligence）
2. 海洋数字孪生（Ocean Digital Twin / Marine Digital Twin）
3. 海洋可视化（Ocean Visualization / Geospatial Display）
4. 海洋数据质量（Ocean Data Quality Control / QA/QC）
5. 海洋数据处理（Ocean Data Processing / Computing）
6. 海洋数据管理与共享（Ocean Data Management & Sharing，**含地质样品共享、数据共享平台**）
7. 开放航次与科考（Open Cruises / Research Expeditions，**含船时共享 Ship Time Sharing**）
8. 海洋数据中心（Ocean Data Centers / Infrastructure）
9. 工具与代码资源（Tools & Code Resources）

> 每方向目标 **3-5 条**，全日报 **27-45 条**。各方向的"可收录/禁止归入"判定见
> `quality_standards.md` 的「方向归类严格规则」。

## 数据流（角色版）

```
搜集内容 → 来源覆盖矩阵逐组打卡（阶段二）
         → 归类自检（阶段三，写入前）
         → $BUILD_SCRIPT（写入sections数据）
         → $PYTHON $BUILD_SCRIPT（正则替换 $DATA_SOURCE 中第18行 SECTIONS）
         → $PYTHON $GEN_HTML（读取 $DATA_SOURCE → 生成HTML到 $HTML_OUT）
         → 复制到 $GH_REPO/posts/
         → 更新 $GH_REPO/index.html + $GH_REPO/archive.html
         → git pull --rebase → git commit → git push
         → $PYTHON $DATA_SOURCE（推送飞书文档）
         → $PYTHON $RUN_DAILY_REPORT（飞书机器人通知，未配置 webhook 则跳过）
         → 五项质量审查（链接+一致性 / 时效 / 来源覆盖 / 归类与条数 / 去重）
         → 阶段六记忆写入
```

## 新用户接入步骤

1. 在工作区找到或创建 `feishu_write_doc.py`（只须含 `SECTIONS = [...]` 占位）
2. 在工作区创建 `build_daily.py` 和 `gen_html.py`（参考技能仓库中的脚本模板）
3. 在工作区 workspace MEMORY.md 中记录角色映射
4. 确认 GitHub Pages 仓库路径，记录在 MEMORY.md 中
