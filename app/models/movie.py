from marshmallow import Schema, fields
from setup_db import db
from app.models.genre import GenreSchema
from app.models.director import DirectorSchema


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.String)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship("Genre")
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Nested(GenreSchema)
    director_id = fields.Nested(DirectorSchema)