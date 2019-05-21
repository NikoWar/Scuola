import socket as sck

HOST = "localhost"
PORT = 1984

c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
c.connect((HOST, PORT))
c.sendall("Ciao".encode())
c.recv(4096)
c.close()