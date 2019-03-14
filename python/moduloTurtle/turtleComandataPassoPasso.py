#Nicolò Guerra 4AROB

from turtle import *
import random
t=Turtle()  #instanzio oggetto Turtle
t.begin_poly()  #inizia a disegnare

while True:   #while per calcolare la sequenza
    print("Inserisci un comando per far muovere la turtle ('f','b','r','l')")
    print("(Inserisci 'e' per uscire)")
    comando=input()
    if(len(comando))>1:
        print("Inserisci un comando per volta!")
    else:
        if comando=='f':  #if annidate per controllare la turtle
            t.forward(10)
        else:
            if comando=='r':
                t.right(90)
                t.forward(10)
            else:
                if comando=='l':
                    t.left(90)
                    t.forward(10)
                else:
                    if comando=='b':
                        t.back(10)
                    else:
                        if comando=='e':
                            break
                        else:
                            print("Comando inserito non valido") #stampa se non viene riconosciuto un comando

t.end_fill()    #smette di disegnare
done()      #rimane disegnato 