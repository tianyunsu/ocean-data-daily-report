#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
阶段一 · IEEE 期刊通道（Crossref created-date 版）

背景（2026-11-04 建立）：
  OpenAlex 对 IEEE 期刊的 publication_date 做了「年份塌缩」——TGRS 2026 全部记录
  的 publication_date 都是 2026-01-01。任何基于 from_publication_date 的窗口检索
  都会命中 0 条，导致 IEEE 期刊论文结构性无法进入日报。
  实测：TGRS(0196-2892) 在 2026-10-21~2026-11-04 窗口
        OpenAlex = 0 篇 / Crossref from-created-date = 120 篇（海洋相关 15 篇）。

做法：
  1) 用 Crossref `filter=issn:<issn>,from-created-date:<start>,until-created-date:<end>`
     拉窗口内新注册 DOI（created = DOI 注册日，≈ 首发日）
  2) 按海洋关键词筛标题
  3) 命中项用 OpenAlex 按 DOI 取摘要（Crossref 侧 IEEE 记录 abstract 恒为 None）

用法：
  py -3 stage1_ieee_crossref.py                       # 默认窗口：近 14 天
  py -3 stage1_ieee_crossref.py --start 2026-10-21 --end 2026-11-04
  py -3 stage1_ieee_crossref.py --json _stage1_ieee.json
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

UA = 'ocean-daily-report/1.0 (mailto:sutiany@163.com)'

# 阶段一强制的 9 个 IEEE 期刊；每刊列多个 ISSN 变体（print / online）
IEEE_JOURNALS = {
    'JOE':    ['0364-9059', '1558-1691'],   # IEEE Journal of Oceanic Engineering
    'TGRS':   ['0196-2892', '1558-0644'],   # IEEE Trans. Geoscience and Remote Sensing
    'GRSL':   ['1545-598X', '1558-0571'],   # Geoscience and Remote Sensing Letters
    'JSTARS': ['1939-1404', '2151-1535'],   # IEEE JSTARS
    'GRSM':   ['2473-2397', '2168-6831'],   # Geoscience and Remote Sensing Magazine
    'T-RO':   ['1552-3098', '1941-0468'],   # IEEE Trans. Robotics
    'RA-L':   ['2377-3766', '2470-9476'],   # Robotics and Automation Letters
    'TNNLS':  ['2162-237X', '2162-2388'],   # Trans. Neural Networks and Learning Systems
    'TIP':    ['1057-7149', '1941-0042'],   # Trans. Image Processing
}

# 海洋相关性关键词（标题级；宁宽勿窄，靠后续人工/摘要复核收敛）
OCEAN_KW = re.compile(
    r'\b(ocean|oceanic|marine|maritime|seawater|sea[- ]surface|sea[- ]ice|seafloor|'
    r'seabed|bathymetr\w*|underwater|subsea|submarine|sonar|acoustic\w*|'
    r'wave|waves|wavefield|tide|tidal|tsunami|coastal|coast|estuar\w*|'
    r'arctic|antarctic|polar|glacier|iceberg|'
    r'salinity|temperature[- ]salinity|edd(y|ies)|front detection|'
    r'chlorophyll|phytoplankton|algal|coral|plankton|fisher\w*|'
    r'vessel|ship|shipwreck|harbor|harbour|port|'
    r'current|circulation|mixed[- ]layer|thermocline|'
    r'swell|storm[- ]surge|sea[- ]level|wave[- ]energy|offshore|deep[- ]sea)\b',
    re.IGNORECASE,
)


def http_json(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:                                   # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f'request failed: {url} :: {last}')


def crossref_window(issn, start, end, rows=1000, max_pages=8):
    """Crossref：按 createdAt 窗口拉一个 ISSN 的全部 DOI（cursor 翻页）。"""
    out, cursor = [], '*'
    for _ in range(max_pages):
        params = {
            'filter': f'issn:{issn},from-created-date:{start},until-created-date:{end}',
            'rows': str(rows),
            'cursor': cursor,
            'select': 'DOI,title,created,container-title,type',
        }
        url = 'https://api.crossref.org/works?' + urllib.parse.urlencode(params)
        msg = http_json(url)['message']
        items = msg.get('items', [])
        out.extend(items)
        cursor = msg.get('next-cursor')
        if not items or not cursor or len(out) >= msg.get('total-results', 0):
            break
    return out


def openalex_abstract(doi, api_key=''):
    """OpenAlex 按 DOI 取摘要（还原 abstract_inverted_index）。"""
    url = f'https://api.openalex.org/works/https://doi.org/{doi}'
    if api_key:
        url += '?api_key=' + api_key
    try:
        w = http_json(url, tries=2)
    except Exception:                                            # noqa: BLE001
        return '', None
    inv = w.get('abstract_inverted_index') or {}
    if not inv:
        return '', w.get('publication_date')
    pos = []
    for word, idxs in inv.items():
        for i in idxs:
            pos.append((i, word))
    pos.sort()
    return ' '.join(w for _, w in pos), w.get('publication_date')


def read_key():
    env = os.environ.get('OPENALEX_API_KEY', '').strip()
    if env:
        return env
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_openalex_key.txt')
    if os.path.exists(p):
        return open(p, encoding='utf-8').read().strip()
    return ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--start', default=(dt.date.today() - dt.timedelta(days=14)).isoformat())
    ap.add_argument('--end', default=dt.date.today().isoformat())
    ap.add_argument('--json', default='_stage1_ieee.json')
    ap.add_argument('--no-abstract', action='store_true', help='跳过 OpenAlex 摘要抓取（更快）')
    args = ap.parse_args()

    key = read_key()
    print(f'[stage1-ieee] window {args.start} ~ {args.end}  (OpenAlex key: {"yes" if key else "no"})')
    print('-' * 78)

    report = []
    for name, issns in IEEE_JOURNALS.items():
        raw = []
        for issn in issns:
            try:
                raw.extend(crossref_window(issn, args.start, args.end))
            except Exception as e:                               # noqa: BLE001
                print(f'  ! {name} {issn}: {e}')
        # 去重（同一 DOI 可能两个 ISSN 都返回）
        seen, items = set(), []
        for it in raw:
            d = (it.get('DOI') or '').lower()
            if not d or d in seen:
                continue
            seen.add(d)
            items.append(it)

        hits = []
        for it in items:
            title = (it.get('title') or [''])[0]
            title = re.sub(r'<[^>]+>', ' ', title)
            title = re.sub(r'\s+', ' ', title).strip()
            if not OCEAN_KW.search(title):
                continue
            d = it['DOI']
            created = '-'.join(str(x) for x in it['created']['date-parts'][0][:3])
            ab, _ = ('', None) if args.no_abstract else openalex_abstract(d, key)
            hits.append({'doi': d, 'title': title, 'created': created,
                         'journal': (it.get('container-title') or [''])[0],
                         'abstract_len': len(ab), 'abstract': ab})

        print(f'{name:7s} total={len(items):4d}  ocean_hits={len(hits)}')
        for h in hits:
            flag = 'ABS' if h['abstract_len'] else 'no-ab'
            print(f'   [{flag:5s}] {h["created"]}  {h["title"][:78]}')
            print(f'            https://doi.org/{h["doi"]}')
        report.append({'journal': name, 'issns': issns,
                       'total': len(items), 'hits': hits})

    tot = sum(len(r['hits']) for r in report)
    print('-' * 78)
    print(f'SUM ocean_hits={tot}  → {args.json}')
    json.dump(report, open(args.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if tot < 3:
        print('WARN: 命中 < 3 条，建议放宽 OCEAN_KW 或检查窗口/ISSN')
    return 0


if __name__ == '__main__':
    sys.exit(main())
