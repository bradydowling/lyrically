expletives = ["Fuck", "fuck", "Shit", "shit", "pussy", "bitch"]

# TODO: Make into a module on PYPI called pottytalk


def censor(lyrics):
    cleaned_lyrics = lyrics
    cleaned_lyrics = cleaned_lyrics.replace("Fuck", "F***")
    cleaned_lyrics = cleaned_lyrics.replace("fuck", "f***")
    cleaned_lyrics = cleaned_lyrics.replace("Shit", "S***")
    cleaned_lyrics = cleaned_lyrics.replace("shit", "s***")
    cleaned_lyrics = cleaned_lyrics.replace("pussy", "p****")
    cleaned_lyrics = cleaned_lyrics.replace("Bitch", "B****")
    cleaned_lyrics = cleaned_lyrics.replace("bitch", "b****")
    cleaned_lyrics = cleaned_lyrics.replace("my God", "my gosh")
    cleaned_lyrics = cleaned_lyrics.replace("Oh God", "Oh gosh")
    cleaned_lyrics = cleaned_lyrics.replace("Goddamn", "Gosh dang")
    cleaned_lyrics = cleaned_lyrics.replace("God damn", "Gosh dang")
    cleaned_lyrics = cleaned_lyrics.replace("damn", "dang")
    cleaned_lyrics = cleaned_lyrics.replace("Damn", "Dang")
    cleaned_lyrics = cleaned_lyrics.replace("Ass ", "A** ")
    cleaned_lyrics = cleaned_lyrics.replace("ass ", "a** ")
    return cleaned_lyrics


def count_expletives(lyrics):
    expletives_num = 0
    for word in lyrics.split():
        if word in expletives:
            expletives_num += 1
    return expletives_num
