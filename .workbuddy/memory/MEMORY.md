# 海洋AI研究日报系统记忆

## 系统配置
- **用户**：苏老师 · **自动化ID**：`ai`（`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）
- **GitHub**：https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（含 `SECTIONS=[...]`），由 `build_daily_YYYYMMDD.py` 正则替换；`GH_REPO`=仓库根目录；用系统 PATH 的 `python`
- **HTML 生成器**：`gen_html_YYYYMMDD.py`（自包含，`ast.literal_eval` 解析 SECTIONS，禁止 import feishu 模块）

## 一致性机制（手动=自动，铁律）
- `ocean-daily-report` skill 是手动/自动共用唯一权威源，自动化 prompt 纯委托该 skill。
- 每次执行（无论手动/自动）必须产出相同工件：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 更新本文件去重基准 + 追加 `automations/ai/memory.md`。
- 通用方法论 skill `automation-consistency`（用户级）沉淀「诊断断层→改铁律→纯委托→补日志」。

## 跨机器执行机制
- 记忆随仓库（`.workbuddy/memory/`、`automations/` 纳入 git）；skill 用 `sync_skills.py` 双向同步（install=仓库→用户目录，collect=反向，status=比对）。
- 铁律：①执行前 `git pull origin main` + `sync_skills.py install`；②执行后 `git push origin main`；③禁同日并行；④非主力机改 skill 须 collect 后 push。新机器见 `SETUP_NEW_MACHINE.md`。

## 执行流程（6 阶段，GitHub Pages + 飞书 双发布）
```
阶段0  git pull origin main + sync_skills.py install（跨机器同步；禁同日并行）
阶段1  顶会论文检索(23会议+IEEE期刊,≥5条强制,不可跳过)
阶段1B 国内院所新闻巡检(海洋所/南海所/深海所/青大/南科大等) + 顶级期刊综述检查(GRSM/RSE等)
阶段2  9方向常规检索 + 来源覆盖矩阵逐组打卡(A组9组+B组+阶段一)，建去重黑名单(近12期)
阶段3  build_daily_XXX.py写SECTIONS + 归类自检(写入前) + gen_html_XXX.py生成HTML
阶段4  复制posts/ + 更新index.html/archive.html + commit + push
阶段4.5 飞书推送 feishu_write_doc.py（推文档）+ run_daily_report.py（机器人通知，需 $env:PYTHONUTF8=1）
阶段5  五项审查：链接+摘要一致性 / 时效 / 来源覆盖 / 归类与条数 / 去重
阶段6  写YYYY-MM-DD.md日志 + 更新本文件去重基准 + 追加automations/ai/memory.md
```

**规模与时效口径（2026-09-15 用户拍板，已写入 skill）**：每方向 **3-5 条**，全日报 **27-45 条**（某方向确无新内容可为 0，不凑数）；时效维持 **≤14 天**，**近 7 天作为同方向内排序优先权重**（非硬门槛）。
飞书推送失败（API 超时/404）**不阻断发布**，如实记日志即可；未配置 `FEISHU_WEBHOOK_URL` 时机器人通知自动跳过。

## 内容质量规则（必须遵守）
1. 近7天优先；14–60天需豁免；>60天一律删除（arXiv 以 v1 首次提交日为准，不以聚合站索引日）。
2. 每条 URL 必须实测可访问（WebFetch/urllib 200），404/403/超时一律不收录（反爬 403 见故障表）。
3. 工具版本特性必须从官方 release notes 核实，不得推断。
4. 摘要必须从原文提取，不得据标题推断。
4b. **date 字段以实测发布/更新时间为准**；聚合站（PulseAugur/PubScholar/Google）显示的是索引日而非发布日。
4c. **发布前必须 `grep -rl` 核查 `posts/` 跨期去重**（最高频事故点，08-26 曾 7 处重复）。
5. 方向归类按文章内容判断，不按来源机构功能。
6. 跨方向去重：同 URL 只能出现在一个方向。
7. 主页新闻必须找具体链接，不得用机构主页 URL。
8. 9方向严格定义：一海洋AI（AI/ML/DL用于海洋预报·观测·生态）；二数字孪生（须是海洋数字孪生本身：架构/框架/案例/会议）；三可视化（方法/工具/平台/Dashboard/GIS）；四数据质量（QA/QC/异常检测，不含测绘进展·数据量统计）；五数据处理（再处理/融合/插值/重采样，不含软件发布→九）；六数据管理与共享（政策/FAIR/元数据标准/开放政策）；七开放航次与科考（航次/调查船/潜水器/无人船/海洋装备）；八海洋数据中心（NCEI/PANGAEA/CMEMS等仓储档案馆，不含IT基础设施·纯物理海洋学）；九工具与代码资源（仅软件新版本发布）。硬件装备→七；评估报告→八或三；同一软件不同URL只归九。**宁可某方向为空（写明"暂无新增"）也不凑数**。
9. 发布前分类自检：①核心主题符不符合方向定义 ②是否因内容不足被迫归入 ③是否已出现在其他方向 ④"海底数据中心"是否IT基础设施 ⑤综合期刊论文是否按内容归类。
   - **完整判定表**（9 行"可收录/禁止归入" + 6 条关键规则）**已迁入 skill**：`references/quality_standards.md` 的「方向归类严格规则」；第 8/9 条为本文件的历史简版，以 skill 为准。
10. **摘要一致性（09-15 起阶段五必查）**：摘要须准确反映原文核心观点，关键数字（精度/分辨率/样本量/天数/金额/坐标）、方法名、机构名、人名、时间点必须能在原文找到出处；批量导入时**不得张冠李戴**（把相邻条目的事实串入他条）。无法核实的表述须改写或剔除。
11. **规模**：每方向 3-5 条、全日报 27-45 条；某方向确无新内容可为 0。
12. **来源覆盖**：每期必须按 skill 的「来源覆盖矩阵」逐组打卡（A 组 9 类 + B 组出版商 + 阶段一 23 会议/IEEE 期刊），零覆盖组写入日志并归因；**零覆盖超过 6 组视为检索不足，须当场补检**。
    > 历史教训：2026-07-31「纯委托」重构丢失该整节约束，导致 7/31–9/15 约 12 期长尾来源零覆盖——IEEE Xplore 近 14 期 **0 次命中**，27 组来源中 11 组为零。迁移类改造必须逐条 diff 原约束清单（见 SKILL.md 陷阱 14）。

## 来源覆盖矩阵（2026-09-15 恢复，阶段二强制项）
- **起因**：原 prompt 的「检索来源（每次执行必须全覆盖）」条款在 2026-07-31「纯委托」重构时**未迁入 SKILL.md**，导致此后连续 12 期仅覆盖 5 类来源（arXiv/MDPI/CMEMS/NOAA/国内政府），ACS/DOAJ/ProQuest/RSC/SAGE/T&F/IOP/ACM 命中为 0。
- **A 组（可直接检索）**：arXiv/EarthArXiv/ESSOAr、Scholar/OpenAlex/SemanticScholar/Crossref、DOAJ、Copernicus(EGU)/Springer Nature/Frontiers/MDPI、CNKI/万方/维普、GitHub/PyPI/conda/DockerHub、CMEMS/NOAA/PANGAEA/Argo/SeaDataNet/IODE/SEANOE、W3C/ISO/OGC/CF/RDA/OBP、中文科技媒体与国际媒体。
- **B 组（403 反爬，须走官方 API+二次确认）**：Elsevier/ScienceDirect、Wiley/AGU、IEEE Xplore、T&F、SAGE、ACS、RSC、Science/AAAS、ACM DL、IOP。
- **C 组（阶段五自检）**：逐组核对命中情况，零命中组须如实记录原因；**矩阵要求「逐组检索」而非「逐组必有产出」，严禁凑覆盖**。
- 详见 SKILL.md 陷阱 14（重构静默丢约束）、陷阱 15（skill 双副本漂移）。

## GitHub Pages 架构
- main 分支：源码+每日日报（posts/、index.html、archive.html）；supplement 分支：另一台机器结果（无需本地拉取）；gh-pages：Actions 自动部署（勿手编）。
- 每次生成后必须**同时**更新 index.html 和 archive.html（post-excerpt 是硬编码文本，删改条目后两处都要同步）。

## 常见故障处理
| 问题 | 解决方案 |
|------|---------|
| git push TLS错误 | `git config --unset http.sslbackend` |
| git push 代理拦截 | `git config --global --unset http.proxy && git push origin main` |
| git push 127.0.0.1:65532失败 | `unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` 后 `git -c http.proxy= -c https.proxy= push origin main` |
| git push 443超时/reset | GitHub 直连不稳，循环重试 3–5 次（Git Bash 无 sleep，勿放循环内）；SSH 无 publickey 不可用；Windows 下 push 需 `dangerouslyDisableSandbox: true` |
| git commit 无法识别身份 | 仓库级 `git config user.name "tianyunsu" && git config user.email "tianyunsu@users.noreply.github.com"` |
| Python urllib 出网被拒(WinError 10061) | 沙箱阻断 Python 直连外网；链接校验改用 WebFetch 工具，勿写探测脚本 |
| urllib 返回 403（MDPI/ScienceDirect/Wiley 等） | Cloudflare 反爬，非死链，不得直接剔除。**首选 `verify_paper.py`（Crossref+OpenAlex 官方 API）核实元数据**，不受 403 影响且更快更准；无 DOI 时再用 WebFetch 二次确认 |
| arXiv 老文补登伪新稿 | 高 arXiv ID ≠ 新成果，必查 v1 提交日与原文年份（09-04 剔除 HorizonNet 2608.30471，实为 2018 旧文） |
| **present_files 预览污染本地 HTML** | 预览本地 .html 会被注入 `data-page-node-id="..."`。**铁律：先 commit+push 再 present；present 后 `git status` 复查，变脏立即 `git checkout --` 还原**（线上已干净） |
| **转载站在大陆不可访问** | Yahoo/Yahoo News 自 2021-11-01 起对大陆返回"服务不可访问"页 = 死链。**选源优先原始媒体**；遇 Yahoo/MSN 类转载须回溯首发来源并核对其日期是否为索引日 |
| urllib 命中但内容是挑战页 | PyPI 等返回 200 但 title 为 "Client Challenge" = 反爬挑战页，≠ 内容有效。须 WebFetch 二次确认包存在、版本与发布日期 |
| **臆造 URL（按模式猜测）** | **严禁凭 URL 模式推断链接**。09-14 两条按自然资源部 URL 规则拼出的 `mnr.gov.cn/...2830895/2830896.html` 实测均 404 且站内无此稿。无直链时改用可访问权威转载源并如实标注来源 |
| **批量抓同一期刊整期致跨期重复** | 09-14 从 JMSE 14(16) 取 1453/1462，**分别已在 08-18 与 08-10 收录**。**铁律：整期批量取稿时每个 DOI 尾号单独 grep `posts/`**，不能只对新取 URL 做集合比对 |
| **"已去重"自述不可信** | 另一台机器 09-14 日志自称"无重复""全部≤14天"，实测两项均不成立。**铁律：跨机接手必须独立复算 URL 集合差与时效差，不采信对方结论** |
| Edit 报 File has been modified | 用 Bash 改过同文件后，再 Read 一次即可继续 Edit |
| 飞书链路（长期不可用，可跳过） | `run_daily_report.py` 需 `$env:PYTHONUTF8=1`；`deploy_report.py` 卡住则手动复制 HTML→posts/ 再 push；docx blocks 404 疑 app token 缺权限 |

## 去重基准（只留最近 5 期；更早一律 `grep -rl posts/`）
> `posts/` 即全量存档，规则 4c 的 grep 比读基准更可靠。本节仅列「易被再次检索命中」的标识符。

- **09-07（15条+2备注[D2/D3空]）**：MHWCorrNet(南海所,JGR:MLC)、2608.29347、2609.03382 SurgeGen、EchoST-SSL(水科院)、su18178986、PhyEnv-GAN、S-DEIM、卫星岸线(Comm.Earth&Env)、西班牙MITECO战略、NSF OOIFB、BGC-Argo资金(KPBS)、OSIL浮标、coops-mcp 0.1.1
- **09-08（13条+2备注[D3/D4空]）**：NWM混合海浪(中山大学)、2609.04411 AquaBEV、SEMI-DETR白鲸、2609.04635、Fugro OCEANITY、A-Predator(RS3035)、JMSE14(17)1657、EMODnet392万欧元招标、雪龙2号浮标、极地数据中心开放课题、南海大数据平台、2609.02605 Mini-Girona、2609.03207水声信道库
- **09-09（13条+1备注[D2空]）**：Neptune(2609.08606,CMCC)、"丝路海运"北极气象导航+港口气象智能体、2609.07399 SKANN、2609.06261、2609.06253 DARB、Water18(17)2209、2609.02996 GNN海图、2609.07998 DQN、CORD、深海一号+蛟龙、2609.08241、cstar-ocean 0.13.5
- **09-14（16条+1备注[D9空]）**：2609.11230 KiloDA、Ocean-E2E(KDD,清华SAIL)、2609.10920 HFR、2609.10564、2609.09247、EMODnet→EDITO同步、WakeAtlas、Sentinel-6B、CFOSAT SWIM三代、RS3003 MG-GCNN、UN海洋十年指南、EMODnet Biology底拖网、向阳红18、向阳红10西太热液区、雪龙2号破冰引航、NOAA SOUP
- **09-15（16条，9方向全有）**：2609.15676 MambaMPD、2609.15484 CatchMonitor、LeadNet泛北极冰间水道(qdio)、DISCUSS深海微生物数字孪生(科学网/Nature Sensors)、DTO-BioFlow、CCGS Amundsen门户、SST强迫静默切换(Climate Dynamics)、韩国东岸冷水(10.1029/2026JC024312)、Med-CORDEX(os-22-2725-2026)、FAIR海洋空间数据(npj Ocean Sust)、E-ODP研讨会、中俄北冰洋走航科考(网易转载)、CMEMS WAV-305、Parcels v4.0、hydrolib-core、oceanval
- **已剔除（勿再收）**：OceanParcels v3.1.4、Fugro OCEANITY、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL(>60天)、MBARI MOLA(原发05-04)

## 经验教训（勿重复犯）
- **跨期去重**：最高频事故。占位主页 URL 连续两期重复会触发去重，应建 URL 池轮换；Nautilus/EX 系列共用总览页须改用具体 news-release 页。
- **日期核实**：聚合站日期 ≠ 发布日，必须 WebFetch/API 核实原文（08-03、08-14、09-03 三次教训）。
- **WebFetch 失败 ≠ 放行**：改 WebSearch 交叉验证（09-03 据此拦截一条 3 月旧航次）。
- **来源覆盖**：约束必须写进 skill，不能只留在 automation prompt（07-31 重构丢约束，09-15 修复）。
- **主题盲区**：国内院所新闻、极地/海冰主题曾漏检，已写入 SKILL.md 巡检清单；遗漏项须在 MEMORY.md 标注「待补录+原始日期+窗口」形成闭环。
- **用户指定条目与去重冲突**：先核实历史收录（grep posts/ + 查原文是否新进展），把结论+三个选项（不重复／标注更新补录／原样重复）交用户拍板；确认后写入「永久归属某期」闭环（09-04 GRSM 案例）。
