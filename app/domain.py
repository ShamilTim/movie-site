class ShortFilm:
    def __init__(self, id, type, title, release_year, country, brief_description, certificate, runtime):
        self.id = id
        self.type = type
        self.title = title
        self.release_year = release_year
        self.country = country
        self.brief_description = brief_description
        self.certificate = certificate
        self.runtime = runtime


class Film:
    def __init__(self, id, image, title, release_year, country, director, brief_description, certificate, runtime,
                 tags, trailer):
        self.id = id
        self.image = image
        self.title = title
        self.release_year = release_year
        self.country = country
        self.director = director
        self.brief_description = brief_description
        self.certificate = certificate
        self.runtime = runtime
        self.tags = tags
        self.trailer = trailer


class Feature(Film):
    def __init__(self, id, image, title, release_year, country, director, main_roles, genres, box_office,
                 brief_description, certificate, runtime, tags, trailer):
        super().__init__(id, image, title, release_year, country, director, brief_description, certificate,
                         runtime, tags, trailer)
        self.main_roles = main_roles
        self.genres = genres
        self.box_office = box_office


class Documentary(Film):
    def __init__(self, id, image, title, release_year, country, director, category, brief_description, certificate,
                 runtime, tags, trailer):
        super().__init__(id, image, title, release_year, country, director, brief_description, certificate,
                         runtime, tags, trailer)
        self.category = category


class Cartoon(Film):
    def __init__(self, id, image, title, release_year, country, method_of_creation, director, genres,
                 brief_description, certificate, duration, runtime, tags, trailer):
        super().__init__(id, image, title, release_year, country, director, brief_description, certificate,
                         runtime, tags, trailer)
        self.method_of_creation = method_of_creation
        self.genres = genres
        self.duration = duration
