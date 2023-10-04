import tkinter as tk
import threading
import time

def migrate():
    def simulate_migration(stage):
        canvas.itemconfig(stage_text, text=f"Stage {stage}")
        for i in range(101):
            canvas.coords(stage_bar, 10, 10, 10 + i, 30)
            canvas.update()
            time.sleep(0.01)
        if stage == 10:
            canvas.itemconfig(stage_text, text="Migration Completed", fill="green")
        else:
            canvas.itemconfig(stage_text, text=f"Error in Stage {stage}", fill="red")

    for stage in range(1, 11):
        t = threading.Thread(target=simulate_migration, args=(stage,))
        t.start()

root = tk.Tk()
root.title("Migration Progress")

canvas = tk.Canvas(root, width=320, height=50)
canvas.pack(pady=10)

stage_text = canvas.create_text(10, 35, anchor=tk.W, text="", font=("Helvetica", 10))
stage_bar = canvas.create_rectangle(10, 10, 10, 30, fill="green")

migrate_button = tk.Button(root, text="Migrate", command=migrate)
migrate_button.pack(pady=10)

root.mainloop()