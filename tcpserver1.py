from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind server to specific IP and port
serverSocket.bind(("10.24.80.252", serverPort))
serverSocket.listen(5)

# Displaying the server IP and Port information
print(f"--Server Siap Melayani Request pada IP: 10.24.80.252, Port: {serverPort}--")
nomer = 1

while True:
    connectionSocket, addr = serverSocket.accept()
    client_ip, client_port = addr
    try:
        pesanRequest = connectionSocket.recv(1024)
        if pesanRequest:
            print(f"{nomer}. Client <{client_ip}>: {nomer}_{pesanRequest.decode().upper()}")
            nomer += 1
            pesanReply = pesanRequest.decode()
            connectionSocket.send(pesanReply.encode())
        else:
            print(f"Client <{client_ip}> memutuskan koneksi.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        connectionSocket.close()

serverSocket.close()
