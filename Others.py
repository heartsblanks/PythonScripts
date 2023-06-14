import re

# Specify the input file name
input_file = 'input_file.txt'

# Open the input file for reading
with open(input_file, 'r') as file:
    content = file.readlines()

# Initialize variables
label_value = ''
message_flow_content = ''
output_file = ''

# Process the lines
for line in content:
    if line.startswith('MessageFlow'):
        # Check for the line starting with 'MessageFlow'
        if message_flow_content:
            # If previous content exists, write it to the output file
            if output_file and message_flow_content.strip():
                with open(output_file, 'w') as file:
                    file.write(message_flow_content.strip())
                    print(f"Created file: {output_file}")
            message_flow_content = ''  # Reset the content
        label_match = re.search(r'label\s*=\s*\'([^\']+)\'', line)
        if label_match:
            # Extract the label value
            label_value = label_match.group(1)
            output_file = label_value.split('.')[-1] + '.txt'
    message_flow_content += line
    if label_value and line.startswith('MessageFlow') and line.strip() != 'MessageFlow':
        # Check for the next line starting with 'MessageFlow' (excluding 'MessageFlow' line itself)
        if output_file and message_flow_content.strip():
            with open(output_file, 'w') as file:
                file.write(message_flow_content.strip())
                print(f"Created file: {output_file}")
        message_flow_content = line  # Start new content from the next 'MessageFlow' line

# Write the final message flow content to the output file
if output_file and message_flow_content.strip():
    with open(output_file, 'w') as file:
        file.write(message_flow_content.strip())
        print(f"Created file: {output_file}")