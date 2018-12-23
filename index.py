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

artistName = "Bazzi"
songName = "Beautiful"
api = genius.Genius(genius_key)
song = api.search_song(songName, artistName)

print("Lyrics")
print(cleanLyrics.censor(song.lyrics))

lyricsStats = getLyricsStats(song.lyrics)
print("Total characters:", lyricsStats["charsNum"])

lyricWords = song.lyrics.split()
wordMap = getWordFrequency(lyricWords)
print("Total words: %s (%s unique)" % (lyricsStats["wordsNum"], len(wordMap)))

print("Similies used in this song:", wordMap["like"])
lyricLines = song.lyrics.split("\n")
if len(lyricLines) > 0:
    print("Lines with similies in them:")
    similieNum = 0
    for line in lyricLines:
        if "like" in line:
            similieNum += 1
            print("%s. %s" % (similieNum, line))

# print("Word frequency: ", getWordFrequency(lyricWords))