import lyricsgenius as genius
import cleanLyrics
with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")

def getLyricsStats(lyrics):
    characters = len(lyrics)
    words = len(lyrics.split())
    stats = {"charsNum": characters, "wordsNum": words}
    return stats

api = genius.Genius(genius_key)
song = api.search_song("The Glorious Five", "Logic")
print("Lyrics")
print(cleanLyrics.censor(song.lyrics))
lyricsStats = getLyricsStats(song.lyrics)
print("Total characters: ", lyricsStats["charsNum"])
print("Word count: ", lyricsStats["wordsNum"])
