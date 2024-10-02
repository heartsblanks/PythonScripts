import pandas as pd
from datetime import datetime

# Assume this method is already defined somewhere in your code
def execute_sql_query(sql_query, params):
    cursor.execute(sql_query, params)

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

# Columns used to check for existing records (composite key)
key_columns = ["FLOW_NAME", "PAP", "PF_NUMBER", "MANDANT"]

# Iterate over rows and insert or update the SQLite table
for index, row in df.iterrows():
    # Extract relevant columns based on the mapping
    excel_data = {table_col: row[excel_col].strip() if isinstance(row[excel_col], str) else row[excel_col]
                  for table_col, excel_col in column_mapping.items() if excel_col != "Current Timestamp"}

    # Get the current timestamp for UPDATED_TIMESTAMP
    excel_data["UPDATED_TIMESTAMP"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prepare the insert statement with ON CONFLICT to handle updates
    insert_query = f"""
    INSERT INTO your_table_name ({', '.join(column_mapping.keys())})
    VALUES ({', '.join(['?' for _ in column_mapping.keys()])})
    ON CONFLICT ({', '.join(key_columns)}) 
    DO UPDATE SET {', '.join([f"{col} = excluded.{col}" for col in column_mapping.keys() if col != "UPDATED_TIMESTAMP"])}
    , UPDATED_TIMESTAMP = excluded.UPDATED_TIMESTAMP
    """

    # Create the params from the excel_data
    params_data = tuple(excel_data.values())

    # Execute the insert or update query using your method
    execute_sql_query(insert_query, params_data)

print("Data has been successfully inserted or updated in the table.")