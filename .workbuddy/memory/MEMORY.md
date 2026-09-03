# 海洋AI研究日报系统记忆（精简版）

## 系统配置
- **用户**：苏老师
- **自动化任务ID**：`ai`，Schedule：`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`
- **GitHub**：https://github.com/tianyunsu/ocean-data-daily-report
- **网站**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（含 `SECTIONS = [...]`），用 `build_daily_YYYYMMDD.py` 正则替换
- **GH_REPO**：仓库根目录（= WORKSPACE）；python 用系统 PATH 的 `python`
- **HTML 生成器**：`gen_html_YYYYMMDD.py`（自包含，`ast.literal_eval` 解析 SECTIONS，禁止 import feishu 模块）

## 一致性机制（手动=自动，铁律）
- `ocean-daily-report` skill 是手动/自动共用唯一权威源，自动化 prompt 纯委托该 skill。
- 每次执行（无论手动/自动）必须产出相同工件：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 更新本文件去重基准。
- 通用方法论 skill `automation-consistency`（用户级）沉淀"诊断断层→改铁律→纯委托→补日志"流程。

## 跨机器执行机制（2026-07-31 建立）
- 记忆随仓库（`.workbuddy/memory/`、`automations/` 纳入 git）；skill 用 `sync_skills.py` 双向同步（install=仓库→用户目录，collect=反向，status=比对）。
- 铁律：①执行前 `git pull origin main` + `sync_skills.py install`；②执行后 `git push origin main`；③禁同日并行；④非主力机改 skill 须 collect 后 push。新机器见 `SETUP_NEW_MACHINE.md`。

## 执行流程（6 阶段，GitHub Pages 为主，飞书为辅）
```
阶段0 git pull origin main
阶段1 顶会论文检索(23会议+IEEE期刊,≥5条强制,不可跳过)
阶段1B 国内院所新闻巡检(海洋所/南海所/深海所/青大/南科大等)
阶段2 9方向常规检索(建去重黑名单)
阶段3 build_daily_XXX.py写SECTIONS + gen_html_XXX.py生成HTML
阶段4 复制posts/ + 更新index.html/archive.html + commit + push
阶段5 链接WebFetch验证 + 时效审计
阶段6 写YYYY-MM-DD.md日志 + 更新本文件去重基准 + 追加automations/ai/memory.md
```
飞书推送（可选）：`feishu_write_doc.py` + `run_daily_report.py`（需 `$env:PYTHONUTF8=1`）。

## 内容质量规则（必须遵守）
1. 近7天优先；14–60天需豁免；>60天一律删除（arXiv 以 v1 首次提交日为准，不以聚合站索引日）。
2. 每条 URL 必须 WebFetch 返回 200，404/403/超时一律不收录。
3. 工具版本特性必须从官方 release notes 核实，不得推断。
4. 摘要必须从原文提取，不得据标题推断。
4b. **date 字段以 WebFetch 实测发布/更新时间为准**。聚合站（PulseAugur/PubScholar/Google）显示日常为索引日而非发布日，必须复核（09-03：两条标 09-01 实为 08-31）。
4c. **发布前必须 `grep -rl` 核查 `posts/` 目录去重**（最高频事故点，08-26 曾 7 处重复）。
5. 方向归类按文章内容判断，不按来源机构功能。
6. 跨方向去重：同 URL 只能出现在一个方向。
7. 主页新闻必须找具体链接，不得用机构主页 URL。
8. 9方向严格定义：一海洋AI（AI/ML/DL用于海洋预报·观测·生态）；二数字孪生（须是海洋数字孪生本身：架构/框架/案例/会议）；三可视化（方法/工具/平台/Dashboard/GIS）；四数据质量（QA/QC/异常检测，不含测绘进展·数据量统计）；五数据处理（再处理/融合/插值/重采样，不含软件发布→九）；六数据管理与共享（政策/FAIR/元数据标准/开放政策）；七开放航次与科考（航次/调查船/潜水器/无人船/海洋装备）；八海洋数据中心（NCEI/PANGAEA/CMEMS等仓储档案馆，不含IT基础设施·纯物理海洋学）；九工具与代码资源（仅软件新版本发布）。硬件装备→七；评估报告→八或三；同一软件不同URL只归九。**宁可某方向为空（写明"暂无新增"）也不凑数**。
9. 发布前分类自检：①核心主题符不符合方向定义 ②是否因内容不足被迫归入 ③是否已出现在其他方向 ④"海底数据中心"是否IT基础设施 ⑤综合期刊论文是否按内容归类。

## GitHub Pages 架构
- main 分支：源码+每日日报（posts/、index.html、archive.html）；supplement 分支：另一台机器结果（无需本地拉取）；gh-pages：Actions 自动部署（勿手编）。
- 每次生成后必须**同时**更新 index.html 和 archive.html（post-excerpt 是硬编码文本，删改条目后两处都要同步）。

## 常见故障处理
| 问题 | 解决方案 |
|------|---------|
| git push TLS错误 | `git config --unset http.sslbackend` |
| git push 代理拦截 | `git config --global --unset http.proxy && git push origin main` |
| git push 127.0.0.1:65532失败 | `unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` 后 `git -c http.proxy= -c https.proxy= push origin main` |
| git push 443超时/reset | GitHub直连不稳，**循环重试3-5次**（Git Bash 无 sleep，勿放循环内）。SSH 因无 publickey 不可用 |
| git commit 无法识别身份 | 仓库级 `git config user.name "tianyunsu" && git config user.email "tianyunsu@users.noreply.github.com"` |
| Python urllib 出网被拒(WinError 10061) | 沙箱阻断 Python 直连外网。链接校验改用 WebFetch 工具，勿写探测脚本 |
| Edit 报 File has been modified | 用 Bash 改过同文件后，再 Read 一次即可继续 Edit |
| 飞书链路（长期不可用，可跳过） | `run_daily_report.py` 需 `$env:PYTHONUTF8=1`；`deploy_report.py` 卡住则手动复制HTML→posts/ 再 push；docx blocks 404 疑 app token 缺权限 |

## 去重基准（滚动更新，只留最近 6 期）
> **≤08-26 的历史条目不再在此罗列**——`posts/` 目录本身就是全量存档，规则 4c 的 `grep -rl` 比读基准更可靠。本节只保留近 6 期用于快速人工比对，超出窗口一律 grep posts/。

- **08-26（13条）**：IJCAI-ECAI AI4G #AI4G39海洋热极端预警(08-20)、世界模型接地LLM规划AUV/ASV 2608.19661(IROS)、SAM2点提示底栖分割2608.17561、生成式资料同化锋面级联2608.14955、浑浊水下多标注者2608.15363、OLAR DTO四层架构综述olar.0160、NERACOOS Mariner's Dashboard beta、中大西洋HFR SeaSonde R25自动QC、PANGAEA元数据架构现代化、第10次中俄联合科考(08-20起62天)、库克群岛EX2605欢迎仪式+多金属结核场
- **08-31（10条）**：AquaFlow单目3DGS SLAM水下流式重建2608.22906(08-25)、NemoSplat前馈4D高斯溅射2608.22888(08-24)、BenthicFlow流匹配底栖3D环境2608.23173(08-24)、《AI+海洋协同发展共识》深圳发布(08-26)、Nautilus NA181威克岛小飞象章鱼+二战沉船(08-27)、Stonefish深水仿真扩展2608.26888(08-27)。**⚠️遗漏复盘**：IEEE GRSM北极海冰综述(任沂斌/李晓峰, doi:10.1109/MGRS.2026.3720616)新闻稿08-26发布未收录——根因"海冰/极地"关键词缺失+国内院所未巡检。整改：SKILL.md 已加海冰/极地检索词+院所巡检清单+顶刊综述检查
- **09-02（18条有效，D3/D4为空）**：IEEE GRSM北极海冰遥感深度学习综述(08-26,补录08-31遗漏)、3D-USE水下增强场景级3DGS(arXiv 08-28)、RGI-Net递归门控注入水下复原(JMSE 08-31)、西电"深海勇士"号智慧眼1500米海试(陕西日报 09-01)、HFQI-YOLO轻量化水下实时检测(MST 09-01)、南科大-深圳海洋大学海洋超算与数字孪生联合实验室(08-28)、Transformer U-Net从SWOT重力反演海底地形(JGR 08-27)、MambaIR-MSP红外引导被动微波SST超分(JGR 08-28)、CIM-TTDA测试时域适应SAR海岸水淹(JGR:MLC 08-19)、虚拟ADCP滑翔机重建全深度海流剖面(ESSOAr 07-27,豁免)、辽宁海洋数据7项规范+省级海洋与极地数据中心(08-26)、OBIS执委会第8次会议+3200万条新记录(09-01)、中国第16次北冰洋科考雪龙号12冰站+雪龙2号(08-07/08-09)、"嘉庚"号马来西亚海洋课堂四国33师生(08-27)、EMSO EVOLVE启动19机构10国(09-01)、Argo Australia 20周年28.5万剖面(08-26)、bluertopo v0.0.2(CRAN 08-27)、CopernicusMarine v0.4.9(CRAN 08-28)。**注**：09-01 无产出（会话中断）
- **09-03（18条，9方向全有）**：季节感知混合卷积-Transformer南极海冰浓度预报(arXiv 2608.30654, v1=08-31)、KSG-Net海上3D船舶检测(arXiv 2609.02077, 09-02)、Enhanced Crossformer多浮标波高预报(JMSE 1629, 09-02)、单变量DL波高预报收益边界测评(Ocean Eng 124202, 08-31)、双路径降解感知网络风机RUL(JMSE 1595, Published=08-31)、Eco Wave Power+德国AI engineering波浪能数字孪生(09-02)、红海全球目的地数字孪生10km²(09-02)、连云港空天地一体化智慧渔港(09-01)、CMEMS "Mediterranean in Motion"地中海增温叙事(08-28)、海洋碳数据代表性量化(arXiv 2609.00133, 08-31)、HarmoCore函数潜在扩散波场重建(arXiv 2609.00679, 09-02)、AUWave稀疏浮标重建波高场(Ocean Eng 127187, 08-31)、《海洋科学数据快报》DEOS创刊(09-01)、海洋四所参加SOOS/SCAR大会(09-02)、"蓝梦同航"联合调查实习航次青岛启航(08-29)、Nautilus NA181二战沉船考古窗口(09-01)、OSI SAF AMSR3海冰产品业务化(09-01)、NOAA CO-OPS潮汐基准计算器TADC升级(09-01)。**去重**：27关键词grep全NONE。**时效**：全≤6天。**日期修正**：2608.30654 与 JMSE 1595 均从标注09-01改为实测08-31

## 经验教训（勿重复犯）
- **跨期去重**：最高频事故。占位主页 URL 连续两期重复会触发去重，应建 URL 池轮换；Nautilus/EX 系列航次共用总览页时须改用具体 news-release 页。
- **日期核实**：聚合站（PulseAugur/PubScholar/Google）日期≠发布日，必须 WebFetch 原文（08-03、08-14、09-03 三次教训）。
- **WebFetch 失败≠放行**：改 WebSearch 交叉验证（09-03 据此拦截一条 3 月旧航次）。
- **主题盲区**：国内院所新闻、极地/海冰主题曾漏检，已写入 SKILL.md 巡检清单。遗漏项应在 MEMORY.md 标注"待补录+原始日期+窗口"形成闭环。
