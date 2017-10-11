import socket              

         
host = 'localhost'
port = 12345   

tcp_server = socket.socket()              
tcp_server.bind((host, port)) 

data = open('received_message.rtf','wb')
tcp_server.listen(5)   
print('Waiting for client')              


while True:
    client_socket, addr = tcp_server.accept()     
    incoming_file = client_socket.recv(1024)
    while (incoming_file):
        print "Downloading"
        data.write(incoming_file)
        incoming_file = client_socket.recv(1024)
    data.close()
    print "File transfer done"
    client_socket.send('File received.')
    client_socket.close()   
    tcp_server.close()             