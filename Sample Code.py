import csv
import json

csv_file = 'data.csv'
json_file = 'data.json'

data = {'IIB10': [], 'EAI': [], 'ETL': [], 'ACE12': [], 'DS': [], 'GIT': [], 'CVS': [], 'MAVEN': [], 'Common': []}

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['IIB10'] == 'Y':
            data['IIB10'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['EAI'] == 'Y':
            data['EAI'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['ETL'] == 'Y':
            data['ETL'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['ACE12'] == 'Y':
            data['ACE12'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['DS'] == 'Y':
            data['DS'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['GIT'] == 'Y':
            data['GIT'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['CVS'] == 'Y':
            data['CVS'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['MAVEN'] == 'Y':
            data['MAVEN'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})
        if row['Common'] == 'Y':
            data['Common'].append({'Name': row['Name'], 'Value': row['Value'], 'Type': row['Type'], 'Path': row['Path']})

with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)
