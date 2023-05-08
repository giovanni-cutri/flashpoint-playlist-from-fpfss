# Flashpoint Playlists from Submissions
A tool to create Flashpoint playlists of games submitted by a particular user.

# Getting started

Requires Python 3, which you can download [here](https://www.python.org/downloads/), along with the *Beatiful Soup* library.

- Download the *playlist-creator.py* file from this repository and place it in any folder.
- Inside that same folder, you will need to copy two files:
    - The playlist you want to sort, in JSON format (which is the default export format from the Flashpoint launcher);
     - The *flashpoint.sqlite* file, which you can find in your local Flashpoint copy, inside the *Data* folder.

# Usage

In order to create the playlist, go to FPFSS, use advanced search to get all the submission of the user and increase the number of results per page so they all appear on a single page.

Then copy the HTML source code of the web page and save it in a file called "source.txt" in the same folder of the script.

Finally, run *playlist-creator.py* and it will automatically generate a *playlist.json* file containing your playlist.

# Warnings

- The script checks for the titles of the games in the Flashpoint database and associates them with their Id. However, two different games can share the same title, which means the script will find only one of them (possibly the incorrect one) and add it to the playlist.

- The script creates only one playlist, which includes both games and animations.
