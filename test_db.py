import sqlite3
conn = sqlite3.Connection("skilling_programme.db")
cursor = conn.execute("SELECT * FROM student")
rows = cursor.fetchall()
print(rows)
conn.close()