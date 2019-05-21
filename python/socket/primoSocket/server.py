import socket as sck

HOST = "localhost"
PORT = 1984

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
con, addr =s.accept()
print("Connect to "+ str(addr))
data=con.recv(4096)
print(data.decode())
con.sendall(data)
s.close()