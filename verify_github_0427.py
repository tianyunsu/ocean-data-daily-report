import urllib.request, json

url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/commits/main'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
print(f"Latest commit: {data['sha']}")
print(f"Message: {data['commit']['message'][:80]}")

# Check posts/2026-04-27.html exists
url2 = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts/2026-04-27.html'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Python'})
try:
    with urllib.request.urlopen(req2) as r2:
        d2 = json.loads(r2.read())
    import base64
    content = base64.b64decode(d2['content']).decode('utf-8')
    # Count items
    import re
    dates = re.findall(r"'date':\s*'([0-9]{4}-[0-9]{2}-[0-9]{2})'", content)
    from datetime import datetime
    cutoff = datetime(2026, 3, 28)
    today = datetime(2026, 4, 27)
    violations = [d for d in dates if datetime.strptime(d, '%Y-%m-%d') < cutoff]
    print(f"\nGitHub posts/2026-04-27.html:")
    print(f"  Total items: {len(dates)}")
    print(f"  Violations (>30 days): {len(violations)}")
    if violations:
        for v in violations:
            print(f"  VIOLATION: {v}")
    else:
        print("  ALL OK - 0 violations")
except Exception as e:
    print(f"Error: {e}")
