from lxml import etree

# Specify the tag name to extract
tag_name = 'page'

# Read the XML file into memory and parse it using lxml
try:
    with open('original_file.xml', 'r') as file:
        xml_string = file.read()
    root = etree.fromstring(xml_string)
except OSError as e:
    print(f'Error reading/parsing XML file: {e}')
    exit()
except etree.XMLSyntaxError as e:
    print(f'Error parsing XML file: {e}')
    exit()

# Extract all elements with the specified tag name from the XML tree
elements = root.xpath(f'//{tag_name}')

# Create a new XML tree with only the extracted elements
new_root = etree.Element('root')
for element in elements:
    new_root.append(element)

# Convert the new XML tree to a string with customized formatting options
pretty_xml = etree.tostring(new_root, encoding='unicode', pretty_print=True, xml_declaration=True, doctype='<!DOCTYPE doc>', standalone=True)

# Write the formatted XML string to a new file
try:
    with open('extracted_file.xml', 'w') as file:
        file.write(pretty_xml)
except OSError as e:
    print(f'Error writing extracted XML file: {e}')
    exit()
