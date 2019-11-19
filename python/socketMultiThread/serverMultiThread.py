import socket
import sqlite3
import serverSettings
from threading import Thread 

client_online = {}
connection_online = {}

class ServerThread(Thread):

    def __init__(self, connection, ip_address, port):
       self.connection = connection
       self.ip_address = ip_address
       self.port = port

    def run(self):
        msg = self.connection.recv(4096).decode()
        rec_nick, _, _ = msg.split("§")
        connection_online.get(rec_nick, client_online["default"]).send(msg.encode())



class ServerThreadsManager(Thread):

    def __init__(self, server_ip, server_port, max_clients):
        Thread.__init__(self)
        self.server_ip = server_ip
        self.server_port = server_port
        self.max_clients = max_clients
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP IPv4 socket creation
        #DataBase
        self.db_connection = sqlite3.connect(serverSettings.DB_NAME)
        self.cursor = self.db_connection.cursor()

    def run(self):
        self.sock.bind((self.server_ip, self.server_port))
        self.sock.listen(self.max_clients) 
        try:
            connection, (ip, port) = self.sock.accept() 
        except InterruptedError:
            print("INTERRUPT ERROR")

        newConnection = ServerThread(connection, ip, port)

        nickList = self.cursor.execute(f"SELECT nick_name FROM CLIENT WHERE ip_address={ip}")
        if len(nickList)==1:
            client_online[nickList[0]] = newConnection
            connection_online[client_online[0]] = connection


mngThread = ServerThreadsManager(serverSettings.SERVER_IP, serverSettings.PORT, serverSettings.MAX_CLIENT)
mngThread.start()