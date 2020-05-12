import flask
from flask import request, jsonify
import sqlite3
from datetime import datetime
import threading

app = flask.Flask(__name__)
path_db = 'static/db_chat.db'

@app.route('/api/v1/receive', methods=['GET'])
def messageForMe():
    if 'id_dest' in request.args:
        dest = int(request.args['id_dest'])
    try:
        sqliteConn = sqlite3.connect(path_db)
        cursor = sqliteConn.cursor()

        cursor.execute(f'''SELECT user_id
                            FROM utenti
                            WHERE user_id = {dest};''')

        user = cursor.fetchall()

        if (len(user)==1):
            cursor.execute(f"""SELECT sender_id, text, timestamp
                            FROM messaggi
                            WHERE received = 0 AND receiver_id={dest};""")
            res = cursor.fetchall()
            
            cursor.execute(f'''UPDATE messaggi 
                               SET received = 1 
                               WHERE timestamp < datetime('now') and receiver_id = {i[2]}''')

            sqliteConn.commit()

            if(len(res)==0):
                return 'No message for you :('
        else:
            return 'Invalid user id'

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (sqliteConn):
            print('Chiusura connessione DB')
            sqliteConn.close()
            return jsonify(res)

@app.route('/', methods=['GET'])
def home():
    return "<h1>CHAT</h1><p>Prototipo di chat con Flask.</p>"


@app.route('/api/v1/user_list', methods=['GET'])
def api_all():
    try:
        sqliteConn = sqlite3.connect(path_db)
        cursor = sqliteConn.cursor()

        cursor.execute("SELECT * FROM utenti")
        user = cursor.fetchall()

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (sqliteConn):
            print('chiusura connessione DB')
            sqliteConn.close()
            return jsonify(user)

@app.route('/api/v1/send', methods=['GET'])
def api_title():
    if 'id_dest' in request.args and 'text' in request.args and 'id_mitt' in request.args:
        dest = int(request.args['id_dest'])
        text = request.args['text']
        mitt = int(request.args['id_mitt'])
    else:
        return 'Error: possible missing arguments'
    
    try:
        sqliteConn = sqlite3.connect(path_db)
        cursor = sqliteConn.cursor()
        
        cursor.execute(f'''SELECT user_id
                            FROM utenti
                            WHERE user_id = {dest} or user_id = {mitt};''')

        user = cursor.fetchall()

        if (len(user)>1):
            date = datetime.now() 
            time = date.strftime("%H:%M:%S")

            len_text = len(text)

            cursor.execute(f'''
                INSERT INTO messaggi(receiver_id, sender_id, timestamp, text, length, received) 
                VALUES ({dest}, {mitt}, "{text}", "{time}", {len_text}, {False});''')

            sqliteConn.commit()
        else:
            return 'Invalid user'

    except sqlite3.Error as error:
        print('Error: ' + error)
    
    finally:
        if (sqliteConn):
            sqliteConn.close()
            return 'Message sent in the correct way'

if __name__== "__main__":   #chiamata al main "riciclabile" 
    app.run(host="192.168.1.140", port=int(8080), debug=True)