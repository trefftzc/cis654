#
# Taken from Computer Networking - A Top-Down Approach by Kurose & Ross
# 7th. Edition
# Page 161
#

from socket import *
serverName = 'localhost' # 'hostname' in the original source code
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()