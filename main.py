import tkinter as tk
import time

def migrate():
    def simulate_migration(stage):
        progress = 0
        stage_canvas = stage_canvases[stage]
        stage_text = stage_texts[stage]

        for i in range(101):
            progress = i
            stage_canvas.coords(stage_bar, 10, 10, 10 + progress, 30)
            stage_canvas.itemconfig(stage_text, text=f"Stage {stage} - {progress}%")
            stage_canvas.update()
            time.sleep(0.01)

        if progress == 100:
            stage_canvas.itemconfig(stage_text, text=f"Stage {stage} - Completed", fill="green")
        else:
            stage_canvas.itemconfig(stage_text, text=f"Stage {stage} - Error", fill="red")

        # Check if this is the last stage before trying to access the next stage
        if stage < 10:
            simulate_migration(stage + 1)

root = tk.Tk()
root.title("Migration Progress")

stage_canvases = []
stage_texts = []

for stage in range(11):
    stage_frame = tk.Frame(root)
    stage_frame.pack(pady=10)

    stage_canvas = tk.Canvas(stage_frame, width=320, height=40)
    stage_canvas.pack()

    stage_text = stage_canvas.create_text(10, 20, anchor=tk.W, text=f"Stage {stage} - 0%")
    stage_bar = stage_canvas.create_rectangle(10, 10, 10, 30, fill="green")

    stage_canvases.append(stage_canvas)
    stage_texts.append(stage_text)

migrate_button = tk.Button(root, text="Migrate", command=lambda: simulate_migration(1))
migrate_button.pack(pady=10)

root.mainloop()