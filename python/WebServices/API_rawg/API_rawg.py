import flask
import requests
import sqlite3
from PIL import Image
from io import BytesIO

URL = 'https://api.rawg.io/api/games?dates=2001-01-01,2001-12-31&ordering=-rating'

def getData(URL):
    raw_data = requests.get(url=URL)
    print(raw_data)

    data = raw_data.json()
    insertVideoGames(data)

def insertVideoGames(data):
    try:
        sqlConn = sqlite3.connect('./db_videogames.db')
        cursor = sqlConn.cursor()
        
        for d in data['results']:
            if(d['background_image'] != None):
                response = requests.get(url= d['background_image'])
                img = Image.open(BytesIO(response.content))
            
            cursor.execute(f'''INSERT INTO Videogames 
                            (slug, name, playtime, released, background_image, image, rating, rating_top, ratings_count,
                            reviews_text_count, added, suggestions_count, id_videogame, score, reviews_count, saturated_color, dominant_color
                        ) VALUES 
                            ("{d['slug']}", 
                            "{d['name']}", 
                            "{d['playtime']}", 
                            "{d['released']}", 
                            "{d['background_image']}",
                            "{img}",  
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
        print('DB caricato')

def isLoad():
    res = []
    try:
        sqlConn = sqlite3.connect('./db_videogames')
        cursor = sqlConn.cursor()
            
        cursor.execute(f'''SELECT * FROM Videogames;''')
        res = cursor.fetchall()
              
    except sqlite3.Error as error:
        print('Error: ' + str(error))
    finally:
        sqlConn.close()

    return (len(res) == 0)

def printer(array, switch):
    if (switch == 'CLASSIFICA'):
        for n, a in enumerate(array):
            print(f'POSIZIONE {n+1}: {a[0]}, VOTO: {a[1]}')
    else:
        for a in enumerate(array):
            print(f'DATA DI RILASCIO  {a[1][1]}, NOME GIOCO: {a[1][0]}')

if(not isLoad()):
    print('DB già caricato')
    
    while True:
        scelta = int(input('0-> ESCI \n1->CLASSIFICA IN BASE AL VOTO\n2->IN ORDINE DI DATA DI USCITA CRESCENTE\n ------->'))
        if (scelta == 0):
            break
        if (scelta == 1):
            try:
                sqlConn = sqlite3.connect('./db_videogames')
                cursor = sqlConn.cursor()
                    
                cursor.execute(f'''SELECT name, rating FROM Videogames ORDER BY rating DESC;''')
                res = cursor.fetchall()
                printer(res, 'CLASSIFICA')

            except sqlite3.Error as error:
                print('Error: ' + str(error))
            finally:
                sqlConn.close()
        if (scelta == 2):
            try:
                sqlConn = sqlite3.connect('./db_videogames')
                cursor = sqlConn.cursor()
                    
                cursor.execute(f'''SELECT name, released FROM Videogames ORDER BY released ASC;''')
                res = cursor.fetchall()
                printer(res, 'DATA')

            except sqlite3.Error as error:
                print('Error: ' + str(error))
            finally:
                sqlConn.close()
else:
    getData(URL)