#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 SECTIONS 数据为 2026-04-07"""
import re

NEW_SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. Science Bulletin综述:AI海洋现象预报的分类体系与大型海洋模型展望',
                'badge': '[综述]',
                'abstract': 'Science Bulletin（Science China Press）于2026年4月2日发表由李晓峰等学者撰写的综述"Artificial intelligence for ocean phenomena forecasting"，系统评述AI海洋预报的分类体系：小时-天尺度大气强迫灾害、天-周/月中尺度波浪动力学、月-年尺度耦合气候-冰冻圈模态。提出面向海洋现象的大型海洋模型（LOM）概念，旨在弥合海洋状态变量预报与海洋现象预报之间的鸿沟，为AI驱动的海洋预报提供五个基本设计见解。DOI: 10.1016/j.scib.2026.04.002',
                'source': 'Science Bulletin / ScienceDirect',
                'date': '2026-04-02',
                'url': 'https://www.sciencedirect.com/science/article/pii/S2095927326003336'
            },
            {
                'title': '2. Springer Blue Biotechnology综述:AI技术赋能可持续海洋资源管理',
                'badge': '[综述]',
                'abstract': 'Springer Blue Biotechnology于2026年4月2日发表开放获取综述"Leveraging AI techniques for sustainable marine resources"，系统回顾机器学习与深度学习在海洋生物多样性评估、渔业管理、污染检测和气候影响预测中的最新进展。文章指出数据驱动模型正从日益多样化的海洋观测数据中提取可操作知识，同时分析了AI整合到可持续海洋治理中面临的结构性挑战与新兴机遇。DOI: 10.1186/s44315-026-00054-0',
                'source': 'Blue Biotechnology / Springer',
                'date': '2026-04-02',
                'url': 'https://link.springer.com/article/10.1186/s44315-026-00054-0'
            },
            {
                'title': '3. Lloyd\'s Register 4月刊:海事AI转型潜力——从边缘创新走向运营核心',
                'badge': '[报告]',
                'abstract': 'Lloyd\'s Register知识平台Horizons于2026年4月刊发布报告"Understanding the potential for marine AI transformation"，指出海事AI市场2024年估值41.3亿美元，预计未来五年CAGR达23%。AI正从边缘实验走向运营战略核心，但成功取决于数据质量与组织准备度。LR推出数字成熟度指数（DMI）扩展版帮助航运企业评估AI就绪水平，强调人员技能与治理框架的重要性。',
                'source': 'Lloyd\'s Register / Horizons',
                'date': '2026-04',
                'url': 'https://www.lr.org/en/knowledge/horizons/april-2026/understanding-the-potential-for-marine-ai-transformation/'
            },
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin / Marine Digital Twin',
        'items': [
            {
                'title': '1. Ocean Aero环境动力无人艇:世界首艘AUSV推动海洋自主观测',
                'badge': '[新装备]',
                'abstract': 'Ocean Aero公司2026年4月发布最新动态，其研发的世界首艘且唯一的环境动力自主水下与水面航行器（AUSV）持续推动海洋自主观测能力边界。该AUSV利用波浪和太阳能驱动，无需传统燃料即可执行长续航海洋数据采集任务，对海洋数字孪生系统的实时数据 feeding 和验证具有重要意义，被视为海洋观测技术的重要突破。',
                'source': 'Ocean Aero / Mintz',
                'date': '2026-04-02',
                'url': 'https://www.mintz.com/insights-center/viewpoints/2151/2026-04-02-sustainable-energy-infrastructure-client-feature-ocean'
            },
            {
                'title': '2. Posidonia 2026:海事AI技术将集中亮相全球航运盛会',
                'badge': '[会议]',
                'abstract': 'Seatrade Maritime于2026年4月2日报道，即将召开的Posidonia 2026（6月9-13日，雅典）将集中展示海事AI领域最新进展。业界正通过安全、合规和投资回报三大维度评估AI应用，航运数字化和AI自主系统将成为核心议题之一，反映海事行业对AI技术规模化落地的审慎态度与期待。',
                'source': 'Seatrade Maritime',
                'date': '2026-04-02',
                'url': 'https://www.seatrade-maritime.com/event-news/maritime-ai-developments-to-be-showcased-at-posidonia-2026'
            },
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization / Marine Data Visualization',
        'items': [
            {
                'title': '1. MAGICA暑期学校:沿海海洋数据开放科学分析与可视化实践（4月20-24日）',
                'badge': '[培训]',
                'abstract': '由CMCC基金会主办、MAGICA和FERS项目资助支持的"Open Science in Practice for Coastal Ocean Data Analysis and Visualization"暑期学校将于2026年4月20-24日在意大利Bertinoro举行。课程以实践为导向，学员将使用Jupyter Notebook和开源工具，在云环境中进行沿海海洋模型与观测数据的分析与可视化，学习透明协作的数据工作流程，包括数据共享、版本控制和长期可复现性。GitHub仓库已开放课程资料。',
                'source': 'CMCC / MAGICA / GitHub',
                'date': '2026-04-02(更新)',
                'url': 'https://github.com/OpenScienceComputing/Open_Science_2026'
            },
            {
                'title': '2. Global Fishing Watch更新:海洋透明度可视化数据持续扩充',
                'badge': '[更新]',
                'abstract': 'Global Fishing Watch于2026年3月31日更新其可视化平台，持续推进海洋活动透明度建设。平台通过地图可视化和数据分析为科学研究和政策制定提供支持，每日处理约200万平方公里海洋数据，监测全球捕捞活动。GFW的可视化工具和开放数据API是全球海洋渔业治理的重要基础设施。',
                'source': 'Global Fishing Watch',
                'date': '2026-03-31',
                'url': 'https://globalfishingwatch.org/'
            },
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality / Marine Data Quality Control',
        'items': [
            {
                'title': '1. NOAA IOOS发布2026年4月通讯:OTT海洋技术转化资助机会开放',
                'badge': '[资助]',
                'abstract': 'NOAA综合海洋观测系统（IOOS）于2026年4月初发布最新通讯，宣布OTT（Ocean Technology Transition）计划2026年度资助机会正式开放。该计划旨在缩短海洋观测技术从研究到业务化的转化周期，寻求处于高级开发阶段的原型技术（包括传感器、平台增强和数据管理技术）。意向书建议截止4月27日，最终申请截止7月15日。通讯同时展示了太平洋西北部捕蟹笼低成本溶解氧传感器的部署案例。',
                'source': 'NOAA IOOS',
                'date': '2026-04-03',
                'url': 'https://ioos.noaa.gov/communications/eyes-on-the-ocean-ioos-bi-weekly/eyes-on-the-ocean-ioos-newsletter-april-2026/'
            },
            {
                'title': '2. IODE发布海洋数据QA/QC在线培训课程新安排',
                'badge': '[培训]',
                'abstract': 'IODE于2026年3月30日在IOC海洋培训门户更新QA/QC培训课程信息，与海洋十年数据共享协调办公室及多国专家合作，为全球海洋数据管理从业者提供海洋数据质量保证和质量控制入门培训。课程涵盖数据质量评估、异常检测和多要素质控实操，持续推动全球海洋数据质控能力建设。',
                'source': 'IODE / IOC-UNESCO',
                'date': '2026-03-30(更新)',
                'url': 'https://iode.org/training-course-data-quality-assurance-qa-and-quality-control-qc-in-the-ocean-decade/'
            },
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing / Marine Data Processing',
        'items': [
            {
                'title': '1. WMO发布2026年3月-4月全球季节性气候更新:ENSO中性过渡期',
                'badge': '[报告]',
                'abstract': '世界气象组织（WMO）于2026年3月20日发布全球季节性气候更新，指出2025年11月至2026年1月全球海表温度持续偏高。预计2026年3-5月赤道太平洋将经历从La Nina向ENSO中性状态的过渡期。该报告整合全球海洋观测数据和多个预测模型输出，是海洋气候数据处理和预测的权威参考。',
                'source': 'WMO',
                'date': '2026-03-20',
                'url': 'https://wmo.int/media/update/global-seasonal-climate-update-march-april-may-2026'
            },
            {
                'title': '2. Nature:人类活动加剧海表温度体制转换频率与振幅',
                'badge': '[论文]',
                'abstract': 'Nature Communications于2026年3月19日发表研究"Human-induced intensification of sea surface temperature regime shifts"，结合观测与模拟数据揭示全球大型海洋生态系统中海表温度体制转换的频率和振幅增加了130-140%。该研究对海洋数据处理中的长期趋势识别和体制转换检测方法学具有重要影响，凸显了人类活动对海洋气候状态变化的深层影响。',
                'source': 'Nature Communications',
                'date': '2026-03-19',
                'url': 'https://www.nature.com/articles/s41467-026-70986-z'
            },
            {
                'title': '3. Open Waters平台发布:开源海洋软件与数据导航门户',
                'badge': '[新平台]',
                'abstract': 'Open Waters（openwaters.io）于2026年3月22日正式发布，定位为开源海洋软件与数据的导航门户，帮助用户发现和理解通过开源协作构建的海上工具。该平台汇集各类海洋数据处理、可视化和分析工具，为海洋科研人员提供一站式的开源工具发现与比较服务。',
                'source': 'Open Waters',
                'date': '2026-03-22',
                'url': 'https://openwaters.io/'
            },
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing Services',
        'items': [
            {
                'title': '1. Geo Blue Planet渔业数据研讨会:海洋数据支撑可持续渔业（4月21-22日）',
                'badge': '[会议]',
                'abstract': '联合国海洋十年"海洋预测的协调观测"（GEO Blue Planet）将于2026年4月21-22日在伦敦NEAFC总部举办渔业数据研讨会，聚焦海洋环境观测数据（卫星和现场）与建模如何支持全球可持续渔业管理。研讨会将汇集渔业科学家、数据管理者和政策制定者，探讨海洋数据产品在渔业评估和治理中的应用路径。',
                'source': 'GEO Blue Planet / UN Ocean Decade',
                'date': '2026-03-25(发布)',
                'url': 'https://geoblueplanet.org/wp-content/uploads/2026/03/Fisheries-Workshop-Concept-Note.pdf'
            },
            {
                'title': '2. Ocean Connect Asia 2026:自主系统与海洋数据技术区域会议',
                'badge': '[会议]',
                'abstract': 'Ocean Connect Asia 2026于2026年3月31日-4月1日在新加坡举行，作为区域海洋科技交流平台，汇聚自主系统、机器人和无人化解决方案领域的前沿进展。会议涵盖海洋数据采集、水下通信和海洋监测技术等方向，推动亚太地区海洋数据技术的创新与协作。',
                'source': 'Ocean Connect Asia',
                'date': '2026-04-01',
                'url': 'https://www.maritimeindustries.org/events/all-events/ocean-connect-asia-2026'
            },
            {
                'title': '3. DCO在OSM26展示海洋数据共享服务最新进展',
                'badge': '[会议]',
                'abstract': '数据共享协调办公室（DCO）在2026年2月于格拉斯哥举行的海洋科学大会（OSM26）上展示最新成果，主题为"Bridging the Ocean with Data: Connected Regional Services Driving a Resilient, Interoperable Global Ocean"。DCO展示了区域数据服务的最新进展及其在全球海洋数据互操作中的角色，推动开放数据服务的采纳。',
                'source': 'DCO / OSM26 / UN Ocean Decade',
                'date': '2026-02(OSM26)',
                'url': 'https://www.linkedin.com/posts/dco-ocean-data-sharing_dco-ods-at-osm26-activity-7429535657951244288-pnqL'
            },
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises / Ship Time Sharing',
        'items': [
            {
                'title': '1. Schmidt Ocean Institute公布2026年科考航次计划:聚焦南大西洋深海探索',
                'badge': '[航次]',
                'abstract': 'Schmidt Ocean Institute于2026年发布年度科考航次计划，R/V Falkor (too) 2026年将继续探索南大西洋这一全球最缺乏研究的海域之一。SOI持续为国际科研团队提供免费船时，支持深海探索、海洋生物发现和新技术验证。该计划是国际开放船时共享的重要实践，对推动全球海洋科学前沿发现具有关键作用。',
                'source': 'Schmidt Ocean Institute',
                'date': '2026(年度计划)',
                'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/'
            },
            {
                'title': '2. NSF共享航次计划网站更新:2027年度需求征集进行中',
                'badge': '[通知]',
                'abstract': '国家自然科学基金共享航次计划（NORC）官方网站持续更新，当前正在进行2027年度共享航次计划考察需求征集工作。网站同步展示在研航次信息、搭载需求填写注意事项和首席科学家培训材料，为中国海洋科学考察船时共享的核心管理平台。',
                'source': 'NORC / NSFC',
                'date': '2026-04(更新)',
                'url': 'https://www.norc.com.cn/'
            },
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers / Marine Data Centers',
        'items': [
            {
                'title': '1. NOAA IOOS春季会议成果:高频雷达战略与数据网络升级',
                'badge': '[会议]',
                'abstract': 'NOAA IOOS于2026年3月在华盛顿特区举行春季会议，讨论战略方向、高频雷达战略、水位监测和网络摄像头计划等核心议题。IOOS重新授权法案（H.R. 2294）已于3月16日在美国众议院通过，为系统持续运营提供立法保障。各区域协会（GCOOS、NANOOS、GLOS、SECOORA等）在观测技术部署和数据平台开发方面取得新进展。',
                'source': 'NOAA IOOS',
                'date': '2026-03',
                'url': 'https://ioos.noaa.gov/'
            },
            {
                'title': '2. 中科院海洋科学大数据中心(MSDC)6天前更新:西太平洋数据持续扩充',
                'badge': '[更新]',
                'abstract': '中科院海洋科学大数据中心（MSDC）于2026年4月1日完成最新更新，持续发布高质量海洋科学数据集。中心整合热带海洋海表风应力、上层海温异常、全球大洋CO2分压格点数据等多类型数据产品，展现了国内海洋AI应用与数据开放共享的深度结合，是国内重要的海洋数据中心节点。',
                'source': '中科院海洋科学大数据中心 MSDC',
                'date': '2026-04-01(更新)',
                'url': 'http://msdc.qdio.ac.cn/'
            },
            {
                'title': '3. WMO发布全球海洋监测最新简报:海表温度偏高持续',
                'badge': '[报告]',
                'abstract': '世界气象组织（WMO）持续发布全球海洋监测简报，最新数据显示2025年12月至2026年2月全球海表温度持续高于平均水平。该简报整合全球海洋观测系统数据，对理解全球气候变暖背景下海洋热含量变化和极端海洋事件预测具有基础性支撑作用。',
                'source': 'WMO',
                'date': '2026-03-20',
                'url': 'https://cpc.ncep.noaa.gov/products/GODAS/ocean_briefing_gif/global_ocean_monitoring_current.pdf'
            },
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources / Ocean Tools & Software',
        'items': [
            {
                'title': '1. Copernicus Marine Toolbox持续更新:CLI与Python API双模式海洋数据访问',
                'badge': '[工具]',
                'abstract': 'Mercator Ocean International维护的Copernicus Marine Toolbox在GitHub持续活跃，提供命令行界面（CLI）和Python API两种数据访问方式。工具支持全球海洋物理、生物地球化学和海冰数据的元数据查询与批量下载，是访问Copernicus Marine Service数据产品的官方推荐工具。Copernicus Marine Service官网于4月6日完成最新更新。',
                'source': 'Copernicus Marine / GitHub',
                'date': '2026-04-06(更新)',
                'url': 'https://github.com/mercator-ocean/copernicus-marine-toolbox'
            },
            {
                'title': '2. Frontiers论文:AI能力转型推动海洋绿色技术创新的实证研究',
                'badge': '[论文]',
                'abstract': 'Frontiers in Marine Science于2026年3月20日发表论文"Artificial Intelligence, Capability Transformation, and Marine Green Technology Innovation"，通过构建综合分析框架，系统探讨了AI如何影响海洋绿色技术开发。研究发现AI通过能力转型机制驱动海洋绿色技术创新，该结论在多重稳健性检验后仍然成立，为AI赋能海洋可持续发展提供了实证支撑。DOI: 10.3389/fmars.2026.1816756',
                'source': 'Frontiers in Marine Science',
                'date': '2026-03-20',
                'url': 'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1816756/full'
            },
            {
                'title': '3. AI at Sea发布海事AI周报:DNV推出RuleAgent自然语言分类规则导航工具',
                'badge': '[工具]',
                'abstract': 'AI at Sea海事AI情报平台于2026年3月29日发布周报，重点介绍DNV推出的RuleAgent AI工具——该工具使用户能够通过自然语言在30,000页海事分类规则中导航查询。此外报道了多艘自主航行船舶的海试进展和AI驱动的船体检测技术更新，为海事AI工具生态提供了最新动态。',
                'source': 'AI at Sea',
                'date': '2026-03-29',
                'url': 'https://www.aiatsea.com/news'
            },
        ]
    },
]

# Read original file
with open('C:/Users/Administrator/WorkBuddy/Claw/feishu_write_doc.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find SECTIONS start and end
start_line = None
end_line = None
depth = 0
for i, line in enumerate(lines):
    if 'SECTIONS = [' in line:
        start_line = i
        depth = 0
    if start_line is not None and i >= start_line:
        depth += line.count('[') - line.count(']')
        if depth == 0:
            end_line = i
            break

print(f'SECTIONS: lines {start_line+1}-{end_line+1}')

# Generate new SECTIONS text
sections_text = 'SECTIONS = [\n'
for sec in NEW_SECTIONS:
    sections_text += '    {\n'
    sections_text += f"        'title': {repr(sec['title'])},\n"
    sections_text += f"        'en': {repr(sec['en'])},\n"
    sections_text += "        'items': [\n"
    for item in sec['items']:
        sections_text += '            {\n'
        sections_text += f"                'title': {repr(item['title'])},\n"
        sections_text += f"                'badge': {repr(item['badge'])},\n"
        sections_text += f"                'abstract': (\n                    {repr(item['abstract'])}\n                ),\n"
        sections_text += f"                'source': {repr(item['source'])},\n"
        sections_text += f"                'date': {repr(item['date'])},\n"
        sections_text += f"                'url': {repr(item['url'])}\n"
        sections_text += '            },\n'
    sections_text += '        ]\n'
    sections_text += '    },\n'
sections_text += ']\n'

# Rebuild file
new_lines = lines[:start_line] + [sections_text] + lines[end_line+1:]

with open('C:/Users/Administrator/WorkBuddy/Claw/feishu_write_doc.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'[OK] SECTIONS updated with {len(NEW_SECTIONS)} sections')
total = sum(len(s['items']) for s in NEW_SECTIONS)
print(f'     Total items: {total}')
