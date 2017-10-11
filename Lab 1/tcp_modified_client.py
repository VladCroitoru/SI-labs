import socket

IP = 'localhost'
PORT = 12347


client_socket = socket.socket()


client_socket.connect((IP, PORT))
print('connected successfuly')


while True:
	message = client_socket.recv(1024)
	print(message.decode())
	if message.strip() == 'disconnect':
		client_socket.close()

