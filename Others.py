from lxml import etree

def get_max_node_id(data):
    max_id = 0
    for node in data.findall('.//nodes'):
        node_id = int(node.get('{http://www.omg.org/XMI}id').split('_')[-1])
        max_id = max(max_id, node_id)
    return max_id

def create_new_node(new_node_tag, new_node_details, namespaces):
    new_node = etree.Element(new_node_tag, nsmap=namespaces)
    for key, value in new_node_details.items():
        new_node.set(key, value)
    translation_element = etree.Element('translation', nsmap=namespaces)
    translation_element.set('string', new_node_details['translation'])
    new_node.append(translation_element)
    return new_node

def replace_node_entry(root, old_node_tag, new_node_tag, new_node_details):
    max_id = get_max_node_id(root)
    new_node_details['xmi:id'] = f'FCMComposite_1_{max_id + 1}'

    namespaces = {}
    for key, value in root.nsmap.items():
        if key is None:
            key = ''
        namespaces[key] = value

    updated_root = etree.Element(root.tag, nsmap=namespaces)
    for key, value in root.attrib.items():
        updated_root.set(key, value)

    for node in root.findall('.//nodes'):
        if node.get('xmi:type') == old_node_tag:
            new_node = create_new_node(new_node_tag, new_node_details, namespaces)
            updated_root.append(new_node)
        else:
            updated_root.append(node)

    return etree.ElementTree(updated_root)  # Return the updated ElementTree

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

# Parse the XML data using lxml
tree = etree.fromstring(xml_data)

# Run the replace_node_entry function with the updated new_node_details
updated_tree = replace_node_entry(tree, 'Sum_APIInputCatchHandler.subflow:FCMComposite_1', 'MQINPUT_SF.subflow:FCMComposite_1', new_node_details)

# Write the updated XML content to the file
with open('updated_msgflow.xml', 'wb') as file:
    file.write(etree.tostring(updated_tree, encoding='utf-8', xml_declaration=True))