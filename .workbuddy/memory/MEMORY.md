# 海洋AI研究日报系统记忆（精简版）

## 系统配置

- **用户**：苏老师
- **自动化任务ID**：`ai`
- **CWD**：`C:/Users/Administrator/WorkBuddy/Claw`（正确）
- **Schedule**：`FREQ=DAILY;BYHOUR=9;BYMINUTE=0`
- **GitHub**：https://github.com/tianyunsu/ocean-data-daily-report
- **网站**：https://tianyunsu.github.io/ocean-data-daily-report/

## 一致性机制（手动 = 自动，关键约定）

- **单一权威源**：`ocean-daily-report` skill 是手动触发与定时自动化共用的唯一流程定义；自动化 prompt 已改为对该 skill 的纯委托，不重复内联细节。
- **阶段六记忆写入**：每次执行（无论手动/自动）必须写入：`.workbuddy/memory/YYYY-MM-DD.md` 每日日志 + `MEMORY.md` 去重基准更新；可选追加 `automations/ai/memory.md` 执行摘要。
- **一致性铁律**：手动触发 ≠ 简化执行，必须产出与自动完全相同的工件（`daily_reports/海洋AI简报_YYYY-MM-DD.html` + `posts/YYYY-MM-DD.html` + 记忆文件）。
- **通用方法论 skill**：`automation-consistency`（用户级 `~/.workbuddy/skills/`）沉淀了"诊断手动/自动记忆断层 → 改 skill 铁律 → 自动化 prompt 纯委托 → 补写历史日志"的完整流程，其他定时任务可复用。

## 日报结构

9个方向：海洋AI、数字孪生、可视化、数据质量、数据处理、数据管理与共享、开放航次/船时共享、海洋数据中心、工具与代码资源

## 执行流程

```
步骤1 - 更新 feishu_write_doc.py SECTIONS 数据
步骤2 - 生成 HTML 简报 (daily_reports/海洋AI简报_YYYY-MM-DD.html)
步骤3 - 执行 feishu_write_doc.py（推送飞书文档）
步骤4 - 执行 run_daily_report.py（飞书机器人通知，需 $env:PYTHONUTF8=1）
步骤5 - 执行 deploy_report.py（发布到 GitHub Pages）
```

## 内容质量规则（必须遵守）

1. **近7天优先**，超1个月一律删除，1周~1个月仅保留高价值内容
2. **每条URL必须先fetch返回200**，404/403/超时一律不收录
3. **工具版本特性必须从官方release notes核实**，不得推断
4. **摘要必须从原文提取**，不得根据标题推断内容
5. **方向归类按文章内容判断**，不按来源机构功能判断
6. **跨方向去重**：同URL只能出现在一个方向中
7. **主页新闻必须找到具体链接**，不得使用机构主页URL
8. **各方向严格定义**（2026-05-13教训 → 2026-05-18强化）：
   - **一、海洋AI**：AI/ML/DL模型用于海洋预报、海洋观测、海洋生态模拟。关键词：neural network, transformer, GNN, deep learning, ML, AI model, 预报模型
   - **二、海洋数字孪生**：必须是关于海洋数字孪生本身（架构、框架、应用案例、会议）。不含一般AI模型或数值模型
   - **三、海洋可视化**：必须是关于可视化方法/工具/平台（地图、Dashboard、数据可视化技术、GIS）。不含纯生态学/物理海洋学论文（即使论文中用了图表）
   - **四、海洋数据质量**：必须是关于QA/QC方法、质量控制流程、数据异常检测。不含测绘进展、数据量统计
   - **五、海洋数据处理**：必须是关于数据处理方法/流程/算法（再处理、融合、插值、重采样）。不含软件工具版本发布（→归九）
   - **六、海洋数据管理与共享**：数据政策、FAIR原则、数据共享平台、元数据标准、培训活动、数据开放政策
   - **七、开放航次/船时共享**：科考航次、调查船、海上作业、潜水器、无人船、海洋装备
   - **八、海洋数据中心**：必须是海洋数据仓库/档案馆（如NCEI、PANGAEA、CMEMS数据中心）。不含：IT计算基础设施（海底服务器机房→不归任何方向）、纯气候/物理海洋学论文（→若无合适方向则不收录）
   - **九、工具与代码资源**：仅限软件工具、代码库、开发框架、数据处理程序的新版本发布
   - 硬件装备（无人船、潜水器、传感器）→ 归"开放航次"或对应方向
   - 评估报告/状况报告 → 归"数据中心"或"可视化"，不归工具
   - **宁可某方向为空，也不凑数填入不相关内容**
   - **同软件不同URL（如PyPI和GitHub）只能归一个方向**：归九（工具）

9. **发布前分类自检清单**（2026-05-18教训，每条必须检查）：
   - [ ] 该条内容的核心主题是否与所在方向的严格定义一致？
   - [ ] 是否因为某方向内容不足而被迫归入？（如果是→删除该条）
   - [ ] 该条是否已出现在其他方向中？（URL去重）
   - [ ] "海底数据中心"类新闻是否为IT基础设施（服务器机房）？（如果是→不归八）
   - [ ] Nature Communications/Science 等综合期刊的论文是否按内容而非期刊归入？（按内容判断）

## GitHub Pages 架构

- **main 分支**：源代码 + 每日日报（posts/、index.html、archive.html）
- **supplement 分支**：另一台机器检索结果（不需要本地拉取）
- **gh-pages 分支**：由Actions自动部署（不要手动编辑）
- 每次生成日报后必须同时更新 index.html 和 archive.html

## SECTIONS 数据替换方法（可靠）

使用 `make_new_feishu_v2.py` 方法：
1. 找到原始文件中 `SECTIONS = [` 的精确位置
2. 用 bracket-counting（depth 计数）找到对应的结束 `]`
3. 用新的 SECTIONS 数据整体替换这一段
4. 验证：`compile(new_content, 'feishu_write_doc.py', 'exec')`

## 常见故障处理

| 问题 | 解决方案 |
|------|---------|
| git push TLS错误 | `git config --unset http.sslbackend` |
| git push代理拦截 | `git config --global --unset http.proxy && git push origin main` |
| git push HTTPS超时 | `git remote set-url origin git@github.com:tianyunsu/ocean-data-daily-report.git && git push origin main` |
| push后验证 | `Invoke-RestMethod https://api.github.com/repos/tianyunsu/ocean-data-daily-report/git/refs/heads/main` |
| run_daily_report.py编码错误 | `$env:PYTHONUTF8=1; python run_daily_report.py` |
| deploy_report.py卡住 | 手动：复制HTML到posts/ → 更新index/archive → git push |
| automation CWD错误 | SQL: `UPDATE automations SET cwds='["C:/Users/Administrator/WorkBuddy/Claw"]' WHERE id='ai'` |
| 飞书docx blocks API 404 | 文档可创建（返回doc_id L65edOx0qoOX9dxFfWWc9PZDnff），但内容写入全部返回404，疑为app token缺少`docx:document:readonly`或写入权限范围 |
| sandbox阻止SSH push | `GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=accept-new" git push origin main`（绕过host key检查） |

## 去重基准（滚动更新）

- 2026-04-30：19条已发布（含GOFLOW、NOAAGlobalTemp v6.1、xarray v2026.04.0、GEBCO_2026、PANGAEA Event-Campaign Merge、IndOBIS等）
- 2026-05-06：24条（含Copernicus AI下一代业务化海洋产品、DestinE GMD论文、DSON-DT深海数字孪生、东北浮游生物数据集等）
- 2026-05-07：24条（含GOFLOW、NOAA首套深海eDNA数据集、OSR 9哥白尼海洋状况报告、Argo叶绿素再处理、Seabed 2030 28.7%等）
- 2026-05-08：18条（含EGU 2026 DestinE数字孪生展示、NOAA $21.6M无人系统合同、Thomas Jefferson五大湖测绘、WMO厄尔尼诺预测、三篇Nature Communications论文、IOCCG PACE再处理与HyperCP v1.2.15等）
- 2026-05-09：26条（与05-08部分重叠+新增，含OceanPile、GOFLOW、DestinE GMD、EGU OS4.8、NOAA无人系统、WMO厄尔尼诺、Nature Communications热带气旋预测、NOAA eDNA、Seabed 2030等）
- 2026-05-13：25条（初版22条分类修正后25条。含OCEANPILE浙大海洋语料库、陈大可院士AI海洋理论、GDAL 3.13.0、HyperCP v1.2.15、NCEI Data Tour Notebooks、"探索一号"全球深渊探索156天、"深蓝百万里"西太平洋航次、NCEI云迁移AWS、BGC-Argo+二次QC、NOAA无人水文测量/LR30采购、自主船舶数字孪生综述JMSA、OSR 9等）
- 2026-05-15：21条（含AxiomOcean arXiv 2605.10455、CMEMS AI下一代海洋产品、GEOXYGEN ESSD全球DO数据集、BGC-Argo+ QC预印本、王军成院士AI海洋观测、奋斗者号156天航次完成、MCC 2026挑战赛、NCEI云迁移AWS、2篇Nature Communications NC 05-07/05-11等）
- 2026-05-18：18条（修正后，2026-05-18重新发布。含Njord GNN集成预报 arXiv 2605.15470、ECMWF IFS 50r1/AIFS v2首次AI波浪预报 2026-05-12、STC南海校正器 Frontiers 2026-05-13、DITTO Summit 2026横滨、NSR柴扉海洋DT综述、CopernicusLAC Chile可视化平台、玄武Argo数字孪生异常检测、JAMSTEC Argo QC path-signature J. Oceanogr. 2026-04-29、North Pacific nutrient ML reconstruction ESSD 2026-04-28、Eos美国海平面科学削减、NCEI云迁移FAQ、PANGAEA工作坊、深蓝百万里西太平洋收官、Schmidt 2026计划、Seabed 2030 28.7%、pyTMD v3.0.7、Copernicus Marine Toolbox v2.4.1、Gribstream IFS/AIFS v2迁移指南）
- 2026-05-25：27条（含中科院"琅琊"海洋大模型北极海冰全球第一05-19、信通院AI赋能海洋产业报告05-18、DestinE气候DT第二代1990-2049模拟数据集05-18、海洋DT助力全球治理Maritime Technology Review 05-21、DITTO峰会横滨、SwinIR南海风场降尺度Frontiers 04-16、东海叶绿素ML预测MDPI 04-30、JAMSTEC Argo路径签名QC 04-29、IOOS QARTOD、BGC-Argo+ ESSD 05-12、UNet海洋风场降尺度05-01、ML海洋数据同化综述Ocean Modelling 02-01、IODE虚拟实验室、HUB Ocean平台、NOAA WOD季度更新04-09、探索一号+奋斗者156天太平洋穿越05-10、NOAA Okeanos EX2603 05-16、Schmidt亚马逊峡谷浊流05-17、西澳eDNA巨型鱿鱼Environmental DNA 03-07、CMEMS月报、NASA PO.DAAC ECCO教程05-12、PANGAEA 04-28、CMT v2.4.1 05-11、Parcels粒子追踪、ODV、六边形DGGS Big Earth Data 05-20、DEA无代码数据故事平台）
- 2026-05-28：19条（含OceanAI大模型山东科大05-28、Volador 1.0 MOE-Swin-Transformer南海海气耦合arXiv 05-21、Njord概率GNN集合预报arXiv 05-15、聚类算法地中海海表变率arXiv 05-27、DSON-DT深海观测网数字孪生05-01、海洋DT全球治理05-21、六边形DGGS 05-20、DEA无代码05-01、IOOS QARTOD、UNet海洋风场降尺度05-01、IOC海洋数据战略计划05-20、IODE虚拟实验室、中科院创新二号北黄海05-19、IOOS 5月通讯HF雷达/滑翔机05-22、NOAA Okeanos EX2603 05-16、Schmidt亚马逊峡谷05-17、CMEMS Q1 2026数据扩展05-26、CMEMS月报05-24、Parcels）
- 2026-05-29：5条（淡周。含OCEANS 2026三亚大会海洋AI专题05-26、MSP DataViz v1.0-beta 3D海洋可视化05-24、OceanSR-Prob扩散模型风速降尺度Neurocomputing05-22、PACE Data Hackweek开放科学报告Oceanography05-19、CMEMS Understanding Our Ocean II科普系列05-26）
- 2026-06-01：4条（FuXi-Ocean DL全球海洋预报npj Climate、CMEMS Understanding Our Ocean III、IOOS DMAC 2026年会、IOOS 5月通讯）
- 2026-06-11~06-26：supplement分支机器生成（约100条，不做逐条记录，去重时参考posts/目录）
- 2026-07-01：扩散模型全球海况/ENSO arxiv、CMEMS第9届大会AI+物理混合、MyOcean Health Viewer、EU OceanEye GOOS、GLODAPv3、Sentinel-6B、ICAMS
- 2026-07-06：DL印度季风/风暴分辨AI/Argo热含量arxiv、EOSC Blue-Cloud DT、Copernicus Ocean Temp Bulletin
- 2026-07-09：中科院LangYa框架、CNN海洋生物多样性Frontiers、ISPRS海洋色遥感3D+AI、EDITO平台、geoai-py
- 2026-07-13：世航智能沧穹CEORION融资、湛江湾1号海洋鸿蒙、三亚深海科考AI、华大智造海洋生物AI、WavyOcean 3.0(首报)
- 2026-07-16：DCGNet/域偏移基准/有害藻华ML arxiv、南溟海洋大模型、MOL IBM AI船舶风险
- 2026-07-21：SALT/AquaStereo arxiv、崂山实验室预报模型、蓝鲲智种大模型、WAIC 2026 AI赋能海洋论坛、GLODAPv3、Sentinel-6B、pyglider、VirtualFleet
- 2026-07-24：AUV海底压缩/DREAM VLM/多智能体RL arxiv、CVPR 2026水下视觉集中爆发(Earth2Ocean/NemoNet/UDVSR-Net/AdaMSCol)、台风风暴潮预报、CMEMS SST产品
- **2026-07-28**：21条。顶会论文：MarineEVT(ECCV 2026)、RHCNet/MARIS/BiPA(CVPR 2026)、MaCVi Workshop(CVPR 2026)；其他：生成状态空间模型、AUV浮游生物、WavyOcean 3.0、Nautilus NA180、wavespectra v4.8.0、raschii v2.0.0、CMEMS Argo QC3
- **2026-07-31**：16条。KIST-Ocean Science Advances、琅琊2.0、Immersive Ocean ILIAD ISPRS、BGC-Argo VAE biofouling、青岛可信数据空间、数据产权登记、Okeanos EX2605、科学号第15次西太、CMEMS 7月新版本、GEBCO 2026研讨会、pyo-oracle v1.0.0。**去重事故**：MARIS(CVPR 2026)、WavyOcean 3.0、CMEMS Argo QC3已在上期报道
