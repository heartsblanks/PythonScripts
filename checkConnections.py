import subprocess

class checkConnections:
    def __init__(self):
        pass

    def check_git_connection(self):
        try:
            subprocess.check_call(["git", "--version"])
            return True
        except subprocess.CalledProcessError:
            return False

    def check_cvs_connection(self):
        try:
            subprocess.check_call(["cvs", "--version"])
            return True
        except subprocess.CalledProcessError:
            return False

    def check_command(self, command):
        try:
            subprocess.check_call(command)
            return True
        except subprocess.CalledProcessError:
            return False
