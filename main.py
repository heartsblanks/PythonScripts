from lxml import etree

# Load the MXSD file
mxsd_doc = etree.parse('example.mxsd')

# Set the namespace mapping for MXSD
mxsd_ns = {'mx': 'http://schemas.microsoft.com/2003/10/Serialization/'}

# Convert the MXSD to XSD
for element in mxsd_doc.xpath('//mx:*', namespaces=mxsd_ns):
    element.tag = etree.QName(element.tag).localname

# Remove the MXSD namespace declaration
xsd_doc = etree.ElementTree(mxsd_doc.getroot())
xsd_doc.getroot().nsmap.clear()
xsd_doc.write('example.xsd', pretty_print=True)
