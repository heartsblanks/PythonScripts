import re
import sqlite3  # Change this import for your specific database

# Connect to the database (adjust for your database setup)
conn = sqlite3.connect('mq_definitions.db')  # Change the database name if needed
cursor = conn.cursor()

# Sample input string with DEFINE statements
input_string = """
DEFINE QLOCAL('MY.QUEUE') REPLACE
DEFINE CHANNEL('MY.CHANNEL') CHLTYPE(SVRCONN) MCAUSER('mqm')
DEFINE QREMOTE('MY.REMOTE.QUEUE') RNAME('REMOTE.QUEUE') RQMNAME('REMOTE.QUEUE.MANAGER')
DEFINE QUEUE('MY.QUEUE') MAXDEPTH(5000)
DEFINE QDEFINE('MY.DEFINE.QUEUE') REPLACE
DEFINE CHANNEL('MY.SECOND.CHANNEL') CHLTYPE(SVRCONN) MCAUSER('mqm2')
"""

# Regex pattern to match DEFINE statements for queues and channels
pattern = r"DEFINE\s+(Q\w+|CHANNEL)\('([^']+)'\)(.*)"

# Find all matches
matches = re.findall(pattern, input_string)

# Prepare SQL for inserting data
insert_query = """
INSERT INTO mq_definitions (Type, Name, REPLACE, CHLTYPE, MCAUSER, RNAME, RQMNAME, MAXDEPTH)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

# Insert each match into the database
for type_, name, properties in matches:
    # Extract additional properties
    additional_props = re.findall(r"(\w+)\s*=\s*('.*?'|[^ ]+)", properties)
    properties_dict = {name.strip(): value.strip("'") for name, value in additional_props}
    
    # Prepare the data for insertion
    data = {
        'Type': type_,
        'Name': name,
        'REPLACE': properties_dict.get('REPLACE', ''),
        'CHLTYPE': properties_dict.get('CHLTYPE', ''),
        'MCAUSER': properties_dict.get('MCAUSER', ''),
        'RNAME': properties_dict.get('RNAME', ''),
        'RQMNAME': properties_dict.get('RQMNAME', ''),
        'MAXDEPTH': properties_dict.get('MAXDEPTH', None)
    }

    # Execute the insert statement
    cursor.execute(insert_query, (
        data['Type'], data['Name'], data['REPLACE'],
        data['CHLTYPE'], data['MCAUSER'], 
        data['RNAME'], data['RQMNAME'], 
        data['MAXDEPTH']
    ))

# Commit changes and close the connection
conn.commit()
conn.close()