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

# Create a dictionary to store the group nodes by the first character
group_nodes = {}

# Create a custom checkbutton widget
def toggle_check():
    item_id = tree.focus()
    current_tags = tree.item(item_id, 'tags')

    if 'checked' in current_tags:
        tree.item(item_id, tags=('group',))
    else:
        tree.item(item_id, tags=('group', 'checked'))

def handle_click(event):
    region = tree.identify_region(event.x, event.y)

    if region == 'cell':
        item_id = tree.identify_row(event.y)
        column = tree.identify_column(event.x)

        if column == '#0' and 'XXX' in tree.item(item_id, 'text'):
            toggle_check()
            return 'break'

tree.bind('<Button-1>', handle_click)

# Configure the TreeView to show checkboxes
tree.tag_configure('checked', image='checkbox_checked.png')
tree.tag_configure('unchecked', image='checkbox_unchecked.png')
tree.tag_bind('checked', '<Button-1>', toggle_check)
tree.tag_bind('unchecked', '<Button-1>', toggle_check)

# Set initial checkbox state
tree.tag_configure('group', image='checkbox_unchecked.png')

# Insert groups and flows into the TreeView
for group_id, group_data in grouped_df:
    # Get the first character of the group ID
    first_char = group_id[0]

    # Check if the first character exists in the dictionary
    if first_char in group_nodes:
        # If it exists, insert the group node under the corresponding parent node
        parent_node = group_nodes[first_char]
        group_node = tree.insert(parent_node, 'end', text=f'{group_id}XXX', open=True, tags=('group',))
    else:
        # If it doesn't exist, create a new parent node and insert the group node under it
        parent_node = tree.insert('', 'end', text=first_char, open=True)
        group_node = tree.insert(parent_node, 'end', text=f'{group_id}XXX', open=True, tags=('group',))

        # Store the parent node in the dictionary for future use
        group_nodes[first_char] = parent_node

    # Insert flow nodes as children of the group
    for _, row in group_data.iterrows():
        tree.insert(group_node, 'end', text=row['Flow'])

# Pack the TreeView widget
tree.pack()

# Start the Tkinter event loop
window.mainloop()