import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

URL = "http://127.0.0.1:5000/register"
IP_SERVER = "127.0.0.1"
PORT = 5000

s.connect((IP_SERVER, PORT))
strToSend=""

username = "Giruz"
password = "1234"

method = "GET" #/POST

request_type = f"{method} {URL} HTTP/1.0\n\n"
headers = ''
body_entity = f"username={username}&password={password}"

request = f"{request_type}\n{headers}\n\n{body_entity}"

s.send(request_type.encode())
data = None
code = []
html_code = []
while data !='':
    data = s.recv(4096).decode()
    code.append(data)
    print("Server: %s" % data)

html_code = code[-2]
html_code = [html_code.find("<html>"):]

with open("body.html", 'w', encoding='utf-8') as f:
    
    f.write(code)

s.close()