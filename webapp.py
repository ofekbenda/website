import requests

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

json = {
    "date_time": "26/12/2021 21:20",
    "message": "יומולדת לאופקקק"
}
r = requests.post("http://127.0.0.1:5000/flashNews/0", json=json)

print(r.json())
# mail_to_post