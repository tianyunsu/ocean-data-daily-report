import sqlite3
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

db_path = r'C:\Users\Administrator\AppData\Roaming\WorkBuddy\automations\automations.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Get tables
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
print("Tables:", tables)

# Get all columns for each table
for table in tables:
    table_name = table[0]
    c.execute(f"PRAGMA table_info({table_name})")
    cols = c.fetchall()
    print(f"\nColumns in {table_name}:", [col[1] for col in cols])
    
    # Get data
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    for row in rows:
        print(repr(row))

conn.close()
