import pandas as pd
import sqlite3
import re

# Connect to your database (SQLite in this example, you can use others like MySQL or PostgreSQL)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Load the Excel file
file_path = 'your_file.xlsx'
xls = pd.ExcelFile(file_path)

# Iterate over each sheet
for sheet_name in xls.sheet_names:
    # Replace '-' with '_' in the table name
    table_name = re.sub(r'-', '_', sheet_name)

    # Read the data from the sheet
    df = pd.read_excel(xls, sheet_name=sheet_name)

    # Use the first row as column names and drop the first row from the data
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])

    # Create table if it doesn't exist
    columns = ', '.join([f'"{col}" TEXT' for col in df.columns])
    create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns});'
    cursor.execute(create_table_query)

    # Insert data into the table
    for row in df.itertuples(index=False):
        placeholders = ', '.join(['?' for _ in row])
        insert_query = f'INSERT INTO "{table_name}" VALUES ({placeholders})'
        cursor.execute(insert_query, row)

    conn.commit()

# Close the connection
conn.close()