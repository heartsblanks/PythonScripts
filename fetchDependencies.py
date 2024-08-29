import concurrent.futures
import paramiko
import json

class SSHExecutor:
    def __init__(self, hostname, username, private_key_path):
        self.hostname = hostname
        self.username = username
        self.private_key_path = private_key_path
        self.ssh = self._create_ssh_connection()

    def _create_ssh_connection(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(self.private_key_path)
        ssh.connect(self.hostname, username=self.username, pkey=private_key)
        return ssh

    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode().strip()

    def close(self):
        self.ssh.close()

def get_project_dependencies(ssh_executor, project_dir):
    dependencies = []

    # Fetch dependencies from the .project,v file
    project_command = f"awk '/<projects>/,/<\\/projects>/' {project_dir}/.project,v | grep '<project>' | awk -F'[<>]' '{{print $3}}'"
    project_output = ssh_executor.execute_command(project_command)
    if project_output:
        dependencies.extend(project_output.splitlines())

    # Fetch dependencies from the .classpath,v file
    classpath_command = f"grep -oP '<classpathentry[^>]*? path=\"/[^\\\"]*\"' {project_dir}/.classpath,v | awk -F'path=\"/' '{{print $2}}' | awk -F'\"' '{{print $1}}'"
    classpath_output = ssh_executor.execute_command(classpath_command)
    if classpath_output:
        dependencies.extend(classpath_output.splitlines())

    return dependencies

def generate_dependency_report(hostname, username, private_key_path, project_dirs):
    """Generate a JSON report of projects grouped by their dependencies."""
    dependency_map = {}

    with SSHExecutor(hostname, username, private_key_path) as ssh_executor:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_project = {executor.submit(get_project_dependencies, ssh_executor, project_dir): project_dir for project_dir in project_dirs}

            for future in concurrent.futures.as_completed(future_to_project):
                project_dir = future_to_project[future]
                try:
                    dependencies = future.result()
                    project_name = project_dir.split('/')[-1]

                    for dep in dependencies:
                        if dep not in dependency_map:
                            dependency_map[dep] = []
                        dependency_map[dep].append(project_name)
                except Exception as e:
                    print(f"Error processing {project_dir}: {e}")

    # Save the report as a JSON file
    with open('dependency_report.json', 'w') as json_file:
        json.dump(dependency_map, json_file, indent=4)

    print("Dependency report generated: dependency_report.json")

# Example usage with a list of directories
project_dirs = [f"/projects/project_{i}" for i in range(1500)]  # Replace with actual directory paths
generate_dependency_report('hostname', 'username', 'Z:\\.ssh\\id_rsa', project_dirs)