import socket 

IP = 'localhost'
PORT = 12345

message = 'Revolutinary.'

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto(message.encode(), (IP, PORT))

udp_socket.close()

