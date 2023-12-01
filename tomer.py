import tkinter as tk
from datetime import datetime
import time

def start_timer():
    global start_time
    start_time = datetime.now()
    update_timer()

def stop_timer():
    current_time = datetime.now() - start_time
    formatted_time = str(current_time).split(".")[0]
    timer_label.config(text=f"Time taken: {formatted_time}")

def update_timer():
    current_time = datetime.now() - start_time
    formatted_time = str(current_time).split(".")[0]
    timer_label.config(text=f"Time: {formatted_time}")
    root.after(1000, update_timer)  # Update every 1000 milliseconds (1 second)

def simulate_task():
    start_timer()  # Start the timer
    for i in range(11):
        progress_var.set(i * 10)  # Update progress bar
        root.update_idletasks()
        time.sleep(1)
    stop_timer()  # Stop the timer

# Create the main window
root = tk.Tk()
root.title("Progress with Timer")

# Initialize variables
progress_var = tk.IntVar()

# Create and place widgets
progress_bar = tk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10)

timer_label = tk.Label(root, text="Time: 00:00:00")
timer_label.pack()

start_button = tk.Button(root, text="Start", command=simulate_task)
start_button.pack(pady=10)

# Start the GUI
root.mainloop()