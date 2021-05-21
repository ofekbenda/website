from db import db


class SourcesModel(db.Model):
    __tablename__ = 'sources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    link = db.Column(db.String(200))

    def __init__(self, title: str, link: str):
        """
        Creates DataTable Object
        :param title: name of Source
        :param link: link to Source explanation
        """
        self.title = title
        self.link = link

    def __str__(self) -> str:
        """
        :return: Nicely Formatted String of Object
        """
        return f"title={self.title}, link={self.link}"

    def __repr__(self):
        """
        :return: Representation of Object
        """
        return f"DataTable(title={self.title}, link={self.link})"

    def json(self):
        return {str(self.id):
                    {"title": self.title,
                     "link": self.link}
                }

    def parser(self):
        return self.title, self.link        # return tuple of <title, link>

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_title(cls, _title):
        return cls.query.filter_by(title=_title).first()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get(cls):
        data = [table.parser() for table in cls.query.all()]
        return data