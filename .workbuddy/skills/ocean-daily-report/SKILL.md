---
name: ocean-daily-report
description: >
  海洋AI研究日报生成技能。当用户要求"执行海洋AI研究日报"、"生成海洋日报"、"出今天的日报"
  或类似表达时使用。该技能覆盖 9大方向（海洋AI、数字孪生、可视化、数据质量、数据处理、
  数据管理与共享、航次科考、数据中心、工具资源）的内容搜集、去重、HTML生成、GitHub Pages发布、
  以及质量审查（链接验证+时效性审计）的完整流程。新用户首次使用时须先建立路径映射
  （见 references/file_locations.md），技能本身不依赖硬编码路径。
agent_created: true
---

# 海洋AI研究日报生成技能

## 概述

本技能为"海洋AI研究日报"任务提供完整的可重复工作流：从内容搜集到质量审查。日报覆盖 9 大方向，
**每方向 3-5 条**精选动态，**全日报 27-45 条**（某方向确无新内容时可为 0，见「常见陷阱 1」宁缺不凑数）。
产出物为 HTML 简报，发布到 GitHub Pages + 飞书文档。

## 前置条件

首次使用前，在 workspace MEMORY.md 中记录以下角色的实际路径（参见 `references/file_locations.md`）：

- `$DATA_SOURCE` — 日报数据源文件（`feishu_write_doc.py`，含 `SECTIONS = [...]` 占位）
- `$GH_REPO` — GitHub Pages 仓库根目录
- `$PYTHON` — Python 解释器路径

不需要预置 `build_daily.py` 和 `gen_html.py`，这些脚本可在生成时动态创建。

### 新用户初始化（三步走）

**Step 1 — 获取技能**：将技能目录复制到 `~/.workbuddy/skills/ocean-daily-report/`。

**Step 2 — 建立映射**：在 workspace MEMORY.md 中填写角色→路径映射。

**Step 3 — 初始化骨架文件**：

```
① 复制数据源模板：
   cp assets/template_feishu_write_doc.py → $DATA_SOURCE 路径
   （此文件含 9 方向 SECTIONS 占位 + feishu/docx 辅助函数）

② 初始化 GitHub Pages 仓库：
   python scripts/init_gh_repo.py $GH_REPO
   （自动创建 posts/、index.html、archive.html、style.css、.gitignore）

③ 关联远程仓库并首次推送：
   cd $GH_REPO
   git remote add origin <你的GitHub仓库URL>
   git add . && git commit -m "init: 海洋AI日报站点骨架"
   git push -u origin main

④ 在 GitHub repo 的 Settings → Pages 中：
   Source: Deploy from a branch
   Branch: main / (root)
```

完成后即可正常执行日报生成任务。

## 重要：本技能为手动/自动共享指令源（权威唯一来源）

本 skill 是**手动执行和自动化执行共用的唯一权威指令源**。无论以何种方式触发日报生成，都必须：
- 加载本 skill（自动化：阶段0强制加载；手动：对话开始时加载）
- 读取 `$WORKSPACE/.workbuddy/memory/MEMORY.md` 获取去重基准
- 执行完成后**严格按阶段六写入以下全部记忆文件**（手动与自动完全一致，不可因触发方式不同而产生差异）
- 如发现有新经验/新规则，同步更新本 skill 和 MEMORY.md

⚠️ **一致性铁律**：手动执行 ≠ 简化执行。手动触发的日报必须产出与自动化定时运行**完全相同**的工件与记忆文件，包括 `daily_reports/海洋AI简报_YYYY-MM-DD.html`、`posts/YYYY-MM-DD.html`、飞书文档、`.workbuddy/memory/YYYY-MM-DD.md`、以及 `MEMORY.md` 去重基准更新。任何"跳过某步"的做法都会造成记忆断层，必须避免。

⚠️ **跨机器铁律**（多台电脑执行时必须遵守）：记忆随 git 仓库同步，skill 随 `sync_skills.py` 同步。

1. **阶段零（执行前置）**：若当前不是主力机，或距上次执行可能有其他机器提交过，先执行 `git pull origin main`，再执行 `python sync_skills.py install`。**未拉取最新记忆就开始检索 = 去重基准过期 = 必然重复收录**。
2. **阶段六收尾**：记忆写入后必须 `git push origin main`，否则另一台机器下次执行会漏掉本期条目。
3. **禁止两台机器同一天并行执行**，会造成 git 冲突与内容重复。
4. skill 若在非主力机上被修改，需 `python sync_skills.py collect` 回收进仓库后 push，否则改动丢失。
5. 新机器完整配置步骤见仓库根目录 `SETUP_NEW_MACHINE.md`。

## 工作流总览

完整的日报生成分为 **6 个阶段**，按顺序执行，不得跳过：

### 阶段一：顶会论文与 IEEE 期刊检索（强制，不可跳过）

⚠️ **此阶段是 2026-07-31 质检后发现的最大盲区，必须在所有常规检索之前执行。**

**必须检索以下 23 个顶级会议 + IEEE 学术期刊**中与海洋/地球科学相关的 2026 年论文：

**第一梯队（高相关，10个）**：CVPR、ICCV、ECCV、NeurIPS、ICML、ICLR、AAAI、IJCAI、CoRL、MICCAI
**第二梯队（中相关，7个）**：ACL、EMNLP、NAACL、COLM、UAI、COLT、MLSYS
**第三梯队（低相关但纳入，6个）**：INTERSPEECH、IWSLT、NDSS、USENIX-Fast、USENIX-Sec、OSDI
**IEEE 学术期刊（强制，每期必查）**：JOE、TGRS、GRSL、JSTARS、GRSM（高相关）；T-RO、RA-L、TNNLS、TIP（方法迁移）。详见下文"IEEE 学术期刊清单"。

检索方法（每种都必须使用）：
1. **OpenReview**: `"ocean" OR "marine" OR "underwater" site:openreview.net`
2. **CVF Open Access**: https://openaccess.thecvf.com/search (搜索 underwater, marine, ocean)
3. **ACL Anthology**: https://aclanthology.org/search
4. **DBLP**: https://dblp.org/search?q=ocean+marine+underwater
5. **Papers with Code**: https://paperswithcode.com/search?q=ocean+marine+underwater
6. **Google Scholar**: `"<CONFERENCE> 2026" ocean OR marine OR underwater`
7. **WebSearch 通用**: 针对每个会议搜索 `CVPR 2026 underwater marine ocean` 等
8. **IEEE Xplore**: https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=ocean%20marine%20underwater （或 `site:ieeexplore.ieee.org ocean marine 2026`），按期刊筛选最近 1-2 期

筛选标准：方法应用型 > 方法可迁移型 > 纯方法型。Workshop/Tutorial 中涉及海洋的也收录。
日期以首次公开可访问日期为准（arXiv v1、OpenReview 公开日、**IEEE Xplore Early Access 日**）。

**此阶段必须产出 ≥5 条初筛结果**，如不足 5 条则扩大关键词（bathymetry, sea surface temperature, ocean current, plankton, coral, seafloor, AUV, ROV, sonar, acoustics, climate, remote sensing, **sea ice, Arctic, polar**）。

> ⚠️ **来源限定（2026-09-20 新增，堵住"arXiv 顶数"漏洞）**：
> 这 ≥5 条中**至少 2 条必须来自会议论文或 IEEE 期刊**（可为 OpenAlex `type:proceedings-article`、
> OpenReview、CVF/ACL Anthology、IEEE Xplore Early Access），**arXiv 预印本不得全额顶数**。
> 若某期确实检索不到会议论文（如 9 月中旬处于顶会周期空档：CVPR 6 月、ICCV 10 月、NeurIPS 12 月、
> IGARSS 7 月、OCEANS 9 月底），**必须用 `harvest.py` 的 `type:proceedings-article` 结果举证**，
> 并在日志写明"本期会议论文确为 0，已举证"。
> 历史教训：2026-09-20 期 IEEE Xplore 零覆盖的同时 arXiv 占比冲到 63%，即此漏洞所致。

常见陷阱：顶会论文日期歧义——以首次公开可访问日期为准，非会议召开日。详见 `references/quality_standards.md` 的"顶会论文日期规则"。

### 阶段二：常规来源检索

1. **读取历史日报**：从 `$GH_REPO/posts/` 读取**最近 12 期**日报（不是只看 5 份或 14 天），解析出已报道的事件/论文/产品，
   构建去重黑名单（同时参考 `$WORKSPACE/.workbuddy/memory/MEMORY.md` 的去重基准）。
   - `supplement` 分支自 2026-06-14 起已停更（最新提交 `4638ad5`），**当前不再纳入去重范围**；
     若该分支将来恢复更新，须重新纳入检查。
2. **逐方向搜索**：对 9 大方向逐一执行 WebSearch/WebFetch，搜索近两周（≤14天）的新内容。
   **每方向目标 3-5 条**；同一方向内若候选多于 5 条，**优先取近 7 天内发布的**（排序权重见
   `references/quality_standards.md` 的"近 7 天优先权重"）。
   预印本优先：arXiv physics.ao-ph, cs.CV, cs.LG；EarthArXiv；ESSOAr。
   ⚠️ **必须同时按下方「来源覆盖矩阵」逐项打卡**——9 方向表只给"主要来源"提示，
   不等于完整来源清单；仅按 9 方向表检索会长期漏掉长尾来源（见该节历史教训）。
   **打卡留痕（强制）**：每检索一组来源，就地记录"来源组 + 用过的关键词 + 命中条数"，
   阶段五据此复核覆盖率。**不得只在事后补写"已全覆盖"。**
3. **时效性预检**：**在搜集阶段**即标记每条素材的发布日期，
   剔除不满足条件的条目（规则见阶段六的 `references/quality_standards.md`）。
   ⚠️ **日期核实**：搜索引擎显示的日期可能是网页索引/修改日期，非原始发布日期。
   对于政策文件、战略计划、国际会议文档等，必须通过内容交叉验证（如摘要中提及的会议年份）
   或多源比对（如 AGRIS、OceanExpert）确认真实发布日期。详见 `references/quality_standards.md` 的"日期核实规则"。
4. **去重确认**：对比历史黑名单 + MEMORY.md 去重基准，剔除重复条目。

### 来源覆盖矩阵（每期必查 · 强制，不得遗漏）

> ⚠️ **历史教训（2026-07-31 迁移丢失，2026-09-15 复盘确认）**
> 2026-07-31 将自动化 prompt 重构为对本 skill 的"**纯委托**"（单一权威源，消除双源漂移）时，
> 原 prompt 中「**检索来源（每次执行必须全覆盖以下所有来源类型，不得遗漏）**」整节
> **没有被迁移进 skill**（初始版本 `3514a0b` 已实测：ProQuest/Semantic Scholar/DOAJ/CNKI/DockerHub/SeaDataNet/ISO/OGC 命中数均为 0）。
> 此后每期（手动+自动）都只在"9 大方向表"的"主要搜索来源"提示下检索，实际收敛为
> **arXiv / MDPI / CMEMS / NOAA / 国内政府网站** 五家，长尾来源连续 12 期零覆盖。
> **本节即为该约束的正式归宿。阶段二必须逐项打卡，阶段五必须复核覆盖率。**
>
> 迁移类教训通用规则：**把一份自包含提示词收敛为"纯委托 skill"时，必须逐条 diff 原提示词的约束清单，
> 确认每一条都在 skill 中有归宿——"精简"不等于"可以丢约束"。**

#### A 组 · 可直接检索（每期必须实际发起检索）

| 来源组 | 具体来源 | 检索方式 |
|--------|---------|---------|
| 预印本 | arXiv（physics.ao-ph / cs.CV / cs.LG）、EarthArXiv、ESSOAr | arXiv API 按 `submittedDate` 倒序；EarthArXiv/ESSOAr 走 `site:` 检索 |
| 学术索引 | Google Scholar、OpenAlex、Semantic Scholar、Crossref | OpenAlex/Crossref 用 API（`verify_paper.py` 已内置）；Scholar/Semantic 用 WebSearch |
| 开放获取聚合 | DOAJ | `site:doaj.org <关键词>` |
| 出版商（可直连） | EGU/Copernicus（Ocean Science、Biogeosciences、GMD、ESSD）、Frontiers、MDPI（RS/JMSE）、Springer Nature 及 Nature 子刊（Nat. Commun./Nat. Clim. Change/Sci. Rep.） | WebSearch + WebFetch；MDPI/Springer 遇 403 改用 `verify_paper.py` |
| 代码与发布 | GitHub Releases、PyPI、conda-forge、DockerHub | `site:github.com/<org>/releases`；PyPI JSON API `https://pypi.org/pypi/<pkg>/json` |
| 数据服务 | Copernicus Marine (CMEMS)、NOAA（NCEI / IOOS / CoastWatch / OceanReports / Okeanos）、PANGAEA、Argo GDAC、SeaDataNet、IODE/IOC-UNESCO、Euro-Argo ERIC、SEANOE | 各站 news / product / dataset 页 WebFetch |
| 标准与治理 | W3C、ISO、OGC、CF Conventions、OceanBestPractices、RDA | WebSearch + 站点 news |
| 中文平台 | 知网 CNKI、万方、维普；中科院/自然资源部/教育部高校发布 | `site:cnki.net`、`site:wanfangdata.com.cn`、`site:cqvip.com`；院所新闻巡检见「补充检索」节 |
| 科技媒体 | 国内：搜狐、腾讯、光明日报、科技日报、中国海洋报、中国科学报、新华网；国际：Eos（AGU）、Oceanography Magazine、MTS Journal | WebSearch |

#### B 组 · 需 API/间接访问（不能直爬，须走替代路径，并在日志注明"经 API 核实"）

| 来源 | 障碍 | 替代路径 |
|------|------|---------|
| Elsevier（ScienceDirect） | 403 反爬 | `verify_paper.py`（Crossref+OpenAlex）+ WebSearch 标题检索 |
| Wiley / AGU（JGR-Oceans、GRL、Earth's Future） | 403 反爬 | 同上；AGU/Eos 新闻稿作补充入口 |
| IEEE Xplore（JOE/TGRS/GRSL/JSTARS/GRSM/RA-L/T-RO/TNNLS/TIP） | 403 反爬 | `verify_paper.py` + `site:ieeexplore.ieee.org`（IEEE 期刊为**阶段一强制项**） |
| Taylor & Francis（J. Operational Oceanography） | 反爬 | `site:tandfonline.com` + `verify_paper.py` |
| SAGE（Progress in Oceanography） | 订阅 | 同上 |
| ACS（ES&T、ACS Earth Space Chem.）/ RSC（ES: Processes & Impacts） | 反爬 | 同上 |
| Science / AAAS | 订阅 + 反爬 | `site:science.org` + `verify_paper.py` |
| ACM Digital Library | 反爬 | `site:dl.acm.org` |
| IOP（Environmental Research Letters） | 反爬 | `site:iopscience.iop.org` |
| **ProQuest** | **商业数据库，无公开入口** | **不可直接检索**；学位论文/灰色文献改由 DOAJ + Google Scholar + 万方 覆盖，并在日志注明"ProQuest 无公开入口，已用 Scholar/DOAJ 替代" |

> B 组的正确用法：**发现 → 用 WebSearch 标题检索定位 → 用 `verify_paper.py` 核实元数据 → 用 WebFetch 复核**。
> 不要因为站点 403 就把整组来源从检索计划里划掉；也不要因为"点不开"就伪造链接（见「常见陷阱 10」）。

#### C 组 · 覆盖自检（阶段五新增，强制）

生成 HTML 后，除链接验证与时效审计外，**必须**执行来源覆盖自检：

1. **统计本期实际来源**：
   ```bash
   grep -oE 'https?://[a-zA-Z0-9._-]+' posts/YYYY-MM-DD.html | sed 's|https\?://||' | sort | uniq -c | sort -rn
   ```
2. **与近 12 期做覆盖率比对**，列出本期**零覆盖的来源组**（A 组 + B 组 + 阶段一的 23 会议/IEEE 期刊）。
3. 对零覆盖组逐条归因，只能落成三类之一：
   - `本期确无新内容`（须已实际检索过）
   - `检索无结果`（须给出用过的关键词）
   - `未检索` → **必须当场补检，不得留到下期**
4. 把覆盖率小结（含零覆盖组与归因）写入当日 `.workbuddy/memory/YYYY-MM-DD.md`。
5. **页脚声明必须与实际来源一致**：HTML 页脚不得硬编码未实际使用的来源
   （历史遗留 `Data sources: arXiv, GitHub, CMEMS, NOAA, CNKI and more` 中的 CNKI 实测从未使用过——
   `gen_html_*.py` 应改为按本期实际域名动态生成页脚，或至少删去未使用的来源名）。
6. **打卡留痕模板**（建议原样复制到当日日志，逐组填写后再写"已覆盖"）：
   ```text
   | 来源组 | 是否检索 | 关键词 | 命中 |
   |--------|---------|--------|------|
   | 预印本 arXiv/EarthArXiv/ESSOAr | Y/N | ... | n |
   | 学术索引 OpenAlex/Crossref/Scholar | ... | ... | n |
   | 出版商（Elsevier/Springer/Wiley/IEEE/T&F/SAGE/ACS/RSC/Science/IOP/MDPI/Frontiers/EGU/ACM） | ... | ... | n |
   | 开放获取 DOAJ | ... | ... | n |
   | 中文平台 CNKI/万方/维普 + 院所官网 | ... | ... | n |
   | 代码与发布 GitHub/PyPI/conda-forge/DockerHub | ... | ... | n |
   | 标准与治理 W3C/ISO/OGC/CF/OceanBestPractices/RDA | ... | ... | n |
   | 数据服务 CMEMS/NOAA/PANGAEA/Argo/SeaDataNet/IODE/SEANOE/Euro-Argo | ... | ... | n |
   | 科技媒体（国内官媒 + Eos/Oceanography/MTS） | ... | ... | n |
   | 阶段一：23 会议 + IEEE 期刊 | ... | ... | n |
   ```
   **判定门槛**：零覆盖组超过 **6 组** 即视为本轮检索不足，须回到阶段二补检后再收尾。

---

## 前沿跟踪四层架构（2026-09-20 苏老师拍板 · 新增）

> **背景**：日报是"精选摘要"，不是"跟踪工具"。实测近 14 天窗口内全海洋类期刊论文约 **2,249 篇**，
> 与海洋AI/数字孪生/数据类相关的约 **350 篇**，而日报只呈现 27–45 条（留存率约 10%）。
> 若只用日报一个出口，必然"看得到近的、看不到全的"。故增设 L0/L1 两层采集与承载，
> **日报（L2）质量红线不降级**：池内条目允许只有元数据，进日报的仍必须逐条核链、核时效、核摘要一致。

| 层 | 职责 | 产出物 | 工具 |
|----|------|--------|------|
| **L0 采集** | 9 方向查询模板 × OpenAlex/arXiv 全量抓取（T+1） | `data/pool/YYYY-MM-DD.jsonl` | `harvest.py` |
| **L1 文献池** | 去重（DOI/arXiv ID/标题指纹）+ 期刊分级 + 相关度打分 + 历史比对 | `data/library.db`、`data/pool_index.json` | `screen.py`、`tier_engine.py`、`source_metrics.py` |
| **L2 日报** | 从 S/A 级池中精选，逐条核实（现有流程，不变） | `daily_reports/`、`posts/` | `build_daily_*.py`、`gen_html_*.py` |
| **L3 新出口** | ① 前沿看板：全池可检索（方向/分级/时间/关键词）② 周报：池内统计驱动的趋势综述 | `frontier.html`、`weekly/` | 静态 JSON + 前端筛选 |

**执行顺序**：阶段二开始时**先跑 `harvest.py` + `screen.py`**，用池结果指导方向检索（池内已有的一律不重复找），
再补 A/B 组的人工检索（媒体、政策、代码发布等池覆盖不到的来源）。

```bash
py -3 harvest.py --date YYYY-MM-DD --days 14     # L0：约 3,000+ 条/14 天
py -3 source_metrics.py --limit 400              # 期刊指标缓存（首次可分批）
py -3 screen.py --date YYYY-MM-DD                # L1：分级+打分 → 约 300 条入池
```

### 期刊分级口径（2026-09-20 苏老师拍板，权威）

判定顺序：**预印本升级 → 人工登记表 → 最新一期预警/剔除名单 → 出版集团规则 → 指标自动评级 → 待确认**

| 等级 | 含义 | 举例 |
|------|------|------|
| **S** | Science / Nature / PNAS **正刊及顶级子刊**（最高优先级） | Nature, Science, PNAS, Nature Climate Change, Nature Geoscience, Nature Sustainability, Nature Communications, Communications Earth & Environment, Science Advances, npj Ocean Sustainability |
| **A** | 领域权威期刊（学会旗舰刊、高影响力子刊） | JGR: Oceans, GRL, RSE, IEEE TGRS, IEEE JOE, Ocean Modelling, Progress in Oceanography, ESSD, Ocean Science, GMD, Biogeosciences, ICES JMS, JPO, **Scientific Reports**（2026-09-20 确认）、**Ocean Engineering**（确认）、**npj Heritage Science**（由 S 下调，确认） |
| **B** | 主流 SCI 期刊；**中文刊按各学科影响因子排名前 25%** | Marine Pollution Bulletin, Applied Ocean Research, Ocean Dynamics, Marine Geology, Marine Policy, Acta Oceanologica Sinica, **海洋学报**、**遥感学报** |
| **C** | 一般期刊 / 新刊 / 开放获取集团刊；中文普通核心 | **Frontiers 全集团**、PLOS ONE、Heliyon、PeerJ、**海洋科学**、**中国海洋大学学报**、热带海洋学报 |
| **P** | 预印本**无期刊版本**时独立标记，排序低于 S/A 期刊论文 | arXiv, EarthArXiv, ESSOar |
| **D** | **预警 / 受限期刊（强制标注，不删除，供人工取舍）** | MDPI 全集团刊（JMSE/Remote Sensing/Water/Sensors/Sustainability/Fishes/Oceans…）、Hindawi 系、中科院与中信所预警名单刊、**SCI(SCIE)/EI 剔除刊** |

**四条硬规则**：
1. **期刊质量优先于一切**：同等相关度下 S > A > B > C > P > D，D 级强制置底。
2. **预警刊不得静默剔除**：必须保留 + 在标题处标注原因（哪个名单、哪一年），由苏老师取舍；
   标注不是论文评价，不否定该刊全部成果。
3. **预警/剔除名单只用最新一期**：中科院官方明确"不应把多年累积列表合并使用"，整改移出后即不再预警。
   名单数据存于 `data/journal_tiers.json` 的 `warning_lists`，`active` 字段控制是否生效。
4. **预印本升级（时效优先，2026-09-20 苏老师新增）**：预印本若**已对应期刊论文**，按**所属期刊等级**排序
   （不再一律压到 P 之下），并保留"预印本"标注。匹配依据依次为：① 同一 DOI 的期刊记录 →
   ② 同一标题（归一化指纹）的期刊记录 → ③ arXiv `journal_ref` 解析出的刊名。均未命中才归 P。
   理由：预印本是最快的时效渠道，不应因其形态被降级；发现新成果的时间点以预印本首发日计。

**中文期刊口径（2026-09-20 确认）**：按**各学科影响因子排名**分档（《中国学术期刊影响因子年报》学科分区 /
CNKI 学科排名）——学科前 25% → B，其余 → C 并标注。已确认：海洋学报 B、遥感学报 B、海洋科学 C、
中国海洋大学学报 C、热带海洋学报 C。

**指标自动评级阈值（2026-09-20 整体下调，海洋/地学类 h-index 普遍低于生物医学）**：
| 等级 | 条件 |
|------|------|
| A | `h ≥ 90 且 两年均被引 ≥ 2.5`，或 `h ≥ 200` |
| B | `h ≥ 35 且 两年均被引 ≥ 1.2`，或 `h ≥ 90`，或 `两年均被引 ≥ 4.0` |
| C | `h ≥ 8` 或 `两年均被引 ≥ 0.5`；低于此线仍归 C 但标注「指标偏低，建议复核」 |

- 由 **OR 改为双条件**，避免巨型综合刊（年发文 > 2500）指标虚高误判；该类刊自动降一级并标注。
- 自动评级结果一律带「未登记，待校准」标记，进入问答式校准流程。实现在 `tier_engine.py::auto_tier`。

**已知名单（2026-09-20 核实）**：
- 中科院文献情报中心 2025 年（2025-03-19 发布，5 本）：Wireless Personal Communications、Natural Resources Forum、
  Computers & Electrical Engineering、Numerical Heat Transfer Part A-Applications、Scalable Computing-Practice and Experience
- 中信所 2025 年（2025-12-07 发布，103 本；本表仅录入已核实条目）：Agronomy、Coatings、Genes、Chemosphere、
  Computers in Biology and Medicine、IEEE Transactions on Intelligent Vehicles、Environmental Toxicology、
  Bioengineered、Cureus、Frontiers in Microbiology/Endocrinology/Energy Research/Cell and Developmental Biology 等
- **EI Compendex DISCONTINUED（2026-07-09 更新，全表 228 条）**：本表录入 `Final Coverage ≥2022` 的 **19 条近期剔除刊**
  （Scalable Computing、Computational Intelligence and Neuroscience、Computer Systems Science and Engineering、
  Waves in Random and Complex Media、Neutrosophic Sets and Systems、Data and Metadata 等）；早年已停检的 209 条归 `EI剔除存档`
  （不生效，仅备查）。数据源：`https://www.ei-cn.com/News/309.html`
- **Web of Science 核心合集剔除（Clarivate 2025-12 ～ 2026-07 月度更新，SCIE/SSCI 部分）**：本表录入已核实的 **16 条**，
  含本领域相关的 **Sea Technology（2026-02 Cease）**、Ingegneria Sismica、Traitement du Signal、
  Mechanics of Advanced Materials and Structures 等。ESCI 变动量过大未全录，需按需补录。
- **待办**：中信所完整 103 本名单、WoS ESCI 剔除完整名单需继续导入 `data/journal_tiers.json`

### 期刊分级问答式校准（每期可执行）

自动评级无法覆盖所有期刊。**未登记期刊自动进入待确认清单**，由苏老师用问答方式确认后入库，
不需要苏老师手工整理样例：

1. 每期筛选后查看清单：`py -3 tier_engine.py --pending`，或读 `data/pending_journals.txt`（按命中篇数降序）
2. 在日报交付时**只挑命中 ≥2 篇的期刊**（通常 5–10 本）向苏老师提问，格式：
   > 「《Ocean Engineering》命中 3 篇，当前自动评级为 A。请确认：维持 A / 升为 S / 降为 B？」
3. 苏老师回复后写入 `data/journal_tiers.json` 的 `journals` 段（登记表优先于自动评级），并记入日志。

### 每期必报的覆盖指标（写入当日日志）

| 指标 | 口径 | 目标 |
|------|------|------|
| 采集量 | `harvest.py` 原始条数 | 记录即可 |
| 池内量 | `screen.py` 池内条数 | 记录即可 |
| 日报收录 | 本期有效条数 | 27–45 |
| 留存率 | 日报 / 池内 | 记录即可（透明化，不设阈值） |
| **arXiv 占比** | arXiv 条数 / 日报条数 | **≤ 50%** |
| **期刊来源占比** | 期刊条数 / 日报条数 | **≥ 40%** |
| 零覆盖来源组 | C 组自检 | ≤ 6 组 |

### 阶段三：编写数据

1. 构建 sections 数据结构，格式如下：
   ```python
   {
       "title": "一、海洋人工智能",
       "en": "Ocean AI / Marine Artificial Intelligence",
       "items": [
           {
               "title": "条目标题（含来源和日期）",
               "badge": "[论文]",  # [论文]/[要闻]/[动态]/[工具]/[数据]/[报告]/[政策]/[航次]/[开源]/[关注]
               "abstract": "2-4句摘要",
               "source": "期刊/机构",
               "url": "https://...",
               "date": "2026-06-XX"
           }
       ]
   }
   ```
2. **用 Write 工具**将 sections 数据写入 `$WORKSPACE/build_daily.py`。
   ⚠️ **不要用 bash heredoc**：中文内容会乱码。
   ⚠️ **字符串值统一用单引号**，避免双引号嵌套导致 SyntaxError。
3. **归类自检（写入文件前必须执行）**：对每条内容逐条回答"这条内容的核心主题是否与所在方向的定义匹配？"
   不匹配的要么移到正确方向，要么删除。判定标准见 `references/quality_standards.md` 的「方向归类严格规则」。
   自检结果（改归/删除了几条）记入当日日志。
4. 执行 `$PYTHON $WORKSPACE/build_daily.py`，通过正则替换将 SECTIONS 写入 `$DATA_SOURCE` 第18行。
5. 生成 HTML 脚本 `$WORKSPACE/gen_html.py`（读取 DATA_SOURCE → 生成 `海洋AI简报_YYYY-MM-DD.html`）
   并执行。

### 阶段四：发布

1. 复制 HTML 到 `$GH_REPO/posts/YYYY-MM-DD.html`
2. 更新 `$GH_REPO/index.html`：在最新 post-card `<div>` 之前插入新卡片
3. 更新 `$GH_REPO/archive.html`：在 `<ul>` 列表顶部插入新条目
4. Git 操作：
   ```bash
   cd $GH_REPO
   git pull --rebase origin main
   git add posts/YYYY-MM-DD.html index.html archive.html
   git commit -m "publish: YYYY年MM月DD日 海洋AI技术日报"
   git push origin main
   ```
   - **git push 必须在 Bash 中执行且 `dangerouslyDisableSandbox: true`**（Windows 下 PowerShell 编码问题会导致失败）。
   - rebase 冲突时：`GIT_EDITOR=true git rebase --continue`
   - ⚠️ **先 commit+push，再做任何本地 HTML 预览**（预览会注入 `data-page-node-id` 属性污染文件，见「常见陷阱」）。
5. **推送飞书文档**：执行 `$PYTHON $DATA_SOURCE`（即 `feishu_write_doc.py`），把 SECTIONS 内容推送到飞书文档。
   - 若飞书 API 超时/404，**不阻断发布**：如实记入当日日志（含错误码），GitHub Pages 侧照常产出。
6. **发送飞书机器人通知**：执行 `$PYTHON $RUN_DAILY_REPORT`（`run_daily_report.py`）。
   - 未配置 `FEISHU_WEBHOOK_URL` 时脚本会跳过，记入日志即可，不视为失败。

> **关于 `deploy_report.py`**：旧流程用它发布到 GitHub Pages，现已由第 4 步的直接 `git push` 取代
> （更可控、可 review diff）。该脚本**已废弃，不再调用**；若保留在仓库中仅作历史参考。

### 阶段五：质量审查

加载 `references/quality_standards.md` 执行**五项审查**（缺一不可）：

1. **链接有效性与摘要一致性**：
   - **有效性**：逐条验证所有 href 是否返回 200。失效链接须搜索替代来源，修复后重新生成 HTML + 重新 push。
   - **一致性（易漏）**：逐条核对简报摘要与原文内容是否相符——摘要须准确反映原文核心观点，
     **不得出现与原文不符的表述，也不得把相邻条目的事实张冠李戴**。摘要里的关键数字（精度、天数、分辨率、
     样本量、金额、台站名）必须在原文中能找到出处。
   - ⚠️ 部分中国学术期刊网站（如 jao.org.cn）会返回 403 Forbidden（反爬虫机制），
     此时通过搜索引擎确认文章存在且内容一致即可判定链接有效。
   - ⚡ **MDPI / ScienceDirect / Wiley / IEEE 等反爬站点：优先用 `verify_paper.py`（Crossref + OpenAlex 官方 API）核实元数据**，
     一次拿到标题/期刊/作者/发表日期/摘要，不受 403 影响、比 WebFetch 更快更准。详见 `references/quality_standards.md` 的"反爬站点核实规则"。
2. **时效性审计**：用 Python 提取所有条目日期，计算距今天数，
   标出 >7天 / >14天 / >60天 的条目。不合格条目须替换或标注豁免理由。
   **同方向内若有 >7 天的条目与 ≤7 天的条目并存，须优先保留近 7 天的**（排序权重规则）。
   `verify_paper.py` 已内置时效判定（OK / 需豁免 / 超期），可直接复用。
3. **来源覆盖自检**：按上文「来源覆盖矩阵 · C 组」统计本期实际来源域名，
   与近 12 期比对，列出零覆盖来源组并逐条归因（确无新内容 / 检索无结果 / 未检索→当场补检）。
   ⚠️ **不得只在日志里写"已全覆盖"**——跨机器接手时对方日志的质检自述不可采信（见「常见陷阱 12」），
   必须给出域名清单或命令输出作为证据。
4. **归类与条目数终检**：对照 `references/quality_standards.md` 的「方向归类严格规则」复核每条归属；
   统计各方向条数，**目标每方向 3-5 条**（某方向确无新内容时可为 0，不得凑数）。
5. **去重复核**：URL 集合差（本期 vs 近 12 期）+ 关键词/DOI/卷期号 grep，确认 0 重复。

### 阶段六：记忆写入（不可跳过，手动与自动完全一致）

任务完成后**必须**写入以下全部记忆工件，手动触发与自动化定时运行写入**完全相同**的文件、相同的内容结构：

1. **每日工作日志** `$WORKSPACE/.workbuddy/memory/YYYY-MM-DD.md`
   - 追加（不覆盖）执行日志：条目数、覆盖方向、关键发现、异常说明（如飞书API 404、WEBHOOK 未配置、git冲突解决等）
   - **必含三项留痕**：① 阶段二的来源检索打卡（来源组 + 关键词 + 命中数）；
     ② 阶段三的归类自检结果（改归/删除几条、原因）；③ 阶段五的来源覆盖率小结（零覆盖组 + 归因）。
   - 若文件不存在则创建
2. **去重基准** `$WORKSPACE/.workbuddy/memory/MEMORY.md`
   - 在本期"去重基准（滚动更新）"小节中追加本期核心条目（标题 + 日期 + 方向），供未来去重检索
3. **经验沉淀**
   - 如发现本 skill、quality_standards 或 MEMORY.md 中有遗漏的规则/新经验，立即更新
4. **（可选但推荐）自动化执行摘要** `$WORKSPACE/.workbuddy/automations/ai/memory.md`
   - 手动执行时若希望与自动运行共用一条执行历史，可在该文件追加本期高层面执行摘要（条目数、是否部署、异常）
   - 目的：使"手动 vs 自动"在回顾时有统一视图，杜绝记忆断层

⚠️ 手工执行**不得**省略以上任一步骤。阶段六与阶段三是保证"记忆一致"的两道关卡：阶段三确保 `daily_reports/海洋AI简报_YYYY-MM-DD.html` 源文件落盘，阶段六确保记忆落盘。

## 9大方向与搜索策略

> **规模口径**：每方向目标 **3-5 条**（全日报 27-45 条）；某方向确无新内容时**可为 0，不得凑数**。
> 本表只给"主要来源"**提示**，**不等于完整来源清单**——每期必须同时按上文「来源覆盖矩阵」逐组打卡。

| # | 方向 | 主要搜索来源 | 搜索关键词示例 |
|---|------|-------------|---------------|
| 1 | 海洋人工智能 | arXiv physics.ao-ph, **顶会论文(强制检索23个会议)**, **IEEE期刊(JOE/TGRS/GRSM)**, Nature, npj 系列, 国内新闻 | "ocean AI deep learning 2026", `"CVPR 2026" underwater marine`, "海洋大模型 2026", **"Arctic sea ice deep learning", "北极海冰 AI 遥感", "sea ice remote sensing review 2026"** |
| 2 | 海洋数字孪生 | CMEMS, NOAA, 国内政策, **顶会论文(MLSys/NeurIPS)** | "digital twin ocean 2026", "海洋数字孪生 最新" |
| 3 | 海洋可视化 | CMEMS MyOcean, GitHub, 学术工具, **顶会论文(CVPR/ICCV/ECCV)** | `"CVPR 2026" ocean visualization`, "ocean visualization tool 2026" |
| 4 | 海洋数据质量 | Springer, Argo, GOOS, **顶会论文(ICML/NeurIPS)**, **IEEE期刊(TGRS/GRSL)** | `"ICML 2026" ocean data quality`, "Argo quality control machine learning 2026" |
| 5 | 海洋数据处理 | arXiv, Nature Sci Data, **顶会论文(NeurIPS/ICLR)**, J. Oceanography, **IEEE期刊(TGRS/JSTARS)** | `"NeurIPS 2026" ocean data`, "ocean data processing AI 2026", "SST super-resolution sea ice dataset 2026" |
| 6 | 数据管理与共享（**含地质样品共享**、数据共享平台） | IOC, EMODnet, 信通院, CMEMS | "ocean data sharing FAIR policy 2026", "geological sample sharing", "海洋地质样品 共享" |
| 7 | 开放航次与科考（**含船时共享**） | NOAA Ocean Exploration, 高校科考新闻, **顶会论文(CoRL/ICRA)** | "NOAA Okeanos Explorer 2026", "海洋科考 2026", "ship time sharing", "船时共享" |
| 8 | 海洋数据中心 | GEBCO, ECCO, 国内海洋数据中心 | "GEBCO 2026", "ECCO update" |
| 9 | 工具与代码资源 | PyPI, GitHub, **顶会论文开源代码**, 学术工具论文 | `"ICLR 2026" ocean code release`, "oceanography Python package release 2026" |

### 补充检索：国内海洋所新闻巡检（每期必查）

国内主要海洋研究机构官网"科研进展"栏目常发布**顶刊论文新闻稿**（重磅综述/里程碑论文），搜索引擎关键词不易覆盖，**每期必须主动巡检**：

| 机构 | 官网路径 | 巡检内容 |
|------|---------|---------|
| 中科院海洋研究所（青岛） | `qdio.cas.cn/2019Ver/News/kyjz/` | 海洋AI、遥感、海冰/极地、数据方向论文新闻 |
| 中科院南海海洋研究所（广州） | `gzb.cas.cn/kyj/` | 南海/热带海洋研究动态 |
| 自然资源部第一/第二/第三海洋研究所 | 官网"科研动态" | 海洋遥感、数据处理、极地 |
| 中国极地研究中心 | `chinare.org.cn` 新闻 | 极地/海冰遥感与AI |

> ⚠️ **教训案例（2026-08-31）**：中科院海洋所 08-26 发布《Deep Learning Applications in Arctic Sea Ice Remote Sensing: A Review》（IEEE GRSM, IF 13.7, 任沂斌一作/李晓峰通讯）新闻稿，三期日报（08-25/08-26/08-31）均因**检索关键词未覆盖"海冰/极地"主题**而遗漏。该文完全符合收录条件（顶级期刊综述+发布5天内）。**此后每期检索必须包含 "Arctic sea ice" / "北极海冰" / "极地遥感" 关键词，并巡检上表国内机构新闻栏目。**

### 顶级期刊综述检查（每期必查）

**IEEE GRSM / RSE / Reviews of Geophysics / Nature Reviews Earth & Environment / OLAR 等期刊的重磅综述**属于"顶级来源"，即使发布超过14天，只要 ≤60 天且不与历史重复，可按重要性豁免收录。检索时对以下期刊单独查询最近1-2期目录或新闻稿：
- IEEE Geoscience and Remote Sensing Magazine（GRSM, IF≈13.7）
- Remote Sensing of Environment（RSE）
- Nature Reviews Earth & Environment
- 中文顶刊综述（《海洋学报》《海洋科学进展》等）

## 顶会论文与期刊检索

在阶段一搜索时，除 arXiv 和新闻来源外，**必须检索以下顶级会议与 IEEE 期刊**中与海洋/地球科学相关的论文。
这些会议与期刊涵盖了计算机视觉、机器学习、NLP、机器人、系统安全等领域中可能应用于海洋AI的方法论和工作。

### 会议清单（按相关度分组）

#### 第一梯队：高相关（海洋AI直接受益）

| 会议缩写 | 全称 | 领域 | 海洋相关切入点 |
|---------|------|------|---------------|
| CVPR | IEEE/CVF Conference on Computer Vision and Pattern Recognition | 计算机视觉 | 水下图像增强/恢复、海洋生物分割与检测、遥感海洋观测 |
| ICCV | International Conference on Computer Vision | 计算机视觉 | 同 CVPR，水下场景理解、海洋遥感 |
| ECCV | European Conference on Computer Vision | 计算机视觉 | 同 CVPR |
| NeurIPS | Conference on Neural Information Processing Systems | 机器学习 | 海洋预报模型、气候建模、物理启发的神经网络 |
| ICML | International Conference on Machine Learning | 机器学习 | 海洋数据同化、时空预测、科学机器学习 |
| ICLR | International Conference on Learning Representations | 深度学习 | 表征学习在海洋/气候中的应用 |
| AAAI | AAAI Conference on Artificial Intelligence | 人工智能 | 海洋环境智能监测、AI在海洋的应用 |
| IJCAI | International Joint Conference on Artificial Intelligence | 人工智能 | 同 AAAI |
| CoRL | Conference on Robot Learning | 机器人学习 | 水下机器人自主学习、AUV/ROV 控制 |
| MICCAI | Medical Image Computing and Computer Assisted Intervention | 医学影像 | 分割/检测方法可迁移至海洋生物影像 |

#### 第二梯队：中相关（方法迁移与交叉应用）

| 会议缩写 | 全称 | 领域 | 海洋相关切入点 |
|---------|------|------|---------------|
| ACL | Annual Meeting of the Association for Computational Linguistics | 自然语言处理 | 海洋科学文献挖掘、科学LLM |
| EMNLP | Conference on Empirical Methods in Natural Language Processing | 自然语言处理 | 同 ACL |
| NAACL | North American Chapter of the Association for Computational Linguistics | 自然语言处理 | 同 ACL |
| COLM | Conference on Language Modeling | 语言模型 | 海洋领域大语言模型 |
| UAI | Conference on Uncertainty in Artificial Intelligence | 不确定性量化 | 海洋预报不确定性、贝叶斯海洋建模 |
| COLT | Conference on Learning Theory | 学习理论 | 理论保证（较少直接应用但提供基础） |
| MLSYS | Conference on Machine Learning and Systems | ML系统 | 海洋大数据处理管道、分布式训练 |

#### 第三梯队：低相关但纳入检索

| 会议缩写 | 全称 | 领域 | 海洋相关切入点 |
|---------|------|------|---------------|
| INTERSPEECH | Annual Conference of the International Speech Communication Association | 语音处理 | 海洋科考语音数据、声学海洋学 |
| IWSLT | International Conference on Spoken Language Translation | 语音翻译 | 多语言海洋科考协作 |
| NDSS | Network and Distributed System Security Symposium | 网络安全 | 海洋观测网络安全、数据基础设施安全 |
| USENIX-Fast | USENIX Conference on File and Storage Technologies | 存储系统 | 海洋大数据存储架构 |
| USENIX-Sec | USENIX Security Symposium | 安全 | 同 NDSS |
| OSDI | USENIX Symposium on Operating Systems Design and Implementation | 操作系统 | 海洋数据基础设施系统设计 |

### 检索方法

1. **OpenReview 检索**（覆盖 ICLR, NeurIPS, COLM, UAI 等）：
   - 搜索 `"ocean" OR "marine" OR "underwater" site:openreview.net`
   - 或访问 `https://openreview.net/search?term=ocean+marine&group=<会议group>`

2. **会议官网/论文集检索**（覆盖 CVPR, ICCV, ECCV, ACL, EMNLP 等）：
   - 搜索 `"<CONFERENCE> 2026" ocean OR marine OR underwater OR "sea surface" OR bathymetry`
   - CVPR/ICCV/ECCV 可用 `CVF Open Access` 搜索：`https://openaccess.thecvf.com/search`
   - ACL/EMNLP/NAACL 可用 `ACL Anthology` 搜索：`https://aclanthology.org/search`

3. **DBLP 检索**（全会议覆盖）：
   - 访问 `https://dblp.org/search?q=ocean+marine+underwater`
   - 可按会议筛选结果

4. **Papers with Code 检索**（寻找带开源代码的论文）：
   - 访问 `https://paperswithcode.com/search?q=ocean+marine+underwater`

5. **Google Scholar 定向检索**：
   - `"<CONFERENCE> 2026" "ocean" OR "marine" OR "underwater"`
   - 可叠加关键词：`bathymetry`, `sea surface temperature`, `ocean current`, `plankton`, `coral`, `seafloor`

6. **IEEE Xplore 期刊检索**（覆盖全部 IEEE 期刊，每期必查）：
   - 访问 `https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=ocean%20marine%20underwater`
   - 或搜索 `site:ieeexplore.ieee.org ocean marine 2026`
   - 建议按期刊筛选（见下方 IEEE 学术期刊清单），优先查看**最近 1-2 期**的 Early Access / 最新论文
   - 论文日期以 **IEEE Xplore 上的出版日期**为准（Early Access 日期即为首发日，按此判定时效）

### IEEE 学术期刊清单（每期必查）

IEEE 旗下期刊是海洋AI/遥感方向的重要来源，与顶会论文同等优先级。按相关度分组：

#### 高相关（海洋/遥感直接对口）

| 期刊缩写 | 全称 | 领域 | 海洋相关切入点 |
|---------|------|------|---------------|
| JOE | IEEE Journal of Oceanic Engineering | 海洋工程 | 海洋观测系统、水下声学、AUV/ROV、海洋仪器 |
| TGRS | IEEE Transactions on Geoscience and Remote Sensing | 遥感 | 海表温度/盐度反演、海冰遥感、SAR海洋应用、遥感深度学习 |
| GRSL | IEEE Geoscience and Remote Sensing Letters | 遥感（快报） | 同 TGRS，短篇快讯时效更高 |
| JSTARS | IEEE J. Sel. Topics in Applied Earth Obs. & Remote Sensing | 遥感应用 | 海洋遥感应用、数据立方体、深度学习遥感 |
| GRSM | IEEE Geoscience and Remote Sensing Magazine | 遥感（综述/顶刊, IF≈13.7） | **重磅综述**（如北极海冰深度学习综述）、应用综述 |

#### 中相关（机器人/AI 方法迁移）

| 期刊缩写 | 全称 | 领域 | 海洋相关切入点 |
|---------|------|------|---------------|
| T-RO | IEEE Transactions on Robotics | 机器人 | 水下机器人规划、自主导航 |
| RA-L | IEEE Robotics and Automation Letters | 机器人快报 | AUV/ROV 感知与控制、水下抓取 |
| TNNLS | IEEE Trans. on Neural Networks and Learning Systems | 神经网络 | 海洋时序预测、时空深度学习 |
| TIP | IEEE Transactions on Image Processing | 图像处理 | 水下图像增强/恢复 |
| TGRS 系列同源 | IEEE Trans. on Computational Imaging / Instrumentation & Measurement | 成像/测量 | 海洋传感器数据处理 |

#### 检索提醒
- **GRSM 综述优先**：GRSM 每期 1-2 篇重磅综述，属于"顶级来源"豁免范畴（≤60 天可收录），是本期遗漏教训的直接对策（见 2026-08-31 复盘）
- **TGRS/GRSL 海冰主题**：检索时叠加 `sea ice`、`Arctic`、`polar` 关键词（与 8/31 教训联动）
- **Early Access 日期即首发日**：IEEE 论文以 Xplore 上线日为 `date` 字段，非正式卷期日

### 筛选标准

- **方法应用型**：顶会论文中直接将AI方法应用于海洋/水下场景的——优先收录
- **方法可迁移型**：方法本身通用但在论文中使用了海洋数据集验证的——次优先收录
- **纯方法型**：方法未涉及海洋但可明显迁移的（如时空预测、遥感分割）——仅在对应方向无直接海洋论文时酌情收录，需在摘要中说明迁移路径
- 会议 workshop/tutorial 中涉及海洋AI的也值得关注

## 技术注意事项

### 跨平台兼容
- Python 路径：优先用 `$PYTHON`（workspace MEMORY.md 中记录）
- 中文编码：bash heredoc 不兼容中文，始终用 Write 工具写 `.py` 文件
- Git push：Windows 下必须 Bash + `dangerouslyDisableSandbox: true`

### 新用户接入
首次使用技能时：
1. 加载 `references/file_locations.md` 了解角色定义
2. 在工作区定位关键文件，在 workspace MEMORY.md 中建立角色→路径映射
3. 确保 `$DATA_SOURCE` 中存在 `SECTIONS = [...]` 占位行（第18行附近）

## 常见陷阱

1. **凑数思维**：某方向无新内容时不要填充旧素材，减少条目或标注"本周暂无明显进展"
2. **跳过时效性检查**：搜集时就要标记日期，不要在最后才审计——那时已浪费了大量时间写入旧内容
3. **忘记去重**：必须先读历史日报做黑名单，不要在已写完后才发现重复
4. **链接不验证**：每次 push 后必须验证，失效链接损害读者信任
5. **搜索引擎日期误用**：搜索引擎旁显示的日期可能是网页索引日期而非发布日期，导致旧内容以"近期"日期混入日报。对政策/战略/会议类文档必须交叉验证实际发布年份
6. **工具版本号未核实**：搜索到的PyPI包版本可能不是最新版。工具类条目（第9方向）需在PyPI或pyrank.org确认最新版本号后再写入日报，避免报告已过时的版本
7. **中国学术期刊反爬虫403**：jao.org.cn等中国学术期刊网站对WebFetch返回403 Forbidden。此时通过搜索引擎确认文章存在且内容（DOI、标题、作者、数据）一致即可判定链接有效
8. **顶会论文日期歧义**：会议论文有多个日期——投稿日、录用日、arXiv预印本日、OpenReview公开日、会议召开日、正式出版日。默认以**首次公开可访问日期**为准（arXiv v1 或 OpenReview 公开日）。**例外**：当以"顶会录用/召开"为新闻时点时，可用会议接收/举办日期作为条目 `date`（标题标注会议来源，且摘要须注明预印本原始公开日）；纯预印本（无会议录用）不得套用会议日期。详见 `references/quality_standards.md` 的"顶会论文日期规则"
9. **用户指定条目与去重规则冲突**：用户可能点名要求把某篇论文/新闻加入当天日报，而它其实已在往期收录。处理流程（**不做默默照做，也不做默默拒绝**）：
   1. 先 `grep` 历史 `posts/*.html` 确认是否收录、收录在哪一期、用的是什么链接；
   2. 再检索原文（期刊页/DOI/IEEE Xplore）确认往期之后**是否出现新进展**（正式卷期上线、修订、撤稿、数据更新、获奖等）；
   3. 把结论连同三个选项交给用户拍板：① 不重复收录（遵守去重铁律）② 以新信源/新进展标注"更新"补录 ③ 原样重复收录；
   4. 用户确认后，必须在本期日志与 `MEMORY.md` 去重基准中写明"**该条目永久归属 YYYY-MM-DD 期，后续不再收录**"，形成闭环，避免同一问题反复提出。
   > 案例：IEEE GRSM 北极海冰综述（doi:10.1109/MGRS.2026.3720616）原始发布 08-26，09-02 期已补录；09-04 用户再次要求加入，核实无新进展后经确认维持不收录，已在 MEMORY.md 标注永久归属 09-02。

10. **臆造 URL（按模式猜测）**：**严禁凭 URL 模式推断链接**。2026-09-14 期出现两条 `mnr.gov.cn/dt/hy/202609/t20260911_2830895.html` / `_2830896.html`，是按自然资源部既有 URL 规则拼出来的，实测**双 404**，该栏目真实 ID 段为 2938xxx（非 2830xxx），站内根本没有对应稿件。
    - **铁律**：每条 `url` 必须实测返回 200 才可入库（阶段五不可省）。
    - 当检索结果里只有转载稿、找不到原始媒体直链时，**改用可访问的权威转载源并如实标注转载关系**（如"新华社（记者温竞华）· 经川观新闻转载"），**绝不"造"URL**。

11. **批量抓同一期刊整期导致跨期重复**：按 MDPI 某一期（如 JMSE 14(16)）批量取稿极易撞历史条目。2026-09-14 期从 JMSE 14(16) 取了 1453/1462 两条，**分别已在 08-18 期与 08-10 期收录**，且 08-21、08-31 两期还在"暂无新增"占位里明确写过"DTF-Net 已收录"。
    - **铁律**：期刊整期批量取稿时，**每个 DOI 尾号都要单独 `grep posts/`**，不能只对新取到的 URL 做一次集合比对——集合比对能发现同 URL 重复，但挡不住"同一期不同文章此前已各自收录过"这种情况。
    - 更稳的做法：比对时不只比 `href`，同时用**论文标题关键词 + 期刊卷期号 + 作者**三路 grep。

12. **轻信其他机器的质检自述**：跨机器接手时，对方日志里的质检结论不可直接采信。2026-09-14 另一台机器日志自称"`grep -rl posts/` 跨期去重：无重复""所有条目 ≥2026-08-31（≤14 天）"，**实测两项均不成立**（3 处跨期重复；2 条为 08-07 / 08-08）。
    - **铁律**：跨机器接手必须**独立复算**——URL 集合差（本期 vs 近 12 期）+ 时效差（逐条 `datetime` 差值）。
    - 接手发现缺陷时，按"改数据源 → 重新生成 HTML → 同步 index/archive → 重新质检 → commit+push"完整闭环修复，不要在已发布 HTML 上做散点修补（会与 `build_daily_*.py` 源文件脱钩）。

13. **链接指向站点首页**：条目 `url` 不得用机构/平台首页（如 `emodnet.ec.europa.eu/en/`），必须给到**承载该条内容的页面**（数据产品页、文章页、release 页）。阶段五质检应专门扫一遍"是否有点向首页的 URL"。

14. **"纯委托"重构时静默丢失约束**：把自包含 prompt 收敛为"唯一权威源 skill"能消除双源漂移，但**收敛过程本身会丢约束**。2026-07-31 的改造就丢掉了整节「来源全覆盖清单」，直到 2026-09-15 才被发现——期间每期都少检索了 10+ 组来源，且因为 skill 是唯一权威源，**缺口被自动继承、无人再提**。
    - **铁律**：任何"prompt → skill"或"skill A → skill B"的迁移，**必须逐条 diff 原文本的约束清单**，并逐条确认在新载体中有归宿；无法迁移的条目要显式记录"已废弃 + 原因"，不得静默消失。
    - 同理，**页脚/README 里的来源声明要与实际使用一致**（见「常见陷阱 13 / 覆盖矩阵 C 组第 5 条」）。

15. **skill 双副本漂移（仓库版 vs 用户级目录）**：仓库 `.workbuddy/skills/ocean-daily-report/` 与 `~/.workbuddy/skills/ocean-daily-report/` 是**两份文件**，靠 `sync_skills.py` 手动对齐。2026-09-15 实测两份 `SKILL.md` md5 不同（仓库版停留在 09-08，用户版已更新到 09-14，差 4 条陷阱），意味着**非主力机加载的是缺 4 条规则的旧版**。
    - **铁律**：每次修改 skill 后，主力机执行 `python sync_skills.py collect`（用户目录 → 仓库）并 `git push`；其他机器执行前用 `python sync_skills.py install`（仓库 → 用户目录）。
    - **阶段五自检**：`python sync_skills.py status`，两份不一致即视为质检不合格，当场对齐后再收尾。

16. **量化口径散落多处导致漂移**：时效（7/14/60 天）、去重窗口（5 份 / 12 期 / 14 天）、条目数（2-3 / 3-5）等数字曾散落在 `SKILL.md`、`references/quality_standards.md`、`MEMORY.md`、automation prompt 四处且互不一致——2026-09-15 核对实测：`quality_standards.md` 写"最近 **5 份**"、`SKILL.md` 写"最近 **14 天**"，而实践用"近 **12 期**"，三者并存。
    - **铁律**：任何口径变更必须**一次性同步全部载体**，并 grep 全库（含 `~/.workbuddy/skills/`、`$GH_REPO/.workbuddy/skills/`、自动化 prompt）确认无残留旧值。

17. **放宽口径 → 检索轮次减少 → 长尾来源被"合法"漏掉**：2026-07-31 起时效放宽到 14/60 天、条目数下调到每方向 2-3 条后，检索强度随之下降，近 14 期里 arXiv 独占 49/111 个链接，27 组来源中 11 组零覆盖（含 IEEE Xplore 零命中）。
    - **用户 2026-09-15 拍板口径**：时效维持 **≤14 天**，但**近 7 天作为同方向内的排序优先权重**；条目数**回到每方向 3-5 条**。
    - **原则**：口径与检索强度必须联动评估——放宽时效或减少条数时，不会自动减少检索义务，来源覆盖矩阵照旧逐组打卡。

18. **只依赖 arXiv 导致期刊进展整体漏检**：2026-09-20 期 arXiv 占比冲到 **63%（17/27）**，为近 9 期最高（区间 6%–54%）。反证实测（OpenAlex 官方 API，同一 14 天窗口）：
    全海洋类期刊论文 **2,249 篇**，其中海洋+深度学习 **225 篇**、海洋数字孪生/同化/数值模式 **80 篇**——**期刊侧从不空窗**。
    漏检实例：`10.1016/j.oceaneng.2026.128203`（Ocean Engineering，深海采矿立管损伤识别，大连海事大学，在线首发 09-18）、
    `10.1016/j.marpolbul.2026.120317`（Marine Pollution Bulletin，语义子原型遥感溢油检测，09-18）均未被收录。
    - **根因**：来源覆盖矩阵 A 组把 OpenAlex/Crossref 的检索方式写成"用 API（`verify_paper.py` 已内置）"，
      **角色被定义为"核验工具"而非"发现工具"**，实战中只用于事后核实，从未用于主动发现。
    - **铁律**：每期**必须**执行 `harvest.py`（L0 全量采集）→ `screen.py`（L1 筛选），用池结果驱动方向检索；
      arXiv 占比 > 50% 视为检索结构异常，须在日志举证原因。
    - **区分客观因素**：顶会周期确有空档（9 月中旬 CVPR/ICCV/NeurIPS/IGARSS/OCEANS 均不在出版期），
      会议论文少属实；但**期刊不存在空档**，"只剩 arXiv"不能归因于客观空窗。

19. **期刊"在线首发"与"期号日"混用导致误判**：Elsevier/Wiley 等期刊的 Crossref 记录返回的是**期号日**，
    OpenAlex 返回的是**在线首发日**，二者可差数月。2026-09-20 实测同一篇论文：Crossref = 2026-10-01 / 2026-12-01，
    OpenAlex = 2026-09-18。
    - **铁律**：**时效判定以 OpenAlex `publication_date`（在线首发日）为准**，Crossref 期号日仅作参考；
      若只信 Crossref，会把最新在线论文判成"未来出版"或"超期"而错误剔除。
    - 同理，`verify_paper.py` 输出中若出现"两源日期不一致"，须人工判断以在线首发日为准。

20. **预警期刊被静默剔除**：MDPI 等预警刊、中科院/中信所预警名单刊内容被直接丢弃，会导致"高质量内容未收录、低质量内容看不见"的双重不透明。
    - **铁律**：预警/受限期刊**保留在池内、强制置底、标题标注原因（名单 + 年份）**，由苏老师取舍；
      标注不是论文评价，不否定该刊全部成果。
    - 预警名单**只用最新一期**（中科院官方规则：不累积使用，整改移出后即不再预警），
      原始数据存于 `data/journal_tiers.json` 的 `warning_lists`，用 `active` 字段控制生效。

21. **预印本"一刀切压级"造成时效损失**：原口径把预印本一律压到 S/A 期刊论文之下（P 权重 2.5 vs A 5）。
    但预印本是**最快的时效渠道**——同一成果常常先上 arXiv、数月后才见刊；若其已发表/被期刊接受，仍按 P 排序，
    等于用"形态"惩罚"速度"，与"尽可能及时掌握前沿"的目标冲突。
    - **铁律（2026-09-20 苏老师拍板）**：预印本**若已对应期刊论文**，按**所属期刊等级**排序并保留"预印本"标注；
      匹配依据依次为 ① 同 DOI 的期刊记录 → ② 同标题（归一化指纹）的期刊记录 → ③ arXiv `journal_ref` 解析刊名。
      均未命中才归 P。实现见 `screen.py` 第一阶段索引 + `tier_engine.classify(preprint_journal=...)`。
    - **注意**：升级后仍保留"预印本"标记，避免把关口径被误解为"预印本=同行评审成果"。

22. **只看 SCI 而漏掉 EI / 剔除刊**：苏老师 2026-09-20 指出 SCI 与 EI **都有预警期刊和定期剔除的期刊**，
    这些刊也应归 D 级或排除检索。此前只录入了中科院/中信所预警名单，**未覆盖数据库剔除维度**。
    - **已补名单**：`EI剔除2026`（EI Compendex DISCONTINUED，2026-07-09 更新，全表 228 条，录入 Final Coverage ≥2022 的 19 条）、
      `WoS剔除2026`（Clarivate 2025-12～2026-07 月度更新，SCIE/SSCI 剔除 16 条，含海洋领域相关的 Sea Technology）。
    - **铁律**：名单按"是否可能出现在当期检索中"筛选——**终检年份早于窗口的条目归存档（`active: false`）**，
      不参与实时判定，避免把早已停检的刊误报为预警。名单支持 `{"name","issn","reason"}` 结构化条目，ISSN 亦可命中。
    - **遗留**：中信所 103 本全表、WoS **ESCI** 剔除全表（量级大）待补录。
