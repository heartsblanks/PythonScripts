import os
import re
import sqlite3  # Change this import for your specific database

# Connect to the database (adjust for your database setup)
conn = sqlite3.connect('mq_definitions.db')  # Change the database name if needed
cursor = conn.cursor()

# Directory containing the MQSC files
directory = 'mqsc_files'  # Change this to your directory path

# Regex pattern to match DEFINE statements for queues and channels
pattern = r"DEFINE\s+(Q\w+|CHANNEL)\('([^']+)'\)(.*)"

# Process each file in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.mqsc'):  # Ensure we're processing only MQSC files
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as file:
            input_string = file.read()

        # Find all matches
        matches = re.findall(pattern, input_string)

        # Insert each match into the database
        for type_, name, properties in matches:
            # Extract additional properties
            additional_props = re.findall(r"(\w+)\s*=\s*('.*?'|[^ ]+)", properties)
            properties_dict = {name.strip(): value.strip("'") for name, value in additional_props}

            # Add Type and Name to the properties dictionary
            properties_dict['Type'] = type_
            properties_dict['Name'] = name

            # Create dynamic insert statement
            columns = ', '.join(properties_dict.keys())
            placeholders = ', '.join(['?'] * len(properties_dict))
            insert_query = f"INSERT INTO mq_definitions ({columns}) VALUES ({placeholders})"

            # Execute the insert statement
            cursor.execute(insert_query, tuple(properties_dict.values()))

# Commit changes and close the connection
conn.commit()
conn.close()