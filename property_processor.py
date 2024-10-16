import re
from collections import defaultdict

def parse_env_properties(file_path):
    # Dictionary to store different categories of properties
    properties = {
        "integration_server": None,
        "queues": set(),  # Store unique queue names ending with _EVT, _ERR, or _CPY
        "database_names": defaultdict(dict),  # Store {property_name: {environment: value}}
        "property_values": defaultdict(dict)  # Store {property_name: {environment: value}}
    }
    
    # Define regex patterns
    integration_server_pattern = re.compile(r"^prod\.broker\.eg=(.+)$", re.MULTILINE)
    queue_pattern = re.compile(r"=(.+?(_EVT|_ERR|_CPY))$", re.MULTILINE)
    db_property_pattern = re.compile(r"^(?P<env>\w+)\.replace\.replacement\.17=(?P<value>.+)$", re.MULTILINE)
    dynamic_property_pattern = re.compile(r"^(?P<env>\w+)?\.?replace\.replacement\.(?P<prop_num>\d+)=(?P<value>.+)$", re.MULTILINE)
    prop_value_pattern = re.compile(r"^replace\.value\.(?P<num>\d+)=(?P<property_name>.+)$", re.MULTILINE)

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

    # 3. Specific Database Property ({RPL_DB00}) for `replace.replacement.17`
    db_property_name = "{RPL_DB00}"
    for match in db_property_pattern.finditer(content):
        env = match.group("env")
        properties["database_names"][db_property_name][env] = match.group("value").strip()

    # 4. Dynamic Properties (replace.value.<num> for each property, environment-specific values)
    for match in prop_value_pattern.finditer(content):
        num = match.group("num")  # Number, like "23" in replace.value.23
        property_name = match.group("property_name").strip()

        # Find all env-specific or common values for this property
        for env_match in dynamic_property_pattern.finditer(content):
            env = env_match.group("env") or "common"  # Use "common" if no environment prefix
            prop_num = env_match.group("prop_num")
            value = env_match.group("value").strip()

            # Only process if it matches the current property number
            if prop_num == num:
                # Check if the property is a database property (contains "RPL_DB")
                if "RPL_DB" in property_name:
                    properties["database_names"][property_name][env] = value
                else:
                    properties["property_values"][property_name][env] = value

    return properties

# Usage example
properties = parse_env_properties('your_properties_file.properties')

# Access the parsed data
print("Integration Server:", properties["integration_server"])
print("Queues:", properties["queues"])
print("Database Names:", properties["database_names"])  # Organized by {property_name: {env: value}}
print("Property Values:", properties["property_values"])
