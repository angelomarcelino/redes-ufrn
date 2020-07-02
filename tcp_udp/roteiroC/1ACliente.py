
from socket import * 


serverName = 'localhost' 
serverPort = 61000 
clientSocket = socket(AF_INET, SOCK_DGRAM)

reply = 'Comando errado'

while reply == 'Comando errado':     
    message = input('Digite data: ')
    clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort)) 
    reply, serverAddress = clientSocket.recvfrom(2048)
    print('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, reply.decode('utf-8')))
    reply = reply.decode('utf-8')
clientSocket.close() 