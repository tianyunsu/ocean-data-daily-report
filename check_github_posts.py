import urllib.request, json

# Check main branch recent posts
url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
with urllib.request.urlopen(req) as r:
    files = json.loads(r.read())

recent_posts = [f for f in files if f['name'].startswith('2026-04-') and f['name'] >= '2026-04-20']
recent_posts.sort(key=lambda x: x['name'])
print('=== Main branch recent posts ===')
for p in recent_posts:
    print(f'  {p["name"]}')

# Check supplement branch
url2 = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/git/trees/supp?recursive=1'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Python'})
try:
    with urllib.request.urlopen(req2) as r:
        tree = json.loads(r.read())
    supp_files = [f['path'] for f in tree.get('tree', []) if f['path'].startswith('posts/') and f['path'] >= 'posts/2026-04-20']
    supp_files.sort()
    print()
    print('=== Supplement branch recent posts ===')
    for f in supp_files:
        print(f'  {f}')
except Exception as e:
    print(f'Error checking supplement: {e}')
