import tkinter as tk

class InstallOrchestration:
    def __init__(self, master):
        self.master = master
        self.master.title("Install Orchestration")
        
        # Create label and entry widgets for the user to input data
        tk.Label(master, text="Enter Data:").grid(row=0, column=0)
        self.data_entry = tk.Entry(master)
        self.data_entry.grid(row=0, column=1)
        
        # Create submit and quit buttons
        tk.Button(master, text="Submit", command=self.submit).grid(row=1, column=0)
        tk.Button(master, text="Quit", command=self.quit).grid(row=1, column=1)
        
    def submit(self):
        # Retrieve data from entry widget
        data = self.data_entry.get()
        
        # Do something with data...
        
        # Clear entry widget
        self.data_entry.delete(0, tk.END)
    
    def quit(self):
        # Close window
        self.master.destroy()

# Create top-level window
root = tk.Tk()
root.title("Select EAI or ETL")

# Create radio buttons for EAI and ETL
var = tk.StringVar()
var.set("EAI")
eai_button = tk.Radiobutton(root, text="EAI", variable=var, value="EAI")
etl_button = tk.Radiobutton(root, text="ETL", variable=var, value="ETL")
eai_button.pack()
etl_button.pack()

# Create submit and quit buttons
submit_button = tk.Button(root, text="Submit", command=root.destroy)
quit_button = tk.Button(root, text="Quit", command=root.destroy)
submit_button.pack()
quit_button.pack()

# Run main loop
root.mainloop()

# Create InstallOrchestration window based on user selection
if var.get() == "EAI":
    root = tk.Tk()
    app = InstallOrchestration(root)
    root.mainloop()
elif var.get() == "ETL":
    root = tk.Tk()
    app = InstallOrchestration(root)
    root.mainloop()
