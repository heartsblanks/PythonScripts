import os
import csv
from tkinter import messagebox
from tkinter import filedialog
import logging

class createVariables:
    def __init__(self, system_type):
        self.system_type = system_type
        self.logger = logging.getLogger(__name__)

    def create(self):
        try:
            with open("variable_details.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == "Y" and self.system_type == "EAI":
                        self.create_variable(row)
                    elif row[1] == "Y" and self.system_type == "ETL":
                        self.create_variable(row)
        except Exception as e:
            self.logger.error(f"Error while reading variable_details.csv: {str(e)}")
            raise e

    def create_variable(self, row):
        var_name = row[2]
        var_value = row[3]
        update_path = row[4]
        var_type = row[5]

        try:
            if update_path == "Y":
                if os.path.isabs(var_value):
                    if os.path.exists(var_value):
                        os.environ["PATH"] += ";" + var_value
                    else:
                        self.show_error_message(row)
                        self.logger.error(f"Variable {var_name} could not be created. {var_value} is not a valid path.")
                else:
                    os.environ["PATH"] += ";" + var_value

            if var_type == "E":
                if os.path.isabs(var_value):
                    if os.path.exists(var_value):
                        os.environ[var_name] = var_value
                        self.__dict__[var_name] = var_value
                    else:
                        self.show_error_message(row)
                        self.logger.error(f"Variable {var_name} could not be created. {var_value} is not a valid path.")
                else:
                    os.environ[var_name] = var_value
                    self.__dict__[var_name] = var_value

            elif var_type == "I":
                if os.path.isabs(var_value):
                    if os.path.exists(var_value):
                        self.__dict__[var_name] = var_value
                    else:
                        self.show_error_message(row)
                        self.logger.error(f"Variable {var_name} could not be created. {var_value} is not a valid path.")
                else:
                    self.__dict__[var_name] = var_value
        except Exception as e:
            self.logger.error(f"Error while creating variable {var_name}: {str(e)}")
            raise e

    def show_error_message(self, row):
        message = f"Could not create variable for {row[2]} with value {row[3]}. Please update the variable_details.csv file with a valid path."
        result = messagebox.askyesno("Error", message)
        if result:
            file_path = filedialog.askopenfilename(initialdir=".", title="Select CSV file", filetypes=[("CSV files", "*.csv")])
            os.startfile(file_path)
        else:
            raise Exception(message)
