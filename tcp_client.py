#
# Taken from Computer Networking - A Top-Down Approach by Kurose & Ross
# 7th. Edition
# Page 166
#

from socket import *
serverName = 'localhost' # 'hostname' in the original source code
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ',modifiedSentence.decode())
clientSocket.close()