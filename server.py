import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('10.50.225.43', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is up and running. Waiting for a connection...')

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()

    try:
        print('Connected with:', client_address)

        # Receive the data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print('Received:', data)

        if data == 'Hi':
            # Send the response back to the client
            response = 'Hi'
            client_socket.send(response.encode('utf-8'))
            print('Sent:', response)

    finally:
        # Close the connection
        client_socket.close()
