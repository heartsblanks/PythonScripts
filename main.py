import subprocess
import tkinter as tk

def execute_maven_command(maven_command, frame, callback):
    process = subprocess.Popen(maven_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output_text = tk.Text(frame, wrap=tk.WORD, font=("Courier New", 10))
    output_text.pack()
    output_text.config(bg="black", fg="white")

    def update_output():
        line = process.stdout.readline()
        if line:
            output_text.insert(tk.END, line)
            output_text.see(tk.END)
            frame.after(1, update_output)
        else:
            return_code = process.wait()
            callback(return_code == 0, return_code)
            output_text.config(state=tk.DISABLED)

    update_output()