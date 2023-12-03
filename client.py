import os
import maze
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




# Get user input
user_input = input("Press any key to start!\n")

# Play the game on the client side
maze.play(maze.maze, user_input,client_socket)

if user_input.lower() == 'exit':
    client_socket.close()