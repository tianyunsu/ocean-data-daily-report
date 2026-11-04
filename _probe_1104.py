# -*- coding: utf-8 -*-
import urllib.request, ssl, sys, time
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36'}
urls = [
 'https://e.huawei.com/cn/news/2026/industries/government/shenzhen-municipal-ocean-development-bureau',
 'https://www.163.com/dy/article/LA8E8S0305118HJE.html',
 'https://qdio.cas.cn/2019Ver/News/kyjz/202610/t20261028_8299912.html',
 'https://doi.org/10.48550/arXiv.2610.29313',
 'https://doi.org/10.1145/3840750.3841451',
 'https://www.sznews.com/news/content/2026-10/23/content_32199065.htm',
 'https://weibo.com/ttarticle/p/show?id=2309405359283964608565',
 'https://www.sec.gov/Archives/edgar/data/1846715/000121390026114691/ea031043701ex99-1.htm',
 'https://zenodo.org/records/23674230',
 'https://www.mapgis.com/index.php?a=shows&catid=33&id=1913',
 'https://doi.org/10.1177/14738716261492254',
 'https://doi.org/10.3390/app162110608',
 'https://doi.org/10.3389/fmars.2026.1909271',
 'https://cran.r-project.org/web/packages/argoFloats',
 'https://doi.org/10.48550/arXiv.2610.37731',
 'https://doi.org/10.1038/s41598-026-76456-2',
 'https://doi.org/10.5194/essd-2026-807',
 'https://doi.org/10.5194/essd-18-7963-2026',
 'https://qdhy.cbpt.cnki.net/portal/journal/portal/client/paper/a51033eda8eede3695317df1ee90d24b',
 'https://doi.org/10.48550/arXiv.2610.36410',
 'https://seabed2030.org/?p=3268',
 'https://cioos.ca/new/cioos-joins-the-iode-global-network-as-an-associate-data-unit',
 'https://oceanexplorer.noaa.gov/expedition/ex2701',
 'https://doi.org/10.1029/2026GL124056',
 'https://doi.org/10.1038/s41598-026-78685-x',
 'http://ysfri.ac.cn/info/1108/59428.htm',
 'https://m.cnfin.com/cmjj-lb//zixun/20261030/4488855_1.html',
 'https://marine.copernicus.eu/fr/user-corner/product-roadmap/transition-information',
 'https://www.zhonghongwang.com/show-493-479404-1.html',
 'https://pypi.org/project/oceanarray/',
 'https://www.ebiotrade.com/newsf/2026-10/20261023104103527.htm',
 'https://zenodo.org/records/21251092',
 'https://doi.org/10.3390/computers15110763',
]
for u in urls:
    code = 'ERR'
    try:
        req = urllib.request.Request(u, headers=UA)
        with urllib.request.urlopen(req, timeout=35, context=ctx) as r:
            code = r.status
    except Exception as e:
        code = type(e).__name__ + ':' + str(getattr(e, 'code', ''))
    print(f'{code}\t{u}')
    time.sleep(0.3)
