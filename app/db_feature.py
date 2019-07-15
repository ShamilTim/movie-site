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
            id TEXT PRIMARY KEY,
            image TEXT NOT NULL,
            title TEXT NOT NULL,
            release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
            country TEXT NOT NULL,
            director TEXT NOT NULL,
            main_roles TEXT NOT NULL,
            genres TEXT NOT NULL,
            box_office INTEGER NOT NULL,
            brief_description TEXT NOT NULL,
            certificate TEXT NOT NULL,
            runtime TEXT NOT NULL,
            tags TEXT NOT NULL,
            trailer TEXT NOT NULL 
        );
        ''')
        db.commit()


def get_feature_films(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, image, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags, trailer FROM feature_films''')
        items = []
        for row in cursor:
            items.append(
                Feature(
                    row['id'],
                    row['image'],
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
                    row['tags'],
                    row['trailer']
                )
            )
        return items


def add_feature(db, feature_films):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO feature_films(id, image, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags, trailer) VALUES (:id, :image, :title, :release_year, :country, :director,
         :main_roles, :genres, :box_office, :brief_description, :certificate, :runtime, :tags, :trailer)''',
                       {'id': feature_films.id,
                        'image': feature_films.image,
                        'title': feature_films.title,
                        'release_year': feature_films.release_year,
                        'country': feature_films.country,
                        'director': feature_films.director,
                        'main_roles': feature_films.main_roles,
                        'genres': feature_films.genres,
                        'box_office': feature_films.box_office,
                        'brief_description': feature_films.brief_description,
                        'certificate': feature_films.certificate,
                        'runtime': feature_films.runtime,
                        'tags': feature_films.tags,
                        'trailer': feature_films.trailer})
        db.commit()


def get_feature_by_id(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, image, title, release_year, country, director, main_roles, genres, box_office,
        brief_description, certificate, runtime, tags, trailer FROM feature_films WHERE id = :id''', {'id': id})
        for row in cursor:
            return Feature(
                row['id'],
                row['image'],
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
                row['tags'],
                row['trailer']
            )


def update_feature(db, feature_film):
    with db:
        cursor = db.cursor()
        cursor.execute('''UPDATE feature_films SET image = :image, title = :title, release_year = :release_year,
        country = :country, director = :director, main_roles = :main_roles, genres = :genres, box_office = :box_office,
        brief_description = :brief_description, certificate = :certificate, runtime = :runtime, tags = :tags,
        trailer = :trailer
        WHERE id = :id''', {'id': feature_film.id,
                            'image': feature_film.image,
                            'title': feature_film.title,
                            'release_year': feature_film.release_year,
                            'country': feature_film.country,
                            'director': feature_film.director,
                            'main_roles': feature_film.main_roles,
                            'genres': feature_film.genres,
                            'box_office': feature_film.box_office,
                            'brief_description': feature_film.brief_description,
                            'certificate': feature_film.certificate,
                            'runtime': feature_film.runtime,
                            'tags': feature_film.tags,
                            'trailer': feature_film.trailer})
        db.commit()


def remove_feature(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM feature_films WHERE id = :id', {'id': id})
        db.commit()
