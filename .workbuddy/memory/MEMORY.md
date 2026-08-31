# 海洋AI研究日报系统记忆（精简版）

## 系统配置
- **用户**：苏老师
- **自动化任务ID**：`ai`，Schedule：`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`
- **GitHub**：https://github.com/tianyunsu/ocean-data-daily-report
- **网站**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（含 `SECTIONS = [...]`，用 build_daily.py 正则替换）
- **GH_REPO**：仓库根目录（= WORKSPACE）；运行 python 用系统 PATH 的 `python` 命令

## 一致性机制（手动=自动，铁律）
- `ocean-daily-report` skill 是手动/自动共用唯一权威源；自动化 prompt 纯委托该 skill。
- 每次执行（无论手动/自动）必须产出相同工件：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 更新本 MEMORY.md 去重基准。
- 通用方法论 skill `automation-consistency`（用户级）沉淀了"诊断断层→改铁律→纯委托→补日志"流程。

## 跨机器执行机制（2026-07-31 建立）
- 记忆随仓库（`.workbuddy/memory/`、`automations/` 纳入 git）；skill 用 `sync_skills.py` 双向同步（install=仓库→用户目录，collect=用户目录→仓库，status=比对）。
- 铁律：①执行前 `git pull origin main` + `sync_skills.py install`；②执行后 `git push origin main`；③禁同日并行；④非主力机改skill须 collect 后 push。新机器配置见 `SETUP_NEW_MACHINE.md`。

## 执行流程（GitHub Pages 为主，飞书为辅）
```
阶段1 顶会论文检索(23会议,强制) → 阶段2 9方向常规检索(去重黑名单) →
阶段3 build_daily.py写SECTIONS + gen_html.py生成HTML →
阶段4 复制posts/ + 更新index.html/archive.html + git pull --rebase + commit + push →
阶段5 链接验证+时效审计 → 阶段6 写YYYY-MM-DD.md日志 + 更新本MEMORY去重基准
```
飞书推送（可选）：`feishu_write_doc.py` + `run_daily_report.py`（需 `$env:PYTHONUTF8=1`）+ `deploy_report.py`。

## 内容质量规则（必须遵守）
1. 近7天优先，超1个月一律删除，1周~1个月仅留高价值；
2. 每条URL必须先 fetch 返回200，404/403/超时一律不收录；
3. 工具版本特性必须从官方 release notes 核实，不得推断；
4. 摘要必须从原文提取，不得据标题推断；
4b. **date 字段必须以 WebFetch 实测页面发布/更新时间为准**，不得按"检索到的月份"填写。凡 date 精度仅到 YYYY-MM 的条目，发布前必须 WebFetch 复核（08-03教训：两条标07实为02-12/2025-08-29）；
4c. **发布前必须 grep posts/ 目录核查关键词去重**（08-26教训：初稿7处与近3期重复——DLESyM已08-24收、OceanLight/DINOv2声呐已08-21收、EX2606/Argo GDAC快照/CMEMS 8月更新已08-25收、Seagull Coast实为07-14发布>30天；**跨期去重是最高频事故点**）；
5. 方向归类按文章内容判断，不按来源机构功能；
6. 跨方向去重：同URL只能出现在一个方向；
7. 主页新闻必须找具体链接，不得用机构主页URL；
8. 9方向严格定义（2026-05-18强化）：
   - 一、海洋AI：AI/ML/DL用于海洋预报/观测/生态模拟。关键词 neural network/transformer/GNN/deep learning/预报模型
   - 二、海洋数字孪生：必须是海洋数字孪生本身（架构/框架/案例/会议），不含一般AI/数值模型
   - 三、海洋可视化：可视化方法/工具/平台（地图/Dashboard/数据可视化/GIS），不含纯生态/物理海洋学论文
   - 四、海洋数据质量：QA/QC方法/质量控制流程/异常检测，不含测绘进展/数据量统计
   - 五、海洋数据处理：处理方法/流程/算法（再处理/融合/插值/重采样），不含软件版本发布（→九）
   - 六、海洋数据管理与共享：数据政策/FAIR/共享平台/元数据标准/培训/开放政策
   - 七、开放航次/船时共享：科考航次/调查船/海上作业/潜水器/无人船/海洋装备
   - 八、海洋数据中心：数据仓库/档案馆（NCEI/PANGAEA/CMEMS数据中心）；不含IT基础设施(海底机房)、纯气候/物理海洋学论文
   - 九、工具与代码资源：仅限软件工具/代码库/框架/程序新版本发布
   - 硬件装备→开放航次或对应方向；评估报告/状况报告→数据中心或可视化；同一软件不同URL只归一个方向(九)
   - **宁可某方向为空，也不凑数**
9. 发布前分类自检：①核心主题是否符合方向定义 ②是否因内容不足被迫归入 ③是否已出现在其他方向(URL去重) ④"海底数据中心"是否IT基础设施 ⑤综合期刊论文是否按内容归类

## GitHub Pages 架构
- main 分支：源码+每日日报（posts/、index.html、archive.html）；supplement 分支：另一台机器结果（无需本地拉取）；gh-pages：Actions自动部署（勿手编）。
- 每次生成后必须同时更新 index.html 和 archive.html（post-excerpt 摘要是硬编码文本，删改条目后必须同步 Edit 两处）。

## 常见故障处理
| 问题 | 解决方案 |
|------|---------|
| git push TLS错误 | `git config --unset http.sslbackend` |
| git push 代理拦截 | `git config --global --unset http.proxy && git push origin main` |
| git push 连127.0.0.1:65532失败 | 环境变量代理失效。`unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` 后再 `git -c http.proxy= -c https.proxy= push origin main` |
| git push 443超时/Connection reset | GitHub直连不稳定，**循环重试3-5次通常可成功**（Git Bash无sleep勿在循环调用）。SSH因本机无publickey不可用 |
| git commit 报 unable to auto-detect email | 仓库级：`git config user.name "tianyunsu" && git config user.email "tianyunsu@users.noreply.github.com"` |
| run_daily_report.py编码错误 | `$env:PYTHONUTF8=1; python run_daily_report.py` |
| deploy_report.py卡住 | 手动：复制HTML到posts/ → 更新index/archive → git push |
| Python urllib 出网被拒(WinError 10061) | 沙箱阻断Python直连外网。链接校验改用 WebFetch 工具，勿写Python探测脚本 |
| generate_html_daily.py 报 No module named 'requests' | 该脚本exec了feishu_write_doc.py头部。改用自包含生成器：`ast.literal_eval` 解析SECTIONS（如gen_html.py），不触发任何import |
| 飞书docx blocks 404 | 疑app token缺docx写入权限 |

## 去重基准（滚动更新，近期=主要比对对象）
- 04-30~06-01（合并）：GOFLOW/xarray v2026.04.0/GEBCO_2026/OSR 9/Seabed 2030 28.7%/OCEANPILE浙大/GDAL 3.13.0/NCEI Data Tour/探索一号156天/NCEI云迁移AWS/BGC-Argo+二次QC/AxiomOcean 2605.10455/Njord GNN 2605.15470/ECMWF IFS 50r1+AIFS v2波浪/DITTO Summit 横滨/琅琊北极海冰/DestinE DT第二代/SwinIR南海降尺度/IOOS QARTOD/六边形DGGS/DEA无代码/OceanAI大模型山东科大/Volador 1.0/DSON-DT/IOC海洋数据战略/CMEMS Q1扩展/FuXi-Ocean。06-11~06-26 supplement分支约100条（去重参考posts/目录）
- 07-01：扩散模型海况/ENSO arxiv、CMEMS第9届大会、MyOcean Health、EU OceanEye、GLODAPv3、Sentinel-6B、ICAMS
- 07-06：DL印度季风/风暴分辨AI/Argo热含量arxiv、EOSC Blue-Cloud DT、Copernicus Ocean Temp Bulletin
- 07-09：中科院LangYa、CNN海洋生物多样性Frontiers、ISPRS海洋色遥感3D+AI、EDITO、geoai-py
- 07-13：世航智能沧穹CEORION融资、湛江湾1号海洋鸿蒙、三亚深海科考AI、华大智造海洋生物AI、WavyOcean 3.0(首报)
- 07-16：DCGNet/域偏移基准/有害藻华ML arxiv、南溟海洋大模型、MOL IBM AI船舶风险
- 07-21：SALT/AquaStereo arxiv、崂山实验室预报模型、蓝鲲智种大模型、WAIC 2026 AI赋能海洋论坛、pyglider、VirtualFleet
- 07-24：AUV海底压缩/DREAM VLM/多智能体RL arxiv、CVPR 2026水下视觉(Earth2Ocean/NemoNet/UDVSR-Net/AdaMSCol)、台风风暴潮预报、CMEMS SST产品
- 07-28：MarineEVT(ECCV)/RHCNet/MARIS/BiPA(CVPR)/MaCVi Workshop/生成状态空间模型/AUV浮游生物/WavyOcean 3.0/Nautilus NA180/wavespectra v4.8.0/raschii v2.0.0/CMEMS Argo QC3
- 07-31：KIST-Ocean、琅琊2.0、ILIAD ISPRS、BGC-Argo VAE biofouling、青岛可信数据空间、数据产权登记、Okeanos EX2605、科学号西太、CMEMS 7月新版本、GEBCO研讨会、pyo-oracle v1.0.0。**去重事故**：MARIS/WavyOcean 3.0/CMEMS Argo QC3已在上期报道
- 08-03（16条）：HybridOM(ICML)、BALLAST(ICML)、SWIN-DeepONet(IJCAI-ECAI)、多尺度CNN+DropKey海况估计、V-JEPA波浪、ECCV 2026海洋视觉征稿、DestinE第三阶段、CMEMS MyOcean Pro 3D、边缘云QC专利、BGC-Argo CHLA再处理、ODIS筹备IODE-29、IOC执理会数据互操作决议、Schmidt加勒比盐指航次、CMEMS新MFC、xarray/uxarray v2026.07.0。**时效修正**：海洋十年公民科学FAIR指南实为02-12、中国Argo智能系统2025-08-29编辑，均剔除
- 08-07（17条）：盘古海洋预报大模型工程化(08-03)、生成式AI海啸概率预报2608.04327、BG4Sea季节预报2607.16731(豁免)、Swimm3R 2608.00950、DITTO Summit早鸟(07-30更新)、2DCNN-LSTM沙波测深、贝叶斯AUV生境测绘(豁免)、RAISE-Ocean入选科学十年、MDImageNet(中国台湾海洋委员会)、DORI虎鲸声学5298h、奋斗者号Nature鲸类化石(豁免)、Nautilus NA181(08-20起)、cstar-ocean v0.8.0、oceanspy v0.3.6(豁免)
- 08-10（14条）：中国科协海洋AI大模型论坛、王凡多智能体战略、UUV视觉控制2608.04723、UUV规划学习2608.05365、ML事件感知QC JMSE、AUV海底图像远程感知2607.18013(豁免)、青岛海洋公共数据团体标准、海洋十年第11轮征集、EX2605最后阶段(更新)、NA180结束NA181接力(更新)、raschii v2.0.1、wavespectra v5.0预告
- 08-14（13条）：琅琊大模型Science Bulletin(08-12)、Multi-AUV值梯度扩散RL 2608.12436、李群随机PINN 2608.08356、BenthiCat光-声数据集ESSD、CMEMS In Situ TAC澳滑翔机综述(豁免)、科学号西太返港、EX2605收官(更新)、gridstats v2.6.0、π-SUB水下基准(08-11)。**时效修正**：marinesitu.eu文章实为04-30剔除；EX2605 URL与08-10重复改media-resources
- 08-18（12条）：AMR-Pose AUV相对位姿2608.12866、LinStereo+SeaStereo ECCV(豁免)、福建渔区海况预报(08-10)、日照港集装箱数字孪生(08-14)、DTF-Net风数据质控JMSE、条件多元函数PCA海豹剖面2608.05376、哨兵-2光学测深70-80米、OBIS南极ROV数据集TANGO、EX2606预告(08-19起)、GEBCO_2026 WMS。**时效剔除**：TIDE(2512.07171)、PDIM(01-23)、OceanMCP(02-21)、Schmidt盐指(与08-03重复)
- 08-21（13条）：OceanLight 2608.16070(08-17)、退化感知跨模态融合DINOv2+声呐2608.19710(08-20)、Dynamic SpectraFormer 2608.18662、MHE TDOA 2608.16024(IFAC WC)、OceanDepths 2608.16373(ESA)、EMODnet第24届指导委员会、Nautilus NA181启航(更新)、EX2607预告(09-24起)。**去重修正**：EX2607与08-18 EX2606共用NOAA总览页重复改news-release页
- 08-24（11条）：DLESyM-Ocean 2608.11545(08-12,华盛顿大学+NVIDIA)、Underwater Color Restoration 2608.15598(Sea-thru作者)、PRCV 2026哈尔滨、DBSD-Net SST超分2608.15423、HiAOOS 2026北极航次(08-17)。**时效剔除**：SeagrassFinder(2024-12)、SIMPGEN(2025-03)、WavyOcean AOGS(重复)。**经验**：占位主页URL连续两期重复触发去重，建URL池轮换
- 08-25（21条）：盘古大模型工程化(CCTV 08-13)、WaveGraph GNN 2608.16449、RCNN SST降尺度2608.10022、CORAL-AUV CFD RL(CoRL)、GNN-BiLSTM韩国热浪预警、广州南沙AquaLink+HKUST(GZ) DT、CMEMS MyOcean洋流可视化、SIREN-TV SSH重建、SGD-SST 2.0、U-Net地中海SST重建、青岛海洋公共数据标准(08-12)、国家数据局涉海数据(08-25)、ROSA数据治理指南、探索6000 AUV南海冷泉商业化、NOAA库克群岛26天深潜、Nautilus AUV Sentry马里亚纳、**EX2606美属萨摩亚ROV+测绘(08-20~09-17)**、**CMEMS 8月产品更新(北极波浪/Baltic/Arctic潮汐3km/Arctic BGC)**、NOAA NOS OFS v1.7.1、earthlens v0.14.0、MDOcean v1.4.4。**顶会时效**：HybridOM(2月>60天)、AAAI DRM-Net/DiveSeg(>60天)均排除
- 08-26（13条有效/9方向）：IJCAI-ECAI 2026 AI4G #AI4G39海洋热极端预警(08-20,Bremen)、世界模型接地LLM规划AUV/ASV 2608.19661(08-20,IROS 2026 AQ2UASIM)、SAM2点提示底栖密集分割2608.17561(08-18)、生成式资料同化锋面级联2608.14955(08-15,审稿Comms EE)、浑浊水下多标注者2608.15363(08-15,ECCVW'26 Marine Vision)、OLAR DTO四层架构综述10.34133/olar.0160(08-17)、NERACOOS Mariner's Dashboard beta(08-25)、IOOS Model Viewer WFCOM(08-25)、中大西洋HFR SeaSonde R25自动QC(08-25)、PANGAEA元数据架构现代化(08-17)、第10次中俄海洋联合科考(08-20起62天)、库克群岛EX2605欢迎仪式+意外多金属结核场(08-17)、uxarray v2026.08.0(08-18)。**去重教训（07处）**：初稿DLESyM(08-24已收)/OceanLight(08-21已收)/DINOv2声呐(08-21已收)/EX2606(08-25已收)/Argo GDAC快照(08-25已收)/CMEMS 8月更新(08-25已收)/Seagull Coast(07-14>30天)全剔除——**教训4c：发布前grep posts/核查**
- 08-31（10条/9方向）：AquaFlow单目3DGS SLAM水下流式重建2608.22906(08-25,浙大+上海AI实验室等,定位误差-13.2%/PSNR+4.74dB vs WaterSplat-SLAM)、NemoSplat前馈4D高斯溅射介质感知水下动态重建2608.22888(08-24,港科大+北理工)、BenthicFlow流匹配生成可扩展水下底栖3D环境2608.23173(08-24,埃因霍温理工,ECCV 2026 Marine Vision)、全国首份《AI+海洋协同发展共识》深圳发布(深珠湛,08-26)、E/V Nautilus NA181威克岛航次发现小飞象章鱼+探索二战沉船(08-27更新)、Stonefish深水物理与传感器仿真扩展2608.26888(08-27,赫瑞瓦特)。**时效剔除**：巴塞罗那港海洋数字孪生(piernext 04-23发布>60天)、SASC-USOD(2605.15535原版5月>60天)。**趋势**：8月下旬水下3D重建热点(AquaFlow/NemoSplat/BenthicFlow/uw3dgs/深水模拟器5篇同周)。**⚠️遗漏复盘(用户反馈)**：IEEE GRSM北极海冰综述《Deep Learning Applications in Arctic Sea Ice Remote Sensing: A Review》(任沂斌一作/李晓峰通讯,IF 13.7,doi:10.1109/MGRS.2026.3720616)新闻稿08-26发布(中科院海洋所官网)未被任何一期收录——根因：检索关键词未覆盖"海冰/极地"主题+国内院所新闻源未巡检+顶刊综述无单独检查。**整改**：SKILL.md已新增北极海冰检索词/国内海洋所新闻巡检清单/顶刊综述检查。**该综述≤60天可豁免，下期(09-01+)可补录，标注原始日期2026-08-26**

