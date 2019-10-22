import socket
import serverSettings
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((serverSettings.SERVER_IP, serverSettings.PORT))

class ServerThread(Thread):

    def __init__(self, connection, clientIp, clientPort):   #metodo costruttore
        Thread.__init__(self)
        #variabili di classe
        self.clientIp = clientIp    
        self.clientPort = clientPort    
        self.connection = connection

    def run(self):
        print(f"***Established connection with {self.clientIp}:{self.clientPort}***")
        while True:
            message = self.connection.recv(serverSettings.BUFFSIZE).decode()

            if message == serverSettings.CLOSE_CONNECTION_MSG:
                break
            elif message == "":
                pass
            elif message != serverSettings.CLOSE_CONNECTION_MSG:
                print(f"From {self.clientIp}:{self.clientPort} > {message}")
                self.connection.send(message.encode())

        print("Close thread")
        self.connection.close()
        


class ConnectionsManager(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.connectionsList=[]
        self.threadList=[]

    def run(self):
        print(f"Listening new connections on port {serverSettings.PORT}")
        while True:
            sock.listen(serverSettings.MAX_CLIENT)
            connection, (ip, port) = sock.accept()
            newThread = ServerThread(connection, ip, port)
            newThread = Thread(args=(newThread, ))
            newThread.start()
            self.connectionsList.append(newThread)
            self.threadList.append(newThread)
