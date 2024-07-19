import uuid
import sqlite3
import requests
import bs4
import json

base_url = "https://fpfss.unstable.life"

# generate unique id for the playlist
playlist_id = str(uuid.uuid4())

# create an empty playlist
empty_playlist = {
    "id": playlist_id,
    "games": [],
    "title": "No Title",
    "description": "No Description",
    "author": "",
    "icon": "",
    "library": "arcade",
    "extreme": bool(0)
}

f = open("cookie.txt", "r", encoding = "utf-8")
cookie = f.read()
f.close()

headers = {"Cookie": f"login={cookie}"}

f = open("url.txt", "r", encoding = "utf-8")
url = f.read()
f.close()

res = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(res.text, "html.parser")
urls = []
elements = soup.select("td.center a")

for i in elements:
    if i.getText() == "View":
        url = f"{base_url}{i.attrs['href']}"
        urls.append(url)

ids = []
titles = []

for url in urls:
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    if "Marked the submission as added to Flashpoint. Game ID:" in res.text:    # if the submission was added to Flashpoint after April 27, 2023, the game ID is shown in the page
        submission_comments = soup.select("div.comment-body")
        for i in submission_comments:
            if "Marked the submission as added to Flashpoint. Game ID:" in i.getText():
                id = i.getText().split("Game ID: ")[-1].strip()
                ids.append(id)
    else:    # otherwise, resort to the title
        title = soup.select(".submission-table-title")[0].getText()
        titles.append(title)

# get the remaining ids from titles
con = sqlite3.connect("flashpoint.sqlite")
cur = con.cursor()

for title in titles:
    res = cur.execute('SELECT id FROM game WHERE title = ?', (title,))
    try:
        value = res.fetchall()[0][0]
    except:
        continue
    id = value
    ids.append(id)

ids.reverse()    # reverse the list
new_playlist = empty_playlist
games = []

for count, id in enumerate(ids):
    game = {
        "order" : count,
        "notes": "",
        "gameId": id
    }
    games.append(game)

new_playlist["games"] = games

with open("playlist.json", "w") as f:
        json.dump(new_playlist, f, indent=4)
