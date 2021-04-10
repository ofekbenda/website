__author__ = "Daniel Harari"

from datetime import datetime
from db import db


class NewsFlashModel(db.Model):
    __tablename__ = 'news_flash'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))
    date_time = db.Column(db.DateTime)

    HASH_DAYS_DICT = {
        0: "שני",
        1: "שלישי",
        2: "רביעי",
        3: "חמישי",
        4: "שישי",
        5: "שבת",
        6: "ראשון"
    }

    def __init__(self, message: str, date_time: datetime = datetime.now()):
        """
        Initializes a NewsFlash obj that contains the new, date, time and day of the week
        :param message: The flash news text
        :param date_time: Date of the news
        """
        self.message = message
        self.date_time = date_time

    def __repr__(self) -> str:
        """
        creates obj representation of NewsFlash
        :return: Obj representation
        """
        return f"NewsFlashModel(news={self.msg}, date_time={self.date_time})"

    def __str__(self) -> str:
        """
        Creates a Nicely formatted string representation of the NewsFlashModel obj
        :return: Nicely formatted string representation of the NewsFlashModel
        """
        return f"""
        News: {self.msg},
        Date: {self.date_time.strftime("%d/%m/%Y %H:%M")}
        """

    @property
    def day_of_week(self):
        return self.HASH_DAYS_DICT.get(self.date.weekday())

    @property
    def date(self):
        return self.date_time.date()

    @property
    def time(self):
        return self.date_time.time().strftime("%H:%M")

    def json(self):
        return {f"{self.date.strftime('%d/%m/%y')} {self.day_of_week}": {"id": self.id, self.time: self.message}}

    @classmethod
    def english_days(cls):
        """
        Turns days into days in Hebrew
        :return: None
        """
        cls.HASH_DAYS_DICT[0] = "Monday"
        cls.HASH_DAYS_DICT[1] = "Tuesday"
        cls.HASH_DAYS_DICT[2] = "Wedensday"
        cls.HASH_DAYS_DICT[3] = "Thursday"
        cls.HASH_DAYS_DICT[4] = "Friday"
        cls.HASH_DAYS_DICT[5] = "Saturday"
        cls.HASH_DAYS_DICT[6] = "Sunday"

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # @staticmethod
    # def json_list(org_json):
    #     data = org_json['data']
    #     new_json = dict().
    #     for flash in data:
    #         if flash.keys()[0] in new_json["keys"]:
    #             day_key = flash.keys()[0]
    #             if flash[day_key].keys()[0] in new_json[day_key].keys()[0]:
    #                 time_key = flash[day_key].keys()[0]
    #                 new_json[day_key][time_key] += f'\n\n{flash[day_key][time_key]}'
    #             else:
    #                 new_json[day_key] = {org_json[day_key].keys()[1]:
    #         else:
    #             flash.