#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill 跨机器同步工具（海洋AI研究日报系统）

背景：
    记忆文件（.workbuddy/memory/、.workbuddy/automations/）已随仓库一起 git 跟踪，
    clone 即可获得。但 skill 存放在【用户级目录】 ~/.workbuddy/skills/，不在仓库内，
    换一台电脑就会丢失，导致手动执行日报时加载不到权威指令源。

    本脚本把仓库内的 .workbuddy/skills/ 与用户级 ~/.workbuddy/skills/ 做双向同步，
    保证任意机器上手动执行日报，用的都是同一套 skill 与经验。

用法：
    python sync_skills.py install    # 仓库 -> 用户目录（新电脑首次配置 / git pull 后执行）
    python sync_skills.py collect    # 用户目录 -> 仓库（本机改了 skill 后，回收进仓库再 push）
    python sync_skills.py status     # 只比对差异，不做任何修改

同步范围：
    ocean-daily-report      日报生成的唯一权威指令源（6 阶段流程）
    automation-consistency  手动/自动执行一致性方法论
"""

import filecmp
import hashlib
import shutil
import sys
from pathlib import Path

SKILLS = ["ocean-daily-report", "automation-consistency"]

REPO_ROOT = Path(__file__).resolve().parent
REPO_SKILLS = REPO_ROOT / ".workbuddy" / "skills"
USER_SKILLS = Path.home() / ".workbuddy" / "skills"


def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def list_files(root: Path):
    if not root.exists():
        return {}
    return {
        p.relative_to(root).as_posix(): p
        for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }


def compare(name: str):
    """返回 (仅仓库有, 仅用户有, 内容不同) 三个列表"""
    src = list_files(REPO_SKILLS / name)
    dst = list_files(USER_SKILLS / name)
    only_repo = sorted(set(src) - set(dst))
    only_user = sorted(set(dst) - set(src))
    diff = sorted(
        k for k in set(src) & set(dst) if file_hash(src[k]) != file_hash(dst[k])
    )
    return only_repo, only_user, diff


def show_status():
    print(f"仓库 skill 目录 : {REPO_SKILLS}")
    print(f"用户 skill 目录 : {USER_SKILLS}")
    print("-" * 64)
    clean = True
    for name in SKILLS:
        only_repo, only_user, diff = compare(name)
        if not (only_repo or only_user or diff):
            print(f"[一致] {name}")
            continue
        clean = False
        print(f"[差异] {name}")
        for f in only_repo:
            print(f"       仅仓库有   : {f}")
        for f in only_user:
            print(f"       仅用户目录 : {f}")
        for f in diff:
            print(f"       内容不同   : {f}")
    print("-" * 64)
    if clean:
        print("两侧完全一致，无需同步。")
    else:
        print("存在差异：install = 仓库覆盖用户目录，collect = 用户目录回收进仓库。")
    return clean


def sync(src_root: Path, dst_root: Path, label: str):
    if not src_root.exists():
        print(f"来源目录不存在，已跳过：{src_root}")
        return
    dst_root.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    for name in SKILLS:
        src = src_root / name
        if not src.exists():
            print(f"[跳过] {name}（来源缺失）")
            continue
        dst = dst_root / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        n = len(list_files(dst))
        total += n
        print(f"[同步] {name}  ({n} 个文件)")
    print("-" * 64)
    print(f"{label} 完成，共 {total} 个文件。")


def main():
    action = sys.argv[1] if len(sys.argv) > 1 else "status"

    if action == "status":
        show_status()
    elif action == "install":
        print("方向：仓库 -> 用户目录（让本机 skill 与仓库保持一致）")
        print("-" * 64)
        sync(REPO_SKILLS, USER_SKILLS, "安装")
        print("下一步：新会话中说「执行海洋AI研究日报」即可命中 skill。")
    elif action == "collect":
        print("方向：用户目录 -> 仓库（把本机 skill 改动回收，准备 push）")
        print("-" * 64)
        sync(USER_SKILLS, REPO_SKILLS, "回收")
        print("下一步：git add -A .workbuddy && git commit && git push origin main")
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
