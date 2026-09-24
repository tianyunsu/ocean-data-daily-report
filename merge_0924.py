# -*- coding: utf-8 -*-
"""Merge newly-verified 2026-09-24 items into the existing build_daily_0924.py SECTIONS."""
import ast
import re

SRC = 'build_daily_0924.py'
raw = open(SRC, encoding='utf-8').read()

S = None
for n in ast.walk(ast.parse(raw)):
    if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'SECTIONS':
        S = ast.literal_eval(n.value)
        break
assert S, 'SECTIONS not found'

# keep the existing main() tail
m = re.search(r'\n\ndef main\(\):', raw)
tail = raw[m.start():] if m else ''


def item(title, badge, abstract, source, url, date):
    return {'title': title, 'badge': badge, 'abstract': abstract,
            'source': source, 'url': url, 'date': date}


NEW = {
    '三、海洋可视化': [
        item(
            'LeadNet 与 80 米分辨率泛北极冬季冰间水道数据集',
            '[论文]',
            '中科院海洋所人工智能海洋学研究组提出面向 Sentinel-1 SAR 影像的冰间水道智能检测模型 LeadNet，并据此构建 80 米分辨率的泛北极冬季冰间水道数据集。LeadNet 为双分支结构，分别从 Sentinel-1 HH 极化后向散射影像与灰度共生矩阵纹理中提取特征并在编码阶段融合，以增强复杂海冰背景下细窄水道的识别能力；测试覆盖格陵兰海、楚科奇海、波弗特海、喀拉海、东西伯利亚海及北极中央区，平均交并比 mIoU 0.78、Kappa 0.73，对 100—300 米宽的细窄水道仍保持较好识别能力。研究处理了 2019 年 10 月至 2020 年 4 月北纬 65°以北的 14093 景 Sentinel-1 超宽幅影像，生成含逐景分类结果与逐月频率图的数据集（GeoTIFF，约 1.09 TB，已公开）；形态统计显示宽度小于 300 米或长度小于 5 公里的水道贡献了总水道面积的约 20%—40%，在晚冬与早春显著增加。',
            'International Journal of Digital Earth / 中科院海洋所',
            'https://doi.org/10.1080/17538947.2026.2728309',
            '2026-09-10',
        ),
    ],
    '五、海洋数据处理': [
        item(
            '考虑海浪状态的风应力新参数化方案提升风暴潮与海浪模拟',
            '[论文]',
            '中科院海洋所灾害性海洋动力过程研究组针对近海强风下海气动力参数化不确定性大的问题，提出考虑海浪状态的风应力参数化方案。研究基于多个海区观测资料，发现近岸强风条件下主导波浪的波陡能较好表征风应力变化，据此构建同时考虑观测高度、主导波长与波陡的参数化形式。将该方案应用于台风“梅花”影响下东海近岸风暴潮—海浪耦合模拟，结果表明传统仅依赖 10 米风速的经验公式在强风浪下明显低估风应力及其驱动的海洋动力响应，而新方案使风暴潮与有效波高模拟更接近观测，有效降低了近海极端动力过程模拟的不确定性。成果发表于 Journal of Physical Oceanography。',
            'Journal of Physical Oceanography / 中科院海洋所',
            'https://qdio.cas.cn/2019Ver/News/kyjz/202609/t20260911_8280846.html',
            '2026-09-11',
        ),
        item(
            '语义子原型网络：遥感影像海洋溢油检测',
            '[论文]',
            '遥感监测海洋溢油对海洋环境保护、污染监管与应急处置至关重要，但油水边界模糊不规则、油膜常常小且破碎、溢油外观随油膜厚度与光照变化，导致精准检测困难。Marine Pollution Bulletin 在线论文提出基于语义子原型的检测方法，通过构建具判别性的类别子原型表征来应对类内差异大、样本不均衡的问题，提升复杂海况下溢油区域的识别能力，为遥感溢油业务化监测提供方法支撑。',
            'Marine Pollution Bulletin',
            'https://doi.org/10.1016/j.marpolbul.2026.120317',
            '2026-09-18',
        ),
    ],
    '八、海洋数据中心': [
        item(
            'GEBCO_2026 全球水深网格（15 弧秒）持续开放获取',
            '[数据]',
            'GEBCO_2026 网格于 2026 年 4 月发布，提供全球陆海高程数据，空间分辨率 15 弧秒，网格规模 43200 行 × 86400 列（约 37.3 亿个数据点）。其“基座”为 SRTM15+ 2.8 版（融合陆地地形与基于卫星重力预测的海底地形，并采用 SWOT 卫星高精度重力场与机器学习方法），再叠加 Seabed 2030 四个区域中心的多波束等实测网格，通过“移除—恢复”混合与羽化处理拼接为无缝全球地形模型。该网格已提供 Web 地图服务（WMS）图层，公众可免费使用；本期第三方数据平台也已收录该网格。',
            'GEBCO / Data Basin',
            'https://databasin.org/datasets/f128529f1106485c906883ecb82be7d7',
            '2026-09-14',
        ),
        item(
            'Argo 全球数据汇编中心发布最新全球数据快照',
            '[数据]',
            '国际 Argo 计划的全球数据汇编中心（Argo GDAC，布列斯特与蒙特雷）发布最新全球数据快照（含 BGC-Argo Sprof 子集）。Argo 是由约 3000 台自由漂流剖面浮标组成的全球阵列，测量上层 2000 米温度与盐度，每年提供约 10 万条温盐剖面及流速数据，平均间距约 3°；部分浮标还携带溶解氧、叶绿素等生化参数传感器。所有数据经自动质量控制后在数小时内近实时公开，科学质量控制（延迟模式）数据在采集后 6 个月内通过 GDAC 发布，是海洋与气候研究的关键开放数据底座。',
            'SEANOE / Argo GDAC',
            'https://www.seanoe.org/data/00311/42182/',
            '2026-09-08',
        ),
    ],
    '九、工具与代码资源': [
        item(
            'Copernicus Marine Toolbox 发布 2.5.0b1',
            '[工具]',
            'Copernicus Marine Toolbox（官方 Python 库与 CLI 数据访问工具）发布 2.5.0b1 预发布版。工具箱提供 describe（浏览产品目录与元数据）、subset（按变量、经纬度范围、时间与深度切片，支持 NetCDF/Zarr/CSV/Parquet）、get（按通配符或正则下载原始文件）、open_dataset（经 xarray 远程惰性加载）与 read_dataframe（直接读入 pandas）等能力，数据量与带宽均无配额限制；支持 pip、conda-forge、Docker 与独立可执行文件多种安装方式，可覆盖约 97% 的 Copernicus Marine 数据集切片需求。',
            'PyPI / GitHub (mercator-ocean/copernicus-marine-toolbox)',
            'https://github.com/mercator-ocean/copernicus-marine-toolbox/releases',
            '2026-09-15',
        ),
    ],
}

# 七：用「广海局 AUV 南海超深水搜寻」替换信息量较低的「海洋内波研讨会」
AUV = item(
    '广州海洋地质调查局 AUV 在南海超深水完成失联设备搜寻',
    '[动态]',
    '广州海洋地质调查局 AUV 技术团队在南海中央海盆水深超 4000 米海域成功执行深水搜寻任务，精准定位此前失联的海底科研设备。任务基于单 AUV 平台构建“广域声学搜索—精细声学刻画—近底光学查证”的多层级递进式目标搜索模式：AUV 先以 40—60 米离底高度完成 60 余平方公里声呐全域扫测，再降至 20 米离底高度对重点目标实施高分辨率精细声学探测，最后下潜至距海底 6 米利用高性能光学设备完成近底影像查证，成功搜获海底失联设备。该任务验证了深海无人智能装备在超深水复杂环境下的作业能力，为深海资源勘探与水下应急搜救积累了经验。',
    '中国科学报 / 科学网',
    'https://news.sciencenet.cn/htmlnews/2026/9/571169.shtm',
    '2026-09-09',
)

by_title = {s['title']: s for s in S}
for sec_title, items in NEW.items():
    assert sec_title in by_title, sec_title
    by_title[sec_title]['items'].extend(items)

# replace in 七
q = by_title['七、开放航次与科考']
print('七 before:', [i['title'][:22] for i in q['items']])
idx = None
for i, it in enumerate(q['items']):
    if '内波与混合研讨会' in it['title']:
        idx = i
        break
if idx is None:
    raise SystemExit('未找到内波研讨会条目')
q['items'][idx] = AUV

new_repr = repr(S).replace('\\x27', "'")
out = ('# -*- coding: utf-8 -*-\n'
       '"""Write SECTIONS for 2026-09-24 into feishu_write_doc.py (regex replace)."""\n'
       'import re\n\n'
       'SECTIONS = ' + new_repr + '\n' + tail)
open(SRC, 'w', encoding='utf-8').write(out)

tot = sum(len(s['items']) for s in S)
print('rewritten. per-direction:', {s['title'][:2]: len(s['items']) for s in S})
print('TOTAL', tot)
