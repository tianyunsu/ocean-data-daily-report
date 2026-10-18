# 海洋AI研究日报系统记忆

## 系统配置
- **用户**：苏老师 · **自动化ID**：`ai`（`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）
- **仓库**：https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（`SECTIONS` 由 `build_daily_YYYYMMDD.py` repr 正则替换）；**HTML**：`gen_html_YYYYMMDD.py`（自包含，`ast.literal_eval`）；**发布**：`posts/YYYY-MM-DD.html` + `index.html` + `archive.html` + git push；**L3**：`gen_frontier.py` + `weekly_report.py`
- **本机 Python**：`py -3`（飞书/机器人/校验）；系统 `Python313\python.exe`（链接实测）
- **OpenAlex key（2026-10-16 起）**：本地文件 `_openalex_key.txt`（**已 gitignore，公开仓库绝不入库**）；读取顺序「环境变量 `OPENALEX_API_KEY` > 本地文件」；`harvest.py` / `verify_paper.py` / `source_metrics.py` 三处已内置读取，有 key 走 cursor 翻页、无 key 回退 `page=` 分页

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
| 飞书文档 API 404（**2026-10-18 已定位并修复**） | **根因不是 token 失效，是脚本写错 API 端点**：`POST .../documents/{doc}/blocks` 不存在，正确为 `POST .../documents/{doc}/blocks/{doc}/children`（body 用 `children`，非 `blocks`）。实测 app_id/secret 换 token 一直成功（code=0），文档 GET 也正常。另修 `tr()`：加粗/链接必须放 `text_run.text_element_style`，旧字段 `text_run.style`/`text_run.link` 被飞书**静默忽略**（HTTP 200 但不生效）；并补 `feishu_doc_url.txt` + stdout `SUCCESS` 两个上层依赖信号。**教训：HTTP 200 ≠ 业务成功，须校验 code 并回读落库结果** |
| OpenAlex cursor 翻页 401 "API key required" | **2026-10-15 起新政**：第 2 页起 cursor 需免费 key → **已配置 key**（`_openalex_key.txt`），恢复 cursor 翻页；无 key 回退 `page=` 分页（上限 1 万条） |
| OpenAlex 重查询 429 "Insufficient budget" | 无 key 共享 IP 日预算 $0.10；**已配置 key（独立 $1/天）后消除**；key 失效时改用 WebSearch/官网人工补检 |
| `harvest.py --dirs` 重跑覆写池文件（陷阱 25） | 重跑前先 `cp data/pool/日期.jsonl data/pool/_bak_日期.jsonl`，失败后合并恢复（10-16 两次复现） |
| OpenAlex 会议论文静默为 0 | **2026-10-18 实测**：类型值已改 `conference-paper`，旧值 `proceedings-article` 对任意年份均返回 0（2025 全年亦 0）→ harvest.py 已修；排查用「已知会议论文反查」做阳性对照 |

## 去重基准（最近 3 期；更早 `grep -rl posts/`）
> `posts/` 为全量存档；本节仅列「易被再次检索命中」的标识符，完整条目见当日日志。

- **10-18（27条）**：15481603.2026.2748224 Sub-Eddy-Net 亚中尺度涡 SST 检测、lol2.70168 大堡礁 742 站点珊瑚 DL、978-3-032-37682-4_39 ECML PKDD 碳吸收时间模拟器、33012/2026.20644 ION GNSS+ UUV-NAV、oceaneng.2026.128558 物理约束扩散声呐增广、coasts6040045 海岸水文数字孪生综述（MDPI/D）、apor.2026.105282 海浪降阶+同化、ocemod.2026.102849 GNN 同化、arxiv 2610.19097 冰下三维重建基准、x5tj8d 巨砾分割、fmars.2026.1977051 DriftGuard、ismeco/ycag297 原核绝对丰度、egusphere-2026-5747 次表层热浪再分析、oceaneng.2026.128770 滑翔机能耗多步预测、s41597-026-08422-6 UPED 三模态数据集、essd-2026-670 PhyEddy-Net、CAOE 124—2026 南海大数据接口标准、bdj.14.e196603 浮游植物性状、EMODnet Chemistry WFS 231b288d、x5x81x 冰系浮标布放、fmars.2026.1944587 滑翔机主动声学、GEBCO 秘书处摩纳哥、geodata 30378725417220 122 种外来动物、智慧海洋大数据大赛 25 强、apor.2026.105257 Metocean-stats v1.2、softx.2026.103108 DATRASextra、oceantide 0.9.0
- **10-16（27条）**：s41586-026-11126-x Nature 次季节 ML 误差订正、arxiv 2610.19772 PANN 过程加性神经网络、ggag426 SP-PINN 海底硫化物自然电位、oceaneng.2026.128706 PINN 水下电场、oceaneng.2026.128550 DRL 仿生 AUV、2610.14645 原生涡分辨率模拟器、tc-20-5867 南极 SIC 同化次季节、eworldship 224966 远海丝路数字化交付、csr.105798 达尔文港波流、2610.07472 SURGE 声纳高斯泼溅、prnewswire Costa Rica 地图、essd-2026-771 marinedb、2041-210x.70431 UNIQAT、ieeexplore 11712251 ELMAR 海况分类、2610.11368 缪子成像潮汐、fmars.1909271 EMODnet×OBPS 方法溯源、hubocean.earth/press/news/whalechart/odp 鲸类图、bluelifehub MedBlueTech、2610.04536 WasserMan、2610.09690 NAViLoss、oceaneng.2026.128450 PSO 路径规划、oceaneng.2026.128720 波浪滑翔机限速、nmemc 环境智报平台、seabed2030 MEWO、toutiao 7694109833414443539 青岛海洋大数据、Unidata/cftime v1.6.6.1、lom3.70099 seaEchoTSCalculator
- **10-14（32条）**：neurips.cc/virtual/2026/poster/152997 DC-Ocean 潜在压缩预报、arxiv 2610.16584 CNN 北极快速海冰消亡、2610.09446 ArcticQA 弃答基准、2610.17936 PUGS 水下动态3DGS、2610.07788 图像空间折射校正、2610.09668 剖面浮标统计、s41612-026-01564-9 东亚极端冬季可预报性、rineng.2026.113466 海底热液羽流在线识别、oceaneng.2026.128726 数字孪生 AUV 容错、ecmx.2026.102346 波浪能数字孪生 MARL、ocecoaman.2026.108398 DTO 维度分析、trust-itservices EOSC 欧洲 DTO 节点投产、markaren/threepp 尾流场、2026gl124831 北极边界层云、isprs-archives-XLVIII-M-12-2026-25-2026 邻接效应校正、2026pa005469 氧同位素海平面、essd-18-7475-2026 中美近岸 Rrs、essd-18-7391-2026 WAPOSAL 波浪、rs18193402 VIIRS 透明度、maritime-spatial-planning 课程、zenodo 23238291 O2A Registry、emodnet biology course 更新、dsr.2026.104768 Gorringe 鲨类、2026gl124079 智利甲烷、15481603.2026.2741774 红树林海岸挤压、tio.org.cn/OWUP/.../5159 DOpH、ioc.unesco GESAMP 53、seanoe 01089/120103 MEDITS_ES、seanoe 00464/57596 Argo-BUFR 转换器、datadryad 1rn8pk19k 鲸类基线、argopy v1.5.0、ctdam v2.14.0

- **已剔除（勿再收）**：OceanParcels v3.1.4、Fugro OCEANITY/EDITO（09-08）、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL(>60天)、MBARI MOLA(05-04)、ICE-3D/DenseNet-121、ditto_summit2026、EX2606/EX2607 预告页、南海海洋大数据智能管理平台/南海孪境（09-08）、s43247-026-03899-w 北极原住民框架（09-24）、Ocean State Report 旧期预告页、NA182（09-27）、Voyis 船体检测（09-17）、Robosys VOYAGER（原文2026-03）、arXiv 2609.37964 任务驱动可视化（10-05 已发）、arXiv 2610.03888 REACT 活性示踪剂重建（10-08 已发）、OceanStream Globe/MyOcean Pro v17/CASPROD/GLODAPv3/EMSO EVOLVE/OceanEye（均已发文）、arXiv 2610.03743 北极 SIC（v1=08-22 过期）、arXiv 2610.03739 SWOT 去噪（v1=09-22 过期）、arXiv 2610.17939 Sea-Net 与 2610.04449（非海洋）、WaterClear-GS 2610.19753（01-27 过期）、OceanXL 2609.29985（09-24 过期）、ESSD 西太温盐场 3D-U-Net++ essd-18-4617-2026（09-07 首发，toutiao 10-09 转载）、Ocean Science 2903 北大西洋海平面（09-25 过期）、GMD MONKI 19-9677（行星大气，非海洋）、JSTARS 3736460 GNSS-IR（09-23 过期）、rs18193402 VIIRS 透明度（10-14 已发勿再收）、**essd-18-7345-2026 UVP5 全球浮游生物数据库（10-08 已发，中文标题勿再收）**、**中国大洋100航次第二航段（10-11 已发）**、**E/V Nautilus NA182 夏威夷航次（09-27 已发）**、**中国第16次北冰洋考察（10-05 已发）**、**OceanParcels v4.0（09-15 已发，v4.0.2 补丁不单列）**、**arXiv 2610.09668 剖面浮标统计海洋学（10-14 已发）**、**NCEI WOA 新增密度/电导/MLD 气候态（原始新闻 2021-03-31，聚合站旧闻新炒）**

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
- **OpenAlex 政策（2026-10-15 起）**：cursor 翻页需免费 API key、重查询按额度扣费 429 → `page=` 基础分页免 key（上限 1 万条）；**建议申请免费 key 一并解决 401+429**；harvest.py 已打补丁（10-16）
- **事件日 ≠ 报道日**：条目日期取报道/论文发布日，不取事件发生日（MedBlueTech 10-01 事件 → 10-02 文章）；arXiv 一律以 v1 提交日为准、逐条 API 核实，聚合站日期两次被证伪（10-16）
- **分页上限会静默截断池（10-16 发现）**：旧 `page=` 回退分页每查询上限 `max_pages×200`=800 条 → 方向 1 真值 2,388 条却只取到 800（池内 1,155 恰为 800+预印本）；**已配置 key 恢复 cursor 翻页（上限 4,000）解除截断**，此后各期池覆盖面提升。排查口径：`meta.count` 与池内条数差额过大即为截断
- **OpenAlex 最近 2 日索引滞后（T+2/T+3）**：实测 10-13~10-16 = 276 条、10-15~10-16 仅 2 条 → 池内「最近两天条目偏少」属正常时滞，非请求缺陷，勿据此误判采集失败
- **会议通道静默失效（10-18）**：OpenAlex 类型值 `proceedings-article` → `conference-paper`，旧值对任意年份返回 0 且**不报错**，会议覆盖长期归零无人察觉；修复后窗口内 240 条、采纳 2 条。凡「依赖外部词表」的过滤器须定期做阳性对照
- **中文条目去重必须用中文片段 grep（10-18）**：UVP5 数据库、大洋100 航次均因往期用中文标题、本期用 DOI/英文标题而在 URL 集合差中漏判 → 铁律：每条中文条目另跑一次「中文标题片段」grep，不能只比 URL
- **池量跃升需解释**：W42 池内 1,539 vs 上期 175，主因 cursor 翻页恢复 + 会议通道修复，不是产出突变；周报综述须写明，避免趋势误读
- **HTTP 200 ≠ 业务成功（10-18 飞书修复）**：飞书 docx 写入用错端点（`/blocks` 缺 `/{block_id}/children`）报 404 被误判为「token 失效」多期；`text_run.style`/`text_run.link` 非法字段则**静默忽略**（HTTP 200 但不生效）→ 铁律：第三方 API 接入后必须①校验响应体 code ②回读落库结果（本次回读发现 27 条链接全丢）。正确写法见 SKILL 陷阱 31
- **公开仓库禁硬编码凭证（2026-10-18 整改）**：飞书 `APP_ID`/`APP_SECRET` 曾明文写在 14 个脚本 + `FEISHU_UPLOAD_GUIDE.md` 里（苏老师主动点出）。已建 `_feishu_auth.py` 统一供给（环境变量 > 本地 `_feishu_credentials.env`，已 gitignore），与 OpenAlex key 同一纪律；全仓库 grep 残留为 0。**遗留事项：secret 仍在 git 历史，须去飞书开放平台轮换。** 阶段五五审新增一项「改动文件是否新增硬编码凭证」
- **远程文档写入必须幂等复用（2026-10-18）**：飞书云空间曾堆积 137 个日报文档、89 个同日重复，根因是脚本每次运行都新建。已改 `feishu_write_doc.py` 为「按标题匹配当天文档 → 清空正文重写 → 未命中才新建」。铁律：凡按天产出写远程文档的任务一律复用固定标识文档，禁止每次新建
- **文档「创建成功」≠ 内容写进去**：实测 2026-04-15 ~ 2026-10-16 的飞书日报**全是空壳**（块数=1，docx 端点失效期只建文档写不进内容），仅 3 月及更早、修复后的 10-18 有真实内容。**教训：写完必须回读块数校验**
- **App Secret 轮换（2026-10-18 已完成）**：网页重置由苏老师本人扫码完成（脚本无法代做），新 Secret 已写入 `_feishu_credentials.env` 并经端到端验证（137 块 / 27 链接 / 文档总数不增）。旧 Secret 实测 `code=10014 app secret invalid` **已彻底作废**，git 历史里的旧值不再构成风险。`_rotate_feishu_secret.py` 已支持管道模式（`echo <secret> | py -3 _rotate_feishu_secret.py`），验证失败不改文件
