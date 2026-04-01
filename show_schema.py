import sqlite3

conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

cursor.execute("SELECT sql FROM sqlite_master WHERE name='tickets';")
schema = cursor.fetchone()[0]

print("\n===== TICKETS TABLE SCHEMA =====\n")
print(schema)
print("\n================================\n")

conn.close()