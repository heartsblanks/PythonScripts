import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import hashlib
import logging
from WorkspaceFunctions import WorkspaceUtils
from createVariables import createVariables
from checkConnections import checkConnections
from checkOutProjects import checkOutProjects
from installPlugins import installPlugins


# Set up logging
LOG_FILE = "install_orchestration.log"
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)

class InstallOrchestration:
    def __init__(self, master):
        self.master = master
        master.title("Install Orchestration")

        # Set up styles
        self.setup_styles()

        # Create EAI button
        self.create_system_button("EAI", ["IIB10", "ACE12"])

        # Create ETL button
        self.create_system_button("ETL", ["DS"])

    def setup_styles(self):
        # Create custom styles
        custom_styles = {
            "SystemButton.TButton": {"background": "#4d4d4d", "foreground": "white", "activebackground": "#808080", "activeforeground": "white", "highlightthickness": 0},
            "SubmitButton.TButton": {"background": "#4d4d4d", "foreground": "white", "activebackground": "#808080", "activeforeground": "white", "highlightthickness": 0},
            "QuitButton.TButton": {"background": "#4d4d4d", "foreground": "white", "activebackground": "#808080", "activeforeground": "white", "highlightthickness": 0},
            "OptionLabel.TLabel": {"background": "#d9d9d9", "foreground": "#4d4d4d"},
            "Option.TEntry": {"background": "white", "foreground": "#4d4d4d"},
            "Option.TRadiobutton": {"background": "#d9d9d9", "foreground": "#4d4d4d", "highlightthickness": 0},
        }
        style = ttk.Style()
        for style_name, options in custom_styles.items():
            style.configure(style_name, **options)

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

    def passwordUpdate(self):
        # Create new top level window
        self.password_update_window = tk.Toplevel(self.master)
        self.password_update_window.title("Password Update")

        # Create labels and entries
        hb_password_label = ttk.Label(self.password_update_window, text="HB Password", style="OptionLabel.TLabel")
        hb_password_label.grid(row=0, column=0, pady=5)
        hb_password_entry = ttk.Entry(self.password_update_window, show="*", style="Option.TEntry")
        hb_password_entry.grid(row=0, column=1)

        ho_password_label = ttk.Label(self.password_update_window, text="HO Password", style="OptionLabel.TLabel")
        ho_password_label.grid(row=1, column=0, pady=5)
        ho_password_entry = ttk.Entry(self.password_update_window, show="*", style="Option.TEntry")
        ho_password_entry.grid(row=1, column=1)

        # Create submit button
        submit_button = ttk.Button(self.password_update_window, text="Submit", command=lambda: self.updatePasswords(hb_password_entry.get(), ho_password_entry.get()), style="SubmitButton.TButton")
        submit_button.grid(row=2, column=0, pady=10)

        # Create quit button
        quit_button = ttk.Button(self.password_update_window, text="Quit", command=self.password_update_window.destroy, style="QuitButton.TButton")
        quit_button.grid(row=2, column=1, pady=10)

    def updatePasswords(self, hb_password, ho_password):
        # Encrypt passwords
        encrypted_hb_password = hashlib.sha256(hb_password.encode()).hexdigest()
        encrypted_ho_password = hashlib.sha256(ho_password.encode()).hexdigest()

        # Update password files
        with open("hb_password.txt", "w") as f:
            f.write(encrypted_hb_password)
        with open("ho_password.txt", "w") as f:
            f.write(encrypted_ho_password)

        # Close window
        self.password_update_window.destroy()

    def performInstallation(self, system_type, install_type):
        # Get values from form
        installation_type = self.installation_type_var.get()
        if install_type in ["IIB10", "ACE12"]:
            auto_reboot = self.auto_reboot_var.get()
            ho_password = self.ho_password_entry.get()
        else:
            auto_reboot = "N/A"
            ho_password = "N/A"
        repo_update = self.repo_update_var.get()
        hb_password = self.hb_password_entry.get()

        # Encrypt passwords
        encrypted_hb_password = hashlib.sha256(hb_password.encode()).hexdigest()
        encrypted_ho_password = hashlib.sha256(ho_password.encode()).hexdigest()

        # Check workspace directory
        workspace_utils = WorkspaceUtils(install_type)
        workspace_utils.checkWorkspaceDirectory()

        # Create variables
        variables_creator = createVariables(system_type)
        variables_creator.create()
        
        # Check connections
        connections_checker = checkConnections()
        connections_checker.check()

        # Check out projects
        projects_checker = checkOutProjects(system_type)
        projects_checker.checkOut()

        # Install plugins
        plugin_installer = installPlugins(system_type)
        plugin_installer.install_iib_toolkit_plugin()
        plugin_installer.install_ace_toolkit_plugin()
        plugin_installer.install_eclipse_plugin()
        plugin_installer.install_maven_cli()
        plugin_installer.install_jre()
        plugin_installer.install_maven_plugin()

        # Perform installation
        logging.info(f"Performing {system_type} installation for {install_type} with the following options:")
        logging.info(f"- Unattended installation: {installation_type}")
        logging.info(f"- HB Password: {encrypted_hb_password}")
        if install_type in ["IIB10", "ACE12"]:
            logging.info(f"- Reboot Automatically: {auto_reboot}")
            logging.info(f"- HO Password: {encrypted_ho_password}")
        logging.info(f"- Repository update type: {repo_update}")

        # Close window
        self.system_setup_options_window.destroy()

        
        
root = tk.Tk()
InstallOrchestration(root)
root.mainloop()        
