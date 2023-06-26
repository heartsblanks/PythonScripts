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

# Create a dictionary to store the group nodes by the first character
group_nodes = {}

# Create a custom checkbutton widget
def toggle_check(event):
    item_id = tree.focus()
    current_state = tree.item(item_id, 'value')

    if current_state == 'checked':
        tree.item(item_id, value='unchecked')
    else:
        tree.item(item_id, value='checked')

def handle_click(event):
    region = tree.identify_region(event.x, event.y)

    if region == 'cell':
        item_id = tree.identify_row(event.y)
        column = tree.identify_column(event.x)

        if column == '#0' and 'XXX' in tree.item(item_id, 'text'):
            toggle_check(event)
            return 'break'

tree.bind('<Button-1>', handle_click)

# Configure the TreeView to show checkboxes
tree.heading('#0', text='ID')
tree.column('#0', width=100, anchor='w')

# Insert groups and flows into the TreeView
for group_id, group_data in grouped_df:
    # Get the first character of the group ID
    first_char = group_id[0]

    # Check if the first character exists in the dictionary
    if first_char in group_nodes:
        # If it exists, insert the group node under the corresponding parent node
        parent_node = group_nodes[first_char]
        group_node = tree.insert(parent_node, 'end', text=f'{group_id}XXX')
    else:
        # If it doesn't exist, create a new parent node and insert the group node under it
        parent_node = tree.insert('', 'end', text=first_char)
        group_node = tree.insert(parent_node, 'end', text=f'{group_id}XXX')

        # Store the parent node in the dictionary for future use
        group_nodes[first_char] = parent_node

    # Insert flow nodes as children of the group
    for _, row in group_data.iterrows():
        tree.insert(group_node, 'end', text=row['Flow'])

    # Add a checkbox for the group node
    checkbutton = ttk.Checkbutton(tree)
    tree.item(group_node, image='', values=[checkbutton], tags='checkbutton')
    checkbutton.bind('<Button-1>', toggle_check)

# Set the image for checked and unchecked checkboxes
checked_image = tk.PhotoImage(file='Files/checkbox_checked.png')
unchecked_image = tk.PhotoImage(file='Files/checkbox_unchecked.png')

# Configure the TreeView to display the checkbox images
tree.tag_configure('checkbutton', image=unchecked_image)
tree.tag_bind('checkbutton', '<Button-1>', toggle_check)

# Pack the TreeView widget
tree.pack()

# Start the Tkinter event loop
window.mainloop()