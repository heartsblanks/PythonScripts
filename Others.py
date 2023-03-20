import re
from lxml import etree

# Open the XML file and read it into a string
with open('original_file.xml', 'rb') as file:
    xml_string = file.read().decode('utf-8', 'ignore')

# Remove invalid characters from the XML string using a regular expression
regex = re.compile('[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD]')
xml_string = regex.sub('', xml_string)

# Parse the formatted XML string using lxml
try:
    root = etree.fromstring(xml_string)
except etree.XMLSyntaxError as e:
    print(f'Error parsing XML: {e}')
    exit()

# Format the parsed tree to a string
pretty_xml = etree.tostring(root, encoding='unicode', pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype='<!DOCTYPE doc>', standalone=True)

# Write the formatted XML string to a new file
try:
    with open('formatted_file.xml', 'w') as file:
        file.write(pretty_xml)
except OSError as e:
    print(f'Error writing formatted XML file: {e}')
    exit()
