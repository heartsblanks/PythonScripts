import tkinter as tk

class InstallOrchestration:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x150')
        self.root.title('Install Orchestration')
        
        self.submit_button = tk.Button(self.root, text='Submit', command=self.select_option)
        self.submit_button.pack(side='left', padx=10, pady=10)
        
        self.quit_button = tk.Button(self.root, text='Quit', command=self.root.destroy)
        self.quit_button.pack(side='right', padx=10, pady=10)
        
        self.top_level_window = tk.Toplevel(self.root)
        self.top_level_window.title('Select Option')
        self.top_level_window.geometry('300x100')
        
        self.eai_button = tk.Button(self.top_level_window, text='EAI', command=self.select_eai)
        self.eai_button.pack(side='left', padx=10, pady=10)
        
        self.etl_button = tk.Button(self.top_level_window, text='ETL', command=self.select_etl)
        self.etl_button.pack(side='right', padx=10, pady=10)
        
        self.root.mainloop()
    
    def select_option(self):
        pass
    
    def select_eai(self):
        self.eai_window = tk.Toplevel(self.root)
        self.eai_window.title('Select EAI Option')
        self.eai_window.geometry('300x100')
        
        self.iib_button = tk.Button(self.eai_window, text='IIB10', command=self.get_eai_options)
        self.iib_button.pack(side='left', padx=10, pady=10)
        
        self.ace_button = tk.Button(self.eai_window, text='ACE12', command=self.get_eai_options)
        self.ace_button.pack(side='right', padx=10, pady=10)
        
        self.password_button = tk.Button(self.eai_window, text='Password Update', command=self.password_update)
        self.password_button.pack(side='bottom', padx=10, pady=10)
    
    def select_etl(self):
        pass
    
    def get_eai_options(self):
        pass
    
    def password_update(self):
        pass

if __name__ == '__main__':
    InstallOrchestration()
 