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

if len(sys.argv) > 2:
    input_filename = sys.argv[1]
    stats_file_name = sys.argv[2]
    throughput_value = sys.argv[3]
    tid_values = sys.argv[4:]
    
    # Generate the output filename by appending "output" to the input filename
    output_filename = os.path.splitext(input_filename)[0] + "_output.txt"

    # Read the data from the input file
    with open(input_filename, "r") as file:
        data = file.read()

    # cpu_values = []  # List to store the %CPU values

    # Split the data into individual bursts based on empty lines
    bursts = data.strip().split('\n\n')

    print("tid values are: ", tid_values)
    with open('v8_stats_'+stats_file_name+'_cRPC.txt', 'a') as file:
        for i, tid_value in enumerate(tid_values):
            cpu_values = []
            for burst in bursts:
                # Split each burst into lines and iterate over them
                lines = burst.strip().split('\n')

                # print("checkpoint 1")
                for line in lines:
                    # Split each line into columns
                    columns = line.split()
                    if len(columns) < 5: continue
                    # print("checkpoint 2")
                    # Check if the line contains the TID value
                    # print("column 4 is: ", columns[4])
                    if columns[4] == tid_value:
                        # print("checkpoint 3")
                        cpu_percentage = float(columns[9])
                        cpu_values.append(cpu_percentage)


            # median = statistics.median(cpu_values)
            maximum = max(cpu_values)
            # mean = statistics.mean(cpu_values)



            # Write the %CPU values to the output file
            # with open(output_filename, "w") as output_file:
            #     for cpu_value in cpu_values:
            #         output_file.write(str(cpu_value) + "\n")

            # Count the values over 95
            count_over_95 = len([x for x in cpu_values if x >= 95])
            count_over_90 = len([x for x in cpu_values if x >= 90])
            # Calculate the percentage
            percentage_over_95 = (count_over_95 / len(cpu_values)) * 100
            # Open the output file in append mode
            # v7 is chaining in the callback, like A->B->C->B->A
            # v7+changed pidstat time 1s->2s
            # with open('v8_stats_'+stats_file_name+'_no_cRPC.txt', 'a') as file: # v3 is when I used the map instead #v4 has no of data points >95 and >90 #v5 checks candidates for saturation points #v6 includes a separate crpc_appendEntries
            # Write the median, maximum, and mean to the file
            if i == 0:
                file.write("{}  {} {} {} {} ".format(
                    os.path.splitext(input_filename)[0],
                    str(maximum),
                    count_over_95,
                    count_over_90,
                    throughput_value
                ))
            else:
                file.write("{} {} {} ".format(
                    str(maximum),
                    count_over_95,
                    count_over_90
                ))
        file.write("\n")      
else:
    print("Usage: python proc_cpu_utilization.py <input_filename> <tid_value>")
