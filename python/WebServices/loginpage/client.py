import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

URL = "http://127.0.0.1:5000/register"  #url standard
IP_SERVER = "127.0.0.1"                 #ip server
PORT = 5000                             #processo

s.connect((IP_SERVER, PORT))
strToSend=""

username = "Niko"                      #credenziali per loggare
password = "ciao"

method = "GET" #/POST

#formulazione richiesta
request_type = f"{method} {URL} HTTP/1.0"
body_entity = f"username={username}&password={password}"
headers = f'Content-Type: application/x-www-form-urlencoded\nContent-Length: {len(body_entity)}'

request = f"{request_type}\n{headers}\n\n{body_entity}"

s.send(request_type.encode())
data = None
code = []
html_code = []

while data !='':
    data = s.recv(4096).decode()
    code.append(data)
    print("Server: %s" % data)

html_code = code[-2]    #prende la penultima istanza del vettore contenente stringhe e codice
html_code = html_code[html_code.find("<html>"):]    #carico tutte le informazioni a partire da "<html>"

out_file = open('register.html', 'w')
out_file.write(html_code)   #scrivo su file il codice html
out_file.close()

s.close()