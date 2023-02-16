import tkinter as tk
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
        # Set up custom styles
        self.master.option_add("*Button.Background", "#4d4d4d")
        self.master.option_add("*Button.Foreground", "white")
        self.master.option_add("*Button.activeBackground", "#808080")
        self.master.option_add("*Button.activeForeground", "white")
        self.master.option_add("*Button.highlightThickness", 0)
        self.master.option_add("*Label.Background", "#d9d9d9")
        self.master.option_add("*Label.Foreground", "#4d4d4d")
        self.master.option_add("*Radiobutton.Background", "#d9d9d9")
        self.master.option_add("*Radiobutton.Foreground", "#4d4d4d")
        self.master.option_add("*Radiobutton.highlightThickness", 0)
        self.master.option_add("*Entry.Background", "white")
        self.master.option_add("*Entry.Foreground", "#4d4d4d")
        self.master.option_add("*Entry.highlightThickness", 0)

    def create_system_button(self, system_name, options):
        # Create button
        button = tk.Button(self.master, text=system_name, command=lambda: self.displaySystemOptions(options), style="SystemButton.TButton")
        button.pack(fill="x", padx=10, pady=10)

    def displaySystemOptions(self, options):
        # Create new top level window
        self.system_options_window = tk.Toplevel(self.master)
        system_type = self.system_options_window.title(" ".join(options) + " Options")

        # Set up custom styles for this window
        self.setup_system_options_styles()

        # Create buttons
        for option in options:
            button = tk.Button(self.system_options_window, text=option, command=lambda option=option: self.displaySystemSetupOptions(system_type, option), style="SystemButton.TButton")
            button.pack(fill="x", padx=10, pady=5)

        # Create Password update button
        password_update_button = tk.Button(self.system_options_window, text="Password update", command=self.passwordUpdate, style="SystemButton.TButton")
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
        self.system_setup_options_window.title(system_type + " Setup Options")

        # Set up custom styles for this window
        self.setup_system_setup_options_styles()

        # Create labels and options
        self.installation_type_var = self.create_label_and_options("Unattended installation", ["Yes", "No"])
        self.hb_password_entry = self.create_label_and_entry("HB Password")
        self.repo_update_var = self.create_label_and_options("Repository", ["Update", "Replace"])

        # Create submit button
        submit_button = tk.Button(self.system_setup_options_window, text="Submit", command=lambda: self.performInstallation(system_type, install_type), style="SubmitButton.TButton")
        submit_button.pack(pady=10)

        # Create quit button
        quit_button = tk.Button(self.system_setup_options_window, text="Quit", command=self.system_setup_options_window.destroy, style="QuitButton.TButton")
        quit_button.pack(pady=10)

    def setup_system_setup_options_styles(self):
        self.system_setup_options_window.option_add("*Button.Background", "#4d4d4d")
        self.system_setup_options_window.option_add("*Button.Foreground", "white")
        self.system_setup_options_window.option_add("*Button.activeBackground", "#808080")
        self.system_setup_options_window.option_add("*Button.activeForeground", "white")
        self.system_setup_options_window.option_add("*Button.highlightThickness", 0)
        self.system_setup_options_window.option_add("*Label.Background", "#d9d9d9")
        self.system_setup_options_window.option_add("*Label.Foreground", "#4d4d4d")

    def create_label_and_options(self, label_text, option_values):
        label = tk.Label(self.system_setup_options_window, text=label_text, style="OptionLabel.TLabel")
        label.pack(pady=5)
        var = tk.StringVar(value=option_values[0])
        for option_value in option_values:
            radio = tk.Radiobutton(self.system_setup_options_window, text=option_value, variable=var, value=option_value, style="Option.TRadiobutton")
            radio.pack()
        return var

    def create_label_and_entry(self, label_text):
        label = tk.Label(self.system_setup_options_window, text=label_text, style="OptionLabel.TLabel")
        label.pack(pady=5)
        entry = tk.Entry(self.system_setup_options_window, show="*", style="Option.TEntry")
        entry.pack()
        return entry

    def performInstallation(self, system_type, install_type):
        # Get values from form
        installation_type = self.installation_type_var.get()
        hb_password = self.hb_password_entry.get()
        repo_update = self.repo_update_var.get()

        # Encrypt passwords
        encrypted_hb_password = hashlib.sha256(hb_password.encode()).hexdigest()

        # Perform installation
        print(f"Performing {system_type} installation for {install_type} with the following options:")
        print(f"- Unattended installation: {installation_type}")
        print(f"- HB Password: {encrypted_hb_password}")
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
        self.hb_password_label = tk.Label(self.password_update_window, text="HB Password", style="OptionLabel.TLabel")
        self.hb_password_label.pack(pady=5)
        self.hb_password_entry = tk.Entry(self.password_update_window, show="*", style="Option.TEntry")
        self.hb_password_entry.pack()

        # Create HO Password label and
        # entry
        self.ho_password_label = tk.Label(self.password_update_window, text="HO Password", style="OptionLabel.TLabel")
        self.ho_password_label.pack(pady=5)
        self.ho_password_entry = tk.Entry(self.password_update_window, show="*", style="Option.TEntry")
        self.ho_password_entry.pack()

        # Create submit button
        submit_button = tk.Button(self.password_update_window, text="Submit", command=self.encryptAndStorePassword, style="SubmitButton.TButton")
        submit_button.pack(pady=10)

        # Create quit button
        quit_button = tk.Button(self.password_update_window, text="Quit", command=self.password_update_window.destroy, style="QuitButton.TButton")
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
