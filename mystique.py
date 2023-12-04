import tkinter as tk
from tkinter import ttk
import time

class MystiqueIntro:
    def __init__(self, root):
        self.root = root
        self.root.title("Mystique Intro")
        self.root.geometry("800x600")

        self.label = ttk.Label(root, text="Welcome to the Mystique Experience!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.animate_intro()

    def animate_intro(self):
        self.label.config(text="")
        mystique_text = "Mystique"

        for char in mystique_text:
            time.sleep(0.5)  # Adjust the sleep duration for your desired pace
            self.label.config(text=self.label.cget("text") + char)
            self.root.update()

        # Add additional animation or transitions as needed
        # For example, you could add fading effects, image transitions, etc.

        # After the intro animation, you might want to transition to the main application

if __name__ == "__main__":
    root = tk.Tk()
    app = MystiqueIntro(root)
    root.mainloop()