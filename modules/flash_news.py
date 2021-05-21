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
        return f"NewsFlashModel(news={self.message}, date_time={self.date_time})"

    def __str__(self) -> str:
        """
        Creates a Nicely formatted string representation of the NewsFlashModel obj
        :return: Nicely formatted string representation of the NewsFlashModel
        """
        return f"""
        News: {self.message},
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
        return {f"{self.date} {self.day_of_week}": {self.time: self.message}}

    def parser(self):
        return {f"{self.day_of_week} {self.date.strftime('%d/%m/%Y')}": (self.time, self.message)}

    @classmethod
    def find_row(cls, _datetime, _message):
        data = NewsFlashModel.query.all()  # get all table
        res = None
        for item in data:
            if _datetime == item.date_time and _message == item.message:
                res = item
                break

        return res

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()