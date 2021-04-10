from flask_restful import reqparse, Resource
from datetime import datetime
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

    @staticmethod
    def get(_id):
        post = PostModel.find_by_id(_id)
        if post:
            return post.json()
        return {"msg": f"Post '{_id}' was not found"}, 404

    @classmethod
    def post(cls, _id):
        if PostModel.find_by_id(_id):
            return {"msg": f"Post of id {_id} already exists"}, 400
        data = cls.parser.parse_args()
        post = PostModel(**data)
        try:
            post.save_to_db()
        except ValueError:
            return {"msg": "File was not found"}, 404
        except Exception as e:
            print(e)
            return {"msg": "An error has occurred while inserting this item"}, 500
        return {"msg": "Post posted", "data": post.json()}, 201

    @classmethod
    def put(cls, _id):
        post = PostModel.find_by_id(_id)
        data = cls.parser.parse_args()
        if not post:
            post = PostModel(**data)
        else:
            post.message = data['message']
            post.date_time = data['date_time']
        try:
            post.save_to_db()
        except ValueError:
            return {"msg": "File was not found"}, 404
        except Exception as e:
            print(e)
            return {"msg", "An error has occurred while updating this item"}, 500
        return {"msg": "Item posted", "data": post.json()}, 200

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
    def get(cls, post_amount=50):
        data = cls.parser.parse_args()
        if data['post_amount']:
            return {"data": [post.json() for post in PostModel.query.all()[-data['post_amount']:]]}
        if post_amount:
            return {"data": [post.json() for post in PostModel.query.all()[-post_amount:]]}
        return {"data": [post.json() for post in PostModel.query.all()]}
