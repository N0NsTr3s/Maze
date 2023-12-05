import os

import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def receive_data(client_socket):
    return client_socket.recv(1024).decode('utf-8')

def send_data(client_socket, data):
    client_socket.send(data.encode('utf-8'))

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = socket.gethostbyname("localhost")
port = 6789

# Connect to the server
client_socket.connect((host, port))

# Receive the welcome message from the server
welcome_message = receive_data(client_socket)
print(welcome_message)


input("Press Enter to continue...")
while True:

    # Get user input
    direction = input("Which direction do you want to move (u/d/l/r)? Or do you give up? (Yes): ")

    if direction == 'exit':
        client_socket.close()

    while direction not in ["u", "d", "l", "r", "Yes"]:
        print("Invalid direction")
        direction = input("Which direction do you want to move (u/d/l/r)? Or do you give up? (Yes): ")
        
        continue
    send_data(client_socket, direction)       
    response = receive_data(client_socket)
    if "You won!" in response or "Ok!" in response or "A Monster ate you!!" in response or "You`ve hit a wall" in response:
        print(response)
    else:
        pass