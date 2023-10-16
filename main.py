import os
import subprocess
import ast
import concurrent.futures

def get_imports(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                yield n.name
        if isinstance(node, ast.ImportFrom):
            yield node.module

def is_package_installed(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def install_package(package_name):
    subprocess.run(["pip", "install", package_name])

def process_python_file(file_path):
    for package_name in get_imports(file_path):
        if not is_package_installed(package_name):
            print(f"{package_name} is not installed. Installing...")
            install_package(package_name)

directory_path = '/your/directory/path'

# Specify the number of concurrent workers
num_workers = 4

with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                executor.submit(process_python_file, file_path)