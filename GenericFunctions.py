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

# Define the mapping of Excel column names to desired names
excel_to_db_mapping = {
    'Actual_First_Column_Name': 'db_col_1',   # Excel column maps to DB column
    'type': 'PROJECT_TYPE',                     # Excel 'type' maps to DB 'PROJECT_TYPE'
    'Actual_Third_Column_Name': 'db_col_3'     # Additional mapping as needed
}

# Loop through all sheets and insert data into the same pre-existing table
for sheet_name in xls.sheet_names:
    # Read the data from the current sheet
    df = pd.read_excel(xls, sheet_name=sheet_name)

    # Strip whitespace from the column names
    df.columns = df.columns.str.strip()

    # Print the actual column names loaded
    print(f"Columns in {sheet_name}: {df.columns.tolist()}")

    # Check if the desired columns are present
    missing_columns = [col for col in excel_to_db_mapping.keys() if col not in df.columns]
    if missing_columns:
        print(f"Missing columns in sheet {sheet_name}: {missing_columns}")
        continue

    # Keep only the desired columns
    df = df[list(excel_to_db_mapping.keys())]

    # Rename columns in the DataFrame to match the database schema
    df.rename(columns=excel_to_db_mapping, inplace=True)

    # Modify the specified column (db_col_1): split by '/' and take the second part
    df['db_col_1'] = df['db_col_1'].apply(
        lambda x: x.split('/')[1] if isinstance(x, str) and '/' in x else x
    )

    # Prepare the columns for insertion
    db_columns = ', '.join(excel_to_db_mapping.values())  # Database column names

    # Insert the data into the table
    for row in df.itertuples(index=False):
        values = [
            row.db_col_1,          # Modified first column
            row.PROJECT_TYPE,      # 'type' column mapped to PROJECT_TYPE
            row.db_col_3           # Third column
        ]
        
        placeholders = ', '.join(['?' for _ in values])  # Prepare placeholders for SQL insertion
        insert_query = f'INSERT INTO "{table_name}" ({db_columns}) VALUES ({placeholders})'
        cursor.execute(insert_query, values)

    print(f"Data from sheet {sheet_name} inserted into {table_name}")

    conn.commit()

# Close the connection
conn.close()