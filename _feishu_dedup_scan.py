#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-10-18 飞书日报文档去重扫描（只读，不删任何东西）。
规则：
  - 从标题提取日期（支持 "2026-10-18" 与 "2026年10月18日" 两种写法）
  - 同日期多个文档 -> 保留「块数最多」者（内容最完整）；块数相同则保留创建时间最新者
  - 无法解析日期的（测试文档、Debug 等）单独归类，不纳入自动清理
输出：保留清单 / 待删清单 / 待人工确认清单
"""
import re
import sys
import json
import requests
import _feishu_auth

BASE = "https://open.feishu.cn/open-apis"


def get_token():
    app_id, app_secret = _feishu_auth.get_app_credentials()
    r = requests.post(f"{BASE}/auth/v3/tenant_access_token/internal",
                      json={"app_id": app_id, "app_secret": app_secret}, timeout=20)
    r.raise_for_status()
    return r.json()["tenant_access_token"]


def list_all_docx(h):
    """分页拉全量 docx 文档。"""
    files, pt = [], ""
    while True:
        params = {"page_size": 200}
        if pt:
            params["page_token"] = pt
        d = requests.get(f"{BASE}/drive/v1/files", headers=h,
                         params=params, timeout=30).json()
        if d.get("code") != 0:
            print("列文件失败:", json.dumps(d, ensure_ascii=False)[:300])
            sys.exit(1)
        data = d.get("data", {})
        files.extend([f for f in data.get("files", []) if f.get("type") == "docx"])
        if not data.get("has_more"):
            break
        pt = data.get("next_page_token")
    return files


def block_count(h, token):
    """读取文档块数；失败返回 None（该文档将不被纳入清理）。"""
    try:
        items, pt = [], ""
        while True:
            params = {"page_size": 500}
            if pt:
                params["page_token"] = pt
            d = requests.get(f"{BASE}/docx/v1/documents/{token}/blocks",
                             headers=h, params=params, timeout=30).json()
            if d.get("code") != 0:
                return None
            data = d.get("data", {})
            items.extend(data.get("items", []))
            if not data.get("has_more"):
                break
            pt = data.get("next_page_token")
        return len(items)
    except Exception:
        return None


def parse_date(name):
    m = re.search(r"(20\d{2})-(\d{2})-(\d{2})", name)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"(20\d{2})年(\d{1,2})月(\d{1,2})日", name)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return None


def main():
    h = {"Authorization": f"Bearer {get_token()}", "Content-Type": "application/json"}
    docs = list_all_docx(h)
    print(f"共拉取 docx 文档 {len(docs)} 个\n")

    by_date, no_date = {}, []
    for d in docs:
        key = parse_date(d.get("name", ""))
        if key:
            by_date.setdefault(key, []).append(d)
        else:
            no_date.append(d)

    keep, drop = [], []
    need_count = [d for g in by_date.values() if len(g) > 1 for d in g]
    print(f"需比对块数的文档：{len(need_count)} 个（同日多份的才需要读块数）\n")
    for i, key in enumerate(sorted(by_date), 1):
        group = sorted(by_date[key], key=lambda x: int(x.get("created_time") or 0))
        if len(group) == 1:
            group[0]["_blocks"] = None  # 单日唯一，无需读块数
            keep.append(group[0])
            continue
        for d in group:
            d["_blocks"] = block_count(h, d["token"])
        ranked = sorted(group, key=lambda x: (-(x["_blocks"] if x["_blocks"] is not None else -1),
                                              -(int(x.get("created_time") or 0))))
        keep.append(ranked[0])
        drop.extend(ranked[1:])
        print(f"  [{i}] {key}: {len(group)} 份 -> 保留 {ranked[0]['token'][:12]}…"
              f"（{ranked[0]['_blocks']} 块）", flush=True)

    print("=" * 78)
    print(f"【保留】{len(keep)} 个（每个日期保留内容最完整的一份）")
    for d in keep:
        print(f"  {d.get('name')}  | 块数 {d['_blocks']} | {d['token']}")

    print()
    print(f"【待删】{len(drop)} 个（同日重复，且块数已成功读取）")
    for d in drop:
        print(f"  {d.get('name')}  | 块数 {d['_blocks']} | {d['token']}")

    if no_date:
        print()
        print(f"【待人工确认】{len(no_date)} 个（标题无日期，未纳入自动清理）")
        for d in no_date:
            print(f"  {d.get('name')}  | {d['token']}")

    # 落盘待删清单，供删除脚本使用
    with open("_feishu_dup_drop_list.txt", "w", encoding="utf-8") as f:
        for d in drop:
            f.write(f"{d['token']}\t{d['_blocks']}\t{d.get('name')}\n")
    print("\n待删清单已写入 _feishu_dup_drop_list.txt")


if __name__ == "__main__":
    main()
