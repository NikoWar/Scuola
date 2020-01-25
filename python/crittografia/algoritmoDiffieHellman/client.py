import socket
import parametri
import DiffieHellman
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_SERVER = "192.168.10.91"
parametri.PORT = 1984

s.connect((IP_SERVER, parametri.PORT))
strToSend=""

a = random.randint(0, parametri.N)

B = int(s.recv(4096).decode())
strToSend = str(DiffieHellman.generaValore(a))
s.sendall(strToSend.encode())

print("Server: %s" % B)
print(f"Il valore è {(B**a)%parametri.N}") 
s.close()