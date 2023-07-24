import xmltodict

def increment_location(location, x_increment, y_increment):
    x, y = map(int, location.split(','))
    new_x = x + x_increment
    new_y = y + y_increment
    return f"{new_x},{new_y}"

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
for index, start_node_id in enumerate(start_nodes, start=1):
    start_node = None
    for node in top_level_nodes:
        if node['@xmi:id'] == start_node_id:
            start_node = node
            break
    if start_node:
        current_location = start_node['@location']
        new_location = increment_location(current_location, 50 * index, 0)
        start_node['@location'] = new_location

# Follow connections and assign new locations to connected nodes
for start_node_id in start_nodes:
    current_node_id = start_node_id

    while current_node_id:
        # Find the current node using its ID
        current_node = None
        for node in top_level_nodes:
            if node['@xmi:id'] == current_node_id:
                current_node = node
                break

        # If current node exists, assign a new location to its connected nodes
        if current_node:
            current_location = current_node['@location']
            new_location = increment_location(current_location, 50, 0)

            # Find the target nodes from connections and update their locations
            target_node_ids = [
                connection['@targetNode'] for connection in connections
                if connection['@sourceNode'] == current_node_id
            ]

            for target_node_id in target_node_ids:
                for target_node in top_level_nodes:
                    if target_node['@xmi:id'] == target_node_id:
                        target_node['@location'] = new_location

            # Move to the first target node for the next iteration
            if target_node_ids:
                current_node_id = target_node_ids[0]
            else:
                # If there are no target nodes, exit the loop
                break

# Convert the updated data back to XML format
updated_xml = xmltodict.unparse(parsed_data, pretty=True)

# Write the updated XML content to the file
with open('updated_msgflow.xml', 'w') as file:
    file.write(updated_xml)