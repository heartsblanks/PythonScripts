import xml.etree.ElementTree as ET

def read_project_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def get_values_by_tags(root, tags):
    values = []
    for tag in tags:
        elements = root.findall(tag)
        for element in elements:
            values.append(element.text)
    return values

def append_missing_values(original_values, target_values, target_parent, tag_name):
    for value in original_values:
        if value not in target_values:
            new_element = ET.SubElement(target_parent, tag_name)
            new_element.text = value

def find_parent_element(root, tags):
    current_element = root
    for tag in tags:
        child_element = None
        for child in current_element:
            if child.tag == tag:
                child_element = child
                break
        if child_element is None:
            child_element = ET.SubElement(current_element, tag)
        current_element = child_element
    return current_element

def is_nested_tag(tag_elements, index):
    if index >= len(tag_elements):
        return False

    current_tag = tag_elements[index]
    for i in range(index + 1, len(tag_elements)):
        if current_tag in tag_elements[i]:
            return True
    return False

def write_project_file(file_path, root):
    tree = ET.ElementTree(root)
    root.set('xmlns', 'http://schemas.eclipse.org/2004/09/standard-fe')
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)

def update_project_file(source_file, destination_file, tags):
    source_root = read_project_file(source_file)
    destination_root = read_project_file(destination_file)

    for tag in tags:
        tag_elements = tag.split('/')
        source_values = get_values_by_tags(source_root, [tag])
        destination_values = get_values_by_tags(destination_root, [tag])

        if is_nested_tag(tag_elements, 0):
            target_parent = find_parent_element(destination_root, tag_elements)
        else:
            target_parent = destination_root

        tag_name = tag_elements[-1]
        append_missing_values(source_values, destination_values, target_parent, tag_name)

    write_project_file(destination_file, destination_root)

# Example usage:
source_project_file = 'path_to_source_project_file.xml'
destination_project_file = 'path_to_destination_project_file.xml'
tags_to_update = ['buildSpec/buildCommand/name', 'natures/nature']

update_project_file(source_project_file, destination_project_file, tags_to_update)