import socket
from threading import Thread

msgDict = {}

class ReceiverThread(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
    
    def run(self):
        while True:
            data = self.socket.recv(4096).decode()
            print(f"Server {data}")

            _, send_nick, msg = data.split("§")

            if msgDict.get(send_nick, "null") == "null":
                msgDict[send_nick] = [msg]
            
            else:
                msgDict[send_nick].append(msg)
            
            print(msgDict)
            
                
class SenderThread(Thread):
    
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
    
    def run(self):
        while True:
            strToSend=""
            strToSend = input("\n>")
            if(strToSend=="exit"):
                break
            else:
                self.socket.sendall(strToSend.encode())
        
        self.socket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_SERVER = "192.168.0.105"
PORT = 2500

s.connect((IP_SERVER, PORT))

rec_thread = ReceiverThread(s)
send_thread = SenderThread(s)

rec_thread.start()
send_thread.start()