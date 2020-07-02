
from socket import *


serverName = 'localhost' 
serverPort = 61000 
clientSocket = socket(AF_INET,SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 

reply = '404'

while reply == '404':
    sentence = input('Digite obter arquivo.txt: ')
    clientSocket.send(sentence.encode('utf-8'))
    reply = clientSocket.recv(1024)
    reply = reply.decode('utf-8')
    
    file = open("arquivoR.txt", "w")
    file.write(reply)
    file.close()

    #print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, reply.decode('utf-8')))

clientSocket.close() 
