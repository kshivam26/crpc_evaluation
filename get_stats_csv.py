def get_median_throughput(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        throughputs = [float(line.strip().split()[-1]) for line in data]
        sorted_throughputs = sorted(throughputs)
        median_idx = len(sorted_throughputs) // 2
        median_throughput = sorted_throughputs[median_idx]
        return median_throughput

def get_row_by_throughput(filename, target_throughput):
    with open(filename, 'r') as file:
        data = file.readlines()
        for line in data:
            throughput = float(line.strip().split()[-1])
            if throughput == target_throughput:
                return line.strip()

def keep_highest_max_value_set(row):
    values = row.split()
    max_values = [float(values[i]) for i in range(8, len(values) - 1, 7)]
    max_value = str(max(max_values))
    # print("max_value is: ", max_value)
    result = " ".join(values[1:8])
    # print("current result is: ", result)
    for i in range(8, len(values), 7):
        # print("current value[i] is: ", values[i])
        if (values[i] == max_value):
            # print("current value equals max value")
            for j in range(i, i+7):
                result += " " + values[j]
            break
    result+= " " + values[-1]
    # print("result is: ", result)
    # highest_max_value_set = [str(max_value) if float(values[i]) == max_value else '0' for i in range(8, len(values), 7)]
    return result

def generate_configurations():
    config_list = []
    num_clients_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    num_replicas_range = [3, 5, 7]

    for num_clients in num_clients_range:
        for num_replicas in num_replicas_range:
            config = f"{num_clients}c1s{num_replicas}r1p"
            config_list.append(config)

    return config_list



def main():
    
    config_list = generate_configurations()
    num_clients_range = [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    num_replicas_range = [3, 5, 7]

    with open("v10_stats/stats_csv_110_to_200.txt", 'a') as file:
        for num_clients in num_clients_range:
            for num_replicas in num_replicas_range:        
                no_cRPC_file = f"v10_stats/v10_stats_{num_clients}c1s{num_replicas}r1p_no_cRPC"
                cRPC_file = f"v10_stats/v10_stats_{num_clients}c1s{num_replicas}r1p_cRPC"
                
                no_cRPC_median_throughput = get_median_throughput(no_cRPC_file)
                cRPC_median_throughput = get_median_throughput(cRPC_file)

                no_cRPC_median_row = get_row_by_throughput(no_cRPC_file, no_cRPC_median_throughput)
                cRPC_median_row = get_row_by_throughput(cRPC_file, cRPC_median_throughput)

                print(no_cRPC_file)
                result = str(num_clients) + " " + str(num_replicas) + " " + keep_highest_max_value_set(cRPC_median_row) + " " + keep_highest_max_value_set(no_cRPC_median_row)
                print (result)
                file.write(result)
                file.write("\n")   
                
            

if __name__ == "__main__":
    main()
