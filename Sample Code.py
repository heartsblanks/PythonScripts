import tkinter as tk
from cryptography.fernet import Fernet

class PasswordUpdateWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Password Update")
        self.hb_password = tk.StringVar()
        self.ho_password = tk.StringVar()
        
        tk.Label(self, text="HB Password").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.hb_password, show="*").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="HO Password").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.ho_password, show="*").grid(row=1, column=1, padx=5, pady=5)
        
        submit_button = tk.Button(self, text="Submit", command=self.submit_passwords)
        submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
    def submit_passwords(self):
        hb_password = self.hb_password.get().encode()
        ho_password = self.ho_password.get().encode()
        
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_hb_password = f.encrypt(hb_password)
        encrypted_ho_password = f.encrypt(ho_password)
        
        self.master.passwords = {"hb_password": encrypted_hb_password, "ho_password": encrypted_ho_password}
        self.destroy()

class InstallOrchestration:
    def __init__(self, master):
        self.master = master
        self.master.title("Install Orchestration")
        
        self.option_var = tk.StringVar()
        self.eai_options = ["IIB10", "ACE12", "Password Update"]
        self.etl_options = ["Password Update"]
        
        tk.Label(self.master, text="Choose an option:").grid(row=0, column=0, padx=5, pady=5)
        
        tk.Radiobutton(self.master, text="EAI", variable=self.option_var, value="EAI").grid(row=1, column=0, padx=5, pady=5)
        tk.Radiobutton(self.master, text="ETL", variable=self.option_var, value="ETL").grid(row=2, column=0, padx=5, pady=5)
        
        submit_button = tk.Button(self.master, text="Submit", command=self.show_next_window)
        submit_button.grid(row=3, column=0, padx=5, pady=5)
        
    def show_next_window(self):
        option = self.option_var.get()
        
        if option == "EAI":
            EAIWindow(self.master, self.eai_options)
        elif option == "ETL":
            PasswordUpdateWindow(self.master)

class EAIWindow(tk.Toplevel):
    def __init__(self, master, options):
        super().__init__(master)
        self.title("EAI Options")
        
        self.unattended_var = tk.StringVar(value="yes")
        self.update_type_var = tk.StringVar(value="Replace")
        self.reboot_var = tk.StringVar(value="yes")
        self.hb_password = tk.StringVar()
        self.ho_password = tk.StringVar()
        
        tk.Label(self, text="Unattended").grid(row=0, column=0, padx=5, pady=5)
        tk.OptionMenu(self, self.unattended_var, "yes", "no").grid(row=0, column=1
        tk.Label(self, text="Repository Update Type").grid(row=1, column=0, padx=5, pady=5)
        tk.OptionMenu(self, self.update_type_var, "Replace", "Update").grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Reboot Automatically").grid(row=2, column=0, padx=5, pady=5)
        tk.OptionMenu(self, self.reboot_var, "yes", "no").grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self, text="HB Password").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.hb_password, show="*").grid(row=3, column=1, padx=5, pady=5)
        tk.Label(self, text="HO Password").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.ho_password, show="*").grid(row=4, column=1, padx=5, pady=5)
        
        submit_button = tk.Button(self, text="Submit", command=self.submit_values)
        submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
    def submit_values(self):
        unattended = self.unattended_var.get()
        update_type = self.update_type_var.get()
        reboot = self.reboot_var.get()
        
        hb_password = self.hb_password.get().encode()
        ho_password = self.ho_password.get().encode()
        
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_hb_password = f.encrypt(hb_password)
        encrypted_ho_password = f.encrypt(ho_password)
        
        self.master.eai_values = {
            "unattended": unattended,
            "update_type": update_type,
            "reboot": reboot,
            "hb_password": encrypted_hb_password,
            "ho_password": encrypted_ho_password
        }
        
        self.destroy()

# create the main window and run the program
root = tk.Tk()
InstallOrchestration(root)
root.mainloop()
