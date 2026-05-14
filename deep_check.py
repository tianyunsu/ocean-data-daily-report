#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, re, warnings
warnings.filterwarnings('ignore')
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def fetch(name, url, keywords=[]):
    try:
        r = requests.get(url, headers=H, timeout=15)
        content = r.text
        clean = re.sub(r'<[^>]+>', ' ', content[:6000])
        clean = re.sub(r'\s+', ' ', clean).strip()
        print(f'=== {name} [{r.status_code}] ===')
        print(clean[:400])
        for kw in keywords:
            found = kw.lower() in content.lower()
            print(f'  Keyword "{kw}": {found}')
        print()
    except Exception as e:
        print(f'=== {name} [ERR] === {e}')
        print()

# 1. CoastWatch - says 'retired'
fetch('CoastWatch', 'https://coastwatch.noaa.gov/', ['retired', 'new website'])

# 2. DITTO - check for governance framework content
fetch('DITTO', 'https://ditto-oceandecade.org/', ['governance', 'framework', 'summit', 'yokohama', 'japan'])

# 3. EGUsphere main page - does it describe BGC preprint?
fetch('EGUsphere main', 'https://egusphere.copernicus.org/', ['biogeochemistry', 'BGC', 'carbon'])

# 4. IODE data - does it describe Ocean InfoHub?
fetch('IODE data', 'https://iode.org/data/', ['InfoHub', 'Ocean InfoHub', 'ecosystem'])

# 5. ICES news - check if 2025 annual report mentioned
fetch('ICES news', 'https://ices.dk/news/', ['2025', 'annual', 'open data', '89'])

# 6. SeaDataNet - check if 3.0 is mentioned
fetch('SeaDataNet', 'https://www.seadatanet.org/', ['3.0', 'semantic', 'interoperability'])

# 7. CMEMS access-data - check if SST product specifically mentioned  
fetch('CMEMS access-data', 'https://marine.copernicus.eu/access-data/', ['SST', 'sea surface temperature', '1/12'])

# 8. SOCAT - check if ETOOCC2 v2.1 is mentioned
fetch('SOCAT', 'https://www.socat.info/', ['ETOOCC2', 'v2.1', 'quality control standard'])

# 9. GO-BGC - check if workshop Aug 2026 mentioned
fetch('GO-BGC', 'https://www.go-bgc.org/', ['2026', 'workshop', 'August', 'Monterey'])

# 10. Blue-Cloud - check if 9 materials mentioned
fetch('Blue-Cloud', 'https://blue-cloud.d4science.org/', ['nine', '9', 'training', 'materials', 'open access'])

# 11. NOAA AOML argo - check if it matches description
fetch('NOAA AOML Argo', 'https://www.aoml.noaa.gov/argo/', ['quality control', 'QC', 'deployment'])
