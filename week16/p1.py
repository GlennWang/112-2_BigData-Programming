import sqlite3

# 連接到 SQLite 資料庫，資料庫不存在時會自動創建
conn = sqlite3.connect('myDatabaseName.db')
cursor = conn.cursor()

# 創建 playerinfo 表
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

# 插入四筆資料
cursor.execute('''
    INSERT INTO playerinfo (name, xpos, ypos, exp) 
    VALUES 
    ('韓德森', 14, 35, 1431),
    ('史密斯', 21, 86, 4563),
    ('王貝克', 10, 5, 231),
    ('魏斯特', 73, 13, 5400)
''')

# 確認資料插入
cursor.execute('SELECT * FROM playerinfo')
rows = cursor.fetchall()

for row in rows:
    print(row)

# 確認修改資料
cursor.execute('SELECT name, exp FROM playerinfo')
rows = cursor.fetchall()

for row in rows:
    print(row)

# 使用完畢後關閉連接
conn.commit()
conn.close()
