import socket
ADDRESS="0.0.0.0"
PORT = 1984

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDRESS, PORT))
s.listen()

conn, clientAddress = s.accept()
print("Connesso con ", conn)

while True:
    data = conn.recv(4096).decode()
    print("\n>client %s: %s" %(clientAddress, data))
    strToSend=input(">")
    conn.sendall(strToSend.encode())

    if(strToSend=="0"):
        break

conn.close()
s.close()

'''
BERKELEY

socket()    NON BLOCCANTE   CS
bind()      NON BLOCCANTE   S
listen()    NON BLOCCANTE   S
accept()    BLOCCANTE       S
recv()      BLOCCANTE       CS
sendall()   NON BLOCCANTE   CS
close()     NON BLOCCANTE   CS
connect()   BLOCCANTE       C

'''