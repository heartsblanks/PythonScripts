import re

# Specify the input file name
input_file = 'input_file.txt'

# Open the input file for reading
with open(input_file, 'r') as file:
    content = file.readlines()

# Initialize variables
output_files = {}
label_value = None  # Initialize label_value
writing_content = False
message_flow_content = ''

# Process the lines
for line in content:
    if line.startswith('MessageFlow'):
        # Check for the line starting with 'MessageFlow'
        if writing_content:
            # If previous content exists, store it in the appropriate output file
            if label_value in output_files and message_flow_content.strip():
                output_files[label_value].write(message_flow_content.strip() + '\n')
            message_flow_content = ''  # Reset the content

        # Extract the label value
        label_match = re.search(r"label='([^']+)'", line)
        if label_match:
            label_value = label_match.group(1)
            if label_value not in output_files:
                # Create a new output file for the label value
                output_file = label_value.split('.')[-1] + '.txt'
                output_files[label_value] = open(output_file, 'w')
            writing_content = True  # Start writing content

    message_flow_content += line

# Write the final message flow content to the output file
if label_value in output_files and message_flow_content.strip():
    output_files[label_value].write(message_flow_content.strip() + '\n')

# Close all output files
for file in output_files.values():
    file.close()

print("Output files created successfully.")