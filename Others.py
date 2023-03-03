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
