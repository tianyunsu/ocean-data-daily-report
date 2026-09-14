# -*- coding: utf-8 -*-
"""patch_index_archive_0914.py — 同步更新首页卡片与归档页中 09-14 期的摘要描述
   （原描述包含已被移除的 3 条重复条目，须一并替换）"""
import io, sys

# ---------- index.html ----------
NEW_EXCERPT = ('<p class="post-excerpt">9 个研究方向 · 16 条精选资讯。扩散模型从稀疏站点重建公里尺度风场（KiloDA）；'
               'KDD 2026 清华 Ocean-E2E 端到端神经同化极端海洋热浪预报；Sentinel-6 双星同轨串联飞行完成星间交叉校验（NASA 09-09）；'
               'CFOSAT SWIM 海浪谱三代产品与 ERA5 海况分级质量评估（《海洋学报》09-04）；'
               'EMODnet 全量数据集实现与 EDITO 数据湖自动化同步；WakeAtlas 免费 CesiumJS 三维海洋探索平台上线；'
               'NOAA NCEI 深海样品管理系统 SOUP 上线（09-10）。</p>')

p = 'index.html'
s = io.open(p, encoding='utf-8').read()
i = s.find('<p class="post-excerpt">9 个研究方向 · 16 条精选资讯。扩散模型')
if i < 0:
    print('[FAIL] index.html 未找到 09-14 摘要'); sys.exit(1)
j = s.find('</p>', i) + len('</p>')
s = s[:i] + NEW_EXCERPT + s[j:]
io.open(p, 'w', encoding='utf-8').write(s)
print('[OK] index.html 09-14 卡片摘要已更新 (%d -> %d 字符)' % (j - i, len(NEW_EXCERPT)))

# ---------- archive.html ----------
NEW_LI = ('<li><a href="posts/2026-09-14.html"><strong>2026-09-14</strong></a>（周日） · 9个方向 · 16条动态 · 重点：'
          'KiloDA 扩散模型从稀疏站点重建公里尺度风场（arXiv 09-10）；Ocean-E2E 清华 KDD 2026 端到端神经同化极端海洋热浪预报（KDD 08-09）；'
          '高频雷达波浪高度估计窗口包络统计方法（arXiv 09-11）；ML 天气预报模型挪威北部站点评估（arXiv 09-11）；'
          '扩散先验引导稀疏观测高分辨率温度降尺度（arXiv 09-09）；EMODnet 全量数据集实现与 EDITO 数据湖自动化同步（09-01）；'
          'WakeAtlas 免费 CesiumJS 三维海洋探索平台上线（09-12）；Sentinel-6 双星同轨串联飞行完成星间交叉校验（NASA 09-09）；'
          'CFOSAT SWIM 海浪谱三代版本质量评估（《海洋学报》09-04）；MG-GCNN 多粒度图神经网络三维海洋环境场重建（RS 09-04）；'
          '联合国海洋十年发布社会经济数据共享指南（DCO-ODS 09-10）；EMODnet Biology 北海底拖网捕捞底栖影响数据产品（09-11）；'
          '东海秋季共享航次向阳红18启航（09-10）；西太平洋发现大型高温热液区、向阳红10号联合科考（09-11）；'
          '雪龙2号为法国塔拉极地站破冰引航110海里（09-11）；NOAA NCEI 上线深海样品数据管理系统 SOUP（09-10）等。</li>\n')

p = 'archive.html'
s = io.open(p, encoding='utf-8').read()
start = s.find('<li><a href="posts/2026-09-14.html">')
if start < 0:
    print('[FAIL] archive.html 未找到 09-14 条目'); sys.exit(1)
end = s.find('<li>', start + 10)
if end < 0:
    print('[FAIL] archive.html 未找到 09-14 条目结束位置'); sys.exit(1)
s = s[:start] + NEW_LI + s[end:]
io.open(p, 'w', encoding='utf-8').write(s)
print('[OK] archive.html 09-14 归档项已更新 (%d -> %d 字符)' % (end - start, len(NEW_LI)))
