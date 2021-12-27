import sqlite3
con = sqlite3.connect("demo.db")
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS "student" ("id"	INTEGER,"name"	TEXT,"age"	INTEGER,PRIMARY KEY("id"));')
print("Database Created")
con.close()