from app.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_director_by_id(self, did):
        return self.session.query(Director).get(did)
