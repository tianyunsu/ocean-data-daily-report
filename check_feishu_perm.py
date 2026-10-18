#!/usr/bin/env python3
import requests, json

# 2026-10-18 安全整改：凭证明文已从公开仓库移除，改由 _feishu_auth 统一供给
# （环境变量 FEISHU_APP_ID / FEISHU_APP_SECRET 优先，其次本地 _feishu_credentials.env）
import _feishu_auth
APP_ID, APP_SECRET = _feishu_auth.get_app_credentials()
DOC_ID = "EAalduuvFoNvv3xiaaQc5p5JnLc"

r = requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15)
token = r.json()["tenant_access_token"]
print(f"token OK: {token[:12]}...")

headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 1. 查询文档基本信息
meta_r = requests.get(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{DOC_ID}",
    headers=headers, timeout=15
)
print("\n[1] 文档元信息:")
print(json.dumps(meta_r.json(), ensure_ascii=False, indent=2)[:800])

# 2. 查询公开权限设置
link_r = requests.get(
    f"https://open.feishu.cn/open-apis/drive/v1/permissions/{DOC_ID}/public?type=docx",
    headers=headers, timeout=15
)
print("\n[2] 公开权限设置:")
print(json.dumps(link_r.json(), ensure_ascii=False, indent=2)[:800])

# 3. 尝试设置"组织内任何人可阅读"
patch_r = requests.patch(
    f"https://open.feishu.cn/open-apis/drive/v1/permissions/{DOC_ID}/public?type=docx",
    headers=headers,
    json={
        "link_share_entity": "tenant_readable",
        "external_access_entity": "open",
        "security_entity": "anyone_readable",
        "comment_entity": "anyone_can_view",
        "share_entity": "anyone",
        "manage_collaborator_entity": "collaborator_full_access"
    },
    timeout=15
)
print("\n[3] 设置公开访问结果:")
print(json.dumps(patch_r.json(), ensure_ascii=False, indent=2)[:800])

# 4. 获取文档访问URL（直接访问路径）
# 有些企业文档在 https://<企业>.feishu.cn 下，不在 docs.feishu.cn
print(f"\n[4] 尝试访问URL: https://docs.feishu.cn/docx/{DOC_ID}")
test_r = requests.get(f"https://docs.feishu.cn/docx/{DOC_ID}", timeout=10, allow_redirects=True)
print(f"    HTTP状态: {test_r.status_code}, 最终URL: {test_r.url}")
