import sqlite3

from app.domain import Cartoon


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def init_db(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cartoons(
            id TEXT PRIMARY KEY,
            image TEXT NOT NULL,
            title TEXT NOT NULL,
            release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
            country TEXT NOT NULL,
            method_of_creation TEXT NOT NULL,
            director TEXT NOT NULL,
            genres TEXT NOT NULL,
            brief_description TEXT NOT NULL,
            certificate TEXT NOT NULL,
            duration TEXT NOT NULL,
            runtime TEXT NOT NULL,
            tags TEXT NOT NULL
        );
        ''')
        db.commit()


def get_cartoons(db):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, image, title, release_year, country, method_of_creation, director, genres,
        brief_description, certificate, duration, runtime, tags FROM cartoons''')
        items = []
        for row in cursor:
            items.append(
                Cartoon(
                    row['id'],
                    row['image'],
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


def add_cartoon(db, cartoons):
    with db:
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO cartoons(id, image, title, release_year, country, method_of_creation, director, genres, brief_description,
        certificate, duration, runtime, tags) VALUES (:id, :image, :title, :release_year, :country, :method_of_creation, :director,
        :genres, :brief_description, :certificate, :duration, :runtime, :tags)''',
                       {'id': cartoons.id,
                        'image': cartoons.image,
                        'title': cartoons.title,
                        'release_year': cartoons.release_year,
                        'country': cartoons.country,
                        'method_of_creation': cartoons.method_of_creation,
                        'director': cartoons.director,
                        'genres': cartoons.genres,
                        'brief_description': cartoons.brief_description,
                        'certificate': cartoons.certificate,
                        'duration': cartoons.duration,
                        'runtime': cartoons.runtime,
                        'tags': cartoons.tags})
        db.commit()


def get_cartoons_by_id(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('''SELECT id, image, title, release_year, country, method_of_creation, director, genres,
        brief_description, certificate, duration, runtime, tags FROM cartoons WHERE id = :id''', {'id': id})
        for row in cursor:
            return Cartoon(
                row['id'],
                row['image'],
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


def update_cartoon(db, cartoon):
    with db:
        cursor = db.cursor()
        cursor.execute('''UPDATE cartoons SET image = :image, title = :title, release_year = :release_year, country = :country,
        method_of_creation = :method_of_creation, director = :director, genres = :genres,
        brief_description = :brief_description, certificate = :certificate, duration = :duration, runtime = :runtime,
        tags = :tags WHERE id = :id''',
                       {'id': cartoon.id,
                        'image': cartoon.image,
                        'title': cartoon.title,
                        'release_year': cartoon.release_year,
                        'country': cartoon.country,
                        'method_of_creation': cartoon.method_of_creation,
                        'director': cartoon.director,
                        'genres': cartoon.genres,
                        'brief_description': cartoon.brief_description,
                        'certificate': cartoon.certificate,
                        'duration': cartoon.duration,
                        'runtime': cartoon.runtime,
                        'tags': cartoon.tags})
        db.commit()


def remove_cartoon(db, id):
    with db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM cartoons WHERE id = :id', {'id': id})
        db.commit()
