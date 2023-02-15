import tkinter as tk

class InstallOrchestration:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Installation Orchestration")
        
        # Top level window
        self.top_level_frame = tk.Frame(self.root)
        self.top_level_frame.pack(padx=10, pady=10)
        
        self.eai_etl_var = tk.StringVar(value="EAI")
        
        eai_etl_label = tk.Label(self.top_level_frame, text="Select EAI or ETL:")
        eai_etl_label.pack()
        
        eai_etl_radiobutton1 = tk.Radiobutton(self.top_level_frame, text="EAI", variable=self.eai_etl_var, value="EAI")
        eai_etl_radiobutton1.pack()
        
        eai_etl_radiobutton2 = tk.Radiobutton(self.top_level_frame, text="ETL", variable=self.eai_etl_var, value="ETL")
        eai_etl_radiobutton2.pack()
        
        submit_button = tk.Button(self.top_level_frame, text="Submit", command=self.submit)
        submit_button.pack(side="left")
        
        quit_button = tk.Button(self.top_level_frame, text="Quit", command=self.root.destroy)
        quit_button.pack(side="right")
        
        self.root.mainloop()
    
    def submit(self):
        if self.eai_etl_var.get() == "EAI":
            self.create_eai_window()
        elif self.eai_etl_var.get() == "ETL":
            self.create_etl_window()
    
    def create_eai_window(self):
        self.eai_window = tk.Toplevel(self.root)
        self.eai_window.title("EAI Installation")
        
        eai_label = tk.Label(self.eai_window, text="Select an option:")
        eai_label.pack()
        
        iib_radiobutton = tk.Radiobutton(self.eai_window, text="IIB10", variable=self.eai_etl_var, value="IIB10")
        iib_radiobutton.pack()
        
        ace_radiobutton = tk.Radiobutton(self.eai_window, text="ACE12", variable=self.eai_etl_var, value="ACE12")
        ace_radiobutton.pack()
        
        password_radiobutton = tk.Radiobutton(self.eai_window, text="Password Update", variable=self.eai_etl_var, value="Password Update")
        password_radiobutton.pack()
        
        submit_button = tk.Button(self.eai_window, text="Submit", command=self.get_eai_options)
        submit_button.pack(side="left")
        
        quit_button = tk.Button(self.eai_window, text="Quit", command=self.eai_window.destroy)
        quit_button.pack(side="right")
    
    def create_etl_window(self):
        self.etl_window = tk.Toplevel(self.root)
        self.etl_window.title("ETL Installation")
        
        etl_label = tk.Label(self.etl_window, text="Select an option:")
        etl_label.pack()
        
        setup_radiobutton = tk.Radiobutton(self.etl_window, text="Setup", variable=self.eai_etl_var, value="Setup")
        setup_radiobutton.pack()
        
        password_radiobutton = tk.Radiobutton(self.etl_window, text="Password Update", variable=self.eai_etl_var, value="Password Update")
        password_radiobutton.pack()
        
        submit_button = tk.Button(self.etl_window, text="Submit", command=self.get_etl_options)
        submit_button.pack(side="left")
        
        quit_button = tk.Button(self.etl_window, text="Quit", command=self.etl_window.destroy)
        quit_button.pack(side="right")
        
        def get_eai_options(self):
    self.eai_options_window = tk.Toplevel(self.root)
    self.eai_options_window.title("EAI Installation Options")
    
    installation_type_label = tk.Label(self.eai_options_window, text="Unattended Installation:")
    installation_type_label.pack()
    
    installation_type_var = tk.StringVar(value="No")
    installation_type_radiobutton1 = tk.Radiobutton(self.eai_options_window, text="Yes", variable=installation_type_var, value="Yes")
    installation_type_radiobutton1.pack()
    installation_type_radiobutton2 = tk.Radiobutton(self.eai_options_window, text="No", variable=installation_type_var, value="No")
    installation_type_radiobutton2.pack()
    
    repository_update_label = tk.Label(self.eai_options_window, text="Repository Update Type:")
    repository_update_label.pack()
    
    repository_update_var = tk.StringVar(value="Replace")
    repository_update_radiobutton1 = tk.Radiobutton(self.eai_options_window, text="Replace", variable=repository_update_var, value="Replace")
    repository_update_radiobutton1.pack()
    repository_update_radiobutton2 = tk.Radiobutton(self.eai_options_window, text="Update", variable=repository_update_var, value="Update")
    repository_update_radiobutton2.pack()
    
    reboot_label = tk.Label(self.eai_options_window, text="Reboot Automatically:")
    reboot_label.pack()
    
    reboot_var = tk.BooleanVar(value=False)
    reboot_checkbutton = tk.Checkbutton(self.eai_options_window, text="Yes", variable=reboot_var)
    reboot_checkbutton.pack()
    
    hb_password_label = tk.Label(self.eai_options_window, text="Enter HB Password:")
    hb_password_label.pack()
    
    hb_password_entry = tk.Entry(self.eai_options_window, show="*")
    hb_password_entry.pack()
    
    ho_password_label = tk.Label(self.eai_options_window, text="Enter HO Password:")
    ho_password_label.pack()
    
    ho_password_entry = tk.Entry(self.eai_options_window, show="*")
    ho_password_entry.pack()
    
    submit_button = tk.Button(self.eai_options_window, text="Submit", command=self.eai_options_window.destroy)
    submit_button.pack(side="left")
    
    quit_button = tk.Button(self.eai_options_window, text="Quit", command=self.eai_options_window.destroy)
    quit_button.pack(side="right")

def get_etl_options(self):
    self.etl_options_window = tk.Toplevel(self.root)
    self.etl_options_window.title("ETL Installation Options")
    
    installation_type_label = tk.Label(self.etl_options_window, text="Unattended Installation:")
    installation_type_label.pack()
    
    installation_type_var = tk.StringVar(value="No")
    installation_type_radiobutton1 = tk.Radiobutton(self.etl_options_window, text="Yes", variable=installation_type_var, value="Yes")
    installation_type_radiobutton1.pack()
    installation_type_radiobutton2 = tk.Radiobutton(self.etl_options_window, text="No", variable=installation_type_var, value="No")
    installation_type_radiobutton2.pack()
    
    repository_update_label = tk.Label(self.etl_options_window, text="Repository Update Type:")
    repository_update_label.pack()
    
    repository_update_var = tk.StringVar(value="Replace")
    repository_update_radiobutton1 = tk.Radiobutton(self.etl_options_window, text="Replace", variable=repository_update_var, value="Replace")
    repository_update_radiobutton1.pack()
    repository_update_radiobutton2 = tk.Radiobutton(self.etl_options_window, text="Update", variable=repository_update_var, value="Update")
    repository_update_radiobutton2.pack()
    
        hb_password_label = tk.Label(self.etl_options_window, text="Enter HB Password:")
    hb_password_label.pack()
    
    hb_password_entry = tk.Entry(self.etl_options_window, show="*")
    hb_password_entry.pack()
    
    submit_button = tk.Button(self.etl_options_window, text="Submit", command=self.etl_options_window.destroy)
    submit_button.pack(side="left")
    
    quit_button = tk.Button(self.etl_options_window, text="Quit", command=self.etl_options_window.destroy)
    quit_button.pack(side="right")

def password_update(self):
    self.password_window = tk.Toplevel(self.root)
    self.password_window.title("Password Update")
    
    old_password_label = tk.Label(self.password_window, text="Enter Old Password:")
    old_password_label.pack()
    
    old_password_entry = tk.Entry(self.password_window, show="*")
    old_password_entry.pack()
    
    new_password_label = tk.Label(self.password_window, text="Enter New Password:")
    new_password_label.pack()
    
    new_password_entry = tk.Entry(self.password_window, show="*")
    new_password_entry.pack()
    
    submit_button = tk.Button(self.password_window, text="Submit", command=self.password_window.destroy)
    submit_button.pack(side="left")
    
    quit_button = tk.Button(self.password_window, text="Quit", command=self.password_window.destroy)
    quit_button.pack(side="right")

def run(self):
    self.root.mainloop()

if name == "main":
install_orchestration = InstallOrchestration()
install_orchestration.run()


