#!/usr/bin/env python3
import requests, json

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
DOC_ID = "EAalduuvFoNvv3xiaaQc5p5JnLc"

r = requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15)
token = r.json()["tenant_access_token"]
headers = {"Authorization": f"Bearer {token}"}

# 1. 获取企业信息（含企业域名）
tenant_r = requests.get(
    "https://open.feishu.cn/open-apis/tenant/v2/tenant/query",
    headers=headers, timeout=15
)
print("[1] 企业信息:")
d = tenant_r.json()
print(json.dumps(d, ensure_ascii=False, indent=2)[:1200])

# 2. 从企业信息中找租户域名
tenant_key = d.get("data", {}).get("tenant", {}).get("tenant_key", "")
domain = d.get("data", {}).get("tenant", {}).get("domain", "")
print(f"\ntenant_key: {tenant_key}")
print(f"domain: {domain}")

# 3. 尝试几种可能的URL格式
possible_urls = [
    f"https://feishu.cn/docx/{DOC_ID}",
    f"https://{domain}.feishu.cn/docx/{DOC_ID}" if domain else None,
    f"https://open.feishu.cn/docx/{DOC_ID}",
]
print("\n[3] 测试不同URL格式:")
for url in possible_urls:
    if url:
        try:
            test_r = requests.get(url, timeout=8, allow_redirects=True)
            print(f"  {test_r.status_code}: {url} -> {test_r.url}")
        except Exception as e:
            print(f"  ERROR: {url} -> {e}")

# 4. 尝试获取文档的web_url
meta_r = requests.get(
    f"https://open.feishu.cn/open-apis/drive/v1/files/{DOC_ID}?type=docx",
    headers=headers, timeout=15
)
print("\n[4] Drive文件信息:")
print(json.dumps(meta_r.json(), ensure_ascii=False, indent=2)[:800])
