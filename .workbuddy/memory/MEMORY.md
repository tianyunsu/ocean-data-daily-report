# 海洋AI研究日报系统记忆（精简版）

## 系统配置
- **用户**：苏老师
- **自动化任务ID**：`ai`，Schedule：`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`
- **GitHub**：https://github.com/tianyunsu/ocean-data-daily-report
- **网站**：https://tianyunsu.github.io/ocean-data-daily-report/
- **DATA_SOURCE**：`feishu_write_doc.py`（含 `SECTIONS = [...]`，第18行附近，用 build_daily.py 正则替换）
- **GH_REPO**：仓库根目录（= WORKSPACE）
- **PYTHON**：C:\Users\ENVY\.workbuddy\binaries\python\versions\3.13.12\python.exe

## 一致性机制（手动=自动，铁律）
- `ocean-daily-report` skill 是手动/自动共用唯一权威源；自动化 prompt 纯委托该 skill。
- 每次执行（无论手动/自动）必须产出相同工件：`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + `.workbuddy/memory/YYYY-MM-DD.md` + 更新本 MEMORY.md 去重基准。
- 通用方法论 skill `automation-consistency`（用户级）沉淀了"诊断断层→改铁律→纯委托→补日志"流程。

## 跨机器执行机制（2026-07-31 建立）
- 记忆随仓库（`.workbuddy/memory/`、`automations/` 纳入 git）；skill 用 `sync_skills.py` 双向同步（install=仓库→用户目录，collect=用户目录→仓库，status=比对）。
- 铁律：①执行前 `git pull origin main` + `sync_skills.py install`；②执行后 `git push origin main`；③禁同日并行；④非主力机改skill须 collect 后 push。
- 新机器配置见仓库根 `SETUP_NEW_MACHINE.md`。

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
4b. **date 字段必须以 WebFetch 实测页面发布/更新时间为准**，不得按"检索到的月份"填写。凡 date 精度仅到 YYYY-MM 的条目，发布前必须 WebFetch 复核（2026-08-03 教训：两条标 2026-07 的实为 2026-02-12 与 2025-08-29，均逾期）；
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
- 每次生成后必须同时更新 index.html 和 archive.html。

## 常见故障处理
| 问题 | 解决方案 |
|------|---------|
| git push TLS错误 | `git config --unset http.sslbackend` |
| git push代理拦截 | `git config --global --unset http.proxy && git push origin main` |
| git push HTTPS超时 | `git remote set-url origin git@github.com:tianyunsu/ocean-data-daily-report.git && git push origin main` |
| sandbox阻止SSH push | `GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=accept-new" git push origin main` |
| run_daily_report.py编码错误 | `$env:PYTHONUTF8=1; python run_daily_report.py` |
| deploy_report.py卡住 | 手动：复制HTML到posts/ → 更新index/archive → git push |
| Python urllib 出网被拒(WinError 10061) | 沙箱阻断 Python 直连外网。链接校验改用 WebFetch 工具，勿写 Python 探测脚本 |
| git push 连 127.0.0.1:65532 失败 | 环境变量 `HTTP_PROXY/HTTPS_PROXY` 指向不可用代理。`unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy` 后再 `git -c http.proxy= -c https.proxy= push origin main` |
| git push 443 超时/Connection reset | GitHub 直连不稳定，**循环重试 3-5 次通常可成功**（注意 Git Bash 无 `sleep`，勿在循环中调用）。SSH 方式因本机无 publickey 不可用 |
| git commit 报 unable to auto-detect email | 仓库级配置：`git config user.name "tianyunsu" && git config user.email "tianyunsu@users.noreply.github.com"` |
| generate_html_daily.py 报 No module named 'requests' | 该脚本 `exec` 了 feishu_write_doc.py 头部（含 import requests）。改用 `gen_html_0803.py` 式自包含生成器：`ast.literal_eval` 解析 SECTIONS，不触发任何 import |
| 改条目后首页仍显示旧内容 | index.html / archive.html 的 post-excerpt 摘要是硬编码文本，删改条目后必须同步 Edit 这两处 |
| 飞书docx blocks 404 | 疑app token缺docx写入权限 |

## 去重基准（滚动更新）
- 2026-04-30~05-09：GOFLOW、NOAAGlobalTemp v6.1、xarray v2026.04.0、GEBCO_2026、PANGAEA Event-Campaign Merge、IndOBIS、Copernicus AI下一代业务化海洋产品、DestinE GMD论文、DSON-DT深海数字孪生、OSR 9哥白尼海洋状况报告、NOAA首套深海eDNA数据集、Argo叶绿素再处理、Seabed 2030 28.7%、EGU 2026 DestinE数字孪生展示、NOAA $21.6M无人系统合同、WMO厄尔尼诺预测、Nature Communications(热带气旋预测等)、IOCCG PACE再处理、HyperCP v1.2.15、OceanPile
- 2026-05-13：OCEANPILE浙大海洋语料库、陈大可院士AI海洋理论、GDAL 3.13.0、NCEI Data Tour Notebooks、探索一号全球深渊156天、深蓝百万里西太航次、NCEI云迁移AWS、BGC-Argo+二次QC、NOAA无人水文测量/LR30、自主船舶数字孪生综述JMSA
- 2026-05-15：AxiomOcean arXiv 2605.10455、CMEMS AI下一代海洋产品、GEOXYGEN ESSD全球DO数据集、王军成院士AI海洋观测、奋斗者号156天航次、MCC 2026挑战赛、NASA PO.DAAC ECCO教程
- 2026-05-18：Njord GNN集成预报 arXiv 2605.15470、ECMWF IFS 50r1/AIFS v2首次AI波浪预报 05-12、STC南海校正器 Frontiers 05-13、DITTO Summit 2026横滨、NSR柴扉海洋DT综述、CopernicusLAC Chile可视化平台、玄武Argo数字孪生异常检测、JAMSTEC Argo QC path-signature J.Oceanogr 04-29、North Pacific nutrient ML ESSD 04-28、Eos美国海平面科学削减、pyTMD v3.0.7、Copernicus Marine Toolbox v2.4.1
- 2026-05-25：中科院琅琊海洋大模型北极海冰 05-19、信通院AI赋能海洋产业报告 05-18、DestinE气候DT第二代1990-2049 05-18、海洋DT助力全球治理 05-21、SwinIR南海风场降尺度、东海叶绿素ML MDPI 04-30、IOOS QARTOD、BGC-Argo+ ESSD 05-12、UNet海洋风场降尺度、ML海洋数据同化综述、IODE虚拟实验室、HUB Ocean、NOAA WOD季度更新、探索一号+奋斗者156天太平洋 05-10、NOAA Okeanos EX2603 05-16、Schmidt亚马逊峡谷 05-17、西澳eDNA巨型鱿鱼、CMEMS月报、PANGAEA 04-28、六边形DGGS Big Earth Data 05-20、DEA无代码平台
- 2026-05-28：OceanAI大模型山东科大 05-28、Volador 1.0 MOE-Swin-Transformer南海海气耦合 arXiv 05-21、Njord概率GNN集合预报 arXiv 05-15、聚类算法地中海海表变率 arXiv 05-27、DSON-DT深海观测网DT 05-01、六边形DGGS 05-20、DEA无代码 05-01、IOC海洋数据战略计划 05-20、中科院创新二号北黄海 05-19、IOOS 5月通讯 05-22、CMEMS Q1 2026数据扩展 05-26
- 2026-05-29（淡周5条）：OCEANS 2026三亚大会海洋AI专题 05-26、MSP DataViz v1.0-beta 3D海洋可视化 05-24、OceanSR-Prob扩散模型风速降尺度 Neurocomputing 05-22、PACE Data Hackweek报告 Oceanography 05-19、CMEMS Understanding Our Ocean II 05-26
- 2026-06-01：FuXi-Ocean DL全球海洋预报 npj Climate、CMEMS Understanding Our Ocean III、IOOS DMAC 2026年会、IOOS 5月通讯
- 2026-06-11~06-26：supplement分支机器生成（约100条，去重参考posts/目录）
- 2026-07-01：扩散模型全球海况/ENSO arxiv、CMEMS第9届大会AI+物理混合、MyOcean Health Viewer、EU OceanEye GOOS、GLODAPv3、Sentinel-6B、ICAMS
- 2026-07-06：DL印度季风/风暴分辨AI/Argo热含量arxiv、EOSC Blue-Cloud DT、Copernicus Ocean Temp Bulletin
- 2026-07-09：中科院LangYa框架、CNN海洋生物多样性 Frontiers、ISPRS海洋色遥感3D+AI、EDITO平台、geoai-py
- 2026-07-13：世航智能沧穹CEORION融资、湛江湾1号海洋鸿蒙、三亚深海科考AI、华大智造海洋生物AI、WavyOcean 3.0(首报)
- 2026-07-16：DCGNet/域偏移基准/有害藻华ML arxiv、南溟海洋大模型、MOL IBM AI船舶风险
- 2026-07-21：SALT/AquaStereo arxiv、崂山实验室预报模型、蓝鲲智种大模型、WAIC 2026 AI赋能海洋论坛、pyglider、VirtualFleet
- 2026-07-24：AUV海底压缩/DREAM VLM/多智能体RL arxiv、CVPR 2026水下视觉(Earth2Ocean/NemoNet/UDVSR-Net/AdaMSCol)、台风风暴潮预报、CMEMS SST产品
- 2026-07-28：MarineEVT(ECCV 2026)、RHCNet/MARIS/BiPA(CVPR 2026)、MaCVi Workshop(CVPR 2026)、生成状态空间模型、AUV浮游生物、WavyOcean 3.0、Nautilus NA180、wavespectra v4.8.0、raschii v2.0.0、CMEMS Argo QC3
- 2026-07-31：KIST-Ocean Science Advances、琅琊2.0、Immersive Ocean ILIAD ISPRS、BGC-Argo VAE biofouling、青岛可信数据空间、数据产权登记、Okeanos EX2605、科学号第15次西太、CMEMS 7月新版本、GEBCO 2026研讨会、pyo-oracle v1.0.0。**去重事故**：MARIS/WavyOcean 3.0/CMEMS Argo QC3已在上期报道
- 2026-08-03（16条/9方向）：HybridOM(ICML 2026)、BALLAST(ICML 2026)、SWIN-DeepONet(IJCAI-ECAI 2026)、多尺度CNN+DropKey-Transformer海况估计(JMSE 07-29)、V-JEPA视频波浪参数(arXiv 07-15)、ECCV 2026海洋视觉研讨会征稿、DestinE第三阶段、CMEMS路线图MyOcean Pro 3D(07-27)、边缘云协同实时QC专利CN122346797A(07-07)、BGC-Argo CHLA再处理(07-11)、ODIS指导小组筹备IODE-29(07-22/23)、IOC执行理事会第59届数据互操作决议(07-03)、Schmidt加勒比盐指航次(08-06起)、CMEMS 7月服务发布新MFC(07-07)、xarray v2026.07.0、uxarray v2026.07.0。**时效修正**：草稿中「海洋十年公民科学FAIR指南」实为2026-02-12发布、「中国Argo智能系统」页面2025-08-29编辑，均>60天已删除替换
- 2026-08-07（17条/9方向）：盘古海洋智能预报大模型工程化落地(08-03,全国首个AI+全栈国产算力)、生成式AI海啸概率预报arXiv 2608.04327(08-05)、BG4Sea生物地球化学季节预报arXiv 2607.16731(07-18,豁免,Mercator Ocean)、Swimm3R水下3D重建arXiv 2608.00950(08-02)、DITTO Summit 2026早鸟注册/8-25议程(07-30,更新)、2DCNN-LSTM Sentinel-2沙波测深Remote Sens 18(15):2511(08-01)、贝叶斯多模态AUV生境测绘EAAI+multimodal-auv(07-01,豁免)、海洋二所RAISE-Ocean入选联合国科学十年第三批全球计划(08-01)、MDImageNet海废影像资料集CC BY 4.0+国际AI竞赛(中国台湾海洋委员会,07-30)、DORI虎鲸声学数据集5298小时(08-07,KDD 2026审稿)、奋斗者号Nature鲸类化石群(06-10发表,豁免58天)、E/V Nautilus NA181威克岛深海探索(08-20起)、cstar-ocean v0.8.0(08-05,更新)、oceanspy v0.3.6(06-15,豁免53天)
- 2026-08-10（14条/9方向）：中国科协年会海洋系统AI大模型专题论坛(07-28)、王凡所长多智能体协同大模型战略、UUV视觉控制框架arXiv 2608.04723(08-05,IFAC WC 2026)、UUV规划学习框架arXiv 2608.05365(08-05)、ML辅助事件感知QC框架JMSE 14(16):1462(08-08)、AUV海底图像AI远程感知arXiv 2607.18013(07-30,豁免26天)、青岛发布全国首个海洋公共数据团体标准(08-06)、联合国海洋十年第11轮行动征集、NOAA Okeanos EX2605库克群岛探险进入最后阶段(更新)、E/V Nautilus NA180即将结束NA181接力(更新)、raschii v2.0.1、wavespectra v5.0预告
- 2026-08-14（13条/9方向）：琅琊海洋大模型技术框架Science Bulletin论文(08-12,更新,1/12°全球1-7天128变量)、Multi-AUV值梯度引导多智能体扩散RL arXiv 2608.12436(08-12)、李群随机PINN水下航行器动力学arXiv 2608.08356(08-08)、BenthiCat光-声多模态数据集ESSD(08-10,约百万SSS瓦片+3.6万标注)、CMEMS In Situ TAC综述澳32台滑翔机150万条剖面入网(07-30,豁免15天)、科学号西太共享航次返港捕捉3次台风(08-07,更新)、NOAA EX2605库克群岛ROV探险收官(08-13,更新)、gridstats v2.6.0(08-12)、π-SUB物理信息合成水下图像基准(arXiv 08-11)。**时效修正**：marinesitu.eu One Ocean文章实为04-30发布(>60天)已改引CMEMS主站07-30综述；EX2605 URL与08-10重复改media-resources页
- 2026-08-18（12条/9方向）：AMR-Pose主动LED标记+概率切换PnP协同AUV相对位姿arXiv 2608.12866(08-13)、LinStereo线性复杂度全局注意力水下立体匹配+SeaStereo数据集ECCV 2026 arXiv 2606.25437(06-24,豁免55天)、福建渔区海况预报全国首个省级渔区七天逐时预报(08-10)、山东港口日照港集装箱数字孪生系统上线(08-14)、DTF-Net深度学习关联检验风数据质控JMSE 14(16):1453(08-07)、条件多元函数PCA重建海豹生物记录器部分温盐剖面arXiv 2608.05376(08-05)、哨兵-2超时相数据立方体光学测深70-80米Science of Remote Sensing(08-14/EUSPA 08-16)、OBIS南极ROV底栖图像丰度数据集TANGO1-TANGO2(08-14)、NOAA EX2606美属萨摩亚ROV探险(08-19起)、GEBCO_2026网格WMS图层上线(08-04)。**时效剔除**：TIDE(arXiv 2512.07171实为2025-12-08提交>60天)、PDIM(Acta Oceanol Sin 2026-01-23发表>60天)、OceanMCP(coops-mcp首发02-21>60天)、Schmidt/Rutgers盐指航次(与08-03重复)
