import math
import random
import parametri

def generaValore(num):
    return (parametri.g**num)%parametri.N

def decrittografia(numRicevuto, numGenerato):
    return (numRicevuto**numGenerato)%parametri.N

def algoritmoManInTheMiddle(valoreScambiato):
    for y in range(0, parametri.N):
        if (parametri.g**y)%parametri.N == valoreScambiato:
            return y
    