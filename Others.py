import xmltodict

def increment_location(location, x, y):
    x_value, y_value = map(int, location.split(','))
    new_x = x_value + x
    new_y = y_value + y
    return f"{new_x},{new_y}"

def adjust_node_location(node_id, y_offset, target_nodes, nodes_with_connections, node_locations):
    node = next(node for node in nodes_with_connections if node['@xmi:id'] == node_id)
    location = node['@location']
    
    if node_id not in target_nodes:
        node_locations[node_id] = location
        y_offset += 50
    
    for connection in nodes_with_connections[node]['connections']:
        if connection['@sourceNode'] == node_id and connection['@sourceTerminalName'] != 'InTerminal.in':
            target_node_id = connection['@targetNode']
            if target_node_id in target_nodes:
                node_locations[target_node_id] = increment_location(node_locations[node_id], 0, y_offset)
                y_offset += 50
            else:
                adjust_node_location(target_node_id, y_offset, target_nodes, nodes_with_connections, node_locations)

def update_node_locations(file_path):
    # Read the XML data from the file
    with open(file_path, 'r') as file:
        xml_data = file.read()

    # Parse the XML data using xmltodict
    parsed_data = xmltodict.parse(xml_data)

    # Find all nodes with connections
    nodes_with_connections = parsed_data['ecore:EPackage']['eClassifiers']['composition']['nodes']

    # Extract the target nodes of each connection
    target_nodes = set(connection['@targetNode'] for node in nodes_with_connections for connection in node.get('connections', []))

    # Create a dictionary to store the node locations
    node_locations = {}

    # Handle each node
    for node in nodes_with_connections:
        node_id = node['@xmi:id']
        adjust_node_location(node_id, 0, target_nodes, parsed_data['ecore:EPackage']['eClassifiers']['composition'], node_locations)

    # Update the locations in the parsed_data dictionary
    for node in nodes_with_connections:
        node_id = node['@xmi:id']
        if node_id in node_locations:
            node['@location'] = node_locations[node_id]

    # Convert the updated data back to XML format
    updated_xml = xmltodict.unparse(parsed_data, pretty=True)

    # Write the updated XML content to the file
    with open('updated_msgflow.xml', 'w') as file:
        file.write(updated_xml)

# Prompt the user to input the file name
file_name = input("Enter the XML file name: ")
update_node_locations(file_name)