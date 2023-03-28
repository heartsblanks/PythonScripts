import tkinter as tk
import tkinter.filedialog
import os
import chardet
import multiprocessing

class FileSearch:
    def __init__(self, window):
        self.window = window
        self.window.title("File Search")

        # Create a label and entry widget for the search text
        search_text_label = tk.Label(window, text="Search Text:")
        search_text_label.pack()
        self.search_text_entry = tk.Entry(window)
        self.search_text_entry.pack()

        # Create a button to allow the user to select a directory
        browse_button = tk.Button(window, text="Select Directory", command=self.browse_directory)
        browse_button.pack()

        # Create a button to start the search
        search_button = tk.Button(window, text="Search", command=self.search_files)
        search_button.pack()

    def browse_directory(self):
        """Open a file dialog to allow the user to select a directory."""
        self.directory_path = tk.filedialog.askdirectory()

    def search_files(self):
        """Search for files that contain the specified search text."""
        # Get the search text from the entry widget
        search_text = self.search_text_entry.get()
        # Search for files in the selected directory
        matching_files = []
        # Create a pool of processes to search the directories in parallel
        pool = multiprocessing.Pool()
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                # Check if the search text is in the file name
                if search_text.lower() in file.lower():
                    matching_files.append(os.path.join(root, file))
                else:
                    # Check if the file contains the search text
                    if file.endswith(('.txt', '.pdf', '.doc', '.docx', '.ppt', '.pptx')):
                        file_path = os.path.join(root, file)
                        # Search the file in a separate process
                        result = pool.apply_async(search_file, args=(file_path, search_text))
                        # Add the file path to the matching files list if it contains the search text
                        if result.get():
                            matching_files.append(file_path)
        # Close the process pool
        pool.close()
        pool.join()
        # Display the matching files in a message box
        if matching_files:
            tk.messagebox.showinfo("Search Results", "The following files contain the search text:\n\n" + "\n".join(matching_files))
        else:
            tk.messagebox.showinfo("Search Results", "No files were found containing the search text.")

def search_file(file_path, search_text):
    """Search for the specified text in a file."""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        # Use chardet to detect the encoding of the file
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        if encoding is None:
            # If encoding is None, try a list of common encodings
            encodings = ['utf-8', 'iso-8859-1', 'cp1252', 'utf-16', 'utf-32']
            for e in encodings:
            try:
                text = raw_data.decode(encoding=e)
                if search_text in text:
                    return True
            except UnicodeDecodeError:
                pass
    else:
        # If encoding is detected, decode the file using that encoding
        text = raw_data.decode(encoding=encoding)
        if search_text in text:
            return True
return False
Create the main window

window = tk.Tk()

Create an instance of the FileSearch class

file_search = FileSearch(window)

Run the main event loop

window.mainloop()
