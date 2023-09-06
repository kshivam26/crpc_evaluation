def move_records(record_list):
    return record_list[3:6] + record_list[:3] + record_list[6:]

import os

# Function to move records 4 to 6 as the first three records in a list
# Replace 'folder_path' with the path to your folder containing the files
folder_path = os.getcwd()

# List all files in the folder
files = os.listdir(folder_path)

for filename in files:
    file_path = os.path.join(folder_path, filename)

    # Read the content from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Perform the operation (move records 4 to 6 as the first three records)
    updated_lines = move_records(lines)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
