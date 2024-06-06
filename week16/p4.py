import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Define the query to count departments containing '資訊' for each school
query = '''
SELECT school, count(*) as department_count 
FROM student112 
WHERE department LIKE '%資訊%' 
GROUP BY school;
'''

# Execute the query and load the data into a DataFrame
df_info_departments = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Display the result
print(df_info_departments)
