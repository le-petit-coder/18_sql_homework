import flask
from flask_restx import Resource, Namespace

from app.models.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):
    def get_all(self):
        args = flask.request.args
        if len(args):
            return movie_schema.dump(
                movie_service.get_movie(**args)
            ), 200
        return movie_schema.dump(movie_service.get_all_movies()), 200

    def post(self):
        data = flask.request.json
        if movie_service.post_movie(data):
            return "movie created", 201
        else:
            return "creation failed"


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get_by_id(self, mid):
        return movie_schema.dump(movie_service.get_movie_by_id(mid=mid)), 200

    def update_movie(self):
        data = flask.request.json
        if movie_service.update_movie(data):
            return "update done", 200
        else:
            return "update failed"

    def delete_movie(self, mid):
        if movie_service.delete_movie(mid):
            return "delete done", 204
        else:
            return "delete failed"
