#Su python si può importare in più modi
 #import LIBRERIA
 #LIBRERIA metodo

 #import LIBRERIA as L
 #L.metodo

 #from LIBRERIA import NOME(I)MODULO(I)
 #metodo

#Nicolò Guerra 4AROB

from turtle import *
t=Turtle()  #instanzio oggetto Turtle
print("Qaunti numeri della sequenza vuoi calcolare?")
i=int(input())
t.begin_poly()  #inizia a disegnare
cnt=0
n1=1    #dihiarazione variabili
n2=1
n3=0

while(cnt<i):   #while per calcolare la sequenza
    n3=n1+n2
    n2=n3
    n1=n2
    t.forward(n3)   #disegna in avanti
    t.left(90)      #gira di 90 gradi
    cnt+=1

t.end_fill()    #smette di disegnare
done()      #rimane su 