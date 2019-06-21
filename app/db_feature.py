import sqlite3

from app.domain import Feature


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def init_db(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS feature_films(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
            country TEXT NOT NULL,
            director TEXT NOT NULL,
            main_roles TEXT NOT NULL,
            genres TEXT NOT NULL,
            box_office INTEGER NOT NULL,
            brief_description TEXT NOT NULL,
            certificate INTEGER NOT NULL CHECK ( certificate >= 0 ) DEFAULT 0,
            runtime TEXT NOT NULL,
            tags TEXT NOT NULL
        );
        ''')
        db.commit()


def get_feature_films(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags FROM feature_films''')
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
                )
            )
        return items


def add_feature(db, feature_films):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO feature_films(title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags) VALUES (:title, :release_year, :country, :director, :main_roles,
        :genres, :box_office, :brief_description, :certificate, :runtime, :tags)''',
                       {'title': feature_films.title,
                        'release_year': feature_films.release_year,
                        'country': feature_films.country,
                        'director': feature_films.director,
                        'main_roles': feature_films.main_roles,
                        'genres': feature_films.genres,
                        'box_office': feature_films.box_office,
                        'brief_description': feature_films.brief_description,
                        'certificate': feature_films.certificate,
                        'runtime': feature_films.runtime,
                        'tags': feature_films.tags})
        db.commit()


def get_feature_by_id(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags FROM feature_films WHERE id = :id''', {'id': id})
        for row in cursor:
            return Feature(
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
            )
