from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_movies(self):
        return self.dao.get_all_movies()

    def get_movie_by_id(self, mid):
        return self.dao.get_movie_by_id(mid)

    def get_movies_by_year(self, year):
        return self.dao.get_movies_by_year(year)

    def get_movie(self, **kwargs):
        return self.dao.get_movie(**kwargs)

    def post_movie(self, **kwargs):
        self.dao.post_movie(**kwargs)

    def update_movie(self, **kwargs):
        self.dao.update_movie(**kwargs)

    def delete_movie(self, mid):
        self.dao.delete_movie(mid)
