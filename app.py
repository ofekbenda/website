from json import dumps

from flask import Flask, render_template, send_from_directory
import pandas as pd
from flask_restful import Api
from resources.posts import Post, PostList
from resources.flash_news import FlashNews, FlashNewsList
from modules.posts import PostModel
import requests
from db import db


app = Flask(__name__, static_url_path='')
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files/databases/data.db'
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Post, '/post/<int:_id>')
api.add_resource(PostList, '/posts/')
api.add_resource(FlashNews, '/flashNews/<int:_id>')
api.add_resource(FlashNewsList, '/flashNews/')

#------ clean cache --------#
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    THIS FUNCTION PREVENTS CACHING OF STATIC FILES
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# ------ HOME PAGE -------- #
@app.route('/', methods=("POST", "GET"))
def home():
    # main_updates type is main-updates[date]:DataFrame == {time: content}:Dict
    main_updates = pd.read_json('./databases/HomePageUpdates.json', typ='series')
    return render_template('Home.html', main_updates = main_updates)

# ------ UPDATES PAGE -------- #
@app.route('/updates', methods=("POST", "GET"))
def updates():
    # mails = pd.read_excel("./databases/mails.xlsx")
    mails = PostList.get()
    mails = pd.DataFrame(PostModel.json_list(mails))
    topics = pd.read_json('./databases/tags.json', typ='series')
    return render_template('updates.html', mails= mails, topics=topics)

# ------ DataTables PAGE -------- #
#ma'atarim and ma'garim

@app.route('/dataTables', methods=("POST", "GET"))
def dataTables():
    data = pd.read_json('./databases/data.json')
    print(data)

    return render_template('DataTables-1.html', data=data.values)

# ------ STATIC FILE PAGE -------- #
@app.route('/files/<path:path>')
def send_js(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(debug=True)