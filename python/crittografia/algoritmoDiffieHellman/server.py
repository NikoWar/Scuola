import socket
import parametri
import DiffieHellman
import random

ADDRESS="0.0.0.0"
parametri.PORT = 1984

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDRESS, parametri.PORT))
s.listen()

conn, clientAddress = s.accept()
print("Connesso con ", conn)

b = random.randint(0, parametri.N)

strToSend=str(DiffieHellman.generaValore(b))
conn.sendall(strToSend.encode())

A = int(conn.recv(4096).decode())
print("\n>client %s: %s" %(clientAddress, A))

print(f"Il valore è {(A**b)%parametri.N}")

conn.close()
s.close()