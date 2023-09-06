# import statistics
# import glob

# # Get a list of files starting with "v7"
# file_list = glob.glob("v7*.txt")

# # Iterate over each file
# for file_name in file_list:
#     # Read the data from the file
#     with open(file_name, "r") as file:
#         data = file.readlines()

#     # Dictionary to store the median value for each unique first column value
#     median_values = {}

#     for record in data:
#         parts = record.split()
#         first_col = parts[0]
#         last_col = float(parts[-1])

#         if first_col not in median_values:
#             median_values[first_col] = [last_col]
#         else:
#             median_values[first_col].append(last_col)

#     # Filter the rows with the median value for the last column for each unique first column
#     filtered_data = []
#     for key, values in median_values.items():
#         median_value = statistics.median(values)
#         filtered_data.extend([record for record in data if record.startswith(key) and float(record.split()[-1]) == median_value])

#     # Write the filtered data to the output file
#     output_file_name = f"filtered_data_{file_name.split('.')[0]}.txt"
#     with open(output_file_name, "w") as file:
#         file.writelines(filtered_data)

#     print(f"Filtered data has been written to {output_file_name}")

import statistics
import glob

# Get a list of files starting with "v7"
# file_list = glob.glob("v9*.txt")
file_list = glob.glob("v9*no_cRPC.txt") # filter only no_crpc files

# Iterate over each file
for file_name in file_list:
    # Read the data from the file
    with open(file_name, "r") as file:
        data = file.readlines()

    # Dictionary to store the median value for each unique first column value
    median_values = {}

    for record in data:
        parts = record.split()
        first_col = parts[0]
        last_col = int(float(parts[4]))  # Strip off decimal value

        if first_col not in median_values:
            median_values[first_col] = [last_col]
        else:
            median_values[first_col].append(last_col)

    # Filter the rows with the median value for the last column for each unique first column
    filtered_data = []
    for key, values in median_values.items():
        median_value = statistics.median(values)
        filtered_data.extend([record for record in data if record.startswith(key) and int(float(record.split()[4])) == median_value])

    # Write the filtered data to the output file
    output_file_name = f"filtered_data/filtered_data_{file_name.split('.')[0]}.txt"
    with open(output_file_name, "w") as file:
        file.writelines(filtered_data)

    print(f"Filtered data has been written to {output_file_name}")
