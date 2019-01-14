import lyricsgenius as genius
import clean_lyrics
import pronouncing
import readability
import subprocess
import click
import re

with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")


def get_lyrics_stats(lyrics):
    expletives = clean_lyrics.count_expletives(lyrics)
    characters = len(lyrics)
    words = len(lyrics.split())
    stats = {"chars_num": characters, "words_num": words, "expletives_num": expletives}
    return stats


def strip_nonalpha_chars(word):
    return re.sub(r'[\[\]\(\)\,]', '', word)


def get_word_frequency(lyrics):
    # need to sort and cleanup this dict
    words_map = dict()
    for word in lyrics:
        plain_word = strip_nonalpha_chars(word)
        if plain_word in words_map:
            words_map[plain_word] += 1
        else:
            words_map[plain_word] = 1
    return words_map


def get_longest_word(lyrics):
    lyric_words = lyrics.split()
    longest_word = ""
    for word in lyric_words:
        plain_word = strip_nonalpha_chars(word)
        if len(plain_word) > len(longest_word):
            longest_word = plain_word
    return longest_word


def get_spotify_song():
    command = "osascript getCurrentSong.AppleScript"
    spotify_song_string = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8")
    # TODO: handle no Spotify song
    # TODO: Trim whitespace (newline) after song name
    song_title = spotify_song_string.split("^@^")[1].split(" - ")[0]
    song_title = re.sub(r'\(ft.[^)]*\)', '', song_title)
    song_title = re.sub(r'\(feat.[^)]*\)', '', song_title)
    artist_name = spotify_song_string.split("^@^")[0]
    song_info = {"song": song_title, "artist": artist_name}
    return song_info


def show_similes(lyrics):
    lyric_lines = lyrics.split("\n")
    simile_lines = list()
    if len(lyric_lines) > 0:
        for line in lyric_lines:
            if "like" in line and line not in simile_lines:
                simile_lines.append(line)

    print("Similes used in this song:", len(simile_lines))
    if len(simile_lines) > 0:
        click.echo("Lines with similes in them:")
        for simile_num, simile_line in enumerate(simile_lines):
            click.echo("%s. %s" % (simile_num + 1, simile_line))


@click.command()
@click.option("--artist", help="Artist of the song to search for")
@click.option("--song", help="Song title to search for")
@click.option("--clean", default=True, help="Whether the lyrics should be censored/cleaned")
@click.option("--lyrics", default=True, help="Whether the lyrics should be output")
@click.option("--stats", default=False, help="Whether the statistical analysis of the lyrics should be output")
@click.option("--similes", default=False, help="Alpha: Whether to count/list all lines with the word \"like\" in them")
def main(artist, song, clean, lyrics, stats, similes):
    spotify_song = get_spotify_song()["song"]
    spotify_artist = get_spotify_song()["artist"]
    api = genius.Genius(genius_key, remove_section_headers=True)
    if song and artist:
        song_info = api.search_song(song, artist)
    elif spotify_song and spotify_artist:
        song_info = api.search_song(spotify_song, spotify_artist)
    else:
        return click.echo("No artist and song title found, try playing and song in Spotify first")
    try:
        hasattr(song_info, "lyrics")
        if lyrics:
            click.echo("Lyrics:")
            if clean:
                lyrics_string = clean_lyrics.censor(song_info.lyrics)
            else:
                lyrics_string = song_info.lyrics
            click.echo(lyrics_string)

        if stats == "True" or stats == "true" or stats == "TRUE":
            lyrics_stats = get_lyrics_stats(song_info.lyrics)
            print("Total characters:", lyrics_stats["chars_num"])

            lyric_words = song_info.lyrics.split()
            word_map = get_word_frequency(lyric_words)
            click.echo("Total words: %s (%s unique)" % (lyrics_stats["words_num"], len(word_map)))
            click.echo("Total expletives: %s" % lyrics_stats["expletives_num"])

            if clean:
                longest_word = clean_lyrics.censor(get_longest_word(song_info.lyrics))
            else:
                longest_word = get_longest_word(song_info.lyrics)

            click.echo("Longest word: %s (%s letters)" % (longest_word, len(longest_word)))
            click.echo("Words by frequency:")
            word_map_sorted = sorted(word_map.items(), key=lambda kv: kv[1])
            word_map_sorted.reverse()
            word_num = 1
            for word_key, word_frequency in word_map_sorted:
                click.echo("%s). %s - %s" % (word_num, word_key, word_frequency))
                word_num += 1
                if word_num > 10:
                    break

            if similes:
                show_similes(song_info.lyrics)

            results = readability.getmeasures(song_info.lyrics, lang='en')
            print("Grade reading level: %s" % results['readability grades']['Kincaid'])

            # TODO: Import syllabic counters
            # TODO: See which lines rhyme with each other
            # TODO: Remove parenthetical words or count them with non-parenthesized words
            # TODO: Add how many lines, stanzas, and words per line/stanza

            # click.echo(pronouncing.rhymes("player"))
    except AttributeError:
        return click.echo("No songs found with this info")


if __name__ == "__main__":
    main()
