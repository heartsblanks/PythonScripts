import tkinter as tk
from tkinter import ttk
import pandas as pd

# Assuming you have a DataFrame called 'df' with columns 'ID' and 'Flow'
grouped_df = df.groupby('ID')

# Create the Tkinter window
window = tk.Tk()
window.title("TreeView Example")

# Create the TreeView widget
tree = ttk.Treeview(window, columns=('Flow'), show='tree')

# Create a dictionary to store the checkbutton values by item ID
checkbutton_values = {}

# Create a custom checkbutton widget
def toggle_check(item_id):
    current_value = checkbutton_values.get(item_id, False)
    checkbutton_values[item_id] = not current_value
    update_checkbutton(item_id)

def update_checkbutton(item_id):
    is_checked = checkbutton_values.get(item_id, False)
    tree.item(item_id, text=is_checked)

def handle_click(event):
    item_id = tree.identify_row(event.y)
    column = tree.identify_column(event.x)

    if column == '#0' and 'XXX' in tree.item(item_id, 'text'):
        toggle_check(item_id)
        return 'break'

tree.bind('<Button-1>', handle_click)

# Configure the TreeView to show checkboxes
tree.heading('#0', text='Checkbox')

# Insert groups and flows into the TreeView
for group_id, group_data in grouped_df:
    # Get the first character of the group ID
    first_char = group_id[0]

    # Insert group node
    group_node = tree.insert('', 'end', text=f'{group_id}XXX')

    # Insert flow nodes as children of the group
    for _, row in group_data.iterrows():
        flow_node = tree.insert(group_node, 'end', text=row['Flow'])
        checkbutton_values[flow_node] = False
        update_checkbutton(flow_node)

# Pack the TreeView widget
tree.pack()

# Start the Tkinter event loop
window.mainloop()