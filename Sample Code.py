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
        # create a new window for unattended installation options
        ui_window = tk.Toplevel(self.root)
        ui_window.title("Unattended Installation Options")

        # create radio buttons for Unattended Installation, Repository Update Type, and Reboot automatically options
        ui_label = ttk.Label(ui_window, text="Unattended Installation:")
        ui_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        ui_yes_radio = ttk.Radiobutton(ui_window, text="Yes", value="yes", variable=self.ui_option)
        ui_yes_radio.grid(column=1, row=0, sticky="w")
        ui_no_radio = ttk.Radiobutton(ui_window, text="No", value="no", variable=self.ui_option)
        ui_no_radio.grid(column=2, row=0, sticky="w")

        rut_label = ttk.Label(ui_window, text="Repository Update Type:")
        rut_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        rut_update_radio = ttk.Radiobutton(ui_window, text="Update", value="update", variable=self.rut_option)
        rut_update_radio.grid(column=1, row=1, sticky="w")
        rut_replace_radio = ttk.Radiobutton(ui_window, text="Replace", value="replace", variable=self.rut_option)
        rut_replace_radio.grid(column=2, row=1, sticky="w")

        ra_label = ttk.Label(ui_window, text="Reboot Automatically:")
        ra_label.grid(column=0, row=2, padx=5, pady=5, sticky="w")
        ra_yes_radio = ttk.Radiobutton(ui_window, text="Yes", value="yes", variable=self.ra_option)
        ra_yes_radio.grid(column=1, row=2, sticky="w")
        ra_no_radio = ttk.Radiobutton(ui_window, text="No", value="no", variable=self.ra_option)
        ra_no_radio.grid(column=2, row=2, sticky="w")

        # create a button to submit the options and a button to quit the window
        submit_button = ttk.Button(ui_window, text="Submit", command=self.installation_setup)
        submit_button.grid(column=1, row=3)
        quit_button = ttk.Button(ui_window, text="Quit", command=ui_window.destroy)
        quit_button.grid(column=2, row=3)

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
