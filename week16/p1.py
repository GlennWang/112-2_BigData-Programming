import sqlite3

conn = sqlite3.connect('myDatabaseName.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS playerinfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        xpos INT,
        ypos INT,
        exp INT,
        lastlogin TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    INSERT INTO playerinfo (name, xpos, ypos, exp) 
    VALUES 
    ('韓德森', 14, 35, 1431),
    ('史密斯', 21, 86, 4563),
    ('王貝克', 10, 5, 231),
    ('魏斯特', 73, 13, 5400)
''')

cursor.execute('SELECT * FROM playerinfo')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('SELECT name, exp FROM playerinfo')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
