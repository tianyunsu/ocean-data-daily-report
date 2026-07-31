#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新用户接入脚本：初始化 GitHub Pages 仓库骨架
用法：python init_gh_repo.py /path/to/new/repo
"""
import os, sys, shutil

if len(sys.argv) < 2:
    print("用法: python init_gh_repo.py /path/to/new/repo")
    sys.exit(1)

repo_dir = os.path.abspath(sys.argv[1])

# 确定模板目录（脚本在 skills/ocean-daily-report/scripts/ 下运行）
script_dir = os.path.dirname(os.path.abspath(__file__))
skill_dir = os.path.dirname(script_dir)  # .../ocean-daily-report/
assets_dir = os.path.join(skill_dir, "assets")

# 创建目录结构
os.makedirs(os.path.join(repo_dir, "posts"), exist_ok=True)

# 复制模板文件
templates = {
    "template_index.html": "index.html",
    "template_archive.html": "archive.html",
    "template_style.css": "style.css",
}
for src, dst in templates.items():
    src_path = os.path.join(assets_dir, src)
    dst_path = os.path.join(repo_dir, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"  ✅ {dst}")
    else:
        print(f"  ⚠️  模板不存在: {src_path}")

# 创建 .gitignore
gitignore_path = os.path.join(repo_dir, ".gitignore")
with open(gitignore_path, "w") as f:
    f.write(".DS_Store\nThumbs.db\n")
print(f"  ✅ .gitignore")

# 初始化 git（如果尚未初始化）
if not os.path.exists(os.path.join(repo_dir, ".git")):
    os.system(f'cd "{repo_dir}" && git init && git checkout -b main')
    print(f"  ✅ git init + main branch")

print(f"\n仓库初始化完成: {repo_dir}")
print(f"下一步:")
print(f"  1. cd {repo_dir}")
print(f'  2. git remote add origin <你的GitHub仓库URL>')
print(f'  3. git add . && git commit -m "init: 海洋AI日报站点骨架"')
print(f'  4. git push -u origin main')
print(f'  5. 在 GitHub repo Settings → Pages 中启用 Pages')
