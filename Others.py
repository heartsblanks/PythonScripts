import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master):
        self.master = master

        self.treeview = ttk.Treeview(self.master, columns=("Flow"), show="tree")
        self.treeview.pack()

        self.data = [
            ("123", "1023"),
            ("123", "1123"),
            ("435", "4035"),
            ("435", "4135"),
            ("780", "7080"),
        ]

        self.populate_treeview()

    def populate_treeview(self):
        unique_ids = list(set(item[0] for item in self.data))
        unique_ids.sort()

        for unique_id in unique_ids:
            group_name = f"{unique_id}XXX"  # Group name is ID followed by 3 X's
            group_node = self.treeview.insert("", "end", text=group_name, open=True)

            for item in self.data:
                if item[0] == unique_id:
                    self.treeview.insert(group_node, "end", text=item[1], values=(item[1]))

    def toggle_checkbox(self, event):
        item_id = self.treeview.identify_row(event.y)
        if item_id:
            tags = self.treeview.item(item_id, "tags")
            if "item" in tags:
                current_value = self.treeview.item(item_id, "text")
                new_value = f"[x] {current_value}" if "[x]" not in current_value else current_value.replace("[x]", "")
                self.treeview.item(item_id, text=new_value)


root = tk.Tk()
app = Application(root)
root.mainloop()