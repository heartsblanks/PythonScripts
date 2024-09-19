import sqlite3
import os
import re
from datetime import datetime

# Assuming SSHExecutor is a class that handles SSH connections and command execution
class SSHExecutor:
    def __init__(self, host, user, password):
        # Initialization code for connecting to the host
        pass

    def execute_command(self, command):
        # Code to execute a command on the remote host and return the output
        pass

def fetch_wtx_projects(ssh_executor, directory):
    """Fetch all folder names starting with 'WTX'."""
    command = f"ls -d {directory}/WTX*"
    result = ssh_executor.execute_command(command)
    # Assuming the result is a list of folder paths
    return result.splitlines()

def fetch_latest_log(ssh_executor, project_directory):
    """Fetch the latest log file from the project directory."""
    command = f"ls -t {project_directory}/*.log | head -n 1"
    latest_log = ssh_executor.execute_command(command).strip()
    return latest_log

def extract_cvs_tag(log_content):
    """Extract the cvs_tag value from the log content."""
    match = re.search(r'cvs_tag=(\S+)', log_content)
    if match:
        return match.group(1)
    return None

def insert_into_db(project_name, cvs_tag):
    """Insert project details into SQLite database."""
    conn = sqlite3.connect('wtx_project_details.db')
    cursor = conn.cursor()

    # Ensure table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WTX_PROJECT_DETAILS (
            project_name TEXT,
            pap TEXT,
            production_tag TEXT
        )
    ''')

    # Insert project data
    cursor.execute('''
        INSERT INTO WTX_PROJECT_DETAILS (project_name, pap, production_tag)
        VALUES (?, ?, ?)
    ''', (project_name, 'PAP_Value', cvs_tag))  # Assuming 'PAP_Value' is a placeholder for your actual PAP value

    conn.commit()
    conn.close()

def main():
    # SSH details for both hosts
    first_host_ssh = SSHExecutor('first_host', 'user', 'password')
    second_host_ssh = SSHExecutor('second_host', 'user', 'password')

    # Directory on first host containing WTX projects
    first_host_directory = "/path/to/first/host/directory"
    
    # Fetch WTX project folders
    wtx_projects = fetch_wtx_projects(first_host_ssh, first_host_directory)

    # Process each project
    for project in wtx_projects:
        # Connect to second host and fetch the latest log file for each project
        latest_log_file = fetch_latest_log(second_host_ssh, f"/path/to/second/host/directory/{os.path.basename(project)}")
        
        # Fetch log file content
        log_content = second_host_ssh.execute_command(f"cat {latest_log_file}")
        
        # Extract cvs_tag from the log file content
        cvs_tag = extract_cvs_tag(log_content)
        if cvs_tag:
            # Insert project name and cvs_tag into the SQLite database
            insert_into_db(os.path.basename(project), cvs_tag)

if __name__ == "__main__":
    main()