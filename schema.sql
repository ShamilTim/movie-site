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

CREATE TABLE IF NOT EXISTS documentary_films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
    country TEXT NOT NULL,
    director TEXT NOT NULL,
    category TEXT NOT NULL,
    brief_description TEXT NOT NULL,
    certificate INTEGER NOT NULL CHECK ( certificate >= 0 ) DEFAULT 0,
    runtime TEXT NOT NULL,
    tags TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cartoons(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
    country TEXT NOT NULL,
    method_of_creation TEXT NOT NULL,
    director TEXT NOT NULL,
    genres TEXT NOT NULL,
    brief_description TEXT NOT NULL,
    certificate INTEGER NOT NULL CHECK ( certificate >= 0 ) DEFAULT 0,
    duration TEXT NOT NULL,
    runtime TEXT NOT NULL,
    tags TEXT NOT NULL
);

CREATE TABLE films(
    film_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER NOT NULL CHECK ( release_year > 1894 AND release_year < 2025 ),
    country TEXT NOT NULL,
    director TEXT NOT NULL,
    brief_description TEXT NOT NULL,
    certificate INTEGER NOT NULL CHECK ( certificate >= 0 ) DEFAULT 0,
    runtime TEXT NOT NULL,
    tags TEXT NOT NULL
);

CREATE VIEW films
AS SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
FROM feature_films
UNION
SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
FROM documentary_films
UNION
SELECT id, title, release_year, country, director, brief_description, certificate, runtime, tags
FROM cartoons;

DROP VIEW films;

DROP TABLE feature_films;
DROP TABLE documentary_films;
DROP TABLE cartoons;

SELECT * FROM feature_films;
SELECT * FROM films;