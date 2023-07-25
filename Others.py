import xmltodict

def increment_location(location, x_increment, y_increment):
    x, y = map(int, location.split(','))
    new_x = x + x_increment
    new_y = y + y_increment
    return f"{new_x},{new_y}"

def update_node_locations(node_id, x_increment, y_increment):
    current_node = next((node for node in top_level_nodes if node['@xmi:id'] == node_id), None)
    if current_node and node_id not in updated_nodes:
        current_location = current_node['@location']
        new_location = increment_location(current_location, x_increment, y_increment)
        current_node['@location'] = new_location
        updated_nodes.add(node_id)

        # Find downstream target nodes and sort them by target terminal name
        downstream_connections = [connection for connection in connections if connection['@sourceNode'] == node_id]
        downstream_target_nodes = sorted(set(connection['@targetNode'] for connection in downstream_connections),
                                         key=lambda target_node_id: next(connection['@targetTerminalName'] for connection in connections if connection['@targetNode'] == target_node_id))

        # Recursively update locations for downstream target nodes
        for i, target_node_id in enumerate(downstream_target_nodes):
            target_node = next((node for node in top_level_nodes if node['@xmi:id'] == target_node_id), None)
            if target_node:
                all_same_target = all(connection['@targetNode'] == target_node_id for connection in downstream_connections)
                y_increment_value = target_node_positions.get(target_node_id, 0)

                # Adjust Y increment based on the number of downstream target nodes and their positions
                if not all_same_target:
                    y_increment_value = -50 + (i - 1) * 50

                update_node_locations(target_node_id, 0, y_increment_value)

# Read the XML data from the file
with open('your_msgflow_file.xml', 'r') as file:
    xml_data = file.read()

# Parse the XML data using xmltodict
parsed_data = xmltodict.parse(xml_data)

# Get the nodes and connections
top_level_nodes = parsed_data['ecore:EPackage']['eClassifiers']['composition']['nodes']
connections = parsed_data['ecore:EPackage']['eClassifiers']['composition']['connections']

# Find the start nodes (nodes without input connections)
start_nodes = []
for node in top_level_nodes:
    node_id = node['@xmi:id']
    if not any(connection['@targetNode'] == node_id for connection in connections):
        start_nodes.append(node_id)

# Assign unique locations to start nodes
updated_nodes = set()
target_node_positions = {}
for i, start_node_id in enumerate(start_nodes):
    start_node = next((node for node in top_level_nodes if node['@xmi:id'] == start_node_id), None)
    if start_node:
        y_increment_value = 20 + i * 100
        start_node['@location'] = f"0,{y_increment_value}"
        update_node_locations(start_node_id, 0, y_increment_value)

# Convert the updated data back to XML format
updated_xml = xmltodict.unparse(parsed_data, pretty=True)

# Write the updated XML content to the file
with open('updated_msgflow.xml', 'w') as file:
    file.write(updated_xml)