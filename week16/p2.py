import pandas as pd
import sqlite3
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://stats.moe.gov.tw/files/detail/112/112_students.csv'

df = pd.read_csv(url)

columns = ["學校名稱", "科系名稱", "日間∕進修別", "等級別", "一年級男生", "一年級女生", "縣市名稱"]
df = df[columns]
df.columns = ["school", "department", "system", "degree", "male_1", "female_1", "city"]
df['city'] = df['city'].str.replace(r'^\d+\s*', '', regex=True)
df['male_1'] = pd.to_numeric(df['male_1'], errors='coerce').fillna(0).astype(int)
df['female_1'] = pd.to_numeric(df['female_1'], errors='coerce').fillna(0).astype(int)

conn = sqlite3.connect('students.db')
create_table_query = '''
CREATE TABLE IF NOT EXISTS student112 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    school TEXT,
    department TEXT,
    system TEXT,
    degree TEXT,
    male_1 INTEGER,
    female_1 INTEGER,
    city TEXT
);
'''
conn.execute(create_table_query)
conn.commit()

df.to_sql('student112', conn, if_exists='append', index=False)
conn.close()
