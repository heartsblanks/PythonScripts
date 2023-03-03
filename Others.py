import subprocess

# Define the command to execute
ssh_app = '/path/to/ssh/app'
deploy_login = 'user@host'
user_password = 'password'
command = f'echo {user_password} | sudodeploy -encrypt 2>/dev/null | tail -n1'

# Execute the command and capture its output
output = subprocess.run([ssh_app, deploy_login, '-batch', command], capture_output=True, text=True).stdout.strip()

# Parse the output to extract the encrypted password
encrypted = output.split('=')[1].strip()

# Set the encrypted password as an environment variable
import os
os.environ['ENCRYPTED'] = encrypted

import subprocess

# Define the PLINK command to execute
plink_path = 'C:/path/to/plink.exe'
putty_private_key = 'C:/path/to/putty-private-key.ppk'
plink_command = f'{plink_path} -no-antispoof -i {putty_private_key} user@host command-to-execute'

# Execute the command and capture its output
output = subprocess.run(plink_command, capture_output=True, text=True).stdout.strip()

# Print the output
print(output)

command = f'{PLINK_PATH} -no-antispoof -i {PUTTY_PRIVATE_KEY} user@host "echo {USER_PASSWORD} | sudodeploy -encrypt 2>/dev/null | tail -n1"'



