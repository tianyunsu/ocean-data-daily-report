# 海洋AI研究日报系统记忆

> **本文件每次执行都会注入上下文，只保留「每日必需 + 决策判据」。**
> 历史台账、事故取证、滚出 3 期窗口的去重标识符、勿再收名单、待拍板事项 → **`.workbuddy/memory/ARCHIVE.md`**（检索才读）。
> **压缩纪律**：注入被截断即触发归档；已完成 11-04 / 11-05 / 11-06 / 11-09 / 11-11（第五次）/ **11-11（第六次，因注入截断）** 六次压缩，明细只搬不改迁 ARCHIVE，信息零丢失。

## 系统配置
- **用户** 苏老师 · **自动化ID** `ai`（`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）· **2026-10-18 起 PAUSED**，任务定义留云端，手动触发；改回 ACTIVE 即恢复
- **仓库** https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点** https://tianyunsu.github.io/ocean-data-daily-report/
- **数据流**：`build_daily_YYYYMMDD.py` 用 repr 正则把 `SECTIONS` 注入 `feishu_write_doc.py` → `gen_html_YYYYMMDD.py` 用 `ast.literal_eval` 读回出 HTML（**改内容只改 build_daily，必须重跑 build_daily 再跑 gen_html**）→ `posts/YYYY-MM-DD.html` + `index.html` + `archive.html` → push → 飞书/机器人
- **Python** `py -3`（全流程）；链接实测用系统 `Python313\python.exe`
- **OpenAlex key** 本地 `_openalex_key.txt`（gitignore）；读取序「环境变量 `OPENALEX_API_KEY` > 本地文件」，有 key 走 cursor 翻页，无 key 回退 `page=`
- **飞书凭证** 唯一入口 `_feishu_auth.get_app_credentials()`（环境变量 > `_feishu_credentials.env`，gitignore）

## 四层架构（2026-09-20）
- **L0** `harvest.py` → `data/pool/YYYY-MM-DD.jsonl`；**L1** `screen.py`+`tier_engine.py` → `data/library.db` + `data/pool_index.json`；**L2** 日报；**L3** `gen_frontier.py` → `frontier.html` + `weekly_report.py` → `weekly/YYYY-Www.html`
- 池文件入库（`.gitignore` 只忽略 `_*.jsonl`），`library.db` 不入库；周报触发＝周日或距上期 ≥7 天，`--end` 取运行当日
- **L1 打分**＝期刊权重（S6/A5/B4/C3/P2.5/D1）×100 + 相关度×8 + 时效 + 海洋契合度
  - **对象 vs 介质**：`ocean/marine/coastal/bathymetry/seabed/fisheries/Arctic…`＝研究海洋；`seawater/water/wave/polar/tide + catalyst/battery/clinical/crop/hydrogel…`＝用海非研究海 → 判 `off` 降权 −150

## 期刊分级
- **S** Nature/Science/PNAS 正刊及顶级子刊；**A** AGU/Copernicus/IEEE/Elsevier 顶刊、Sci Rep、Ocean Engineering；**B** 主流 SCI / 中文前25%；**C** Frontiers/PLOS/Heliyon 集团刊；**D** MDPI/Hindawi/预警剔除刊 → **强制置底 + 标题标注原因（名单/集团 + 年份）**
- **P 预印本**：已对应期刊则按期刊等级排序并保留「预印本」标注；匹配序 同 DOI → 归一化标题 → `journal_ref` → OpenAlex locations
- **判定顺序**：预印本升级 → 登记表 → 最新预警/剔除名单（只用最新一期，`active` 控制）→ 集团规则 → 指标自动评级 → 待确认
- **阈值** A h≥120 或 h≥70&c≥3；B h≥50 或 h≥30&c≥2 或 c≥4；C h≥8 或 c≥0.5
- **已录名单** 中科院2025(5)、中信所2025(14)、EI剔除2026(19/228)、WoS剔除2026(16)
- **铁律** 零覆盖来源组 ≤6；arXiv 占比 ≤50%；**期刊占比 ≥40%**；综述链接必须回查 `library.db.url`

## 执行流程与一致性
`阶段0 git pull+sync_skills.py install` → `阶段1 顶会/IEEE（≥5 条初筛）` → `阶段2 harvest+screen+来源矩阵` → `阶段3 build_daily+gen_html` → `阶段4 发布+飞书/机器人+周报/看板` → `阶段5 五审` → `阶段6 记忆写入`
- `ocean-daily-report` skill 是**唯一权威源**，prompt 纯委托；流程调整先改 skill
- 每期产出：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 滚动本文件 + 双路径追加 `automations/ai/memory.md`
- 规模：每方向 3–5 条、合计 27–45；某方向确无新内容可为 0，**宁缺不凑数**；≤14 天，近 7 天优先；禁同日并行执行

## 内容质量规则（完整版见 SKILL）
1. 时效 ≤14 天；14–60 天须豁免说明；>60 天删除（arXiv 以 v1 提交日为准）
2. 每条 URL 实测可访问（403/000 用 `verify_paper.py` 复核）；工具版本须官方 release notes 核实；**摘要自原文提取，不据标题推断**
3. 跨期去重三路（URL 集合差 + 中文片段 + DOI/卷期）；同 URL 只在一个方向；主页新闻须给具体链接
4. 来源矩阵逐组打卡（零覆盖 >6 组须补检）；阶段一采纳条目须在阶段三构建时即纳入，非事后补丁

## 常见故障（完整表见 ARCHIVE 8.1）
| 问题 | 解决方案 |
|------|---------|
| Windows push 沙箱拦 `~/.ssh` | Bash + `dangerouslyDisableSandbox: true` |
| rebase 因未提交改动失败 | `screen.py` 会改 `journal_tiers.json`/`pending_journals.txt` → **先 commit → 再 rebase → 再 push** |
| 403（MDPI/ScienceDirect/Wiley/AGU/T&F） | 反爬≠死链，`verify_paper.py` 核实 |
| 飞书 API 404 | 根因是端点写错非 token：`POST .../documents/{doc}/blocks/{doc}/children`（body `children`）；样式须放 `text_run.text_element_style`（SKILL 陷阱 31） |
| `index/archive` 出现 Python 源码明文 | publish 正则跨节捕获 → 一律 **AST 抽条目 + 跳过无 url/`[备注]` 项**，替换前断言区间含 `'badge':`（模板 `repair_publish_1105.py`） |
| `verify_paper.py` 判 IEEE「超期 3xx 天」 | 日期塌缩伪告警；首发日以 `stage1_ieee_crossref.py` 的 Crossref `created` 为准 |

## 去重基准
> `posts/` 是**全量存档**，去重脚本必扫全量；本节只留当期指针。最近 3 期＝**11-11（本期）/ 11-09 / 11-06**；11-06 及更早、11-09 的完整清单与高风险标识符已迁入 `ARCHIVE.md` 第一节 / 8.2；勿再收完整名单见第二节。

- **每期阶段六**：把本期全量标识符写入当日日志，并把「最易被再次命中」的高风险标识符压成本节一行；滚出 3 期窗口即迁入 ARCHIVE。
- **标注语义**：新增勿再收条目必须写明属「质量弃用」还是「xx 期已发」，二者不可混。

## 漏检核查（完整取证 ARCHIVE 第四节）
- **根因 1 · IEEE 日期塌缩（系统性）**：TGRS 等刊 OpenAlex `publication_date` 恒为当年 1-1 → 按日期窗拉 IEEE 期刊恒返 0。修复 `stage1_ieee_crossref.py --start/--end`（Crossref `from-created-date`）→ `_stage1_ieee.json`，**阶段一 IEEE 组必须跑**。
- **根因 2 · 链接形式不一致**：同一成果可能用 DOI / 出版商直链 / 机构新闻稿 → 只做 URL 集合差会假阴性；去重前须 DOI 归一化，新条目**优先 `https://doi.org/...`**。
- **纪律**：核查「是否收录」须同时 grep DOI 尾段数字、期刊简称+卷+页、英文标题词、中文标题词；处置结论落成「已收录 / 时间窗正当排除 / 系统未运行 / 真实漏检 + 根因」四类之一。

## 每日铁律速查（取证原文 ARCHIVE 第七节 / 8.4）
1. **五审独立复算去重**，阶段二口头「已去重」不可信；「新闻稿/中文标题 ↔ DOI」两个标识符都查。
2. **期刊占比 ≥40% 在阶段三 `build_daily` 出数时立即核算**，不达标就地补检，别等五审。
3. **方向三/四/六/八是结构性期刊荒漠** → 阶段二用 OpenAlex `title_and_abstract.search` 定向补检。
4. **双源无摘要即弃用**（OpenAlex `abstract_inverted_index` 与 Crossref `abstract` 皆空），绝不据标题推断。
5. **阶段一 IEEE 组必须跑 Crossref created 通道**；IEEE 首发日以 `created` 为准。
6. **publish 一律 AST，禁用正则**；改内容必重跑 build_daily → gen_html；改数据源后 `git checkout <首发commit>^ -- index.html archive.html` 再 publish。
7. **Zenodo 概念 DOI 须 WebFetch 查 Tombstone**；概念 DOI 尾号常与版本 DOI 差 1，按尾段数字 grep。
8. **飞书回读校验** `code=0` / 块数 / 链接数 / 新条目已写入 / 旧重复已移除；HTTP 200 ≠ 业务成功。
9. **OpenAlex 滤镜**：`primary_location.source.issn:`（非 `issn:`）、真实空格（非 `%20`）、`conference-paper`（非 `proceedings-article`）、阳性对照 + 核对 `meta.count`；`host_organization` 不可靠；索引滞后 T+2/T+3；池 jsonl DOI URL 小写存储。
10. **事件日 ≠ 报道日**；**宁缺不凑数**；**中文条目去重必须用中文片段 grep**；工具版本查官方 release notes；GitHub Pages 重建约 100 s，复核加 `?v=n`。
11. **补录板块**：漏检有价值时末尾单列「十、补录」（`count_as_direction=False`），`badge='[备注]'` 不计 effective，`date` 填首发日并写明原因；footer 来源按 `sections` 动态生成。
12. **公开仓库禁硬编码凭证**（统一 `_feishu_auth`，五审含该项）；远程文档写入须幂等复用 + 回读；用户指定条目与去重冲突时先核实历史收录并交苏老师拍板。

## 归档索引
| 需要什么 | 去哪里 |
|---|---|
| 各期全量去重标识符、勿再收名单、已发不重发标注 | `ARCHIVE.md` 第一、二节 |
| 已结案事故取证（凭证 / 文档堆积 / 截断 / 11-09 重复闭环 / 11-05 高风险） | 第三节 3.1–3.8 |
| Crossref IEEE 通道实测、日期字段取证、抽查结论、DOI 归一化细则 | 第四节 4.1–4.4 |
| 待拍板事项 / 维护约定 | 第五、六节 |
| 经验判据取证数字、第六次压缩迁入的原文（故障表、去重基准、经验教训） | 第七节 / **第八节 8.1–8.4** |
