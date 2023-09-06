import matplotlib.pyplot as plt

# List of input file names
input_files = ['filtered_stats_1c1s3r1p_cRPC.txt', 'filtered_stats_1c1s3r1p_no_cRPC.txt', 'filtered_stats_3c1s3r1p_cRPC.txt', 'filtered_stats_3c1s3r1p_no_cRPC.txt', 'filtered_stats_9c1s3r1p_cRPC.txt', 'filtered_stats_9c1s3r1p_no_cRPC.txt']

for input_file in input_files:
    # Read data from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extract data from each line
    filenames = []
    medians = []
    over_95 = []
    throughputs = []

    for line in lines[1:]:
        values = line.strip().split()
        filenames.append(values[0])
        throughputs.append(float(values[5]))
        medians.append(float(values[3]))
        over_95.append(float(values[1].strip('%')))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(filenames, throughputs, label='Throughput')
    plt.plot(filenames, medians, label='Median')
    plt.plot(filenames, over_95, label='>95%')
    plt.xlabel('Filename')
    plt.ylabel('Value')
    plt.title('CPU utilization comparison - {}'.format(input_file))
    plt.xticks(rotation=45, ha='right', fontsize=8)  # Adjust the rotation and fontsize as needed
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin as needed
    plt.legend()

    # Save the plot to a figure file
    output_file = 'plot_{}.png'.format(input_file.split('.')[0])
    plt.savefig(output_file)
    plt.close()
