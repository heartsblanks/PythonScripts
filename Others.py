import paramiko
import select

# create SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to remote host
ssh_client.connect(hostname='your_host', username='your_username', password='your_password')

# open SSH channel
ssh_channel = ssh_client.invoke_shell()

# consume any data before executing mqsireportproperties
while ssh_channel.recv_ready():
    ssh_channel.recv(1024)

# execute mqsireportproperties command
command = 'mqsireportproperties <brokername> -o HTTPConnector -b httplistener -a | awk -F "[= ]" "/port/{print $4}"'
ssh_channel.send(command + '\n')

# wait until there is data to read
while not ssh_channel.recv_ready():
    select.select([ssh_channel], [], [], 1)

# consume any data before the mqsireportproperties output
while ssh_channel.recv_ready():
    ssh_channel.recv(1024)

# read the mqsireportproperties output
output = ''
while ssh_channel.recv_ready():
    output += ssh_channel.recv(1024).decode('utf-8')

# print the output
print(output.strip())

# close SSH channel and client
ssh_channel.close()
ssh_client.close()
