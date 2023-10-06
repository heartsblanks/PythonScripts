import os

def get_tool_install_directory_and_version(tool_name, install_directory):
    tool_install_directory = None
    latest_version = None

    for folder in os.listdir(install_directory):
        if tool_name.lower() in folder.lower() and os.path.isdir(os.path.join(install_directory, folder)):
            tool_install_directory = os.path.join(install_directory, folder)
            version_folders = sorted([subfolder for subfolder in os.listdir(tool_install_directory) if os.path.isdir(os.path.join(tool_install_directory, subfolder))], reverse=True)
            
            if version_folders:
                latest_version = version_folders[0]

    return tool_install_directory, latest_version

# Example usage:
tool_name = "ACE"  # Change this to the tool you're looking for
install_directory = "C:\\Program Files\\IBM"  # Change this to the actual install directory

install_dir, latest_version = get_tool_install_directory_and_version(tool_name, install_directory)

if install_dir:
    if latest_version:
        print(f"Install directory for {tool_name} is: {os.path.join(install_dir, latest_version)}")
    else:
        print(f"Install directory for {tool_name} is: {install_dir}")
else:
    print(f"{tool_name} not found in {install_directory}")