import socket as sck

HOST = "192.168.10.56"
PORT = 50002

c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
c.connect((HOST, PORT))

while True:
    text = input()
    if text == "e":
        break
    c.sendall(text.encode())
    data=c.recv(4096)
    stringaCoord = data.decode()
    stringaCoord = str(stringaCoord)
    _, coordX, coordY = stringaCoord.split(" ")
    coordX = coordX[0:-1]
    coordX = float(coordX)
    coordY = float(coordY)
    print(coordX, coordY)
    
c.close()