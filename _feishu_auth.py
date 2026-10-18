#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书应用凭证统一加载入口（2026-10-18 苏老师决定整改硬编码明文）。

读取顺序（与 OpenAlex key 一致）：
    1. 环境变量  FEISHU_APP_ID / FEISHU_APP_SECRET
    2. 本地文件  _feishu_credentials.env（已加入 .gitignore，绝不入库）

安全铁律：本仓库是**公开仓库**，任何脚本、文档、记忆文件都不得再出现
APP_ID / APP_SECRET 明文。新增调用方一律 `import _feishu_auth` 后取凭证。
"""
import os

ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_feishu_credentials.env")


def _load_env_file():
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


def get_app_credentials():
    """返回 (app_id, app_secret)。环境变量优先，其次本地 env 文件。"""
    file_values = _load_env_file()
    app_id = os.environ.get("FEISHU_APP_ID") or file_values.get("FEISHU_APP_ID", "")
    app_secret = os.environ.get("FEISHU_APP_SECRET") or file_values.get("FEISHU_APP_SECRET", "")
    return app_id, app_secret


def credentials_ok():
    app_id, app_secret = get_app_credentials()
    return bool(app_id and app_secret)


if __name__ == "__main__":
    if credentials_ok():
        app_id, _ = get_app_credentials()
        print(f"OK 凭证可用（app_id={app_id[:10]}...）")
    else:
        print("MISSING 未找到凭证：请设置环境变量，或创建本地 _feishu_credentials.env")
