import sqlite3

from app.domain import Film, Feature, Documentary, Cartoon


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def get_films(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        SELECT id, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags
        FROM feature_films;
        ''')
        items = []
        for row in cursor:
            items.append(
                Feature(
                    row['id'],
                    row['title'],
                    row['release_year'],
                    row['country'],
                    row['director'],
                    row['main_roles'],
                    row['genres'],
                    row['box_office'],
                    row['brief_description'],
                    row['certificate'],
                    row['runtime'],
                    row['tags']
                ))
        cursor.execute('''
        SELECT id, title, release_year, country, director, category, brief_description, certificate, runtime, tags
        FROM documentary_films;
        ''')
        for row in cursor:
            items.append(
                Documentary(
                    row['id'],
                    row['title'],
                    row['release_year'],
                    row['country'],
                    row['director'],
                    row['category'],
                    row['brief_description'],
                    row['certificate'],
                    row['runtime'],
                    row['tags']
                ))
        cursor.execute('''
        SELECT id, title, release_year, country, method_of_creation, director, genres, brief_description, certificate, 
        duration, runtime, tags
        FROM cartoons;''')
        for row in cursor:
            items.append(
                Cartoon(
                    row['id'],
                    row['title'],
                    row['release_year'],
                    row['country'],
                    row['method_of_creation'],
                    row['director'],
                    row['genres'],
                    row['brief_description'],
                    row['certificate'],
                    row['duration'],
                    row['runtime'],
                    row['tags']
                )
            )
        return items


def search_films_by_title(db, title):
    with db:
        cursor = db.cursor()
        rows = cursor.execute('''
        SELECT id, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags
        FROM feature_films
        WHERE title LIKE title = :title''', {'title': title})
        for row in rows:
            print(row)
            type(row)
            return row

# def search_films_by_title(films, title):
#     result = []
#     for film in films:
#         if film['title'] == title:
#             result.append(film)
#             print(film)
#     print(result)
#     return result
