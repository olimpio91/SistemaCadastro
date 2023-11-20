import sqlite3

c = sqlite3.connect('Users.db')
cur = c.cursor()
cur.execute('SELECT * FROM Registered')
response = cur.fetchall()

print(response)