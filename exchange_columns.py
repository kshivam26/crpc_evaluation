# import os

# def move_fifth_column_to_end(data):
#     columns = data.strip().split()
#     if len(columns) >= 5:
#         fifth_column = columns.pop(4)
#         columns.append(fifth_column)
#     return ' '.join(columns)

# # Get the list of files starting with "filtered_data"
# input_files = [filename for filename in os.listdir(".") if filename.startswith("filtered_data_v9")]

# for input_file in input_files:
#     with open(input_file, 'r') as file:
#         # Read the contents of the input file
#         data = file.read()

#     # Modify the data
#     modified_data = move_fifth_column_to_end(data)

#     # Create the output file name
#     output_file = "v9_results/column_exchange_" + input_file

#     # Write the modified data to the output file
#     with open(output_file, 'w') as file:
#         file.write(modified_data)

#     print(f"Processed '{input_file}' and saved the modified data to '{output_file}'.")


import os

def move_fifth_column_to_end(data):
    lines = data.strip().split('\n')
    modified_lines = []

    for line in lines:
        columns = line.strip().split()
        if len(columns) >= 5:
            fifth_column = columns.pop(4)
            columns.append(fifth_column)
        modified_lines.append(' '.join(columns))
    
    return '\n'.join(modified_lines)

# Get the list of files starting with "filtered_data"
input_files = [filename for filename in os.listdir("filtered_data") if filename.startswith("filtered_data_v9")]
print(input_files)
for input_file in input_files:
    with open(os.path.join("filtered_data", input_file), 'r') as file:
        # Read the contents of the input file
        data = file.read()

    # Modify the data
    modified_data = move_fifth_column_to_end(data)

    # Create the output file name
    output_file = "v9_results/column_exchange_" + input_file

    # Write the modified data to the output file
    with open(output_file, 'w') as file:
        file.write(modified_data)

    print(f"Processed '{input_file}' and saved the modified data to '{output_file}'.")
