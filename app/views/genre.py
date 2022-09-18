from flask_restx import Resource, Namespace

from app.models.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genre_schema.dump(genre_service.get_all_genres()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        return genre_schema.dump(genre_service.get_genre_by_id(gid=gid)), 200
