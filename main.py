import xmltodict

# Parse the XML using xmltodict
with open("your_message_flow.xml", "r") as xml_file:
    xml_data = xml_file.read()
    message_flow_data = xmltodict.parse(xml_data)

# Create a dictionary to store node positions
node_positions = {}

# Create a dictionary to keep track of connections for each source node
source_connections = {}

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

    if source_node in source_connections:
        source_connections[source_node].append(connection)
    else:
        source_connections[source_node] = [connection]

# Function to check if a node position overlaps with existing nodes
def is_overlapping(position, existing_positions):
    for pos in existing_positions:
        if abs(pos[0] - position[0]) <= 30 and abs(pos[1] - position[1]) <= 30:
            return True
    return False

# Arrange connections for each source node while avoiding overlaps
for source_node, connections in source_connections.items():
    x_position = node_positions[source_node][0]
    y_position = node_positions[source_node][1]

    # Collect connections to the same target node
    same_target_connections = [conn for conn in connections if conn['@targetNode'] == connections[0]['@targetNode']]

    if len(same_target_connections) > 1:
        y_offset_multiplier = 1
        for connection in same_target_connections:
            target_node = connection['@targetNode']
            new_position = (x_position + x_offset * y_offset_multiplier, y_position)
            while is_overlapping(new_position, list(node_positions.values())):
                new_position = (new_position[0], new_position[1] + y_offset)
            node_positions[target_node] = new_position
            y_offset_multiplier += 1
    else:
        for connection in connections:
            target_node = connection['@targetNode']
            new_position = (x_position, y_position)
            while is_overlapping(new_position, list(node_positions.values())):
                new_position = (new_position[0], new_position[1] + y_offset)
            node_positions[target_node] = new_position

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