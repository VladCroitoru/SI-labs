import socket

IP = 'localhost'
PORT = 12347


client_socket = socket.socket()


client_socket.connect((IP, PORT))
print('connected successfuly')


message = client_socket.recv(1024)
print(message.decode())

client_socket.close()