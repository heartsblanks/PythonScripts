import re
from collections import defaultdict

def parse_env_properties(file_path):
    # Dictionary to store different categories of properties
    properties = {
        "integration_server": None,
        "queues": set(),  # Store unique queue names ending with _EVT, _ERR, or _CPY
        "database_names": {},  # Only store {environment: database_value} for replace.replacement.17
        "property_values": defaultdict(dict)  # replace.value.XX with env-specific or common values
    }
    
    # Define regex patterns
    integration_server_pattern = re.compile(r"^prod\.broker\.eg=(.+)$", re.MULTILINE)
    queue_pattern = re.compile(r"=(.+?(_EVT|_ERR|_CPY))$", re.MULTILINE)
    database_pattern = re.compile(r"^(?P<env>\w+)\.replace\.replacement\.17=(?P<value>.+)$", re.MULTILINE)
    property_pattern = re.compile(r"^(?P<env>\w+)?\.?replace\.replacement\.(?P<prop_num>\d+)=(?P<value>.+)$", re.MULTILINE)
    prop_value_pattern = re.compile(r"^(?P<env>\w+)?\.replace\.value\.(?P<prop_num>\d+)=(?P<value>.+)$", re.MULTILINE)

    # Read file content
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Integration Server (prod.broker.eg)
    match = integration_server_pattern.search(content)
    if match:
        properties["integration_server"] = match.group(1).strip()

    # 2. Queue Names (_EVT, _ERR, _CPY)
    for match in queue_pattern.finditer(content):
        queue_name = match.group(1).strip()
        properties["queues"].add(queue_name)

    # 3. Database Names (replace.replacement.17 per environment)
    for match in database_pattern.finditer(content):
        env = match.group("env")
        properties["database_names"][env] = match.group("value").strip()

    # 4. Property Values (replace.value.XX and replace.replacement.XX per environment)
    for match in prop_value_pattern.finditer(content):
        env = match.group("env") or "common"  # Use "common" for env-agnostic values
        prop_num = match.group("prop_num")
        value = match.group("value").strip()
        properties["property_values"][env][f"replace.value.{prop_num}"] = value

    # Process other replacements while excluding identified queues
    processed_queues = {f"replace.replacement.{num}" for num in properties["queues"]}
    for match in property_pattern.finditer(content):
        env = match.group("env") or "common"  # Use "common" for env-agnostic values
        prop_num = match.group("prop_num")
        key = f"replace.replacement.{prop_num}"
        
        # Only add if it's not one of the known queues
        if key not in processed_queues:
            properties["property_values"][env][key] = match.group("value").strip()

    return properties

# Usage example
properties = parse_env_properties('your_properties_file.properties')

# Access the parsed data
print("Integration Server:", properties["integration_server"])
print("Queues:", properties["queues"])
print("Database Names:", properties["database_names"])  # Now simpler with {environment: database_value}
print("Property Values:", properties["property_values"])
