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

## 2026-11-05 期 · 自动化执行（周四）
- **触发**：苏老师手动触发自动化 `ai`（rrule 仍 PAUSED，任务定义留云端）。
- **条数**：**32 条 / 9 方向**（一5/二3/三3/四3/五5/六3/七4/八3/九3），**期刊 14 条 = 43.8%**（≥40% 在阶段三定稿即核算），学术类 59.4%，D 级 0 条。
- **阶段一**（本期首次完整验证 11-04 新增修复）：`stage1_ieee_crossref.py` 窗口 10-22~11-05 → total 414 / ocean_hits 33；8 条 IEEE 论文全部来自该通道（VesselBench、QuaSAR、SWOT 15 弧秒、CAT 3D、SonarT165、AUV 洋流抑制、PPAP、GLHR）。会议通道采纳 CIKM 2026 两条（EarthOracle、AquaNord-SE）。
- **阶段二**：harvest 7,437 条 → 池内 254 条（`{'?':107,'A':42,'B':50,'C':23,'D':17,'P':12,'S':3}`）；方向三/四/六/八仍为期刊荒漠，阶段二即用 WebSearch 补中文机构动态与工具版本。
- **弃用**：`oceaneng.2026.129259`、`isprsjprs.2026.10.039/.038`、`TGRS.2026.3749930` —— OpenAlex + Crossref 双源无摘要。
- **发布**：commit `8082592`；Pages 三页 200、posts 条目数 32；飞书新建 `ARz7dXPgNoulsyx2yykcgEONnqX`（157 块 / 6 批，回读 158 块，同日同名文档 1 个）；webhook `code:0`；邮件未配置。**周报不触发**（周四，距 W45 仅 3 天）。
- **事故修复**：11-04 的 publish 用正则抽条目，遇无 url 的 `[备注]` 条目跨节捕获，把 build 脚本源码明文写进 `index.html`/`archive.html`（线上乱码）。本期以 `repair_publish_1105.py`（AST + 行区间断言）重写 11-04 卡片与归档条目并插入 11-05，线上污染计数归零。
- **新经验**：①publish 一律 AST，禁用正则；②IEEE Crossref created 通道已在真实窗口验证有效；③无摘要弃用清单已成型，Elsevier/IEEE 双源缺摘要比例仍高；④MEMORY.md 二次压缩 16,444→16,206 B，11-04 清单与漏检明细迁 ARCHIVE。

## 2026-11-06 期 · 自动化执行（周五）
- **触发**：苏老师手动触发自动化 `ai`（rrule 仍 PAUSED，任务定义留云端）；起点 `1315086`，pull 已最新，sync_skills 同步 9 文件。
- **条数**：**36 条 / 9 方向**（一5/二3/三4/四5/五5/六4/七4/八3/九3），**期刊 15 条 = 41.7%**（阶段三定稿即核算达标）、arXiv 11.1%、会议/顶会 5 条、D 级 0 条；时效 10-23~11-05 全部 ≤14 天（≤7 天 25 条）。
- **阶段一**：IEEE Crossref created 通道 total 414 / ocean_hits 33；采纳 JOE×2 + TGRS×2。顶会采纳 NeurIPS 2026 四篇（Nereus / PhysFTM / GNN-VIEW / BGC 零样本校正）+ ADIPEC 2026 一篇。
- **阶段二**：harvest 7,785 条 → 池内 259 条（`?107/A42/B49/C28/D16/P14/S3`）；结构性期刊荒漠延续，阶段二即用 OpenAlex 八组定向补检，补入 15 篇有摘要期刊论文。
- **新发现**：Zenodo 概念 DOI `10.5281/zenodo.23930484`（EOSC Marine D1.1 Handbook）实际跳转到作者撤回的 Tombstone → 已剔除；今后 Zenodo 条目须 WebFetch 复核落地页状态。另弃用 4 例 IEEE 双源无摘要论文。
- **发布**：commit `e7c10bb` + `ed0e832`；Pages 三页 200、posts 条目数 36、源码污染计数 0；飞书新建 `Bnhfd1YYHoIRtqxLLazcjhK3n0g`（173 块 / 6 批，回读 174 块 / 18,050 字符，36 条标题全命中，同日同名 1 个）；webhook code=0；邮件未配置。**周报不触发**（周五，距 W45 仅 4 天）。
- **五审**：链接 12 条非 200 全为 IEEE/T&F/AGU/CSIRO/OnePetro 反爬（已用 `verify_paper.py` 回查元数据），死链 0；URL/DOI 与中文标题片段跨期 0 重复；来源矩阵打卡模板 10 行全 Y、零覆盖 0 组，细分未采纳出版商组均已给出关键词与归因。
- **记忆**：新建 `.workbuddy/memory/2026-11-06.md`；MEMORY.md 第三次压缩 16,332→15,910 B（11-05 清单与漏检明细迁 ARCHIVE）并滚动 11-06 基准；ARCHIVE 第一节新增 11-06 全量 36 项；新增「Zenodo Tombstone」「双源无摘要」两条经验。
- **遗留**：邮件凭证未配置；跨期三项待拍板（D 级加严 / 周报期号 / 自动化 `ai` 状态）未变。

---

## 2026-11-11（周三）· 自动化执行
- **阶段零**：承接 11-09 收尾（ARCHIVE 补 11-09 全量 36 项 + 3.7/3.8 + 第七节；MEMORY 第五次压缩 18,192→16,154 B；commit 30428ec）；sync_skills 9 文件一致；pull --rebase + push 后 HEAD==ORIGIN==30428ec。**因注入截断执行第六次压缩**：MEMORY 16,154→9,727 B，原文迁 ARCHIVE 第八节 8.1–8.4。教训：注入预算按字符/token 计而非字节。
- **阶段一**：IEEE Crossref created 通道 ocean_hits 21（4 条 11-09 已发、9 条新增双源无摘要弃用）；OpenAlex 会议通道 236 候选 / 180 去重；MARINER 会议版判为 04-15 已发剔除；oceanpy 2.0.8 名称误导弃用。合格初筛 ≥5 条全部在阶段三构建时纳入。
- **阶段二**：harvest 8,501 行 → screen 池内 248 条（?92/A37/B53/C26/D17/P19/S4）；OpenAlex 八组定向补检 93 条；PyPI JSON + GitHub releases + 机构新闻页替代连续 fetch failed 的 WebSearch；4 条真重复剔除（zenodo.23777351 / s40623-026-02566-w / lom3.70102 / 2118.235285-ms，均 11-04 或 11-06 期已发）；5 条 Zenodo 概念 DOI 全部 WebFetch 复核 live、非 Tombstone，尾号 +1 规则 5/5 命中。
- **阶段三/四**：40 条 9 方向（一5 二5 三3 四5 五5 六5 七5 八3 九4），期刊/会议论文 22 条 55.0%，arXiv 3 条 7.5%；build_daily_1111.py → gen_html_1111.py（动态日期 + 周三）→ publish_1111.py（AST 抽条目 + 期刊占比断言）；commit f70b714，HEAD==ORIGIN，工作区干净；飞书 AcPWdWPHXonv9NxXVovcWZQmnOc 189 块且按标题幂等复用（清空旧 189 块后重写），webhook code=0，邮件凭证未配置跳过；**周报不触发**（周三，距 W46 仅 2 天）。
- **五审**：URL 实测 200×20 / 202×2 / 403×11 / 000×7，死链 0（403 为反爬、000 为代理波动，均经 WebFetch 或 OpenAlex+Crossref 复核）；时效 10-29~11-10 全在 14 天窗口；来源矩阵 16 组逐组打卡、零覆盖 0 组；归类与条数达标；三路去重 0 重复。两处口径修正：中文片段只取纯中文连续段、HTTP 状态码 int/str 归一。
- **记忆**：新建 .workbuddy/memory/2026-11-11.md（含 40 项全量标识符与弃用台账）；MEMORY.md 滚动 11-11 基准并补 4 条活跃判据；ARCHIVE.md 第八节承接第六次压缩原文；本文件双路径追加。
- **新经验**：①双源无摘要弃用非永久黑名单（Crossref 会后补摘要，11-11 转收 JSTARS.3750434 / TGRS.3750154）②WebSearch 失效时四路直连替代通道 ③中文片段去重须用纯中文连续段 ④Zenodo 概念 DOI 尾号 +1 第三次复验 5/5 命中。
- **遗留**：邮件凭证未配置；跨期三项待拍板（D 级加严 / 周报期号 / 自动化 ai 状态）未变；11-09 期未见本文件追加记录。
