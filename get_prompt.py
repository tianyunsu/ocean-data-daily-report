import sqlite3
import sys

db_path = r'C:\Users\Administrator\AppData\Roaming\WorkBuddy\automations\automations.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT id, name, prompt, status, rrule, cwds FROM automations WHERE id='ai'")
row = c.fetchone()
if row:
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Status: {row[3]}")
    print(f"RRule: {row[4]}")
    print(f"CWDs: {row[5]}")
    print(f"\n=== PROMPT ===\n{row[2]}")
conn.close()
