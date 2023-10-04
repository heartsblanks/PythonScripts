import tkinter as tk
from tkinter import ttk
import time
import threading

def migrate():
    def simulate_migration(stage):
        stage_progress_bars[stage].start()
        stage_label.config(text=f"Stage {stage}")
        for i in range(101):
            time.sleep(0.01)
            stage_progress_bars[stage].step(1)
            root.update_idletasks()
        stage_progress_bars[stage].stop()
        if stage == 10:
            stage_label.config(text="Migration Completed", fg="green")
        else:
            stage_label.config(text=f"Error in Stage {stage}", fg="red")

    for stage in range(1, 11):
        t = threading.Thread(target=simulate_migration, args=(stage,))
        t.start()

root = tk.Tk()
root.title("Migration Progress")

stage_progress_bars = []
for _ in range(11):
    progress_bar = ttk.Progressbar(root, mode="determinate", length=300)
    stage_progress_bars.append(progress_bar)
    progress_bar.pack(pady=5)

stage_label = tk.Label(root, text="", pady=10)
stage_label.pack()

migrate_button = tk.Button(root, text="Migrate", command=migrate)
migrate_button.pack(pady=10)

root.mainloop()