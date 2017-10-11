import socket 

IP = 'localhost'
PORT = 12345


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((IP, PORT))

message, addr = udp_socket.recvform(1024)

print(message)

udp_socket.close()