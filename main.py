import tkinter as tk
import tkinter.ttk as ttk
import time

def simulate_migration(stage, progress, stage_canvas, stage_text):
    for i in range(101):
        progress.set(i)
        stage_canvas.coords(stage_bar, 10, 10, 10 + i, 30)
        stage_text.set(f"Stage {stage} - {i}%")
        root.update_idletasks()
        time.sleep(0.01)

    if progress.get() == 100:
        stage_text.set(f"Stage {stage} - Completed")
        stage_canvas.itemconfig("rect", fill="green")
    else:
        stage_text.set(f"Stage {stage} - Error")
        stage_canvas.itemconfig("rect", fill="red")

def migrate():
    for stage in range(1, 11):
        simulate_migration(stage, stage_progress[stage], stage_canvases[stage], stage_texts[stage])

root = tk.Tk()
root.title("Migration Progress")

stage_canvases = {}
stage_texts = {}
stage_progress = {}

for stage in range(1, 11):
    stage_frame = tk.Frame(root)
    stage_frame.pack(pady=10)

    stage_canvas = tk.Canvas(stage_frame, width=320, height=40)
    stage_canvas.pack()

    stage_text = tk.StringVar()
    stage_label = tk.Label(stage_canvas, textvariable=stage_text, anchor=tk.W)
    stage_label.place(x=10, y=10)

    stage_progress[stage] = tk.IntVar()
    stage_bar = ttk.Progressbar(stage_canvas, mode="determinate", length=300, variable=stage_progress[stage])
    stage_bar.place(x=10, y=20)

    stage_canvases[stage] = stage_canvas
    stage_texts[stage] = stage_text

migrate_button = tk.Button(root, text="Migrate", command=migrate)
migrate_button.pack(pady=10)

root.mainloop()