import tkinter as tk
import subprocess

def run_command():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Command Prompt")

    # Create a Text widget to display the command output
    output_text = tk.Text(window, wrap=tk.WORD, font=("Courier New", 10))
    output_text.pack()

    # Create an Entry widget for entering commands
    command_entry = tk.Entry(window)
    command_entry.pack()

    def execute_command():
        command = command_entry.get()
        if command:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in process.stdout:
                output_text.insert(tk.END, line)
                output_text.see(tk.END)  # Auto-scroll to the end of the Text widget
            command_entry.delete(0, tk.END)  # Clear the Entry widget

    # Create a button to execute the command
    execute_button = tk.Button(window, text="Execute Command", command=execute_command)
    execute_button.pack()

    window.mainloop()

# Run the command prompt when the script starts
run_command()