from flask_restful import Resource, reqparse
from modules.data_table import DataTableModel


class DataTable(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, type=str, help='Must contain name of DataTable')
    parser.add_argument('path', required=False, type=str, help="Must pe valid path to website")
    parser.add_argument('dash', required=False, type=str, help="Must pe valid path to dashboard")

    @staticmethod
    def get():
        data_table = DataTableModel.get()
        if data_table:
            return data_table
        return {"msg": f"DataTables was not found"}, 404

    @classmethod
    def post(cls):
        # Parse the arguments that send with the post request
        data = cls.parser.parse_args()

        if DataTableModel.find_by_title(data.title):
            return {"msg": f"DataTable title already exists"}, 400

        if data.title == '' or data.path == '':
            return {"msg": f"DataTable's title / wiki path is missing"}, 400

        data_table = DataTableModel(**data)
        try:
            data_table.add()
        except Exception as e:
            print(e)
            return {"msg": "An error has occurred while inserting this item"}, 500
        return {"msg": "DataTable posted", "data": data_table.json()}, 201

    @classmethod
    def delete(cls):
        data = cls.parser.parse_args()
        data_table = DataTableModel.find_by_title(data.title)
        if not data_table:
            return {"msg": f"DataTable doesn't exist"}, 404
        try:
            data_table.delete()
            return {"msg": f"Item {data.title} was deleted successfully"}, 200
        except Exception as e:
            print(e)
            return {"msg", "An error has occurred deleting this item"}, 500


class DataTableList(Resource):
    @staticmethod
    def get():
        return DataTableModel.get()
