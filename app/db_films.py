import sqlite3

from app.domain import ShortFilm


def open_db(url):
    db = sqlite3.connect(url)
    db.row_factory = sqlite3.Row
    return db


def get_films(db):
    with db:
        items = []
        cursor = db.cursor()
        cursor.execute('''
        SELECT id, title, 'FEATURE' type, release_year, country, brief_description, certificate, runtime
        FROM feature_films
        UNION
        SELECT id, title, 'DOCUMENTARY' type, release_year, country, brief_description, certificate, runtime
        FROM documentary_films
        UNION
        SELECT id, title, 'CARTOON' type, release_year, country, brief_description, certificate, runtime
        FROM cartoons
        ''')
        for row in cursor:
            items.append(
                ShortFilm(
                    row['id'],
                    row['type'],
                    row['title'],
                    row['release_year'],
                    row['country'],
                    row['brief_description'],
                    row['certificate'],
                    row['runtime']
                )
            )
        return items


def search_films_by_title(db, search):
    with db:
        items = []
        cursor = db.cursor()
        cursor.execute('''
        SELECT id, title, 'FEATURE' type, release_year, country, brief_description, certificate, runtime
        FROM feature_films
        WHERE title LIKE :search OR release_year LIKE :search OR country LIKE :search OR director LIKE :search
        OR main_roles LIKE :search OR genres LIKE :search OR certificate LIKE :search OR tags LIKE :search
        UNION
        SELECT id, title, 'DOCUMENTARY' type, release_year, country, brief_description, certificate, runtime
        FROM documentary_films
        WHERE title LIKE :search OR release_year LIKE :search OR country LIKE :search OR director LIKE :search
        OR category LIKE :search OR certificate LIKE :search OR tags LIKE :search
        UNION
        SELECT id, title, 'CARTOON' type, release_year, country, brief_description, certificate, runtime
        FROM cartoons
        WHERE title LIKE :search OR release_year LIKE :search OR country LIKE :search OR method_of_creation LIKE :search
        OR director LIKE :search OR genres LIKE :search OR certificate LIKE :search OR duration LIKE :search
        OR tags LIKE :search
        ''', {'search': '%' + search + '%'})
        for row in cursor:
            items.append(
                ShortFilm(
                    row['id'],
                    row['type'],
                    row['title'],
                    row['release_year'],
                    row['country'],
                    row['brief_description'],
                    row['certificate'],
                    row['runtime']
                )
            )
        return items
