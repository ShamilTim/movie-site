import sqlite3

from app.domain import Film


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def get_films(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
        FROM feature_films
        UNION
        SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
        FROM documentary_films
        UNION
        SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
        FROM cartoons;
          ''')
        items = []
        for row in cursor:
            items.append(
                Film(
                    row['id'],
                    row['title'],
                    row['release_year'],
                    row['country'],
                    row['director'],
                    row['brief_description'],
                    row['certificate'],
                    row['runtime'],
                    row['tags']
                )
            )
        return items


def get_film_by_id(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
        FROM feature_films
        UNION
        SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags 
        FROM documentary_films
        UNION
        SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
        FROM cartoons
        WHERE id = :id''', {'id': id})
        for row in cursor:
            return Film(
                row['id'],
                row['title'],
                row['release_year'],
                row['country'],
                row['director'],
                row['brief_description'],
                row['certificate'],
                row['runtime'],
                row['tags']
            )


def remove(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM films WHERE id = :id', {'id': id})
        db.commit()


# def verify_id_feature(db, id):
#    with db:
#        cursor = db.cursor()
#        cursor.execute('SELECT id FROM feature_films WHERE id = :id LIMIT 1', {'id': id})
#        row = cursor.fetchone()
#        print(row)
#        return row


# def verify_id_documentary(db, id):
#    with db:
#        cursor = db.cursor()
#        cursor.execute('SELECT id FROM documentary_films WHERE id = :id LIMIT 1', {'id': id})
#        row = cursor.fetchone()
#        return row


# def verify_id_cartoon(db, id):
#    with db:
#        cursor = db.cursor()
#        cursor.execute('SELECT id FROM cartoons WHERE id = :id LIMIT 1', {'id': id})
#        row = cursor.fetchone()
#        return row
