import tkinter as tk
from ttkwidgets import ScrolledFrame

def add_stage():
    global stage_count
    if stage_count < 100:  # Adjust the limit as needed
        stage_label = tk.Label(inner_frame, text=f"Stage {stage_count + 1}")
        stage_label.grid(row=stage_count, column=0, sticky='w')
        stage_count += 1

root = tk.Tk()
root.title("Scrollable Stages Example")

sf = ScrolledFrame(root)
sf.pack(fill='both', expand=True)

inner_frame = sf.interior()

stage_count = 0

add_button = tk.Button(root, text="Add Stage", command=add_stage)
add_button.pack()

root.mainloop()