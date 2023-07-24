import xmltodict

def increment_location(location, x, y):
    x_value, y_value = map(int, location.split(','))
    new_x = x_value + x
    new_y = y_value + y
    return f"{new_x},{new_y}"

def adjust_node_location(node_id, y_offset, target_nodes, node_locations):
    node = next(node for node in nodes_with_connections if node['@xmi:id'] == node_id)
    location = node['@location']
    
    if node_id not in target_nodes:
        node['@location'] = increment_location(location, 50, y_offset)
        y_offset += 50
    
    for connection in node.get('connections', []):
        if connection['@sourceNode'] == node_id and connection['@sourceTerminalName'] != 'InTerminal.in':
            target_node_id = connection['@targetNode']
            if target_node_id in target_nodes:
                target_node = next(node for node in nodes_with_connections if node['@xmi:id'] == target_node_id)
                target_node['@location'] = increment_location(location, 0, y_offset)
                y_offset += 50
            else:
                adjust_node_location(target_node_id, y_offset, target_nodes, node_locations)

def update_node_locations(file_path):
    # Read the XML data from the file
    with open(file_path, 'r') as file:
        xml_data = file.read()

    # Parse the XML data using xmltodict
    parsed_data = xmltodict.parse(xml_data)

    # Find all nodes with connections
    nodes_with_connections = parsed_data['ecore:EPackage']['eClassifiers']['composition']['nodes']

    # Identify start nodes
    start_nodes = set()
    for node in nodes_with_connections:
        node_id = node['@xmi:id']
        for connection in node.get('connections', []):
            target_node_id = connection['@targetNode']
            start_nodes.discard(target_node_id)
            start_nodes.add(node_id)

    # Process nodes in sequence
    node_locations = {}
    for node_id in start_nodes:
        adjust_node_location(node_id, 0, start_nodes, node_locations)

    # Convert the updated data back to XML format
    updated_xml = xmltodict.unparse(parsed_data, pretty=True)

    # Write the updated XML content to the file
    with open('updated_msgflow.xml', 'w') as file:
        file.write(updated_xml)

# Prompt the user to input the file name
file_name = input("Enter the XML file name: ")
update_node_locations(file_name)