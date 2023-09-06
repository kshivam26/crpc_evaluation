import matplotlib.pyplot as plt
import numpy as np
"""
This script compares the median and >95% values from two sets of data files.
Each set of data files should contain the same number of files, and the comparison is performed between corresponding files
from both sets.

To use this script:
1. Update the 'input_files1' and 'input_files2' lists with the file names of the first and second set of data files,
   respectively.
2. Ensure that the two lists have the same length.
3. Run the script.

The script generates a line plot to compare the median and >95% values for each pair of files. The x-axis represents the
file names, and the y-axis represents the values. The median values are shown with blue lines, the >95% values are shown
with orange lines, and the throughput values are shown with green lines.

The generated plot provides a visual comparison of the corresponding median, >95%, and throughput values between the two
sets of data files.
"""

# List of input file names for the first set of data
input_files2 = ['filtered_stats_1c1s3r1p_cRPC.txt', 'filtered_stats_3c1s3r1p_cRPC.txt', 'filtered_stats_9c1s3r1p_cRPC.txt']  # Replace with your input file names

# List of input file names for the second set of data
input_files1 = ['filtered_stats_1c1s3r1p_no_cRPC.txt', 'filtered_stats_3c1s3r1p_no_cRPC.txt', 'filtered_stats_9c1s3r1p_no_cRPC.txt']  # Replace with your input file names

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
        filenames1.append(values[0].split('_')[0])
        medians1.append(float(values[3]))
        over_951.append(float(values[1].strip('%')))
        throughputs1.append(float(values[5]))

    for line in lines2[1:]:
        values = line.strip().split()
        filenames2.append(values[0].split('_')[0])
        medians2.append(float(values[3]))
        over_952.append(float(values[1].strip('%')))
        throughputs2.append(float(values[5]))

    # Plotting
    fig, ax1 = plt.subplots(figsize=(24, 12))

    index = np.arange(len(filenames1))

    ax1.plot(index, medians1, label='Median Utilization - No_CPRC', color='b', marker='o')
    ax1.plot(index, medians2, label='Median Utilization - CPRC', color='r', marker='s')
    ax1.set_xlabel('Number of concurrent requests per client')
    ax1.set_ylabel('Median CPU Utilization')
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()

    ax2.plot(index, over_951, label='>95% Utilization - No_CPRC', color='g', marker='o')
    ax2.plot(index, over_952, label='>95% Utilization - CPRC', color='m', marker='s')
    ax2.set_ylabel('>95% CPU Utilization')
    ax2.tick_params(axis='y')

    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 80))
    ax3.plot(index, throughputs1, label='Throughput (req/s) - No_CPRC', marker='^', color='c')
    ax3.plot(index, throughputs2, label='Throughput (req/s) - CPRC', marker='^', color='y')
    ax3.set_ylabel('Throughput (req/s)')
    ax3.tick_params(axis='y')

    # # Rotate x-axis tick labels by 45 degrees
    # plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    plt.xticks(index, filenames1, rotation=45, ha='right')

    # Adjust x-axis and legend positions
    plt.subplots_adjust(bottom=0.2)

    # Combine the legends from all three axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()
    ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, loc='upper center',
               bbox_to_anchor=(0.5, -0.15), ncol=3)

    plt.title('CPU Utilization Comparison - {}'.format(input_files1[i].split('_')[2]))
    
    # Save the plot as a PNG file
    plt.savefig('v2_comparison_plot{}.png'.format(i + 1), bbox_inches='tight')
    plt.close()

    # plt.xticks(index, filenames1, rotation=45, ha='right')

    # # Adjust figure size and spacing
    # fig.tight_layout()

    # # Combine legend for all three axes
    # handles, labels = [], []
    # for ax in [ax1, ax2, ax3]:
    #     h, l = ax.get_legend_handles_labels()
    #     handles.extend(h)
    #     labels.extend(l)

    # # Add the legend
    # fig.legend(handles, labels, loc='upper left')

    # # Save the figure
    # fig.savefig(f'comparison_plot{i}.png', dpi=300)
    # plt.close(fig)