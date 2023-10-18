import tkinter as tk
from Maven import execute_maven_command

def on_command_completion(return_code):
    if return_code == 0:
        print(f"Maven command completed successfully with return code {return_code}")
        # Call the next function or perform other actions here
    else:
        print(f"Maven command failed with return code {return_code}")

root = tk.Tk()
root.title("Maven Command Runner")

# Create a frame within the main window to display the Maven command output
output_frame = tk.Frame(root)
output_frame.pack()

# Create a text widget within the output frame to display the command output
output_text = tk.Text(output_frame, wrap=tk.WORD)
output_text.pack()
output_text.config(bg="black", fg="white")

# Create a button to trigger the Maven command execution
button = tk.Button(root, text="Run Maven Command", command=lambda: execute_maven_command(output_text, on_command_completion))
button.pack()

root.mainloop()

import threading
import subprocess

def execute_maven_command(output_text, callback):
    def run_maven():
        nonlocal return_code
        process = subprocess.Popen('your_maven_command', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        while True:
            line = process.stdout.readline()
            if not line:
                break  # End of output
            output_text.insert('end', line)
            output_text.see('end')  # Auto-scroll to the end of the Text widget
        return_code = process.returncode

        # Signal that the Maven command is complete
        maven_completed.set()

    return_code = None
    maven_completed = threading.Event()

    # Create a new thread to execute the Maven command
    maven_thread = threading.Thread(target=run_maven)
    maven_thread.start()

    maven_thread.join()  # Wait for the Maven thread to complete

    callback(return_code)