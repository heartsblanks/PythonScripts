import os

def get_tool_install_directory(tool_name, install_directory):
    for folder in os.listdir(install_directory):
        if tool_name.lower() in folder.lower():
            if os.path.isdir(os.path.join(install_directory, folder)):
                return os.path.join(install_directory, folder)

    return None

# Example usage:
tool_name = "Putty"  # Change this to the tool you're looking for
install_directory = "C:\\Program Files"  # Change this to the actual install directory

tool_install_directory = get_tool_install_directory(tool_name, install_directory)
if tool_install_directory:
    print(f"Install directory for {tool_name} is: {tool_install_directory}")
else:
    print(f"{tool_name} not found in {install_directory}")