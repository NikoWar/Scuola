#Nicolò Guerra 4AROB

import random
import turtle as t

nTurtle=0
lTurtle=[]
height=800
weight=800

nTurtle=int(input("Quante turtle partecipano alla Turtle Race?"))

for i in range(0, nTurtle):
    lTurtle.append(t.Turtle())

height=height//nTurtle

t.setup(weight, height)
