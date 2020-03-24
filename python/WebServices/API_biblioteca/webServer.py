import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(cursor.execute(f"""
    SELECT * 
    FROM Books;
    """))

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []
    results.append(cursor.execute(f"""
    SELECT id 
    FROM Books
    WHERE id == {id};
    """))
    return jsonify(results)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_title():
    if 'title' in request.args:
        title = request.args
    else:
        return "Error: No title field provided. Please specify a title."
    
    results = []

    results.append(cursor.execute(f"""
    SELECT title 
    FROM Books
    WHERE title == {title};
    """))
    return jsonify(results)

if __name__== "__main__":   #chiamata al main "riciclabile" 
    sqliteConnection = sqlite3.connect('dbBooks.db')
    cursor = sqliteConnection.cursor()
    app.run()


    '''
        HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 245
        Server: Werkzeug/0.16.1 Python/3.8.1
        Date: Tue, 03 Mar 2020 10:26:53 GMT

        Host: 127.0.0.1:5000
        User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        Cache-Control: max-age=0

        QUERY ESEMPIO
        HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 87
        Server: Werkzeug/0.16.1 Python/3.8.1
        Date: Tue, 03 Mar 2020 10:28:10 GMT

        Host: 127.0.0.1:5000
        User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        Cache-Control: max-age=0

        QUERY MODIFICATA
    '''