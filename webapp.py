import requests
from db import db

# json = {
#     "path": "mail1.html",
#     "title": "ממצאי סקר שביעות רצון מההוראה- סמסטר א- תשפא",
#     "author": "teaching-center@bgu.ac.il",
#     "date": "10/10/2020",
#     "tags": "לימודים,הוראה",
#     "essence": "שלום רב,לאחר סיום עיבוד תוצאות הסקר מצורף קישור לממצאיו."
# }
# r = requests.post("http://127.0.0.1:5000/post/0", json=json)
#
# r = requests.get("http://127.0.0.1:5000/post/1")
# # print(r.ok)

# r = requests.delete("http://127.0.0.1:5000/post/2")

# --------------- add to flashNews --------------
json = {
    "date_time": "14/12/2021 21:20",
    "message": "הודעה לאופקקק"
}
r = requests.post("http://127.0.0.1:5000/flashNews", json=json)

# print(r.json())


#---------------- add to sources --------------

# json ={
#     "title": "מקור היסטורי",
#     "link": "https://he.wikipedia.org/wiki/%D7%9E%D7%A7%D7%95%D7%A8_%D7%94%D7%99%D7%A1%D7%98%D7%95%D7%A8%D7%99"
#     }
# r = requests.post('http://127.0.0.1:5000/source/0', json=json)
# print(r)