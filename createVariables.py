import os
import csv

class createVariables:
    def __init__(self, system_type):
        self.system_type = system_type

    def create(self):
        with open("variable_details.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "Y" and self.system_type == "EAI":
                    self.create_variable(row)
                elif row[1] == "Y" and self.system_type == "ETL":
                    self.create_variable(row)

    def create_variable(self, row):
        var_name = row[2]
        var_value = row[3]
        update_path = row[4]
        var_type = row[5]

        if update_path == "Y":
            os.environ["PATH"] += ";" + var_value

        if var_type == "E":
            os.environ[var_name] = var_value
            self.__dict__[var_name] = var_value
        elif var_type == "I":
            self.__dict__[var_name] = var_value

