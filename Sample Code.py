import tkinter as tk
from tkinter import messagebox, ttk


class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")
        self.root.geometry("400x300")

        # initialize variables to store user selections
        self.eai_option = None
        self.ui_option = None
        self.rut_option = None
        self.ra_option = None
        self.eai_password = None

        # create radio buttons for EAI and ETL options
        eai_radio = ttk.Radiobutton(self.root, text="EAI", value="eai", variable=self.eai_option, command=self.show_eai_options)
        eai_radio.grid(column=0, row=0, sticky="w")
        etl_radio = ttk.Radiobutton(self.root, text="ETL", value="etl", variable=self.eai_option)
        etl_radio.grid(column=1, row=0, sticky="w")

        # create a button to quit the application
        quit_button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        quit_button.grid(column=1, row=4)

        self.root.mainloop()

    def show_eai_options(self):
        # create a new window for EAI options
        eai_window = tk.Toplevel(self.root)
        eai_window.title("EAI Options")

        # create radio buttons for IIB, ACE, and Password Update options
        iib_radio = ttk.Radiobutton(eai_window, text="IIB", value="iib", variable=self.eai_option, command=self.dummy_function)
        iib_radio.grid(column=0, row=0, sticky="w")
        ace_radio = ttk.Radiobutton(eai_window, text="ACE", value="ace", variable=self.eai_option, command=self.dummy_function)
        ace_radio.grid(column=1, row=0, sticky="w")
        pwd_radio = ttk.Radiobutton(eai_window, text="Password Update", value="pwd", variable=self.eai_option, command=self.show_password_input)
        pwd_radio.grid(column=2, row=0, sticky="w")

        # create a button to submit the options and a button to quit the window
        submit_button = ttk.Button(eai_window, text="Submit", command=eai_window.destroy)
        submit_button.grid(column=1, row=1)
        quit_button = ttk.Button(eai_window, text="Quit", command=eai_window.destroy)
        quit_button.grid(column=2, row=1)

    def show_password_input(self):
        # create a new window for password input
        pwd_window = tk.Toplevel(self.root)
        pwd_window.title("Password Input")

        # create entry fields and labels for HB and HO passwords
        hb_label = ttk.Label(pwd_window, text="HB Password:")
        hb_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        self.hb_entry = ttk.Entry(pwd_window, show="*")
        self.hb_entry.grid(column=1, row=0)

        ho_label = ttk.Label(pwd_window, text="HO Password:")
        ho_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.ho_entry = ttk.Entry(pwd_window, show="*")
        self.ho_entry.grid(column=1, row=1)

        # create a button to submit the password and encrypt it, and a button to quit the window
                pwd_submit = ttk.Button(pwd_window, text="Submit", command=self.encrypt_password)
        pwd_submit.grid(column=1, row=2)
        quit_button = ttk.Button(pwd_window, text="Quit", command=pwd_window.destroy)
        quit_button.grid(column=2, row=2)

    def encrypt_password(self):
        # get the password input and encrypt it
        hb_pwd = self.hb_entry.get()
        ho_pwd = self.ho_entry.get()

        if hb_pwd and ho_pwd:
            # encrypt the passwords
            self.eai_password = self.dummy_encrypt(hb_pwd) + self.dummy_encrypt(ho_pwd)
            messagebox.showinfo("Success", "Password has been encrypted and stored.")
        else:
            messagebox.showerror("Error", "Please enter both HB and HO passwords.")

    def dummy_function(self):
        # Create the pop-up window for installation options
        self.options_window = tk.Toplevel()
        self.options_window.title("Installation Options")

        # Create the Unattended Installation label and radio buttons
        ui_label = tk.Label(self.options_window, text="Unattended Installation:")
        ui_label.pack()
        self.ui_var = tk.StringVar(value="No")
        ui_yes_button = tk.Radiobutton(self.options_window, text="Yes", variable=self.ui_var, value="Yes")
        ui_yes_button.pack()
        ui_no_button = tk.Radiobutton(self.options_window, text="No", variable=self.ui_var, value="No")
        ui_no_button.pack()

        # Create the Repository Update Type label and radio buttons
        repo_label = tk.Label(self.options_window, text="Repository Update Type:")
        repo_label.pack()
        self.repo_var = tk.StringVar(value="Update")
        repo_update_button = tk.Radiobutton(self.options_window, text="Update", variable=self.repo_var, value="Update")
        repo_update_button.pack()
        repo_replace_button = tk.Radiobutton(self.options_window, text="Replace", variable=self.repo_var, value="Replace")
        repo_replace_button.pack()

        # Create the Reboot Automatically label and radio buttons
        ra_label = tk.Label(self.options_window, text="Reboot Automatically:")
        ra_label.pack()
        self.ra_var = tk.StringVar(value="No")
        ra_yes_button = tk.Radiobutton(self.options_window, text="Yes", variable=self.ra_var, value="Yes")
        ra_yes_button.pack()
        ra_no_button = tk.Radiobutton(self.options_window, text="No", variable=self.ra_var, value="No")
        ra_no_button.pack()

        # Create the Submit and Quit buttons
        submit_button = tk.Button(self.options_window, text="Submit", command=self.installation_setup)
        submit_button.pack(side="left")
        quit_button = tk.Button(self.options_window, text="Quit", command=self.options_window.destroy)
        quit_button.pack(side="right")

        # Wait for user input
        self.options_window.wait_window()


    def installation_setup(self):
        # print out the selected options
        print("EAI Option:", self.eai_option)
        print("Unattended Installation Option:", self.ui_option)
        print("Repository Update Type:", self.rut_option)
        print("Reboot Automatically:", self.ra_option)

    @staticmethod
    def dummy_encrypt(password):
        # just add an 'x' at
        encrypted = "x" + password + "x"
        return encrypted
if __name__ == "__main__":
    app = Application()
    app.run()
