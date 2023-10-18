import tkinter as tk
from maven import execute_maven_command

def on_command_completion(result, return_code):
    if result:
        print(f"Maven command completed successfully with return code {return_code}")
    else:
        print(f"Maven command failed with return code {return_code}")

root = tk.Tk()
root.title("Maven Command Runner")

# Replace 'your_maven_command' with the actual Maven command
maven_command = 'your_maven_command'  # Replace with your actual Maven command

execute_maven_command(maven_command, root, on_command_completion)

root.mainloop()

import subprocess
import tkinter as tk

def execute_maven_command(maven_command, master, callback):
    process = subprocess.Popen(maven_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    window = tk.Toplevel(master)
    window.title("Maven Command Output")

    output_text = tk.Text(window, wrap=tk.WORD, font=("Courier New", 10))
    output_text.pack()
    output_text.config(bg="black", fg="white")

    def update_output():
        line = process.stdout.readline()
        if line:
            output_text.insert(tk.END, line)
            output_text.see(tk.END)
            window.after(1, update_output)
        else:
            process.wait()
            return_code = process.returncode
            window.destroy()
            callback(return_code == 0, return_code)

    run_button = tk.Button(window, text="Run Maven Command", command=update_output)
    run_button.pack()
