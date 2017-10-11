import socket

IP = 'localhost'
PORT = 12345


tcp_server = socket.socket() 

 
tcp_server.bind((IP, PORT))
print('bind successful')


tcp_server.listen(5)
print('server is listening')


client_socket, addr = tcp_server.accept()


message = raw_input('Enter message: ')
client_socket.send(message.encode())


client_socket.close()
tcp_server.close()
