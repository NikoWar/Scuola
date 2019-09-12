import socket as sck

SERVER = "192.168.10.76"
PORT = 4242

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
    testo = input()
    if(testo == "stop"):
        break

    s.sendto(testo.encode(), (SERVER, PORT))

    data, addr = s.recvfrom(4096)
    print(data.decode())

s.close()