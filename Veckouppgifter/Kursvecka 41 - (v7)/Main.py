import ArtistDatabase

lineLength = 56

while True:
    print('---')
    print('Artists:')
    for artist in ArtistDatabase.list_artist():
        print(' - '+artist)
    print('---')

    artist = ArtistDatabase.get_artist(input('Select Artist > '))
    if artist is not None:
        print('*' * lineLength + '\n' + (artist['name'].center(lineLength)) + '\n' + '*' * lineLength)
        [print(f"{key}: {', '.join(artist[key.lower().replace(' ', '_')])}") for key in ["Members", "Genres", "Years Active"]]
    else:
        print("Not found")
    input('Press Enter to Continue...\n')