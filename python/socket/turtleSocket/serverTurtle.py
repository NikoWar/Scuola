from turtle import *
import time
import random
import socket as sck

#INIZIALIZZAZIONE TURTLE
passo=50
angolo=90
t=Turtle()  #instanzio oggetto Turtle
t.begin_poly()  #inizia a disegnare

#INIZIALIZZAZIONE SOCKET
HOST = "0.0.0.0"
PORT = 1984

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

con, adr = s.accept()
print("Connect to "+ str(adr))

while True:   #while per calcolare la sequenza
    data=con.recv(4096)

    if (data.decode()=="e"):
        break

    print(data.decode())
    comando=data.decode()
    if(len(comando))>1:
        con.sendall("Inserisci una stringa per volta".encode())
    elif comando=='f':  #if annidate per controllare la turtle
        t.forward(passo)
        con.sendall("(t.xcor+t.ycor)".encode())
    elif comando=='r':
        t.right(angolo)
        t.forward(passo)
        con.sendall("(t.xcor+t.ycor)".encode())
    elif comando=='l':
        t.left(angolo)
        t.forward(passo)
        con.sendall("(t.xcor+t.ycor)".encode())
    elif comando=='b':
        t.back(passo)
        con.sendall("(t.xcor+t.ycor)".encode())
    elif comando=='e':
        break
    else:
        con.sendall(("Comando inserito non valido").encode())

time.sleep(3)
t.screen.bye()