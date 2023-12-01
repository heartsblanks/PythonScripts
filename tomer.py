import time
from datetime import datetime
import threading

def update_timer():
    while not stop_event.is_set():
        current_time = datetime.now() - start_time
        formatted_time = str(current_time).split(".")[0]
        print(f"Time: {formatted_time}")
        time.sleep(1)

def simulate_task():
    start_timer()  # Start the timer before the loop
    for i in range(1, 11):
        print(i)
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
    print(f"Total Time taken: {formatted_time}")

# Simulate the task in the main thread
simulate_task()

# Call update_timer independently (after the task has completed, for example)
update_timer()