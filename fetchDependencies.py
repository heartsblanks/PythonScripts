import json

def get_project_dependencies(ssh_executor, project_dir):
    """Fetch dependencies from the .project,v and .classpath,v files for a given project directory."""
    dependencies = []

    # Use awk and grep to extract project dependencies from the .project,v file
    project_command = f"awk '/<projects>/,/<\\/projects>/' {project_dir}/.project,v | grep '<project>' | awk -F'[<>]' '{{print $3}}'"
    project_output = ssh_executor.execute_command(project_command)
    if project_output:
        dependencies.extend(project_output.strip().splitlines())

    # Use grep and awk to extract classpath dependencies from the .classpath,v file
    classpath_command = f"grep -oP '<classpathentry[^>]*? path=\"/[^\\\"]*\"' {project_dir}/.classpath,v | awk -F'path=\"/' '{{print $2}}' | awk -F'\"' '{{print $1}}'"
    classpath_output = ssh_executor.execute_command(classpath_command)
    if classpath_output:
        dependencies.extend(classpath_output.strip().splitlines())

    return dependencies

def generate_dependency_report(ssh_executor, project_dirs):
    """Generate a JSON report of projects grouped by their dependencies."""
    dependency_map = {}

    for project_dir in project_dirs:
        project_name = project_dir.split('/')[-1]
        dependencies = get_project_dependencies(ssh_executor, project_dir)

        for dep in dependencies:
            if dep not in dependency_map:
                dependency_map[dep] = []
            dependency_map[dep].append(project_name)

    # Save the report as a JSON file
    with open('dependency_report.json', 'w') as json_file:
        json.dump(dependency_map, json_file, indent=4)

    print("Dependency report generated: dependency_report.json")

# Example usage with a list of directories
project_dirs = [
    "/projects/ABC_project1",
    "/projects/XYZ_project2",
    "/projects/FGH_project3",
    # Add more projects as needed
]

# Assuming ssh_executor is an instance of a class that handles SSH connections and command execution
generate_dependency_report(ssh_executor, project_dirs)