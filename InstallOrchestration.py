import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import hashlib
import logging


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
        style = ttk.Style()
        style.configure("SystemButton.TButton", background="#4d4d4d", foreground="white", activebackground="#808080", activeforeground="white", highlightthickness=0)
        style.configure("SubmitButton.TButton", background="#4d4d4d", foreground="white", activebackground="#808080", activeforeground="white", highlightthickness=0)
        style.configure("QuitButton.TButton", background="#4d4d4d", foreground="white", activebackground="#808080", activeforeground="white", highlightthickness=0)
        style.configure("OptionLabel.TLabel", background="#d9d9d9", foreground="#4d4d4d")
        style.configure("Option.TEntry", background="white", foreground="#4d4d4d")
        style.configure("Option.TRadiobutton", background="#d9d9d9", foreground="#4d4d4d", highlightthickness=0)

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

    def displaySystemSetupOptions(self, system_type, install_type):
        # Create new top level window
        self.system_setup_options_window = tk.Toplevel(self.master)
        self.system_setup_options_window.title(f"{system_type} {install_type} Setup")

        # Set up custom styles for this window
        self.setup_system_setup_options_styles()

        # Create labels and options
        self.installation_type_var = self.create_label_and_options("Unattended installation", ["Yes", "No"])
        self.repo_update_var = self.create_label_and_options("Repository", ["Update", "Replace"])
        self.hb_password_entry = self.create_label_and_entry("HB Password")
        if install_type in ["IIB10", "ACE12"]:
            self.ho_password_entry = self.create_label_and_entry("HO Password")
            self.auto_reboot_var = self.create_label_and_options("Reboot Automatically", ["Yes", "No"])

        # Create submit button
        submit_button = ttk.Button(self.system_setup_options_window, text="Submit", command=lambda: self.performInstallation(system_type, install_type), style="SubmitButton.TButton")
        submit_button.pack(pady=10)

        # Create quit button
        quit_button = ttk.Button(self.system_setup_options_window, text="Quit", command=self.system_setup_options_window.destroy, style="QuitButton.TButton")
        quit_button.pack(pady=10)
        self.system_options_window.destroy()

    def setup_system_setup_options_styles(self):
        self.system_setup_options_window.option_add("*Button.Background", "#4d4d4d")
        self.system_setup_options_window.option_add("*Button.Foreground", "white")
        self.system_setup_options_window.option_add("*Button.activeBackground", "#808080")
        self.system_setup_options_window.option_add("*Button.activeForeground", "white")
        self.system_setup_options_window.option_add("*Button.highlightThickness", 0)
        self.system_setup_options_window.option_add("*Label.Background", "#d9d9d9")
        self.system_setup_options_window.option_add("*Label.Foreground", "#4d4d4d")

    def create_label_and_options(self, label_text, option_values):
        label = ttk.Label(self.system_setup_options_window, text=label_text, style="OptionLabel.TLabel")
        label.pack(pady=5)
        var = tk.StringVar(value=option_values[0])
        for option_value in option_values:
            radio = ttk.Radiobutton(self.system_setup_options_window, text=option_value, variable=var, value=option_value, style="Option.TRadiobutton")
            radio.pack()
        return var

    def create_label_and_entry(self, label_text):
        label = ttk.Label(self.system_setup_options_window, text=label_text, style="OptionLabel.TLabel")
        label.pack(pady=5)
        entry = ttk.Entry(self.system_setup_options_window, show="*", style="Option.TEntry")
        entry.pack()
        return entry
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
        self.checkWorkspaceDirectory(install_type)

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
def checkWorkspaceDirectory(self, install_type):
    version_file_path = f"C:/Workspaces/{install_type}/.metadata/version.ini"
    if not os.path.exists(version_file_path):
        self.workspace_options_window = tk.Toplevel(self.master)
        self.workspace_options_window.title(f"{install_type} Workspace")

        # Create label
        label = ttk.Label(self.workspace_options_window, text="Workspace has not been detected. Do you want to create a new workspace within the standard directory?", style="OptionLabel.TLabel")
        label.pack(pady=5)

        # Create yes button
        yes_button = ttk.Button(self.workspace_options_window, text="Yes", command=lambda: self.createNewWorkspace(install_type), style="SubmitButton.TButton")
        yes_button.pack(pady=10)

        # Create no button
        no_button = ttk.Button(self.workspace_options_window, text="No", command=lambda: self.getCustomWorkspace(install_type), style="QuitButton.TButton")
        no_button.pack(pady=10)

    def createNewWorkspace(self, install_type):
        workspace_path = f"C:/Workspaces/{install_type}"
        os.makedirs(workspace_path, exist_ok=True)
        version_file_path = f"{workspace_path}/.metadata/version.ini"
        if not os.path.exists(version_file_path):
            logging.error(f"Failed to create new workspace for {install_type}")
            return

        self.workspace_options_window.destroy()
    def getCustomWorkspace(self, install_type):
        # Create new top level window
        custom_workspace_window = tk.Toplevel(self.master)
        custom_workspace_window.title("Custom Workspace Location")

        # Set up custom styles for this window
        self.setup_custom_workspace_styles(custom_workspace_window)

        # Create label and entry
        label = ttk.Label(custom_workspace_window, text=f"Enter the location of the {install_type} workspace:", style="OptionLabel.TLabel")
        label.pack(pady=5)
        entry = ttk.Entry(custom_workspace_window, style="Option.TEntry")
        entry.pack()

        # Create submit button
        submit_button = ttk.Button(custom_workspace_window, text="Submit", command=lambda: self.checkCustomWorkspace(custom_workspace_window, entry.get(), install_type), style="SubmitButton.TButton")
        submit_button.pack(pady=10)

        # Create quit button
        quit_button = ttk.Button(custom_workspace_window, text="Quit", command=custom_workspace_window.destroy, style="QuitButton.TButton")
        quit_button.pack(pady=10)

    def checkCustomWorkspace(self, custom_workspace_window, workspace_path, install_type):
        if os.path.exists(os.path.join(workspace_path, install_type, ".metadata", "version.ini")):
            self.workspace_path = workspace_path
            custom_workspace_window.destroy()
            logging.info(f"Using custom workspace: {self.workspace_path}")
        else:
            messagebox.showerror("Error", f"{install_type} workspace not found at the provided location.")

    def passwordUpdate(self):
        # Create new top level window
        self.password_update_window = tk.Toplevel(self.master)
        self.password_update_window.title("Password Update")

        # Set up custom styles for this window
        self.setup_password_update_styles()

        # Create HB Password label and entry
        self.hb_password_label = ttk.Label(self.password_update_window, text="HB Password", style="OptionLabel.TLabel")
        self.hb_password_label.pack(pady=5)
        self.hb_password_entry = ttk.Entry(self.password_update_window, show="*", style="Option.TEntry")
        self.hb_password_entry.pack()

        # Create HO Password label and entry
        self.ho_password_label = ttk.Label(self.password_update_window, text="HO Password", style="OptionLabel.TLabel")
        self.ho_password_label.pack(pady=5)
        self.ho_password_entry = ttk.Entry(self.password_update_window, show="*", style="Option.TEntry")
        self.ho_password_entry.pack()

        # Create submit button
        submit_button = ttk.Button(self.password_update_window, text="Submit", command=self.encryptAndStorePassword, style="SubmitButton.TButton")
        submit_button.pack(pady=10)

        # Create quit button
        quit_button = ttk.Button(self.password_update_window, text="Quit", command=self.password_update_window.destroy, style="QuitButton.TButton")
        quit_button.pack(pady=10)


    def setup_password_update_styles(self):
        self.password_update_window.option_add("*Button.Background", "#4d4d4d")
        self.password_update_window.option_add("*Button.Foreground", "white")
        self.password_update_window.option_add("*Button.activeBackground", "#808080")
        self.password_update_window.option_add("*Button.activeForeground", "white")
        self.password_update_window.option_add("*Button.highlightThickness", 0)
        self.password_update_window.option_add("*Label.Background", "#d9d9d9")
        self.password_update_window.option_add("*Label.Foreground", "#4d4d4d")


    def encryptAndStorePassword(self):
        # Get passwords from form
        hb_password = self.hb_password_entry.get()
        ho_password = self.ho_password_entry.get()

        # Encrypt passwords
        encrypted_hb_password = hashlib.sha256(hb_password.encode()).hexdigest()
        encrypted_ho_password = hashlib.sha256(ho_password.encode()).hexdigest()

        # Store passwords (replace with appropriate code for your application)
        logging.info(f"Storing HB password: {encrypted_hb_password}")
        logging.info(f"Storing HO password: {encrypted_ho_password}")

        # Close window
        self.password_update_window.destroy()
     


root = tk.Tk()
InstallOrchestration(root)
root.mainloop()
