import sqlite3

from app.domain import Cartoon


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def get_cartoons(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, title, release_year, country, method_of_creation, director, genres,
        brief_description, certificate, duration, runtime, tags FROM cartoons''')
        items = []
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


def get_cartoons_by_id(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, title, release_year, country, method_of_creation, director, genres,
        brief_description, certificate, duration, runtime, tags FROM cartoons''')
        for row in cursor:
            return Cartoon(
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


def remove(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''DELETE FROM cartoons WHERE id = :id''', {'id': id})
        db.commit()
