import lyricsgenius as genius
import clean_lyrics
import pronouncing
import sys

with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")


def get_lyrics_stats(lyrics):
    characters = len(lyrics)
    words = len(lyrics.split())
    stats = {"chars_num": characters, "words_num": words}
    return stats


def get_word_frequency(lyrics):
    # need to sort and cleanup this dict
    words_map = dict()
    for word in lyrics:
        if word in words_map:
            words_map[word] += 1
        else:
            words_map[word] = 1
    return words_map


artist_name = "Logic"
song_name = "Under Pressure"
api = genius.Genius(genius_key)
song = api.search_song(song_name, artist_name)

print("Lyrics")
print(clean_lyrics.censor(song.lyrics))

lyricsStats = get_lyrics_stats(song.lyrics)
print("Total characters:", lyricsStats["chars_num"])

lyricWords = song.lyrics.split()
wordMap = get_word_frequency(lyricWords)
print("Total words: %s (%s unique)" % (lyricsStats["words_num"], len(wordMap)))

print("Similes used in this song:", wordMap["like"])
lyricLines = song.lyrics.split("\n")
if len(lyricLines) > 0:
    print("Lines with similes in them:")
    simile_num = 0
    for line in lyricLines:
        if "like" in line:
            simile_num += 1
            print("%s. %s" % (simile_num, line))

# print("Word frequency: ", getWordFrequency(lyricWords))

# Todo: [Hook], [Verse 1], etc

print(pronouncing.rhymes("player"))