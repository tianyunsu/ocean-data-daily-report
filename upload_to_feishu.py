import requests, json, sys
sys.stdout.reconfigure(encoding='utf-8')

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
TENANT_DOMAIN = "wcn5jx0ifkx3.feishu.cn"
PARENT_NODE = "nodcniyHJwzrxNg5JOFA2cTatDg"

import os, time

DOCX_FILE = r"C:\Users\Administrator\WorkBuddy\Claw\daily_reports\海洋AI简报_2026-03-16.docx"
HTML_FILE = r"C:\Users\Administrator\WorkBuddy\Claw\daily_reports\海洋AI简报_2026-03-16.html"

def get_token():
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
    )
    return r.json()["tenant_access_token"]

def upload_all(token, file_path, file_name, parent_node):
    """单次上传（文件较小时直接用 upload_all）"""
    file_size = os.path.getsize(file_path)
    with open(file_path, "rb") as f:
        file_data = f.read()

    r = requests.post(
        "https://open.feishu.cn/open-apis/drive/v1/files/upload_all",
        headers={"Authorization": f"Bearer {token}"},
        data={
            "file_name": file_name,
            "parent_type": "explorer",
            "parent_node": parent_node,
            "size": file_size,
        },
        files={"file": (file_name, file_data)},
        timeout=60,
    )
    data = r.json()
    print(f"upload_all [{file_name}]: {json.dumps(data, ensure_ascii=False)[:400]}")
    if data.get("code") == 0:
        return data["data"]["file_token"]
    return None

def import_docx(token, file_token, doc_name, parent_node):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "file_extension": "docx",
        "file_token": file_token,
        "type": "docx",
        "file_name": doc_name,
        "point": {"mount_type": 1, "mount_key": parent_node},
    }
    r = requests.post(
        "https://open.feishu.cn/open-apis/drive/v1/import_tasks",
        json=body, headers=headers, timeout=15
    )
    data = r.json()
    print(f"导入任务: {json.dumps(data, ensure_ascii=False)[:400]}")
    if data.get("code") == 0:
        return data["data"]["ticket"]
    return None

def poll_import(token, ticket):
    headers = {"Authorization": f"Bearer {token}"}
    for i in range(20):
        time.sleep(3)
        r = requests.get(
            f"https://open.feishu.cn/open-apis/drive/v1/import_tasks/{ticket}",
            headers=headers, timeout=15
        )
        data = r.json()
        if data.get("code") != 0:
            print(f"轮询失败: {data}")
            break
        result = data["data"]["result"]
        status = result.get("job_status")
        print(f"  [{i+1}] status={status}")
        if status == 0:
            return result.get("token")
        elif status not in (1, 2):
            print(f"  导入错误: {result}")
            break
    return None

def main():
    token = get_token()
    print(f"Token: {token[:16]}...\n")

    print("=== 上传 Word 文件到飞书云盘 ===")
    docx_ft = upload_all(token, DOCX_FILE, "海洋AI简报_2026-03-16.docx", PARENT_NODE)
    if docx_ft:
        print(f"Word 云盘链接: https://{TENANT_DOMAIN}/file/{docx_ft}\n")

    print("=== 上传 HTML 文件到飞书云盘 ===")
    html_ft = upload_all(token, HTML_FILE, "海洋AI简报_2026-03-16.html", PARENT_NODE)
    if html_ft:
        print(f"HTML 云盘链接: https://{TENANT_DOMAIN}/file/{html_ft}\n")

    print("=== 将 Word 导入为飞书原生文档 ===")
    if docx_ft:
        ticket = import_docx(token, docx_ft, "海洋AI简报_2026-03-16", PARENT_NODE)
        if ticket:
            print("等待导入完成...")
            doc_token = poll_import(token, ticket)
            if doc_token:
                url = f"https://{TENANT_DOMAIN}/docx/{doc_token}"
                print(f"\n[SUCCESS] 飞书原生文档: {url}")
                with open(r"C:\Users\Administrator\WorkBuddy\Claw\feishu_doc_url_import.txt", "w", encoding="utf-8") as f:
                    f.write(url + "\n")

if __name__ == "__main__":
    main()
