# 海洋AI研究日报系统记忆

> **本文件每次执行都会注入上下文，因此只保留「每日必需 + 决策判据」。**
> 历史台账、已结案事故的取证叙述、滚出 3 期窗口的去重标识符、勿再收完整名单、待拍板事项 → 见 **`.workbuddy/memory/ARCHIVE.md`**（检索才读，可持续增长）。
> **压缩纪律**：超 16 KB 触发归档；已完成 11-04 / 11-05 / 11-06 / 11-09 / **11-11** 五次压缩，明细只搬不改迁 ARCHIVE，信息零丢失。

## 系统配置
- **用户**：苏老师 · **自动化ID** `ai`（rrule `FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）· **2026-10-18 起 PAUSED**，任务定义留云端，由苏老师手动触发；改回 ACTIVE 即恢复
- **仓库** https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点** https://tianyunsu.github.io/ocean-data-daily-report/
- **数据流**：`build_daily_YYYYMMDD.py` 用 repr 正则把 `SECTIONS` 注入 `feishu_write_doc.py` → `gen_html_YYYYMMDD.py` 用 `ast.literal_eval` 读 `feishu_write_doc.py` 出 HTML（**改内容只改 build_daily，必须重跑 build_daily 再跑 gen_html**）→ `posts/YYYY-MM-DD.html` + `index.html` + `archive.html` → push → 飞书/机器人
- **Python**：`py -3`（全流程）；链接实测用系统 `Python313\python.exe`
- **OpenAlex key**：本地 `_openalex_key.txt`（gitignore）；读取序「环境变量 `OPENALEX_API_KEY` > 本地文件」，`harvest.py`/`verify_paper.py`/`source_metrics.py` 内置；有 key 走 cursor 翻页，无 key 回退 `page=`
- **飞书凭证**：唯一入口 `_feishu_auth.get_app_credentials()`（环境变量 > `_feishu_credentials.env`，gitignore）

## 四层架构（2026-09-20）
- **L0** `harvest.py` → `data/pool/YYYY-MM-DD.jsonl`；**L1** `screen.py`+`tier_engine.py` → `data/library.db` + `data/pool_index.json`；**L2** 日报；**L3** `gen_frontier.py` → `frontier.html` + `weekly_report.py` → `weekly/YYYY-Www.html`
- 池文件入库（`.gitignore` 只忽略 `_*.jsonl`），`library.db` 不入库；周报触发＝周日或距上期 ≥7 天，`--end` 取运行当日
- **L1 打分**＝期刊权重（S6/A5/B4/C3/P2.5/D1）×100 + 相关度×8 + 时效 + 海洋契合度
  - **对象 vs 介质**：`ocean/marine/coastal/bathymetry/seabed/fisheries/Arctic…`＝研究海洋；`seawater/water/wave/polar/tide + catalyst/battery/clinical/crop/hydrogel…`＝用海非研究海 → 判 `off` 降权 −150

## 期刊分级
- **S** Nature/Science/PNAS 正刊及顶级子刊；**A** AGU/Copernicus/IEEE/Elsevier 顶刊、Sci Rep、Ocean Engineering；**B** 主流 SCI / 中文前25%；**C** Frontiers/PLOS/Heliyon 集团刊；**D** MDPI/Hindawi/预警剔除刊 → **强制置底 + 标题标注原因（名单/集团 + 年份）**
- **P 预印本**：已对应期刊则按期刊等级排序并保留「预印本」标注；匹配序 同 DOI → 归一化标题 → `journal_ref` → OpenAlex locations
- **判定顺序**：预印本升级 → 登记表 → 最新预警/剔除名单（只用最新一期，`active` 控制）→ 集团规则 → 指标自动评级 → 待确认
- **阈值**：A h≥120 或 h≥70&c≥3；B h≥50 或 h≥30&c≥2 或 c≥4；C h≥8 或 c≥0.5
- **已录名单**：中科院2025(5)、中信所2025(14)、EI剔除2026(19/228)、WoS剔除2026(16)
- **铁律**：零覆盖来源组 ≤6；arXiv 占比 ≤50%；**期刊占比 ≥40%**；综述链接必须回查 `library.db.url`

## 执行流程与一致性
`阶段0 git pull+sync_skills.py install` → `阶段1 顶会/IEEE（≥5 条初筛）` → `阶段2 harvest+screen+来源矩阵` → `阶段3 build_daily+gen_html` → `阶段4 发布+飞书/机器人+周报/看板` → `阶段5 五审` → `阶段6 记忆写入`
- `ocean-daily-report` skill 是唯一权威源，prompt 纯委托；流程调整先改 skill
- 每期产出：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 滚动本文件 + 双路径追加 `automations/ai/memory.md`
- 规模：每方向 3–5 条、合计 27–45；某方向确无新内容可为 0，**宁缺不凑数**；≤14 天，近 7 天优先；禁同日并行执行

## 内容质量规则（完整版见 SKILL）
1. 时效 ≤14 天；14–60 天须豁免说明；>60 天删除（arXiv 以 v1 提交日为准）
2. 每条 URL 实测可访问（403/000 用 `verify_paper.py` 复核）；工具版本须官方 release notes 核实；摘要自原文提取，不据标题推断
3. 跨期去重三路（URL 集合差 + 中文片段 + DOI/卷期）；同 URL 只在一个方向；主页新闻须给具体链接
4. 来源矩阵逐组打卡（零覆盖 >6 组须补检）；阶段一采纳条目须在阶段三构建时即纳入，非事后补丁

## 常见故障
| 问题 | 解决方案 |
|------|---------|
| Windows push 沙箱拦 `~/.ssh` | Bash + `dangerouslyDisableSandbox: true` |
| pull --rebase 因未暂存改动失败 | `screen.py` 会改 `journal_tiers.json`/`pending_journals.txt` → **先 `git add -A` 再 rebase/push** |
| 复合 git 命令静默中断 | 收尾必查 `HEAD == origin/main` + 工作区干净 |
| 403（MDPI/ScienceDirect/Wiley/AGU/T&F） | 反爬≠死链，`verify_paper.py` 核实 |
| curl 000 / 502 Tunnel / URLError / 302·404·405 | 沙箱代理波动或站禁用 HEAD → 换 `curl -L -m 45` 重测、HEAD 失败回退 GET、或 WebFetch 复核 |
| 臆造 URL / 聚合站日期 | 严禁按模式推断；一律查原文首发日 |
| 飞书 API 404 | **根因是端点写错非 token**：`POST .../documents/{doc}/blocks/{doc}/children`（body `children`）。样式须放 `text_run.text_element_style`，旧 `text_run.style/link` 被**静默忽略**。详见 SKILL 陷阱 31 |
| 飞书文档同日重复 | 按标题 `海洋AI技术日报 YYYY-MM-DD` 命中即清空重写，未命中才新建（陷阱 33） |
| `index/archive` 里出现 Python 源码明文 | publish 正则跨节捕获（遇无 url 的 `[备注]` 条目必发）→ 改 AST 抽条目 + 跳过无 url 项；模板见 `repair_publish_1105.py`，替换前先断言区间含 `'badge':` |
| OpenAlex 401/429 | cursor 第 2 页起需 key、重查询扣额度；失效改 WebSearch/Crossref 人工补检 |
| OpenAlex 会议论文为 0 | 类型值须 `conference-paper`（旧 `proceedings-article` 恒返 0 且不报错）；用已知会议论文反查做阳性对照 |
| `git add -A` 后 `pull --rebase` 报 uncommitted changes（11-09） | 暂存态同样会阻断 rebase → **先 commit → 再 rebase → 再 push** |
| `verify_paper.py` 判 IEEE 论文「超期 312 天」（11-09） | 日期塌缩伪告警，非超期；首发日以 `stage1_ieee_crossref.py` 的 Crossref `created` 为准 |
| `gen_html` 模板硬编码「日期范围」（11-09） | 复制上期模板须同时改 TODAY/TODAY_CN/周几/日期范围；已改为 `DATE_MIN/DATE_MAX` 动态计算 |
| Zenodo 概念 DOI 的 OpenAlex 日期早于当期（11-09） | 那是记录首次出现日；时效按具体版本发布日（v1.8 = 11-04），并 WebFetch 复核非 Tombstone |

## 去重基准（最近 3 期；更早 `grep -rl posts/`）
> `posts/` 为全量存档；本节只列「易被再次检索命中」的标识符，完整条目见当日日志。**11-06 及更早期次、11-09 的完整清单均已迁入 ARCHIVE.md 第一节**（去重脚本本就扫 `posts/` 全量，此处仅留「最易被再次命中」的当期基准；需要时 grep ARCHIVE）。最近 3 期＝11-11（本期）/11-09/11-06。

- **11-09（36条，期刊21条58.3%）·完整 36 项见 ARCHIVE**。高风险标识符：FASST `arXiv.2610.36297`、GAP `s41612-026-01585-4`、TIP `3748963`、JSTARS `3751362`/`3750208`/`3747308`、LGRS `3750909`、TGRS `3751156`/`3749724`、LRA `3747601`、OCEAN-X `ecomagazine.com`、FIO-AOW `scs.mnr.gov.cn/202611/10d58a41`、CDO `0131-6184-2026-5-60-69`、CMIP6 `wcd-7-2155-2026`、Abyssal Claims v1.8 `zenodo.19745884`、顶测深剖面 `im-2026-02-02-003`、海滩垃圾足迹 `ecolind.2026.115751`、GNSS-R `10095020.2026.2753898`、孟加拉湾波候 `joc.70653`、SWOT+DTU21 `gji/ggag480`、涡街综述 `20964471.2026.2753277`、HY-3A、OPMM2 `fmars.2026.1941879`、PODA 奖、ISO/TC211 S-100、保护智能 `csp2.70437`、第43次南极考察队、MARLEY `dsr.2026.104771`、OSR10 `marine-ireland.ie/node/2150`、NCEI GTSPP `0319413`、马里亚纳海底图 `oceanvines.org`、pystac 1.16.0 / rio-tiler 9.4.13 / pyvista 0.49.2。
- **11-06（36条，期刊15条41.7%）·完整 36 项见 ARCHIVE**。高风险：Nereus `2610.41705`、PhysFTM `2611.03717`、GNN-VIEW `2610.35693`、BGC 零样本 `2610.39777`、JOE `3733262`/`3724447`、TGRS `3748509`/`3746583`、GRL `2026gl122406`/`2026gl123962`、GOOS 2026 `10.71245/yfva2935`、星海-BBNJ、海山图志、CMEMS `OC-1116`、MICAP `2751876`、CWAVE_S1TC `jtech-d-26-0075.1`、GAS11、PANGAEA `998107`、earthkit-data 1.3.1、gridded v0.8.2、AI 预报评测标准。
- **11-05 及更早**：已滚出 3 期窗口，全量清单见 `ARCHIVE.md` 第一节，高风险子集见第三节 3.8；去重时直接 `grep -rl posts/`。

- **勿再收名单** → 已整体迁入 `ARCHIVE.md` 第二节（含「已收录不重发」显式标注条目）。**新增条目时须标注属「质量弃用」还是「xx 期已发」**，二者语义不同，否则后人会误读。11-09 新增显式标注：WOA II 地理—主题可视化 `10.1177/14738716261492254` 属「11-02 期已发」，本期误收后已剔除。

## 漏检核查与已知盲区（2026-11-04 建立）
> 苏老师抽查「某篇是否收录」的处置台账，每条须落成「已收录 / 时间窗正当排除 / 系统未运行 / 真实漏检 + 根因」四类之一。完整案例与取证见 `ARCHIVE.md` 4.3–4.4。

- **已核查结论**（取证见 `ARCHIVE.md` 4.3）：ESSD 3D-U-Net++ → 09-04 已收录；GBM 海洋锋 → 首发早于首期，正当排除；PINN 不确定性 → 双源无摘要不收；KunPeng → **真实漏检**，11-04 补录。
- **根因 1 · IEEE 日期塌缩（系统性，最严重）**：TGRS 等刊 OpenAlex `publication_date` 恒为当年 1-1，`created/updated_date` 也不等于首发日 → 按日期窗口拉 IEEE 期刊恒返 0。修复：`stage1_ieee_crossref.py --start/--end [--no-abstract]`（Crossref `from-created-date`）→ `_stage1_ieee.json`。**阶段一 IEEE 组必须跑。**
- **根因 2 · 链接形式不一致**：同一成果可能用 DOI / 出版商直链 / 机构新闻稿 → 只做 URL 集合差会假阴性。去重前须 DOI 归一化（细则 `ARCHIVE.md` 4.4），新条目**优先 `https://doi.org/...`**。
- **根因 3**：最早期次 `2026-03-23`，此前论文属天然缺口。
- **纪律**：核查「是否收录」不能只 grep DOI，须同时 grep DOI 尾段数字、期刊简称+卷+页、英文标题词、中文标题词；「已剔除」须标注属「质量弃用」还是「xx 期已发」。

## 经验教训（活跃判据）
**内容与口径**
- **五审必须独立复算去重（11-09 铁律）**：阶段二「已去重」不可信，须独立跑 URL 集合差 + 中文片段 + DOI 尾段三路；「新闻稿/中文标题 ↔ DOI」并存的成果两个标识符都要查（完整事故 `ARCHIVE.md` 3.7）。
- **改数据源后回滚式重发**：`git checkout <本期首发 commit>^ -- index.html archive.html` 再重跑 publish，避免卡片重复插入；随后完整重跑 build_daily → gen_html → publish → 飞书 → 周报注入。
- **飞书回读校验项（11-09）**：`code=0` / 块数 / 链接数 / 新条目已写入 / 旧重复已移除；仅看 200 ≠ 内容正确。W46 综述 25 链接全数回查 `library.db.url`（异常 0），池内噪声（高频词 `disease`/`china`、方向七/九混入医学/农学）须人工复核，自动聚类不可直接当结论（详见 `ARCHIVE.md` 3.7）。
- **期刊占比 ≥40% 在阶段三定稿时核算（11-04）**：本期到五审才发现 29.4%，补救等于重跑两遍发布。`build_daily` 出数立即算占比，不达标就地补检。
- **方向三/四/六/八是结构性「期刊荒漠」（11-04）**：可视化/数据质量/数据管理/数据中心的产出形态是产品发布、机构动态、工具版本，池里几乎无期刊论文 → **阶段二就用 OpenAlex `title_and_abstract.search` 定向补检**。
- **无摘要即不收（11-02）**：Elsevier/ACM/OUP 新刊（Ocean Engineering / ISPRS / DSR）在 OpenAlex（`abstract_inverted_index` 空）、Crossref（`abstract` 缺）、S2 三处齐缺，ScienceDirect 有 CAPTCHA。**绝不据标题推断摘要**；改从 `data/pool/*.jsonl` 的 `abstract` 字段筛有摘要的候选。
- **宁缺不凑数（09-15 拍板）**：不为凑数跨类硬塞；日期不可核验时同样不收。
- **事件日 ≠ 报道日**：取报道/论文发布日；arXiv 以 v1 提交日为准，聚合站日期多次被证伪。
- **中文条目去重必须用中文片段 grep**：否则 URL 集合差会漏判。

> 下列判据的完整取证数字/操作步骤见 `ARCHIVE.md` 第七节（原文照录）。

**OpenAlex / Crossref**
- **阶段一 IEEE 组必须跑 `stage1_ieee_crossref.py`**（Crossref created 通道，11-05 复验有效）；IEEE 首发日以 Crossref `created` 为准，`publication_date` 恒塌缩为当年 1-1。
- **双源无摘要即弃用**：OpenAlex `abstract_inverted_index` 与 Crossref `abstract` 皆空 → **绝不据标题推断**（弃用清单见 ARCHIVE 第七节）。
- **滤镜/字段**：`issn:` 返 400 → 须 `primary_location.source.issn:`（JOE issn_l `0364-9059`）；0 结果先怀疑字段名；`host_organization` 不可靠（不能判出版商零覆盖）；`%20` 会被二次编码恒返 0 → 滤镜用真实空格；`page=` 有 `max_pages×200` 上限 → 做阳性对照 + 核对 `meta.count`。
- **索引滞后 T+2/T+3** 属正常；**池 jsonl 的 DOI URL 小写存储** → 跨源比对须大小写归一。

**产出与发布**
- **Zenodo 概念 DOI 须 WebFetch 查 Tombstone**（撤回页）；概念 DOI 尾号常与版本 DOI 差 1，按尾段数字 grep。
- **publish 一律用 AST 抽条目，禁用正则**：跳过无 url/`[备注]` 项，替换前断言区间含 `'badge':`（模板 `repair_publish_1105.py`）。
- **补录板块**：漏检有价值时末尾单列「十、补录」（`count_as_direction=False`），台账 `badge='[备注]'` 不计 effective，`date` 填首发日并写明原因；footer 来源按 `sections` 动态生成（勿写死）。
- **改内容必须重跑 build_daily 再跑 gen_html**；**回滚式重发**先 `git checkout <base> -- index.html archive.html` 再 publish；GitHub Pages 重建约 100 s，复核加 `?v=n` 破 CDN；周报 ISO 期号会跳号（W43→W45）。

**历史事故铁律**（完整叙述见 ARCHIVE 第三节）
- **HTTP 200 ≠ 业务成功**：①校验响应体 `code` ②回读落库（飞书曾 200 全通而 27 条链接全丢）。
- **公开仓库禁硬编码凭证**：已统一 `_feishu_auth`；五审含「改动文件是否新增硬编码凭证」。
- **远程文档写入须幂等复用 + 回读块数**：曾堆积 137 个文档、89 个同日重复。
- **主题盲区**：国内院所新闻、极地/海冰；会议通道曾长期归零（10-18 修复）。
- **用户指定条目与去重冲突**：先核实历史收录，给结论 + 三选项交苏老师拍板。

## 归档索引
| 需要什么 | 去哪里 |
|---|---|
| 10-25 及更早期次去重标识符 | `ARCHIVE.md` 第一节 |
| 勿再收完整名单（含「已发不重发」标注） | `ARCHIVE.md` 第二节 |
| 已结案事故取证叙述（凭证/文档堆积/截断等） | `ARCHIVE.md` 第三节 |
| Crossref IEEE 通道实测数字、KunPeng 日期字段取证 | `ARCHIVE.md` 第四节 |
| 待拍板事项（D 级加严 / 周报期号 / 自动化状态） | `ARCHIVE.md` 第五节 |
| 11-09 事故闭环、11-05 高风险标识符 | `ARCHIVE.md` 第三节 3.7 / 3.8 |
| 经验判据的取证数字与操作步骤原文 | `ARCHIVE.md` 第七节 |
