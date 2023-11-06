import subprocess
import string

# Define the network path you want to check
network_path = r"\\server\share"

# Check if the network path is already mapped and return the drive letter
def get_mapped_drive(network_path):
    result = subprocess.run("net use", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        parts = line.split()
        if len(parts) >= 3 and parts[0].endswith(":") and parts[1].lower() == network_path.lower():
            return parts[0]
    return None

# Find an available drive letter
def find_available_drive():
    used_drive_letters = [d[0] for d in string.ascii_uppercase if get_mapped_drive(f"{d}:")]
    available_drive_letters = [d for d in string.ascii_uppercase if d not in used_drive_letters]

    if available_drive_letters:
        return available_drive_letters[0]
    else:
        return None

mapped_drive = get_mapped_drive(network_path)
if mapped_drive:
    print(f"The network path {network_path} is already mapped to drive {mapped_drive}.")
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