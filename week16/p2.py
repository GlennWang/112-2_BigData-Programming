import pandas as pd
import sqlite3
import ssl

# Disable SSL verification to read the CSV file
ssl._create_default_https_context = ssl._create_unverified_context

# URL of the CSV file
url = 'https://stats.moe.gov.tw/files/detail/112/112_students.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(url)

# Define the columns to be extracted
columns = ["學校名稱", "科系名稱", "日間∕進修別", "等級別", "一年級男生", "一年級女生", "縣市名稱"]

# Extract only the relevant columns
df = df[columns]

# Rename columns to match the desired table schema
df.columns = ["school", "department", "system", "degree", "male_1", "female_1", "city"]

# Remove any leading numbers and whitespace from the 'city' column
df['city'] = df['city'].str.replace(r'^\d+\s*', '', regex=True)

# Ensure all columns have consistent data types
df['male_1'] = pd.to_numeric(df['male_1'], errors='coerce').fillna(0).astype(int)
df['female_1'] = pd.to_numeric(df['female_1'], errors='coerce').fillna(0).astype(int)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create the student112 table
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

# Insert data into the student112 table
df.to_sql('student112', conn, if_exists='append', index=False)

# Close the database connection
conn.close()
