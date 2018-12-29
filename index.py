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

lyrics_stats = get_lyrics_stats(song.lyrics)
print("Total characters:", lyrics_stats["chars_num"])

lyric_words = song.lyrics.split()
word_map = get_word_frequency(lyric_words)
print("Total words: %s (%s unique)" % (lyrics_stats["words_num"], len(word_map)))

print("Similes used in this song:", word_map["like"])
lyric_lines = song.lyrics.split("\n")
if len(lyric_lines) > 0:
    print("Lines with similes in them:")
    simile_num = 0
    for line in lyric_lines:
        if "like" in line:
            simile_num += 1
            print("%s. %s" % (simile_num, line))

# print("Word frequency: ", getWordFrequency(lyricWords))

# Todo: [Hook], [Verse 1], etc

print(pronouncing.rhymes("player"))