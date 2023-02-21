import csv
import json

csv_file = 'data.csv'
json_file = 'data.json'

data = {'IIB10': {'Files': [], 'Directories': [], 'Variables': []}, 'EAI': {'Files': [], 'Directories': [], 'Variables': []},
        'ETL': {'Variables': []}, 'ACE12': {'Files': [], 'Directories': [], 'Variables': []},
        'DS': {'Variables': []}, 'GIT': {'Variables': []},
        'CVS': {'Variables': []}, 'MAVEN': {'Variables': []}, 'Common': {'Variables': []}}

column_types = {'IIB10': ['Files', 'Directories', 'Variables'], 'EAI': ['Files', 'Directories', 'Variables'],
                'ETL': ['Variables'], 'ACE12': ['Files', 'Directories', 'Variables'],
                'DS': ['Variables'], 'GIT': ['Variables'], 'CVS': ['Variables'], 'MAVEN': ['Variables'], 'Common': ['Variables']}

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for env_type, col_types in column_types.items():
            if row[env_type] == 'Y':
                for col_type in col_types:
                    if row[col_type] == 'Y':
                        data[env_type][col_type].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
                    elif not col_types.count('Directories') and not col_types.count('Files'):
                        data[env_type]['Variables'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})

with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)
