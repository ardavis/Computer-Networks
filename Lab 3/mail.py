# -*- coding: cp1252 -*-
from socket import *

# Choose a mail server
mailserver = 'mailhost.kettering.edu'
mailport = 25

# Create a socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))

recv0 = clientSocket.recv(1024)
print recv0
if recv0[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
#mailFromCommand = 'MAIL FROM: <harr8289@kettering.edu>\r\n'
mailFromCommand = 'MAIL FROM: <davi9267@kettering.edu>\r\n'
clientSocket.send(mailFromCommand)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
    print '250 reply not received from server. MAIL FROM'

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <davi9267@kettering.edu>\r\n'
clientSocket.send(rcptToCommand)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
    print '250 reply not received from server. RCPT TO'

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
    print '354 reply not received from server. DATA'

# Send message data.
msg = "\r\n I love computer networks!\r\n"
clientSocket.send(msg)

# Message ends with a single period.
endmsg = "\r\n.\r\n"
clientSocket.send(endmsg)
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != '250':
    print '250 reply not received from server. End Msg'

# Send QUIT command and get server response
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand)
recv7 = clientSocket.recv(1024)
print recv7
if recv7[:3] != '221':
    print '221 reply not received from server. Quit'
