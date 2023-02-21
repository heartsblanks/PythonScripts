import os
import json
import logging

json_file = 'data.json'

with open(json_file, 'r') as file:
    data = json.load(file)

class Constants:
    def __init__(self, env_type):
        if env_type in ['IIB10', 'ACE12', 'EAI', 'ETL', 'DS', 'GIT', 'CVS', 'MAVEN', 'Common']:
            self.env_type = env_type
            for item in data[env_type]:
                if item['Type'] == 'E':
                    try:
                        if os.path.isabs(item['Value']):
                            if os.path.isdir(item['Value']) or os.path.isfile(item['Value']):
                                os.environ[item['Name']] = item['Value']
                                setattr(self, item['Name'], item['Value'])
                                if item['Path'] == 'Y':
                                    os.environ['PATH'] += os.pathsep + item['Value']
                            else:
                                raise ValueError(f"{item['Value']} is not a valid directory or file path.")
                        else:
                            os.environ[item['Name']] = item['Value']
                            setattr(self, item['Name'], item['Value'])
                    except Exception as e:
                        logging.error(str(e))
                elif item['Type'] == 'I':
                    try:
                        if os.path.isabs(item['Value']):
                            if os.path.isdir(item['Value']) or os.path.isfile(item['Value']):
                                setattr(self, item['Name'], item['Value'])
                                if item['Path'] == 'Y':
                                    os.environ['PATH'] += os.pathsep + item['Value']
                            else:
                                raise ValueError(f"{item['Value']} is not a valid directory or file path.")
                        else:
                            setattr(self, item['Name'], item['Value'])
                    except Exception as e:
                        logging.error(str(e))
        else:
            raise ValueError(f"{env_type} is not a valid environment type.")


from Constants import Constants
import logging

logging.basicConfig(filename='constants.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

try:
    constants = Constants('IIB10')
    print(constants.BROKER_URL)
    print(constants.MQ_HOST)
    print(constants.MQ_PORT)
except Exception as e:
    logging.error(str(e))
    print(str(e))
