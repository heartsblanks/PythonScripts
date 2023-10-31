import xmltodict

# Parse the XML using xmltodict
with open("your_message_flow.xml", "r") as xml_file:
    xml_data = xml_file.read()
    message_flow_data = xmltodict.parse(xml_data)

# Create a dictionary to store node positions
node_positions = {}

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
    else:
        # Check if all connections are to the same target node
        same_target = all(target_node == conn['@targetNode'] for conn in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['connections'] if conn['@sourceNode'] == source_node)
        if same_target:
            x_position = node_positions[target_node][0] + x_offset
            y_position = node_positions[target_node][1]
        else:
            existing_targets = [t for t in node_positions if node_positions[t][1] < node_positions[source_node][1]]
            num_existing_targets = len(existing_targets)
            if num_existing_targets == 0:
                x_position = node_positions[source_node][0] + x_offset
                y_position = node_positions[source_node][1] - y_offset
            elif num_existing_targets == 1:
                x_position = node_positions[source_node][0] + x_offset
                y_position = node_positions[source_node][1] + y_offset
            else:
                x_position = node_positions[source_node][0] + (num_existing_targets - 1) * x_offset
                y_position = node_positions[source_node][1] - y_offset

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