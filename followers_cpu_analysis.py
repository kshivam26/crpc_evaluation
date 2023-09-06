import subprocess
import signal

# pidstat_filename = "10_con.txt"
# depfast_output_filename = "output_con10.txt"

# array_con = [10, 15, 20, 30, 35, 40, 45, 50, 60, 75, 100, 200, 400, 500, 600, 700, 1000, 2000, 4000, 5000, 10000]
# array_con = [10, 15]

array_con = [10, 20, 30, 40, 50, 75, 100]
# array_con = [800, 400, 200, 100, 75, 60, 50, 40, 35, 30, 20, 15, 10]
# array_con = [10, 20, 30, 40]
# array_con = [13000, 16000, 19000, 22000, 25000, 28000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
# array_con = [70000, 80000, 90000, 100000]
# array_con = [100, 75, 50, 40, 30, 20, 10]
# array_con = [400, 200, 100, 75, 50, 40, 30, 20, 10]
array_con = [3200, 1600, 800, 400, 200, 100, 75, 50, 40, 30, 20, 10]
array_con = [3200]
repeated_array_con = [element for element in array_con for _ in range(1)]
# file_list = ["3c1s3r1p", "5c1s3r1p", "10c1s3r1p", "20c1s3r1p", "30c1s3r1p", "40c1s3r1p", "50c1s3r1p", "60c1s3r1p"]
# file_list = ["3c1s3r1p", "5c1s3r1p", "10c1s3r1p", "20c1s3r1p", "30c1s3r1p", "40c1s3r1p", "50c1s3r1p", "60c1s3r1p"]
# file_list = ["60c1s3r1p", "50c1s3r1p", "40c1s3r1p", "30c1s3r1p", "20c1s3r1p", "10c1s3r1p", "5c1s3r1p", "3c1s3r1p"]
# file_list = ["10c1s5r1p", "10c1s7r1p", "10c1s3r1p", "1c1s5r1p", "1c1s3r1p"]
# file_list = ["1c1s5r1p", "1c1s3r1p"]
# file_list = ["40c1s7r1p"]
# file_list = ["60c1s7r1p"]
# file_list = ["10c1s3r1p", "5c1s3r1p", "3c1s3r1p"]
# file_list = ["10c1s5r1p", "10c1s3r1p", "8c1s5r1p", "8c1s3r1p", "5c1s5r1p", "5c1s3r1p", "3c1s5r1p", "3c1s3r1p","1c1s5r1p", "1c1s3r1p"]
# file_list = ["10c1s7r1p"]
file_list = ["5c1s5r1p"]


## testing higher number of con
# file_list = ["20c1s3r1p", "10c1s3r1p", "5c1s3r1p"]

new_array = [(elem1, elem2) for elem1 in file_list for elem2 in repeated_array_con]

for (f, el) in new_array:
    print("current file and con: ", f, el)
    pidstat_filename = str(el) + "_con.txt"
    depfast_output_filename = str(el) + "_con_output.txt"
    
    print("starting iteration for input: ", el)
    # Run the first command: pidstat
    # first_command = ["pidstat", "2", "-u", "-G", "deptran", "-t"]
    first_command = ["./top_script.sh"]
    # with open(pidstat_filename, "w") as first_output_file:
    #     first_process = subprocess.Popen(first_command)

    # first_process = subprocess.Popen("python", "top_script_python.py")

    first_process = subprocess.Popen(first_command)

    # Run the second command: build/deptran_server
    second_command = [
        "depfast-ae/build/deptran_server",
        "-f",
        "depfast-ae/config/none_fpga_raft.yml",
        "-f",
        "depfast-ae/config/"+f+".yml",
        "-f",
        "depfast-ae/config/rw.yml",
        "-f",
        "depfast-ae/config/concurrent_"+ str(el)+".yml",
        "-P",
        "localhost",
        "-d",
        "100",
    ]
    with open(depfast_output_filename, "w") as second_output_file:
        second_process = subprocess.Popen(second_command, stdout=second_output_file, stderr=subprocess.PIPE)

    # Wait for the second command to finish
    second_process.wait()

    print("waiting for second_process to finish", flush=True)

    # Send a kill signal to the first process
    first_process.terminate()

    import re

    # Open the file
    # filename = "output_con10.txt"  # Replace with your file name
    with open(depfast_output_filename, "r") as file:
        content = file.read()

    tid_values = []
    # Extract the value corresponding to "tid is" using regular expression
    tid_pattern = r"tid of leader is (\d+)"
    tid_match = re.search(tid_pattern, content)
    tid_values.append(tid_match.group(1) if tid_match else None)

    # Extract the value of tids corresponding to non-leaders
    tid_pattern = r"tid of non-leader is (\d+)"
    tid_matches = re.findall(tid_pattern, content)
    for match in tid_matches:
        tid_values.append(match)
        
    print("current tid_values are: ", tid_values)

    # Extract the value corresponding to "throughput" using regular expression
    throughput_pattern = r"Throughput: (\d+\.\d+)"
    throughput_matches = re.findall(throughput_pattern, content)
    throughput_value = 0
    # Print the found throughput values
    for val in throughput_matches:
        throughput_value += float(val)

    # Display the extracted values
    # print("Value corresponding to 'tid is':", tid_value)
    print("Value corresponding to 'throughput':", throughput_value)



    # Run the third command: python proc_cpu_utilization.py 10000_con.txt 2963637
    third_command = [
        "python",
        "cpu_utilization_followers_analysis.py",
        pidstat_filename,
        f,
        str("{:.2f}".format(throughput_value))
    ]

    for v in tid_values:
        third_command.append(v)

    third_process = subprocess.Popen(third_command)

    # Wait for the second command to finish
    third_process.wait()
