import werkzeug
from flask_restful import reqparse, Resource
from datetime import datetime

from werkzeug.datastructures import FileStorage

from modules.posts import PostModel


class Post(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('path', type=str, help='File path is required', required=True)
    parser.add_argument('title', type=str, help='Mail Subject is required', required=True)
    parser.add_argument('author', type=str, help='Post publisher is required', required=True)
    parser.add_argument('date', type=lambda x: datetime.strptime(x, "%d/%m/%Y").date(), default=datetime.now().date(),
                        help="date must be in format dd/mm/yyyy HH:MM")
    parser.add_argument('essence', type=str, help='essence is required', required=True)
    parser.add_argument('tags', type=str)

    parser1 = reqparse.RequestParser()
    parser1.add_argument('filename', type=FileStorage, location='files/posts', required=False)
    parser1.add_argument('tags', type=str)

    @staticmethod
    def get():
        post = PostList.get()
        if post:
            return post
        return {"msg": f"Post '{post}' was not found"}, 404

    # @staticmethod
    # def get_by_id(_id):
    #     post = PostModel.find_by_id(_id)
    #     if post:
    #         return post.json()
    #     return {"msg": f"Post '{_id}' was not found"}, 404

    @classmethod
    def post(cls):
        # cls.parser.add_argument('filename', type=werkzeug.datastructures.FileStorage, location='files/posts')
        data = cls.parser1.parse_args()
        print(data)
        # data = PostModel.mail_to_post("static/mails/"+data.filename["name"], data.tags)
            # .parser.parse_args()
        # if PostModel.find_by_title(data.title):
        #     return {"msg": f"Post title already exists"}, 400
        #
        # post = PostModel(**data)
        # PostList.save_post_file()
        #
        # try:
        #     post.save_to_db()
        # except ValueError:
        #     return {"msg": "File was not found"}, 404
        # except Exception as e:
        #     print(e)
        #     return {"msg": "An error has occurred while inserting this item"}, 500
        # return {"msg": "Post posted", "data": post.json()}, 201

    @staticmethod
    def delete(_id):
        post = PostModel.find_by_id(_id)
        if not post:
            return {"msg": f"Post {_id} doesn't exist"}, 404
        try:
            post.delete_from_db()
            return {"msg": f"Item {_id} deleted successfully"}, 200
        except Exception as e:
            print(e)
            return {"msg", "An error has occurred deleting this item"}, 500


class PostList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('post_amount', required=False, type=int, help='post_amount has to be an integer')

    @classmethod
    def get(cls):
        data = cls.parser.parse_args()
        # if data['post_amount']:
        #     return [post.json() for post in PostModel.query.all()[-data['post_amount']:]]
        # return [post.json() for post in PostModel.query.all()]
        data = PostModel.query.all()               # get all table
        data = [post.json() for post in data]      # parse it with json format
        return data

    @classmethod
    def save_post_file(cls):
        cls.parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files/posts')
        args = cls.parser.parse_args()
        mail_file = args['file']
        print(mail_file)
        # mail_file.save(mail_file)
