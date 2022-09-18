from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService
from setup_db import db

director_service = DirectorService(DirectorDAO(db.session))
genre_service = GenreService(GenreDAO(db.session))
movie_service = MovieService(MovieDAO(db.session))