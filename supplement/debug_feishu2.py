#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
精准调试：逐步排查写入失败原因
"""
import requests, json, time

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"

def get_token():
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15
    )
    return r.json()["tenant_access_token"]

token = get_token()
h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
print(f"token ok: {token[:12]}...")

# 用上一次成功创建的文档
doc_id = "CgszdluWUoZILDxmE0KcpVVSnZj"
print(f"doc_id: {doc_id}")

# 先查文档所有块
all_r = requests.get(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks",
    headers=h, timeout=15
)
all_data = all_r.json()
print(f"\n当前文档所有块:")
print(json.dumps(all_data, ensure_ascii=False, indent=2)[:1500])

# 用 tr() 格式测试写入单块（加上 index=0 对比）
def tr(content, bold=False):
    return {"text_run": {"content": content, "text_element_style": {
        "bold": bold, "inline_code": False, "italic": False,
        "strikethrough": False, "underline": False
    }}}

test_block = {"block_type": 2, "text": {"elements": [tr("测试段落 test")], "style": {}}}

print(f"\n测试1: index=0 对根块写入段落")
r1 = requests.post(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
    headers=h, json={"children": [test_block], "index": 0}, timeout=15
)
print(json.dumps(r1.json(), ensure_ascii=False, indent=2)[:600])

time.sleep(0.5)

print(f"\n测试2: 不传 index 对根块写入段落")
r2 = requests.post(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
    headers=h, json={"children": [test_block]}, timeout=15
)
print(json.dumps(r2.json(), ensure_ascii=False, indent=2)[:600])

time.sleep(0.5)

print(f"\n测试3: 写入 heading1 块")
h1_block = {"block_type": 3, "text": {"elements": [tr("标题测试")], "style": {}}}
r3 = requests.post(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
    headers=h, json={"children": [h1_block], "index": 0}, timeout=15
)
print(json.dumps(r3.json(), ensure_ascii=False, indent=2)[:600])

time.sleep(0.5)

print(f"\n测试4: 写入 divider(22) 块")
div_block = {"block_type": 22}
r4 = requests.post(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
    headers=h, json={"children": [div_block], "index": 0}, timeout=15
)
print(json.dumps(r4.json(), ensure_ascii=False, indent=2)[:600])

time.sleep(0.5)

print(f"\n测试5: 中文内容 heading + paragraph + divider 一次性写入")
multi = [
    {"block_type": 3, "text": {"elements": [tr("一、海洋人工智能")], "style": {}}},
    {"block_type": 2, "text": {"elements": [tr("Ocean AI / Marine Artificial Intelligence")], "style": {}}},
    {"block_type": 22},
]
r5 = requests.post(
    f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children",
    headers=h, json={"children": multi, "index": 0}, timeout=15
)
print(json.dumps(r5.json(), ensure_ascii=False, indent=2)[:800])
