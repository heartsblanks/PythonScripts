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

# Sort start nodes based on their Y location value
start_nodes.sort(key=lambda node_id: int([node['@location'].split(',')[1] for node in top_level_nodes if node['@xmi:id'] == node_id][0]))

# Assign unique locations to start nodes
y_increment = 20
for start_node_id in start_nodes:
    start_node = next(node for node in top_level_nodes if node['@xmi:id'] == start_node_id)
    current_location = start_node['@location']
    new_location = increment_location(current_location, 0, y_increment)
    start_node['@location'] = new_location
    y_increment += 100

# Follow connections and assign new locations to connected nodes
for start_node_id in start_nodes:
    current_node_id = start_node_id

    # Create a dictionary to store the target nodes and their Y increments
    target_node_positions = {}

    while current_node_id:
        # Find the current node using its ID
        current_node = next(node for node in top_level_nodes if node['@xmi:id'] == current_node_id)

        # If current node exists, assign a new location to its connected nodes
        if current_node:
            current_location = current_node['@location']
            new_location = increment_location(current_location, 50, 0)

            # Find the target nodes from connections and update their locations
            target_node_ids = [
                connection['@targetNode'] for connection in connections
                if connection['@sourceNode'] == current_node_id
            ]

            # Check if all target nodes are the same
            all_same_target = len(set(target_node_ids)) == 1

            for i, target_node_id in enumerate(target_node_ids, start=1):
                for target_node in top_level_nodes:
                    if target_node['@xmi:id'] == target_node_id:
                        if all_same_target:
                            target_location = increment_location(new_location, 0, 0)
                        else:
                            target_location = increment_location(new_location, 0, -50 + (i - 1) * 50)

                        target_node['@location'] = target_location

                        # Store the target node and its Y increment in the dictionary
                        target_node_positions[target_node_id] = -50 + (i - 1) * 50

            # Move to the first target node for the next iteration
            if target_node_ids:
                current_node_id = target_node_ids[0]
            else:
                # If there are no target nodes, exit the loop
                break

    # Update the Y increments for all target nodes connected to the same node
    for target_node_id in target_node_positions:
        for target_node in top_level_nodes:
            if target_node['@xmi:id'] == target_node_id:
                current_location = target_node['@location']
                x, y = map(int, current_location.split(','))
                new_y = y + target_node_positions[target_node_id]
                target_node['@location'] = f"{x},{new_y}"

# Convert the updated data back to XML format
updated_xml = xmltodict.unparse(parsed_data, pretty=True)

# Write the updated XML content to the file
with open('updated_msgflow.xml', 'w') as file:
    file.write(updated_xml)