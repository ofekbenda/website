from flask_restful import Resource, reqparse
from modules.sources import SourcesModel


class Source(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, type=str, help='Must contain name of Source')
    parser.add_argument('link', required=False, type=str, help="Must pe valid path to website")

    @staticmethod
    def get():
        source = SourcesModel.get()
        if source:
            return source
        return {"msg": f"Sources was not found"}, 404

    @classmethod
    def post(cls):
        # Parse the arguments that send with the post request
        data = cls.parser.parse_args()

        if SourcesModel.find_by_title(data.title):
            return {"msg": f"Source title already exists"}, 400

        if data.title == '' or data.link == '':
            return {"msg": f"Source title/link is missing"}, 400

        source = SourcesModel(**data)
        try:
            source.add()
        except Exception as e:
            print(e)
            return {"msg": "An error has occurred while inserting this item"}, 500
        return {"msg": "Source inserted", "data": source.json()}, 201

    @classmethod
    def delete(cls):
        data = cls.parser.parse_args()
        source = SourcesModel.find_by_title(data.title)
        print(source)
        if not source:
            return {"msg": f"DataTable doesn't exist"}, 404
        try:
            source.delete()
            return {"msg": f"Item {data.title} was deleted successfully"}, 200
        except Exception as e:
            print(e)
            return {"msg", "An error has occurred deleting this item"}, 500


class SourceList(Resource):
    parser = reqparse.RequestParser()

    @classmethod
    def get(cls):
        return SourcesModel.get()
