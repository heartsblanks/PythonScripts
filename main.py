import subprocess
import tkinter as tk
import threading

def execute_maven_command():
    command = "mvn install"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        text_box.insert(tk.END, line)
        text_box.see(tk.END)
        root.update_idletasks()
    process.wait()

def display_output():
    thread = threading.Thread(target=execute_maven_command)
    thread.start()

root = tk.Tk()
text_box = tk.Text(root)
text_box.pack()

tk.Button(root, text="Run Maven Command", command=display_output).pack()

root.mainloop()