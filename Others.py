import xml.etree.ElementTree as ET

def get_max_node_id(root):
    max_id = 0
    for node in root.findall('.//nodes'):
        node_id = int(node.get('{http://www.omg.org/XMI}id').split('_')[-1])
        max_id = max(max_id, node_id)
    return max_id

def create_new_node(new_node_tag, new_node_details, nsmap):
    new_node = ET.Element(new_node_tag, nsmap=nsmap)
    for key, value in new_node_details.items():
        new_node.set(key, value)
    translation_element = ET.Element('translation', nsmap=nsmap)
    translation_element.set('string', new_node_details['translation'])
    new_node.append(translation_element)
    return new_node

def replace_node_entry(root, old_node_tag, new_node_tag, new_node_details):
    max_id = get_max_node_id(root)
    new_node_details['xmi:id'] = f'FCMComposite_1_{max_id + 1}'

    nsmap = root.nsmap  # Retrieve the original namespaces from the original ElementTree
    ET.register_namespace('', nsmap[None])  # Register the default namespace

    updated_root = ET.Element(root.tag, nsmap=nsmap)
    for key, value in root.attrib.items():
        updated_root.set(key, value)

    for node in root.findall('.//nodes'):
        if node.get('xmi:type') == old_node_tag:
            new_node = create_new_node(new_node_tag, new_node_details, nsmap)
            updated_root.append(new_node)
        else:
            updated_root.append(node)

    return ET.ElementTree(updated_root)  # Return the updated ElementTree

# Sample replaced node entry details with label name
new_node_details = {
    'xmi:id': '',  # Replace with the new node ID after finding the maximum existing node ID and incrementing by 1
    'xmi:type': 'MQINPUT_SF.subflow:FCMComposite_1',
    'location': '400,300',
    'translation': 'MQ Input SF',  # Update the translation value directly without xmi:type and single quotes
    'labelName': 'postSum',  # Include the labelName attribute in the new node details
    # Add other details for the new node entry here
}

# Get the file path from the user
file_path = input("Enter the path of the file containing data: ")

# Parse the XML data from the file to create the ElementTree
try:
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Run the replace_node_entry function with the updated new_node_details
    updated_tree = replace_node_entry(root, 'Sum_APIInputCatchHandler.subflow:FCMComposite_1', 'MQINPUT_SF.subflow:FCMComposite_1', new_node_details)

    # Write the updated XML content to the file
    with open('updated_msgflow.xml', 'wb') as file:
        updated_tree.write(file, encoding='utf-8', xml_declaration=True)

    print("XML data successfully updated and saved to 'updated_msgflow.xml'.")
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
except ET.ParseError:
    print("Invalid XML data in the file. Please check the XML content and try again.")