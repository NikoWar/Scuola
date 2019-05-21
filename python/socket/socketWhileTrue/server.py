import socket as sck

HOST = "localhost"
PORT = 1984

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
con, addr =s.accept()
print("Connect to "+ str(addr))
while True:
    data=con.recv(4096)
    print(data.decode())
    if data.decode() == "stop":
        break
    con.sendall(input().encode())

s.close()