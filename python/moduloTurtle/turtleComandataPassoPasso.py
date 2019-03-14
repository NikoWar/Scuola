#Nicolò Guerra 4AROB

from turtle import *
import time
import random
passo=50
angolo=90
t=Turtle()  #instanzio oggetto Turtle
t.begin_poly()  #inizia a disegnare

while True:   #while per calcolare la sequenza
    print("Inserisci un comando per far muovere la turtle ('f','b','r','l')")
    print("(Inserisci 'e' per uscire)")
    comando=input()
    if(len(comando))>1:
        print("Inserisci un comando per volta!")
    elif comando=='f':  #if annidate per controllare la turtle
        t.forward(passo)
    elif comando=='r':
        t.right(angolo)
        t.forward(passo)
    elif comando=='l':
        t.left(angolo)
        t.forward(passo)
    elif comando=='b':
        t.back(passo)
    elif comando=='e':
        break
    else:
        print("Comando inserito non valido") #stampa se non viene riconosciuto un comando

time.sleep(3)
t.screen.bye()