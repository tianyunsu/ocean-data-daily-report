# 自动化 ai 执行摘要（与 .workbuddy/automations/ai/memory.md 同步维护）

## 2026-11-02 期（周一·**W45 周报**）
- **日报**：32 条（一4/二3/三3/四3/五6/六3/七4/八3/九3），9 方向全有内容；commit `9816e24`（日报）+ `02571e9`（weekly 2026-W45 + frontier）。
- **周报判定**：距 W43（10-25）8 天 ≥7 → 触发；产出 2026-W45（窗口 10-20~11-02，池内 660 · S/A 124 · 综述样本 551）+ 深度综述（36 链接：29 条回查 library.db 命中、4 个唯一新闻链接池外全实测 200，0 臆造）。**ISO 期号跳号**：11-02 为 W45，W44 期号不存在（周日→周一触发所致），已在日志说明。
- **阶段零**：起点 `9b13c28`；pull 最新；sync_skills 一致。
- **规模指标**：harvest 7,264 行 → 池内 244（?78/A42/B38/C26/D15/P21/S4）→ 32 条，留存率 13.1%；arXiv 3.1%、期刊 84.4%、零覆盖组 1（顶会）。
- **阶段一**：会议通道 47 条海洋候选、RA-L 窗口 46 条（海洋 4 条），但**候选在 OpenAlex/Crossref/S2 三处均无摘要、ScienceDirect/ACM 反爬**，按「无摘要不收」纪律本期顶会/IEEE 组零覆盖并留痕（非检索失效）；IEEE 期刊 TGRS 日期塌缩问题延续。
- **去重**：URL/中文标题/DOI 三路跨期 0 命中。
- **五审**：①32 链接实测 9 异常（8×403 Wiley/MDPI/AGU/OUP + 1 ERR），全部 Crossref 复核为真 → 死链 0；②时效 ≤7天20/8-14天12/>14天0；③D 级 2 条（Buildings、Applied Sciences）置底+标注；④32 条落在 27–45 区间；⑤无新增硬编码凭证。
- **踩坑**：`publish_1102.py` 首次运行 WEEKDAY 与 excerpt 数据源仍是上期（前一次 patch 因 assert 提前退出未落盘）→ 回滚 index/archive 后重跑，终态「周一 / 32 条」。
- **飞书**：`ZRdbd6qXfoZHGcxdr77cmimZnEb`，157 块，同日复用；机器人 webhook code=0；邮件未配置跳过。
- **新经验**：①Elsevier/ACM/OUP 新刊摘要三源齐缺 → 从池 jsonl 的 abstract 字段筛候选，无摘要即不收；②周报 ISO 期号会因周日→周一跳号，建议改按「距上期天数」命名。
- **待苏老师确认**：自动化 `ai` 状态此前查询显示 ACTIVE（记忆为 10-18 设为 PAUSED），本次仍为手动/定时触发，未擅自变更。

## 2026-11-04 期（周三 · 无周报）
- **日报**：**40 条**（一5/二4/三5/四4/五5/六4/七4/八5/九4），9 方向全有内容；commit `9dfe95c`（34 条首版）→ **`dddc2e9`（40 条终版）**。
- **周报判定**：周三，距上期 W45（11-02）仅 2 天，不满足「周日或距上期 ≥7 天」→ **不触发**，已在日志留痕。
- **阶段零**：起点 `d4e14ff`；pull 最新；sync_skills 9 文件一致。
- **规模指标**：harvest 7,325 行 → 池内 244（?98/A41/B46/C26/D18/P12/S3）→ 40 条，留存率 16.4%；arXiv 7.5%、**期刊 40.0%（16/40）**、零覆盖组 6。
- **阶段一**：`type:conference-paper` 通道 473 条；RA-L 7 条（海洋 4）；JOE/TGRS/GRSL/JSTARS/GRSM/T-RO/TNNLS/TIP 窗口全 0（IEEE 日期塌缩延续）。采纳 ACM MM 2026 GreenToken + RA-L ISOPoT，**顶会与 IEEE 两组均非零覆盖**。
- **核心插曲**：首版 34 条期刊占比仅 **29.4%**（<40% 硬指标）→ 用 OpenAlex `title_and_abstract.search` 六组定向补检定向下补 6 篇期刊（Scientific Drilling GEODESC、JAWRA OSTDS、JTECH X 波段波向、BAMS NNJA、ESSD IBRA、L&O Methods 小波）→ 40 条、期刊占比 40.0% 达标，随即回滚 index/archive 重跑 publish。
- **去重**：URL 集合差 0、DOI 0、中文片段「小波」3 期命中均不同事件；主动剔除 `fmars.2026.1909271`（10-16 已发）与 `os-22-3403-2026`（GLODAPv3 已 3 期覆盖）。
- **五审**：①40 链接实测 12 非 200（ACM/IEEE/Wiley×3/AGU/MDPI/SEC/Zenodo×2/Seabed2030/CIOOS 反爬 + sciencenet 禁 HEAD），6 条新增 DOI 均取到完整摘要 → 死链 0；②时效 ≤7天18/8-14天22/>14天0；③零覆盖 6 组（Elsevier/T&F/SAGE/ACS-RSC/Science-AAAS/IOP）≤6 通过；④40 ∈ 27–45，各方向 3–5；⑤D 级 1 条（WindAnalysis，MDPI Computers）置底+标注。
- **飞书**：`KJFxdx1a6oZDFGx7fnjcLe1fnvh`，清空 165 块 → 写 189 块 / 7 批，回读 190 块一致；机器人 webhook code=0；邮件未配置跳过。
- **新经验**：①期刊占比须在阶段三定稿时核算，不能拖到五审；②方向三/四/六/八是结构性「期刊荒漠」，须在阶段二就用 OpenAlex 定向补检；③OpenAlex `host_organization` 滤镜不可靠（返 Springer/OUP），不能判定出版商零覆盖；④filter 值写 `%20` 会被二次编码导致恒返 0 且不报错，须用真实空格；⑤GitHub Pages 重建约 100 s，复核须等待并加 `?v=`。
- **待苏老师确认**：①D 级加严三选一（引用门槛 / 每日配额 ≤2 条 / Frontiers 并入标注）；②周报 ISO 期号跳号是否改「距上期天数」命名；③自动化 `ai` 状态查询为 ACTIVE 与 10-18 记忆 PAUSED 不一致。

## 2026-11-04 期 · 补录（10:43 苏老师拍板）
- **触发**：核查 4 篇抽查文章（1 已收录 / 1 早于上线 / 1 双源无摘要 / 1 真实漏检）后，苏老师回复「补录」。
- **做法**：日报末尾新增**「十、补录 · 往期漏检勘误」**板块，补录 2 篇 TGRS（KunPeng 首发 2026-06-30、GBM 洋面锋 2026-02-03），①③ 做成 `[备注]` 台账条目。不散进 9 方向——方向一/五已满 5 条，散入会破上限。
- **条数**：40 → **42**（另 1 条备注不计）；header「42 条 / 9 方向」，板块 10 个。
- **口径**：`count_as_direction=False` 使补录板块不计方向数；`[备注]` 不计 effective；补录 `date` 填首发日、正文写明漏检原因，五审时效 **>14 天 2 条**须单列说明而非判违规。
- **顺带修复**：gen_html footer「本期来源」原为 11-02 写死列表（派生到新期即失真）→ 改为按条目 `source` 动态去重生成。
- **发布**：commit `2096ca1`；线上 posts/index/archive 均 200、posts 页 64,507 字节；飞书 `KJFxdx1a6oZDFGx7fnjcLe1fnvh` 清 189 块 → 写 204 块 / 7 批；webhook code=0；邮件未配置。
- **验证**：死链 0（15 条非 200 全为反爬/沙箱波动，Sci Rep 与 ESSD 复测 GET 200、L&O Methods 403 属 Wiley 反爬）；URL/DOI 跨期 0 重叠；「GBM」往期 3 处命中均为 LightGBM。
