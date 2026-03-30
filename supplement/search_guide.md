# 海洋AI研究日报搜索指南

## 使用说明
本文档为搜索代理执行日报检索时的操作指南。

## 搜索配置

### 时间范围
- **优先级**：近1周 > 近1个月 > 近3个月
- **默认范围**：最近7天
- **日期过滤**：只保留在目标日期范围内的内容

### 检索方向（9个）

#### 1. 海洋人工智能（Ocean AI）
**关键词：**
- AI marine / ocean
- Machine learning oceanography
- Deep learning marine
- Artificial intelligence ocean
- Neural network ocean
- 智能海洋 / 海洋AI / 海洋人工智能

**来源：**
- arXiv (cs.LG, stat.ML, physics.ao-ph)
- Google Scholar
- IEEE Xplore
- ScienceDirect
- 中国知网

#### 2. 海洋数字孪生（Ocean Digital Twin）
**关键词：**
- Digital twin ocean
- Ocean digital twin
- DTO (Digital Twin Ocean)
- Marine digital twin
- 数字孪生海洋

**来源：**
- EDITO.eu
- Mercator Ocean
- Google Scholar
- arXiv

#### 3. 海洋可视化（Ocean Visualization）
**关键词：**
- Ocean visualization
- Marine data visualization
- Ocean dashboard
- 海洋可视化 / 海洋数据可视化

**来源：**
- Copernicus Marine
- NASA Climate.gov
- World Ocean Observatory
- NOAA Ocean Explorer
- GitHub (visualization projects)

#### 4. 海洋数据质量（Ocean Data Quality）
**关键词：**
- Ocean data quality
- Marine data QA/QC
- QARTOD
- Ocean data validation
- 海洋数据质量 / 质量控制

**来源：**
- IOOS QARTOD
- OceanBestPractices
- UNESCO IOC
- NOAA IOOS

#### 5. 海洋数据处理（Ocean Data Processing）
**关键词：**
- Ocean data processing
- Marine data analysis
- Oceanographic data
- xarray ocean
- 海洋数据处理

**来源：**
- GitHub (xarray, xoa, netCDF4)
- PyPI
- arXiv
- Google Scholar

#### 6. 海洋数据管理与共享服务（Ocean Data Management）
**关键词：**
- Ocean data management
- Marine data sharing
- IODE
- Ocean data services
- 海洋数据管理 / 数据共享

**来源：**
- IODE / IOC-UNESCO
- Copernicus Marine
- SeaDataNet
- NOAA NCEI

#### 7. 开放航次/船时共享（Open Cruises）
**关键词：**
- Open cruise
- Ship time sharing
- Shared expedition
- 开放航次 / 船时共享

**来源：**
- NSFC (国家自然科学基金委)
- One Ocean Expedition
- 国际海洋考察组织网站

#### 8. 海洋数据中心（Ocean Data Centers）【广泛检索】
**检索策略：不限于具体列出的三个，广泛检索所有海洋数据中心相关动态**

**关键词（英文）：**
- Ocean data centers
- Ocean archives
- Ocean data repository
- Marine data centers
- Marine data repository
- Ocean data infrastructure
- Oceanographic data centers
- NODC (National Oceanographic Data Center)
- Ocean data storage
- Ocean data catalog

**关键词（中文）：**
- 海洋数据中心
- 海洋数据档案馆
- 海洋数据仓储
- 海洋数据基础设施

**检索来源：**
- IODE member centers
- NOAA NCEI
- JAMSTEC Data Center
- BODC (British Oceanographic Data Centre)
- ICDC (ICES Data Centre)
- 中科院海洋数据中心
- 国家海洋科学数据中心
- ESRIN (Earth Observation Centre)
- PO.DAAC (NASA Physical Oceanography DAAC)

**关注要点：**
- ✅ 新数据集发布
- ✅ 数据中心服务升级
- ✅ 数据访问政策更新
- ✅ 新的合作与联盟
- ✅ 数据质量改进
- ✅ 数据可视化增强
- ✅ API更新
- ✅ 元数据标准更新

#### 9. 工具与代码资源（Tools & Code Resources）【多方向检索】
**检索策略：覆盖5个子方向，关注代码平台的更新信号**

##### 子方向1：数据处理流水线
**关键词：**
- Ocean data processing pipeline
- Marine data pipeline
- Oceanographic data workflow
- Data processing automation
- ETL ocean data
- Ocean data transformation

##### 子方向2：QA/QC 方法与实现
**关键词：**
- Ocean data quality control
- Marine data QA/QC
- QARTOD
- Ocean data validation
- Data quality tools
- Quality assurance marine data
- QC algorithms ocean

##### 子方向3：可视化组件与 Dashboard
**关键词：**
- Ocean data visualization
- Marine dashboard
- Ocean plotting tools
- Visualization components
- Interactive ocean data
- Marine data UI
- Ocean data viewer

##### 子方向4：数字孪生相关框架/示例
**关键词：**
- Ocean digital twin framework
- Marine digital twin code
- Digital twin ocean
- DTO framework
- Ocean modeling framework
- Digital twin examples

##### 子方向5：数据共享服务端/客户端工具
**关键词：**
- Ocean data sharing tools
- OPeNDAP
- ERDDAP
- Ocean data API
- Data client tools
- Marine data services
- Ocean data access

**检索平台与关注信号：**

**GitHub:**
- 🚀 关注信号：新 release、重大 PR、活跃 issue、roadmap 更新
- 搜索方式：GitHub search + GitHub API
- 常见项目：xarray/xarray, xarray-contrib/xarray, SciTools/cartopy, glotzerlab/freud, pyoceans/pyoos

**PyPI / conda-forge:**
- 📦 关注信号：新版本发布
- 搜索方式：PyPI RSS feeds, conda-forge package updates

**Docker Hub:**
- 🐳 关注信号：容器镜像更新
- 搜索方式：Docker Hub API, image tags monitoring

**Read the Docs:**
- 📖 关注信号：文档更新、新教程
- 搜索方式：RTD build notifications

**Jupyter / Colab:**
- 📊 关注信号：教程/示例数据发布
- 搜索方式：GitHub notebooks, Colab galleries

**常见工具/库关键词：**
- 核心库：xarray, cartopy, xoa, erddapy, owslib
- 可视化：cmocean, seaborn-ocean, matplotlib-ocean, bokeh-ocean
- 数据访问：pyoos, pyodide, opendap, netCDF4, h5netcdf
- 框架：OceanDT, OceanModels.jl, GOES-2-GLM, Python Ocean Package (POP)

## 搜索流程

### 步骤1：配置时间范围
```python
from datetime import datetime, timedelta
end_date = datetime.now()
start_date = end_date - timedelta(days=7)  # 默认近一周
```

### 步骤2：按方向执行搜索
对每个方向执行搜索，收集候选条目

### 步骤3：时间过滤
筛选只包含在 [start_date, end_date] 范围内的内容

### 步骤4：去重
基于标题关键词进行去重检测，删除重复内容

### 步骤5：重新编号
为每个方向的内容重新编号，确保从1开始连续

### 步骤6：更新 SECTIONS
将结果更新到 `feishu_write_doc.py` 的 SECTIONS 数据结构中

### 步骤7：生成日报
- 运行 `generate_html_report.py` 生成 HTML 简报
- 运行 `feishu_write_doc.py` 生成飞书文档

## 输出格式要求

每个条目必须包含以下字段：
```python
{
    'title': '标题（包含序号，如"1. 标题内容"）',
    'badge': '[标签]',  # 如：[新发]、[更新]、[发布]等
    'abstract': '摘要内容',
    'source': '来源',
    'date': '发布日期',  # YYYY-MM-DD 格式
    'url': '原文链接'
}
```

## 注意事项

1. **时间严格性**：优先展示近一周内容，超出范围的降级展示
2. **来源权威性**：优先收录权威来源（arXiv, 官方网站等）
3. **内容相关性**：确保内容与检索方向高度相关
4. **信息完整性**：尽量包含完整的标题、摘要、来源、日期和链接
5. **标签准确性**：根据内容类型添加合适的标签
6. **去重有效性**：避免重复发布相同内容
7. **编号连续性**：删除重复后重新编号，保证序号连续

## 快速参考

- 检索策略文档：`search_strategy.md`
- 搜索指南文档：`search_guide.md`（本文件）
- 日报生成脚本：`generate_html_report.py`, `feishu_write_doc.py`
- 工作记忆：`.workbuddy/memory/MEMORY.md`
- 每日记录：`.workbuddy/memory/YYYY-MM-DD.md`
