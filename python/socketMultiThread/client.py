import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_SERVER = input("Indirizzo del server: ")
PORT = int(input("Porta: "))

s.connect((IP_SERVER, PORT))
strToSend=""

while True:
    strToSend = input("\n>")
    if(strToSend=="0"):
        break

    s.sendall(strToSend.encode())
    data = s.recv(4096).decode()
    print("Server: %s" % data)

s.close()