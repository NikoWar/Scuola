#Nicolò Guerra 4AROB

from turtle import *
import random
passo=50
angolo=90
t=Turtle()  #instanzio oggetto Turtle
print("Inserisci una stringa di comandi ('f','b','r','l')")
comandi=input()
t.begin_poly()  #inizia a disegnare

for comando in comandi:   #while per calcolare la sequenza
    if comando=='f':  #if annidate per controllare la turtle
        t.forward(passo)
    elif comando=='r':
        t.right(angolo)
        t.forward(passo)
    elif comando=='l':
        t.left(angolo)
        t.forward(passo)
    elif comando=='b':
        t.back(passo)
    else:
        print("Comando inserito non valido") #stampa se non viene riconosciuto un comando
            

t.end_fill()    #smette di disegnare
done()      #rimane disegnato 