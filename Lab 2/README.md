# InfoSec Lab 2
## Objective: Learn how to use the network as an attack vector.
### Implementation:
1. First of all download all the necessarry tools:
    - XAMPP (running the Apache WebServer)
    - OWASP Switchblade 4.0 (desinged to test your networks/servers security and ability to withstand an attack)

1. Run the "ipconfig" in the Command Prompt to get the localhost address or just use 127.0.0.1.
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/cmd_1.png "Windows IP configuration")

1. Run the XAMPP Control Panel and start the Apache service.
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/xampp_2.png "Apache Control Panel window")

1. Open a browser window and check the localhost for the running Apache page, can also be done by pressing the admin button in the XAMPP CP.
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/target.png "The target page")

1. Start the Switchblade tool and enter the IPv4 address in the URL field.
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/OWASP_2.png "The DoS tool window")

1. Now enter the Connections and Connections rate as you desire and press the 'Run attack' button.
     - Press the 'Netstat' button to view the TCP sockets that are being run in real time.
     - Check the task manager to see the CPU usage during the attack.
     - Refresh the target page to see if it is still up and running.
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/gif_process.gif "Gif of the attack")

### Results:
1. The CPU usage during the attack spiked:
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/taskmgr_final.png "CPU usage during attack")

1. By checking the acces logs, we can check the connections created:
![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%202/images/access_logs.png "Acces logs")

### Conclusion:
The main idea behind a DoS attack is to overwhelm the server with requests/connections and exhaust its processing power/bandwidth or ability to respond to the real users hence the "denial" of service. Generally done by creating thousands of connections and slowly get or post data from/to the servers. There are several types of DoS attacks depending on the layer and weakness targeted, in the laboratory work above we got an HTTP slow GET/POST attack demonstration.
Securing a network can be done throught various software, the use of SYN cookies as a measure to counter the SYN flood and the use of proxy servers that act as a filter and a traffic control police officer, by deciding what goes through and fragmenting the traffic. But no matter how much you invest to prevent such an attack, a good rule of thumb is to always ensure that your network can recover from an attack if it happens to fall from one.
