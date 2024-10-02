import sqlite3
import re
import os
from datetime import datetime
from urllib.parse import quote
from collections import defaultdict

# Function to extract project name from file content
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

# Function to read the file content from a local directory
def get_file_content_from_local(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to process the data and update project details in batches
def update_project_details(repo_org, file_folder, branch):
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Original table where data is stored
    source_table = 'your_source_table'

    # Fetch all columns from the source table (using SELECT *)
    cursor.execute(f"SELECT * FROM {source_table}")
    rows = cursor.fetchall()

    # Retrieve the column names from the source table
    cursor.execute(f"PRAGMA table_info({source_table})")
    table_info = cursor.fetchall()
    column_names = [info[1] for info in table_info]  # Extract column names

    # Dictionary to store grouped data for each PAP and PF_NUMBER
    grouped_data = defaultdict(lambda: {'mandants': set(), 'integration_servers': set(), 'latest_production_tag': None, 'row': None})

    # Iterate over each row to group data by PAP and PF_NUMBER
    for row in rows:
        row_dict = dict(zip(column_names, row))  # Map column names to row values
        pap = row_dict['PAP']
        pf_number = row_dict['PF_NUMBER']
        mandant = row_dict['MANDANT']
        integration_server = row_dict.get('INTEGRATION_SERVER')
        production_tag = row_dict['PRODUCTION_TAG']
        platform = row_dict.get('PLATFORM')

        # Extract the date from the PRODUCTION_TAG
        tag_date = extract_date_from_production_tag(production_tag)

        # Update the mandants and integration servers (adding them to a set to avoid duplicates)
        grouped_data[(pap, pf_number)]['mandants'].add(mandant)
        grouped_data[(pap, pf_number)]['integration_servers'].add(integration_server)

        # Check if the current production tag is the latest one for this PAP and PF_NUMBER
        if (grouped_data[(pap, pf_number)]['latest_production_tag'] is None or
                (tag_date and tag_date > extract_date_from_production_tag(grouped_data[(pap, pf_number)]['latest_production_tag']))):
            grouped_data[(pap, pf_number)]['latest_production_tag'] = production_tag
            grouped_data[(pap, pf_number)]['row'] = row_dict  # Keep the latest row

    # Prepare data for batch insert/update
    project_data = []

    # Iterate over the grouped data
    for (pap, pf_number), data in grouped_data.items():
        row_dict = data['row']

        # Convert mandants and integration servers to comma-separated strings
        mandants = ', '.join(sorted(data['mandants']))
        integration_servers = ', '.join(sorted(data['integration_servers']))
        production_tag = data['latest_production_tag']

        # Build the file path and read the content from the local directory
        encoded_file_name = quote(pf_number)
        file_path = os.path.join(file_folder, encoded_file_name)
        file_content = get_file_content_from_local(file_path)

        # Extract the project name from the file content
        project_name = extract_project_name(file_content)

        if project_name:
            # Prepare the data for batch insert/update
            project_type = pf_number  # Assuming PROJECT_TYPE is derived from PF_NUMBER
            project_data.append((project_name, pap, project_type, mandants, production_tag, integration_servers, row_dict['PLATFORM']))

    # Perform batch insert/update with the WHERE clause to update only if there are changes
    if project_data:
        insert_query = f"""
        INSERT INTO PROJECT_DETAILS (PROJECT_NAME, PAP, PROJECT_TYPE, MANDANT, PRODUCTION_TAG, INTEGRATION_SERVER, PLATFORM)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(PROJECT_NAME, PAP, PROJECT_TYPE)
        DO UPDATE SET PRODUCTION_TAG = excluded.PRODUCTION_TAG,
                      MANDANT = excluded.MANDANT,
                      INTEGRATION_SERVER = excluded.INTEGRATION_SERVER,
                      PLATFORM = excluded.PLATFORM
        WHERE PROJECT_DETAILS.PRODUCTION_TAG != excluded.PRODUCTION_TAG
            OR PROJECT_DETAILS.MANDANT != excluded.MANDANT
            OR PROJECT_DETAILS.INTEGRATION_SERVER != excluded.INTEGRATION_SERVER
            OR PROJECT_DETAILS.PLATFORM != excluded.PLATFORM;
        """

        # Batch insert all rows
        cursor.executemany(insert_query, project_data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data has been successfully inserted or updated in the PROJECT_DETAILS table.")