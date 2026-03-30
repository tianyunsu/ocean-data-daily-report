#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试：用最简单的方式测试飞书文档块写入
"""
import requests, json

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"

# 获取token
token_resp = requests.post(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
)
token = token_resp.json()["tenant_access_token"]
print(f"token: {token[:12]}...")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 创建一个新文档
cr = requests.post(
    "https://open.feishu.cn/open-apis/docx/v1/documents",
    headers=headers, json={"title": "API Debug Test"}, timeout=15
)
doc_id = cr.json()["data"]["document"]["document_id"]
print(f"doc_id: {doc_id}")
print(f"doc url: https://docs.feishu.cn/docx/{doc_id}")

# 获取根块结构
rb = requests.get(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}",
    headers=headers, timeout=15
)
rb_data = rb.json()
print(f"\n根块响应:\n{json.dumps(rb_data, ensure_ascii=False, indent=2)}")

# 获取文档所有块
all_blocks = requests.get(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks",
    headers=headers, timeout=15
)
print(f"\n所有块:\n{json.dumps(all_blocks.json(), ensure_ascii=False, indent=2)}")

# 尝试最简单的 paragraph 块写入（index=0）
simple_block = {
    "block_type": 2,
    "text": {
        "elements": [
            {"tag": "text_run", "text_run": {"content": "Hello Ocean AI!", "text_element_style": {}}}
        ],
        "style": {}
    }
}
print(f"\n尝试写入简单段落块...")
wr = requests.post(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
    headers=headers,
    json={"children": [simple_block], "index": 0},
    timeout=15
)
print(f"写入响应:\n{json.dumps(wr.json(), ensure_ascii=False, indent=2)[:800]}")
