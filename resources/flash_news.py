from flask_restful import Resource, reqparse
from modules.flash_news import NewsFlashModel
from datetime import datetime


class FlashNews(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message', required=True, type=str, help='Flash news has to contain a message')
    parser.add_argument('date_time', required=False, type=lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M"),
                        help="Datetime must be in format dd/mm/yyyy HH:MM", default=datetime.now())

    @staticmethod
    def get():
        flash_news = FlashNewsList.get()
        if flash_news:
            return flash_news
        return {"msg": f"NewsFlash were not found"}, 404

    @classmethod
    def post(cls):
        # Parse the arguments that send with the post request
        data = cls.parser.parse_args()

        if data.message == '' or data.date_time == '':
            return {"msg": f"Source title/link is missing"}, 400

        news_to_insert = NewsFlashModel(**data)

        # if the day already exist with another date - DELETE all news with the old date
        dates_list = FlashNewsList.get().keys()
        for item in dates_list:
            day, date = item.split()
            if day == news_to_insert.day_of_week and date != news_to_insert.date.strftime('%d/%m/%Y'):
                FlashNewsList.delete_by_date(date)

        try:
            news_to_insert.add()
        except Exception as e:
            print(e)
            return {"msg": "An error has occurred while inserting this item"}, 500
        return {"msg": "news inserted", "data": news_to_insert.json()}, 201

    @classmethod
    def delete(cls):
        data = cls.parser.parse_args()
        news_to_delete = NewsFlashModel.find_row(data.date_time, data.message)

        if news_to_delete is not None:
            try:
                news_to_delete.delete()
                return {"msg": "Item deleted successfully", "item": news_to_delete.parser()}, 200
            except Exception as e:
                print(e)
                return {"msg", "An error has occurred deleting this item"}, 500
        else:
            return {"msg": f"NewsFlash {data} doesn't exist"}, 404


class FlashNewsList(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('news_amount', required=False, type=int, help='news_amount has to be an integer')

    @classmethod
    def group_by_day(cls, ls):
        res = {}
        for elem in ls:
            key, val = list(elem.keys()), list(elem.values())
            if key[0] in res:
                res[key[0]].append(val[0])
            else:
                res[key[0]] = [val[0]]
        return res

    @classmethod
    def get(cls):
        data = NewsFlashModel.query.all()               # get all table
        data = [flash.parser() for flash in data]      # parse it with json format
        data = cls.group_by_day(data)                 # group all news by date
        return data

    @classmethod
    # delete all the news with data from table
    def delete_by_date(cls, _date):
        data = NewsFlashModel.query.all()
        for item in data:
            item_date = item.date_time.date().strftime("%d/%m/%Y")
            if item_date == _date:
                item.delete()
