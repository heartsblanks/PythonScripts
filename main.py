import tkinter as tk
import time

def simulate_migration(stage, progress, stage_canvas, stage_text):
    for i in range(101):
        progress.set(i)
        progress_width = i * 3
        stage_canvas.coords(stage_bar, 10, 10, 10 + progress_width, 30)
        stage_text.set(f"Stage {stage} - {i}%")
        root.update_idletasks()
        time.sleep(0.01)

    if i == 100:
        stage_text.set(f"Stage {stage} - Completed")
        stage_canvas.itemconfig(stage_bar, fill="green")
    else:
        stage_text.set(f"Stage {stage} - Error")
        stage_canvas.itemconfig(stage_bar, fill="red")

def migrate(stage):
    if stage > 10:
        return
    simulate_migration(stage, stage_progress[stage], stage_canvases[stage], stage_texts[stage])
    root.after(10, migrate, stage + 1)

root = tk.Tk()
root.title("Migration Progress")

stage_canvases = {}
stage_texts = {}

for stage in range(1, 11):
    stage_frame = tk.Frame(root)
    stage_frame.pack(pady=10)

    stage_canvas = tk.Canvas(stage_frame, width=320, height=40)
    stage_canvas.pack()

    stage_text = tk.StringVar()
    stage_label = tk.Label(stage_canvas, textvariable=stage_text, anchor=tk.W)
    stage_label.place(x=10, y=10)

    stage_bar = stage_canvas.create_rectangle(10, 10, 10, 30, fill="green")

    stage_canvases[stage] = stage_canvas
    stage_texts[stage] = stage_text

migrate_button = tk.Button(root, text="Migrate", command=lambda: migrate(1))
migrate_button.pack(pady=10)

root.mainloop()