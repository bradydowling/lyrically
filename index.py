import lyricsgenius as genius
import clean_lyrics
import pronouncing
import subprocess
import click

with open(".genius_key", "r") as myfile:
    genius_key = myfile.read().replace("\n", "")


def get_lyrics_stats(lyrics):
    expletives = clean_lyrics.count_expletives(lyrics)
    characters = len(lyrics)
    words = len(lyrics.split())
    stats = {"chars_num": characters, "words_num": words, "expletives_num": expletives}
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


def get_longest_word(lyrics):
    longest_word = lyrics[0]
    for word in lyrics:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def get_spotify_song():
    command = "osascript getCurrentSong.AppleScript"
    spotify_song = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8")
    return spotify_song


@click.command()
@click.argument("artist")
@click.argument("song")
@click.option("--clean", default=True, help="Whether the lyrics should be censored/cleaned")
@click.option("--lyrics", default=True, help="Whether the lyrics should be output")
@click.option("--stats", default=False, help="Whether the statistical analysis of the lyrics should be output")
def main(artist, song, clean, lyrics, stats):
    print(get_spotify_song())
    api = genius.Genius(genius_key)
    song_info = api.search_song(song, artist)
    try:
        hasattr(song_info, "lyrics")
        # Todo: Remove [Hook], [Verse 1], etc
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

            lyric_lines = song_info.lyrics.split("\n")
            simile_lines = list()
            if len(lyric_lines) > 0:
                for line in lyric_lines:
                    if "like" in line and line not in simile_lines:
                        simile_lines.append(line)

            print("Similes used in this song:", len(simile_lines))
            click.echo("Lines with similes in them:")
            for simile_num, simile_line in enumerate(simile_lines):
                click.echo("%s. %s" % (simile_num + 1, simile_line))

            click.echo("Words by frequency:")
            word_map_sorted = sorted(word_map.items(), key=lambda kv: kv[1])
            word_map_sorted.reverse()
            word_num = 1
            for word_key, word_frequency in word_map_sorted:
                click.echo("%s). %s - %s" % (word_num, word_key, word_frequency))
                word_num += 1
                if word_num > 10:
                    break

            # Todo: Import syllabic counters
            # Todo: See which lines rhyme with each other

            # click.echo(pronouncing.rhymes("player"))
    except AttributeError:
        return click.echo("No songs found with this info")


if __name__ == "__main__":
    main()
