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
| urllib 返回 403（MDPI/ScienceDirect/Wiley 等） | Cloudflare 反爬，非死链，不得直接剔除。**首选 `verify_paper.py`（Crossref + OpenAlex 官方 API）核实元数据**，不受 403 影响且更快更准；无 DOI 时再用 WebFetch 二次确认（09-04 两条 MDPI、09-07 三条均据此通过）。详见 SKILL.md「反爬站点核实规则」 |
| arXiv 老文补登伪新稿 | 高 arXiv ID 不等于新成果，必查 v1 提交日与原文年份（09-04 剔除 HorizonNet 2608.30471，实为 2018 旧文） |
| **present_files 预览污染本地 HTML** | 预览本地 .html 会被注入 `data-page-node-id="..."` 属性（150 处 diff）。**铁律：先 commit+push 再 present；present 后必须 `git status` 复查，若 posts/*.html 变脏立即 `git checkout --` 还原**（线上已是干净版，无需再 push）。09-04 首次发现，历史 20+ 期均无此属性 |
| **转载站在中国大陆不可访问** | Yahoo / Yahoo News 自 2021-11-01 起对大陆返回"服务不可访问"公告页，链接等于死链。**选源优先原始媒体**；遇到 Yahoo/MSN 类转载，必须回溯首发来源（09-07 BGC-Argo 条目由 Yahoo→KPBS 08-28 首发）。同理核验转载站日期是否为索引日 |
| urllib 命中但内容是挑战页 | PyPI 等站点返回 200 但 title 为 "Client Challenge" = 反爬挑战页，不等于内容有效。须 WebFetch 二次确认包是否存在、版本与发布日期（09-07 coops-mcp 0.1.1 据此确认真实且 Released Sep 4, 2026） |
| Edit 报 File has been modified | 用 Bash 改过同文件后，再 Read 一次即可继续 Edit |
| 飞书链路（长期不可用，可跳过） | `run_daily_report.py` 需 `$env:PYTHONUTF8=1`；`deploy_report.py` 卡住则手动复制HTML→posts/ 再 push；docx blocks 404 疑 app token 缺权限 |

## 去重基准（滚动更新，只留最近 5 期）
> **≤08-26 的历史条目不再在此罗列**——`posts/` 目录本身就是全量存档，规则 4c 的 `grep -rl` 比读基准更可靠。本节只保留近 6 期用于快速人工比对，超出窗口一律 grep posts/。

- **09-03（18条，9方向全有）**：季节感知卷积-Transformer南极海冰浓度预报(arXiv 2608.30654, v1=08-31)、KSG-Net海上3D船舶检测(2609.02077, 09-02)、Enhanced Crossformer多浮标波高预报(JMSE 1629, 09-02)、单变量DL波高预报收益边界(OceanEng 124202, 08-31)、双路径降解感知网络风机RUL(JMSE 1595, 08-31)、Eco Wave Power波浪能数字孪生(09-02)、红海全球目的地数字孪生(09-02)、连云港空天地智慧渔港(09-01)、CMEMS地中海in Motion叙事(08-28)、海洋碳数据代表性量化(2609.00133, 08-31)、HarmoCore函数潜在扩散波场重建(2609.00679, 09-02)、AUWave稀疏浮标波高场(OceanEng 127187, 08-31)、《海洋科学数据快报》DEOS创刊(09-01)、海洋四所SOOS/SCAR(09-02)、蓝梦同航青岛启航(08-29)、Nautilus NA181沉船考古窗口(09-01)、OSI SAF AMSR3海冰业务化(09-01)、NOAA TADC潮汐计算器升级(09-01)

- **09-04（17条，9方向全有）**：合成孔径声呐ATR CNN/Transformer对比(arXiv 2609.01800, 09-01)、ICE-3D逐日北极海冰厚度(天津大学, RS 18(17)2991, 09-03)、SHIP-AID浅水沉船GeoAI(RS 18(17)2884, 08-26)、残差-状态空间北极海冰分割(《中国航海》08-31)、厦门文鳐船舶海洋大模型+海嘉数字中枢(09-04)、Fugro新加坡AI海洋数字孪生(09-03)、北海预报中心近岸淹没数字孪生采购(09-02)、NEODAAS航次卫星可视化门户(08-26)、IMOS Live升级AusTemp+75浮标(08-27)、多传感器融合水色叶绿素精度评估(Front.RemoteSens 08-26)、注意力3D-U-Net++西太三维温盐场+ESSD数据集(09-04)、BBNJ信息交换机制CHM数据治理(Front.Mar.Sci 1840546, 08-31)、EMODnet数据吸纳新阶段(08-31)、海南下半年共享航次+深海科创积分(09-04)、上海海洋大学中西印度洋调查船租赁(08-31)、第11次国家科学数据中心主任联席会舟山(09-03)、OpenDrift v1.14.12(08-31)。剔除：2608.30471为2018旧文补登
- **09-07（15条+2备注[D2/D3无新增]）**：MHWCorrNet可解释DL订正ECMWF海洋热浪次季节预报CSI+9%(JGR:MLC, 南海所, 09-01)、本体+多LLM认知架构AUV共享自主(2608.29347, v1=08-29)、SurgeGen两阶段扩散风暴潮情景生成(2609.03382, 09-03)、EchoST-SSL渔业回声自监督时空表征(IEEE Sensors J., 水科院, 09-03)、RFA+RCSA改进YOLO11n水下垃圾检测(Sustainability su18178986, 09-02)、PhyEnv-GAN船舶行为异常检测(OceanEng, 09-01)、S-DEIM稀疏离散经验插值0.2%格点重建SST(JGR:MLC JH001279, 08-27)、海滩为标尺卫星岸线近岸潮汐10km→100m(Comm.Earth&Env, 09-01)、西班牙MITECO+IEO-CSIC 2576万欧元海洋战略(09-01)、NSF未来海洋观测优先级征集截止9/30(OOIFB, 实测09-02)、美国BGC-Argo资金中断(KPBS 08-28首发, 已替换Yahoo/Surfer转载)、OSIL 3.0米海洋观测浮标(MarineTechNews, 09-03)、coops-mcp 0.1.1(PyPI, 09-04)。日期修正3处：NSF 09-01→09-02、OSIL 09-04→09-03、BGC-Argo Yahoo→KPBS
- **09-08（13条+2备注[D3/D4无新增]）**：NWM神经波浪模型：首个AI+数值模式混合海浪模型(OceanEng 366 127556, 中山大学×南信大, 09-06)、AquaBEV 3D声呐监督单目水下BEV占用(arXiv 2609.04411, 09-03)、SEMI-DETR半监督34张标注白鲸幼鲸检出(Front.Mar.Sci 09-04, FAU+DFO)、Too Rare to Learn气旋轨迹硬编码反损孟加拉湾模拟器(2609.04635, 09-04)、Fugro加入欧盟OCEANITY共建EDITO(09-07, 区别于09-04新加坡枢纽)、A-Predator各向异性核点卷积MBES点云配准(RS 18(17)3035, 西北工大, 09-05)、DenseNet-121跨河口颜色锋识别(JMSE 14(17)1657, 09-06)、EMODnet生物与海床栖息地392万欧元招标截止10-23(EuroGOOS, 09-03)、雪龙2号冰站无人机投放浮标+抗低温磁探无人机(新华社, 09-05)、国家极地科学数据中心开放课题设极地AI-Ready方向(09-04)、南海海洋大数据智能管理平台130TB+AI识别(《中国测绘》, 09-04)、Mini-Girona I-AUV开源干预型水下机器人(2609.02605, 09-02)、Underwater Acoustic Channel Library(2609.03207, 09-02)。院所：qdio 09-04温盐场实时智能重构=本期ESSD同源新闻稿不收
- **09-09（13条+1备注[D2无新增]）**：Neptune全球海洋—海冰次季节AI模拟器CNN+SFNO双版本1°/0.25°稳定预报60天(arXiv 2609.08606, CMCC+Columbia, 09-08)、"丝路海运"北极航线气象导航启用：风云卫星+AI 15天逐日海冰预报海杰7船全覆盖(中国经济网, 09-08)、SKANN原始波形选择性核声学网络开放集跨航次船舶再识别(2609.07399, 09-07)、视觉基础模型适配声呐首次无位姿3D声呐重建(2609.06261, 09-05)、DARB方向非对称realism桥双向声呐-光学翻译(2609.06253, 09-05)、"丝路海运"港口气象风险智能体58座港口(国务院国资委, 09-09, 腾讯同日稿不含此内容)、水域时序异常检测ML综述106篇(Water 18(17)2209, 09-05)、GNN海图变化关键性分类(2609.02996, 09-02)、小批量风险规避DQN水下机器人导航(2609.07998, 09-07)、CORD沿海海洋韧性数据协作体获海洋十年认可(IOC UNESCO, 09-04, CORD≠CORDIS)、"深海一号"搭载"蛟龙"号青岛起航(人民日报, 09-06)、EastAsiaClimateExtremes东亚极端事件AI-Ready含MHW(2609.08241, 09-08)、cstar-ocean 0.13.5海洋碳建模工作流(PyPI, 09-05, 前收v0.6.0/v0.8.0)。剔除：MBARI MOLA页面Updated Sep8但原发May4(>60天)


## 经验教训（勿重复犯）
- **跨期去重**：最高频事故。占位主页 URL 连续两期重复会触发去重，应建 URL 池轮换；Nautilus/EX 系列航次共用总览页时须改用具体 news-release 页。
- **日期核实**：聚合站（PulseAugur/PubScholar/Google）日期≠发布日，必须 WebFetch 原文（08-03、08-14、09-03 三次教训）。
- **WebFetch 失败≠放行**：改 WebSearch 交叉验证（09-03 据此拦截一条 3 月旧航次）。
- **主题盲区**：国内院所新闻、极地/海冰主题曾漏检，已写入 SKILL.md 巡检清单。遗漏项应在 MEMORY.md 标注"待补录+原始日期+窗口"形成闭环。
- **用户指定条目与去重冲突时**：先核实历史收录（grep posts/ + 检索原文是否有新进展），把结论+三个选项（不重复／标注更新补录／原样重复）交给用户拍板，不要默默照做也不要默默拒绝。确认后必须把"永久归属某期，后续不再收录"写进去重基准，形成闭环（09-04 GRSM 综述案例）。
