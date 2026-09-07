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
每方向 2-3 条精选动态，全日报 18-22 条。产出物为 HTML 简报，发布到 GitHub Pages。

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

⚠️ **一致性铁律**：手动执行 ≠ 简化执行。手动触发的日报必须产出与自动化定时运行**完全相同**的工件与记忆文件，包括 `daily_reports/海洋AI简报_YYYY-MM-DD.html`、`posts/YYYY-MM-DD.html`、`.workbuddy/memory/YYYY-MM-DD.md`、以及 `MEMORY.md` 去重基准更新。任何"跳过某步"的做法都会造成记忆断层，必须避免。

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

常见陷阱：顶会论文日期歧义——以首次公开可访问日期为准，非会议召开日。详见 `references/quality_standards.md` 的"顶会论文日期规则"。

### 阶段二：常规来源检索

1. **读取历史日报**：从 `$GH_REPO/posts/` 读取最近 14 天的日报，解析出已报道的事件/论文/产品，
   构建去重黑名单（同时参考 `$WORKSPACE/.workbuddy/memory/MEMORY.md` 的去重基准）。
2. **逐方向搜索**：对 9 大方向逐一执行 WebSearch/WebFetch，搜索近两周（≤14天）的新内容。
   预印本优先：arXiv physics.ao-ph, cs.CV, cs.LG；EarthArXiv；ESSOAr。
3. **时效性预检**：**在搜集阶段**即标记每条素材的发布日期，
   剔除不满足条件的条目（规则见阶段六的 `references/quality_standards.md`）。
   ⚠️ **日期核实**：搜索引擎显示的日期可能是网页索引/修改日期，非原始发布日期。
   对于政策文件、战略计划、国际会议文档等，必须通过内容交叉验证（如摘要中提及的会议年份）
   或多源比对（如 AGRIS、OceanExpert）确认真实发布日期。详见 `references/quality_standards.md` 的"日期核实规则"。
4. **去重确认**：对比历史黑名单 + MEMORY.md 去重基准，剔除重复条目。

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
3. 执行 `$PYTHON $WORKSPACE/build_daily.py`，通过正则替换将 SECTIONS 写入 `$DATA_SOURCE` 第18行。
4. 生成 HTML 脚本 `$WORKSPACE/gen_html.py`（读取 DATA_SOURCE → 生成 `海洋AI简报_YYYY-MM-DD.html`）
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

### 阶段五：质量审查

加载 `references/quality_standards.md` 执行两项审查：

1. **链接验证**：用 WebFetch 逐条验证所有 href 链接。
   失效链接须搜索替代来源，修复后重新生成 HTML + 重新 push。
   ⚠️ 部分中国学术期刊网站（如 jao.org.cn）会返回 403 Forbidden（反爬虫机制），
   此时通过搜索引擎确认文章存在且内容一致即可判定链接有效。
2. **时效性审计**：用 Python 提取所有条目日期，计算距今天数，
   标出 >14天 / >30天 / >60天 的条目。不合格条目须替换或标注豁免理由。

### 阶段六：记忆写入（不可跳过，手动与自动完全一致）

任务完成后**必须**写入以下全部记忆工件，手动触发与自动化定时运行写入**完全相同**的文件、相同的内容结构：

1. **每日工作日志** `$WORKSPACE/.workbuddy/memory/YYYY-MM-DD.md`
   - 追加（不覆盖）执行日志：条目数、覆盖方向、关键发现、异常说明（如飞书API 404、WEBHOOK 未配置、git冲突解决等）
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

| # | 方向 | 主要搜索来源 | 搜索关键词示例 |
|---|------|-------------|---------------|
| 1 | 海洋人工智能 | arXiv physics.ao-ph, **顶会论文(强制检索23个会议)**, **IEEE期刊(JOE/TGRS/GRSM)**, Nature, npj 系列, 国内新闻 | "ocean AI deep learning 2026", `"CVPR 2026" underwater marine`, "海洋大模型 2026", **"Arctic sea ice deep learning", "北极海冰 AI 遥感", "sea ice remote sensing review 2026"** |
| 2 | 海洋数字孪生 | CMEMS, NOAA, 国内政策, **顶会论文(MLSys/NeurIPS)** | "digital twin ocean 2026", "海洋数字孪生 最新" |
| 3 | 海洋可视化 | CMEMS MyOcean, GitHub, 学术工具, **顶会论文(CVPR/ICCV/ECCV)** | `"CVPR 2026" ocean visualization`, "ocean visualization tool 2026" |
| 4 | 海洋数据质量 | Springer, Argo, GOOS, **顶会论文(ICML/NeurIPS)**, **IEEE期刊(TGRS/GRSL)** | `"ICML 2026" ocean data quality`, "Argo quality control machine learning 2026" |
| 5 | 海洋数据处理 | arXiv, Nature Sci Data, **顶会论文(NeurIPS/ICLR)**, J. Oceanography, **IEEE期刊(TGRS/JSTARS)** | `"NeurIPS 2026" ocean data`, "ocean data processing AI 2026", "SST super-resolution sea ice dataset 2026" |
| 6 | 数据管理与共享 | IOC, EMODnet, 信通院, CMEMS | "ocean data sharing FAIR policy 2026" |
| 7 | 开放航次与科考 | NOAA Ocean Exploration, 高校科考新闻, **顶会论文(CoRL/ICRA)** | "NOAA Okeanos Explorer 2026", "海洋科考 2026" |
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
