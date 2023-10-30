import tkinter as tk
from tkinter import ttk

def add_stage():
    global stage_count
    if stage_count < 100:  # Adjust the limit as needed
        stage_label = tk.Label(inner_frame, text=f"Stage {stage_count + 1}")
        stage_label.grid(row=stage_count, column=0, sticky='w')
        stage_count += 1
        update_canvas_scrollregion()

def update_canvas_scrollregion():
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Stages Example")

canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

inner_frame = ttk.Frame(frame)
inner_frame.grid(row=0, column=0)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

stage_count = 0

add_button = tk.Button(root, text="Add Stage", command=add_stage)
add_button.pack()

root.mainloop()