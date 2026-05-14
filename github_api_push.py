#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 GitHub REST API 推送修正后的日报
绕过 git push 的网络问题
"""
import base64, json, urllib.request, urllib.error

REPO = "tianyunsu/ocean-data-daily-report"
BRANCH = "main"

# Files to push
FILES = {
    'posts/2026-04-24.html': 'daily_reports/海洋AI简报_2026-04-24.html',
    'index.html': 'index.html',
    'feishu_write_doc.py': 'feishu_write_doc.py',
}

TOKEN_FILE = 'C:/Users/Administrator/.workbuddy/github_token.txt'
try:
    with open(TOKEN_FILE, 'r') as f:
        token = f.read().strip()
    print(f"Token loaded: {token[:4]}...")
except:
    token = None
    print("No token file found")

API = "https://api.github.com"

def api(method, path, data=None, token=None):
    url = f"{API}{path}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "WorkBuddy-Python/1.0",
    }
    if token:
        headers["Authorization"] = f"token {token}"
    if data:
        headers["Content-Type"] = "application/json"
        data = json.dumps(data).encode()

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        return json.loads(e.read()), e.code

# 1. Get current commit SHA
print("1. Getting current main branch commit...")
result, status = api("GET", f"/repos/{REPO}/branches/{BRANCH}")
if status != 200:
    print(f"ERROR: {result}")
else:
    base_tree_sha = result['commit']['commit']['tree']['sha']
    print(f"   base_tree_sha: {base_tree_sha}")

# 2. Create blobs for files
blobs = {}
for git_path, local_path in FILES.items():
    with open(local_path, 'rb') as f:
        content = f.read()
    encoded = base64.b64encode(content).decode()
    data = {"content": encoded, "encoding": "base64"}
    result, status = api("POST", f"/repos/{REPO}/git/blobs", data, token)
    if status != 201:
        print(f"ERROR creating blob for {git_path}: {result}")
    else:
        blobs[git_path] = result['sha']
        print(f"   Blob created for {git_path}: {result['sha']}")

# 3. Create new tree
tree_items = []
for git_path, blob_sha in blobs.items():
    tree_items.append({"path": git_path, "mode": "100644", "type": "blob", "sha": blob_sha})

data = {"base_tree": base_tree_sha, "tree": tree_items}
result, status = api("POST", f"/repos/{REPO}/git/trees", data, token)
if status != 201:
    print(f"ERROR creating tree: {result}")
else:
    new_tree_sha = result['sha']
    print(f"   New tree created: {new_tree_sha}")

    # 4. Create commit
    commit_data = {
        "message": "Fix: 替换9条超期内容，重新生成2026-04-24日报（2024-2025年过期条目已删除）",
        "tree": new_tree_sha,
        "parents": [result['commit']['sha']]
    }
    # Actually get the current commit SHA for parents
    branch_info, _ = api("GET", f"/repos/{REPO}/branches/{BRANCH}")
    current_commit_sha = branch_info['commit']['sha']
    commit_data["parents"] = [current_commit_sha]

    result, status = api("POST", f"/repos/{REPO}/git/commits", commit_data, token)
    if status != 201:
        print(f"ERROR creating commit: {result}")
    else:
        new_commit_sha = result['sha']
        print(f"   Commit created: {new_commit_sha}")

        # 5. Update branch reference
        result, status = api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}",
                            {"sha": new_commit_sha, "force": False}, token)
        if status == 200:
            print(f"   Branch updated to: {new_commit_sha}")
            print("SUCCESS! Files pushed to GitHub")
        else:
            print(f"ERROR updating branch: {result}")
