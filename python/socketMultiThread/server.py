import socket
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = "127.0.0.1"
PORT = 1234

class ClientThread(Thread): #dichiarazione classe

    def __init__(self, clientIp, clientPort):   #metodo costruttore
        Thread.__init__(self)
        self.clientIp = clientIp
        self.clientPort = clientPort            #variabili di classe
        print(f"New thread started from {clientIp}, {clientPort}")  #messaggio per verificare la connessione

    def run(self):
        while True:
            data = conn.recv(BUFFSIZE)              #ricevo i dati, la stringa
            print(f"Server received data: {data.decode()} from {self.clientIp}")    #stampo quello che ricevo + indirizzo client
            if data.decode()=="exit":
                break   #esco dal while True
            conn.send("RECEIVED".encode())

class ThreadDiControllo(Thread):
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))
s.listen(5)
listOfThreads=[]
print("Multithread python server : Waiting for client")

while True:
    (conn, (ip, port)) = s.accept()     #inizio la connessione
    newThread = ClientThread(ip, port)  #nuovo thread
    newThread.start()
    listOfThreads.append(newThread)

for t in listOfThreads:
    t.join()