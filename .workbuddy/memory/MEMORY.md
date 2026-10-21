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

- **10-21（24条）**：cs.tjut.edu.cn/info/1001/2984 NeurIPS PRISM 海上小目标、fmars.2026.1890995 海洋AI八学科综述、ebiotrade 20261017090325761 南海所 DLSCR 次表层流、s41598-026-76042-6 XCAT-UIR 水下复原、2026-99-2910 EAU-Net SAR 近岸分割、fmars.2026.1953622 物理信息 LSTM 浮标漂移、asi9100212 船舶动力数字孪生（MDPI/D）、github Noniv/web-ocean WebGPU 渲染器、gmd-19-9957-2026 ARMS-gb v2.0、marpolbul.2026.120446 南极半岛 CRM、ocecoaman.2026.108411 海岸带知识/数据驱动对比、rs18203504 台风双偏振 QPE（MDPI/D）、os-22-3207-2026 MCMC 地中海低频变率、s12145-026-02274-9 海岸侵蚀淤积混合框架、2025jd045869 气象季节 ML 定义、jmarsys.2026.104319 风暴潮潮汐波浪、jmse14201909 北极海冰厚度重建（MDPI/D）、s12859-026-06660-4 Metacontextify、s42003-026-11025-x 珊瑚脱氧方法学、watertools.cn/news/info/490 深蓝瞭望第2期、blackridgeresearch 日本港内浮式数据中心、worldoil 10/14 stranded gas 数据中心、news.ucsb.edu 022878 oceandatr、PyPI pyaro 0.3.3
- **10-18（27条）**：15481603.2026.2748224 Sub-Eddy-Net、lol2.70168 大堡礁珊瑚 DL、978-3-032-37682-4_39 ECML PKDD 碳吸收、33012/2026.20644 UUV-NAV、oceaneng.2026.128558 声呐增广、coasts6040045 海岸水文 DTO 综述（MDPI/D）、apor.2026.105282 海浪降阶同化、ocemod.2026.102849 GNN 同化、2610.19097 冰下三维重建基准、x5tj8d 巨砾分割、fmars.2026.1977051 DriftGuard、ismeco/ycag297 原核绝对丰度、egusphere-2026-5747 次表层热浪、oceaneng.2026.128770 滑翔机能耗、s41597-026-08422-6 UPED 数据集、essd-2026-670 PhyEddy-Net、CAOE 124—2026 南海接口标准、bdj.14.e196603 浮游植物性状、EMODnet Chemistry WFS 231b288d、x5x81x 冰系浮标、fmars.2026.1944587 滑翔机主动声学、GEBCO 摩纳哥、geodata 30378725417220 外来动物、智慧海洋大数据大赛25强、apor.2026.105257 Metocean-stats v1.2、softx.2026.103108 DATRASextra、oceantide 0.9.0
- **10-16（27条）**：s41586-026-11126-x 次季节 ML 订正、2610.19772 PANN、ggag426 SP-PINN 自然电位、oceaneng.2026.128706 PINN 水下电场、oceaneng.2026.128550 DRL 仿生 AUV、2610.14645 原生涡模拟器、tc-20-5867 南极 SIC 同化、eworldship 224966、csr.105798 达尔文港波流、2610.07472 SURGE 声纳泼溅、prnewswire Costa Rica、essd-2026-771 marinedb、2041-210x.70431 UNIQAT、ieeexplore 11712251 ELMAR、2610.11368 缪子成像潮汐、fmars.1909271 EMODnet×OBPS、hubocean whalechart、bluelifehub MedBlueTech、2610.04536 WasserMan、2610.09690 NAViLoss、oceaneng.2026.128450 PSO 路径、oceaneng.2026.128720 波浪滑翔机、nmemc 环境智报、seabed2030 MEWO、toutiao 7694109833414443539、cftime v1.6.6.1、lom3.70099 seaEchoTSCalculator

- **已剔除（勿再收）**：OceanParcels v3.1.4 / v4.0（09-15 已发，v4.0.2 补丁不单列）、Fugro OCEANITY/EDITO、WavyOcean 3.0、HorizonNet(2018)、Fengyun-3/AOSL、MBARI MOLA、ICE-3D、ditto_summit2026、EX2606/EX2607 预告页、南海海洋大数据智能管理平台/南海孪境、s43247-026-03899-w 北极原住民、OSR 旧期预告、NA182、Voyis 船体检测、Robosys VOYAGER、2609.37964、2610.03888 REACT、OceanStream Globe/MyOcean Pro v17/CASPROD/GLODAPv3/EMSO EVOLVE/OceanEye、2610.03743 北极 SIC、2610.03739 SWOT 去噪、2610.17939 Sea-Net、2610.04449、WireClear-GS 2610.19753、OceanXL 2609.29985、essd-18-4617-2026 西太温盐场、OS 2903 北大西洋海平面、GMD MONKI 19-9677（行星大气）、JSTARS 3736460 GNSS-IR、rs18193402 VIIRS 透明度、essd-18-7345-2026 UVP5 数据库、中国大洋100 航次第二航段、中国第16次北冰洋考察、2610.09668 剖面浮标统计、NCEI WOA 密度/电导/MLD（2021 旧闻）、SWOT Sci Rep 2026-10-17（实为内陆水库）、NOAA GOMO 8 个 AI 试点（2026-10-01，超窗）、NIPS'25 NAUTILUS（2025 论文集）

## 经验教训
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
