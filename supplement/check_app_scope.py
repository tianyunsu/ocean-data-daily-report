import requests, json, sys
sys.stdout.reconfigure(encoding='utf-8')

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"

# 获取 tenant_access_token（应用身份）
r = requests.post(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
)
print("tenant token resp:", r.status_code, r.text[:200])
token = r.json()["tenant_access_token"]

headers = {"Authorization": f"Bearer {token}"}

# 测试：直接用小文件尝试一步上传（upload_all），看报什么错
# drive:file 权限对应的是 upload_all 接口
test_content = b"test"
r2 = requests.post(
    "https://open.feishu.cn/open-apis/drive/v1/files/upload_all",
    headers={"Authorization": f"Bearer {token}"},
    data={
        "file_name": "test.txt",
        "parent_type": "explorer",
        "parent_node": "nodcniyHJwzrxNg5JOFA2cTatDg",
        "size": len(test_content),
    },
    files={"file": ("test.txt", test_content, "text/plain")},
    timeout=15,
)
print("upload_all 测试:", r2.status_code, r2.text[:600])
