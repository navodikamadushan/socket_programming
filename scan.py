import socket

# Define the target host
target_host = '10.50.225.43' 

# Define the range of ports to scan
start_port = 1
end_port = 65535

# Perform the port scan
for port in range(start_port, end_port+1):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt (optional)
        client_socket.settimeout(0.1)
        
        # Attempt to connect to the target port
        result = client_socket.connect_ex((target_host, port))
        
        # Check if the port is open
        if result == 0:
            print(f'Port {port} is opened')
        else:
            print(f"Port {port} is closed, result is {result}")
        
        # Close the socket
        client_socket.close()
    
    except socket.error:
        pass
