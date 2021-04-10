__author__ = "Daniel Harari"

from typing import Dict
import msg_parser
from db import db
import datetime
from genericpath import exists


class PostModel(db.Model):
    __tablename__ = 'posts'
    GIST_MAX_LENGTH = 200
    TAGS_LIST = ['תעסוקה', 'לימודים', 'מלגה', 'התנדבות', 'קורסים', 'הוראה']
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String)
    title = db.Column(db.String(50))
    date = db.Column(db.Date)
    author = db.Column(db.String(50))
    essence = db.Column(db.String(GIST_MAX_LENGTH))
    tags = db.Column(db.String(30))

    def __init__(self,  path: str, title: str, date: datetime.date,  author: str, essence: str, tags: str):
        """
        Initializes a Post object that contains
        :param path: file path to post
        :param title: post subject
        :param date: publish date
        :param author: post publisher
        :param essence: gist of post
        :param tags: categorical tags of post
        """
        self.path = path
        self.title = title
        self.date = date
        self.author = author
        self.essence = essence[:self.GIST_MAX_LENGTH]
        self.tags = ','.join(list(filter(lambda x: x in self.TAGS_LIST, tags.split(','))))

        if not exists("static/mails/"+path):
            raise ValueError("path doesnt exist")

    def __str__(self) -> str:
        """
        creates string representation of posts
        :return string representation of post:
        """
        return f"""
        File path: {self.path},
        Title: {self.title},
        Publisher: {self.author},
        Publish Date: {self.date},
        Tags: {self.tags},
        Gist: {self.essence}
        """

    def __repr__(self) -> str:
        """
        creates obj representation of Post
        :return: Obj representation
        """
        return f"Post(fp={self.path}, subject={self.title}, publish_date={self.date}, publisher={self.author}," \
               f" tags={self.tags}, gist={self.essence})"

    def json(self) -> Dict:
        """
        Creates a Json format object and returns it
        :return: Json of Post
        """
        post_json = {
            "id": self.id,
            "data": {
                "path": self.path,
                "title": self.title,
                "date": f"{self.date}",
                "author": self.author,
                "essence": self.essence,
                "tags": self.tags
            }
        }
        return post_json

    @classmethod
    def set_max_gist_len(cls, length: int) -> int:
        """
        Sets Max Length For gists
        :param length: New max Length For Gists
        :return: Length set
        """
        if type(length) == int and 0 < length <= 500:
            cls.GIST_MAX_LENGTH = length
        else:
            raise ValueError("Value has to be a positive Integer up to 500")
        return cls.GIST_MAX_LENGTH

    @staticmethod
    def read_dict(post_dict: dict) -> 'PostModel':
        """
        Gets a dictionary and forms a Post object from it
        :param post_dict: Dict containing data to create a post
        :return: Post formed by the data in the dict
        """
        post_dict["tags"] = post_dict["tags"].split(',')
        return PostModel(**post_dict)

    @staticmethod
    def mail_to_post(file_path: str, tags: str, custom_gist: str = '', gist_len: int = 200) -> 'PostModel':
        """
        Takes path to message file and creates a Post obj from it
        :param file_path: path to message file
        :param tags: post category tags
        :param custom_gist: custom gist of msg
        :param gist_len: length of gist
        :return: Post object of msg file
        """

        msg = msg_parser.MsOxMessage(file_path)
        gist = custom_gist if custom_gist else msg.body[:gist_len]
        date = msg.sent_date[:-15]
        return PostModel(file_path, msg.subject, datetime.datetime.strptime(date, "%a, %d %b %Y").date(), msg.sender[0],
                         gist, tags)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def json_list(org_json):
        return [post_json['data'] for post_json in org_json["data"]]