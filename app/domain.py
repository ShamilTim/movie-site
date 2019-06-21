class Film:
    def __init__(self, id, title, release_year, country, director, brief_description, certificate, runtime, tags):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.country = country
        self.director = director
        self.brief_description = brief_description
        self.certificate = certificate
        self.runtime = runtime
        self.tags = tags


class Feature(Film):
    def __init__(self, id, title, release_year, country, director, main_roles, genres, box_office, brief_description,
                 certificate, runtime, tags):
        super().__init__(id, title, release_year, country, director, brief_description, certificate, runtime, tags)
        self.main_roles = main_roles
        self.genres = genres
        self.box_office = box_office


class Documentary(Film):
    def __init__(self, id, title, release_year, country, director, category, brief_description, certificate, runtime, tags):
        super().__init__(id, title, release_year, country, director, brief_description, certificate, runtime, tags)
        self.category = category


class Cartoon(Film):
    def __init__(self, id, title, release_year, country, method_of_creation, director, genres, brief_description,
                 certificate, duration, runtime, tags):
        super().__init__(id, title, release_year, country, director, brief_description, certificate, runtime, tags)
        self.method_of_creation = method_of_creation
        self.genres = genres
        self.duration = duration
