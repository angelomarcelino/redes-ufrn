import socket

HOST = '' 
PORT = 8080 

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))

listen_socket.listen(1)

print ('Serving HTTP on port %s ...' % PORT)

while True:
    
    client_connection, client_address = listen_socket.accept()
    
    # imprime a conexão para debug
    print(client_address)
    
    request = client_connection.recv(1024)
    
    # imprime na tela o que o cliente enviou ao servidor
    print(request.decode('utf-8'))
    
    comando = request.decode('utf-8').split()

    # declaracao da resposta do servidor
    try:
        if comando[0] == 'GET':
            try:
                file = comando[1].split('/')[1]  # extrai o nome do arquivo
                
                if file == '':
                    file = 'index.html'
                
                f = open(file, 'r')
                http_response = "HTTP/1.1 200 OK\r\n\r\n" + f.read() + "\r\n"
                
                pass
            except:
                ext = comando[1].split('.')[1] # extrai a extensão do arquivo solicitado
                
                if ext != 'html':
                    http_response = "HTTP/1.1 404 Not Found\r\n\r\n"
                else:
                    f = open('error.html', 'r')
                    http_response = "HTTP/1.1 404 Not Found\r\n\r\n" + f.read() + "\r\n"
                
                pass
        else:
            f = open('badreq.html', 'r')
            http_response = "HTTP/1.1 400 Bad Request\r\n\r\n" + f.read() + "\r\n"
        pass
    except:
        http_response = "NO REQUEST"
        pass
            
    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    print(http_response)
    client_connection.send(http_response.encode('utf-8'))
    
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()