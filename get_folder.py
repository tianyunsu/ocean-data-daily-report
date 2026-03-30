import requests, json, sys
sys.stdout.reconfigure(encoding='utf-8')

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"

r = requests.post(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
)
token = r.json()["tenant_access_token"]
print("token OK:", token[:16])
headers = {"Authorization": f"Bearer {token}"}

# 尝试列出我的云盘文件 (不带参数，默认根目录)
r2 = requests.get(
    "https://open.feishu.cn/open-apis/drive/v1/files",
    headers=headers, timeout=15
)
print("列文件状态:", r2.status_code, r2.text[:800])

# 尝试上传到 my_space (个人空间根目录)
# 预上传测试，使用 parent_type=explorer 不带 parent_node
r3 = requests.post(
    "https://open.feishu.cn/open-apis/drive/v1/files/upload_prepare",
    json={"file_name": "test.txt", "parent_type": "explorer", "parent_node": "", "size": 4},
    headers=headers, timeout=15
)
print("预上传(空parent_node):", r3.status_code, r3.text[:500])

# 试 parent_type=my_space
r4 = requests.post(
    "https://open.feishu.cn/open-apis/drive/v1/files/upload_prepare",
    json={"file_name": "test.txt", "parent_type": "my_space", "size": 4},
    headers=headers, timeout=15
)
print("预上传(my_space):", r4.status_code, r4.text[:500])
