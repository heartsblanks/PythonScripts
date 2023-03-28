import tkinter as tk
import tkinter.filedialog
import os
import chardet
import concurrent.futures

class FileSearch:
    def __init__(self, window):
        self.window = window
        self.window.title("File Search")
        # Create an executor to run tasks in parallel
        self.executor = concurrent.futures.ThreadPoolExecutor()

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
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                # Check if the search text is in the file name
                if search_text.lower() in file.lower():
                    matching_files.append(os.path.join(root, file))
                else:
                    # Check if the file contains the search text
                    if file.endswith(('.txt', '.pdf', '.doc', '.docx', '.ppt', '.pptx')):
                        file_path = os.path.join(root, file)
                        # Search the file in a separate thread
                        future = self.executor.submit(search_file, file_path, search_text)
                        # Add the file path to the matching files list if it contains the search text
                        if future.result():
                            matching_files.append(file_path)

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
        if encoding:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    file_content = f.read()
                    # Check if the search text is in the file
                    if search_text.lower() in file_content.lower():
                        return True
            except:
                pass
    return False

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearch(root)
    root.mainloop()
