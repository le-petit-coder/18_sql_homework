from app.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all_directors(self):
        return self.dao.get_all_directors()

    def get_director_by_id(self, did):
        return self.dao.get_director_by_id(did)
