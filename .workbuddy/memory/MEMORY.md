# 海洋AI研究日报系统记忆

## 系统配置
- **用户**：苏老师 · **自动化ID**：`ai`（`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）
- **仓库**：https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（`SECTIONS` 由 `build_daily_YYYYMMDD.py` repr 正则替换）；**HTML**：`gen_html_YYYYMMDD.py`（自包含，`ast.literal_eval`）；**发布**：`posts/YYYY-MM-DD.html` + `index.html` + `archive.html` + git push；**L3**：`gen_frontier.py` + `weekly_report.py`
- **本机 Python**：`py -3`（飞书/机器人/校验）；系统 `Python313\python.exe`（链接实测）

## 前沿跟踪四层架构（2026-09-20）
- **L0** `harvest.py` → `data/pool/YYYY-MM-DD.jsonl`；**L1** `screen.py`+`tier_engine.py` → `data/library.db` + `data/pool_index.json`；**L2** 日报；**L3** `frontier.html` + `weekly/YYYY-Www.html`
- **跨机复用池**：正式池文件 `data/pool/YYYY-MM-DD.jsonl` 入库（`.gitignore` 仅忽略 `_*.jsonl`）；`library.db` 不入库
- **周报触发**：周日或距上期 ≥7 天；`--end` 取运行当日，ISO 周标签
- **铁律**：综述链接必须回查 `library.db.url`；零覆盖来源组 ≤6；arXiv 占比 ≤50%；期刊占比 ≥40%
- **L1 打分**＝期刊权重（S6/A5/B4/C3/P2.5/D1）×100 + 相关度×8 + 时效 + 海洋契合度
  - **对象 vs 介质**：`ocean/marine/coastal/bathymetry/seabed/fisheries/Arctic…`＝研究海洋；`seawater/water/wave/polar/tide + catalyst/battery/clinical/crop/hydrogel…`＝用海非研究海 → 判 `off` 降权 −150

## 期刊分级口径
- **S** Nature/Science/PNAS 正刊及顶级子刊；**A** AGU/Copernicus/IEEE/Elsevier 顶刊、Sci Rep、Ocean Engineering；**B** 主流 SCI / 中文前25%；**C** Frontiers/PLOS/Heliyon 集团刊；**D** MDPI/Hindawi/预警剔除刊 → 置底标注
- **P 预印本**：已对应期刊则按期刊等级；匹配 DOI/标题/journal_ref/OpenAlex locations
- **判定顺序**：预印本升级 → 登记表 → 最新预警/剔除名单 → 集团规则 → 指标自动评级 → 待确认
- **阈值**：A h≥120 或 h≥70&c≥3；B h≥50 或 h≥30&c≥2 或 c≥4；C h≥8 或 c≥0.5
- **已录预警名单**：中科院2025(5)、中信所2025(14)、EI剔除2026(19/228)、WoS剔除2026(16)

## 一致性机制
- `ocean-daily-report` skill 是唯一权威源，prompt 纯委托
- 每次产出：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 滚动本文件 + 追加 `automations/ai/memory.md`
- 执行前 `git pull`+`sync_skills.py install`；执行后 `push`；禁同日并行

## 执行流程
`阶段0 git pull+sync` → `阶段1 顶会/IEEE` → `阶段2 harvest+screen+来源矩阵` → `阶段3 build_daily+gen_html` → `阶段4 发布+飞书/机器人+周报/看板` → `阶段5 五审` → `阶段6 记忆写入`
- 规模：每方向 3–5 条，合计 27–45；某方向确无新内容可为 0，不凑数；≤14 天，近 7 天优先

## 内容质量规则
1. ≤14 天；14–60 天须豁免；>60 天删除（arXiv 以 v1 提交日为准）
2. 每条 URL 实测可访问；反爬 403 用 `verify_paper.py`（Crossref+OpenAlex）
3. 工具版本须官方 release notes 核实；摘要自原文提取，不据标题推断
4. 双路 grep `posts/` 跨期去重：URL 集合差 + 标题/DOI/卷期号
5. 方向归类按内容；同 URL 只在一个方向；主页新闻须给具体链接
6. 来源矩阵逐组打卡，零覆盖 >6 组须补检

## 常见故障（核心）
| 问题 | 解决方案 |
|------|---------|
| Windows push 沙箱拦截 `~/.ssh` | Bash + `dangerouslyDisableSandbox: true`，让苏老师放行 |
| pull --rebase 因未暂存改动失败 | `screen.py` 改 `journal_tiers.json`/`pending_journals.txt` → **先 `git add -A` 再 rebase/push** |
| commit 后 "nothing to commit" 但提交已生成 | 复合 git 命令任一环非零会静默中断 → 收尾必查 `HEAD == origin/main` |
| 403（MDPI/ScienceDirect/Wiley/AGU/T&F） | 反爬≠死链，用 `verify_paper.py` 核实 |
| 502 "Tunnel connection failed" | 沙箱代理异常，改 WebFetch 复核 |
| HEAD 404/405 但链接有效 | 站禁用 HEAD → 批量核链须 **HEAD 失败回退 GET** |
| 臆造 URL | 严禁按 URL 模式推断；无直链用权威转载源并标注 |
| 聚合站日期 ≠ 发布日 | 一律查原文首发日 |
| present_files 预览污染 HTML | 先 commit+push 再 present；present 后 `git status` 复查 |
| 飞书文档 API 404 | token 反复失效；机器人 webhook 正常，文档 API 待苏老师更新，不阻断 |

## 去重基准（最近 3 期；更早 `grep -rl posts/`）
> `posts/` 为全量存档；本节仅列「易被再次检索命中」的标识符，完整条目见当日日志。

- **10-14（32条）**：neurips.cc/virtual/2026/poster/152997 DC-Ocean 潜在压缩预报、arxiv 2610.16584 CNN 北极快速海冰消亡、2610.09446 ArcticQA 弃答基准、2610.17936 PUGS 水下动态3DGS、2610.07788 图像空间折射校正、2610.09668 剖面浮标统计、s41612-026-01564-9 东亚极端冬季可预报性、rineng.2026.113466 海底热液羽流在线识别、oceaneng.2026.128726 数字孪生 AUV 容错、ecmx.2026.102346 波浪能数字孪生 MARL、ocecoaman.2026.108398 DTO 维度分析、trust-itservices EOSC 欧洲 DTO 节点投产、markaren/threepp 尾流场、2026gl124831 北极边界层云、isprs-archives-XLVIII-M-12-2026-25-2026 邻接效应校正、2026pa005469 氧同位素海平面、essd-18-7475-2026 中美近岸 Rrs、essd-18-7391-2026 WAPOSAL 波浪、rs18193402 VIIRS 透明度、maritime-spatial-planning 课程、zenodo 23238291 O2A Registry、emodnet biology course 更新、dsr.2026.104768 Gorringe 鲨类、2026gl124079 智利甲烷、15481603.2026.2741774 红树林海岸挤压、tio.org.cn/OWUP/.../5159 DOpH、ioc.unesco GESAMP 53、seanoe 01089/120103 MEDITS_ES、seanoe 00464/57596 Argo-BUFR 转换器、datadryad 1rn8pk19k 鲸类基线、argopy v1.5.0、ctdam v2.14.0
- **10-11（28条）**：s41598-026-73332-x Mamba-Transformer、oceaneng.2026.128631 深海采矿悬架、cviu.2026.104971 水下深度法线、gji/ggag421 Sentinel-2 测深、jastp.2026.106988 海盐气溶胶、edito.eu/ditto-summit、dto-bioflow.eu SUBSIM、oceaneng.2026.128641 SA-SRDC-Loc、bg-23-7043-2026 HPLC 色素、03091333261488345 UAV/USV 测深、gmd-19-9441-2026 LADDIE v2.0、01431161.2026.2742387 海水入侵、oceandecode.org/?p=24941、tianjinwe 143082_3904097、gmw.cn 1304574115、sp-7-osr10-10-2026 GlobColour 透明度、eo-1-129-2026 NSIDC 海冰漂移、xcdat v0.11.5、ioos compliance-checker、arxiv 2610.02194 SW1D
- **10-08（35条）**：2025jh000967 SST 降尺度、eswa.2026.134587 LLM4SST、epsl.2026.120368 全球海山 ML、2610.03780 OceanMind、bluegraph.io、essd-18-7269-2026 SWOT 圣劳伦斯基准、rse.2026.115706 南极 SST Landsat、2610.03649 星上异常、rs18193406 GNSS/水准 QC、carbontosea.org oae-data-commons、fmars.2026.1949937 海深 FAIR、data.gov.uk BGS 海洋调查、Project-OSmOSE/OSEkit、PyPI copernicusmarine 2.5.0

- **已剔除（勿再收）**：OceanParcels v3.1.4、Fugro OCEANITY/EDITO（09-08）、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL(>60天)、MBARI MOLA(05-04)、ICE-3D/DenseNet-121、ditto_summit2026、EX2606/EX2607 预告页、南海海洋大数据智能管理平台/南海孪境（09-08）、s43247-026-03899-w 北极原住民框架（09-24）、Ocean State Report 旧期预告页、NA182（09-27）、Voyis 船体检测（09-17）、Robosys VOYAGER（原文2026-03）、arXiv 2609.37964 任务驱动可视化（10-05 已发）、arXiv 2610.03888 REACT 活性示踪剂重建（10-08 已发）、OceanStream Globe/MyOcean Pro v17/CASPROD/GLODAPv3/EMSO EVOLVE/OceanEye（均已发文）

## 经验教训
- 跨期去重：占位主页 URL 会连续重复；Nautilus/EX 系列共用总览页须改用具体 news-release 页
- 日期核实：聚合站/新闻页日期 ≠ 发布日；WebFetch 失败 ≠ 放行，改 WebSearch/Crossref
- 约束必须写进 skill，不能只留在 prompt（07-31 教训）
- 主题盲区：国内院所新闻、极地/海冰曾漏检，已入巡检清单
- 用户指定条目与去重冲突：先核实历史收录，结论+三选项交用户拍板
- "预告"与"正式发布"可视为两次事件（09-20 OSR10 预告 → 10-05 正式发布）
- 连跑多步发布链路须逐步核验，收尾必查 `HEAD == origin/main`
- **宁缺不凑数**：10-11 方向四/八均仅 2 条；剩余候选或被近 3 期采用，或严格归类不符（数据集发布→八；纯海平面/古环境综述不入八），已回退 padding 尝试
- **阶段一成果须在构建时即纳入**：10-14 发布后才审查发现顶会覆盖为空，补丁补入 NeurIPS DC-Ocean → 构建前置检查项应含「阶段一采纳条目清单」
- **WebFetch 成功但 curl 000**：沙箱对 neurips.cc / zenodo.org / seanoe.org 直连失败，WebFetch 可达 → curl 000 ≠ 死链，核链以 WebFetch 为准
- **回滚式重发**：修正已发布报告时，用 `git show <base>:index.html` 回滚 index/archive 再重跑 publish，避免重复插入卡片
