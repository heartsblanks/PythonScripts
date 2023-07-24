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

# Sort start nodes based on y location in ascending order
start_nodes = [node['@xmi:id'] for node in top_level_nodes if not any(connection['@targetNode'] == node['@xmi:id'] for connection in connections)]
start_nodes.sort(key=lambda node_id: int([node['@location'].split(',')[1] for node in top_level_nodes if node['@xmi:id'] == node_id][0]))

# Assign unique locations to start nodes
y_increment = 300
updated_nodes = set()
target_node_positions = {}

for i, start_node_id in enumerate(start_nodes):
    if i == 0:
        new_location = "0,20"
        y_location = 20
    else:
        new_location = f"0,{y_location + i * y_increment}"

    start_node = next(node for node in top_level_nodes if node['@xmi:id'] == start_node_id)
    start_node['@location'] = new_location

    # Follow connections and assign new locations to connected nodes
    current_node_id = start_node_id

    while current_node_id:
        # Find the current node using its ID
        current_node = next(node for node in top_level_nodes if node['@xmi:id'] == current_node_id)

        # If current node exists and hasn't been updated yet, assign a new location to its connected nodes
        if current_node_id not in updated_nodes:
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
                    if target_node['@xmi:id'] == target_node_id and target_node_id not in updated_nodes:
                        if all_same_target:
                            target_location = increment_location(new_location, 0, 0)
                        else:
                            target_location = increment_location(new_location, 0, target_node_positions.get(target_node_id, -50 + (i - 1) * 50))

                        target_node['@location'] = target_location

                        # Store the target node and its Y increment in the dictionary
                        if not all_same_target:
                            target_node_positions[target_node_id] = -50 + (i - 1) * 50

                        # Add the target node to the updated_nodes set
                        updated_nodes.add(target_node_id)

            # Add the current node to the updated_nodes set
            updated_nodes.add(current_node_id)

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