import socket               


host = 'localhost' 
port = 12345                 

client_socket = socket.socket()
client_socket.connect((host, port))


data = open('message.rtf','rb')

sending_file = data.read(1024)

while (sending_file):
    print 'Uploading'
    client_socket.send(sending_file)
    sending_file = data.read(1024)

data.close()
print "Done Sending"
client_socket.shutdown(socket.SHUT_WR)
print client_socket.recv(1024)
client_socket.close()                   
