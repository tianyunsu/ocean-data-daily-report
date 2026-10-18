#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-10-18 按 _feishu_dup_drop_list.txt 删除飞书重复日报文档。
安全设计：
  1. 逐行读清单，删除前再次校验该 token 不在保留清单中（双保险）
  2. 每批 10 个，批间 sleep 0.4s 避开飞书 3 次/秒限流
  3. 每个删除都校验响应 code == 0，失败立即记录并继续（便于事后补救）
  4. 删除走 drive/v1/files（进回收站，可在飞书回收站恢复）
"""
import sys
import time
import requests
import _feishu_auth

BASE = "https://open.feishu.cn/open-apis"
LIST_FILE = "_feishu_dup_drop_list.txt"
KEEP_FILE = "_feishu_dup_keep_list.txt"
BATCH = 10
SLEEP = 0.4


def get_token():
    app_id, app_secret = _feishu_auth.get_app_credentials()
    r = requests.post(f"{BASE}/auth/v3/tenant_access_token/internal",
                      json={"app_id": app_id, "app_secret": app_secret}, timeout=20)
    r.raise_for_status()
    return r.json()["tenant_access_token"]


def main():
    keep = set()
    try:
        with open(KEEP_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    keep.add(line.split("\t")[0].strip())
    except FileNotFoundError:
        print(f"警告：{KEEP_FILE} 不存在，跳过保留清单校验")

    rows = []
    with open(LIST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            rows.append((parts[0], parts[1] if len(parts) > 1 else "?",
                         parts[2] if len(parts) > 2 else ""))

    print(f"待删 {len(rows)} 个，保留清单 {len(keep)} 个")

    h = {"Authorization": f"Bearer {get_token()}", "Content-Type": "application/json"}
    ok, fail, skipped = [], [], []

    for i, (token, blocks, name) in enumerate(rows):
        if token in keep:
            skipped.append((token, name, "在保留清单中，跳过"))
            continue
        try:
            r = requests.delete(f"{BASE}/drive/v1/files/{token}", headers=h,
                                params={"type": "docx"}, timeout=30)
            body = r.json()
            if r.status_code == 200 and body.get("code") == 0:
                ok.append((token, name))
            else:
                fail.append((token, name, f"HTTP {r.status_code} code={body.get('code')} {body.get('msg')}"))
        except Exception as e:
            fail.append((token, name, str(e)[:80]))

        done = i + 1
        if done % BATCH == 0 or done == len(rows):
            print(f"  进度 {done}/{len(rows)}：成功 {len(ok)} 失败 {len(fail)} 跳过 {len(skipped)}", flush=True)
        time.sleep(SLEEP)

    print()
    print(f"完成：成功 {len(ok)} / 失败 {len(fail)} / 跳过 {len(skipped)}")
    if fail:
        print("失败明细（需人工补救）：")
        for t, n, why in fail:
            print(f"  {t} | {n} | {why}")
    if skipped:
        print("跳过明细：")
        for t, n, why in skipped:
            print(f"  {t} | {n} | {why}")

    with open("_feishu_dup_delete_result.txt", "w", encoding="utf-8") as f:
        f.write(f"成功 {len(ok)} / 失败 {len(fail)} / 跳过 {len(skipped)}\n\n")
        f.write("=== 已删除 ===\n")
        for t, n in ok:
            f.write(f"{t}\t{n}\n")
        if fail:
            f.write("\n=== 失败 ===\n")
            for t, n, why in fail:
                f.write(f"{t}\t{n}\t{why}\n")
    print("结果已写入 _feishu_dup_delete_result.txt")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
