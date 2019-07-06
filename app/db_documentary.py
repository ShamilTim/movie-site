import sqlite3

from app.domain import Documentary


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def init_db(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS feature_films(
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
            country TEXT NOT NULL,
            director TEXT NOT NULL,
            category TEXT NOT NULL,
            brief_description TEXT NOT NULL,
            certificate TEXT NOT NULL,
            runtime TEXT NOT NULL,
            tags TEXT NOT NULL
        );
        ''')
        db.commit()


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


def add_documentary(db, documentary_films):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO documentary_films(id, title, release_year, country, director, category, brief_description, certificate,
        runtime, tags) VALUES (:id, :title, :release_year, :country, :director, :category, :brief_description, :certificate,
        :runtime, :tags)''',
                       {'id': documentary_films.id,
                        'title': documentary_films.title,
                        'release_year': documentary_films.release_year,
                        'country': documentary_films.country,
                        'director': documentary_films.director,
                        'category': documentary_films.category,
                        'brief_description': documentary_films.brief_description,
                        'certificate': documentary_films.certificate,
                        'runtime': documentary_films.runtime,
                        'tags': documentary_films.tags})
        db.commit()


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


def update_documentary(db, documentary_film):
    with db:
        cursor = db.cursor()
        cursor.execute('''UPDATE documentary_films SET title = :title, release_year = :release_year, country = :country,
        director = :director, category = :category, brief_description = :brief_description, certificate = :certificate,
        runtime = :runtime, tags = :tags WHERE id = :id''',
        {'id': documentary_film.id, 'title': documentary_film.title, 'release_year': documentary_film.release_year,
         'country': documentary_film.country, 'director': documentary_film.director,
         'category': documentary_film.category, 'brief_description': documentary_film.brief_description,
         'certificate': documentary_film.certificate, 'runtime': documentary_film.runtime,
         'tags': documentary_film.tags})
        db.commit()


def remove_documentary(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM documentary_films WHERE id = :id', {'id': id})
        db.commit()
