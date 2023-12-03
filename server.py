import socket
import os
#import maze  # Assuming you have a module named 'maze'
def receive_data(client_socket):
    return client_socket.recv(1024).decode('utf-8')

def send_data(client_socket, data):
    client_socket.send(data.encode('utf-8'))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("localhost")
port = 6789

server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Send a welcome message to the client
    welcome_message = "Welcome to the maze game server!"
    client_socket.send(welcome_message.encode('utf-8'))

    # Receive data from the client in a loop
    while True:
        data_from_client = receive_data(client_socket)

        if not data_from_client:
            # If no data is received, the client has closed the connection
            print(f"Client {addr} disconnected.")
            break

        # Process the received data (assuming it's coordinates)
        coordinates = data_from_client
        print(f"Message recieved from {addr}: {coordinates}")
