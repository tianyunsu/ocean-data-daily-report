# 海洋AI研究日报系统记忆

## 系统配置
- **用户**：苏老师 · **自动化ID**：`ai`（`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）
- **仓库**：https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（`SECTIONS=[...]`，由 `build_daily_YYYYMMDD.py` 正则替换）；**HTML**：`gen_html_YYYYMMDD.py`（自包含，`ast.literal_eval` 解析，禁止 import feishu）
- **本机 Python**：默认 `python` 缺 `requests`，飞书/机器人须用 **`py -3`**；Bash 偶发 PATH 损坏（grep/head 失效）→ 改用 PowerShell + 专用工具

## 前沿跟踪四层架构（2026-09-20 落地）
- **为什么**：日报每方向 3-5 条是**排版口径**，非覆盖口径。实测 14 天窗口全海洋类期刊 2,249 篇、海洋AI/数字孪生/数据相关约 350 篇，日报仅呈现 27 条（留存 ~10%）。故加 L0/L1/L3，**L2 日报质量红线不降级**。
- **L0** `harvest.py` → `data/pool/YYYY-MM-DD.jsonl`（9 方向 × OpenAlex 期刊 + **OpenAlex-arXiv 预印本通道** + 会议，T+1；实测 3,932 条/14 天）
- **L1** `screen.py` + `tier_engine.py` + `source_metrics.py` → `data/library.db` + `data/pool_index.json`（去重+分级+契合度+打分；实测 3,932→183 条，未登记期刊 0）
- **L2** 日报（6 阶段流程不变）　**L3** `frontier.html`（全池可检索看板）+ `weekly_report.py` → `weekly/YYYY-Www.html` + `weekly/index.html` 索引 + `weekly/synth/YYYY-Www.draft.md`
- **周报综述板块（2026-09-20 新增）**：两层——① 自动综述（脚本生成，逐方向主题簇+代表文献+主要期刊，`TERM_CN` 中文簇名词典）；② 深度综述（写 `weekly/synth/YYYY-Www.md` 后跑脚本自动注入页顶）。综述样本＝池内**剔除 D 级预警刊与「已降权」项**（183→155），剔除数单列不删除。
- **周报访问入口（三处，缺一则用户找不到）**：`index.html`/`archive.html`/`frontier.html` 导航「前沿周报」→ `weekly/index.html`；首页 `</header>` 与 `<main>` 之间的横幅卡片（放 main 外防被 post-card 顶下去）。线上 `…/weekly/index.html`。
- **铁律**：综述里每条链接必须回查 `library.db` 的 `url`，**严禁凭 DOI 规则手写**（09-20 实测臆造 2 处）
- **每期必报指标**：采集量 / 池内量 / 日报收录 / 留存率 / **arXiv 占比 ≤50%** / **期刊占比 ≥40%** / 零覆盖来源组 ≤6
- **L1 打分**：期刊权重（S6/A5/B4/C3/P2.5/D1）×100 + 相关度×8 + 时效 + **海洋契合度**
  - **海洋对象 vs 介质**（09-20 新增，看板降噪关键）：`ocean/marine/coastal/bathymetry/seabed/fisheries/Arctic…`＝研究海洋；
    `seawater/water/wave/polar/tide` **+** `catalyst/battery/clinical/crop/hydrogel…`＝**用海而非研究海** → 判 `off` 降权 −150（**不删除**，看板可切"仅被降权项"复核）。实测 off 18 / 弱相关 71 / 标题即海洋主题 94

## 期刊分级口径（2026-09-20 苏老师拍板 · 七项决策后定稿）
- **S** Nature/Science/PNAS 正刊及顶级子刊；**A** 领域权威（AGU/Copernicus/IEEE/Elsevier 顶刊；Scientific Reports、Ocean Engineering、npj Heritage Science 经确认归 A）
- **B** 主流 SCI / **中文刊学科影响因子前 25%**（海洋学报、遥感学报）；**C** 一般刊·集团刊（**Frontiers 全集团**、PLOS ONE、Heliyon；海洋科学、中国海洋大学学报、热带海洋学报）
- **D** 预警/受限（MDPI 全集团、Hindawi、中科院/中信所预警、**SCI(SCIE)/EI 剔除**）：**强制置底并标注，不删除**
- **P 预印本**：**若已对应期刊论文则按所属期刊等级排序**（时效优先），保留"预印本"标注。匹配依据 ① 采集期 OpenAlex `locations` → ② 同 DOI → ③ 同标题指纹 → ④ arXiv `journal_ref`；均未命中才归 P
- 判定顺序：**预印本升级 → 登记表 → 最新一期预警/剔除名单（支持 ISSN）→ 集团规则 → 指标自动评级 → 待确认**
- **自动评级阈值（按实测下调）**：A `h≥120` 或 `h≥70 且 c≥3.0`；B `h≥50` 或 `h≥30 且 c≥2.0` 或 `c≥4.0`；C `h≥8` 或 `c≥0.5`
  （实测各档 h 中位 S280/A210/B106/C54；**原"仅凭 c≥6.0 进 A"已废**——曾误判旅游/生化刊为 A；巨型刊降级条件＝`年发文>2500 且 c<8`，避免误伤 Advanced Materials）
- 名单规则：**不累积使用**（移出即不再预警），存 `data/journal_tiers.json` 的 `warning_lists`，`active` 控制生效
- 已核实：中科院2025（5本）、中信所2025（103本→录14条）、中科院2024（存档）、**EI剔除2026**（228条中录 `Final Coverage≥2022` 的19条，余209条存档）、**WoS剔除2026**（SCIE/SSCI 16条，含 Sea Technology）
- 出版方别名已补：MDPI 全称 `Multidisciplinary Digital Publishing Institute`、Hindawi Limited、Frontiers Media SA（此前 MDPI 全称漏判，Biosensors/Diversity/Marine Drugs 漏标 D）
- **问答式校准**：未登记刊 → `data/pending_journals.txt`（按命中篇数降序），交付时只挑 ≥2 篇的向苏老师提问

## 一致性机制（手动=自动，铁律）
- `ocean-daily-report` skill 是手动/自动**唯一权威源**，自动化 prompt 纯委托该 skill。
- 每次执行（手动/自动）必须产出相同工件：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 更新本文件去重基准 + 追加 `.workbuddy/automations/ai/memory.md`。
- **跨机器**：记忆随仓库入库；skill 用 `sync_skills.py`（install=仓库→用户，collect=反向，status=比对）。铁律：执行前 `git pull` + `install`，执行后 `push`，禁同日并行。

## 执行流程（6 阶段）
```
阶段0  git pull origin main + sync_skills.py install
阶段1  顶会检索(23会议+IEEE期刊,≥5条强制,≥2条须来自会议/IEEE)
阶段1B 国内院所新闻巡检(海洋所/南海所/深海所/青大/南科大) + 顶级期刊综述检查
阶段2  先跑 harvest.py + screen.py 取全量池，再 9 方向检索 + 来源覆盖矩阵逐组打卡 + 去重黑名单
阶段3  build_daily_XXX.py 写 SECTIONS + 归类自检 + gen_html_XXX.py 出 HTML
阶段4  复制 posts/ + 更新 index.html/archive.html + commit + push
阶段4.5 飞书 feishu_write_doc.py + 机器人 run_daily_report.py（均失败不阻断）
阶段5  五项审查：链接+摘要一致性 / 时效 / 来源覆盖 / 归类与条数 / 去重
阶段6  写日志 + 更新本文件去重基准 + 追加 automations 摘要
```
- **规模时效口径**：每方向 **3-5 条**、全日报 **27-45 条**（确无内容可为 0，不凑数）；**≤14 天**，**近 7 天为同方向排序优先权**（非硬门槛）。

## 内容质量规则（要点；完整判定表以 skill `references/quality_standards.md` 为准）
1. 时效：≤14 天；14–60 天须重要性豁免；>60 天删除（**arXiv 以 v1 提交日为准**，非聚合站索引日）。
2. 每条 URL 必须实测可访问，404/403 超时一律不收（反爬 403 见故障表）。
3. 工具版本特性须从官方 release notes 核实；摘要须自原文提取，不得据标题推断，**不得张冠李戴**。
4. **发布前必须 `grep -rl` 核查 `posts/` 跨期去重**（最高频事故点）。
5. 方向归类按文章内容判断；同 URL 只出现在一个方向；主页新闻须给具体链接。
6. **来源覆盖矩阵逐组打卡**（A 组 9 类 + B 组出版商 + 阶段一会议/IEEE），零覆盖组记日志归因，**>6 组视为检索不足须补检**（详见 skill 陷阱 14/15）。

## GitHub Pages 架构
- main：源码+每日日报（posts/、index.html、archive.html）；supplement：另一台机器结果；gh-pages：Actions 自动部署（勿手编）。
- 每次生成后必须**同时**更新 index.html 和 archive.html（post-excerpt 为硬编码文本，删改条目后两处同改）。

## 常见故障处理
| 问题 | 解决方案 |
|------|---------|
| git push TLS/代理/127.0.0.1:65532 失败 | `git config --unset http.sslbackend`；`unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` 后 `git -c http.proxy= -c https.proxy= push origin main` |
| git push 443 超时/reset | 直连不稳，重试 3–5 次（Git Bash 无 sleep）；SSH 不可用；Windows 下 push 需 `dangerouslyDisableSandbox: true` |
| git commit 无法识别身份 | 仓库级 `git config user.name/user.email`（tianyunsu / tianyunsu@users.noreply.github.com） |
| Python urllib 出网被拒(WinError 10061) | 沙箱阻断直连；链接校验改用 WebFetch，勿写探测脚本 |
| urllib 403（MDPI/ScienceDirect/Wiley） | Cloudflare 反爬≠死链，**首选 `verify_paper.py`（Crossref+OpenAlex 官方 API）**核实元数据；无 DOI 时 WebFetch 二次确认 |
| **arXiv export API 被 WAF 拦截** | `export.arxiv.org/api/query` 对**全部 UA 返回 406**（曾 429），但 `arxiv.org/abs/*` 200 → 端点拦截非网络故障。**改走 OpenAlex**：`filter=locations.source.id:S4306400194`（`harvest.py --preprint-only`）；旧代码还只对方向一检索 arXiv，现已 9 方向覆盖 |
| arXiv 老文补登伪新稿 | 高 arXiv ID ≠ 新成果，必查 v1 提交日与原文年份（09-04 剔除 HorizonNet 实为 2018 旧文） |
| **present_files 预览污染本地 HTML** | 注入 `data-page-node-id`。**先 commit+push 再 present；present 后 `git status` 复查，变脏即 `git checkout --`** |
| 转载站在大陆不可访问 | Yahoo/MSN 类对大陆返回"服务不可访问"=死链，选源优先原始媒体并核对其日期是否为索引日 |
| urllib 命中但内容是挑战页 | 返回 200 而 title 为 "Client Challenge" = 反爬页≠有效内容，须 WebFetch 二次确认 |
| **臆造 URL（按模式猜测）** | **严禁凭 URL 模式推断链接**（09-14 按自然资源部规则拼出的两条实测 404）；无直链改用权威转载源并如实标注 |
| **整期批量取稿致跨期重复** | 09-14 从 JMSE 14(16) 取的两条已分别在 08-18/08-10 收录。**铁律：每个 DOI 尾号单独 grep `posts/`** |
| **"已去重"自述不可信** | 跨机接手必须独立复算 URL 集合差与时效差，不采信对方结论 |
| Edit 报 File has been modified | 用 Bash 改过同文件后，再 Read 一次即可继续 Edit |
| 飞书链路（长期不可用，可跳过） | `run_daily_report.py` 需 `$env:PYTHONUTF8=1`；docx blocks 404 疑 app token 缺权限 |

## 去重基准（最近 3 期；更早一律 `grep -rl posts/`）
> `posts/` 即全量存档，规则 4c 的 grep 比读基准更可靠。本节仅列「易被再次检索命中」的标识符。
- **09-15**：2609.15676 MambaMPD、2609.15484 CatchMonitor、LeadNet泛北极冰间水道、DISCUSS深海微生物数字孪生、DTO-BioFlow、CCGS Amundsen、SST强迫静默切换(Climate Dynamics)、10.1029/2026JC024312、os-22-2725-2026、npj Ocean Sust FAIR、E-ODP、中俄北冰洋走航、CMEMS WAV-305、Parcels v4.0、hydrolib-core、oceanval
- **09-20（27条+1备注[D2空]）**：2609.19768 OceanMoE、海洋Token工厂、2609.16288 Drift Field Net、2609.16347 海冰多标签、2609.20680 OceanSim、2609.18737 水下3DGS、2609.11673 浮游生物扩散、2609.17124 LOTUSim-Energy、2609.20350 PAMGuard 3D声定位、2609.13659 UniqueShip、2609.09451 多冰图软监督、SeaExplorer QC(fmars.2026)、GDCM-EOF(remotesensing.1064)、2609.18531 高光谱叶绿素、2609.12744 AquaCubeAI Φsat-2、2609.17929 声呐+光学建图、JMSE14(18)1676、UN海洋十年数据共享讨论稿(EU 952324)、海洋十年公益倡议(网易L779I5MM)、中-海管局培训中心(腾讯20260918A0AOBG00)、2609.10230 CougarTail、Sentinel-3C、OSR10预告(09-30)、中国海洋发展指数132.3(中新社)、2609.20691 PX4空海两栖、2609.20620 SPAR、2609.10484 HoloOcean
- **09-24（37条·9方向全有）**：j.oceaneng.2026.128219 滑动EOF风浪、s41598-026-70984-7 南极海冰GNN、2609.24591 ECHO海冰修正、2026jh001338 分布感知SWH、engappai.2026.116239 多AUV编队DRL、npg-33-489-2026 相干结构同化、aquaeng.2026.102822 数字孪生渔场、essd-18-6841-2026 全球SWH融合数据集、s41612-026-01531-4 海洋记忆ENSO、s43247-026-03932-y 印度洋跨洋联动、MyOcean Pro v17、oceaneng.2026.128029 内孤立波沉浸式仿真、19475705.2026.2731736 GIS东非TC、17445647.2026.2735222 大加那利海底地貌图、s41597-026-08267-z 挑战者深渊EM124、Niño3.4 3.05℃破纪录(澎湃09-22)、s10596-026-10498-3 GGM异方差UQ、2150704x.2026.2731605 CYGNSS一致性、2609.22574 OcDiffSR、fmars.2026.1934010 原位数据缺口、eurogoos OceanEye联盟(€2.11亿)、hidrografico ABLOS研讨会、1755-0998.70196 eDNA珊瑚全生命之树、qdio内波研讨会(09-18)、oceaneng.2026.128114 双稳态滑翔机、essd-18-6649-2026 CASPROD、bams-d-25-0185.1 业务预报十余年评估、2609.18824 水下数据中心、pci.ecology.100852 PlanktonFlow、mms.70276 Det-LIME、2150704x.2026.2731606 UAV LiDAR海冰厚度、mbmg.10.191426 eDNA MVeM、tethys OCEANS 2026 Monterey
- **已剔除（勿再收）**：OceanParcels v3.1.4、Fugro OCEANITY、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL(>60天)、MBARI MOLA(05-04)、ICE-3D/DenseNet-121、ditto_summit2026、EX2606、Ocean State Report 旧期链接

## 经验教训（勿重复犯）
- **跨期去重**最高频：占位主页 URL 会连续两期重复，须建 URL 池轮换；Nautilus/EX 系列共用总览页须改用具体 news-release 页。
- **日期核实**：聚合站日期 ≠ 发布日（08-03、08-14、09-03 三次教训）；**WebFetch 失败 ≠ 放行**，改 WebSearch 交叉验证。
- **约束必须写进 skill**，不能只留在 automation prompt（07-31 重构丢约束，09-15 修复）。
- **主题盲区**：国内院所新闻、极地/海冰曾漏检，已入 SKILL.md 巡检清单；遗漏项须标「待补录+原始日期+窗口」。
- **用户指定条目与去重冲突**：先核实历史收录，把结论+三选项（不重复／标注更新补录／原样重复）交用户拍板，确认后写"永久归属某期"闭环（09-04 GRSM 案例）。
