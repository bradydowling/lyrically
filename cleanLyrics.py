def censor(lyrics):
    cleanedLyrics = lyrics.replace("Fuck", "F***")
    cleanedLyrics = cleanedLyrics.replace("fuck", "f***")
    cleanedLyrics = cleanedLyrics.replace("Shit", "S***")
    cleanedLyrics = cleanedLyrics.replace("shit", "s***")
    cleanedLyrics = cleanedLyrics.replace("pussy", "p****")
    return cleanedLyrics