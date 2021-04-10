from flask_restful import Resource, reqparse
from modules.flash_news import NewsFlashModel
from datetime import datetime


class FlashNews(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message', required=True, type=str, help='Flash news has to contain a message')
    parser.add_argument('date_time', required=False, type=lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M"),
                        help="Datetime must be in format dd/mm/yyyy HH:MM", default=datetime.now())

    @staticmethod
    def get(_id):
        flash_news = NewsFlashModel.find_by_id(_id)
        if flash_news:
            return flash_news.json()
        return {"msg": f"NewsFlash '{_id}' was not found"}, 404

    @classmethod
    def post(cls, _id):
        if NewsFlashModel.find_by_id(_id):
            return {"msg": f"NewsFlash of id {_id} already exists"}, 400
        data = cls.parser.parse_args()
        news_flash = NewsFlashModel(**data)
        try:
            news_flash.save_to_db()
        except Exception as e:
            print(e)
            return {"msg": "An error has occurred while inserting this item"}, 500
        return {"msg": "NewsFlash posted", "data": news_flash.json()}, 201

    @classmethod
    def put(cls, _id):
        news_flash = NewsFlashModel.find_by_id(_id)
        data = cls.parser.parse_args()
        if not news_flash:
            news_flash = NewsFlashModel(**data)
        else:
            news_flash.message = data['message']
            news_flash.date_time = data['date_time']
        try:
            news_flash.save_to_db()
        except Exception as e:
            print(e)
            return {"msg", "An error has occurred while updating this item"}, 500
        return {"msg": "Item posted", "data": news_flash.json()}, 200

    @staticmethod
    def delete(_id):
        news_flash = NewsFlashModel.find_by_id(_id)
        if not news_flash:
            return {"msg": f"NewsFlash {_id} doesn't exist"}, 404
        try:
            news_flash.delete_from_db()
            return {"msg": f"Item {_id} deleted successfully"}, 200
        except Exception as e:
            print(e)
            return {"msg", "An error has occurred deleting this item"}, 500


class FlashNewsList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('news_amount', required=False, type=int, help='news_amount has to be an integer')

    @classmethod
    def get(cls):
        data = cls.parser.parse_args()
        if data['news_amount']:
            return {"data": [flash.json() for flash in NewsFlashModel.query.all()[-data['news_amount']:]]}
        return {"data": [flash.json() for flash in NewsFlashModel.query.all()]}
