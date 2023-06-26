import tkinter as tk
from tkinter import ttk
import pandas as pd

# Assuming you have a DataFrame called 'df' with columns 'ID' and 'Flow'
grouped_df = df.groupby('ID')

# Create the Tkinter window
window = tk.Tk()
window.title("TreeView Example")

# Create the TreeView widget
tree = ttk.Treeview(window, columns=('Flow'))

# Custom function to toggle the checkbox state
def toggle_checkbox(item_id):
    current_state = tree.item(item_id, 'value')
    tree.item(item_id, value=not current_state)

# Create a custom checkbox column
tree.heading('#0', text='ID', anchor='w')
tree.column('#0', width=100, anchor='w')

# Insert groups and flows into the TreeView
for group_id, group_data in grouped_df:
    # Insert group node with checkbox
    group_node = tree.insert('', 'end', text=f'{group_id}XXX', value=False)

    # Insert flow nodes as children of the group
    for _, row in group_data.iterrows():
        tree.insert(group_node, 'end', text=row['Flow'])

# Bind the checkbox state toggling function to the TreeView
tree.bind('<Button-1>', lambda event: toggle_checkbox(tree.focus()))

# Pack the TreeView widget
tree.pack()

# Start the Tkinter event loop
window.mainloop()