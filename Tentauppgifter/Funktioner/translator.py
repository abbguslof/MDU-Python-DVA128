def translate(text):
    splitText = text.split()
    for x in range(len(splitText)):
        if splitText[x] in words:
            splitText[x] = words[splitText[x]]
    return ' '.join(splitText)

words = {
    'att': 'to',
    'det': 'it',
    'gillar': 'like',
    'jag': 'I',
    'mat': 'food',
    'spela': 'play',
    'tv-spel': 'videogames',
    'roligt': 'fun',
    'är': 'is'
}

while True:
    text = input('text > ')
    print('translation >', translate(text))
    print()