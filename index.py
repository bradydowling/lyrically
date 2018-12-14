import lyricsgenius as genius
with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")

api = genius.Genius(genius_key)
song = api.search_song("The Glorious Five", "Logic")
print("Lyrics")
print(song.lyrics)
print("Total characters: ", len(song.lyrics))
words = song.lyrics.split()
print("Word count: ", len(words))

def censorLyrics(lyricsArray):
    for word in lyricsArray