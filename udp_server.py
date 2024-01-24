#
# Taken from Computer Networking - A Top-Down Approach by Kurose & Ross
# 7th. Edition
# Page 163
#
from socket import *
serverPort = 13000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)