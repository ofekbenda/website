from flask import Flask, render_template, send_from_directory, request
import pandas as pd
from flask_restful import Api

from modules.posts import PostModel
from resources.flash_news import FlashNews, FlashNewsList
from resources.posts import Post, PostList
from resources.data_table import DataTable, DataTableList
from resources.sources import Source, SourceList

from db import db


app = Flask(__name__, static_url_path='')
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files/databases/data.db'
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Post, '/post')
# api.add_resource(PostList, '/posts/')
api.add_resource(FlashNews, '/flashNews')
api.add_resource(Source, '/source')
api.add_resource(DataTable, '/DataTable')

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
    # main_updates = pd.read_json('./databases/HomePageUpdates.json', typ='series')
    # print(main_updates)
    news = FlashNewsList.get()

    return render_template('Home.html', main_updates = news)


# ------ UPDATES PAGE -------- #
@app.route('/updates', methods=("POST", "GET"))
def updates():
    # mails = pd.read_excel("./databases/mails.xlsx")
    mails = pd.DataFrame(PostList.get())                              # get posts from db
    print(f"mail: \n {mails}")
    # print(PostModel.json_list(mails))
    # mails = pd.DataFrame(PostModel.json_list(mails))    # convert to json format
    topics = pd.read_json('./databases/tags.json', typ='series')
    return render_template('updates.html', mails= mails, topics=topics)


# ------ DataTables PAGE -------- #
#ma'atarim and ma'garim
@app.route('/databasesInfo', methods=("POST", "GET"))
def databasesInfo():
    # data = pd.read_json('./databases/data.json')
    datatables = DataTableList.get()
    return render_template('databasesInfo.html', data=datatables)


# ------ Sources PAGE -------- #
@app.route('/sourcesInfo', methods=("POST", "GET"))
def sourcesInfo():
    # data = pd.read_json('./databases/sources.json')
    # data = list(zip(data.values[0],data.values[1]))
    data = SourceList.get()
    return render_template('sourcesInfo.html', data=data)


# ------ Info PAGE -------- #
@app.route('/info', methods=("POST", "GET"))
def info():
    return render_template('info.html')


# ------ Infos-Processing PAGE -------- #
@app.route('/infoProcessing', methods=("POST", "GET"))
def infoPorcessing():
    return render_template('infoProcessing.html')


# ------ info-DataLab PAGE -------- #
@app.route('/infoLab', methods=("POST", "GET"))
def infoLab():
    return render_template('infoLab.html')


# ------ info-Dev PAGE -------- #
@app.route('/infoGeography', methods=("POST", "GET"))
def infoGeography():
    return render_template('infoGeography.html')


# ------ info-Dev PAGE -------- #
@app.route('/infoDevelopment', methods=("POST", "GET"))
def infoDevelopment():
    return render_template('infoDevelopment.html')


# ------ info-Targets PAGE -------- #
@app.route('/infoTargets', methods=("POST", "GET"))
def infoTargets():
    return render_template('infoTargets.html')


# ------ info-Activity PAGE -------- #
@app.route('/infoActivity', methods=("POST", "GET"))
def infoActivity():
    return render_template('infoActivity.html')


# ------ info-Targets PAGE -------- #
@app.route('/infoSensors', methods=("POST", "GET"))
def infoSensors():
    return render_template('infoSensors.html')


# ------ Tools PAGE -------- #
@app.route('/tools', methods=("POST", "GET"))
def tools():
    return render_template('tools.html')


# ------ API PAGE -------- #
@app.route('/API', methods=("POST", "GET"))
def API():
    tags = pd.read_json('./databases/tags.json', typ='series')
    sources = SourceList.get()
    news = FlashNewsList.get()
    datatable = DataTableList.get()
    return render_template('API.html', tags=tags, sources=sources, news=news, datatable=datatable)

# ------ Updates_API -------- #
@app.route('/updates_API', methods=("POST", "GET"))
def updates_API():
    # print(request.files.getlist('file'))
    uploaded_file = request.files['filename']
    if uploaded_file.filename != '':
        uploaded_file.save('files/posts/'+uploaded_file.filename)
    tags = pd.read_json('./databases/tags.json', typ='series')
    return render_template('API.html', tags = tags)


# ------ STATIC FILE PAGE -------- #
@app.route('/files/<path:path>')
def send_js(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(debug=True)