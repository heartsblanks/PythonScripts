import tkinter as tk
from tkinter import ttk
import hashlib

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

        # Create Password update button
        password_update_button = ttk.Button(self.system_options_window, text="Password update", command=self.passwordUpdate, style="SystemButton.TButton")
        password_update_button.pack(fill="x", padx=10, pady=5)


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

        # Perform installation
        print(f"Performing {system_type} installation for {install_type} with the following options:")
        print(f"- Unattended installation: {installation_type}")
        print(f"- HB Password: {encrypted_hb_password}")
        if install_type in ["IIB10", "ACE12"]:
            print(f"- Reboot Automatically: {auto_reboot}")
            print(f"- HO Password: {encrypted_ho_password}")
            
           
        print(f"- Repository update type: {repo_update}")

        # Close window
        self.system_setup_options_window.destroy()


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
        print(f"Storing HB password: {encrypted_hb_password}")
        print(f"Storing HO password: {encrypted_ho_password}")

        # Close window
        self.password_update_window.destroy()

root = tk.Tk()
InstallOrchestration(root)
root.mainloop()
