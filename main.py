import xmltodict
import matplotlib.pyplot as plt

# Parse the XML using xmltodict
with open("your_message_flow.xml", "r") as xml_file:
    xml_data = xml_file.read()
    message_flow_data = xmltodict.parse(xml_data)

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Extract nodes and connections
node_positions = {}
for node in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['nodes']:
    node_id = node['@xmi:id']
    location = node['@location'].split(',')
    x, y = map(float, location)
    node_positions[node_id] = (x, y)
    ax.annotate(node_id, (x, y))  # Add node IDs as labels

for connection in message_flow_data['ecore:EPackage']['eClassifiers']['composition']['connections']:
    source_node = connection['@sourceNode']
    target_node = connection['@targetNode']
    x1, y1 = node_positions[source_node]
    x2, y2 = node_positions[target_node]
    ax.plot([x1, x2], [y1, y2], 'b-')  # Draw lines for connections

# Customize the layout as needed

plt.axis('off')  # Turn off axes
plt.show()  # Display the layout

# You can save the figure as an image or update the XML with the new positions