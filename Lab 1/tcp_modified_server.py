import socket
import time

IP = 'localhost'
PORT = 12347



tcp_server = socket.socket() 

 
tcp_server.bind((IP, PORT))
print('bind successful')


tcp_server.listen(5)
print('server is listening')


client_socket, addr = tcp_server.accept()


time_interval = raw_input('Enter the time interval: ')
print(time_interval)
nr_messages = raw_input('Enter the number of messages to be sent: ')
print(nr_messages)
seconds = 0


for i in range (0, int(nr_messages)):

	client_socket.send(str(seconds) + ' seconds have passed'.encode())
	seconds += int(time_interval)
	time.sleep(float(time_interval))


client_socket.send('disconnect')
client_socket.close()
tcp_server.close()
