import socket as sck

HOST = "192.168.10.53"
PORT = 1984

c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
c.connect((HOST, PORT))

while True:
    text = input()
    if text == "stop":
        break
    c.sendall(text.encode())
    data=c.recv(4096)
    print(data.decode())
    
c.close()