# 海洋AI研究日报系统记忆

## 系统配置
- **用户**：苏老师 · **自动化ID**：`ai`（`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）
- **仓库**：https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（`SECTIONS=[...]`，由 `build_daily_YYYYMMDD.py` repr 正则替换）；**HTML**：`gen_html_YYYYMMDD.py`（自包含，`ast.literal_eval` 解析，禁止 import feishu）；**发布**：`publish_YYYYMMDD.py`（幂等，含跨月自动建 archive 分组）；**L3 看板外壳**：`gen_frontier.py`（2026-10-05 补建，读 `pool_index.json` 幂等生成 `frontier.html`）
- **本机 Python**：默认 `python` 缺 requests，飞书/机器人/校验脚本用 **`py -3`**；链接实测用系统 `Python313\python.exe`

## 前沿跟踪四层架构（2026-09-20 落地）
- **L0** `harvest.py` → `data/pool/YYYY-MM-DD.jsonl`（9 方向 × OpenAlex 期刊 + arXiv 预印本通道 + 会议）；**L1** `screen.py`+`tier_engine.py` → `data/library.db` + `data/pool_index.json`；**L2** 日报；**L3** `frontier.html`（外壳由 `gen_frontier.py` 生成）+ `weekly_report.py` → `weekly/YYYY-Www.html` + `weekly/index.html` + `weekly/synth/*.draft.md`
- **跨机复用池（2026-10-05 苏老师要求）**：`.gitignore` 仅忽略 `data/pool/_*.jsonl`（备份/临时），**正式池文件 `data/pool/YYYY-MM-DD.jsonl` 入库**；`data/library.db` 仍不入库（可由池 jsonl 重建）。另一台机器 `git pull` 后即可复算池与看板，无需重新采集
- **周报两层综述**：① 自动综述（脚本，主题簇+代表文献+期刊）；② 深度综述（写 `weekly/synth/YYYY-Www.md` 后重跑脚本自动注入）。综述样本＝池内剔除 D 级预警刊 + 「已降权」项（剔除数单列、不删除）
- **周报入口三处**：`index.html`/`archive.html`/`frontier.html` 导航「前沿周报」→ `weekly/index.html`；首页 `</header>` 与 `<main>` 间横幅卡片
- **周报触发**：当日为周日，**或距上期 ≥7 天**（2026-10-05 实测：距 09-27 已 8 天 → 触发；`--end` 取运行当日，ISO 周为标签，W40 因 10-04 未跑而跳过，14 天窗口已完整覆盖）
- **铁律**：综述每条链接必须回查 `library.db` 的 `url`，严禁按 DOI 规则手写（09-20 臆造 2 处；本期 27 链接 0 异常）
- **每期必报**：采集量 / 池内量 / 日报收录 / 留存率 / **arXiv 占比 ≤50%** / **期刊占比 ≥40%** / 零覆盖来源组 ≤6
- **L1 打分**＝期刊权重（S6/A5/B4/C3/P2.5/D1）×100 + 相关度×8 + 时效 + 海洋契合度
  - **海洋「对象」vs「介质」**：`ocean/marine/coastal/bathymetry/seabed/fisheries/Arctic…`＝研究海洋；`seawater/water/wave/polar/tide` **+** `catalyst/battery/clinical/crop/hydrogel…`＝**用海非研究海** → 判 `off` 降权 −150（不删除，看板可切"仅被降权项"复核）

## 期刊分级口径（2026-09-20 苏老师拍板）
- **S** Nature/Science/PNAS 正刊及顶级子刊；**A** 领域权威（AGU/Copernicus/IEEE/Elsevier 顶刊；Scientific Reports、Ocean Engineering、npj Heritage Science 确认归 A）；**B** 主流 SCI / 中文刊学科前 25%（海洋学报、遥感学报）；**C** 一般刊·集团刊（Frontiers 全集团、PLOS ONE、Heliyon；海洋科学、中国海洋大学学报、热带海洋学报）；**D** 预警/受限（MDPI 全集团、Hindawi、中科院/中信所预警、SCI(SCIE)/EI 剔除）→ 强制置底标注、不删除
- **P 预印本**：若已对应期刊论文则**按所属期刊等级排序**，保留"预印本"标注；匹配 ① 同 DOI ② 同标题指纹 ③ `journal_ref` ④ OpenAlex `locations`
- 判定顺序：预印本升级 → 登记表 → 最新一期预警/剔除名单（支持 ISSN）→ 集团规则 → 指标自动评级 → 待确认
- **自动评级阈值**：A `h≥120` 或 `h≥70 且 c≥3.0`；B `h≥50` 或 `h≥30 且 c≥2.0` 或 `c≥4.0`；C `h≥8` 或 `c≥0.5`（巨型刊 `年发文>2500 且 c<8` 降一级）
- 名单**不累积**（移出即失效），存 `data/journal_tiers.json` 的 `warning_lists`（`active` 控制）；已录：中科院2025(5)、中信所2025(14)、EI剔除2026(19/228)、WoS剔除2026(SCIE/SSCI 16)
- 出版方别名：MDPI 全称 `Multidisciplinary Digital Publishing Institute`、Hindawi Limited、Frontiers Media SA
- **问答式校准**：未登记刊 → `data/pending_journals.txt`，只挑 ≥2 篇的向苏老师提问

## 一致性机制（手动=自动，铁律）
- `ocean-daily-report` skill 是唯一权威源，自动化 prompt 纯委托该 skill；prompt 只保留流程骨架
- 每次执行必须产出相同工件：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 更新本文件去重基准 + 追加 `.workbuddy/automations/ai/memory.md`
- **跨机器**：记忆随仓库入库；skill 用 `sync_skills.py`（install=仓库→用户，collect=反向，status=比对）。执行前 `git pull`+`install`，执行后 `push`，禁同日并行

## 执行流程（6 阶段）
```
阶段0  git pull origin main + sync_skills.py install（+ status 比对）
阶段1  顶会/IEEE 强制检索（23 会议 + IEEE 期刊，≥5 条，其中 ≥2 条须来自会议或 IEEE 期刊）
阶段1B 国内院所新闻巡检（海洋所/南海所/深海所/极地中心）+ 顶级期刊综述检查
阶段2  先跑 harvest.py + screen.py 取全量池，再 9 方向检索 + 来源覆盖矩阵逐组打卡 + 去重
阶段3  build_daily → 归类自检 → gen_html（改 TODAY/TODAY_CN/**星期**/日期范围/页脚来源）
阶段4  posts/ + index.html + archive.html + commit + push；飞书文档 + 机器人（不阻断）；
       第7步 前沿周报（周日或距上期≥7天）：读 draft → 写 synth md → 链接核验须 0 异常 → 重跑注入 → push
       第8步 L3 看板外壳：py -3 gen_frontier.py（读 pool_index.json 幂等重生成 frontier.html）
阶段5  五审：链接+摘要一致性 / 时效 / 来源覆盖 / 归类与条数 / 去重
阶段6  写日志 + 滚动本文件去重基准 + 追加 automations 摘要
```
- **规模时效**：每方向 **3-5 条**、全日报 **27-45 条**（确无内容可为 0，不凑数）；**≤14 天**，近 7 天为同方向排序优先权（非硬门槛）

## 内容质量规则（完整版以 skill `references/quality_standards.md` 为准）
1. 时效 ≤14 天；14–60 天须重要性豁免；>60 天删除（**arXiv 以 v1 提交日为准**）
2. 每条 URL 必须实测可访问；反爬 403 ≠ 死链，用 `verify_paper.py`（Crossref+OpenAlex）核实
3. 工具版本须从官方 release notes 核实；摘要须自原文提取，不得据标题推断、不得张冠李戴
4. **发布前必须双路 grep `posts/` 跨期去重**（① URL 集合差 ② 标题关键词 + DOI 尾号）
5. 方向归类按内容判断；同 URL 只在一个方向；主页新闻须给具体链接（禁指首页）
6. **来源覆盖矩阵逐组打卡**，零覆盖 >6 组视为检索不足须补检

## 常见故障处理
| 问题 | 解决方案 |
|------|---------|
| git push TLS/代理失败 | `unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` 后 `git -c http.proxy= -c https.proxy= push origin main` |
| git push 超时/reset | 重试 3–5 次；Windows 下 push 需 Bash + `dangerouslyDisableSandbox: true` |
| **push 报 `hostkeys_foreach failed for ~/.ssh/known_hosts: Permission denied` / `Host key verification failed`** | 沙箱拦截 `~/.ssh` 读取（非仓库问题）→ 必须 `dangerouslyDisableSandbox: true` 并让苏老师放行；放行后即可推 |
| **首次纳入池文件后 push 变慢** | `git add -A` 现含 `data/pool/*.jsonl`（约 22 MB / 5 文件）；属正常，勿中断 |
| git commit 身份 | 仓库级 `user.name=tianyunsu` / `user.email=tianyunsu@users.noreply.github.com` |
| **pull --rebase 因未暂存改动失败** | `screen.py` 会改 `data/journal_tiers.json`/`pending_journals.txt`；**先 `git add -A` 再 rebase/push** |
| **`git add` 后 commit 报 "nothing to commit" 但提交已生成** | 若上一步返回非零会短路 push；**须单独核对 `git rev-parse HEAD` vs `origin/main` 并补推** |
| urllib 403（MDPI/ScienceDirect/Wiley/AGU/T&F） | 反爬≠死链，用 `verify_paper.py` 核实；无 DOI 时 WebFetch 二次确认 |
| urllib 502 "Tunnel connection failed"（zenodo 等） | **沙箱代理异常非死链**，改用 WebFetch 复核 |
| arXiv export API 406/429 | 端点级 WAF；`harvest.py` 双通道（官方 API + OpenAlex `locations.source.id:S4306400194`），互为备份 |
| arXiv 老文伪新稿 | 高 arXiv ID ≠ 新成果，必查 v1 提交日（09-04 HorizonNet 实为 2018 旧文） |
| **present_files 预览污染本地 HTML** | 注入 `data-page-node-id`；**先 commit+push 再 present**，present 后 `git status` 复查，变脏即 `git checkout --` |
| 转载站大陆不可访问 | Yahoo/MSN 类返回"服务不可访问"=死链；选原始媒体并核对日期是否为索引日 |
| urllib 200 但是挑战页 | title 为 "Client Challenge" = 反爬页，须 WebFetch 二次确认 |
| **臆造 URL** | 严禁凭 URL 模式推断（09-14 自然资源部规则拼出的两条实测 404）；无直链改用权威转载源并标注 |
| **整期批量取稿致跨期重复** | 每个 DOI 尾号单独 grep `posts/`（09-14 JMSE 14(16) 教训） |
| **"已去重"自述不可信** | 跨机接手必须独立复算 URL 集合差与时效差 |
| **聚合站日期 ≠ 发布日** | 本期实测：Voyis 页"Updated Oct 4"实为 09-17 首发（>14 天）；Robosys 页"Updated Oct 1"实为 2026-03（>60 天）→ 一律查原文首发日 |
| Edit 报 File has been modified | 用 Bash 改过同文件后再 Read 一次即可继续 Edit |
| 飞书文档 API 404（token 反复失效） | 每条链路**每期实跑并分别记录**（成功/失败+状态码）；机器人 webhook 正常（StatusCode 0），文档 API token 待苏老师更新，均不阻断发布 |

## 去重基准（最近 3 期；更早一律 `grep -rl posts/`）
> `posts/` 即全量存档，双路 grep 比读基准更可靠。本节仅列「易被再次检索命中」的标识符。
- **10-05（32条·9方向全有；二/三/七/八/九为3条）**：toutiao 7691582336281887259 海洋Token工厂青岛、scienmag 物理约束AI海洋学综述、oceaneng.2026.128177 DB-PINN声场、oceaneng.2026.128408 LLM多AUV、2026ms005751 拉格朗日时序ML(CCN)、motorship 氨燃料船数字孪生(ABS/KSOE/西门子)、hkcrunch Fujitsu海洋数字孪生CEATEC、oceanstream.io OceanStream Globe(EDITO三维)、climatics.kaust IEEE VIS 2026海洋流场可视化、2609.29985 OceanXL水下3DGS、ocecoaman.2026.108379 GIS舟山岛景观、rse.2026.115699 GNSS-R再校准、essd-18-7143-2026 SHELDA、essd-18-7181-2026 MHW-MAD、10106049.2026.2736392 FY-4B SST验证、oceaneconomist NOAA GOMO 8试点、isprsjprs.2026.09.021 IceNest、s40537-026-01562-x AIS+BiGRU、s41598-026-73554-z eDNA北极峡湾、seares.2026.102753 浅水海底分类综述、calcofi.io v2026.10.01、marineinsitu.eu In Situ TAC罗得岛会议、marpol.2026.107294 海湾数据外交、m.mnr.gov.cn t20260930_2939480 第16次北冰洋考察凯旋、qdio.cas.cn t20261001_8289238 科学轮2605、s10040-026-03181-5 Solotvyno盐矿UX-1Neo、marine.copernicus.eu publication-of-10th-ocean-state-report (OSR10正式发布)、sohu 1083114606 广西海洋科学数据中心、hkcd 8778070 2026海博会、zenodo 22095048 ctdam v2.11.0、zenodo 22117941 ioos_code_lab v3.2.3、ocecoaman.2026.108378 HECO溢油工具
- **09-30（34条·9方向全有；二/三/八为3条）**：robot.tongji.edu.cn/info/1253/2999 NeurIPS2026同济3篇、2609.10855 VLM沿海评测(OCEANS2026 Monterey)、oceaneng.2026.128340 Wind-GeoDiff南海SWH、s41598-026-72013-z DDSF-UNet、env.70148 浮游植物MoE、ss.dlut.edu.cn/1571/34962 北溟灵枢云脑工场、apor.2026.105280 亚中尺度降尺度、shipuniverse JNPA港口数字孪生、PANGAEA.997175 AWI Basemap2026、fmars.2026.1893781 沿海韧性三维框架、iziran.net/news.html?aid=5493085 广东近海海底调查、s41597-026-08345-2 SRAD、s41597-026-08254-4 UCOD、data.gov RSS SMAP L2C SSS V6.0、s26185873 近岸浮标QA、01621459.2026.2739444 JASA三维涡流重建、s44288-026-00736-7 插值法对比、fmars.2026.1951665 东海pCO2 ML重建、jtech-d-25-0110.1 HF雷达表面流、5radar.com/dataproperty 中科知道产权登记、cctv 数据产权登记系统上线、sohu 1080778686 AASTMT+CGOF1.0、nmdis.org.cn 85915 陆海垂直基准案例集、fatopaulista The Gap罗曼什断裂带、oceaneconomist Falkor(too) pCO2、toutiao 7686861881620955698 中-海管局深海科研项目、s41598-026-72152-3 仿生水下机器人、shantou.gov.cn post_2571736 海兰云汕头海底数据中心、toutiao 7688387875678831104 广东AI大会(临港PUE)、splash247 Fugro新加坡数字孪生枢纽、cstar-ocean 0.14.1、regional-mom6 1.0.3、cstar-forge 0.9.0、2041-210x.70406 bacpipe
- **09-27（27条·四1/八1/九2 为池内自然分布）**：jpo-d-26-0131.1 海浪学习黑箱、oceaneng.2026.127974 Cummins PINN、2609.12826 CoralscapesV2、s00300-026-03548-0 环斑海豹CV、2609.30214 C3-JEPA、os-22-2915-2026 LORA-QG、os-22-2691-2026 AABW、apor.2026.105259 地中海波浪能偏差、cexr.2026.100181 VR海豹、jet-04-2026-0032 神经多样性VR、2609.08386 鲨鱼可视化、ica-abs-12-50-2026 ICA三维海洋、ocemod.2026.102825 ROMS大堡礁、os-22-2673-2026 GMSL风订正、rse.2026.115684 VIIRS夜间云、2609.25271 侧扫闭式约束、2609.27712 FP-MUSIC、apor.2026.105271 波浪再分析ML后验、rol.2026.33 EMODnet Ingestion、fmars.2026.1894836 公民科学集成、sio.org.cn/a/snyw/23338.html ISO TC8 SC13、nautiluslive.org/cruise/NA182、01490419.2026.2726371 北海船测重力、fmars.2026.1898407 哥伦比亚ADCP、palaeo.2026.114210 南海全新世海平面DB、gmd-19-8349-2026 SeapoPym、f1000research.190102.1 TOS²CA
- **已剔除（勿再收）**：OceanParcels v3.1.4、Fugro OCEANITY/EDITO（09-08）、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL(>60天)、MBARI MOLA(05-04)、ICE-3D/DenseNet-121、ditto_summit2026、EX2606、EX2607（08-21预告）、南海海洋大数据智能管理平台/南海孪境（09-08）、s43247-026-03899-w 北极原住民框架（09-24）、Ocean State Report 旧期预告页（09-20）、NA182 航次（09-27）、Voyis 船体检测（09-17，>14天）、Robosys VOYAGER 模拟器（原文2026-03）

## 经验教训（勿重复犯）
- **跨期去重**最高频：占位主页 URL 会连续两期重复；Nautilus/EX 系列共用总览页须改用具体 news-release 页
- **日期核实**：聚合站/新闻页日期 ≠ 发布日（08-03、08-14、09-03、**10-05 两次**）；**WebFetch 失败 ≠ 放行**，改 WebSearch/Crossref 交叉验证
- **约束必须写进 skill**，不能只留在 automation prompt（07-31 重构丢约束，09-15 修复）
- **主题盲区**：国内院所新闻、极地/海冰曾漏检，已入 SKILL.md 巡检清单
- **用户指定条目与去重冲突**：先核实历史收录，把结论+三选项交用户拍板，确认后写"永久归属某期"闭环（09-04 GRSM 案例）
- **"预告"与"正式发布"可视为两次事件**：09-20 预告 OSR10 → 10-05 正式发布+结论，判为新进展并标注
- **连跑多步发布链路须逐步核验**：git 复合命令中任一环返回非零会静默中断后续（本期 pull --rebase 与 commit 各中断一次），收尾必查 `HEAD == origin/main`
