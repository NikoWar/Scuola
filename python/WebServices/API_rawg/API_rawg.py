import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route('/insertRecord', methods=['GET'])
def insertBook():
    if 'title' in request.args and 'author' in request.args and 'published' in request.args:
        title = request.args['title']
        author = request.args['author']
        published = int(request.args['published'])
    else:
        return 'Error: possible missing arguments'
    
    try:
        sqliteConn = sqlite3.connect("db_videogames.db")
        cursor = sqliteConn.cursor()

        cursor.execute(f'INSERT INTO Videogames(slug, name, playtime, released, background_image, rating, rating_top, ratings_count,
                        reviews_text_count, added, suggestions_count, id_videogame, score, reviews_count, saturated_color, dominant_color
                        ) VALUES ("{title}", "{author}", "{published}");')
        sqliteConn.commit()
   
   ''' 
    "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"slug"	TEXT,
	"name"	TEXT,
	"playtime"	INTEGER DEFAULT 0,
	"released"	DATE,
	"background_image"	TEXT,
	"rating"	DECIMAL(1 , 2),
	"rating_top"	DECIMAL(1 , 2),
	"ratings_count"	INTEGER,
	"reviews_text_count"	INTEGER,
	"added"	INTEGER,
	"suggestions_count"	INTEGER,
	"id_videogame"	INTEGER,
	"score"	DECIMAL(1 , 2),
	"reviews_count"	INTEGER,
	"saturated_color"	TEXT,
	"dominant_color"
    '''

    except sqlite3.Error as error:
        print('Error: ' + error)
    finally:
        sqliteConn.close()

    return 'Libro caricato'

if __name__== "__main__":   #chiamata al main "riciclabile" 
    app.run()