
from socket import *
import os

serverName = 'localhost' 
serverPort = 61001 
clientSocket = socket(AF_INET,SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 


sentence = input('Digite comando: ')
clientSocket.send(sentence.encode('utf-8'))
clientSocket.close() 



