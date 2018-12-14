import lyricsgenius as genius
with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")
api = genius.Genius(genius_key)
artist = api.search_artist("Logic", max_songs=3)
song = api.search_song("The Glorious Five", artist.name)
print(song.lyrics)
