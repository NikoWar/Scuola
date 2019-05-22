import socket as sck

HOST = "0.0.0.0"    #se vogliamo far collegare uno o più client è meglio utilizzare l'indirizzo IP "this" = 0.0.0.0
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