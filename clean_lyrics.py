expletives = ["Fuck", "fuck", "Shit", "shit", "pussy"]

# TODO: Make into a module on PYPI called pottytalk

def censor(lyrics):
    cleaned_lyrics = lyrics.replace("Fuck", "F***")
    cleaned_lyrics = cleaned_lyrics.replace("fuck", "f***")
    cleaned_lyrics = cleaned_lyrics.replace("Shit", "S***")
    cleaned_lyrics = cleaned_lyrics.replace("shit", "s***")
    cleaned_lyrics = cleaned_lyrics.replace("pussy", "p****")
    cleaned_lyrics = cleaned_lyrics.replace("God", "Gosh")
    cleaned_lyrics = cleaned_lyrics.replace("god", "gosh")
    cleaned_lyrics = cleaned_lyrics.replace("damn", "dang")
    cleaned_lyrics = cleaned_lyrics.replace("Damn", "Dang")
    return cleaned_lyrics


def count_expletives(lyrics):
    expletives_num = 0
    for word in lyrics.split():
        if word in expletives:
            expletives_num += 1
    return expletives_num
