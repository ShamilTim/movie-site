import sqlite3

from app.domain import Documentary


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def get_documentary_films(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, title, release_year, country, director, category, brief_description, certificate, 
        runtime, tags FROM documentary_films''')
        items = []
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
                )
            )
        return items


def get_documentary_by_id(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, title, release_year, country, director, category, brief_description, certificate,
        runtime, tags FROM documentary_films WHERE id = :id''', {'id': id})
        for row in cursor:
            return Documentary(
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
            )
