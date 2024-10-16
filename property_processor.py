import re
from collections import defaultdict

def parse_env_properties(file_path):
    # Initialize dictionaries to store different categories of properties
    properties = {
        "integration_server": None,
        "queues": defaultdict(list),   # To store _EVT, _ERR, _CPY queue names per environment
        "database_names": defaultdict(dict),  # replace.replacement.17 values per environment
        "property_values": defaultdict(dict)  # replace.value.XX with env-specific or common values
    }
    
    # Define regex patterns
    integration_server_pattern = re.compile(r"^prod\.broker\.eg=(.+)$", re.MULTILINE)
    queue_pattern = re.compile(r"^(?P<env>\w+)\.(?P<queue_name>[\w.]+)=(?P<value>.+)$", re.MULTILINE)
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

    # 2. Queue Names (_EVT, _ERR, _CPY for each environment)
    for match in queue_pattern.finditer(content):
        queue_name = match.group("queue_name")
        if queue_name.endswith(("_EVT", "_ERR", "_CPY")):
            env = match.group("env")
            properties["queues"][env].append(match.group("value").strip())

    # 3. Database Names (replace.replacement.17 per environment)
    for match in database_pattern.finditer(content):
        env = match.group("env")
        properties["database_names"][env]["replace.replacement.17"] = match.group("value").strip()

    # 4. Property Values (replace.value.XX and replace.replacement.XX per environment)
    for match in prop_value_pattern.finditer(content):
        env = match.group("env") or "common"  # Use "common" for env-agnostic values
        prop_num = match.group("prop_num")
        value = match.group("value").strip()
        properties["property_values"][env][f"replace.value.{prop_num}"] = value

    # Remove any duplicates from `queues` when processing property values
    processed_queues = {f"{env}.{name}" for env, names in properties["queues"].items() for name in names}

    for match in property_pattern.finditer(content):
        env = match.group("env") or "common"  # Use "common" for env-agnostic values
        prop_num = match.group("prop_num")
        key = f"replace.replacement.{prop_num}"
        
        if key not in processed_queues:
            properties["property_values"][env][key] = match.group("value").strip()

    return properties

# Usage Example
properties = parse_env_properties('your_properties_file.properties')

# Access the parsed data
print("Integration Server:", properties["integration_server"])
print("Queues:", properties["queues"])
print("Database Names:", properties["database_names"])
print("Property Values:", properties["property_values"])
