import subprocess
import os

class CheckOutProjects:
    def __init__(self, system_type, git_repo, cvs_repo, ssh_key):
        self.system_type = system_type
        self.git_repo = git_repo
        self.cvs_repo = cvs_repo
        self.ssh_key = ssh_key

    def checkout(self):
        # Checkout Git project
        if self.git_repo:
            git_command = ["git", "clone", self.git_repo]
            git_env = os.environ.copy()
            git_env["GIT_SSH_COMMAND"] = f"ssh -i {self.ssh_key}"
            git_process = subprocess.run(git_command, env=git_env)
            if git_process.returncode != 0:
                print(f"Failed to checkout Git repository {self.git_repo}")
            else:
                print(f"Checked out Git repository {self.git_repo}")

        # Checkout CVS project
        if self.cvs_repo:
            if self.system_type == "EAI":
                cvs_command = ["cvs", "-d", self.cvs_repo, "login"]
            else:
                cvs_command = ["cvs", "-d", self.cvs_repo, "login", "-l", "DS"]
            cvs_env = os.environ.copy()
            cvs_env["CVS_RSH"] = f"ssh -i {self.ssh_key}"
            cvs_process = subprocess.run(cvs_command, env=cvs_env)
            if cvs_process.returncode != 0:
                print(f"Failed to log in to CVS repository {self.cvs_repo}")
                return

            if self.system_type == "EAI":
                cvs_command = ["cvs", "-d", self.cvs_repo, "co", "EAI"]
            else:
                cvs_command = ["cvs", "-d", self.cvs_repo, "co", "ETL"]
            cvs_env = os.environ.copy()
            cvs_env["CVS_RSH"] = f"ssh -i {self.ssh_key}"
            cvs_process = subprocess.run(cvs_command, env=cvs_env)
            if cvs_process.returncode != 0:
                print(f"Failed to checkout CVS repository {self.cvs_repo}")
            else:
                print(f"Checked out CVS repository {self.cvs_repo}")
