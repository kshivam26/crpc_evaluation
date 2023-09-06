import os
import time
import subprocess

output_file = "top_log_test.txt"

# Clear the output file
open(output_file, "w").close()

while True:
    os.system('clear')
    process_name = 'deptran'
    process_ids = subprocess.check_output(["pgrep", "-d','", "-f", process_name])
    process_ids = process_ids.decode().strip().split(',')

    with open(output_file, "a") as file:
        subprocess.call(["top", "-H", "-b", "-n", "1", "-p"] + process_ids, stdout=file)

    time.sleep(1)
