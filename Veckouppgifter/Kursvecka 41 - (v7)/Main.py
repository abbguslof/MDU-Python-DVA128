import ArtistDatabase

while True:
    for artist in ArtistDatabase.list_artist():
        print(artist)

    ArtistDatabase.get_artist(input('Select Artist > '))
    input('Press Enter to Continue')