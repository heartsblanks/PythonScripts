import sqlite3
import re

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

# Main function to retrieve data, fetch file content, and insert into PROJECT_DETAILS table
def update_project_details(repo_org, file_folder, branch):
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Original table where PAP, PF_NUMBER, MANDANT, and other data are stored
    source_table = 'your_source_table'

    # Get the primary key columns dynamically from the source table
    primary_key_columns = get_primary_key_columns(source_table, cursor)

    # Fetch rows from the original table (PAP, PF_NUMBER, MANDANT, PRODUCTION_TAG, INTEGRATION_SERVER, PLATFORM)
    cursor.execute(f"SELECT PAP, PF_NUMBER, MANDANT, PRODUCTION_TAG, INTEGRATION_SERVER, PLATFORM FROM {source_table}")
    rows = cursor.fetchall()

    # Iterate over each row to fetch the file content and insert into PROJECT_DETAILS
    for row in rows:
        pap, pf_number, mandant, production_tag, integration_server, platform = row
        
        # Fetch the file content where the file name matches PF_NUMBER
        file_content = get_file_content_from_repo(repo_org, file_folder, pf_number, branch)

        # Extract the project name from the file content
        project_name = extract_project_name(file_content)
        
        if project_name:
            # Prepare the insert query for PROJECT_DETAILS
            insert_query = f"""
            INSERT INTO PROJECT_DETAILS (PROJECT_NAME, PAP, PROJECT_TYPE, MANDANT, PRODUCTION_TAG, INTEGRATION_SERVER, PLATFORM)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(PROJECT_NAME, PAP, PROJECT_TYPE, MANDANT)
            DO UPDATE SET PRODUCTION_TAG = excluded.PRODUCTION_TAG,
                          INTEGRATION_SERVER = excluded.INTEGRATION_SERVER,
                          PLATFORM = excluded.PLATFORM;
            """
            # PROJECT_TYPE is derived from PF_NUMBER (based on your requirements, you can modify this part)
            project_type = pf_number  # Assuming PF_NUMBER is used as PROJECT_TYPE

            # Insert or update the data in the PROJECT_DETAILS table
            cursor.execute(insert_query, (project_name, pap, project_type, mandant, production_tag, integration_server, platform))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data has been successfully inserted or updated in the PROJECT_DETAILS table.")