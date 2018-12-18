import lyricsgenius as genius
import cleanLyrics
with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")

def getLyricsStats(lyrics):
    characters = len(lyrics)
    words = len(lyrics.split())
    stats = {"charsNum": characters, "wordsNum": words}
    return stats

def getWordFrequency(lyrics):
    # need to sort and cleanup this dict
    wordsMap = dict()
    for word in lyrics:
        if word in wordsMap:
            wordsMap[word] += 1
        else:
            wordsMap[word] = 1
    return wordsMap

api = genius.Genius(genius_key)
song = api.search_song("The Glorious Five", "Logic")

print("Lyrics")
print(cleanLyrics.censor(song.lyrics))

lyricsStats = getLyricsStats(song.lyrics)
print("Total characters: ", lyricsStats["charsNum"])
print("Word count: ", lyricsStats["wordsNum"])
lyricWords = song.lyrics.split()

print("Word frequency: ", getWordFrequency(lyricWords))
