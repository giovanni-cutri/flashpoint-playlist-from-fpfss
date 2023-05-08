import uuid
import sqlite3
import bs4
import json

# generate unique id for the playlist
playlist_id = str(uuid.uuid4())

# create an empty playlist
empty_playlist = {
    "id": playlist_id,
    "games": [],
    "title": "User's submissions",
    "description": "All the submissions of a particular user.",
    "author": "",
    "icon": "",
    "library": "arcade",
    "extreme": bool(0)
}

f = open("source.txt", "r", encoding = "utf-8")
text = f.read()
f.close()

soup = bs4.BeautifulSoup(text, "html.parser")
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
        "playlistId": playlist_id,
        "order" : count,
        "notes": "",
        "gameId": id
    }
    games.append(game)

new_playlist["games"] = games

with open("playlist.json", "w") as f:
        json.dump(new_playlist, f, indent=4)
