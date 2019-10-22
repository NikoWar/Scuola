import socket
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = "127.0.0.1"
PORT = 1234

close = False
listOfThreads=[]
connectionList=[]

class ClientThread(Thread): #dichiarazione classe

    def __init__(self, clientIp, clientPort, connection):   #metodo costruttore
        Thread.__init__(self)
        self.clientIp = clientIp
        self.clientPort = clientPort            #variabili di classe
        self.connection = connection
        print(f"New thread started from {clientIp}, {clientPort}")  #messaggio per verificare la connessione

    def run(self):
        global close
        
        while True:
            data = self.connection.recv(BUFFSIZE)              #ricevo i dati, la stringa
            print(f"Server received data: {data.decode()} from {self.clientIp}")    #stampo quello che ricevo + indirizzo client
            self.connection.send("RECEIVED".encode())
            if data.decode()=="exit":
                break   #esco dal while True
        
        print("chiusura dal thread")
        close = True
        print(close)
        self.connection.close()
        #s.close()
            

class controlThread(Thread):
    
    def __init__(self, listOfThreads):
        Thread.__init__(self)
        self.listOfThreads=listOfThreads
        print(f"Control Thread")
    
    def run(self):
        global listOfThreads
        while True:
            if(close):
                print("Chiudo le connessioni")
                for t in self.listOfThreads:
                    t.join() 
                    print("Client chiuso")
                break


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))
s.listen(5)

print("Multithread python server : Waiting for client")

controlThread = controlThread(listOfThreads)
controlThread.start()

while True:
    conn, (ip, port) = s.accept()     #inizio la connessione
    connectionList.append(conn)
    newThread = ClientThread(ip, port, conn)  #nuovo thread
    newThread.start()
    listOfThreads.append(newThread)
    print(f"{listOfThreads} stampaaaa")
    
    if(close):
        print(close)
        print(f"{len(listOfThreads)} lunghezza listOfThreads" )
        print(f"{len(connectionList)} lunghezza connectionList" )
        if(listOfThreads==0):
            break

s.close()