import matplotlib.pyplot as plt

# List of input file names for the first set of data
input_files1 = ['filtered_stats_1c1s3r1p_cRPC.txt', 'filtered_stats_3c1s3r1p_cRPC.txt', 'filtered_stats_9c1s3r1p_cRPC.txt']  # Replace with your input file names

# List of input file names for the second set of data
input_files2 = ['filtered_stats_1c1s3r1p_no_cRPC.txt', 'filtered_stats_3c1s3r1p_no_cRPC.txt', 'filtered_stats_9c1s3r1p_no_cRPC.txt']  # Replace with your input file names

# Verify that the two lists have the same length
if len(input_files1) != len(input_files2):
    raise ValueError("The number of input files in both sets should be the same.")

for i in range(len(input_files1)):
    # Read data from the first input file
    with open(input_files1[i], 'r') as file:
        lines1 = file.readlines()

    # Read data from the second input file
    with open(input_files2[i], 'r') as file:
        lines2 = file.readlines()

    # Extract data from each file
    filenames1 = []
    medians1 = []
    over_951 = []
    throughputs1 = []

    filenames2 = []
    medians2 = []
    over_952 = []
    throughputs2 = []    

    for line in lines1[1:]:
        values = line.strip().split()
        filenames1.append(values[0])
        medians1.append(float(values[3]))
        # throughputs1.append(float(values[5]))
        over_951.append(float(values[1].strip('%')))

    for line in lines2[1:]:
        values = line.strip().split()
        filenames2.append(values[0])
        medians2.append(float(values[3]))
        # throughputs2.append(float(values[5]))
        over_952.append(float(values[1].strip('%')))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(filenames2, medians2, label='Median - No_CPRC')
    plt.plot(filenames1, medians1, label='Median - CPRC')
    
    # plt.plot(filenames1, throughputs1, label='Throughput - CPRC')
    # plt.plot(filenames2, throughputs2, label='Throughput - No_CPRC')
    plt.plot(filenames2, over_952, label='>95% - No_CPRC')
    plt.plot(filenames1, over_951, label='>95% - CRPC')
    
    plt.xlabel('Number of concurrent requests per client')
    plt.ylabel('CPU Utilization')
    plt.title('CPU Utilization Comparison - {}'.format(input_files1[i].split('_')[2]))
    plt.xticks(rotation=45, ha='right', fontsize=8)  # Adjust the rotation and fontsize as needed
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin as needed
    plt.legend()

    # Save the plot to a figure file
    output_file = 'plot_comparison_{}.png'.format(input_files1[i].split('_')[2])
    plt.savefig(output_file)
    plt.close()
