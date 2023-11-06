import subprocess
import string

# Define the network path you want to map
network_path = r"\\server\share"

# Check if the network path is already mapped
def is_path_mapped(network_path):
    result = subprocess.run("net use", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return network_path.lower() in result.stdout.lower()

# Find an available drive letter
def find_available_drive():
    used_drive_letters = [d[0] for d in string.ascii_uppercase if is_path_mapped(f"{d}:")]
    available_drive_letters = [d for d in string.ascii_uppercase if d not in used_drive_letters]

    if available_drive_letters:
        return available_drive_letters[0]
    else:
        return None

if is_path_mapped(network_path):
    print(f"The network path {network_path} is already mapped.")
else:
    available_drive_letter = find_available_drive()
    if available_drive_letter:
        map_command = f"net use {available_drive_letter}: {network_path}"
        try:
            subprocess.run(map_command, shell=True, check=True)
            print(f"Mapped {available_drive_letter}: to {network_path}.")
        except subprocess.CalledProcessError:
            print(f"Failed to map {available_drive_letter}: to {network_path}.")
    else:
        print("No available drive letters to map the network path.")