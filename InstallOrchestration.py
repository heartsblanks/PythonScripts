import xml.etree.ElementTree as ET
from collections import OrderedDict

def dict_to_xml(data):
    # Extract the root tag and its associated dictionary of attributes/children
    root_tag, root_data = list(data.items())[0]
    
    # Create the root element
    element = ET.Element(root_tag)
    
    # Loop through the OrderedDict to ensure the sequence is preserved
    for key, value in root_data.items():
        if isinstance(value, OrderedDict):
            # If value is an OrderedDict, treat it as a child element
            child = dict_to_xml({key: value})
            element.append(child)
        else:
            # Otherwise, treat it as an attribute
            element.set(key, str(value))
    
    return element

def prettify_xml(element):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(element, 'utf-8')
    return rough_string.decode('utf-8')

# Sample OrderedDict with root tag
data = OrderedDict([
    ('RootElement', OrderedDict([
        ('attribute1', 'value1'),
        ('attribute2', 'value2'),
        ('ChildElement', OrderedDict([
            ('child_attr1', 'child_value1'),
            ('child_attr2', 'child_value2')
        ]))
    ]))
])

# Convert OrderedDict to XML and preserve the order
xml_element = dict_to_xml(data)

# Output the resulting XML
xml_string = prettify_xml(xml_element)
print(xml_string)