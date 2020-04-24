import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"


@app.route('/allBooks', methods=['GET'])
def api_all():
    try:
        sqliteConn = sqlite3.connect('dbBooks.db')
        cursor = sqliteConn.cursor()

        cursor.execute("SELECT * FROM Books")
        allBooks = cursor.fetchall()

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (sqliteConn):
            print('chiusura connessione DB')
            sqliteConn.close()
    
    return jsonify(allBooks)

@app.route('/booksById', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    try:
        sqliteConn = sqlite3.connect("dbBooks.db")
        cursor = sqliteConn.cursor()

        cursor.execute(f"""
        SELECT title, author, published
        FROM Books
        WHERE id == {id};
        """)

        results = cursor.fetchall()
    except sqlite3.Error as error:
        print('Error: ' + error)
    
    finally:
        if (sqliteConn):
            print('chiusura connessione DB')
            sqliteConn.close()
    
    return jsonify(results)

@app.route('/booksByTitle', methods=['GET'])
def api_title():
    if 'title' in request.args:
        title = request.args['title']
    else:
        return "Error: No title field provided. Please specify a title."
    
    try:
        sqliteConn = sqlite3.connect("dbBooks.db")
        cursor = sqliteConn.cursor()

        cursor.execute(f"""
        SELECT title, author, published
        FROM Books
        WHERE title == {title};
        """)

        results = cursor.fetchall()
    except sqlite3.Error as error:
        print('Error: ' + error)
    
    finally:
        if (sqliteConn):
            sqliteConn.close()
    
    return jsonify(results)

@app.route('/insertBook', methods=['GET'])
def insertBook():
    if 'title' in request.args and 'author' in request.args and 'published' in request.args:
        title = request.args['title']
        author = request.args['author']
        published = int(request.args['published'])
    else:
        return 'Error: possible missing arguments'
    
    try:
        sqliteConn = sqlite3.connect("dbBooks.db")
        cursor = sqliteConn.cursor()

        cursor.execute(f'INSERT INTO Books(title, author, published) VALUES ("{title}", "{author}", "{published}");')
        sqliteConn.commit()
    except sqlite3.Error as error:
        print('Error: ' + error)
    finally:
        sqliteConn.close()

    return 'Libro caricato'

if __name__== "__main__":   #chiamata al main "riciclabile" 
    app.run()
