import urllib.request, json, re
from datetime import datetime

url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts/2026-04-27.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
import base64
content = base64.b64decode(data['content']).decode('utf-8')

# Extract dates from the HTML content
# The HTML has dates in the format YYYY-MM-DD in text
dates = re.findall(r'(\d{4}-\d{2}-\d{2})', content)
unique_dates = sorted(set(dates))

cutoff = datetime(2026, 3, 28)
today = datetime(2026, 4, 27)

print(f"Unique dates in HTML: {len(unique_dates)}")
for d in unique_dates:
    dt = datetime.strptime(d, '%Y-%m-%d')
    days = (today - dt).days
    if dt < cutoff:
        mark = 'XXX OVER30'
    elif days <= 7:
        mark = 'OK recent'
    else:
        mark = 'OK 7-30d'
    print(f"  {mark} {d} ({days}d)")

violations = [d for d in unique_dates if datetime.strptime(d, '%Y-%m-%d') < cutoff]
print(f"\nTotal unique dates: {len(unique_dates)}")
print(f"Violations (>30 days): {len(violations)}")
if violations:
    print(f"VIOLATIONS: {violations}")
else:
    print("ALL OK - 0 violations")
