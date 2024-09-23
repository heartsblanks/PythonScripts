import pandas as pd
import sqlite3

# Connect to your pre-existing database (SQLite in this example)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Load the Excel file
file_path = 'your_file.xlsx'
xls = pd.ExcelFile(file_path, engine='openpyxl')

# Define the table name (which is already created in the database)
table_name = "IIB_project_details"

# Mapping of Excel columns to database columns (based on the Excel column name)
# The Excel 'type' column will map to the 'PROJECT_TYPE' column in the database
column_mapping = {
    'db_col_1': 0,           # Excel column 0 maps to db_col_1
    'PROJECT_TYPE': 'type',  # Excel column 'type' maps to PROJECT_TYPE
    'db_col_3': 2,           # Excel column 2 maps to db_col_3
    'db_col_4': 3,           # Excel column 3 maps to db_col_4
    'db_col_5': 4            # Excel column 4 maps to db_col_5
}

# Loop through all sheets and insert data into the same pre-existing table
for sheet_name in xls.sheet_names:
    # Read the data from the current sheet
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)

    # Check if the DataFrame has data
    if df.empty:
        print(f"No data found in sheet {sheet_name}")
        continue

    # Modify the first column (db_col_1): split by '/' and take the second part
    df.iloc[:, column_mapping['db_col_1']] = df.iloc[:, column_mapping['db_col_1']].apply(
        lambda x: x.split('/')[1] if isinstance(x, str) and '/' in x else x
    )

    # Prepare the columns for insertion
    db_columns = ', '.join(column_mapping.keys())  # Database column names

    # Insert the data into the table
    for row in df.itertuples(index=False):
        values = [
            row[column_mapping['db_col_1']],                # First column after split
            row[df.columns.get_loc(column_mapping['PROJECT_TYPE'])],  # 'type' column mapped to PROJECT_TYPE
            row[column_mapping['db_col_3']],                # 3rd column
            row[column_mapping['db_col_4']],                # 4th column
            row[column_mapping['db_col_5']]                 # 5th column
        ]
        
        placeholders = ', '.join(['?' for _ in values])  # Prepare placeholders for SQL insertion
        insert_query = f'INSERT INTO "{table_name}" ({db_columns}) VALUES ({placeholders})'
        cursor.execute(insert_query, values)

    print(f"Data from sheet {sheet_name} inserted into {table_name}")

    conn.commit()

# Close the connection
conn.close()