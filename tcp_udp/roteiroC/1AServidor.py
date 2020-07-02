
from socket import *
import time


serverName = '' 
serverPort = 61000 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind((serverName, serverPort)) 
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) 
    message = message.decode('utf-8')

    if message=='data':
        reply = str(time.ctime())
        print ('Cliente %s enviou: %s, enviando: %s' % (clientAddress, message, reply))
        serverSocket.sendto(reply.encode('utf-8'), clientAddress)
    else:
        print('Comando errado')
        reply = 'Comando errado'
        print ('Cliente %s enviou: %s, enviando: %s' % (clientAddress, message, reply))
        serverSocket.sendto(reply.encode('utf-8'), clientAddress)
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor