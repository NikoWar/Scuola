import flask
import requests
import sqlite3

URL = 'https://api.rawg.io/api/games?dates=2001-01-01,2001-12-31&ordering=-rating'

def getData(URL):
    raw_data = requests.get(url=URL)
    print(raw_data)

    data = raw_data.json()
    insertVideoGames(data)

def insertVideoGames(data):
    try:
        sqlConn = sqlite3.connect('db_videogames.db')
        cursor = sqlConn.cursor()

        for d in data['results']:
            cursor.execute(f'''INSERT INTO Videogames 
                            (slug, name, playtime, released, background_image, rating, rating_top, ratings_count,
                            reviews_text_count, added, suggestions_count, id_videogame, score, reviews_count, saturated_color, dominant_color
                        ) VALUES 
                            ("{d['slug']}", 
                            "{d['name']}", 
                            "{d['playtime']}", 
                            "{d['released']}", 
                            "{d['background_image']}", 
                            "{d['rating']}",
                            "{d['rating_top']}", 
                            "{d['ratings_count']}", 
                            "{d['reviews_text_count']}", 
                            "{d['added']}", 
                            "{d['suggestions_count']}", 
                            "{str(d['id'])}", 
                            "{d['score']}", 
                            "{d['reviews_count']}", 
                            "{d['saturated_color']}", 
                            "{d['dominant_color']}");''')
            sqlConn.commit()

    except sqlite3.Error as error:
        print('Error: ' + str(error))
    finally:
        sqlConn.close()

    return 'Libro caricato'
getData(URL)
'''
def insertBook():

        cursor.execute(f'INSERT INTO Videogames(slug, name, playtime, released, background_image, rating, rating_top, ratings_count,
                        reviews_text_count, added, suggestions_count, id_videogame, score, reviews_count, saturated_color, dominant_color
                        ) VALUES ("{title}", "{author}", "{published}");')
        sqliteConn.commit()
   

    "id"	
	"slug"	
	"name"	
	"playtime"	
	"released"	
	"background_image"	
	"rating"	
	"rating_top"	
	"ratings_count"	
	"reviews_text_count"	
	"added"	
	"suggestions_count"	
	"id_videogame"	
	"score"	
	"reviews_count"	
	"saturated_color"	
	"dominant_color"

    except sqlite3.Error as error:
        print('Error: ' + error)
    finally:
        sqliteConn.close()

    return 'Libro caricato'

if __name__== "__main__":   #chiamata al main "riciclabile" 
    app.run()
'''