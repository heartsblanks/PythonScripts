import os
import filecmp
import shutil

def compare_and_copy(source_dir, destination_dir):
    # Get the list of files and directories in the source directory
    source_entries = os.listdir(source_dir)

    # Iterate through each entry in the source directory
    for entry in source_entries:
        source_entry_path = os.path.join(source_dir, entry)
        destination_entry_path = os.path.join(destination_dir, entry)

        # Check if the entry is a file
        if os.path.isfile(source_entry_path):
            # Check if the file exists in the destination directory
            if not os.path.exists(destination_entry_path):
                # File does not exist in destination, copy it from source
                shutil.copy2(source_entry_path, destination_entry_path)
            else:
                # File exists in destination, compare contents
                if not filecmp.cmp(source_entry_path, destination_entry_path, shallow=False):
                    # Contents differ, update the file in destination with source content
                    shutil.copy2(source_entry_path, destination_entry_path)

        # Check if the entry is a directory
        elif os.path.isdir(source_entry_path):
            # Check if the directory exists in the destination directory
            if not os.path.exists(destination_entry_path):
                # Directory does not exist in destination, copy it from source
                shutil.copytree(source_entry_path, destination_entry_path)
            else:
                # Directory exists in destination, recursively compare and copy
                compare_and_copy(source_entry_path, destination_entry_path)

# Example usage
source_directory = 'path/to/source/directory'
destination_directory = 'path/to/destination/directory'

compare_and_copy(source_directory, destination_directory)