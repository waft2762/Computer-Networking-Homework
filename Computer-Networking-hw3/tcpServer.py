from socket import *

# create socket
serverSocket = socket(AF_INET,SOCK_STREAM)

# bind local information
address = ('',8080)
serverSocket.bind(address)

# server listens TCP linking request from client
serverSocket.listen(1)
print('The Server is ready to receive')

while True:
    # if there is a client that wants to link server,create a new socket to accept it
    newSocket, clientSocket = serverSocket.accept()
    # receive the data from client
    recvData = newSocket.recv(1024).decode()
    returnData = recvData.upper()
    # return data to the client
    newSocket.send(returnData.encode())
    newSocket.close()
