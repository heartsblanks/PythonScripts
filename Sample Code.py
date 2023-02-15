import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MyApp:
    def __init__(self):
        # create the main window and set its title
        self.root = tk.Tk()
        self.root.title("My App")

        # set the default values for options
        self.eai_option = None
        self.eai_password = None
        self.ui_option = None
        self.rut_option = None
        self.ra_option = None

        # create the main frame
        self.main_frame = ttk.Frame(self.root, padding="30 15 30 15")
        self.main_frame.grid(column=0, row=0, sticky="nsew")

        # create radio buttons for EAI and ETL options
        self.eai_radio = ttk.Radiobutton(self.main_frame, text="EAI", value="eai",
                                         command=self.show_eai_options)
        self.eai_radio.grid(column=0, row=0, sticky="w")
        self.etl_radio = ttk.Radiobutton(self.main_frame, text="ETL", value="etl")
        self.etl_radio.grid(column=0, row=1, sticky="w")

        # create a label to display the selected EAI option
        self.eai_label = ttk.Label(self.main_frame, text="")
        self.eai_label.grid(column=1, row=0, sticky="w")

        # create a button to submit the selected EAI password
        self.eai_submit = ttk.Button(self.main_frame, text="Submit",
                                     command=self.submit_eai_password)
        self.eai_submit.grid(column=2, row=0, sticky="w")

        # create a button to quit the app
        self.quit_button = ttk.Button(self.main_frame, text="Quit", command=self.root.quit)
        self.quit_button.grid(column=1, row=3, sticky="e")

        # set the main frame to expand to fill the window
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=1)

    def run(self):
        self.root.mainloop()

    def show_eai_options(self):
        # create a new window to display EAI options
        eai_window = tk.Toplevel(self.root)
        eai_window.title("EAI Options")

        # create radio buttons for IIB, ACE, and Password Update options
        iib_radio = ttk.Radiobutton(eai_window, text="IIB", value="iib", variable=self.eai_option)
        iib_radio.grid(column=0, row=0, sticky="w")
        ace_radio = ttk.Radiobutton(eai_window, text="ACE", value="ace", variable=self.eai_option)
        ace_radio.grid(column=0, row=1, sticky="w")
        pwd_radio = ttk.Radiobutton(eai_window, text="Password Update", value="pwd", variable=self.eai_option)
        pwd_radio.grid(column=0, row=2, sticky="w")

    def submit_eai_password(self):
        # create a new window to input the EAI password
        pwd_window = tk.Toplevel(self.root)
        pwd_window.title("EAI Password")

        # create labels and entry fields for HB password and HO password
        hb_label = ttk.Label(pwd_window, text="HB Password:")
        hb_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        self.hb_entry = ttk.Entry(pwd_window, show="*")
        self.hb_entry.grid(column=1, row=0)
        ho_label = ttk.Label(pwd_window, text="HO Password:")
        ho_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.ho_entry = ttk.Entry(pwd_window, show="*")
        self.ho_entry.grid(column=1, row=1)

        # create a button to submit the password and encrypt it
        pwd_submit = ttk.Button(pwd_window, text="Submit", command=self.encrypt_password)
        pwd_submit.grid(column=1, row=2)

def encrypt_password(self):
    # get the HB and HO passwords from the entry fields
    hb_password = self.hb_entry.get()
    ho_password = self.ho_entry.get()

    # check if both passwords are entered
    if hb_password == "" or ho_password == "":
        messagebox.showerror("Error", "Please enter both HB and HO passwords")
    else:
        # encrypt the passwords and store them in the object
        self.eai_password = "HB: " + hb_password + ", HO: " + ho_password
        messagebox.showinfo("Success", "Password stored")

def installation_setup(self):
    # create a new window for installation setup
    setup_window = tk.Toplevel(self.root)
    setup_window.title("Installation Setup")

    # create radio buttons and labels for unattended installation, repository update type, and reboot automatically
    ui_radio = ttk.Radiobutton(setup_window, text="Unattended Installation", value="ui", variable=self.ui_option)
    ui_radio.grid(column=0, row=0, sticky="w")
    rut_radio = ttk.Radiobutton(setup_window, text="Repository Update Type", value="rut", variable=self.rut_option)
    rut_radio.grid(column=0, row=1, sticky="w")
    ra_radio = ttk.Radiobutton(setup_window, text="Reboot Automatically", value="ra", variable=self.ra_option)
    ra_radio.grid(column=0, row=2, sticky="w")

    ui_label = ttk.Label(setup_window, text="Unattended Installation:")
    ui_label.grid(column=1, row=0, padx=5, pady=5, sticky="w")
    rut_label = ttk.Label(setup_window, text="Repository Update Type:")
    rut_label.grid(column=1, row=1, padx=5, pady=5, sticky="w")
    ra_label = ttk.Label(setup_window, text="Reboot Automatically:")
    ra_label.grid(column=1, row=2, padx=5, pady=5, sticky="w")

    # create a button to submit the setup options
    setup_submit = ttk.Button(setup_window, text="Submit", command=self.submit_setup)
    setup_submit.grid(column=1, row=3)

def submit_setup(self):
    # check if all options are selected
    if self.ui_option == None or self.rut_option == None or self.ra_option == None:
        messagebox.showerror("Error", "Please select all options")
    else:
        # call the installation_setup function with the selected options
        self.installation_setup(self.ui_option, self.rut_option, self.ra_option)
app = MyApp()
app.run()
