import pandas as pd
from datetime import datetime
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Read the Excel file using pandas
file_path = 'your_excel_file.xlsx'
df = pd.read_excel(file_path, sheet_name='export')

# Mapping of table columns to Excel columns
column_mapping = {
    "FLOW_NAME": "FlowName",
    "PAP": "PAP",
    "PF_NUMBER": "FlowID",
    "MANDANT": "Mandant",
    "PRODUCTION_TAG": "ProdTag",
    "INTEGRATION_SERVER": "IIB EG",
    "PLATFORM": "ACE Node",
    "UPDATED_TIMESTAMP": "Current Timestamp"  # This will use the current timestamp
}

# Primary key columns (already part of the table definition)
key_columns = ["FLOW_NAME", "PAP", "PF_NUMBER", "MANDANT"]

# Iterate over rows and insert or update the SQLite table
for index, row in df.iterrows():
    # Prepare a dictionary for the property values (column name -> value)
    properties_dict = {table_col: row[excel_col].strip() if isinstance(row[excel_col], str) else row[excel_col]
                       for table_col, excel_col in column_mapping.items() if excel_col != "Current Timestamp"}

    # Add the current timestamp for the UPDATED_TIMESTAMP column
    properties_dict["UPDATED_TIMESTAMP"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Dynamically generate column names and placeholders for SQL query
    columns = ', '.join(properties_dict.keys())
    placeholders = ', '.join(['?'] * len(properties_dict))

    # Dynamically generate update columns for the ON CONFLICT clause
    update_columns = ', '.join([f"{key} = ?" for key in properties_dict.keys()])

    # Prepare the values for insertion and update
    insert_values = tuple(properties_dict.values())
    update_values = tuple(properties_dict.values())

    # Combine insert and update values for the execute function
    query_values = insert_values + update_values

    # Prepare the upsert query: insert if it doesn't exist, or update if it exists
    insert_query = f"""
    INSERT INTO your_table_name ({columns})
    VALUES ({placeholders})
    ON CONFLICT({', '.join(key_columns)})
    DO UPDATE SET {update_columns};
    """

    # Execute the upsert query
    cursor.execute(insert_query, query_values)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data has been successfully inserted or updated in the table.")