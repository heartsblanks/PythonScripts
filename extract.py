import sqlite3
import re
from datetime import datetime

# Assume this is your existing method that retrieves file content
def get_file_content_from_repo(repo_org, file_folder, file_name, branch):
    # This method is a placeholder for your existing implementation
    # You will replace it with your actual method to fetch file content from the repository
    pass

# Function to get primary key columns from the table schema
def get_primary_key_columns(table_name, cursor):
    cursor.execute(f"PRAGMA table_info({table_name});")
    table_info = cursor.fetchall()
    
    # Extract column names where pk (primary key) is non-zero
    primary_key_columns = [info[1] for info in table_info if info[5] > 0]
    return primary_key_columns

# Function to extract the project name from file content
def extract_project_name(file_content):
    match = re.search(r"configure\.project\.name\.mfp=(.*)", file_content)
    if match:
        return match.group(1).strip()
    return None

# Function to parse the date from the PRODUCTION_TAG
def extract_date_from_production_tag(production_tag):
    match = re.search(r"TEST-(\d{4}-\d{2}-\d{2}-\d{4})", production_tag)
    if match:
        date_str = match.group(1)
        return datetime.strptime(date_str, "%Y-%m-%d-%H%M")
    return None

# Main function to retrieve data, fetch file content, and insert into PROJECT_DETAILS table
def update_project_details(repo_org, file_folder, branch):
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Original table where data is stored
    source_table = 'your_source_table'

    # Get the primary key columns dynamically from the source table
    primary_key_columns = get_primary_key_columns(source_table, cursor)

    # Fetch all columns from the source table (using SELECT *)
    cursor.execute(f"SELECT * FROM {source_table}")
    rows = cursor.fetchall()

    # Retrieve the column names from the source table
    cursor.execute(f"PRAGMA table_info({source_table})")
    table_info = cursor.fetchall()
    column_names = [info[1] for info in table_info]  # Extract column names

    # Group rows by PAP and filter by the latest PRODUCTION_TAG
    pap_dict = {}
    for row in rows:
        row_dict = dict(zip(column_names, row))  # Map column names to row values
        pap = row_dict['PAP']
        production_tag = row_dict['PRODUCTION_TAG']

        # Extract the date from the PRODUCTION_TAG
        tag_date = extract_date_from_production_tag(production_tag)

        # For each PAP, keep the row with the latest PRODUCTION_TAG date
        if pap not in pap_dict or (tag_date and tag_date > pap_dict[pap]['date']):
            pap_dict[pap] = {'row': row_dict, 'date': tag_date}

    # Iterate over the filtered rows (latest for each PAP)
    for pap, data in pap_dict.items():
        row_dict = data['row']

        # Extract necessary fields from the row
        pf_number = row_dict['PF_NUMBER']
        mandant = row_dict['MANDANT']
        production_tag = row_dict['PRODUCTION_TAG']
        integration_server = row_dict.get('INTEGRATION_SERVER')
        platform = row_dict.get('PLATFORM')

        # Fetch the file content where the file name matches PF_NUMBER
        file_content = get_file_content_from_repo(repo_org, file_folder, pf_number, branch)

        # Extract the project name from the file content
        project_name = extract_project_name(file_content)
        
        if project_name:
            # Dynamically construct the insert query based on column names
            columns = ', '.join(column_names)
            placeholders = ', '.join(['?'] * len(column_names))
            
            # Prepare the insert query for PROJECT_DETAILS
            insert_query = f"""
            INSERT INTO PROJECT_DETAILS (PROJECT_NAME, PAP, PROJECT_TYPE, MANDANT, PRODUCTION_TAG, INTEGRATION_SERVER, PLATFORM)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(PROJECT_NAME, PAP, PROJECT_TYPE, MANDANT)
            DO UPDATE SET PRODUCTION_TAG = excluded.PRODUCTION_TAG,
                          INTEGRATION_SERVER = excluded.INTEGRATION_SERVER,
                          PLATFORM = excluded.PLATFORM;
            """

            # PROJECT_TYPE is derived from PF_NUMBER (you can adjust this if needed)
            project_type = pf_number

            # Insert or update the data in the PROJECT_DETAILS table
            cursor.execute(insert_query, (project_name, pap, project_type, mandant, production_tag, integration_server, platform))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data has been successfully inserted or updated in the PROJECT_DETAILS table.")