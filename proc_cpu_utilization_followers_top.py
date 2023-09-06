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
    version = sys.argv[4]
    tid_values = sys.argv[5:]
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
    current_directory = os.getcwd()


    # Create a folder named "v9"
    # v10 prints, number_of_concurrent (max >95 >90 >80 >70 >60 >50)^#replicas throughput
    # v11 is for testing purposes; tc added , 50ms (3 entries), 100ms (next 3 entries), 200ms (next 3 entries)
    # v12 brings back the crpc ring option; results for all three versions; number of servers initially vary from 9, 11, 13
    # v13 is with ulimit set to 17408; earlier a lot of clients did not spawn and T/P numbers were all over the place
    v13_folder = os.path.join(current_directory, "v13_stats")
    if not os.path.exists(v13_folder):
        os.makedirs(v13_folder)
    
    stats_file_name = 'v13_stats/v13_stats_'+stats_file_name+ f"{'_no_cRPC' if version=='0' else '_cRPC_no_ring' if version=='1' else '_cRPC_ring'}"
    print("the stats file name is: ", stats_file_name)
    
    with open(stats_file_name, 'a') as file:
        file.write("{} ".format(
                    os.path.splitext(input_filename)[0].rsplit("_", 1)[0]
                ))
            
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
            count_over_80 = len([x for x in cpu_values if x >= 80])
            count_over_70 = len([x for x in cpu_values if x >= 70])
            count_over_60 = len([x for x in cpu_values if x >= 60])
            count_over_50 = len([x for x in cpu_values if x >= 50])
            # Calculate the percentage
            # Open the output file in append mode
            # v7 is chaining in the callback, like A->B->C->B->A
            # v7+changed pidstat time 1s->2s
            # with open('v8_stats_'+stats_file_name+'_no_cRPC.txt', 'a') as file: # v3 is when I used the map instead #v4 has no of data points >95 and >90 #v5 checks candidates for saturation points #v6 includes a separate crpc_appendEntries


            file.write("{} {} {} {} {} {} {} ".format(
                str(maximum),
                count_over_95,
                count_over_90,
                count_over_80,
                count_over_70,
                count_over_60,
                count_over_50
            ))
        
        file.write("{}".format(throughput_value))
        file.write("\n")      
else:
    print("Usage: python proc_cpu_utilization.py <input_filename> <tid_value>")
