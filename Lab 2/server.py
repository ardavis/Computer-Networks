# import socket module
from socket import *

serverPort = 4444
serverSocket = socket(AF_INET, SOCK_STREAM)

# prepare a server socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print 'Ready to serve'
while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send('404 File Not Found')

        # Close socket client
        connectionSocket.close()
