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
- **铁律**：综述每条链接必须回查 `library.db` 的 `url`，严禁按 DOI 规则手写（09-20 臆造 2 处；10-11 期 37 链接 0 异常）
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
| **HEAD 返回 404/405 但链接有效** | 部分站禁用 HEAD（10-08：`bluegraph.io` HEAD 405→GET 200；`ecit.cn` HEAD 404→GET 200）→ 批量核链须 **HEAD 失败回退 GET** |
| **臆造 URL** | 严禁凭 URL 模式推断（09-14 自然资源部规则拼出的两条实测 404）；无直链改用权威转载源并标注 |
| **整期批量取稿致跨期重复** | 每个 DOI 尾号单独 grep `posts/`（09-14 JMSE 14(16) 教训） |
| **"已去重"自述不可信** | 跨机接手必须独立复算 URL 集合差与时效差 |
| **聚合站日期 ≠ 发布日** | 本期实测：Voyis 页"Updated Oct 4"实为 09-17 首发（>14 天）；Robosys 页"Updated Oct 1"实为 2026-03（>60 天）→ 一律查原文首发日 |
| Edit 报 File has been modified | 用 Bash 改过同文件后再 Read 一次即可继续 Edit |
| 飞书文档 API 404（token 反复失效） | 每条链路**每期实跑并分别记录**（成功/失败+状态码）；机器人 webhook 正常（StatusCode 0），文档 API token 待苏老师更新，均不阻断发布 |

## 去重基准（最近 3 期；更早一律 `grep -rl posts/`）
> `posts/` 即全量存档，双路 grep 比读基准更可靠。本节仅列「易被再次检索命中」的标识符。
- **10-11（28条·9方向；四/八为2条）**：s41598-026-73332-x 混合Mamba-Transformer水下图像增强、oceaneng.2026.128631 深海采矿履带车自适应NN悬架、cviu.2026.104971 水下深度与表面法线估计、gji/ggag421 Sentinel-2+重力浅水海底地形XGBoost、jastp.2026.106988 海盐气溶胶全球时空预报、edito.eu/ditto-summit EDITO边会、dto-bioflow.eu SUBSIM海底图像分析、edito.eu ssc-2026 社会仿真社区、oceaneng.2026.128641 SA-SRDC-Loc三维水下定位、marine.copernicus.eu product-roadmap MyOcean Pro 3D、paraview-6-2-0、bg-23-7043-2026 HPLC色素精密度、03091333261488345 UAV/USV沿岸水深监测验证、gmd-19-9441-2026 LADDIE v2.0、s40645-026-00851-6 XRF岩芯氧化还原、01431161.2026.2742387 弱监督海水入侵制图、rio.12.e215133 NFDI4Microbiota二期、s44479-026-00009-w 北海生物多样性分子监测、oceandecode.org/?p=24941 UN Ocean Decade数据指南、tianjinwe content_143082_3904097 蛟龙号首赴南太平洋、gmw.cn content_1304574115 蛟龙号466次下潜、163.com L88GJ77O0514R9KQ 57种海洋新物种、sciencenet.cn id=572507 海洋装备绿色智能研讨会、sp-7-osr10-10-2026 GlobColour海洋透明度、eo-1-129-2026 NSIDC海冰漂移南极评估、xcdat v0.11.5、github ioos/compliance-checker、arxiv 2610.02194 SW1D
- **10-08（35条·9方向全有；七/八为3条）**：2025jh000967 SST残差降尺度(JGR:MLC)、eswa.2026.134587 LLM4SST、epsl.2026.120368 全球海山ML、2610.03780 OceanMind多智能体、uri.edu reading-the-oceans-snowflakes 海洋雪AI(NF 70万)、trend.az/casia/4230715 里海数字孪生(IOC/UNESCO)、0131-6184-2026-4-130-139 认知数字海洋(量子+DT+GNN)、bg-23-6879-2026 BGC参数校准、jems.2026.95826 风险感知DT航运、bluegraph.io 三维海况可视化(NOAA 715站)、worldshipping.org digital-global-whale-chart 数字鲸类图谱、prnewswire 302901199 Apaluma Currents、carbonherald ocean-visions mCDR知识平台、essd-18-7269-2026 圣劳伦斯SWOT基准、rse.2026.115706 南极SST Landsat基准、2610.03649 星上异常检测、rs18193406 GNSS/水准大地水准面QC、2610.03888 REACT海洋示踪剂、2610.03759 BridgeCast流匹配、jag.2026.105615 多尺度三维海温反演、2609.34954 SWOT像素云GNN、carbontosea.org oae-data-commons、fmars.2026.1949937 可互操作海深FAIR、data.gov.uk 9fb2372b BGS海洋调查数据、fphy.2026.1941515 科学数据共享博弈、csiro IN2026_V06 P-TROPOE、ecit.cn c7857a144435 大洋97航次B航段、iziran.net aid=5497320 海洋地质七号/九号、essd-18-7345-2026 UVP5、bcssmz.org p=5166 BCSS 8年观测、voiceoftheocean.org baltic-sea-herbarium-1938、lom3.70099 seaEchoTSCalculator、github Project-OSmOSE/OSEkit、pypi copernicusmarine 2.5.0、ohx.2026.e00845 OpenWater Hub
- **10-05（32条·9方向全有；二/三/七/八/九为3条）**：toutiao 7691582336281887259 海洋Token工厂青岛、scienmag 物理约束AI海洋学综述、oceaneng.2026.128177 DB-PINN声场、oceaneng.2026.128408 LLM多AUV、2026ms005751 拉格朗日时序ML(CCN)、motorship 氨燃料船数字孪生(ABS/KSOE/西门子)、hkcrunch Fujitsu海洋数字孪生CEATEC、oceanstream.io OceanStream Globe(EDITO三维)、climatics.kaust IEEE VIS 2026海洋流场可视化(arXiv 2609.37964)、2609.29985 OceanXL水下3DGS、ocecoaman.2026.108379 GIS舟山岛景观、rse.2026.115699 GNSS-R再校准、essd-18-7143-2026 SHELDA、essd-18-7181-2026 MHW-MAD、10106049.2026.2736392 FY-4B SST验证、oceaneconomist NOAA GOMO 8试点、isprsjprs.2026.09.021 IceNest、s40537-026-01562-x AIS+BiGRU、s41598-026-73554-z eDNA北极峡湾、seares.2026.102753 浅水海底分类综述、calcofi.io v2026.10.01、marineinsitu.eu In Situ TAC罗得岛会议、marpol.2026.107294 海湾数据外交、m.mnr.gov.cn t20260930_2939480 第16次北冰洋考察凯旋、qdio.cas.cn t20261001_8289238 科学轮2605、s10040-026-03181-5 Solotvyno盐矿UX-1Neo、marine.copernicus.eu publication-of-10th-ocean-state-report (OSR10正式发布)、sohu 1083114606 广西海洋科学数据中心、hkcd 8778070 2026海博会、zenodo 22095048 ctdam v2.11.0、zenodo 22117941 ioos_code_lab v3.2.3、ocecoaman.2026.108378 HECO溢油工具
- **已剔除（勿再收）**：OceanParcels v3.1.4、Fugro OCEANITY/EDITO（09-08）、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL(>60天)、MBARI MOLA(05-04)、ICE-3D/DenseNet-121、ditto_summit2026、EX2606、EX2607（08-21预告）、南海海洋大数据智能管理平台/南海孪境（09-08）、s43247-026-03899-w 北极原住民框架（09-24）、Ocean State Report 旧期预告页（09-20）、NA182 航次（09-27）、Voyis 船体检测（09-17，>14天）、Robosys VOYAGER 模拟器（原文2026-03）、**arXiv 2609.37964 任务驱动海洋流场可视化（10-05已发）**、**OceanStream Globe / MyOcean Pro v17 / CASPROD / GLODAPv3 / EMSO EVOLVE / OceanEye 联盟（均已发文）**、**rse.2026.115699 GNSS-R 再校准（10-05 已发）**、**essd-18-7253-2026 珠峰气象数据（方向不符）/ earscirev.2026.105719 热带海滩脊（纯古环境）/ 2026gl124090 SWOT 灌溉渠、2026gl124831 北极边界层云（陆地/大气，10-11 未收）**

## 经验教训（勿重复犯）
- **跨期去重**最高频：占位主页 URL 会连续两期重复；Nautilus/EX 系列共用总览页须改用具体 news-release 页
- **日期核实**：聚合站/新闻页日期 ≠ 发布日（08-03、08-14、09-03、**10-05 两次**）；**WebFetch 失败 ≠ 放行**，改 WebSearch/Crossref 交叉验证
- **约束必须写进 skill**，不能只留在 automation prompt（07-31 重构丢约束，09-15 修复）
- **主题盲区**：国内院所新闻、极地/海冰曾漏检，已入 SKILL.md 巡检清单
- **用户指定条目与去重冲突**：先核实历史收录，把结论+三选项交用户拍板，确认后写"永久归属某期"闭环（09-04 GRSM 案例）
- **"预告"与"正式发布"可视为两次事件**：09-20 预告 OSR10 → 10-05 正式发布+结论，判为新进展并标注
- **连跑多步发布链路须逐步核验**：git 复合命令中任一环返回非零会静默中断后续（本期 pull --rebase 与 commit 各中断一次），收尾必查 `HEAD == origin/main`
