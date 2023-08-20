# Flashpoint Playlists from FPFSS
A tool to create [Flashpoint](https://bluemaxima.org/flashpoint/) playlists of games included in the results of a search on [FPFSS](https://fpfss.unstable.life/).

# Getting started

Requires Python 3, which you can download [here](https://www.python.org/downloads/), along with the *Beatiful Soup* library.

- Download the *playlist-creator.py* file from this repository and place it in any folder.
- Inside that same folder, you will need to copy the *flashpoint.sqlite* file, which you can find in your local Flashpoint copy, inside the *Data* folder.

# Usage

- Go to FPFSS, switch to advanced search and perform your search by filling the fields appropriately. Additionally, increase the number of results per page to a sufficient amount so that they all appear on a single page.
- Copy the HTML source code of the web page and save it in a text file called *source.txt* in the same folder of the script.
- Finally, run *playlist-creator.py* and it will automatically generate a *playlist.json* file containing your playlist.

# Warnings

- The script checks for the titles of the games in the Flashpoint database and associates them with their Id. However, two different games can share the same title, which means the script will find only one of them (possibly the incorrect one) and add it to the playlist.

- The playlist will also include games that were submitted, but did not get accepted because they were duplicates of pre-existing games.

- The script creates only one playlist, which includes both games and animations.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/giovanni-cutri/flashpoint-playlist-from-submissions/blob/main/LICENSE) file for details.
