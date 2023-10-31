import networkx as nx
import xmltodict

# Parse the XML using xmltodict
with open("your_message_flow.xml", "r") as xml_file:
    xml_data = xml_file.read()
    message_flow_data = xmltodict.parse(xml_data)

# Create a graph
G = nx.Graph()

# Extract nodes and connections
for node in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['nodes']:
    node_id = node['@xmi:id']
    location = node['@location']
    G.add_node(node_id, location=location)

for connection in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['connections']:
    source_node = connection['@sourceNode']
    target_node = connection['@targetNode']
    G.add_edge(source_node, target_node)

# Layout the graph (you might need a custom layout algorithm)
pos = nx.spring_layout(G)

# Update node locations in the XML
for node in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['nodes']:
    node_id = node['@xmi:id']
    x, y = pos[node_id].tolist()
    node['@location'] = f"{int(x)},{int(y)}"

# Serialize the updated XML
updated_xml = xmltodict.unparse(message_flow_data, pretty=True)

# Save the updated XML
with open("updated_message_flow.xml", "w") as updated_xml_file:
    updated_xml_file.write(updated_xml)