import tkinter as tk
from tkinter import messagebox


class ApplicationInstaller:
    COLOR_PRIMARY = "#2196F3"
    COLOR_SECONDARY = "#FFFFFF"
    FONT_SMALL = ("Arial", 10)
    FONT_MEDIUM = ("Arial", 12)
    FONT_LARGE = ("Arial", 14)

    def __init__(self):
        self.top_level_window = tk.Tk()
        self.top_level_window.title("Application Installer")
        self.top_level_window.geometry("400x400")

        self.create_buttons()

    def create_buttons(self):
        """Create buttons for EAI and ETL"""
        # Create button for EAI
        self.eai_button = tk.Button(
            self.top_level_window,
            text="EAI",
            command=self.display_eai_options,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        self.eai_button.pack(pady=10)

        # Create button for ETL
        self.etl_button = tk.Button(
            self.top_level_window,
            text="ETL",
            command=self.display_etl_options,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        self.etl_button.pack(pady=10)

    def display_eai_options(self):
        """Display options for setting up EAI"""
        # Create new top level window for EAI options
        eai_options_window = tk.Toplevel(self.top_level_window)
        eai_options_window.title("EAI Options")
        eai_options_window.geometry("400x400")

        # Create button for IIB10 setup
        iib10_button = tk.Button(
            eai_options_window,
            text="IIB 10",
            command=self.display_eai_setup_options,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        iib10_button.pack(pady=10)

        # Create button for ACE12 setup
        ace12_button = tk.Button(
            eai_options_window,
            text="ACE 12",
            command=self.display_eai_setup_options,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        ace12_button.pack(pady=10)

        # Create button for EAI password update
        password_update_button = tk.Button(
            eai_options_window,
            text="Password Update",
            command=self.display_eai_password_update,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        password_update_button.pack(pady=10)

        self.top_level_window.destroy()
    def display_eai_setup_options(self):
        """Display options for setting up EAI"""
        # Create new top level window for EAI setup options
        eai_setup_window = tk.Toplevel(self.top_level_window)
        eai_setup_window.title("EAI Setup Options")
        eai_setup_window.geometry("400x400")

        # Create label and radio buttons for installation type
        installation_type_label = tk.Label(
            eai_setup_window,
            text="Unattended Installation:",
            font=self.FONT_MEDIUM,
        )
        installation_type_label.grid(row=0, column=0, pady=10)

        self.installation_type_var = tk.StringVar()
        self.installation_type_var.set("No")

        installation_type_yes = tk.Radiobutton(
            eai_setup_window,
            text="Yes",
            variable=self.installation_type_var,
            value="Yes",
            font=self.FONT_SMALL,
        )
        installation_type_yes.grid(row=1, column=0, pady=10)

        installation_type_no = tk.Radiobutton(
            eai_setup_window,
            text="No",
            variable=self.installation_type_var,
            value="No",
            font=self.FONT_SMALL,
        )
        installation_type_no.grid(row=2, column=0, pady=10)
        # Create label and radio buttons for auto reboot
        auto_reboot_label = tk.Label(
            eai_setup_window,
            text="Reboot Automatically:",
            font=self.FONT_MEDIUM,
        )
        auto_reboot_label.grid(row=3, column=0, pady=10)

        self.auto_reboot_var = tk.StringVar()
        self.auto_reboot_var.set("No")

        auto_reboot_yes = tk.Radiobutton(
            eai_setup_window,
            text="Yes",
            variable=self.auto_reboot_var,
            value="Yes",
            font=self.FONT_SMALL,
        )
        auto_reboot_yes.grid(row=4, column=0, pady=10)

        auto_reboot_no = tk.Radiobutton(
            eai_setup_window,
            text="No",
            variable=self.auto_reboot_var,
            value="No",
            font=self.FONT_SMALL,
        )
        auto_reboot_no.grid(row=5, column=0, pady=10)
        # Create label and entry box for HB password
        hb_password_label = tk.Label(
            eai_setup_window,
            text="HB Password:",
            font=self.FONT_MEDIUM,
        )
        hb_password_label.grid(row=6, column=0, pady=10)

        self.hb_password_entry = tk.Entry(
            eai_setup_window,
            show="*",
            font=self.FONT_SMALL,
        )
        self.hb_password_entry.grid(row=7, column=0, pady=10)
        # Create label and entry box for HO password
        ho_password_label = tk.Label(
            eai_setup_window,
            text="HO Password:",
            font=self.FONT_MEDIUM,
        )
        ho_password_label.grid(row=8, column=0, pady=10)

        self.ho_password_entry = tk.Entry(
            eai_setup_window,
            show="*",
            font=self.FONT_SMALL,
        )
        self.ho_password_entry.grid(row=9, column=0, pady=10)
        # Create label and radio buttons for repository update
        repo_update_label = tk.Label(
            eai_setup_window,
            text="Repository:",
            font=self.FONT_MEDIUM,
        )
        repo_update_label.grid(row=10, column=0, pady=10)

        self.repo_update_var = tk.StringVar()
        self.repo_update_var.set("Update")

        repo_update_update = tk.Radiobutton(
            eai_setup_window,
            text="Update",
            variable=self.repo_update_var,
            value="Update",
            font=self.FONT_SMALL,
        )
        repo_update_update.grid(row=11, column=0, pady=10)
        repo_update_replace = tk.Radiobutton(
            eai_setup_window,
            text="Replace",
            variable=self.repo_update_var,
            value="Replace",
            font=self.FONT_SMALL,
        )
        repo_update_replace.grid(row=12, column=0, pady=10)

        # Create button for submitting EAI setup options
        submit_button = tk.Button(
            eai_setup_window,
            text="Install",
            command=self.install_eai_setup,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        submit_button.grid(row=13, column=0, pady=10)
        # Create button for quitting EAI setup options
        quit_button = tk.Button(
            eai_setup_window,
            text="Quit",
            command=eai_setup_window.destroy,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        quit_button.grid(row=14, column=0, pady=10)

    def install_eai_setup(self):
        """Install EAI setup with user-selected options"""
        try:
            # Get user-selected options
            installation_type = self.installation_type_var.get()
            auto_reboot = self.auto_reboot_var.get()
            hb_password = self.hb_password_entry.get()
            ho_password = self.ho_password_entry.get()
            repo_update = self.repo_update_var.get()

            # TODO: Install EAI setup with selected options
            messagebox.showinfo("Success", "EAI setup installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def display_etl_options(self):
        """Display options for ETL"""
        # Create new top level window for ETL options
        etl_options_window = tk.Toplevel(self.top_level_window)
        etl_options_window.title("ETL Options")
        etl_options_window.geometry("400x400")

        # Create button for DataStage
        datastage_button = tk.Button(
            etl_options_window,
            text="DataStage",
            command=self.display_etl_setup_options,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        datastage_button.grid(row=0, column=0, pady=10)
        # Create button for password update
        password_update_button = tk.Button(
            etl_options_window,
            text="Password Update",
            command=self.password_update,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        password_update_button.grid(row=1, column=0, pady=10)

        # Create button for quitting ETL options
        quit_button = tk.Button(
            etl_options_window,
            text="Quit",
            command=etl_options_window.destroy,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        quit_button.grid(row=2, column=0, pady=10)
    def display_etl_setup_options(self):
        """Display options for ETL setup"""
        # Create new top level window for ETL setup options
        etl_setup_window = tk.Toplevel(self.top_level_window)
        etl_setup_window.title("ETL Setup Options")
        etl_setup_window.geometry("400x400")

        # Create label and radio buttons for installation type
        installation_type_label = tk.Label(
            etl_setup_window,
            text="Unattended Installation:",
            font=self.FONT_MEDIUM,
        )
        installation_type_label.grid(row=0, column=0, pady=10)

        self.installation_type_var = tk.StringVar()
        self.installation_type_var.set("Yes")

        installation_type_yes = tk.Radiobutton(
            etl_setup_window,
            text="Yes",
            variable=self.installation_type_var,
            value="Yes",
            font=self.FONT_SMALL,
        )
        installation_type_yes.grid(row=1, column=0, pady=10)
        installation_type_no = tk.Radiobutton(
            etl_setup_window,
            text="No",
            variable=self.installation_type_var,
            value="No",
            font=self.FONT_SMALL,
        )
        installation_type_no.grid(row=2, column=0, pady=10)

        # Create label and entry box for HB password
        hb_password_label = tk.Label(
            etl_setup_window,
            text="HB Password:",
            font=self.FONT_MEDIUM,
        )
        hb_password_label.grid(row=3, column=0, pady=10)

        self.hb_password_entry = tk.Entry(
            etl_setup_window,
            show="*",
            font=self.FONT_SMALL,
        )
        self.hb_password_entry.grid(row=4, column=0, pady=10)

        # Create label and radio buttons for repository update
        repo_update_label = tk.Label(
            etl_setup_window,
            text="Repository:",
            font=self.FONT_MEDIUM,
        )
        repo_update_label.grid(row=5, column=0, pady=10)

        self.repo_update_var = tk.StringVar()
        self.repo_update_var.set("Update")

        repo_update_update = tk.Radiobutton(
            etl_setup_window,
            text="Update",
            variable=self.repo_update_var,
            value="Update",
            font=self.FONT_SMALL,
        )
        repo_update_update.grid(row=6, column=0, pady=10)
        repo_update_replace = tk.Radiobutton(
            etl_setup_window,
            text="Replace",
            variable=self.repo_update_var,
            value="Replace",
            font=self.FONT_SMALL,
        )
        repo_update_replace.grid(row=7, column=0, pady=10)

        # Create button for submitting ETL setup options
        submit_button = tk.Button(
            etl_setup_window,
            text="Install",
            command=self.install_etl_setup,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        submit_button.grid(row=8, column=0, pady=10)
        # Create button for quitting ETL setup options
        quit_button = tk.Button(
            etl_setup_window,
            text="Quit",
            command=etl_setup_window.destroy,
            width=20,
            height=2,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_SECONDARY,
            font=self.FONT_MEDIUM,
        )
        quit_button.grid(row=9, column=0, pady=10)

    def install_eai_setup(self):
        """Install EAI setup with selected options"""
        try:
            installation_type = self.installation_type_var.get()
            auto_reboot = self.auto_reboot_var.get()
            hb_password = self.hb_password_entry.get()
            repo_update = self.repo_update_var.get()

            # Validate input
            if not hb_password:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid HB password.",
                )
                return

            # Install EAI setup
            # ...

            # Show success message
            messagebox.showinfo(
                "Success",
                "EAI setup installed successfully.",
            )
        except Exception as e:
            # Show error message
            messagebox.showerror(
                "Error",
                f"An error occurred while installing EAI setup: {e}",
            )

    def install_etl_setup(self):
        """Install ETL setup with selected options"""
        try:
            installation_type = self.installation_type_var.get()
            hb_password = self.hb_password_entry.get()
            repo_update = self.repo_update_var.get()

            # Validate input
            if not hb_password:
                messagebox.showerror(
                    "Error",
                    "Please enter a valid HB password.",
                )
                return

            # Install ETL setup
            # ...

            # Show success message
            messagebox.showinfo(
                "Success",
                "ETL setup installed successfully.",
            )
        except Exception as e:
            # Show error message
            messagebox.showerror(
                "Error",
                f"An error occurred while installing ETL setup: {e}",
            )

    def help(self):
        """Display help information"""
        help_message = "This is a GUI application for installing EAI and ETL setups.\n\n"\
            "To install EAI setup, click the 'EAI' button and select the desired options.\n"\
            "To install ETL setup, click the 'ETL' button and select the desired options.\n\n"\
            "For any questions or issues, please contact support."

        # Show help message
        messagebox.showinfo(
            "Help",
            help_message,
        )

if __name__ == "__main__":
    app = ApplicationInstaller()
    app.run()
