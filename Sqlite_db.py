import sqlite3
import pandas as pd

# SQlite database connection
new_connection = sqlite3.connect(r'D:\Python\Applied_Python\demo1.db')

# Loading data into DataFrame
demo_data = pd.read_csv('demo1.csv')

# write the data to a sqlite table
demo_data.to_sql('demo1', new_connection, if_exists='replace', index=False)

# close connection to SQLite database
new_connection.close()
