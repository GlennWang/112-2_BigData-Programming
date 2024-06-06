import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Define the query to retrieve all departments of "國立臺北科技大學"
query = '''
SELECT * FROM student112
WHERE school = '國立臺北科技大學';
'''

# Execute the query and load the data into a DataFrame
df_ntut = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Display the result
print(df_ntut)
