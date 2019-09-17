import socket
ADDRESS = "0.0.0.0"
PORTA_SERVER = 8080

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.bind((ADDRESS, PORTA_SERVER))
socketServer.listen()

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_SERVER = "192.168.10.85"
PORTA_CLIENT = 8080

conn, clientAddress = socketServer.accept()
print("Connesso con ", conn)

socketClient.connect((IP_SERVER, PORTA_CLIENT))

while True:
    data = conn.recv(4096).decode()
    print("\n>client %s: %s" %(clientAddress, data))
    
    strToSend = data

    if(data=="EXIT"):
        break

    socketClient.sendall(strToSend.encode())

conn.close()
socketServer.close()
socketClient.close()