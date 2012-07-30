from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12003

clientSocket = socket(AF_INET, SOCK_DGRAM)
# ping here
for i in range(1, 10):
    startTime = time.time()
    message = 'Ping ' + str(i) + ' ' + str(startTime)

    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    endTime = time.time()

    try:
        print "Modified Message: " + modifiedMessage
        print "RTT: " + str((endTime - startTime) * 1000) + " seconds"
    except:
        print 'Request timed out'

clientSocket.close()

