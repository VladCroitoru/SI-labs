# InfoSec Lab #1 

## Implemented tasks: 
1. send UDP or/and TCP messages.
1. send a message at fixed intervals.
1. port scanning of a given IP.
1. get a page over http. 
1. send file over a network. 

### 1. Sending a TCP message.
Done using a simple TCP server/client. Getting to know the basics commands, creating a socket, binding, establishing a connection, listening and receiving a text message.

### 2. Send a message at fixed intervals.
Used the previous TCP server/client with the addition of a simple loop that takes time and max number of messages as input.

### 3. Port scanning of a given IP.
The idea behind the post scanner is pretty straight forward. Enter the host and the range of ports to be checked, and then it attempts to connect to each port. The output being the list of available ports.

### 4. Get a page over http.
Used a python library to do the whole thing and just printed the results. (the wrong way of implementing the task)

### 5. Send a file over a network.
Done again using the first basic TCP server/client by adding a while loop which basically reads from a file, sends the contents and the receiving end is just writting it down in a different file. Again implemented the wrong way as it is not sending the file over the network.
