from socket import *

# create socket
clientSocket = socket(AF_INET,SOCK_STREAM)
# link to server
serAddr = ("127.0.0.1",8080)
clientSocket.connect(serAddr)

# send lowercase data
sendData = raw_input('Please input lowercase sentence:')
clientSocket.send(sendData.encode())

# receive data from server
recv = clientSocket.recv(1024)
print('From Server:  '+ recv.decode())

#close socket
clientSocket.close()


