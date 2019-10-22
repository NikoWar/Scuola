import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_SERVER = "127.0.0.1"
PORT = 1234

s.connect((IP_SERVER, PORT))
strToSend=""

while True:
    strToSend = input("\n>")

    s.sendall(strToSend.encode())
    if(strToSend=="exit"):
        break
    data = s.recv(4096).decode()
    print("Server: %s" % data)

s.close()