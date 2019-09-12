import socket as sck

HOST = "127.0.0.1"    
PORT = 1984

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)  #AF_INET si potrebbe usare ipv6, SOCK_DGRAM si usa UDP
s.bind((HOST, PORT))    #lega il processo ad una porta e un indirizzo

while True:
    data, addr = s.recvfrom(4096)   #4096 grandezza del buffer di ricezione
    print("ricevuto: "+data.decode()+"\n"+"da: "+str(addr))
    
    s.sendto(data, addr)

    if(data.decode()=="stop"):
        break

s.close()

'''
    BERKLEY
    socket()    NON BLOCCANTE   S-C
    bind()      BLOCCANTE       S
    recvfrom()  NON BLOCCANTE   S-C
    sendto()    NON BLOCCANTE   S-C
    close()     NON BLOCCANTE   S-C
'''
