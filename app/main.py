import csv
import io
import os
import uuid

import waitress
from flask import Flask, render_template, request, redirect, url_for, make_response

from app import db_feature, db_films, db_documentary, db_cartoons
from app.domain import Feature, Documentary, Cartoon


def start():
    app = Flask(__name__)
    db_url = 'db.sqlite'

    @app.route("/", methods=['GET'])
    def index():
        films = db_films.get_films(db_films.open_db(db_url))
        search = request.args.get('search')
        if search:
            results = db_films.search_films_by_title(db_films.open_db(db_url), search)
            return render_template('index.html', films=results, search=search)
        return render_template('index.html', films=films)

    @app.template_filter('film_sublink')
    def film_sublink_filter(film):
        if film.type == 'FEATURE':
            return '/details_feature'

        if film.type == 'DOCUMENTARY':
            return '/details_documentary'

        if film.type == 'CARTOON':
            return '/details_cartoons'

        raise TypeError('Invalid film type')

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
        certificate = request.form['certificate']
        runtime = request.form['runtime']
        tags = request.form['tags']
        id = str(uuid.uuid4())
        feature_film = Feature(id, title, release_year, country, director, main_roles, genres, box_office,
                               brief_description, certificate, runtime, tags)
        db_feature.add_feature(db_feature.open_db(db_url), feature_film)
        return redirect(url_for('index_feature'))

    @app.route('/add_documentary', methods=['GET'])
    def add_documentary_form():
        return render_template('add_documentary.html')

    @app.route('/add_documentary', methods=['POST'])
    def add_documentary():
        title = request.form['title']
        release_year = int(request.form['release_year'])
        country = request.form['country']
        director = request.form['director']
        category = request.form['category']
        brief_description = request.form['brief_description']
        certificate = request.form['certificate']
        runtime = request.form['runtime']
        tags = request.form['tags']
        uuid_id = str(uuid.uuid4())
        documentary_film = Documentary(uuid_id, title, release_year, country, director, category, brief_description,
                                       certificate, runtime, tags)
        db_documentary.add_documentary(db_documentary.open_db(db_url), documentary_film)
        return redirect(url_for('index_documentary'))

    @app.route('/add_cartoon', methods=['GET'])
    def add_cartoon_form():
        return render_template('add_cartoon.html')

    @app.route('/add_cartoon', methods=['POST'])
    def add_cartoon():
        title = request.form['title']
        release_year = int(request.form['release_year'])
        country = request.form['country']
        method_of_creation = request.form['method_of_creation']
        director = request.form['director']
        genres = request.form['genres']
        brief_description = request.form['brief_description']
        certificate = request.form['certificate']
        duration = request.form['duration']
        runtime = request.form['runtime']
        tags = request.form['tags']
        uuid_id = str(uuid.uuid4())
        cartoon = Cartoon(uuid_id, title, release_year, country, method_of_creation, director, genres, brief_description,
                          certificate, duration, runtime, tags)
        db_cartoons.add_cartoon(db_cartoons.open_db(db_url), cartoon)
        return redirect(url_for('index_cartoons'))

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

    @app.route("/edit_feature/<id>", methods=['GET'])
    def edit_feature_form(id):
        feature_film = db_feature.get_feature_by_id(db_feature.open_db(db_url), id)
        return render_template('edit_feature.html', feature_film=feature_film)

    @app.route("/edit_feature/<id>", methods=['POST'])
    def edit_feature(id):
        title = request.form['title']
        release_year = int(request.form['release_year'])
        country = request.form['country']
        director = request.form['director']
        main_roles = request.form['main_roles']
        genres = request.form['genres']
        box_office = int(request.form['box_office'])
        brief_description = request.form['brief_description']
        certificate = request.form['certificate']
        runtime = request.form['runtime']
        tags = request.form['tags']
        feature_film = Feature(id, title, release_year, country, director, main_roles, genres, box_office,
                               brief_description, certificate, runtime, tags)
        db_feature.update_feature(db_feature.open_db(db_url), feature_film)
        return redirect(url_for('details_feature_by_id', id=id))

    @app.route("/edit_documentary/<id>", methods=['GET'])
    def edit_documentary_form(id):
        documentary_film = db_documentary.get_documentary_by_id(db_documentary.open_db(db_url), id)
        return render_template('edit_documentary.html', documentary_film=documentary_film)

    @app.route("/edit_documentary/<id>", methods=['POST'])
    def edit_documentary(id):
        title = request.form['title']
        release_year = int(request.form['release_year'])
        country = request.form['country']
        director = request.form['director']
        category = request.form['category']
        brief_description = request.form['brief_description']
        certificate = request.form['certificate']
        runtime = request.form['runtime']
        tags = request.form['tags']
        documentary_film = Documentary(id, title, release_year, country, director, category, brief_description,
                                       certificate, runtime, tags)
        db_documentary.update_documentary(db_documentary.open_db(db_url), documentary_film)
        return redirect(url_for('details_documentary_by_id', id=id))

    @app.route("/edit_cartoon/<id>", methods=['GET'])
    def edit_cartoon_form(id):
        cartoon = db_cartoons.get_cartoons_by_id(db_cartoons.open_db(db_url), id)
        return render_template('edit_cartoon.html', cartoon=cartoon)

    @app.route("/edit_cartoon/<id>", methods=['POST'])
    def edit_cartoon(id):
        title = request.form['title']
        release_year = int(request.form['release_year'])
        country = request.form['country']
        method_of_creation = request.form['method_of_creation']
        director = request.form['director']
        genres = request.form['genres']
        brief_description = request.form['brief_description']
        certificate = request.form['certificate']
        duration = request.form['duration']
        runtime = request.form['runtime']
        tags = request.form['tags']
        cartoon = Cartoon(id, title, release_year, country, method_of_creation, director, genres,
                               brief_description, certificate, duration, runtime, tags)
        db_cartoons.update_cartoon(db_cartoons.open_db(db_url), cartoon)
        return redirect(url_for('details_cartoon_by_id', id=id))

    @app.route("/remove_feature/<id>", methods=['GET'])
    def remove_feature_form(id):
        feature_film = db_feature.get_feature_by_id(db_feature.open_db(db_url), id)
        return render_template('remove_feature.html', feature_film=feature_film)

    @app.route("/remove_feature/<id>", methods=['POST'])
    def remove_feature(id):
        db_feature.remove_feature(db_feature.open_db(db_url), id)
        return redirect(url_for('index'))

    @app.route("/remove_documentary/<id>", methods=['GET'])
    def remove_documentary_form(id):
        documentary_film = db_documentary.get_documentary_by_id(db_documentary.open_db(db_url), id)
        return render_template('remove_documentary.html', documentary_film=documentary_film)

    @app.route("/remove_documentary/<id>", methods=['POST'])
    def remove_documentary(id):
        db_documentary.remove_documentary(db_documentary.open_db(db_url), id)
        return redirect(url_for('index'))

    @app.route("/remove_cartoon/<id>", methods=['GET'])
    def remove_cartoon_form(id):
        cartoon = db_cartoons.get_cartoons_by_id(db_cartoons.open_db(db_url), id)
        return render_template('remove_cartoon.html', cartoon=cartoon)

    @app.route("/remove_cartoon/<id>", methods=['POST'])
    def remove_cartoon(id):
        db_cartoons.remove_cartoon(db_cartoons.open_db(db_url), id)
        return redirect(url_for('index'))

    @app.route('/export_csv')
    def export_csv():
        feature_films = db_feature.get_feature_films(db_feature.open_db(db_url))
        content = io.StringIO()
        writer = csv.writer(content)
        for feature_film in feature_films:
            writer.writerow([feature_film.id, feature_film.title, feature_film.release_year, feature_film.country,
                             feature_film.director, feature_film.main_roles, feature_film.genres,
                             feature_film.box_office, feature_film.brief_description, feature_film.certificate,
                             feature_film.runtime, feature_film.tags
                             ])
        response = make_response(content.getvalue())
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = 'inline; filename=exported.csv'
        return response

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(debug=True)


if __name__ == '__main__':
    start()
