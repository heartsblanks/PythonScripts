import win32com.client
from tkinter import *

# Define a function to handle the email sending
def send_email():
    try:
        # Create the Outlook application object
        outlook = win32com.client.Dispatch('Outlook.Application')

        # Get the recipient, CC, and BCC addresses from the input fields
        to_address = to_entry.get()
        cc_address = cc_entry.get()
        bcc_address = bcc_entry.get()

        # Create a new mail item and set the recipients and subject
        mail = outlook.CreateItem(0)
        mail.To = to_address
        mail.CC = cc_address
        mail.BCC = bcc_address
        mail.Subject = 'Update'

        # Define the mail body window using tkinter
        mail_window = Tk()
        mail_window.title("Mail Body")

        # Define the mail body input fields using tkinter
        project_label = Label(mail_window, text="Project Name:")
        project_label.pack()
        project_entry = Entry(mail_window, width=30)
        project_entry.pack()
        description_label = Label(mail_window, text="Progress Description:")
        description_label.pack()
        description_entry = Entry(mail_window, width=30)
        description_entry.pack()
        next_steps_label = Label(mail_window, text="Next Steps:")
        next_steps_label.pack()
        next_steps_entry = Entry(mail_window, width=30)
        next_steps_entry.pack()
        blockers_label = Label(mail_window, text="Blockers:")
        blockers_label.pack()
        blockers_entry = Entry(mail_window, width=30)
        blockers_entry.pack()
        time_label = Label(mail_window, text="Time to UAT:")
        time_label.pack()
        time_entry = Entry(mail_window, width=30)
        time_entry.pack()

        # Define a function to handle the "Done" button
        def done():
            # Get the data from the input fields
            project_name = project_entry.get()
            progress_description = description_entry.get()
            next_steps = next_steps_entry.get()
            blockers = blockers_entry.get()
            time_to_uat = time_entry.get()

            # Create a formatted string for the data and add it to the mail body
            data_str = f"Project Name: {project_name}\nProgress Description: {progress_description}\nNext Steps: {next_steps}\nBlockers: {blockers}\nTime to UAT: {time_to_uat}\n\n"
            mail.Body += data_str

            # Clear the input fields and destroy the mail window
            project_entry.delete(0, END)
            description_entry.delete(0, END)
            next_steps_entry.delete(0, END)
            blockers_entry.delete(0, END)
            time_entry.delete(0, END)
            mail_window.destroy()

            # Send the email
            mail.Send()

        # Define the "Done" button using tkinter
        done_button = Button(mail_window, text="Done", command=done)
        done_button.pack()

        # Run the main loop to display the mail window
        mail_window.mainloop()

    except Exception as e:
        # Handle any errors that occur during email sending
        print(f"An error occurred: {e}")
        mail_window.destroy()

# Define the main window using tkinter
main_window = Tk()
main_window.title("Send Email")

# Define the recipient input fields using tkinter
to_label = Label(main_window, text="To:")
to_label.pack()
to_entry = Entry(main_window, width=30)
to_entry.pack()
cc_label = Label(main_window, text="CC:")
cc_label.pack()
cc_entry = Entry(main_window, width=30)
cc_entry.pack()
bcc_label = Label(main_window, text="BCC:")
bcc_label.pack()
bcc_entry = Entry(main_window, width=30)
bcc_entry.pack()

mail_body_button = Button(main_window, text="Mail Body", command=send_email)
mail_body_button.pack()
main_window.mainloop()



def done():
    # Get the data from the input fields
    project_name = project_entry.get()
    progress_description = description_entry.get()
    next_steps = next_steps_entry.get()
    blockers = blockers_entry.get()
    time_to_uat = time_entry.get()

    # Create a formatted string for the data and add it to the mail body
    data_str = f"Project Name: {project_name}\nProgress Description: {progress_description}\nNext Steps: {next_steps}\nBlockers: {blockers}\nTime to UAT: {time_to_uat}\n\n"
    mail.Body += data_str

    # Clear the input fields and destroy the mail window
    project_entry.delete(0, END)
    description_entry.delete(0, END)
    next_steps_entry.delete(0, END)
    blockers_entry.delete(0, END)
    time_entry.delete(0, END)
    mail_window.destroy()

    # Create a new tkinter window to display the email details
    details_window = Tk()
    details_window.title("Email Details")

    # Define Label widgets to display the email details
    project_label = Label(details_window, text=f"Project Name: {project_name}")
    project_label.pack()
    description_label = Label(details_window, text=f"Progress Description: {progress_description}")
    description_label.pack()
    next_steps_label = Label(details_window, text=f"Next Steps: {next_steps}")
    next_steps_label.pack()
    blockers_label = Label(details_window, text=f"Blockers: {blockers}")
    blockers_label.pack()
    time_label = Label(details_window, text=f"Time to UAT: {time_to_uat}")
    time_label.pack()

    # Define a function to send the email
    def send_email():
        mail.Send()
        details_window.destroy()

    # Define a "Send" button to send the email
    send_button = Button(details_window, text="Send", command=send_email)
    send_button.pack()

    # Run the main loop to display the details window
    details_window.mainloop()



