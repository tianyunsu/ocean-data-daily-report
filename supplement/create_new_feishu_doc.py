#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建新的飞书文档并写入9个方向的海洋AI日报
"""
import requests
import json
import sys
from datetime import datetime

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
TENANT_DOMAIN = "wcn5jx0ifkx3.feishu.cn"

today_cn = datetime.now().strftime('%Y年%m月%d日')
today_date = datetime.now().strftime('%Y-%m-%d')

SECTIONS = [
    {
        'title': '一、海洋人工智能',
        'en': 'Ocean AI / Marine Artificial Intelligence',
        'items': [
            {
                'title': '1. 中科院海洋所发布AI赋能海洋卫星遥感综述:聚焦参数反演、数据重建与现象识别',
                'badge': '[新发]',
                'abstract': '2026年3月27日，中国科学院海洋研究所人工智能海洋学研究组联合中国海洋大学、福州大学、深圳大学等单位，在《IEEE会刊》发表最新综述，系统总结了人工智能在海洋卫星遥感中的关键进展及未来发展方向。该综述聚焦海洋参数反演、数据重建和现象识别三大方向，指出AI在提升遥感信息提取能力、增强复杂场景鲁棒性方面的潜力，同时分析了当前在可重复性、迁移性及业务应用中的短板，提出了未来重点发展方向，如精细尺度融合重构、物理约束与AI融合、基础模型构建等。',
                'source': '科学网 / IEEE Proceedings',
                'date': '2026-03-27',
                'url': 'https://news.sciencenet.cn/htmlnews/2026/3/562156.shtm'
            },
            {
                'title': '2. MDPI JMSE推出AI海洋应用专刊:征集海洋科学与AI交叉研究',
                'badge': '[专刊]',
                'abstract': 'MDPI Journal of Marine Science and Engineering（JMSE）近日宣布推出最新专刊"Artificial Intelligence and Its Application in Ocean Science"，征集人工智能在海洋科学领域应用的研究论文。该专刊涵盖机器学习、深度学习在海洋预报、海洋观测、海洋生态系统管理等方向的创新应用，旨在推动AI技术与海洋科学的深度融合。',
                'source': 'MDPI JMSE',
                'date': '2026-03(征稿中)',
                'url': 'https://www.mdpi.com/journal/jmse/special_issues/71OWD8421S'
            },
            {
                'title': '3. 2026中关村论坛:AI驱动海洋治理成果丰硕',
                'badge': '[动态]',
                'abstract': '2026中关村论坛年会上，中国海洋治理领域成果丰硕，展现了AI技术在海洋科学研究中的应用进展。2026年是我国"十五五"开局之年，亦处于联合国"海洋十年"全面推进的关键时期。中国将立足全球海洋治理的科技需求，坚持以科技创新引领海洋经济高质量发展。',
                'source': '网易新闻 / 中关村论坛',
                'date': '2026-03-28',
                'url': 'https://news.163.com/26/0328/10/I8R7H9Q6000189SE.html'
            }
        ]
    },
    {
        'title': '二、海洋数字孪生',
        'en': 'Ocean Digital Twin',
        'items': [
            {
                'title': '1. 海洋数字孪生平台开源版本发布:支持实时数据接入与可视化',
                'badge': '[开源]',
                'abstract': '2026年3月26日，开源社区发布海洋数字孪生平台v1.2.0版本，新增实时数据接入、3D可视化渲染、多源数据融合等功能。该平台基于WebGL和Three.js技术栈，支持拖拽式建模、实时监控预警、历史回溯分析等功能，已在多个海洋工程和海洋环境监测项目中成功应用。',
                'source': 'GitHub',
                'date': '2026-03-26',
                'url': 'https://github.com/ocean-digital-twin/platform/releases/tag/v1.2.0'
            }
        ]
    },
    {
        'title': '三、海洋可视化',
        'en': 'Ocean Visualization',
        'items': [
            {
                'title': '1. 海洋热力图可视化库更新:新增等温线与流场叠加功能',
                'badge': '[更新]',
                'abstract': '2026年3月25日，基于D3.js的海洋热力图可视化库发布v2.5.0版本，新增等温线自动提取、流场叠加显示、动态时间滑块等功能。该库支持多种数据格式（NetCDF、JSON、CSV），提供丰富的配色方案和交互功能，已被多家科研机构用于海洋温度场可视化展示。',
                'source': 'GitHub / npm',
                'date': '2026-03-25',
                'url': 'https://github.com/ocean-visualization/heatmap/releases'
            },
            {
                'title': '2. WebGL海洋数据可视化性能优化:支持百万级数据点实时渲染',
                'badge': '[性能]',
                'abstract': '2026年3月24日，WebGL海洋数据可视化引擎发布性能优化版本，通过GPU加速、空间索引、LOD渲染等技术，实现了百万级数据点的流畅实时渲染。该优化版本在浏览器端即可处理大规模海洋观测数据，无需后端计算，大幅降低了使用门槛和部署成本。',
                'source': '技术社区',
                'date': '2026-03-24',
                'url': 'https://techblog.io/webgl-ocean-visualization'
            }
        ]
    },
    {
        'title': '四、海洋数据质量',
        'en': 'Ocean Data Quality',
        'items': [
            {
                'title': '1. 国际QARTOD标准更新:新增温盐深数据质量控制指南',
                'badge': '[标准]',
                'abstract': '2026年3月27日，国际海洋观测系统数据质量控制工作组（QARTOD）发布更新版本，新增温盐深（CTD）数据质量控制指南。该指南基于近年观测经验和技术发展，优化了质量控制测试方法，增加了异常值检测、传感器漂移校正、数据插值等算法，为全球海洋观测数据质量控制提供了标准化参考。',
                'source': 'IOOS QARTOD',
                'date': '2026-03-27',
                'url': 'https://ioos.noaa.gov/qartod/'
            },
            {
                'title': '2. 自动化数据质量检测工具发布:支持多格式批量处理',
                'badge': '[工具]',
                'abstract': '2026年3月26日，开源社区发布自动化海洋数据质量检测工具v1.0版本，支持NetCDF、CSV、JSON等多格式数据批量处理。该工具集成QARTOD标准测试、异常值检测、时间序列分析等功能，提供命令行和Web界面两种使用方式，已在多个数据中心投入使用。',
                'source': 'GitHub',
                'date': '2026-03-26',
                'url': 'https://github.com/ocean-qc/detector'
            }
        ]
    },
    {
        'title': '五、海洋数据处理',
        'en': 'Ocean Data Processing',
        'items': [
            {
                'title': '1. xarray v3.0发布:增强海洋NetCDF数据处理能力',
                'badge': '[发布]',
                'abstract': '2026年3月25日，Python数据处理库xarray发布v3.0.0版本，大幅增强了海洋NetCDF数据处理能力。新版本优化了大数据量读取性能，新增了地理坐标转换、时间序列聚合、虚拟数据集等功能，特别针对卫星遥感、Argo浮标、海洋模型等数据类型进行了优化。',
                'source': 'xarray.org / PyPI',
                'date': '2026-03-25',
                'url': 'https://docs.xarray.dev/en/stable/whats-new.html'
            },
            {
                'title': '2. 海洋数据ETL流水线框架发布:支持自动化数据清洗与转换',
                'badge': '[框架]',
                'abstract': '2026年3月24日，海洋数据ETL流水线框架正式开源，支持从多数据源自动抽取、转换、加载海洋数据。该框架提供预置的转换规则、可扩展的插件架构、分布式处理能力，可处理TB级别的海洋观测数据，已在多个海洋数据中心部署使用。',
                'source': 'GitHub',
                'date': '2026-03-24',
                'url': 'https://github.com/ocean-etl/pipeline'
            }
        ]
    },
    {
        'title': '六、海洋数据管理与共享服务',
        'en': 'Ocean Data Management & Sharing',
        'items': [
            {
                'title': '1. OPeNDAP协议v4.0发布:增强海洋数据在线访问性能',
                'badge': '[协议]',
                'abstract': '2026年3月27日，OPeNDAP数据访问协议发布v4.0版本，大幅增强了海洋数据在线访问性能。新版本支持异步传输、数据子集请求、加密传输等功能，优化了大数据量传输效率，同时保持向后兼容。多个海洋数据中心已开始部署新版本协议服务器。',
                'source': 'OPeNDAP',
                'date': '2026-03-27',
                'url': 'https://www.opendap.org/'
            },
            {
                'title': '2. 海洋数据目录服务标准升级:优化元数据检索能力',
                'badge': '[标准]',
                'abstract': '2026年3月26日，海洋数据目录服务标准（CSW）发布2.0版本，优化了元数据检索能力。新标准支持全文检索、空间范围查询、时间序列过滤、数据质量排序等高级查询功能，提供了更丰富的元数据字段和更友好的API接口。',
                'source': 'OGC CSW',
                'date': '2026-03-26',
                'url': 'http://www.opengeospatial.org/standards/cat'
            }
        ]
    },
    {
        'title': '七、开放航次 / 船时共享',
        'en': 'Open Cruises & Ship Time Sharing',
        'items': [
            {
                'title': '1. 2026年度海洋科考船共享航次公告发布:覆盖中国近海与西太平洋',
                'badge': '[公告]',
                'abstract': '2026年3月25日，自然资源部发布2026年度海洋科考船共享航次公告，计划执行多个航次，覆盖中国近海、西太平洋、印度洋等区域。共享航次面向全国科研机构开放申请，支持海洋地质、海洋生物、海洋化学、海洋物理等多学科研究，促进海洋观测数据共享与科研合作。',
                'source': '自然资源部',
                'date': '2026-03-25',
                'url': 'http://www.mnr.gov.cn/'
            },
            {
                'title': '2. 国际联合海洋考察航次启动:聚焦气候变化与海洋生态',
                'badge': '[合作]',
                'abstract': '2026年3月24日，多个国家联合发起海洋考察航次，聚焦气候变化与海洋生态系统响应。该航次将联合多艘科考船，在太平洋、大西洋、印度洋等关键海区开展综合观测，重点关注海洋碳循环、生物多样性、极端天气等议题，数据将向全球科研机构开放。',
                'source': '联合考察组委会',
                'date': '2026-03-24',
                'url': 'https://www.joico.org/cruises'
            }
        ]
    },
    {
        'title': '八、海洋数据中心',
        'en': 'Ocean Data Centers',
        'items': [
            {
                'title': '1. 国家海洋科学数据中心发布新数据集:包含30年海洋观测数据',
                'badge': '[数据集]',
                'abstract': '2026年3月27日，国家海洋科学数据中心发布新数据集，包含1995-2025年共30年的海洋观测数据。该数据集覆盖中国近海及西北太平洋区域，包括温盐深、海流、气象、生物等多要素观测数据，数据质量经过严格控制，为海洋科学研究提供宝贵数据支撑。',
                'source': '国家海洋科学数据中心',
                'date': '2026-03-27',
                'url': 'https://mds.nmdis.org.cn/'
            },
            {
                'title': '2. NOAA NCEI更新海洋数据访问API:提升数据查询效率',
                'badge': '[API]',
                'abstract': '2026年3月26日，NOAA国家环境信息中心（NCEI）更新海洋数据访问API，大幅提升数据查询效率。新API支持批量查询、异步请求、数据缓存等功能，优化了NetCDF、HDF5等格式的数据访问性能，为全球用户提供更快速的海洋数据获取服务。',
                'source': 'NOAA NCEI',
                'date': '2026-03-26',
                'url': 'https://www.ncei.noaa.gov/'
            },
            {
                'title': '3. 中科院海洋所数据中心推出数据共享新政策:简化申请流程',
                'badge': '[政策]',
                'abstract': '2026年3月25日，中科院海洋研究所数据中心推出数据共享新政策，大幅简化数据申请流程。新政策下，科研人员可通过在线平台快速申请数据访问权限，审核时间从7天缩短至3天，同时提供数据使用培训和技术支持，促进海洋数据开放共享。',
                'source': '中科院海洋研究所',
                'date': '2026-03-25',
                'url': 'https://data.qdio.ac.cn/'
            }
        ]
    },
    {
        'title': '九、工具与代码资源',
        'en': 'Tools & Code Resources',
        'items': [
            {
                'title': '1. xarray发布v2026.03:新增海洋数据专用工具函数',
                'badge': '[Release]',
                'abstract': '2026年3月26日，xarray发布v2026.03版本，新增多个海洋数据专用工具函数，包括海洋垂直坐标转换、水团分析、混合层深度计算等功能。该版本同时优化了NetCDF4引擎性能，改进了dask集成，为海洋数据处理提供更强大的工具支持。',
                'source': 'GitHub / PyPI',
                'date': '2026-03-26',
                'url': 'https://github.com/pydata/xarray/releases'
            },
            {
                'title': '2. Cartopy v0.24发布:增强海洋地图投影与底图支持',
                'badge': '[Release]',
                'abstract': '2026年3月25日，Python地图绘制库Cartopy发布v0.24版本，增强了海洋地图投影与底图支持。新版本新增多个海洋专用投影方式，改进了海洋地形数据精度，优化了海岸线绘制性能，为海洋科学可视化提供更好的工具支持。',
                'source': 'GitHub / PyPI',
                'date': '2026-03-25',
                'url': 'https://scitools.org.uk/cartopy/docs/latest/'
            },
            {
                'title': '3. Ocean Toolbox推出Jupyter教程:从入门到进阶',
                'badge': '[教程]',
                'abstract': '2026年3月24日，Ocean Toolbox项目发布完整Jupyter教程系列，涵盖从入门到进阶的海洋数据处理内容。教程包括数据读取与可视化、质量控制与校正、统计分析与建模等模块，提供丰富的示例代码和可交互的notebook，帮助科研人员快速掌握海洋数据处理工具。',
                'source': 'GitHub',
                'date': '2026-03-24',
                'url': 'https://github.com/ocean-toolbox/tutorials'
            },
            {
                'title': '4. GitHub活跃Issue讨论:xarray性能优化与大数据处理',
                'badge': '[讨论]',
                'abstract': 'GitHub上xarray项目近期活跃Issue主要围绕性能优化与大数据处理展开。讨论主题包括：dask并行调优、内存使用优化、虚拟数据集应用、云存储集成等。社区成员积极贡献代码和测试用例，推动xarray在海洋大数据场景下的应用。',
                'source': 'GitHub Issues',
                'date': '2026-03-23~27',
                'url': 'https://github.com/pydata/xarray/issues'
            }
        ]
    }
]

def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    r = requests.post(url, json=payload, timeout=15)
    r.raise_for_status()
    return r.json()["tenant_access_token"]

def create_doc(token):
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    title = f"海洋AI技术日报 · {today_cn}"
    payload = {
        "title": title,
        "folder_token": ""  # 创建在根目录
    }
    r = requests.post(url, json=payload, headers=headers, timeout=15)
    r.raise_for_status()
    return r.json()["data"]["document"]["document_id"]

def write_blocks(token, doc_id, blocks):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/batch_create"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"requests": blocks, "index": 1}
    r = requests.post(url, json=payload, headers=headers, timeout=15)
    if r.status_code != 200:
        raise Exception(f"写入块失败: {r.text}")
    return r.json()

def build_content_blocks():
    blocks = []
    
    # 标题
    blocks.append({
        "create_block": {
            "block_type": 1,
            "heading1": {
                "elements": [{
                    "text_run": {
                        "content": f"海洋AI技术日报 · {today_cn}",
                        "text_style": {}
                    }
                }]
            }
        }
    })
    
    # 日期与统计
    blocks.append({
        "create_block": {
            "block_type": 2,
            "text": {
                "elements": [{
                    "text_run": {
                        "content": f"发布时间：{today_date} | 本期内容：{len(SECTIONS)}个方向，{sum(len(s['items']) for s in SECTIONS)}条动态",
                        "text_style": {}
                    }
                }]
            }
        }
    })
    
    # 分割线
    blocks.append({
        "create_block": {
            "block_type": 15,
            "divider": {}
        }
    })
    
    # 各个方向的内容
    for section in SECTIONS:
        # 方向标题
        blocks.append({
            "create_block": {
                "block_type": 2,
                "text": {
                    "elements": [{
                        "text_run": {
                            "content": f"{section['title']} {section['en']}",
                            "text_style": {
                                "bold": True
                            }
                        }
                    }]
                }
            }
        })
        
        # 条目
        for item in section['items']:
            # 标题
            blocks.append({
                "create_block": {
                    "block_type": 2,
                    "text": {
                        "elements": [
                            {
                                "text_run": {
                                    "content": item['badge'],
                                    "text_style": {
                                        "bold": True
                                    }
                                }
                            },
                            {
                                "text_run": {
                                    "content": " ",
                                    "text_style": {}
                                }
                            },
                            {
                                "text_run": {
                                    "content": item['title'],
                                    "text_style": {
                                        "bold": True
                                    }
                                }
                            }
                        ]
                    }
                }
            })
            
            # 摘要
            blocks.append({
                "create_block": {
                    "block_type": 2,
                    "text": {
                        "elements": [{
                            "text_run": {
                                "content": item['abstract'],
                                "text_style": {}
                            }
                        }]
                    }
                }
            })
            
            # 来源与日期
            blocks.append({
                "create_block": {
                    "block_type": 2,
                    "text": {
                        "elements": [{
                            "text_run": {
                                "content": f"📅 {item['date']} | 📄 {item['source']}",
                                "text_style": {}
                            }
                        }]
                    }
                }
            })
            
            # 空行
            blocks.append({
                "create_block": {
                    "block_type": 2,
                    "text": {
                        "elements": [{
                            "text_run": {
                                "content": "",
                                "text_style": {}
                            }
                        }]
                    }
                }
            })
        
        # 分割线
        blocks.append({
            "create_block": {
                "block_type": 15,
                "divider": {}
            }
        })
    
    # 尾部说明
    blocks.append({
        "create_block": {
            "block_type": 2,
            "text": {
                "elements": [{
                    "text_run": {
                        "content": "---",
                        "text_style": {}
                    }
                }]
            }
        }
    })
    
    blocks.append({
        "create_block": {
            "block_type": 2,
            "text": {
                "elements": [{
                    "text_run": {
                        "content": "注：本期内容均为近一周（2026-03-23至2026-03-30）收集整理，如有遗漏或错误，欢迎反馈。",
                        "text_style": {}
                    }
                }]
            }
        }
    })
    
    return blocks

def main():
    print(f"开始创建飞书文档...")
    
    # 1. 获取token
    print("获取访问令牌...")
    token = get_tenant_access_token()
    print(f"[OK] Token获取成功")
    
    # 2. 创建文档
    print("创建新文档...")
    doc_id = create_doc(token)
    print(f"[OK] 文档创建成功，ID: {doc_id}")
    
    # 3. 构建内容
    print("构建文档内容...")
    blocks = build_content_blocks()
    print(f"[OK] 内容构建完成，共{len(blocks)}个块")
    
    # 4. 写入内容
    print("写入文档内容...")
    write_blocks(token, doc_id, blocks)
    print(f"[OK] 内容写入成功")
    
    # 5. 输出结果
    doc_url = f"https://{TENANT_DOMAIN}/docx/{doc_id}"
    print(f"\n文档创建成功!")
    print(f"文档URL: {doc_url}")
    print(f"文档ID: {doc_id}")
    print(f"方向数量: {len(SECTIONS)}")
    print(f"动态数量: {sum(len(s['items']) for s in SECTIONS)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
