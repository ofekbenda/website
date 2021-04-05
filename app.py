from json import dumps

from flask import Flask, request, render_template, jsonify, redirect, flash, send_from_directory
import pandas as pd
from collections import OrderedDict

app = Flask(__name__, static_url_path='')

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
    print(main_updates[0])
    return render_template('Home.html', main_updates = main_updates)

# ------ UPDATES PAGE -------- #
@app.route('/updates', methods=("POST", "GET"))
def updates():
    mails = pd.read_excel("./databases/mails.xlsx")
    topics = pd.read_json('./databases/tags.json', typ='series')
    return render_template('updates.html', mails= mails, topics=topics)


# ------ STATIC FILE PAGE -------- #
@app.route('/files/<path:path>')
def send_js(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(debug=True)