import os
import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox
import hashlib
import logging
from WorkspaceFunctions import WorkspaceUtils
from createVariables import createVariables
from checkConnections import checkConnections
from checkOutProjects import checkOutProjects
from installPlugins import installPlugins
from gui import InstallOrchestrationGUI
from passwordUpdate import PasswordUpdate
from systemSetupOptions import SystemSetupOptions
from installation import Installation
from progressBar import ProgressBar


# Set up logging
LOG_FILE = "install_orchestration.log"
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)


class InstallOrchestration:
    def __init__(self, master):
        self.master = master
        master.title("Install Orchestration")

        # Create EAI button
        self.create_system_button("EAI", ["IIB10", "ACE12"])

        # Create ETL button
        self.create_system_button("ETL", ["DS"])

    def create_system_button(self, system_name, options):
        # Create button
        button = ttk.Button(self.master, text=system_name, command=lambda: self.displaySystemOptions(system_name, options), style="SystemButton.TButton")
        button.pack(fill="x", padx=10, pady=10)
        logging.info(f"Created {system_name} button")

    def displaySystemOptions(self, system_type, options):
        # Create new top level window
        self.system_options_window = tk.Toplevel(self.master)
        self.system_options_window.title(f"{system_type} Options")

        # Set up custom styles for this window
        self.setup_system_options_styles()

        # Create buttons
        for option in options:
            button = ttk.Button(self.system_options_window, text=option, command=lambda option=option: self.displaySystemSetupOptions(system_type, option), style="SystemButton.TButton")
            button.pack(fill="x", padx=10, pady=5)
            logging.info(f"Added {option} button to {system_type} options window")

        # Create Password update button
        password_update_button = ttk.Button(self.system_options_window, text="Password update", command=self.passwordUpdate, style="SystemButton.TButton")
        password_update_button.pack(fill="x", padx=10, pady=5)
        logging.info(f"Added Password update button to {system_type} options window")

    def setup_system_options_styles(self):
        self.system_options_window.option_add("*Button.Background", "#4d4d4d")
        self.system_options_window.option_add("*Button.Foreground", "white")
        self.system_options_window.option_add("*Button.activeBackground", "#808080")
        self.system_options_window.option_add("*Button.activeForeground", "white")
        self.system_options_window.option_add("*Button.highlightThickness", 0)
        self.system_options_window.option_add("*Label.Background", "#d9d9d9")
        self.system_options_window.option_add("*Label.Foreground", "#4d4d4d")

    def passwordUpdate(self):
        password_updater = PasswordUpdate(self.master, self.system_options_window)
        password_updater.create_window()

    def displaySystemSetupOptions(self, system_type, install_type):
        system_setup_options = SystemSetupOptions(self.master, self.system_options_window, system_type, install_type)
        system_setup_options.create_window()

    def performInstallation(self, system_type, install_type, options):
    # Check workspace directory
    workspace_utils = WorkspaceUtils(install_type)
    workspace_utils.checkWorkspaceDirectory()

    # Create variables
    variables_creator = createVariables(system_type)
    variables_creator.createVariables()
    logging.info(f"Created variables for {system_type} {install_type}")

    # Check connections
    connections_checker = checkConnections(system_type, options)
    connections_checker.checkConnections()
    logging.info(f"Checked connections for {system_type} {install_type}")

    # Check out projects
    projects_checker = checkOutProjects(system_type)
    projects_checker.checkOutProjects()
    logging.info(f"Checked out projects for {system_type} {install_type}")

    # Install plugins
    plugins_installer = installPlugins(system_type)
    plugins_installer.installPlugins()
    logging.info(f"Installed plugins for {system_type} {install_type}")

    # Perform installation
    installer = Installation(system_type, install_type)
    installer.performInstallation()
    logging.info(f"Performed installation for {system_type} {install_type}")

        # Check connections
        connections_checker = checkConnections()
        connections_checker.checkMQConnections()

        # Check out projects
        projects_checker = checkOutProjects(install_type)
        projects_checker.checkoutProjects()

        # Install plugins
        plugins_installer = installPlugins(install_type)
        plugins_installer.installPlugins()

        # Create progress bar
        progress_bar = ProgressBar(self.master, "Installation Progress", 4)

        # Start installation
        install_process = Installation(system_type, install_type, options)
        install_process.install(progress_bar)

if __name__ == '__main__':
    root = tk.Tk()
    app = InstallOrchestration(root)
    root.mainloop()

