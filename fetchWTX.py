import sqlite3
import os
import re

def fetch_wtx_projects_from_db():
    """Fetch project name and PF_name from the SQLite database."""
    conn = sqlite3.connect('wtx_project_details.db')
    cursor = conn.cursor()
    
    # Fetch all rows with project_name and PF_name
    cursor.execute('SELECT project_name, PF_name FROM WTX_PROJECT_DETAILS')
    projects = cursor.fetchall()
    
    conn.close()
    return projects

def fetch_latest_log(ssh_executor, project_identifier, directory):
    """Fetch the latest log file for the given project identifier (PF_name or project_name)."""
    command = f"ls -t {directory}/{project_identifier}/*.log | head -n 1"
    latest_log = ssh_executor.execute_command(command).strip()
    return latest_log

def extract_cvs_tag(log_content):
    """Extract the cvs_tag value from the log content."""
    match = re.search(r'cvs_tag=(\S+)', log_content)
    if match:
        return match.group(1)
    return None

def update_db_with_cvs_tag(project_name, cvs_tag):
    """Update the database with the retrieved cvs_tag for the given project."""
    conn = sqlite3.connect('wtx_project_details.db')
    cursor = conn.cursor()

    # Update the table with the new cvs_tag (production_tag)
    cursor.execute('''
        UPDATE WTX_PROJECT_DETAILS
        SET production_tag = ?
        WHERE project_name = ?
    ''', (cvs_tag, project_name))

    conn.commit()
    conn.close()

def main():
    # SSH details for the host
    second_host_ssh = SSHExecutor('second_host', 'user', 'password')

    # Directory on second host containing logs
    second_host_directory = "/path/to/second/host/directory"

    # Fetch projects and PF_names from the database
    projects = fetch_wtx_projects_from_db()

    for project_name, pf_name in projects:
        # Determine the identifier to use (PF_name or project_name)
        project_identifier = pf_name if pf_name else project_name
        
        # Fetch the latest log file based on the project identifier
        latest_log_file = fetch_latest_log(second_host_ssh, project_identifier, second_host_directory)
        
        if latest_log_file:
            # Fetch log file content
            log_content = second_host_ssh.execute_command(f"cat {latest_log_file}")
            
            # Extract cvs_tag from the log file content
            cvs_tag = extract_cvs_tag(log_content)
            
            if cvs_tag:
                # Update the project with the extracted cvs_tag
                update_db_with_cvs_tag(project_name, cvs_tag)

if __name__ == "__main__":
    main()