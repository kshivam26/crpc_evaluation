import re
import statistics

# Define the PID for which you want to calculate the mean/median
pid = "333751"

# Read the text file
with open("top_log_test.txt", "r") as file:
    data = file.read()

# Extract the lines containing the PID
lines = re.findall(rf"\b{pid}\b.*\n", data)

print(lines)

# Extract the "%CPU" values from the lines based on column number
cpu_values = []
for line in lines:
    columns = line.split()
    cpu = float(columns[8])  # Assuming the %CPU column is at index 8
    cpu_values.append(cpu)
    
# Calculate the mean and median
mean = statistics.mean(cpu_values)
median = statistics.median(cpu_values)
max = max(cpu_values)

# Print the results
print(f"Mean %CPU for PID {pid}: {mean:.2f}")
print(f"Median %CPU for PID {pid}: {median:.2f}")
print(f"Max %CPU for PID {pid}: {max:.2f}")