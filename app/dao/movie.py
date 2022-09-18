from app.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movies_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def post_movie(self, **kwargs):
        try:
            self.session.query.add(
                Movie(**kwargs)
            )
            self.session.commit()
            return "movie created"
        except Exception as e:
            print(e)
            self.session.rollback()
            return "creation failed"

    def update_movie(self, **kwargs):
        try:
            self.session.query(Movie).filter(
                Movie.id == kwargs.get("id").update(
                    kwargs))
            self.session.commit()
            return "movie updated"
        except Exception as e:
            print(e)
            self.session.rollbakc()
            return "update failed"

    def delete_movie(self, mid):
        try:
            self.session.query(Movie).filter(Movie.id == mid).delete()
            self.session.commit()
            return "movie deleted"
        except Exception as e:
            print(e)
            self.session.rollback()
            return "delete failed"
