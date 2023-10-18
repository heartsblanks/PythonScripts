import tkinter as tk
from maven import execute_maven_command

def on_command_completion(result, return_code):
    if result:
        print(f"Maven command completed successfully with return code {return_code}")
    else:
        print(f"Maven command failed with return code {return_code}")

root = tk.Tk()
root.title("Maven Command Runner")

# Create a frame within the main window to display the Maven command output
output_frame = tk.Frame(root)
output_frame.pack()

# Replace 'your_maven_command' with the actual Maven command
maven_command = 'your_maven_command'  # Replace with your actual Maven command

print("Before executing Maven command")

execute_maven_command(maven_command, output_frame, on_command_completion)

print("After executing Maven command")

root.mainloop()


import subprocess
import tkinter as tk

def execute_maven_command(maven_command, frame, callback):
    process = subprocess.Popen(maven_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output_text = tk.Text(frame, wrap=tk.WORD, font=("Courier New", 10)
    output_text.pack()
    output_text.config(bg="black", fg="white")

    def update_output():
        line = process.stdout.readline()
        if line:
            output_text.insert(tk.END, line)
            output_text.see(tk.END)
            frame.after(1, update_output)
        else:
            process.wait()
            return_code = process.returncode
            callback(return_code == 0, return_code)
            output_text.config(state=tk.DISABLED)

    update_output()