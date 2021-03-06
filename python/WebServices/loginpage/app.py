'''
    GUERRA NICOLO' 5AROB
'''

from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import hashlib

app = Flask(__name__)

def getHash(s):
    m = hashlib.sha256()
    m.update(s)
    return m.hexdigest()

def check_password(hashed_password, user_password):   #controllo password input hashata e password hashata sul db
    return hashed_password == getHash(user_password)

def validate(username, password):
    with sqlite3.connect('static/db.db') as con:    #mantiene in memoria quest'oggetto solo durante il tempo strettamente necessario a compiere tutte le operazioni sull'oggetto
        cur = con.cursor()                          #creo il cursore per navigareil db
        cur.execute("SELECT * FROM Users")          #istruzione SQL
        rows = cur.fetchall()                       #esecuzione query
        for row in rows:
            dbUser = row[0]                         #riga 0 contiene l'username
            dbPass = row[1]                         #riga 1 contiene la password
            if dbUser == username:           
                return check_password(dbPass, password)   #True/False        

def insertDB(username, password):
    with sqlite3.connect('./static/db.db') as con:
        cur = con.cursor()
        try:
            cur.execute(f'INSERT INTO USERS (USERNAME, PASSWORD) VALUES ("{username}", "{password}")')  #insert sql
        except Exception:
            pass

@app.route('/', methods=['GET', 'POST'])
def signInOrSignUp():
    error = None
    if request.method == 'POST':                        #si usa il metodo POST
        if request.form['submit_button'] == 'Log-In':   #if annidate per determinare su quale pagina venire reinderizzati
            return redirect(url_for('login'))           
        elif request.form['submit_button'] == 'Sign-Up':
            return redirect(url_for('register'))
        else:
            pass # unknown
        
    return render_template('index.html', error = error) #ritorna il template della pagina HTML (posizione e errori)


@app.route('/login', methods=['GET', 'POST'])    #lo '/' indica che si trova nella prima pagina
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']      
        password = request.form['password']                 
        if validate(username, password) == False:
            error = 'Invalid Credentials. Please try again.'    #credenziali sbagliate
        else:
            return redirect(url_for('secret'))

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        insertDB(username, password)            #inserisco credenziali nel db

    return render_template('register.html', error=error)

@app.route('/secret')
def secret():
    return "This is a secret page!"

if __name__== "__main__":   #chiamata al main "riciclabile" 
    app.run()