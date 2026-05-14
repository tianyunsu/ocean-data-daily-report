import urllib.request, json, re

url = 'https://api.github.com/repos/tianyunsu/ocean-data-daily-report/contents/posts/2026-04-27.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
import base64
content = base64.b64decode(data['content']).decode('utf-8')

# Check the HTML file
print(f"HTML file size: {len(content)} chars")

# Look for date patterns
# Try different patterns
patterns = [
    r"'date':\s*'([^']+)'",
    r'data-date="([^"]+)"',
    r'(\d{4}-\d{2}-\d{2})',
]
for p in patterns:
    matches = re.findall(p, content)
    print(f"Pattern {p}: {len(matches)} matches")
    if matches:
        print(f"  First few: {matches[:5]}")

# Check if the file is actually the report
if '海洋AI' in content:
    print("File contains '海洋AI' - OK")
    # Count section count
    section_count = content.count('<h2>')
    print(f"Section headers: {section_count}")
    item_count = content.count('<li>')
    print(f"List items: {item_count}")
else:
    print("File does NOT contain '海洋AI'")
    print("First 500 chars:")
    print(content[:500])
