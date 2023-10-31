import xmltodict

# Parse the XML using xmltodict
with open("your_message_flow.xml", "r") as xml_file:
    xml_data = xml_file.read()
    message_flow_data = xmltodict.parse(xml_data)

# Create a dictionary to store node positions
node_positions = {}

# Create a dictionary to keep track of connections to each target node
target_connections = {}

# Analyze connections and calculate node positions
x_offset = 150  # Horizontal offset between nodes
y_offset = 100  # Vertical offset for multiple connections
current_y = 100  # Initial vertical position

for connection in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['connections']:
    source_node = connection['@sourceNode']
    target_node = connection['@targetNode']

    if source_node not in node_positions:
        node_positions[source_node] = (0, current_y)
        current_y += 100  # Adjust vertical spacing for single connections

    if target_node not in node_positions:
        x_position = node_positions[source_node][0] + x_offset
        node_positions[target_node] = (x_position, node_positions[source_node][1])
        target_connections[target_node] = [connection]
    else:
        if target_node in target_connections:
            target_connections[target_node].append(connection)
        else:
            target_connections[target_node] = [connection]

# Update positions for target nodes with multiple connections
for target_node, connections in target_connections.items():
    if len(connections) > 1:
        source_node = connections[0]['@sourceNode']
        x_position = node_positions[source_node][0]
        y_position = node_positions[source_node][1]

        for i, connection in connections:
            if i == 0:
                # First connection stays on the right
                x_position += x_offset
            elif i == 1:
                # Second connection goes above
                y_position += y_offset
            else:
                # Additional connections go below
                y_position -= y_offset
            node_positions[target_node] = (x_position, y_position)

# Update node locations in the XML
for node in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['nodes']:
    node_id = node['@xmi:id']
    x, y = node_positions[node_id]
    node['@location'] = f"{int(x)},{int(y)}"

# Serialize the updated XML
updated_xml = xmltodict.unparse(message_flow_data, pretty=True)

# Save the updated XML
with open("updated_message_flow.xml", "w") as updated_xml_file:
    updated_xml_file.write(updated_xml)