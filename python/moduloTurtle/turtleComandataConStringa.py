#Nicolò Guerra 4AROB

from turtle import *
import random
t=Turtle()  #instanzio oggetto Turtle
print("Inserisci una stringa di comandi ('f','b','r','l')")
comandi=input()
t.begin_poly()  #inizia a disegnare
cnt=0

while(cnt<len(comandi)):   #while per calcolare la sequenza
    if comandi[cnt]=='f':  #if annidate per controllare la turtle
        t.forward(10)
    else:
        if comandi[cnt]=='r':
            t.right(90)
            t.forward(10)
        else:
            if comandi[cnt]=='l':
                t.left(90)
                t.forward(10)
            else:
                if comandi[cnt]=='b':
                    t.back(10)
                else:
                    print("Comando inserito non valido") #stampa se non viene riconosciuto un comando
            
    cnt+=1

t.end_fill()    #smette di disegnare
done()      #rimane disegnato 