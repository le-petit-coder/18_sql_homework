from flask_restx import Resource, Namespace

from app.models.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return director_schema.dump(director_service.get_all_directors()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        return director_schema.dump(director_service.get_director_by_id(did=did)), 200