import tkinter as tk
import tkinter.ttk as ttk
import time

def simulate_migration(stage, stage_canvas, stage_text, percentage_text, status_text):
    progress = tk.IntVar()
    for i in range(101):
        progress.set(i)
        progress_width = i * 3
        stage_canvas.coords(stage_bar, 0, 0, progress_width, 20)
        stage_text.set(f"Stage {stage}")
        percentage_text.set(f"{i}%")
        status_text.set("Completed" if i == 100 else "In Progress")
        root.update_idletasks()
        time.sleep(0.01)

    if i == 100:
        status_text.set("Completed")
        stage_canvas.itemconfig(stage_bar, fill="green")
    else:
        status_text.set("Error")
        stage_canvas.itemconfig(stage_bar, fill="red")

def migrate(stage):
    if stage > 10:
        return
    simulate_migration(stage, stage_canvases[stage], stage_texts[stage], percentage_texts[stage], status_texts[stage])
    root.after(10, migrate, stage + 1)

root = tk.Tk()
root.title("Migration Progress")

stage_canvases = {}
stage_texts = {}
percentage_texts = {}
status_texts = {}

for stage in range(1, 11):
    stage_frame = tk.Frame(root)
    stage_frame.grid(row=stage, column=0, padx=10, pady=10, sticky="w")

    stage_canvas = tk.Canvas(stage_frame, width=320, height=40)
    stage_canvas.grid(row=0, column=0, columnspan=4)

    stage_text = tk.StringVar()
    stage_label = tk.Label(stage_canvas, textvariable=stage_text, anchor=tk.W)
    stage_label.grid(row=0, column=0, padx=10)

    percentage_text = tk.StringVar()
    percentage_label = tk.Label(stage_canvas, textvariable=percentage_text, anchor=tk.W)
    percentage_label.grid(row=0, column=1, padx=10)

    status_text = tk.StringVar()
    status_label = tk.Label(stage_canvas, textvariable=status_text, anchor=tk.W)
    status_label.grid(row=0, column=2, padx=10)

    stage_bar = stage_canvas.create_rectangle(0, 0, 0, 20, fill="green")

    stage_canvases[stage] = stage_canvas
    stage_texts[stage] = stage_text
    percentage_texts[stage] = percentage_text
    status_texts[stage] = status_text

migrate_button = tk.Button(root, text="Migrate", command=lambda: migrate(1))
migrate_button.grid(row=11, column=0, pady=10)

root.mainloop()