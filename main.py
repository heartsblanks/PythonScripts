import subprocess
import tkinter as tk

# Create a tkinter window and text box
root = tk.Tk()
text_box = tk.Text(root)
text_box.pack()

# Command to execute
command = "mvn install"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

# Function to display real-time output in the tkinter text box
def display_output():
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            text_box.insert(tk.END, output)
            text_box.see(tk.END)
        root.update_idletasks()

# Wait for the command to complete and then execute the next lines of code
process.wait()

# Now you can proceed with the next lines of code
text_box.insert(tk.END, "Maven command has completed.")
root.update_idletasks()

# Start the real-time output display function
display_output()

root.mainloop()