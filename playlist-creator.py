import uuid
import sqlite3
import bs4
import json

id = str(uuid.uuid4())

empty_playlist = {
    "id": id,
    "games": [],
    "title": "User's submissions",
    "description": "All the submissions of a particular user.",
    "author": "",
    "icon": "",
    "library": "arcade",
	"extreme": bool(0)
}

print("In order to create the playlist, go to FPFSS, use advanced search to get all the submission of the user and increase the number of results per page so they all appear on a single page.")
print("Then copy the HTML source code and save it in a file called 'source.txt' in this same folder.")

f = open("source.txt", "r")
text = f.read()
f.close()

soup = bs4.BeautifulSoup(text)
titles = []
elements = soup.select(".submission-table-title")

for i in elements:
    title = i.getText()
    titles.append(title)

con = sqlite3.connect("flashpoint.sqlite")
cur = con.cursor()
ids = []

for title in titles:
    res = cur.execute('SELECT id FROM game WHERE title = ?', (title,))
    try:
        value = res.fetchall()[0][0]
    except:
        continue
    id = value
    ids.append(id)

new_playlist = empty_playlist
games = []

for count, id in enumerate(ids):
    game = {
        "gameId": id,
        "order" : count,
        "notes": ""
    }
    games.append(game)

new_playlist["games"] = games

with open("playlist.json", "w") as f:
        json.dump(new_playlist, f, indent=4)
