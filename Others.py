import xmltodict

def replace_node_entry(data, old_node_tag, new_node_tag, new_node_details):
    nodes = data['ecore:EPackage'].get('composition', {}).get('nodes', [])
    for node in nodes:
        if node.get('@xmi:type') == old_node_tag:
            node['@xmi:type'] = new_node_tag
            node['@xmi:id'] = new_node_details['xmi:id']
            node['@location'] = new_node_details['location']
            node['translation']['@string'] = new_node_details['translation']
            node['@xmlns'] = data['ecore:EPackage']['@xmlns']
            node['@xmlns:xmi'] = data['ecore:EPackage']['@xmlns:xmi']
            node['@xmlns:eflow'] = data['ecore:EPackage']['@xmlns:eflow']
            node['@xmlns:utility'] = data['ecore:EPackage']['@xmlns:utility']
            node['@xmlns:ComIbmLabel.msgnode'] = data['ecore:EPackage']['@xmlns:ComIbmLabel.msgnode']
            break

    return data

# Sample replaced node entry details with label name
new_node_details = {
    'xmi:id': 'FCMComposite_1_9',  # Replace with the new node ID
    'xmi:type': 'MQINPUT_SF.subflow:FCMComposite_1',
    'location': '400,300',
    'translation': 'MQ Input SF',  # Update the translation value directly without xmi:type and single quotes
    # Include other attributes for the new node details if necessary
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