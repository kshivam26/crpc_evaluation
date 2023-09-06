import re

def find_rpcid_x_occurrences(log_file_path, pattern="rpcid: 1151363955; xid:"):
    # Read the log file
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    # Variables to store the results
    result = []
    begin_request_count = 0

    for idx, line in enumerate(lines):
        if "==== inside void async_AppendEntries; calling client->begin_request" in line:
            begin_request_count += 1
            x_occurrences = []
            x_value = None

            for next_line in lines[idx + 1:]:
                if "==== inside void async_AppendEntries; calling client->begin_request" in next_line:
                    break  # Stop checking when the next begin_request pattern is found

                if pattern in next_line:
                    match = re.search(r"xid: (\d+)", next_line)
                    if match:
                        x_value = match.group(1)
                        x_occurrences.append(next_line.strip())
                    elif x_value:
                        x_occurrences.append(f"{next_line.strip()} [Mismatch]")

            if len(x_occurrences) == 6:
                result.append((x_value, x_occurrences))
            else:
                result.append((x_value, ["[Not enough occurrences]"]))

    return result


if __name__ == "__main__":
    log_file_path = "../depfast-ae/logfile.txt"
    occurrences_result = find_rpcid_x_occurrences(log_file_path)

    for idx, (x_value, occurrences) in enumerate(occurrences_result, start=1):
        print(f"Result for occurrence {idx}:")
        if len(occurrences) == 1 and "[Not enough occurrences]" in occurrences:
            print(f"Value of x not found or not enough occurrences before the second 'begin_request' pattern line.")
        else:
            print(f"Value of x: {x_value} appeared six times before the second 'begin_request' pattern line.")
            print("x positions:")
            for pos in occurrences:
                print(pos)
