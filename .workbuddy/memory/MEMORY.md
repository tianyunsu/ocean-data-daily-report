# 海洋AI研究日报系统记忆

> **本文件每次执行都会注入上下文，因此只保留「每日必需 + 决策判据」。**
> 历史台账、已结案事故的取证叙述、滚出 3 期窗口的去重标识符、勿再收完整名单、待拍板事项 → 见 **`.workbuddy/memory/ARCHIVE.md`**（检索才读，可持续增长）。
> **2026-11-04 首次压缩**：22,989 B / 14,371 字符 → 16,324 B / 10,100 字符（−29%），溢出内容迁入 ARCHIVE.md，**信息零丢失**（362 个 token 全量校验，仅余 3 处表述差异）。每超 16 KB 触发一次归档。

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
| curl 000 / 502 Tunnel / URLError / Timeout | 沙箱代理波动（neurips/zenodo/seanoe/Copernicus/Nature）→ 换 `curl -L -m 45` 重测或 WebFetch 复核 |
| HEAD 302/404/405 但链接有效 | 站禁用 HEAD → 核链须 HEAD 失败回退 GET |
| 臆造 URL / 聚合站日期 | 严禁按模式推断；一律查原文首发日 |
| present_files 预览污染 HTML | 先 commit+push 再 present，事后 `git status` 复查 |
| 飞书 API 404 | **根因是端点写错非 token**：`POST .../documents/{doc}/blocks/{doc}/children`（body `children`）。样式须放 `text_run.text_element_style`，旧 `text_run.style/link` 被**静默忽略**。详见 SKILL 陷阱 31 |
| 飞书文档同日重复 | 按标题 `海洋AI技术日报 YYYY-MM-DD` 命中即清空重写，未命中才新建（陷阱 33） |
| OpenAlex 401/429 | cursor 第 2 页起需 key、重查询扣额度；失效改 WebSearch/Crossref 人工补检 |
| `harvest.py --dirs` 重跑覆写池 | 先 `cp data/pool/日期.jsonl data/pool/_bak_日期.jsonl`，失败后合并恢复 |
| OpenAlex 会议论文为 0 | 类型值须 `conference-paper`（旧 `proceedings-article` 恒返 0 且不报错）；用已知会议论文反查做阳性对照 |

## 去重基准（最近 3 期；更早 `grep -rl posts/`）
> `posts/` 为全量存档；本节只列「易被再次检索命中」的标识符，完整条目见当日日志。**11-02 及更早期次已迁入 ARCHIVE.md 第一节**（去重脚本本就扫 `posts/` 全量，此处仅留「最易被再次命中」的当期基准；上期标识符需要时 grep ARCHIVE）。

- **11-04（42条，含补录2条）**：e.huawei 司渊海洋大模型、qdio.cas.cn 8299912 苏禄海内孤立波 TGRS、arxiv 2610.29313 YingLan、10.1145/3840750.3841451 GreenToken ACM MM、10.1109/LRA.2026.3746126 ISOPoT、sznews 32199065 深圳防灾孪生、weibo 5359283964608565 北部湾孪生一等奖、SEC 1846715 Eco Wave 孪生、zenodo.23674230 EDITO EOSC、mapgis id=1913 海洋版、qq 20261028A04ZEQ00 耕海1号一张图、mp.weixin 漂视 CIMPro、10.5194/sd-35-229-2026 GEODESC、10.1111/1752-1688.70158 OSTDS GIS、ckjorc detail/3435 GOCI-II、cran argoFloats、arxiv 2610.37731 摊销后验、10.1175/jtech-d-26-0004.1 X 波段波向、10.5194/essd-2026-807 Morlenn、10.5194/essd-18-7963-2026 MLAWind、qdhy.cbpt.cnki 葵花8号超分、arxiv 2610.36410 LILY、10.1038/s41598-026-76456-2 机载测深激光雷达、seabed2030 波罗的海 BSHC、cioos.ca IODE ADU、watertools 538 Okeanos-OBIS/GBIF、10.1175/bams-d-25-0157.1 NNJA、sciencenet 574029 CliMetS/MOCSI、10.1029/2026GL124056 北极碳质气溶胶、10.1038/s41598-026-78685-x 南极 UAV 海鸟、ysfri 59428 蓝海101、cnfin 4488855 青岛海洋大数据应用中心、watertools 544 Sentinel-6B、copernicus product-roadmap 11月更新、10.5194/essd-18-7839-2026 IBRA 伊势湾、10.1002/lom3.70102 Ricker 小波、pypi oceanarray、zenodo.23749880 thermochain、ebiotrade 20261023104103527 CN-Waves、10.3390/computers15110763 WindAnalysis（MDPI/D）、**10.1109/TGRS.2026.3708338 KunPeng 全球海洋环境预报模型**、**10.1109/TGRS.2026.3660295 GBM 海洋锋检测**（后两条为 11-04 补录）

- **勿再收名单** → 已整体迁入 `ARCHIVE.md` 第二节（含「已收录不重发」显式标注条目）。**新增条目时须标注属「质量弃用」还是「xx 期已发」**，二者语义不同，否则后人会误读。

## 漏检核查与已知盲区（2026-11-04 建立）
> 用途：苏老师抽查「某篇是否收录」时的处置台账。每条须落成「已收录 / 时间窗正当排除 / 系统未运行 / 真实漏检 + 根因」四类之一。取证明细见 `ARCHIVE.md` 第四节。

### 已核查案例
| 文章 | DOI | 结论 | 根因 |
|------|-----|------|------|
| ESSD 注意力增强 3D-U-Net++ 西太温盐重构 | `10.5194/essd-18-4617-2026` | **已收录 2026-09-04**（方向五） | 日报用 Copernicus 直链而非 DOI → 按 DOI 检索出现假阴性 |
| TGRS GBM 海洋锋检测框架 | `10.1109/TGRS.2026.3660295` | 时间窗正当排除（后补录） | 首发 `2026-02-03`，日报最早期次 `2026-03-23` → **系统上线前** |
| The Innovation Informatics PINN 降海洋状态预报不确定性 | `10.59717/j.xinn-inform.2026.100051` | 无摘要不收 | 首发 `2026-07-20`，OpenAlex + Crossref 双源无摘要 |
| TGRS KunPeng 全球海洋环境模型 | `10.1109/TGRS.2026.3708338` | **真实漏检**（后补录） | 首发 `2026-06-30`、有 1716 字符摘要、落在 07-01 窗口内，但 OpenAlex `publication_date` 被归一化为 `2026-01-01` |

### 三类根因（按影响面排序）
1. **IEEE 期刊日期塌缩（最严重，系统性）**：TGRS 等 IEEE 刊在 OpenAlex 的 `publication_date` **恒为当年 1 月 1 日**，`created_date`/`updated_date` 也不等于首发日。后果：按日期窗口拉取时 IEEE 期刊永远返回 0，这些刊的论文**结构性无法进入日报**（10-21/11-02/11-04 三期通道全 0 均源于此）。
   - ✅ **修复方案（已实测有效）**：改用 **Crossref `filter=issn:<issn>,from-created-date:<start>,until-created-date:<end>`**；`created` 字段 = DOI 注册日，与首发日基本一致。
   - 🔧 **已落地工具**：`stage1_ieee_crossref.py`（2026-11-04 新增）。用法 `py -3 stage1_ieee_crossref.py --start YYYY-MM-DD --end YYYY-MM-DD [--no-abstract]`，输出 `_stage1_ieee.json`（已 gitignore）。**阶段一 IEEE 期刊组必须跑此脚本，不得只用 OpenAlex 日期窗口。**
2. **链接形式不一致（去重假阴性）**：同一条目可能用 DOI 链接、出版商直链（Copernicus `/articles/vol/page/year/`、MDPI `/issn/vol/issue/page`、IEEE `document/id`）或机构新闻稿链接；只做 URL 字符串集合差会把已发条目误判为「未收录」→ 重复收录或误入勿再收名单。
   - ✅ **修复**：去重前先做 DOI 归一化 —— `doi.org/(10\..+)` 直取；Copernicus 用 `{journal}.copernicus.org/articles/{vol}/{page}/{year}/` → `10.5194/{journal}-{vol}-{page}-{year}`；兜底标题归一化（去标点、小写、前 60 字符）。
   - 📌 **规范**：新条目**优先用 `https://doi.org/...`**，让 URL 比对天然等价于 DOI 比对。
3. **系统上线前的历史文章**：日报最早期次 `2026-03-23`，此前论文不在任何期次检索范围，属不可补的天然缺口（需覆盖只能显式回溯）。

### 处置纪律
- 核查「某篇是否收录」**不能只 grep DOI** —— 必须同时 grep：DOI 尾段数字、期刊简称+卷+页（如 `18, 4617`）、英文标题关键词、中文标题关键词。
- 「已剔除」名单混有两类语义（质量弃用 vs 已发不重发），新加入时须显式标注。

## 经验教训（活跃判据）
**内容与口径**
- **期刊占比 ≥40% 在阶段三定稿时核算（11-04）**：本期到五审才发现 29.4%，补救等于重跑两遍发布。`build_daily` 出数立即算占比，不达标就地补检。
- **方向三/四/六/八是结构性「期刊荒漠」（11-04）**：可视化/数据质量/数据管理/数据中心的产出形态是产品发布、机构动态、工具版本，池里几乎无期刊论文 → **阶段二就用 OpenAlex `title_and_abstract.search` 定向补检**。
- **无摘要即不收（11-02）**：Elsevier/ACM/OUP 新刊（Ocean Engineering / ISPRS / DSR）在 OpenAlex（`abstract_inverted_index` 空）、Crossref（`abstract` 缺）、S2 三处齐缺，ScienceDirect 有 CAPTCHA。**绝不据标题推断摘要**；改从 `data/pool/*.jsonl` 的 `abstract` 字段筛有摘要的候选。
- **宁缺不凑数（09-15 拍板）**：不为凑数跨类硬塞；日期不可核验时同样不收。
- **事件日 ≠ 报道日**：取报道/论文发布日；arXiv 以 v1 提交日为准，聚合站日期多次被证伪。
- **中文条目去重必须用中文片段 grep**：否则 URL 集合差会漏判。

**OpenAlex / Crossref**
- **滤镜字段会改名（10-25）**：`issn:` 返 400，须 `primary_location.source.issn:`；0 结果先怀疑字段名。JOE 正确 issn_l = `0364-9059`。
- **`host_organization` 不可靠（11-04）**：传 T&F/SAGE/AAAS/IOP 返回 Springer/OUP/BMC → **不能判定出版商零覆盖**。
- **filter 里写 `%20` 会被二次编码（11-04）**：`title_and_abstract.search:ocean%20visualization` 变字面值，恒返 0 且不报错 → 滤镜一律用真实空格。
- **分页/词表静默截断**：`page=` 有 `max_pages×200` 上限 → 须做阳性对照并核对 `meta.count`。
- **索引滞后 T+2/T+3**：池内最近两天偏少属正常，勿误判采集失败。
- **池 jsonl 的 DOI URL 小写存储**：跨源比对须大小写归一。

**产出与发布**
- **补录板块机制（11-04）**：历史漏检且有价值时**不散进 9 方向**（破 3–5 条上限），末尾单列「十、补录 · 往期漏检勘误」。①板块加 `'count_as_direction': False`；②台账用 `badge='[备注]'`（不计 effective）；③补录 `badge='[补录]'` → `badge-errata`，`date` 填**首发日**并写明漏检原因，五审时效须单列说明。publish 条目正则按 `'url'` 匹配，无 url 的备注条目自动排除出卡片摘要。
- **footer 来源按条目动态生成（11-04）**：原写死 11-02 列表，派生新期即失真；遍历 `sections` 的 `source`（按 `/` 与 `（` 截断）去重拼接。
- **改内容必须重跑 build_daily**：`gen_html` 读的是注入后的 `SECTIONS`，否则出一模一样的 HTML。
- **回滚式重发**：先 `git checkout <base> -- index.html archive.html` 再重跑 publish，避免卡片重复插入。
- **GitHub Pages 重建约 100 s（11-04）**：复核须等 60–90 s 并加 `?v=n` 破 CDN。
- **周报 ISO 期号会跳号（11-02）**：W43→W45；如需连续应改按「距上期天数」命名。

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
