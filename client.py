from socket import * 
clientSocket = socket(AF_INET, SOCK_STREAM) 
serverName = "192.168.1.9" 
serverPort = 12000     
clientSocket.connect( (serverName, serverPort) ) 
pesan = input("Masukan pesan yang akan dikirim:") 
clientSocket.send(pesan.encode()) 
reply = clientSocket.recv(1024) 
print("Reply dari server:", reply.decode()) 
clientSocket.close()
