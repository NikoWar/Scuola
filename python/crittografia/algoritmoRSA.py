'''
    Nicolò Guerra 5AROB
'''
import random

def primeNumberRdm():
    rdm_number = random.randint(10, 100)
    k = 6
    cnt_prime_number = 4
    isPrime = True
    while True:
        for p in range(2, k//2):
            if (k % p == 0):
                isPrime = False

        if isPrime:
            cnt_prime_number = cnt_prime_number+1
            if (cnt_prime_number == rdm_number):
                break
        k = k+1
        isPrime = True
    
    print(f"Numero primo > {k}")
    return k

def MCD(a, b):
    while True:
        result = a % b
        if result == 0:
            break
        
        a, b = b, result

    return b

def mcm(a, b):
    return int((a*b)/MCD(a, b))

def findC(m):
    for i in range (2, m):
        if MCD(i, m) == 1:
            break

    return i 

def findD(c, m):
    for i in range (1, m):
        if (i*c)%m == 1:
            break

    return i 

def RSAAlgorithm():
    p = 0
    q = 0
    
    while p == q:
        p = primeNumberRdm()
        q = primeNumberRdm()
    

    n = p*q 
    print(f"n > {n}")
    m = mcm(p-1, q-1)
    print(f"m > {m}")
    c = findC(m)
    print(f"c > {c}")
    d = findD(c, m)
    print(f"d > {d}")
    return d, c, n

def encode(message, c, n):
    return ((message**c)%n)

def decode(message, d, n):
    return ((message**d)%n)


d, c, n = RSAAlgorithm()
message = 13
print(f"Messaggio da inviare > {message}")
codified_message = encode(message, c, n)
print(f"Messaggio codificato > {codified_message}")
decodified_message = decode(codified_message, d, n)
print(f"Messaggio decodificato > {decodified_message}")