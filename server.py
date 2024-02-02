
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and port for the server
server_ip = 'localhost'
server_port = 8080

# Bind the socket to the IP and port
s.bind((server_ip, server_port))

# Listen for incoming connections
s.listen(5)

while True:
    # Accept a connection
    c, addr = s.accept()
    print('Got connection from', addr)

    # Send a message to the client
    c.send(b'Thank you for connecting')

    # Close the connection
    c.close()
