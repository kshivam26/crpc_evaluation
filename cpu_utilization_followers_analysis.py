"""
Script Name: proc_cpu_utilization.py

Description:
This script extracts the %CPU values for a specified TID (Thread ID) from a given input file.
The extracted values are stored in an output file.

Usage:
python proc_cpu_utilization.py <input_filename> <tid_value>

Arguments:
- input_filename: The name or path of the input file containing the data
- tid_value: The Thread ID (TID) for which to extract the %CPU values

Output:
The script generates an output file named <input_filename>output.txt in the same directory
as the input file. This file contains the extracted %CPU values.

Example:
python proc_cpu_utilization.py data.txt 2914653

In the above example, the script reads the data from the file "data.txt" and extracts
the %CPU values for the TID 2914653. The extracted values are stored in the file "data_output.txt".
"""


import sys
import os
import statistics
import re

if len(sys.argv) > 2:
    input_filename = sys.argv[1]
    stats_file_name = sys.argv[2]
    throughput_value = sys.argv[3]
    tid_values = sys.argv[4:]
    # input_filename = top_log_test.txt
    # Generate the output filename by appending "output" to the input filename
    output_filename = os.path.splitext(input_filename)[0] + "_output.txt"

    # Read the data from the input file
    with open("top_log_stats5.txt", "r") as file:
        data = file.read()

    # cpu_values = []  # List to store the %CPU values

    # Split the data into individual bursts based on empty lines
    # bursts = data.strip().split('\n\n')
    # v9 contains the top cpu utilization metrics
    print("tid values are: ", tid_values)
    for i, tid_value in enumerate(tid_values):
        cpu_values = []
        lines = re.findall(rf"\b{tid_value}\b.*\n", data)
        
        if len(lines) == 0:
            print("no lines detected")
            continue
        
        for line in lines:
            columns = line.split()
            cpu = float(columns[8])  # Assuming the %CPU column is at index 8
            # print("the value of cpu is: ", cpu)
            cpu_values.append(cpu)

        maximum = max(cpu_values)
        # mean = statistics.mean(cpu_values)
        # Write the %CPU values to the output file
        # with open(output_filename, "w") as output_file:
        #     for cpu_value in cpu_values:
        #         output_file.write(str(cpu_value) + "\n")
        # Count the values over 95
        count_over_95 = len([x for x in cpu_values if x >= 95])
        count_over_90 = len([x for x in cpu_values if x >= 90])
        count_over_80 = len([x for x in cpu_values if x >= 80])
        count_over_70 = len([x for x in cpu_values if x >= 70])
        count_over_60 = len([x for x in cpu_values if x >= 60])
        count_over_50 = len([x for x in cpu_values if x >= 50])
        
        print("maximum: ", maximum)
        print("count_over_95: ", count_over_95)
        print("count_over_90: ", count_over_90)
        print("count_over_80: ", count_over_80)
        print("count_over_70: ", count_over_70)
        print("count_over_60: ", count_over_60)
        print("count_over_50: ", count_over_50)

        # Calculate the percentage
        percentage_over_95 = (count_over_95 / len(cpu_values)) * 100