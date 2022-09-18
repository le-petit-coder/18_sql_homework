from app.dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all_genres(self):
        return self.dao.get_all_genres()

    def get_genre_by_id(self, gid):
        return self.dao.get_genre_by_id(gid)