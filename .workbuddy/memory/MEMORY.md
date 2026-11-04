# 海洋AI研究日报系统记忆

## 系统配置
- **用户**：苏老师 · **自动化ID** `ai`（rrule `FREQ=DAILY;BYHOUR=9;BYMINUTE=0`）· **2026-10-18 起 PAUSED**：任务定义留在云端，不再每日自动跑，由苏老师在自动化列表手动触发；改回 ACTIVE 即恢复
- **仓库** https://github.com/tianyunsu/ocean-data-daily-report ｜ **站点** https://tianyunsu.github.io/ocean-data-daily-report/
- **数据流**：`build_daily_YYYYMMDD.py` 用 repr 正则把 `SECTIONS` 注入 `feishu_write_doc.py` → `gen_html_YYYYMMDD.py` 用 `ast.literal_eval` 读 `feishu_write_doc.py` 出 HTML（**改内容只改 build_daily，必须重跑 build_daily 再跑 gen_html**）→ `posts/YYYY-MM-DD.html` + `index.html` + `archive.html` → push → 飞书/机器人
- **Python**：`py -3`（全流程）；链接实测可用系统 `Python313\python.exe`
- **OpenAlex key**：本地 `_openalex_key.txt`（gitignore，绝不入库）；读取序「环境变量 `OPENALEX_API_KEY` > 本地文件」，`harvest.py`/`verify_paper.py`/`source_metrics.py` 内置；有 key 走 cursor 翻页，无 key 回退 `page=`
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
- **铁律**：零覆盖来源组 ≤6；arXiv 占比 ≤50%；期刊占比 ≥40%；综述链接必须回查 `library.db.url`

## 执行流程与一致性
`阶段0 git pull+sync_skills.py install` → `阶段1 顶会/IEEE（≥5 条初筛）` → `阶段2 harvest+screen+来源矩阵` → `阶段3 build_daily+gen_html` → `阶段4 发布+飞书/机器人+周报/看板` → `阶段5 五审` → `阶段6 记忆写入`
- `ocean-daily-report` skill 是唯一权威源，prompt 纯委托；流程调整先改 skill
- 每期产出：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 滚动本文件 + 追加 `automations/ai/memory.md`
- 规模：每方向 3–5 条、合计 27–45；某方向确无新内容可为 0，**宁缺不凑数**；≤14 天，近 7 天优先
- 禁同日并行执行

## 内容质量规则
1. ≤14 天；14–60 天须豁免说明；>60 天删除（arXiv 以 v1 提交日为准）
2. 每条 URL 实测可访问；403/000 用 `verify_paper.py`（Crossref+OpenAlex）或 WebFetch 复核
3. 工具版本须官方 release notes 核实；摘要自原文提取，不据标题推断
4. 跨期去重三路：URL 集合差 + 中文标题片段 + DOI/卷期号
5. 方向归类按内容；同 URL 只在一个方向；主页新闻须给具体链接
6. 来源矩阵逐组打卡，零覆盖 >6 组须补检
7. 阶段一采纳条目须在阶段三构建时即纳入（非事后补丁）

## 常见故障
| 问题 | 解决方案 |
|------|---------|
| Windows push 沙箱拦 `~/.ssh` | Bash + `dangerouslyDisableSandbox: true` |
| pull --rebase 因未暂存改动失败 | `screen.py` 会改 `journal_tiers.json`/`pending_journals.txt` → **先 `git add -A` 再 rebase/push** |
| 复合 git 命令静默中断 | 收尾必查 `HEAD == origin/main` + 工作区干净 |
| 403（MDPI/ScienceDirect/Wiley/AGU/T&F） | 反爬≠死链，`verify_paper.py` 核实 |
| curl 000 / 502 Tunnel | 沙箱代理异常（neurips/zenodo/seanoe），改 WebFetch 复核 |
| HEAD 404/405 但链接有效 | 站禁用 HEAD → 核链须 HEAD 失败回退 GET |
| 臆造 URL / 聚合站日期 | 严禁按模式推断；一律查原文首发日 |
| present_files 预览污染 HTML | 先 commit+push 再 present，事后 `git status` 复查 |
| 飞书 API 404 | **根因是端点写错非 token**：正确 `POST .../documents/{doc}/blocks/{doc}/children`（body `children`）。样式须放 `text_run.text_element_style`；旧 `text_run.style/link` 被**静默忽略**。详见 SKILL 陷阱 31 |
| 飞书文档同日重复 | `create_document_and_write()` 按标题 `海洋AI技术日报 YYYY-MM-DD` 命中即清空重写，未命中才新建（陷阱 33） |
| OpenAlex 401/429 | 2026-10-15 起 cursor 第 2 页需 key、重查询扣额度 → 已配 key（独立 $1/天）；失效改 WebSearch/Crossref 人工补检 |
| `harvest.py --dirs` 重跑覆写池 | 先 `cp data/pool/日期.jsonl data/pool/_bak_日期.jsonl`，失败后合并恢复 |
| OpenAlex 会议论文为 0 | 类型值须 `conference-paper`（旧 `proceedings-article` 恒返 0 且不报错）；排查用已知会议论文反查做阳性对照 |

## 去重基准（最近 3 期；更早 `grep -rl posts/`）
> `posts/` 为全量存档；本节只列「易被再次检索命中」的标识符，完整条目见当日日志。

- **11-04（40条）**：e.huawei 司渊海洋大模型、qdio.cas.cn 8299912 苏禄海内孤立波 TGRS、arxiv 2610.29313 YingLan、10.1145/3840750.3841451 GreenToken ACM MM、10.1109/LRA.2026.3746126 ISOPoT、sznews 32199065 深圳防灾孪生、weibo 5359283964608565 北部湾孪生一等奖、SEC 1846715 Eco Wave 孪生、zenodo.23674230 EDITO EOSC、mapgis id=1913 海洋版、qq 20261028A04ZEQ00 耕海1号一张图、mp.weixin 漂视 CIMPro、10.5194/sd-35-229-2026 GEODESC、10.1111/1752-1688.70158 OSTDS GIS、ckjorc detail/3435 GOCI-II、cran argoFloats、arxiv 2610.37731 摊销后验、10.1175/jtech-d-26-0004.1 X 波段波向、10.5194/essd-2026-807 Morlenn、10.5194/essd-18-7963-2026 MLAWind、qdhy.cbpt.cnki 葵花8号超分、arxiv 2610.36410 LILY、10.1038/s41598-026-76456-2 机载测深激光雷达、seabed2030 波罗的海 BSHC、cioos.ca IODE ADU、watertools 538 Okeanos-OBIS/GBIF、10.1175/bams-d-25-0157.1 NNJA、sciencenet 574029 CliMetS/MOCSI、10.1029/2026GL124056 北极碳质气溶胶、10.1038/s41598-026-78685-x 南极 UAV 海鸟、ysfri 59428 蓝海101、cnfin 4488855 青岛海洋大数据应用中心、watertools 544 Sentinel-6B、copernicus product-roadmap 11月更新、10.5194/essd-18-7839-2026 IBRA 伊势湾、10.1002/lom3.70102 Ricker 小波、pypi oceanarray、zenodo.23749880 thermochain、ebiotrade 20261023104103527 CN-Waves、10.3390/computers15110763 WindAnalysis（MDPI/D）
- **11-02（32条）**：oceaneng.2026.129035 GSE ResNeXt 水下声学、s41612-026-01572-9 天星-S2S 扩散集合、jfb.70717 耳石层级 DL、ecolind.2026.115773 山东半岛富营养化、fbuil.2026.1969739 Unity 3D 海平面孪生、2755-2721/2026.38220 船舶电力孪生、buildings16204154 侨乡 HBIM（MDPI/D）、14738716261492254 海洋评估可视化、mafis.4012027010106 QGIS+CMEMS、app162110608 地层正演（MDPI/D）、s41598-026-76333-y 缺测填补、jaic.v10i5.13951 孤立森林质控、arxiv 2610.33609 卫星水深无泄漏、s43247-026-04175-7 格陵兰斜坡、2026jc024403 近海极端海平面、s13131-026-2694-2 RF-SFDL 声速、s10236-026-01869-6 高斯过程潮汐、aiig.2026.100284 生成模型水深、ecss.2026.110293 CNN-ISO 海平面、s10661-026-16088-1 立陶宛分类单元、6ad293ec 军事开放科学海岸遗产、1749-4877.70217 海兽性状库、ce.cn t20261027_3272858 蛟龙 7000 米海试、2026gl125540 南大洋合成浮标、essd-18-7743-2026 渤黄东海粒度、2026gl123670 航空声-震耦合、news.cn 妈祖 2.0、v.china.com.cn 临港海底数据中心、seanews 海博会、rineng.2026.113720 COAST、gji ggag450 OWL、echopype v0.12.0
- **10-25（23条）**：3795866.3844488 MobiCom RollingPol 偏振水下感知、978-3-032-42348-1_22 CCIS 物种分类、autcon.2026.107321 声呐点云去噪、oceaneng.2026.128908 台风相位解析波浪、s12145-026-02283-8 MNDWI 海岸带 CNN-LSTM、fmars.2026.1966759 DTO 惠益分享、s13131-026-2690-6 CORA v2.0 内潮、jmse14211983 轴系 MLP（MDPI/D）、ocemod.2026.102841 3DSeaVizKit、3800965.3834276 CHI PLAY Tidy Tide、2026EA005018 浮标驻留时间、arxiv 2610.29306 波浪谱反演、s44163-026-02461-z 海缆威胁融合、gmd-19-8915-2026 DIRECT 1.0 SST 扩散重建、essd-18-7627-2026 末次间冰期海平面代理、emodnet BioTiles 培训、mbari.org/expedition/multisensory-milos、watertools info/502 深蓝瞭望第6期、rob.70372 多AUV搜救规划、eco-business 海底数据中心生态之辩、dy.163 L91NHHO805527PMU 韩华 60MW、pypi echoregions 0.2.4、pypi coastsat-package 0.5.1

- **已剔除（勿再收）**：OceanParcels v3.1.4 / v4.0（09-15 已发，v4.0.2 补丁不单列）、Fugro OCEANITY/EDITO、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL、MBARI MOLA、ICE-3D、ditto_summit2026、EX2606/EX2607 预告页、南海海洋大数据智能管理平台/南海孪境、s43247-026-03899-w 北极原住民、OSR 旧期预告、NA182、Voyis 船体检测、Robosys VOYAGER、2609.37964、2610.03888 REACT、OceanStream Globe/MyOcean Pro v17/CASPROD/GLODAPv3/EMSO EVOLVE/OceanEye、2610.03743 北极 SIC、2610.03739 SWOT 去噪、2610.17939 Sea-Net、2610.04449、WireClear-GS 2610.19753、OceanXL 2609.29985、essd-18-4617-2026 西太温盐场（**09-04 已收录，非质量原因**，链接用 Copernicus 直链 `essd.copernicus.org/articles/18/4617/2026/`）、OS 2903 北大西洋海平面、GMD MONKI 19-9677（行星大气）、JSTARS 3736460 GNSS-IR、rs18193402 VIIRS 透明度、essd-18-7345-2026 UVP5 数据库、中国大洋100 航次第二航段、中国第16次北冰洋考察、2610.09668 剖面浮标统计、NCEI WOA 密度/电导/MLD（2021 旧闻）、SWOT Sci Rep 2026-10-17（实为内陆水库）、NeurIPS 2026 OC-UIE 全向可控 UIE（10-25 检索时无 arXiv/OpenAlex 收录、日期不可核验，暂不收待复核）、argopy v1.5.0 之外的 pyoceans 例行更新、RA-L 2026 Underwater Photogrammetric Mapping / TurbidPose / AUV Docking 混合测试（11-02 检索时四源均无摘要，无摘要不收）、NOAA GOMO 8 个 AI 试点（2026-10-01，超窗）、NIPS'25 NAUTILUS（2025 论文集）、**fmars.2026.1909271 EMODnet–OBPS 可追溯性（10-16 已发）**、**os-22-3403-2026 GLODAPv3 内部一致性反演（数据产品已 3 期覆盖 07-21/24/28，不重发）**、**s44163-026-02461-z 海缆威胁融合（10-25 已发）**

## 漏检核查与已知盲区（2026-11-04 建立）
> 用途：苏老师抽查「某篇是否收录」时的处置台账。每条须落成「已收录 / 时间窗正当排除 / 系统未运行 / 真实漏检 + 根因」四类之一。

### 已核查案例
| 文章 | DOI | 结论 | 根因 |
|------|-----|------|------|
| ESSD 注意力增强 3D-U-Net++ 西太温盐重构 | `10.5194/essd-18-4617-2026` | **已收录 2026-09-04**（方向五） | 日报用 Copernicus 直链 `essd.copernicus.org/articles/18/4617/2026/` 而非 DOI → 按 DOI 检索出现假阴性 |
| TGRS GBM 海洋锋检测框架 | `10.1109/TGRS.2026.3660295` | 时间窗正当排除 | 真实首发 `2026-02-03`（Crossref created），而日报最早期次为 `2026-03-23` → **系统上线前** |
| The Innovation Informatics PINN 降海洋状态预报不确定性 | `10.59717/j.xinn-inform.2026.100051` | 无摘要不收 | 首发 `2026-07-20`，OpenAlex `abstract_inverted_index` 空 + Crossref `abstract` 空 → 双源无摘要 |
| TGRS KunPeng 全球海洋环境模型 | `10.1109/TGRS.2026.3708338` | **真实漏检** | 首发 `2026-06-30`、有 1716 字符摘要、落在 07-01 期窗口内，但 OpenAlex `publication_date` 被归一化为 `2026-01-01` → 任何日期窗口检索都命中不到 |

### 三类根因（按影响面排序）
1. **IEEE 期刊日期塌缩（最严重，系统性）**：TGRS 等 IEEE 刊在 OpenAlex 的 `publication_date` **恒为当年 1 月 1 日**（TGRS 2026 全部记录均为此值），`created_date`/`updated_date` 也不等于首发日（KunPeng 的 created_date = 2025-10-10，与 Crossref 的 2026-06-30 不符）。后果：**按日期窗口拉取时 IEEE 期刊永远返回 0**，不只是"阶段一 count=0"，而是这些刊的论文**结构性无法进入日报**。10-21/11-02/11-04 三期 IEEE 期刊通道全 0 均源于此。
   - ✅ **修复方案（已实测有效）**：改用 **Crossref `filter=issn:<issn>,from-created-date:<start>,until-created-date:<end>`**。实测 TGRS（issn 0196-2892）在 `2026-10-21~2026-11-04` 窗口返回 **120 篇**（OpenAlex 为 0 篇），其中海洋相关 15 篇（含 `10.1109/tgrs.2026.3745627` 西北太平洋 15 角秒水深预测、`3749930` 多视场星载微波 SST 反演、`3748509` 双波束斜视 SAR 波浪观测、`3749162` VesselBench-800K 船舶检测基准）。Crossref 的 `created` 字段 = DOI 注册日，与首发日基本一致，可信。
   - 🔧 **已落地工具**：`stage1_ieee_crossref.py`（2026-11-04 新增）。用法 `py -3 stage1_ieee_crossref.py --start YYYY-MM-DD --end YYYY-MM-DD [--no-abstract]`，输出 `_stage1_ieee.json`（临时文件，已 gitignore）。实测窗口内 9 刊合计 `total=473 / ocean_hits=38`（JOE 4、TGRS 120/hits 9、GRSL 15/1、JSTARS 106/13、GRSM 4/0、T-RO 13/0、RA-L 164/9、TNNLS 22/0、TIP 25/2）。**阶段一 IEEE 期刊组必须跑此脚本，不得只用 OpenAlex 日期窗口。**
2. **链接形式不一致（去重假阴性）**：同一条目可能用 DOI 链接、出版商直链（Copernicus `/articles/vol/page/year/`、MDPI `/issn/vol/issue/page`、IEEE `document/id`）、机构新闻稿链接中的任意一种。跨期去重若只做 URL 字符串集合差，会把已发条目误判为"未收录"，进而**重复收录**或**误加入勿再收名单**。
   - ✅ **修复方案**：去重前先做 DOI 归一化 —— `doi.org/(10\..+)` 直接取；Copernicus 规则 `{journal}.copernicus.org/articles/{vol}/{page}/{year}/` → `10.5194/{journal}-{vol}-{page}-{year}`（已实测匹配 `10.5194/essd-18-4617-2026`）；兜底用标题归一化（去标点、小写、取前 60 字符）。
   - 📌 **规范**：新条目**优先用 `https://doi.org/...`**，让 URL 比对天然等价于 DOI 比对。
3. **系统上线前的历史文章**：日报最早期次 `2026-03-23`，此前发表的论文不在任何期次的检索范围内，属不可补的天然缺口（如需覆盖只能显式回溯，不在常规流程内）。

### 处置纪律
- 遇到"某篇是否收录"的核查，**不能只 grep DOI** —— 必须同时 grep：DOI 尾段数字、期刊简称+卷+页（如 `18, 4617`）、英文标题关键词、中文标题关键词。
- 「已剔除（勿再收）」名单里混有"已收录"条目，**语义不同**：前者是质量/时效原因弃用，后者是已发不重发。新加入时须显式标注「xx 期已发」。

## 经验教训
- **期刊占比 ≥40% 必须在阶段三定稿时就核算（2026-11-04）**：本期首版 34 条中期刊/会议仅 10 条（29.4%），到五审才发现，补救要连带重跑 build_daily + gen_html + 回滚 index/archive + 重跑 publish，等于做了两遍发布。`build_daily` 出数后立刻算一次占比，不达标就在**阶段三**补检。
- **方向三/四/六/八 是结构性「期刊荒漠」（2026-11-04）**：可视化 / 数据质量 / 数据管理 / 数据中心 这四类的真实产出形态是产品发布、机构动态、工具版本，harvest 池里几乎没有期刊论文（本期该四方向 32 条有摘要候选中期刊仅 5 条，且 4 条已被往期采用）。**必须在阶段二就用 OpenAlex `title_and_abstract.search` 定向补检**，不能指望池子自己涨。
- **OpenAlex `host_organization` 滤镜不可靠（2026-11-04）**：传入 T&F/SAGE/AAAS/IOP 的 organization ID，返回的却是 Springer / OUP / BMC 刊物 → **不能用来判定「某出版商零覆盖」**。零覆盖归因应改走「关键词实检索 + 摘要齐缺说明」两条腿。
- **OpenAlex filter 值里写 `%20` 会被 urlencode 二次编码（2026-11-04）**：`title_and_abstract.search:ocean%20visualization` 经 urlencode 变成字面 `ocean%20visualization`，**恒返 0 且不报错**，极易误判「该主题无新内容」。写滤镜一律用真实空格，编码交给 urlencode。
- **GitHub Pages 重建约 100 s（2026-11-04）**：push 后立即抓取拿到的是旧版（本期先抓到 34 条旧页、误以为发布失败）。复核线上内容须等 60–90 s 并加 `?v=n` 破 CDN 缓存。
- **Elsevier/ACM/OUP 新刊论文摘要三源齐缺（2026-11-02 发现）**：2026-10 的 Ocean Engineering / ISPRS / DSR 等条目在 OpenAlex (`abstract_inverted_index` 为空)、Crossref (`abstract` 缺失)、Semantic Scholar 三处都取不到摘要，ScienceDirect 直接 CAPTCHA 拦截。凡遇到此类条目，**无摘要即不收**，绝不用标题推断摘要；替代做法是从 `data/pool/*.jsonl` 的 `abstract` 字段筛「有摘要」的候选（本期 244 条池中 189 条有摘要）。这也是顶会/IEEE 组本期零覆盖的唯一原因。
- **周报 ISO 期号会跳号（2026-11-02 发现）**：10-25（周日，W43）→ 11-02（周一，W45），W44 期号凭空消失。若需要连续期号，应改 `weekly_report.py` 按「距上期天数」而非 end-date 的 ISO 周命名。
- **OpenAlex 滤镜字段会被改名废弃（2026-10-25 发现）**：`issn:` 直接返回 400 Invalid query parameters，须改 `primary_location.source.issn:`；错误表现为 400 而非静默 0。凡依赖滤镜字段的查询，0 结果时先怀疑字段名变更。另注：JOE 正确 issn_l=0364-9059（曾误记 1545-5821）。
- **池 jsonl 的 DOI URL 小写存储**：跨源 URL 比对（周报链接回查、去重）必须大小写归一，否则把池内条目误判为「池外链接」造成假阴性（10-25 实测 EA005018）。
- **顶会论文日期不可核验时宁缺不收**：NeurIPS 2026 OC-UIE 无 arXiv v1、OpenAlex 未收录、虚拟页无公开日期 → 按「首次公开可访问日期」无法取证，本期不收录并在日志留痕，不得套用会议召开日。
- **宁缺不凑数（2026-09-15 苏老师拍板）**：10-21 仅 24 条（<27 下限）、六个方向低于 3 条，因池内高分候选多被往期采用或归类不符；不为凑数跨类硬塞
- **改内容必须重跑 build_daily**：`gen_html` 读的是 `feishu_write_doc.py` 里注入后的 `SECTIONS`，只改 `build_daily_*.py` 再跑 gen_html 会出一模一样的 HTML（10-21 两次踩到）
- **事件日 ≠ 报道日**：条目日期取报道/论文发布日；arXiv 一律以 v1 提交日为准，聚合站日期多次被证伪
- **中文条目去重必须用中文片段 grep**：往期中文标题、本期 DOI/英文标题时 URL 集合差会漏判
- **分页/词表会静默截断**：`page=` 回退有 `max_pages×200` 上限（曾把 2,388 条截成 800）；OpenAlex 类型值写错则恒返 0。凡依赖外部词表或分页的过滤器须定期做阳性对照，并核对 `meta.count` 与池内条数
- **OpenAlex 索引滞后 T+2/T+3**：池内最近两天条目偏少属正常时滞，勿误判采集失败
- **IEEE 期刊 publication_date 塌缩（2026-10-21 发现）**：OpenAlex 对 TGRS 等 IEEE 刊 2026 年记录把日期统一归一到 `2026-01-01`（TGRS 2026 全年 224 条全为 1 月 1 日，ISSN 过滤本身有效——2025 全年 308 条正常）→ **窗口内 IEEE 期刊命中为 0 属数据源限制，不是检索失效**；补位靠 IEEE Xplore 直查或顶会通道
- **回滚式重发**：修正已发布报告时先 `git show <base>:index.html` 回滚 index/archive 再重跑 publish，避免重复插入卡片
- **HTTP 200 ≠ 业务成功**：第三方 API 必须①校验响应体 code ②回读落库结果（飞书曾 27 条链接全丢而 HTTP 全 200）
- **公开仓库禁硬编码凭证**：飞书 APP_ID/SECRET 曾明文散在 14 个脚本 + 指南文档；已统一 `_feishu_auth`，全库 grep 残留 0；App Secret 已于 10-18 轮换，旧值彻底作废。五审新增「改动文件是否新增硬编码凭证」
- **远程文档写入必须幂等复用 + 回读校验**：曾堆积 137 个文档、89 个同日重复，且 04-15~10-16 全是空壳（块数=1）→ 按天产出写远程文档一律复用固定标识文档，写完回读块数
- **主题盲区**：国内院所新闻、极地/海冰曾漏检，已入巡检清单；会议通道曾长期归零（10-18 修复）
- 用户指定条目与去重冲突：先核实历史收录，给结论 + 三选项交苏老师拍板
