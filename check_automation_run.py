import sqlite3, datetime

db_path = r'C:\Users\Administrator\AppData\Roaming\WorkBuddy\automations\automations.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 查看automation_runs表结构
cur.execute("PRAGMA table_info(automation_runs)")
cols = cur.fetchall()
print("automation_runs columns:", [c[1] for c in cols])

# 查看所有运行记录
cur.execute("SELECT * FROM automation_runs ORDER BY rowid DESC LIMIT 20")
rows = cur.fetchall()
print(f"\nRecent runs: {len(rows)}")
for row in rows:
    print(row)

conn.close()
