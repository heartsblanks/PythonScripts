import os
import logging
import socket

class CheckConnections:
    def __init__(self):
        pass
    
    def check_git_connection(self):
        try:
            os.system("git ls-remote")
            logging.info("Git connection successful")
        except:
            message = "Could not connect to Git. Please check your internet connection and Git configuration."
            logging.error(message)
            raise Exception(message)
    
    def check_cvs_connection(self):
        cvs_host = "cvs.example.com"
        cvs_port = 2401
        try:
            socket.create_connection((cvs_host, cvs_port), timeout=5)
            logging.info("CVS connection successful")
        except:
            message = "Could not connect to CVS. Please check your internet connection and CVS configuration."
            logging.error(message)
            raise Exception(message)
    
    def check_command(self, command):
        try:
            os.system(command)
            logging.info(f"Command '{command}' successful")
        except:
            message = f"Command '{command}' failed. Please check that it is installed and on the PATH."
            logging.error(message)
            raise Exception(message)
