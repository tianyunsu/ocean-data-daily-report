with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_card = '''    <div class="post-card">
      <div class="post-date">2026-04-27 · 周一</div>
      <h2><a href="posts/2026-04-27.html">2026年04月27日 海洋AI技术日报</a></h2>
      <div class="post-excerpt">本期涵盖9个方向，共43条最新动态。近7天新增亮点包括：Frontiers《海洋AI赋能可持续海洋》研究专题（04-24）、DITTO全球DTO治理框架正式启动（04-24）、DITTO Summit 2026日本横滨召开（04-24）、Argo DMQC v2.0发布（04-24）、Zenodo BGC-Argo海色填补数据集（04-25）、PANGAEA IODP 2025航次数据上线（04-25）、Argo数据访问门户Erddap升级（04-23）、IODE Ocean InfoHub启动（04-23）等重要进展。</div>
      <a href="posts/2026-04-27.html" class="read-more">阅读全文 →</a>
    </div>

'''

# Insert after <main class="container"> and before the first post-card
marker = '    <div class="post-card">\n      <div class="post-date">2026-04-24'
content = content.replace(marker, new_card + marker)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html updated!')

# Also update archive.html
with open('archive.html', 'r', encoding='utf-8') as f:
    arch = f.read()

# Find the last occurrence of a post entry and add before it
arch_new = '''    <div class="archive-entry">
      <span class="archive-date">2026-04-27</span>
      <a href="posts/2026-04-27.html">2026年04月27日 海洋AI技术日报（9方向43条）</a>
    </div>
'''
# Insert after <main> and before first archive-entry
arch_marker = '    <div class="archive-entry">'
arch = arch.replace(arch_marker, arch_new + arch_marker, 1)

with open('archive.html', 'w', encoding='utf-8') as f:
    f.write(arch)

print('archive.html updated!')
