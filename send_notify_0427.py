"""Send Feishu bot notification for 2026-04-27."""
import os
import json
import urllib.request

# Read webhook URL
webhook_path = 'feishu_webhook_url.txt'
if os.path.exists(webhook_path):
    with open(webhook_path, 'r', encoding='utf-8') as f:
        webhook_url = f.read().strip()
else:
    webhook_url = os.environ.get('FEISHU_WEBHOOK_URL', '')

if not webhook_url:
    print('No webhook URL found')
    exit(1)

msg = {
    "msg_type": "text",
    "content": {
        "text": "【海洋AI研究日报】2026年4月27日（第27期）已发布！\n\n📊 本期共9个方向、43条研究动态\n\n🔬 近7天新增亮点：\n• Frontiers《海洋AI赋能可持续海洋》研究专题（04-24）\n• DITTO全球DTO治理框架正式启动（04-24）\n• DITTO Summit 2026日本横滨召开（04-24）\n• Argo DMQC v2.0发布（04-24）\n• Zenodo BGC-Argo海色填补数据集（04-25）\n• PANGAEA IODP 2025航次数据上线（04-25）\n• Argo数据访问门户Erddap升级（04-23）\n\n🔗 GitHub Pages: https://tianyunsu.github.io/ocean-data-daily-report/posts/2026-04-27.html\n📄 飞书文档: https://tianyunsu.feishu.cn/docx/ZJL1dHoxjovVpmxqzQCcJjXCnae"
    }
}

data = json.dumps(msg).encode('utf-8')
req = urllib.request.Request(webhook_url, data=data, headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as r:
        resp = json.loads(r.read())
    print(f'Bot notification: {resp}')
except Exception as e:
    print(f'Bot notification failed: {e}')
