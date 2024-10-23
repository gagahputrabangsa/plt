from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("10.24.80.252", serverPort))
serverSocket.listen(5)
print("--Server Siap Melayani Request--")
nomer = 1

while True:
    connectionSocket, addr = serverSocket.accept()
    client_ip, client_port = addr
    try:
        pesanRequest = connectionSocket.recv(1024)
        if pesanRequest:
            # Reply message with the number from the server
            print(f"{nomer}. Client <{client_ip}>: {nomer}_{pesanRequest.decode().upper()}")
            
            pesanReply = f"{nomer}_{pesanRequest.decode()}"
            connectionSocket.send(pesanReply.encode())
            nomer += 1
        else:
            print(f"Client <{client_ip}> memutuskan koneksi.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        connectionSocket.close()

serverSocket.close()
