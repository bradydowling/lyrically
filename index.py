import lyricsgenius as genius
with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")

def cleanLyrics(lyrics):
    cleanedLyrics = lyrics.replace("Fuck", "F***")
    cleanedLyrics = lyrics.replace("fuck", "f***")
    cleanedLyrics = cleanedLyrics.replace("Shit", "S***")
    cleanedLyrics = cleanedLyrics.replace("shit", "s***")
    return cleanedLyrics

api = genius.Genius(genius_key)
song = api.search_song("The Glorious Five", "Logic")
print("Lyrics")
print(cleanLyrics(song.lyrics))
print("Total characters: ", len(song.lyrics))
words = song.lyrics.split()
print("Word count: ", len(words))
