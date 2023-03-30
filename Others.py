command = "mqsireportproperties {} -o HTTPConnector -b httplistener -a | awk -F= '/^[[:space:]]*port/ {{gsub(/[\\\"'']*/, \"\", $2); gsub(/^ */, \"\", $2); print $2}}'".format(brokername)
ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('bash -l -c "{}"'.format(command), get_pty=True)
