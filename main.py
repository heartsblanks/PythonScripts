import xmltodict

# Parse the XML using xmltodict
with open("your_message_flow.xml", "r") as xml_file:
    xml_data = xml_file.read()
    message_flow_data = xmltodict.parse(xml_data)

# Create a dictionary to store node positions
node_positions = {}

# Analyze connections and calculate node positions
y_offset = 50  # Vertical offset between nodes
current_x = 50  # Initial horizontal position

for connection in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['connections']:
    source_node = connection['@sourceNode']
    target_node = connection['@targetNode']

    # If the source node is not in the dictionary, add it at the current position
    if source_node not in node_positions:
        node_positions[source_node] = (current_x, 0)
        current_x += 150  # Adjust horizontal spacing

    # If the target node is not in the dictionary, add it below the source node
    if target_node not in node_positions:
        y_position = node_positions[source_node][1] - y_offset
        node_positions[target_node] = (node_positions[source_node][0], y_position)

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