import tkinter as tk
import tkinter.ttk as ttk
import time

def simulate_migration(stage, progress_bar, stage_text, percentage_text, status_text):
    for i in range(101):
        percentage_text.set(f"{i}%")
        status_text.set("Completed" if i == 100 else "In Progress")
        progress_bar["value"] = i
        root.update_idletasks()
        time.sleep(0.01)

    if i == 100:
        status_text.set("Completed")
        progress_bar["style"] = "green.Horizontal.TProgressbar"
    else:
        status_text.set("Error")
        progress_bar["style"] = "red.Horizontal.TProgressbar"

def migrate(stage):
    if stage > 10:
        return
    simulate_migration(stage, progress_bars[stage], stage_texts[stage], percentage_texts[stage], status_texts[stage])
    root.after(10, migrate, stage + 1)

root = tk.Tk()
root.title("Migration Progress")

# Create dictionaries to store progress bars and text elements
progress_bars = {}
stage_texts = {}
percentage_texts = {}
status_texts = {}

for stage in range(1, 11):
    stage_frame = tk.Frame(root)
    stage_frame.grid(row=stage, column=0, padx=10, pady=10, sticky="w")

    stage_text = tk.StringVar()
    stage_label = tk.Label(stage_frame, textvariable=stage_text, anchor=tk.W)
    stage_label.grid(row=0, column=0, padx=10)

    percentage_text = tk.StringVar()
    percentage_label = tk.Label(stage_frame, textvariable=percentage_text, anchor=tk.W)
    percentage_label.grid(row=0, column=1, padx=10)

    status_text = tk.StringVar()
    status_label = tk.Label(stage_frame, textvariable=status_text, anchor=tk.W)
    status_label.grid(row=0, column=2, padx=10)

    progress_bar = ttk.Progressbar(stage_frame, orient="horizontal", length=320, mode="determinate")
    progress_bar.grid(row=0, column=3, padx=10)

    progress_bars[stage] = progress_bar
    stage_texts[stage] = stage_text
    percentage_texts[stage] = percentage_text
    status_texts[stage] = status_text

# Create a button to start migration
migrate_button = tk.Button(root, text="Migrate", command=lambda: migrate(1))
migrate_button.grid(row=11, column=0, pady=10)

root.mainloop()