import json
# Given configuration template
config_template = '''\
site:
  server: # each line is a partition, the first is the master site_name:port
    - [SERVERS_PLACEHOLDER]
  client: # each line is a partition
    - [CLIENTS_PLACEHOLDER]

# process_name - host_addr map
process:
[SITES_servers]
[SITES_clients]
    
host:
  localhost: 127.0.0.1

'''

# Function to generate configurations for N clients
def generate_client_configurations(num_clients):
    clients = []
    for i in range(1, num_clients + 1):
        client_name = f"c{i}01"
        clients.append(client_name)
    # print(json.dumps(clients))
    
    servers = '["s101:7140", "s201:7141", "s301:7142", "s401:7143", "s501:7144"]'
    sites = '\n'.join([f'  {client}: localhost' for client in clients])

    config = config_template.replace("[SERVERS_PLACEHOLDER]", servers)
    config = config.replace("[CLIENTS_PLACEHOLDER]", json.dumps(clients))
    config = config.replace("[SITES_clients]", sites, 1)
    
    # Add servers under process section
    process_servers = "\n".join([f"  {server}: localhost" for server in ["s101", "s201", "s301", "s401", "s501"]])
    config = config.replace("[SITES_servers]", process_servers, 1)

    return config

# Generate configurations for 20, 30, ..., 200 clients
for num_clients in range(110, 201, 10):
    config = generate_client_configurations(num_clients)
    with open(f"generated_clients/{num_clients}c1s5r1p.yml", "w") as file:
        file.write(config)

