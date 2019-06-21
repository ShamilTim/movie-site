import os

import waitress
from flask import Flask, render_template, request, redirect, url_for

from app import db_feature, db_films, db_documentary, db_cartoons
from app.domain import Feature


def start():
    app = Flask(__name__)
    db_url = 'db.sqlite'

    @app.route("/", methods=['GET'])
    def index():
        films = db_films.get_films(db_films.open_db(db_url))
        return render_template('index.html', films=films)

    @app.route("/index_feature", methods=['GET'])
    def index_feature():
        feature_films = db_feature.get_feature_films(db_feature.open_db(db_url))
        return render_template('index_feature.html', feature_films=feature_films)

    @app.route("/index_documentary", methods=['GET'])
    def index_documentary():
        documentary_films = db_documentary.get_documentary_films(db_documentary.open_db(db_url))
        return render_template('index_documentary.html', documentary_films=documentary_films)

    @app.route("/index_cartoons", methods=['GET'])
    def index_cartoons():
        cartoons = db_cartoons.get_cartoons(db_cartoons.open_db(db_url))
        return render_template('index_cartoons.html', cartoons=cartoons)

    @app.route('/add_feature', methods=['GET'])
    def add_feature_form():
        return render_template('add_feature.html')

    @app.route('/add_feature', methods=['POST'])
    def add_feature():
        title = request.form['title']
        release_year = int(request.form['release_year'])
        country = request.form['country']
        director = request.form['director']
        main_roles = request.form['main_roles']
        genres = request.form['genres']
        box_office = int(request.form['box_office'])
        brief_description = request.form['brief_description']
        certificate = int(request.form['certificate'])
        runtime = request.form['runtime']
        tags = request.form['tags']
        feature_film = Feature(0, title, release_year, country, director, main_roles, genres, box_office,
                               brief_description, certificate, runtime, tags)
        db_feature.add_feature(db_feature.open_db(db_url), feature_film)
        return redirect(url_for('index'))

    @app.route("/details_feature/<id>", methods=['GET'])
    def details_feature_by_id(id):
        feature_film = db_feature.get_feature_by_id(db_feature.open_db(db_url), id)
        return render_template('details_feature.html', feature_film=feature_film)

    @app.route("/details_documentary/<id>", methods=['GET'])
    def details_documentary_by_id(id):
        documentary_film = db_documentary.get_documentary_by_id(db_documentary.open_db(db_url), id)
        return render_template('details_documentary.html', documentary_film=documentary_film)

    @app.route("/details_cartoons/<id>", methods=['GET'])
    def details_cartoon_by_id(id):
        cartoon = db_cartoons.get_cartoons_by_id(db_cartoons.open_db(db_url), id)
        return render_template('details_cartoons.html', cartoon=cartoon)

    @app.route("/remove/<id>", methods=['GET'])
    def remove_form(id):
        film = db_films.get_film_by_id(db_films.open_db(db_url), id)
        return render_template('remove.html', film=film)

    @app.route("/remove/<id>", methods=['POST'])
    def remove(id):
        db_films.remove(db_films.open_db(db_url), id)
        return redirect(url_for('index'))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(debug=True)


if __name__ == '__main__':
    start()
