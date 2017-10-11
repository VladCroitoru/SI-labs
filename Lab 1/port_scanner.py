from threading import Thread
import socket


host_name = raw_input('Enter the host: ')
host = socket.gethostbyname(host_name)
from_port = input('Starting port:  ')
to_port = input('Last port:  ')   

counting_open = []
counting_close = []
threads = []


def scan(port):
	s = socket.socket()
	result = s.connect_ex((host,port))
	#print('port number '+(str(port)))      
	if result == 0:
		counting_open.append(port)
		print((str(port))+' -> open') 
		s.close()
	else:
		counting_close.append(port)
		#print((str(port))+' -> closed') 
		s.close()

for i in range(from_port, to_port+1):
	t = Thread(target=scan, args=(i,))
	threads.append(t)
	t.start()
	
[x.join() for x in threads]

print(counting_open)