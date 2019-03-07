#Nicolò Guerra 4AROB

from turtle import *
import random
t=Turtle()  #instanzio oggetto Turtle
print("Quante volte vuoi svoltare?")
i=int(input())
t.begin_poly()  #inizia a disegnare
cnt=0
n1=1    #dihiarazione variabili
n2=1
n3=0
while(cnt<i):   #while per calcolare la sequenza
    t.forward(1)   #disegna in avanti
    if(random.random()<0.5):
        t.left(90)      #gira di 90 gradi a sx
    else:
        t.right(90)     #gira di 90 gradi a dx
    cnt+=1

t.end_fill()    #smette di disegnare
done()      #rimane disegnato 