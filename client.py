import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = 'Hi'
    client_socket.send(message.encode('utf-8'))
    print('Sent:', message)

    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print('Received:', response)

finally:
    # Close the connection
    client_socket.close()
