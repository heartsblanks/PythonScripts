from lxml import etree

# Read the XML file into memory and remove newlines
try:
    with open('original_file.xml', 'r') as file:
        xml_string = file.read().replace('\n', '')
except OSError as e:
    print(f'Error reading XML file: {e}')
    exit()

# Parse the cleaned XML string using lxml
try:
    root = etree.fromstring(xml_string)
except etree.XMLSyntaxError as e:
    print(f'Error parsing XML file: {e}')
    exit()

# Pretty-print the parsed tree to a string with customized formatting options
pretty_xml = etree.tostring(root, encoding='unicode', pretty_print=True, xml_declaration=True, doctype='<!DOCTYPE doc>', standalone=True)

# Write the formatted XML string to a new file
try:
    with open('formatted_file.xml', 'w') as file:
        file.write(pretty_xml)
except OSError as e:
    print(f'Error writing formatted XML file: {e}')
    exit()
