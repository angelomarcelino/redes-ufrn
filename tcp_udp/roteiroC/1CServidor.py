
from socket import * 
import os

serverName = '' 
serverPort = 61001
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind((serverName,serverPort)) 
serverSocket.listen(1) 
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() 
  sentence = connectionSocket.recv(1024) 
  sentence = sentence.decode('utf-8')
  os.system(sentence)
  
  connectionSocket.close()  # encerra o socket com o cliente
  
serverSocket.close() # encerra o socket do servidor