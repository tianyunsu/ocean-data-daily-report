#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, re, warnings
warnings.filterwarnings('ignore')
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def fetch_full(name, url, show_chars=600):
    try:
        r = requests.get(url, headers=H, timeout=15, allow_redirects=True)
        content = r.text
        clean = re.sub(r'<[^>]+>', ' ', content[:8000])
        clean = re.sub(r'\s+', ' ', clean).strip()
        print(f'=== {name} [{r.status_code}] final_url={r.url} ===')
        print(clean[:show_chars])
        print()
    except Exception as e:
        print(f'=== {name} [ERR] === {e}')
        print()

# CoastWatch retired - find new URL
try:
    r = requests.get('https://coastwatch.noaa.gov/', headers=H, timeout=15, allow_redirects=False)
    print(f'CoastWatch status: {r.status_code}')
    if r.status_code in (301,302,303,307,308):
        print('Redirect to:', r.headers.get('Location'))
    else:
        content = r.text[:2000]
        # find new URL in body
        urls = re.findall(r'https?://[^\s"\'<>]+noaa\.gov[^\s"\'<>]*', content)
        print('Body URLs:', list(set(urls))[:10])
        print('Body:', re.sub(r'<[^>]+>', ' ', content)[:300])
except Exception as e:
    print('CoastWatch err:', e)
print()

# Try new CoastWatch URL
fetch_full('CoastWatch new', 'https://coastwatch.noaa.gov/cwn/index.html')

# Blue-Cloud - does it actually have training materials?
try:
    r2 = requests.get('https://blue-cloud.d4science.org/', headers=H, timeout=15)
    content2 = r2.text
    clean2 = re.sub(r'<[^>]+>', ' ', content2[:5000])
    clean2 = re.sub(r'\s+', ' ', clean2).strip()
    print('=== Blue-Cloud full ===')
    print(clean2[:500])
    has_training = 'training' in content2.lower()
    has_nine = '9 ' in content2 or 'nine' in content2.lower()
    print(f'Has training: {has_training}, has nine: {has_nine}')
    print()
except Exception as e:
    print('Blue-Cloud err:', e)

# SOCAT - does it have ETOOCC2 or v2.1 QC standard?
try:
    r3 = requests.get('https://www.socat.info/', headers=H, timeout=15)
    content3 = r3.text
    clean3 = re.sub(r'<[^>]+>', ' ', content3[:5000])
    clean3 = re.sub(r'\s+', ' ', clean3).strip()
    print('=== SOCAT full ===')
    print(clean3[:400])
    has_etoocc2 = 'etoocc2' in content3.lower()
    has_v21 = 'v2.1' in content3
    print(f'Has ETOOCC2: {has_etoocc2}, Has v2.1: {has_v21}')
    print()
except Exception as e:
    print('SOCAT err:', e)

# SeaDataNet - does it have 3.0 preview?
try:
    r4 = requests.get('https://www.seadatanet.org/', headers=H, timeout=15)
    content4 = r4.text
    has_30 = '3.0' in content4 or 'version 3' in content4.lower()
    has_sem = 'semantic' in content4.lower()
    print('=== SeaDataNet ===')
    clean4 = re.sub(r'<[^>]+>', ' ', content4[:5000])
    clean4 = re.sub(r'\s+', ' ', clean4).strip()
    print(clean4[:400])
    print(f'Has 3.0: {has_30}, Has semantic: {has_sem}')
    print()
except Exception as e:
    print('SeaDataNet err:', e)

# ICES news - does it have 2025 annual open data report specifically?
try:
    r5 = requests.get('https://ices.dk/news/', headers=H, timeout=15)
    content5 = r5.text
    clean5 = re.sub(r'<[^>]+>', ' ', content5[:8000])
    clean5 = re.sub(r'\s+', ' ', clean5).strip()
    print('=== ICES news ===')
    print(clean5[:600])
    has_2025_data = '2025' in content5 and ('open data' in content5.lower() or 'data report' in content5.lower())
    print(f'Has 2025 open data: {has_2025_data}')
    print()
except Exception as e:
    print('ICES err:', e)

# CMEMS access-data - does it mention the specific new SST product with 1/12 degree?
try:
    r6 = requests.get('https://marine.copernicus.eu/access-data/', headers=H, timeout=15)
    content6 = r6.text
    has_sst_grid = '1/12' in content6 or 'SST' in content6
    has_new_product = 'new product' in content6.lower() or 'new sst' in content6.lower()
    print('=== CMEMS access-data ===')
    clean6 = re.sub(r'<[^>]+>', ' ', content6[:5000])
    clean6 = re.sub(r'\s+', ' ', clean6).strip()
    print(clean6[:400])
    print(f'Has SST/1/12: {has_sst_grid}, Has new product: {has_new_product}')
    print()
except Exception as e:
    print('CMEMS err:', e)
