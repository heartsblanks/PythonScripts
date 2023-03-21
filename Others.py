from lxml import etree

# Set the tag name to search for
tag_name = 'page'

# Open the XML file and create an iterator for efficient processing
with open('large_file.xml', 'rb') as file:
    context = etree.iterparse(file, events=('start',), tag=tag_name)

    # Loop through each matching element and print its line
    for event, elem in context:
        print(etree.tostring(elem, encoding='unicode'))

        # Clear the element from memory to free up space
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
