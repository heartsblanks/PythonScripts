import xmltodict

def get_max_node_id(data):
    max_id = 0
    nodes = data['ecore:EPackage'].get('composition', {}).get('nodes', [])
    for node in nodes:
        node_id = int(node['@xmi:id'].split('_')[-1])
        max_id = max(max_id, node_id)
    return max_id

def create_new_node(new_node_tag, new_node_details, namespaces):
    new_node = {
        '@xmi:type': new_node_tag,
        '@xmi:id': new_node_details['xmi:id'],
        '@location': new_node_details['location'],
        'translation': {
            '@xmi:type': 'utility:ConstantString',
            '@string': new_node_details['translation']
        }
    }
    return new_node

def replace_node_entry(data, old_node_tag, new_node_tag, new_node_details):
    max_id = get_max_node_id(data)
    new_node_details['xmi:id'] = f'FCMComposite_1_{max_id + 1}'

    nodes = data['ecore:EPackage'].get('composition', {}).get('nodes', [])
    for node in nodes:
        if node.get('@xmi:type') == old_node_tag:
            new_node = create_new_node(new_node_tag, new_node_details, data['ecore:EPackage']['@xmlns'])
            nodes.insert(0, new_node)
            break

    return data

# Sample replaced node entry details with label name
new_node_details = {
    'xmi:id': '',  # Replace with the new node ID after finding the maximum existing node ID and incrementing by 1
    'xmi:type': 'MQINPUT_SF.subflow:FCMComposite_1',
    'location': '400,300',
    'translation': 'MQ Input SF',  # Update the translation value directly without xmi:type and single quotes
    'labelName': 'postSum',  # Include the labelName attribute in the new node details
    # Add other details for the new node entry here
}

# Read the XML data from the file
with open('your_file.xml', 'r') as file:
    xml_data = file.read()

# Parse the XML data using xmltodict
parsed_data = xmltodict.parse(xml_data)

# Run the replace_node_entry function with the updated new_node_details
updated_data = replace_node_entry(parsed_data, 'Sum_APIInputCatchHandler.subflow:FCMComposite_1', 'MQINPUT_SF.subflow:FCMComposite_1', new_node_details)

# Convert the updated data back to XML format
updated_xml = xmltodict.unparse(updated_data, pretty=True)

# Write the updated XML content to the file
with open('updated_msgflow.xml', 'w') as file:
    file.write(updated_xml)