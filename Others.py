mqsireportproperties <brokername> -o HTTPConnector -b httplistener -a | awk -F "=" '/^[[:space:]]*port/ {gsub(/"/, "", $2); gsub(/^ */, "", $2); print $2}'
import paramiko

# Connect to the remote server using SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('remote_host', username='remote_user', password='password')

# Execute the command and read the output
command = 'mqsireportproperties <brokername> -o HTTPConnector -b httplistener -a | awk -F "=" \'/^[[:space:]]*port/ {{gsub(/"/, "", $2); gsub(/^ */, "", $2); print $2}}\''
ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('bash -l -c "{}"'.format(command), get_pty=True)

# Clear any existing data in the channel buffer
while ssh_stdout.channel.recv_ready():
    ssh_stdout.channel.recv(1024)

# Read the output from the command
output = ssh_stdout.read().decode().strip()

# Print the output
print(output)

# Close the SSH connection
ssh_client.close()
