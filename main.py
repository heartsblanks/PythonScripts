import tkinter as tk
from tkinter import ttk
import time
import threading

def migrate():
    def simulate_migration(stage):
        progress_var.set(0)
        stage_label.config(text=f"Stage {stage}")
        for i in range(101):
            time.sleep(0.01)
            progress_var.set(i)
            root.update_idletasks()
        if stage == 10:
            stage_label.config(text="Migration Completed", fg="green")
        else:
            stage_label.config(text=f"Error in Stage {stage}", fg="red")

    for stage in range(1, 11):
        t = threading.Thread(target=simulate_migration, args=(stage,))
        t.start()

root = tk.Tk()
root.title("Migration Progress")

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, mode="determinate", length=300, variable=progress_var)
progress_bar.pack(pady=10)

stage_label = tk.Label(root, text="", pady=10)
stage_label.pack()

migrate_button = tk.Button(root, text="Migrate", command=migrate)
migrate_button.pack(pady=10)

root.mainloop()