import openpyxl
from datetime import datetime

# Assume this method is already defined somewhere in your code
def execute_sql_query(sql_query, params):
    # Your existing implementation to execute the query
    cursor.execute(sql_query, params)

# Load the Excel file
file_path = 'your_excel_file.xlsx'
wb = openpyxl.load_workbook(file_path)
sheet = wb['export']

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

# Fetch the first row (header) and strip spaces
excel_headers = [cell.value.strip() if cell.value else '' for cell in sheet[1]]

# Iterate over rows and insert or update the SQLite table
for row in sheet.iter_rows(min_row=2, values_only=True):
    # Extract relevant columns based on the mapping
    excel_data = {table_col: None for table_col in column_mapping.keys()}
    for table_col, excel_col in column_mapping.items():
        if excel_col != "Current Timestamp":  # Skip timestamp, we'll handle that manually
            # Strip spaces in Excel column name and find the correct index
            if excel_col.strip() in excel_headers:
                excel_data[table_col] = row[excel_headers.index(excel_col.strip())]

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

    # Execute the insert or update query using your method
    execute_sql_query(insert_query, list(excel_data.values()))

print("Data has been successfully inserted or updated in the table.")