import tkinter as tk
from datetime import datetime
import threading
import time

def update_timer():
    while not stop_event.is_set():
        current_time = datetime.now() - start_time
        formatted_time = str(current_time).split(".")[0]
        timer_label.config(text=f"Time: {formatted_time}")
        time.sleep(1)

def simulate_task():
    start_timer()  # Start the timer before the loop
    for i in range(1, 11):
        output_label.config(text=f"Number: {i}")
        time.sleep(1)
    stop_timer()  # Stop the timer after the loop

def start_timer():
    global start_time, stop_event
    start_time = datetime.now()
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.start()

def stop_timer():
    stop_event.set()  # Set the event to stop the timer
    timer_thread.join()  # Wait for the timer thread to finish
    current_time = datetime.now() - start_time
    formatted_time = str(current_time).split(".")[0]
    timer_label.config(text=f"Total Time taken: {formatted_time}")

# Create the main window
root = tk.Tk()
root.title("Task with Timer")

# Initialize variables
start_time = None
stop_event = None
timer_thread = None

# Create and place widgets
output_label = tk.Label(root, text="Number: ")
output_label.pack(pady=10)

timer_label = tk.Label(root, text="Time: 00:00:00")
timer_label.pack()

start_button = tk.Button(root, text="Start Task", command=simulate_task)
start_button.pack(pady=10)

# Start the GUI
root.mainloop()