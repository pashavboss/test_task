import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    slug = db.Column(db.String(1024), unique=True)
    content = db.Column(db.Text())
    published = db.Column(db.Boolean, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def serialize(self):
        """Return object data in easily serializeable format"""
        obj = {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "content": self.content,
            "published": self.published,
            "timestamp": self.timestamp.isoformat(),
        }
        return obj

    def save(self):
        """
        Persist the search in the database

        :param article:
        :return:
        """
        db.session.add(self)
        db.session.commit()
        return True

    def update(self):
        """
        Persist the updated search in the database

        :param article:
        :return:
        """
        db.session.commit()
        return True

    def delete(self):
        """
        Delete the search in the database

        :param article:
        :return:
        """
        db.session.delete(self)
        db.session.commit()
        return True

    @staticmethod
    def get_all():
        """
        Return a list of all articles.

        :return: list of searchs or empty list
        """
        data = Article.query.all()
        if data is not None:
            return data
        return None
