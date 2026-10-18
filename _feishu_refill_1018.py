#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-10-18 补跑：feishu_write_doc.py 端点修复后，把今日日报内容写入已建好的空文档。
原脚本 main() 每次新建文档；此处复用 10-18 已创建的 doc_id，避免产生废文档。
"""
import requests
import feishu_write_doc as F

DOC_ID = "P8yydOYpEoO14jxfTSYc5GuynHb"


def get_token():
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": F.APP_ID, "app_secret": F.APP_SECRET}, timeout=20,
    )
    r.raise_for_status()
    return r.json()["tenant_access_token"]


def main():
    tok = get_token()
    blocks = F.build_blocks()
    print(f"待写入块数: {len(blocks)}")
    F.write_blocks_to_doc(tok, DOC_ID, blocks)
    print(f"Document URL: https://{F.TENANT_DOMAIN}/docx/{DOC_ID}")


if __name__ == "__main__":
    main()
