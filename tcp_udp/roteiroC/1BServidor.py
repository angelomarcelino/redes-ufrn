
from socket import * 


serverName = '' 
serverPort = 61000 
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind((serverName,serverPort)) 
serverSocket.listen(1) 
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() 
  sentence = connectionSocket.recv(1024) 
  sentence = sentence.decode('utf-8')
  file = open("arquivoE.txt", "r")

  if sentence == 'obter arquivo.txt':
      reply = file.read()
      print ('Cliente %s enviou: %s, transformando em: %s' % (addr, sentence, reply))
  else:
      reply = '404'
      print ('Cliente %s enviou: %s, transformando em: %s' % (addr, sentence, reply))

  connectionSocket.send(reply.encode('utf-8')) 
  connectionSocket.close() # encerra o socket com o cliente
  
  #capitalizedSentence = sentence.upper() 
  
  
serverSocket.close() # encerra o socket do servidor