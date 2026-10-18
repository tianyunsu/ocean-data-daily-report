#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书 App Secret 轮换助手（2026-10-18）。

为什么需要它：旧 Secret 已留在公开仓库的 git 历史里，必须重置才能作废。
本脚本把「重置后」的本地收尾工作压缩成一步：粘贴新 Secret -> 自动写入
_feishu_credentials.env 并立即验证能否换到 token。

用法：
    py -3 _rotate_feishu_secret.py

前置（必须你本人在浏览器完成，脚本无法代做）：
    打开 https://open.feishu.cn/app  ->  扫码登录
    ->  「我的应用」里选中本日报用的应用（App ID cli_a93d48... 开头）
    ->  左侧菜单「凭证与基础信息」
    ->  找到 App Secret 一栏，点右侧「重置」按钮
    ->  复制弹出的新 Secret（只显示这一次）
"""
import os
import sys
import getpass
import requests
import _feishu_auth

ENV_FILE = _feishu_auth.ENV_FILE
AUTH_URL = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"


def test_secret(app_id, app_secret):
    """用给定 secret 换 token，返回 (是否可用, 说明)。"""
    try:
        r = requests.post(AUTH_URL, json={"app_id": app_id, "app_secret": app_secret},
                          timeout=20)
        body = r.json()
    except Exception as e:
        return False, f"网络异常：{e}"
    if body.get("code") == 0 and body.get("tenant_access_token"):
        return True, "可用"
    return False, f"code={body.get('code')} msg={body.get('msg')}"


def read_env_file():
    values = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                values[k.strip()] = v.strip().strip('"').strip("'")
    return values


def write_env_file(app_id, app_secret):
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write("# 飞书自建应用凭证（本地专用，已 gitignore，严禁入库——公开仓库）\n")
        f.write("# 2026-10-18 苏老师决定：明文从所有被 git 跟踪的文件中移除，改由本文件统一供给。\n")
        f.write("# 轮换 App Secret 后只需改下面第二行，然后跑 py -3 _feishu_auth.py 验证。\n")
        f.write(f"FEISHU_APP_ID={app_id}\n")
        f.write(f"FEISHU_APP_SECRET={app_secret}\n")
    # 收紧权限（Windows 上仅提示，不强制）
    try:
        os.chmod(ENV_FILE, 0o600)
    except Exception:
        pass


def main():
    cur = read_env_file()
    app_id = cur.get("FEISHU_APP_ID", "")
    if not app_id:
        print("错误：本地凭证文件里没有 App ID，请先手动补上 FEISHU_APP_ID=...")
        sys.exit(1)

    old_secret = cur.get("FEISHU_APP_SECRET", "")
    if old_secret:
        ok, why = test_secret(app_id, old_secret)
        print(f"[1/3] 旧 Secret 状态：{'仍可用（说明还没重置，或已重置但旧值仍生效）' if ok else '已失效（符合预期）'} — {why}")
        if ok:
            print("      提示：如果你还没去网页点重置，现在去点；点完再回来运行本脚本。")
    else:
        print("[1/3] 本地未找到旧 Secret，跳过旧值检测")

    print()
    print("[2/3] 请粘贴网页上刚复制的新 App Secret，然后回车：")
    print("      （输入内容不会显示在屏幕上，属正常；粘贴后直接回车即可）")
    try:
        if sys.stdin is not None and not sys.stdin.isatty():
            # 管道/重定向模式（如 echo <secret> | py -3 _rotate_feishu_secret.py）：
            # getpass 在非 tty 下会尝试控制终端回显，某些沙箱环境直接挂住，
            # 故此处降级为普通 stdin 读取。注意：此模式下 secret 会经管道传入。
            new_secret = sys.stdin.readline().strip()
        else:
            new_secret = getpass.getpass("      新 Secret > ").strip()
    except Exception:
        new_secret = input("      新 Secret > ").strip()

    if not new_secret:
        print("错误：未输入任何内容，已中止（本地文件未被修改）。")
        sys.exit(1)

    # 常见粘贴事故：带了引号或首尾空白
    new_secret = new_secret.strip().strip('"').strip("'").strip()
    if len(new_secret) < 16:
        print(f"警告：长度仅 {len(new_secret)}，疑似粘贴不完整（正常约 32 位）。")
        if input("仍要继续写入吗？[y/N] ").strip().lower() != "y":
            print("已中止，本地文件未被修改。")
            sys.exit(1)

    print()
    print("[3/3] 验证新 Secret ...")
    ok, why = test_secret(app_id, new_secret)
    if not ok:
        print(f"      新 Secret 验证失败：{why}")
        print("      本地文件未被修改。请检查是否复制完整（可重新去网页复制后再跑本脚本）。")
        sys.exit(1)

    write_env_file(app_id, new_secret)
    print(f"      新 Secret 可用，已写入 {os.path.basename(ENV_FILE)}")
    print()
    print("完成。建议再跑一次 py -3 _feishu_auth.py 确认读取正常。")
    print("提醒：旧 Secret 已随本次重置作废；git 历史里的旧值无法追回，只能靠这次重置失效。")


if __name__ == "__main__":
    main()
