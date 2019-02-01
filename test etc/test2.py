import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("SELECT * FROM container WHERE vuilnisniveau >= 85")
abc = (c.fetchall())
print(abc)