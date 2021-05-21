from db import db
from collections import ChainMap


class DataTableModel(db.Model):
    __tablename__ = 'data_tables'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    path = db.Column(db.String)
    dash = db.Column(db.String)

    def __init__(self, title, path, dash):
        """
        Creates DataTable Object
        :param title: title of DataTable
        :param path: link to DataTable explanation
        :param dash: link to DataTable Dashboard
        """
        self.title = title
        self.path = path
        self.dash = dash

    def __str__(self):
        """
        :return: Nicely Formatted String of Object
        """
        return f"title={self.title}, path={self.path}, dash={self.dash}"

    def __repr__(self):
        """
        :return: Representation of Object
        """
        return f"DataTable(title={self.title}, path={self.path}, dash={self.dash})"

    def json(self):
        return {str(self.id):
                    {"title": self.title,
                     "path": self.path,
                     "dash": self.dash}
                }

    def parser(self):
        return self.title, self.path, self.dash        # return tuple of <title, path, dash>

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

    @classmethod
    def table_json_list(cls):
        return dict(ChainMap(*[table.json() for table in cls.query.all()]))
