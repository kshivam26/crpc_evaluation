import os

def replace_servers_in_process(input_file, output_file, num_new_servers):
    with open(input_file, 'r') as file:
        config_text = file.read()

    # Generate new server ids and ports based on the number of servers to add
    new_servers = [f"s{i+1}01:90{i+1:02}" for i in range(num_new_servers)]

    # Find the location of the server list in the configuration text
    server_list_start = config_text.find('[', config_text.find('server:')) + 1
    server_list_end = config_text.find(']', server_list_start)

    # Replace the existing server list with the new server list
    new_server_list_text = ', '.join([f'"{server}"' for server in new_servers])
    config_text = config_text[:server_list_start] + new_server_list_text + config_text[server_list_end:]

    # Find the start and end indices of the process section
    process_section_start = config_text.find('process:\n') + len('process:\n')
    process_section_end = config_text.find('\n\n', process_section_start)

    # Get the existing process entries and remove the first three lines
    existing_process_entries = config_text[process_section_start:process_section_end].strip()
    existing_process_entries = '\n'.join(existing_process_entries.splitlines()[3:])

    # Append the new process entries for new servers
    new_process_entries = '\n'.join([f'  {server.split(":")[0]}: localhost' for server in new_servers])

    # Update the process section with modified entries
    config_text = config_text[:process_section_start] + new_process_entries + '\n' + existing_process_entries + config_text[process_section_end:]

    # Save the modified configuration to a new YAML file
    # output_file = f"output_config_with_{num_new_servers}_new_servers.yml"
    with open(output_file, 'w') as file:
        file.write(config_text)

    return output_file


# Example usage
current_directory = os.getcwd()
server_folder = os.path.join(current_directory, "servers_new")
if not os.path.exists(server_folder):
    os.makedirs(server_folder)
        
ref_file_main = '<x>c1s<y>r1p.yml'
for i in range(10, 210, 10):
    ref_file = ref_file_main.replace("<x>", str(i))
    
    for j in range(15, 22, 2):
        output_file = server_folder + "/" +ref_file.replace("<y>", str(j))
        input_file = ref_file.replace("<y>", "3")
        result_file = replace_servers_in_process(input_file, output_file, j)
