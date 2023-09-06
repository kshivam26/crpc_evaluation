from collections import OrderedDict

def process_data(input_filename):
    
    """
    Process the data in the input file, remove duplicate rows based on median and >95% columns,
    and write the unique rows to a new output file.

    Args:
        input_filename (str): The name of the input file to process.
    """
    

    # Read the data from the text file while preserving the order
    data = []
    with open(input_filename, 'r') as file:
        for line in file:
            data.append(line.strip().split())

    # Remove duplicates based on median and >95% columns while maintaining the order
    unique_data = OrderedDict()
    for row in data[1:]:
        filename = row[0]
        median = float(row[3])
        over_95 = float(row[1].rstrip('%'))
        key = (median, over_95)
        if filename not in unique_data or key > unique_data[filename][0]:
            unique_data[filename] = (key, row)

    # Write the unique data to a new file while preserving the order
    output_filename = f"filtered_{input_filename}"
    with open(output_filename, 'w') as file:
        max_lengths = [max(len(row[i]) for row in [data[0]] + [r for _, r in unique_data.values()]) for i in range(len(data[0]))]
        for row in [data[0]] + [row for _, row in unique_data.values()]:
            # formatted_row = '  '.join(cell.ljust(max_length) for cell, max_length in zip(row, max_lengths))
            # file.write(formatted_row + '\n')
            file.write('  '.join(row) + '\n')

    print(f"New file '{output_filename}' has been created.")

# List of input file names
input_files = ['stats_1c1s3r1p_cRPC.txt', 'stats_1c1s3r1p_no_cRPC.txt', 'stats_3c1s3r1p_cRPC.txt', 'stats_3c1s3r1p_no_cRPC.txt', 'stats_9c1s3r1p_cRPC.txt', 'stats_9c1s3r1p_no_cRPC.txt']

# Process each input file
for input_file in input_files:
    process_data(input_file)
