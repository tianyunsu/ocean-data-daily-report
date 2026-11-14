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
| 定时任务定义（云端快照） | 仓库 `automations/ai/definition.json` | **只读快照**，随 git 同步；运行时状态仍以 WorkBuddy 自动化服务为准 |

一句话：**仓库负责记忆、脚本和定时任务定义的快照，`sync_skills.py` 负责补上 skill。**

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

## 六、定时任务定义（云端快照）与恢复

`automations/ai/definition.json` 是 WorkBuddy 自动化 `ai`「海洋AI研究日报」定义的**只读快照**，
于 2026-11-14 从云端任务定义导出并纳入版本控制，用于跨机器复原与灾备。
它**不是运行时配置**：改这个文件不会改变调度，真正生效的是 WorkBuddy 自动化服务里的任务。

### 当前定义要点

| 字段 | 值 |
|------|-----|
| id / name | `ai` / 海洋AI研究日报 |
| status | **PAUSED**（2026-10-18 起暂停，日常靠手动触发；改回 ACTIVE 才恢复调度） |
| scheduleType / rrule | `recurring` / `FREQ=DAILY;BYHOUR=9;BYMINUTE=0` |
| cwds | 主力机绝对路径 `C:\Users\Administrator\WorkBuddy\Claw` |
| workspaceScope | `workspace` |
| prompt | 纯委托层：只加载 `ocean-daily-report` skill 并委托 6 阶段，**不内联流程细节** |

### 在另一台机器恢复定时任务

1. 打开 WorkBuddy 自动化管理界面（或让 WorkBuddy 用 `automation_update(mode=create)`），按上表字段新建任务，
   `prompt` 直接取 `definition.json` 的 `automation.prompt`（`py -3 -m json.tool automations/ai/definition.json` 查看）。
2. **`cwds` 必须改成该机的工作区绝对路径**，否则阶段零的 `git pull` 会落在错误目录。
3. **恢复前先停用或删除同名旧任务**：两份任务都在 09:00 触发会造成同日并行执行（违反一致性铁律第 5 条）。
4. 是否把 `status` 设为 `ACTIVE` 需单独决定；仅导入快照不会恢复自动调度。
5. 流程细节以 `.workbuddy/skills/ocean-daily-report/SKILL.md` 为准，禁止把阶段细节写回 prompt。

### 两个必须避开的坑

- ⚠️ **不要用本机 `%APPDATA%\WorkBuddy\automations\automations.db` 恢复**：该库里的 `ai` 仍是旧定义
  （`ACTIVE` + 内联九方向细节），属双源漂移残留。一律以云端服务 + 本快照为准。
- ⚠️ 云端定义一有改动（改 prompt / 频率 / 状态 / 工作目录），须重新导出 `definition.json` 并 push，
  否则仓库快照与线上任务再次漂移。

---

## 七、常见问题

| 问题 | 处理 |
|------|------|
| 新会话没有加载 skill | 确认工作目录是仓库根目录；显式说「加载 ocean-daily-report skill，执行今天的日报」 |
| `sync_skills.py install` 报找不到目录 | 确认在仓库根目录下运行；确认 `.workbuddy/skills/` 已随仓库拉取 |
| push 被 TLS/代理拦截 | `git config --unset http.sslbackend` 或 `git config --global --unset http.proxy` |
| HTTPS push 超时 | 切 SSH：`git remote set-url origin git@github.com:tianyunsu/ocean-data-daily-report.git` |
| 两台机器记忆冲突 | 以时间较新的每日日志为准；`MEMORY.md` 去重基准需手动合并两侧条目，不要直接取一侧覆盖 |
| 该机 Python 编码报错 | 先设 `PYTHONUTF8=1` 再运行脚本 |
| 定时任务定义与线上不一致 | 以 WorkBuddy 自动化服务为准；重新导出 `automations/ai/definition.json` 并 push，不要改本地 `automations.db` |
