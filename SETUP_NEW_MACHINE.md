# 在另一台电脑执行海洋AI研究日报

目标：在任意一台电脑上手动生成日报，效果与主力机（含定时自动化）完全一致——同一套流程、同一套记忆、同一份去重基准。

---

## 一、原理：三类资产分别在哪

| 资产 | 位置 | 跨机器同步方式 |
|------|------|----------------|
| 记忆文件（每日日志、去重基准、自动化执行摘要） | 仓库内 `.workbuddy/memory/`、`.workbuddy/automations/` | **随 git 仓库同步**（已纳入版本控制） |
| skill（唯一权威指令源） | 用户级 `~/.workbuddy/skills/` | **不随仓库**，需用 `sync_skills.py` 安装 |
| 生成与发布脚本 | 仓库根目录（`feishu_write_doc.py`、`deploy_report.py` 等） | 随 git 仓库同步 |
| 历史日报 | 仓库 `posts/`、`daily_reports/` | 随 git 仓库同步 |

一句话：**仓库负责记忆和脚本，`sync_skills.py` 负责补上 skill。**

---

## 二、新电脑首次配置（一次性，约 3 分钟）

### 1. 克隆仓库

```bash
git clone git@github.com:tianyunsu/ocean-data-daily-report.git
# 若该机未配置 SSH key，改用 HTTPS：
# git clone https://github.com/tianyunsu/ocean-data-daily-report.git
```

建议把工作目录放在与主力机相同的语义位置（路径本身不必完全相同，但要固定下来）。

### 2. 安装 skill 到用户级目录

```bash
cd ocean-data-daily-report
python sync_skills.py install
```

会把仓库内 `.workbuddy/skills/` 下的两个 skill 复制到该机的 `~/.workbuddy/skills/`：

- `ocean-daily-report` —— 日报生成的唯一权威指令源（6 阶段流程、9 方向定义、23 个顶会清单、质量标准）
- `automation-consistency` —— 手动/自动执行一致性方法论

### 3. 验证

```bash
python sync_skills.py status
```

输出两个 `[一致]` 即配置完成。

### 4.（可选）配置飞书推送

仅当需要推送飞书文档/机器人时，在该机设置环境变量（主力机上目前飞书 docx 写入 API 有 404 问题，通常可跳过）：

```bash
# Windows PowerShell
$env:FEISHU_WEBHOOK="..."
$env:PYTHONUTF8=1
```

---

## 三、每次手动执行日报的标准动作

```bash
# 第 1 步：拉取最新记忆（关键，否则去重基准过期会出重复条目）
cd ocean-data-daily-report
git pull origin main

# 第 2 步：同步 skill（主力机若更新过 skill，这一步会带过来）
python sync_skills.py install
```

第 3 步：在 WorkBuddy 里新建任务，**工作目录选到这个 clone 出来的仓库根目录**，然后说：

> 执行海洋AI研究日报

触发词会命中 `ocean-daily-report` skill，自动走完 6 个阶段（顶会检索 → 常规检索 → 编写 → 发布 → 质检 → 记忆写入）。

第 4 步：执行完成后，确认记忆已推送（skill 阶段六通常会自动 push，若未推送则手动执行）：

```bash
git add -A .workbuddy posts index.html archive.html daily_reports
git commit -m "docs: 2026-XX-XX 日报 + 记忆"
git push origin main
```

---

## 四、若在该机修改了 skill

skill 改动不会自动进仓库，需要回收后推送，否则主力机拿不到：

```bash
python sync_skills.py collect
git add -A .workbuddy/skills
git commit -m "chore: 更新 skill"
git push origin main
```

主力机下次 `git pull` + `python sync_skills.py install` 即可同步。

---

## 五、一致性铁律（两台机器都适用）

1. **执行前必须 `git pull`**，否则去重基准落后，会重复收录已发布内容。
2. **执行后必须 push 记忆**，否则另一台机器的下一次执行会漏掉本期条目。
3. **手动执行 ≠ 简化执行**：必须走完 skill 的 6 个阶段，尤其阶段六记忆写入不可跳过。
4. **skill 是唯一权威源**：流程要改先改 skill，再 `collect` 回收进仓库；不要在对话里临时口头改流程。
5. **不要在两台机器同时执行同一天的日报**，会造成 git 冲突和内容重复。

---

## 六、常见问题

| 问题 | 处理 |
|------|------|
| 新会话没有加载 skill | 确认工作目录是仓库根目录；显式说「加载 ocean-daily-report skill，执行今天的日报」 |
| `sync_skills.py install` 报找不到目录 | 确认在仓库根目录下运行；确认 `.workbuddy/skills/` 已随仓库拉取 |
| push 被 TLS/代理拦截 | `git config --unset http.sslbackend` 或 `git config --global --unset http.proxy` |
| HTTPS push 超时 | 切 SSH：`git remote set-url origin git@github.com:tianyunsu/ocean-data-daily-report.git` |
| 两台机器记忆冲突 | 以时间较新的每日日志为准；`MEMORY.md` 去重基准需手动合并两侧条目，不要直接取一侧覆盖 |
| 该机 Python 编码报错 | 先设 `PYTHONUTF8=1` 再运行脚本 |
