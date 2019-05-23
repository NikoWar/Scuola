import socket as sck

HOST = "192.168.1.140"
PORT = 1984

c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
c.connect((HOST, PORT))

while True:
    text = input()
    if text == "e":
        break
    c.sendall(text.encode())
    data=c.recv(4096)
    print(data.decode())
    
c.close()