import sqlite3
import pandas as pd

conn = sqlite3.connect('students.db')
query = '''
SELECT school, count(*) as department_count 
FROM student112 
WHERE department LIKE '%資訊%' 
GROUP BY school;
'''

df_info_departments = pd.read_sql_query(query, conn)
conn.close()


print(df_info_departments)
