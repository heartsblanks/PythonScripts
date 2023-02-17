import os
import subprocess
import logging

class CheckOutProjects:
    def __init__(self, system_type):
        self.system_type = system_type
        self.log_file = "checkout.log"

    def checkout_projects(self):
        logging.basicConfig(filename=self.log_file, level=logging.DEBUG)

        try:
            logging.info(f"Starting checkout process for {self.system_type} projects")

            if self.system_type == "EAI":
                # Check out EAI project from CVS
                self.checkout_cvs_project("EAI")
            else:
                # Check out ETL projects from GIT
                self.checkout_git_project("DS")

            logging.info(f"Finished checkout process for {self.system_type} projects")
        except Exception as e:
            logging.error(f"Error checking out projects: {e}")
            raise

    def checkout_cvs_project(self, project_name):
        logging.info(f"Checking out {project_name} project from CVS")

        # Run CVS checkout command
        try:
            cmd = f"cvs checkout {project_name}"
            subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error checking out {project_name} project: {e}")
            raise

    def checkout_git_project(self, project_name):
        logging.info(f"Checking out {project_name} project from GIT")

        # Run GIT checkout command
        try:
            cmd = f"git clone git@github.com:myorg/{project_name}.git"
            subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error checking out {project_name} project: {e}")
            raise
