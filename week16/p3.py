import sqlite3
import pandas as pd

conn = sqlite3.connect('students.db')

query = '''
SELECT * FROM student112
WHERE school = '國立臺北科技大學';
'''

df_ntut = pd.read_sql_query(query, conn)
conn.close()

print(df_ntut)
